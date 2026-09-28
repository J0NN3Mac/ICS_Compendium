#!/usr/bin/env python3
# Copyright (c) 2026 J0NN3Mac and contributors.
# SPDX-License-Identifier: Apache-2.0
# See LICENSES/Apache-2.0.txt and NOTICE in the repository root.
"""Revalidate the capture download register with live HTTP checks.

Fetches only the first 16 bytes of each address (HTTP Range), then compares status, total size
and the capture or archive magic number against catalog/capture-downloads.json. Nothing is written unless
--update is given, in which case size, format, status and the checked date are refreshed for
addresses that verified. Failures are reported and leave the record untouched.

Requires outbound network access. This is the only script in the repository that uses it.
"""
from __future__ import annotations
import argparse
import datetime
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog' / 'capture-downloads.json'
MAGIC = {
    b'\xd4\xc3\xb2\xa1': 'pcap', b'\xa1\xb2\xc3\xd4': 'pcap',
    b'\x4d\x3c\xb2\xa1': 'pcap', b'\xa1\xb2\x3c\x4d': 'pcap',
    b'\x0a\x0d\x0d\x0a': 'pcapng',
    b'\x50\x4b\x03\x04': 'zip', b'\x37\x7a\xbc\xaf': '7z',
}
GZIP = b'\x1f\x8b'

def probe(url: str, timeout: float) -> dict:
    req = urllib.request.Request(url, headers={'Range': 'bytes=0-15', 'User-Agent': 'ICS-Compendium-link-check'})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        head = resp.read(16)
        status = resp.status
        content_range = resp.headers.get('Content-Range', '')
        total = content_range.rsplit('/', 1)[-1] if '/' in content_range else resp.headers.get('Content-Length', '')
    return {'http_status': status, 'size_bytes': int(total) if total.isdigit() else None,
            'detected_format': MAGIC.get(head[:4]) or ('gzip' if head[:2] == GZIP else None), 'content_type': None}

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--update', action='store_true', help='write verified results back to the catalog')
    ap.add_argument('--timeout', type=float, default=30.0)
    ap.add_argument('--only', help='restrict to one resource ID, e.g. R09')
    args = ap.parse_args()
    data = json.loads(CATALOG.read_text(encoding='utf-8'))
    today = datetime.date.today().isoformat()
    failures = 0
    for c in data['captures']:
        if args.only and c['resource_id'] != args.only:
            continue
        try:
            r = probe(c['download_url'], args.timeout)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            failures += 1
            print(f"FAIL {c['capture_id']} {c['file']}: {exc}")
            continue
        problems = []
        if r['http_status'] not in (200, 206): problems.append(f"status {r['http_status']}")
        if r['detected_format'] is None: problems.append('no capture magic number')
        elif r['detected_format'] != c['detected_format']: problems.append(f"format {r['detected_format']} != {c['detected_format']}")
        if r['size_bytes'] != c['size_bytes']: problems.append(f"size {r['size_bytes']} != {c['size_bytes']}")
        if problems:
            failures += 1
            print(f"FAIL {c['capture_id']} {c['file']}: {'; '.join(problems)}")
            continue
        print(f"OK   {c['capture_id']} {c['file']} ({r['size_bytes']:,} bytes, {r['detected_format']})")
        if args.update:
            c['checked'] = today
    if args.update:
        CATALOG.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('Catalog updated; run scripts/generate.py to refresh views.')
    checked = len([c for c in data['captures'] if not args.only or c['resource_id'] == args.only])
    print(f"{checked - failures} of {checked} addresses verified.")
    return 1 if failures else 0

if __name__ == '__main__':
    raise SystemExit(main())
