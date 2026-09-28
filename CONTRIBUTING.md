# Contributing

## Work from the canonical records

Edit `catalog/resources.json`, `catalog/sources.json`, `catalog/supporting-tables.json` or `catalog/seed-sources.json`. Do not hand-edit generated resource cards or table exports. Keep frozen snapshots unchanged.

Use a review branch and pull request. Preserve stable resource/source identifiers. Allocate a new identifier rather than reusing one for a different resource. The import manifest records the initial baseline; it need not list every future addition.

## Evidence standard

Write each acronym in full on first use. Distinguish source-supported statements from author assessments. Record exact releases and supporting source identifiers. Review dates mean documentation review only unless packet inspection, runtime tests or permissions are separately evidenced. Never transform an unknown field into a yes/no assumption for visual completeness.

For a new resource, use [the intake template](templates/resource-intake.md). Add a source record and use its source identifier in the resource. An intake record is not event-ready merely because it has a download link.

## Quality checks

```sh
python3 scripts/generate.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

These checks do not prove upstream facts, privacy clearance, packet fidelity or licensing. Include those review results in the pull-request narrative, with evidence and remaining uncertainty.

## Changes to original workbook fields

The `matrix_fields` object preserves the 25-column baseline. Make intentional semantic changes there, keep resource/category identifiers consistent, and explain any changed review scope. Rebuild derived views. Keep original wording visible in the archived research snapshot; do not replace the original snapshot to disguise a correction.

## Rights and contribution terms

By intentionally submitting an original contribution for inclusion, you offer it under the applicable license in [LICENSE.md](LICENSE.md): CC BY-SA 4.0 for educational content and catalog material, or Apache 2.0 for software. You retain ownership of your contribution; no copyright assignment is required.

Submit only work you own or are authorized to license, including any required employer approval. Identify third-party material, its provenance, governing terms, and modifications rather than representing it as original work. Preserve applicable credits and update [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for any permitted inclusion.

Do not modify the standard legal texts to add attribution, noncommercial, or other conditions. Place project-specific notices outside them. A new raw or generated dataset still requires the artifact-level review in [DATA_POLICY.md](DATA_POLICY.md).
