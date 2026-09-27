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
