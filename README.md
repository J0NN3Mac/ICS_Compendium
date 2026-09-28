# ICS_Compendium

*A Robust Collection of ICS Resources to Build a Solid Knowledge Foundation*

A curated resource for **Industrial Control System (ICS)** and **Supervisory Control and Data Acquisition (SCADA)** awareness, **Operational Technology (OT)** communications, and developer build-a-thons.

**Designated repository:** [J0NN3Mac/ICS_Compendium](https://github.com/J0NN3Mac/ICS_Compendium).

> **Bootstrap status: imported for review.** This foundation was prepared locally on September 27, 2026 and merged onto the `bootstrap/compendium-foundation` branch the same day. The repository held only its initial README at import time; that tagline is retained above. Research entries are inherited from the dated workbook, not newly revalidated here. See [CHANGELOG.md](CHANGELOG.md) and [IMPORT.md](IMPORT.md) for the import record.

## Start here

| Need | Entry point |
| --- | --- |
| Compare the 12 resource families | [Master matrix](docs/master-matrix.md) |
| Read every assessment field | [Resource cards](docs/resources/README.md) |
| Check protocols and the strength of the evidence | [Protocol coverage](docs/reference/protocol-coverage.md) |
| Review access and redistribution gates | [Rights and access](docs/reference/rights-and-access.md) |
| Avoid edition and label mistakes | [Release notes](docs/reference/release-notes.md) |
| Build exercises | [Build plan](docs/reference/build-plan.md) and [scenario template](templates/scenario.md) |
| Prioritize missing coverage | [Gap register](docs/reference/gap-register.md) and [roadmap](docs/roadmap.md) |
| Locate original research | [Primary sources](docs/reference/sources.md) and [user-nominated seeds](docs/reference/seed-sources.md) |
| Understand terms | [Glossary](docs/reference/glossary.md) |
| Import this package | [Import guide](IMPORT.md) |

## What is included

Twelve resource families: **seven dataset/capture collections, three scenario-generation platforms, and two reference frameworks**. The catalog preserves all 25 original comparison fields, 30 primary-source records, ten user-nominated seed sources, twelve gaps, release-specific warnings, and proposed exercise tracks.

This is a **metadata and training-design collection**, not a mirror of third-party datasets. No third-party packet captures, restricted time series, virtual-machine images, or malware files are bundled. Availability, protocol evidence, process truth, and redistribution clearance remain separate questions.

## Source of truth

Edit the JavaScript Object Notation (JSON) records in `catalog/`. Resource identifiers `R01` through `R12` and source identifiers `S01` through `S30` remain stable. Supporting tables retain the workbook's field names.

Markdown pages and comma-separated values (CSV) exports are generated views. The original Excel workbook and CSV in [data/snapshots](data/snapshots/README.md) are frozen historical inputs; they are **not** silently updated when the live catalog changes.

```sh
python3 scripts/generate.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

The scripts use the Python standard library and do not access the network, download data, run simulators, or modify GitHub. Validation checks structure and local consistency, not the factual accuracy of upstream claims.

## Contribution and publication rules

Read [CONTRIBUTING.md](CONTRIBUTING.md), [the data policy](DATA_POLICY.md), and [licensing and rights review](LICENSING.md). Keep uncertain fields explicit. Do not mark an event package cleared, a simulator operational, or a protocol observed without corresponding evidence.

Analysis and replay are intended for offline inspection or isolated, authorized training environments—not production control networks.

## License and credit

Copyright (c) 2026 **J0NN3Mac and contributors**.

Original educational content and catalog material are licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. Original software utilities and tests are licensed under **Apache License 2.0**. These are separate scopes, not interchangeable choices for every file.

See [LICENSE.md](LICENSE.md) for exact scope and an attribution example, [AUTHORS.md](AUTHORS.md) for credit, [NOTICE](NOTICE) for software notices, and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for exclusions. External resources retain their own licenses and access restrictions. The project licenses do not clear third-party datasets for redistribution.
