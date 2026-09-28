# Copyright (c) 2026 J0NN3Mac and contributors.
# SPDX-License-Identifier: Apache-2.0
# See LICENSES/Apache-2.0.txt and NOTICE in the repository root.
"""Regression tests for local structural safeguards, not upstream factual verification."""
from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import validate
from generate import outputs

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)/'repository'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','.git','.venv'))
    def tearDown(self):self.tmp.cleanup()
    def alter(self,fn):
        p=self.root/'catalog/resources.json'
        data=json.loads(p.read_text(encoding='utf-8'));fn(data)
        p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    def test_baseline_validates(self):self.assertEqual(validate(self.root),[])
    def test_generated_views_are_current(self):
        for rel,text in outputs(self.root).items():
            self.assertEqual((self.root/rel).read_text(encoding='utf-8'),text,rel)
    def test_duplicate_resource_id_rejected(self):
        self.alter(lambda d:d['resources'].append(d['resources'][0]))
        self.assertTrue(any('Duplicate resource IDs' in e for e in validate(self.root)))
    def test_unknown_source_rejected(self):
        self.alter(lambda d:d['resources'][0]['source_ids'].append('S9999'))
        self.assertTrue(any('unknown source' in e for e in validate(self.root)))
    def test_missing_field_rejected(self):
        self.alter(lambda d:d['resources'][0]['matrix_fields'].pop('PCAP availability'))
        self.assertTrue(any('matrix fields' in e for e in validate(self.root)))
    def test_raw_capture_rejected(self):
        (self.root/'unapproved.pcap').write_bytes(b'not a real capture')
        self.assertTrue(any('forbidden binary/archive' in e for e in validate(self.root)))
    def test_snapshot_change_rejected(self):
        p=self.root/'data/snapshots/SCADA_Master_Dataset_Matrix_2026-09-27.csv'
        p.write_bytes(p.read_bytes()+b'\n')
        self.assertTrue(any('integrity mismatch' in e for e in validate(self.root)))
    def alter_captures(self,fn):
        p=self.root/'catalog/capture-downloads.json'
        data=json.loads(p.read_text(encoding='utf-8'));fn(data)
        p.write_text(json.dumps(data,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
    def test_capture_unknown_resource_rejected(self):
        self.alter_captures(lambda d:d['captures'][0].__setitem__('resource_id','R99'))
        self.assertTrue(any('unknown resource' in e for e in validate(self.root)))
    def test_capture_bad_format_rejected(self):
        self.alter_captures(lambda d:d['captures'][0].__setitem__('detected_format','html'))
        self.assertTrue(any('detected_format' in e for e in validate(self.root)))
    def test_capture_duplicate_url_rejected(self):
        self.alter_captures(lambda d:d['captures'].append(dict(d['captures'][0],capture_id='C99')))
        self.assertTrue(any('Duplicate capture download URLs' in e for e in validate(self.root)))
    def test_capture_failed_status_rejected(self):
        self.alter_captures(lambda d:d['captures'][0].__setitem__('http_status',404))
        self.assertTrue(any('not a success' in e for e in validate(self.root)))
    def test_broken_local_link_rejected(self):
        (self.root/'bad.md').write_text('[missing](does-not-exist.md)',encoding='utf-8')
        self.assertTrue(any('broken local link' in e for e in validate(self.root)))

if __name__=='__main__':unittest.main()
