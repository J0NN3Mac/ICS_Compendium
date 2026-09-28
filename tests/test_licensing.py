# Copyright (c) 2026 J0NN3Mac and contributors.
# SPDX-License-Identifier: Apache-2.0
# See LICENSES/Apache-2.0.txt and NOTICE in the repository root.
"""Local licensing consistency checks; not an ownership or legal-clearance audit."""
from pathlib import Path
import hashlib
import unittest

ROOT = Path(__file__).resolve().parents[1]
LICENSE_HASHES = {'Apache-2.0.txt': 'cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30', 'CC-BY-SA-4.0.txt': '091d08965bb70d444daccb62c5bcc4345cd4d6a65267da1f06564c95d25d9abb'}


class LicensingTests(unittest.TestCase):
    def test_standard_license_copies_unchanged(self):
        for name, expected in LICENSE_HASHES.items():
            with self.subTest(license=name):
                actual = hashlib.sha256((ROOT / "LICENSES" / name).read_bytes()).hexdigest()
                self.assertEqual(actual, expected)

    def test_scope_and_third_party_exclusions_present(self):
        scope = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
        for phrase in ("CC BY-SA 4.0", "Apache License, Version 2.0", "Third-party materials retain their own licenses", "J0NN3Mac"):
            self.assertIn(phrase, scope)
        self.assertTrue((ROOT / "THIRD_PARTY_NOTICES.md").is_file())
        self.assertIn("do not modify either license", (ROOT / "NOTICE").read_text(encoding="utf-8"))

    def test_directory_notices_present(self):
        for directory in ("scripts", "tests", "docs", "templates", "catalog", "data/exports", "data/snapshots"):
            with self.subTest(directory=directory):
                self.assertTrue((ROOT / directory / "LICENSE.md").is_file())

    def test_original_python_files_have_license_headers(self):
        for directory in ("scripts", "tests"):
            for path in (ROOT / directory).glob("*.py"):
                with self.subTest(file=path.name):
                    header = "\n".join(path.read_text(encoding="utf-8").splitlines()[:5])
                    self.assertIn("SPDX-License-Identifier: Apache-2.0", header)
                    self.assertIn("J0NN3Mac", header)


if __name__ == "__main__":
    unittest.main()
