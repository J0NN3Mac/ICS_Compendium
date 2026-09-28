#!/usr/bin/env python3
"""Generate Markdown and CSV views from the catalog; no network or GitHub access."""
from __future__ import annotations
import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLE_NAMES = {
    'Protocol Coverage': 'protocol-coverage', 'Rights & Access': 'rights-and-access',
    'Release Notes': 'release-notes', 'Build Plan': 'build-plan',
    'Gap Register': 'gap-register', 'Glossary': 'glossary',
}

def load(root: Path, name: str):
    return json.loads((root / 'catalog' / name).read_text(encoding='utf-8'))

def cell(value) -> str:
    return str(value if value is not None else '').replace('|', '\\|').replace('\r\n', '\n').replace('\n', '<br>')

def table(rows: list[dict]) -> str:
    if not rows:
        return '_No entries._\n'
    keys = list(rows[0])
    lines = ['| ' + ' | '.join(cell(k) for k in keys) + ' |', '| ' + ' | '.join('---' for _ in keys) + ' |']
    lines += ['| ' + ' | '.join(cell(row.get(k, '')) for k in keys) + ' |' for row in rows]
    return '\n'.join(lines) + '\n'

def csv_text(rows: list[dict]) -> str:
    out = io.StringIO(newline='')
    if rows:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    return out.getvalue()

def source_links(ids: list[str], prefix: str = '../reference/sources.md') -> str:
    return ', '.join(f'[{i}]({prefix}#{i.lower()})' for i in ids)

def outputs(root: Path) -> dict[str, str]:
    resources = load(root, 'resources.json')['resources']
    sources = load(root, 'sources.json')['sources']
    tables = load(root, 'supporting-tables.json')['tables']
    seeds = load(root, 'seed-sources.json')['sources']
    manifest = load(root, 'import-manifest.json')
    date = manifest['import_date']
    generated = '> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.\n\n'
    boundary = (f'Baseline imported from the {date} research workbook. Review dates and source statements '
                'are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, '
                'or grant redistribution permission.\n\n')
    result: dict[str, str] = {}
    index_rows=[]
    for r in resources:
        f=r['matrix_fields']
        index_rows.append({'ID':r['resource_id'], 'Resource':f"[{f['Resource / scope']}](resources/{r['slug']}.md)",
                          'Category':f['Category'], 'Sector / process':f['Sector / process'],
                          'Redistribution gate':f['Redistribution gate'], 'Adoption action':f['Adoption action']})
        text=f"# {f['Resource / scope']}\n\n"+generated+boundary
        text+=f"**Identifier:** {r['resource_id']}  \n**Record type:** {f['Category']}  \n**Review status:** {r['review']['status']}  \n**Inherited review date:** {r['review']['inherited_review_date']}\n\n"
        text+='[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)\n\n'
        text+='## Assessment fields\n\n'
        fields=[{'Field':k,'Recorded assessment':v} for k,v in f.items() if k not in {'ID','Resource / scope','Primary sources','Rights sources','Verified'}]
        text+=table(fields)+'\n## Sources and provenance\n\n'
        text+=source_links(r['source_ids'])+'\n\n'
        text+='### Recorded primary addresses\n\n'
        for i,u in enumerate(f['Primary sources'].splitlines(),1): text+=f'- [Primary source {i}]({u})\n'
        text+='\n### Recorded rights addresses\n\n'
        for i,u in enumerate(f['Rights sources'].splitlines(),1): text+=f'- [Rights source {i}]({u})\n'
        text+='\nThese references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.\n'
        result[f"docs/resources/{r['slug']}.md"]=text
    result['docs/master-matrix.md']='# Master resource matrix\n\n'+generated+boundary+table(index_rows)+'\nOpen a resource card for all original comparison fields. [CSV export](../data/exports/master-matrix.csv) · [Frozen Excel workbook](../data/snapshots/SCADA_Master_Dataset_Matrix_2026-09-27.xlsx)\n'
    resource_index=[{'ID':r['resource_id'],'Resource':f"[{r['matrix_fields']['Resource / scope']}]({r['slug']}.md)",'Category':r['matrix_fields']['Category']} for r in resources]
    result['docs/resources/README.md']='# Resource cards\n\n'+generated+boundary+table(resource_index)
    result['data/exports/master-matrix.csv']=csv_text([r['matrix_fields'] for r in resources])
    result['data/exports/sources.csv']=csv_text(sources)
    result['data/exports/seed-sources.csv']=csv_text(seeds)
    for name,slug in TABLE_NAMES.items():
        rows=tables[name]
        text=f'# {name}\n\n'+generated+boundary
        if name=='Protocol Coverage':
            text+='Evidence codes are defined in [the glossary](glossary.md). No cell is a claim of newly decoded traffic.\n\n'
            compact=[{k:v for k,v in row.items() if k not in {'Interpretation','Sources'}} for row in rows]
            text+=table(compact)
            text+='\n## Interpretation by resource\n\n'
            for row in rows:
                text+=f"### {row['ID']} — {row['Resource']}\n\n{row['Interpretation']}\n\n"
                text+='Sources: '+', '.join(f'[source {i}]({u})' for i,u in enumerate(row['Sources'].splitlines(),1))+'\n\n'
        elif name=='Glossary':
            text+=table(rows)
        else:
            for i,row in enumerate(rows,1):
                if name=='Rights & Access': title=f"{row['ID']} — {row['Resource']}"
                elif name=='Release Notes': title=f"{row['Resource']} — {row['Release / edition']}"
                elif name=='Build Plan': title=f"{row['Resources']} — {row['Track / learning objective']}"
                else: title=f"{row['Gap ID']} — {row['Gap within selected corpus']}"
                text+=f'## {title}\n\n'
                source_keys={k for k in row if k in {'Sources','Sources / rationale'}}
                text+=table([{'Field':k,'Recorded content':v} for k,v in row.items() if k not in source_keys])+'\n'
                for key in source_keys:
                    text+='Sources: '+', '.join(f'[source {n}]({u})' for n,u in enumerate(str(row[key]).splitlines(),1))+'\n\n'
        result[f'docs/reference/{slug}.md']=text
        result[f'data/exports/{slug}.csv']=csv_text(rows)
    text='# Primary-source register\n\n'+generated+boundary
    for row in sources:
        text+=f"## {row['Source ID']}\n\n**Resource:** {row['Resource']}  \n**Source type:** {row['Source type']}  \n**Inherited review date:** {row['Verified']}\n\n"
        text+=f"[Open original source]({row['Primary URL']})\n\n{row['Supports / limitations']}\n\n"
    result['docs/reference/sources.md']=text
    text='# User-nominated seed sources\n\n'+generated+'These ten starting addresses were supplied by the project owner. They are retained for discovery and future review, separate from the workbook\'s primary-source register. They were not revalidated during this import; proposed roles and the scope warning are inherited context, not a new audit.\n\n'
    for row in seeds:
        text+=f"## {row['seed_id']} — {row['title']}\n\n[Open source]({row['url']})\n\n**Proposed role:** {row['proposed_role']}  \n**Status:** {row['status']}\n\n"
    result['docs/reference/seed-sources.md']=text
    return result

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if a generated view is missing or stale.')
    args=parser.parse_args()
    try:
        desired=outputs(ROOT)
        stale=[]
        for rel,text in desired.items():
            p=ROOT/rel
            if args.check:
                if not p.is_file() or p.read_text(encoding='utf-8')!=text:stale.append(rel)
            else:
                p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8')
        if stale:
            print('Missing or stale generated views:\n'+'\n'.join(stale));return 1
        print(f"{'Checked' if args.check else 'Generated'} {len(desired)} views.")
        return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(f'Generation failed: {exc}');return 1

if __name__=='__main__':raise SystemExit(main())
