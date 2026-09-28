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
    def test_broken_local_link_rejected(self):
        (self.root/'bad.md').write_text('[missing](does-not-exist.md)',encoding='utf-8')
        self.assertTrue(any('broken local link' in e for e in validate(self.root)))

if __name__=='__main__':unittest.main()
