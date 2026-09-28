#!/usr/bin/env python3
"""Validate local catalog structure, references, snapshots and accidental binary inclusion."""
from __future__ import annotations
import csv
import datetime
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
FORBIDDEN={'.pcap','.pcapng','.cap','.har','.vmdk','.vdi','.qcow2','.ova','.iso','.zip','.7z','.tar','.tgz','.gz'}
SKIP_DIRS={'.git','.venv','__pycache__'}

def validate(root: Path) -> list[str]:
    errors=[]
    def read(name):return json.loads((root/'catalog'/name).read_text(encoding='utf-8'))
    try:
        resources=read('resources.json')['resources']
        sources=read('sources.json')['sources']
        seeds=read('seed-sources.json')['sources']
        tables=read('supporting-tables.json')['tables']
        manifest=read('import-manifest.json')
    except (OSError,ValueError,KeyError,TypeError) as exc:
        return [f'Cannot load catalog: {exc}']
    def date_ok(value,context):
        try:datetime.date.fromisoformat(value)
        except (TypeError,ValueError):errors.append(f'{context}: invalid ISO date {value!r}')
    def url_ok(value,context):
        try:
            parsed=urlsplit(value)
            if parsed.scheme not in {'http','https'} or not parsed.netloc or re.search(r'\s',value):raise ValueError()
        except (TypeError,ValueError):errors.append(f'{context}: invalid source URL {value!r}')
    source_ids=[]; resource_ids=[]; seed_ids=[]; slugs=[]
    for s in sources:
        sid=s.get('Source ID','');source_ids.append(sid)
        for key in ['Source ID','Resource','Source type','Primary URL','Supports / limitations','Verified']:
            if not s.get(key):errors.append(f'Source {sid}: missing {key}')
        if not re.fullmatch(r'S\d{2,}',sid):errors.append(f'Invalid source ID: {sid}')
        url_ok(s.get('Primary URL'),sid);date_ok(s.get('Verified'),sid)
    try:
        with (root/'data/snapshots/SCADA_Master_Dataset_Matrix_2026-09-27.csv').open(encoding='utf-8-sig',newline='') as f:
            headers=csv.DictReader(f).fieldnames or []
    except OSError as exc:return errors+[f'Cannot read baseline fields: {exc}']
    categories={'generator':'Generator','dataset_capture':'Dataset / capture','framework':'Framework'}
    for r in resources:
        rid=r.get('resource_id','');resource_ids.append(rid)
        slug=r.get('slug','');slugs.append(slug)
        if not re.fullmatch(r'R\d{2,}',rid):errors.append(f'Invalid resource ID: {rid}')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug):errors.append(f'{rid}: invalid slug')
        fields=r.get('matrix_fields',{})
        if set(fields)!=set(headers):errors.append(f'{rid}: matrix fields do not match the 25-column baseline')
        if any(v is None or v=='' for v in fields.values()):errors.append(f'{rid}: blank matrix field; state uncertainty explicitly')
        if fields.get('ID')!=rid:errors.append(f'{rid}: matrix ID mismatch')
        if categories.get(r.get('category'))!=fields.get('Category'):errors.append(f'{rid}: category mismatch')
        date_ok(fields.get('Verified'),rid)
        review=r.get('review',{})
        if not review.get('status'):errors.append(f'{rid}: missing review status')
        for key in ['inherited_review_date','import_date']:date_ok(review.get(key),f'{rid}/{key}')
        ids=r.get('source_ids',[])
        if not ids:errors.append(f'{rid}: no source references')
        for sid in ids:
            if sid not in source_ids:errors.append(f'{rid}: unknown source {sid}')
        url_to_id={s.get('Primary URL'):s.get('Source ID') for s in sources}
        for field in ['Primary sources','Rights sources']:
            for u in str(fields.get(field,'')).splitlines():
                url_ok(u,f'{rid}/{field}')
                if u not in url_to_id:errors.append(f'{rid}: URL absent from source register: {u}')
                elif url_to_id[u] not in ids:errors.append(f'{rid}: source identifier missing for {u}')
    for s in seeds:
        sid=s.get('seed_id','');seed_ids.append(sid)
        if not re.fullmatch(r'SEED\d{2,}',sid):errors.append(f'Invalid seed ID: {sid}')
        url_ok(s.get('url'),sid)
        if not s.get('status'):errors.append(f'{sid}: missing status')
    for label,values in [('source IDs',source_ids),('resource IDs',resource_ids),('seed IDs',seed_ids),('slugs',slugs)]:
        if len(values)!=len(set(values)):errors.append(f'Duplicate {label}')
    for key,values in [('expected_resource_ids',resource_ids),('expected_source_ids',source_ids),('expected_seed_ids',seed_ids)]:
        missing=set(manifest.get(key,[]))-set(values)
        if missing:errors.append(f'Baseline identities missing ({key}): {sorted(missing)}')
    expected_tables={'Protocol Coverage','Rights & Access','Release Notes','Build Plan','Gap Register','Glossary'}
    if set(tables)!=expected_tables:errors.append('Supporting table set mismatch')
    for name,rows in tables.items():
        if not rows:errors.append(f'{name}: empty table')
        elif any(set(row)!=set(rows[0]) for row in rows):errors.append(f'{name}: inconsistent columns')
        if name in {'Protocol Coverage','Rights & Access'}:
            for row in rows:
                if row.get('ID') not in resource_ids:errors.append(f'{name}: unknown resource {row.get("ID")}')
    for entry in manifest.get('snapshot_files',[]):
        path=(root/entry['path']).resolve()
        if not path.is_relative_to(root.resolve()):errors.append('Snapshot path escapes repository');continue
        if not path.is_file():errors.append(f'Missing snapshot: {entry["path"]}');continue
        raw=path.read_bytes()
        if len(raw)!=entry['size_bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:
            errors.append(f'Snapshot integrity mismatch: {entry["path"]}')
    for p in root.rglob('*'):
        rel=p.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):continue
        if p.is_symlink():errors.append(f'Symlink requires manual review: {rel}');continue
        if not p.is_file():continue
        if p.suffix.lower() in FORBIDDEN:errors.append(f'Metadata-only policy: forbidden binary/archive {rel}')
        if p.suffix.lower()=='.md':
            text=p.read_text(encoding='utf-8')
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
                target=target.strip().split(' "',1)[0]
                if not target or target.startswith(('#','http://','https://','mailto:')):continue
                target=unquote(target.split('#',1)[0])
                dest=(p.parent/target).resolve()
                if not dest.is_relative_to(root.resolve()):errors.append(f'{rel}: link outside repository: {target}')
                elif not dest.exists():errors.append(f'{rel}: broken local link: {target}')
    return errors

def main() -> int:
    try:errors=validate(ROOT)
    except (OSError,ValueError,KeyError,TypeError) as exc:errors=[f'Validation failed: {exc}']
    if errors:
        print('\n'.join(errors));return 1
    print('PASS: catalog fields, IDs, source references, dates, snapshot hashes, local links and metadata-only checks.');return 0

if __name__=='__main__':raise SystemExit(main())
