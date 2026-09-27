# Data intake and publication policy — proposed baseline

This scaffold is **metadata-only by default**. All research statements, permissions and experimental results must retain their provenance and scope.

## Separate four decisions

| Decision | Evidence to record |
| --- | --- |
| Catalog a resource | Original source, owner, exact release and review status |
| Obtain a local research copy | Access process, storage location and permitted users |
| Use it in an internal company event | Event-specific clearance and participant access model |
| Publish or redistribute it | Reviewed grant, notices, scope and approved distribution path |

An entry in this catalog does not mark any later decision complete. Keep permission records separate from public metadata, and exclude personal requester details.

## Intake evidence

Record source addresses, commit/release identity, file hashes, capture dates and vantage, clock alignment, payload completeness, device/tag definitions, label semantics, physical-truth provenance and known limitations. Distinguish documented protocol capability from decoded traffic. Retain original labels alongside normalized labels.

## Default exclusions

Do not commit raw packet captures, access-restricted datasets, third-party archives/images, credentials, private permission correspondence, production network inventories or answer keys for unreleased scored events. Keep raw local working files outside the tracked tree. The validator rejects several common capture/image/archive extensions as an accidental-inclusion guard; it is not a comprehensive privacy or security audit.

## Publication gate

A maintainer must review permission scope, data sensitivity, notices, reproducibility, label quality, capture integrity and participant usability before approving an event artifact. Any future change from metadata-only storage must be explicit, reviewed and accompanied by an artifact manifest.

## Research boundaries

Use offline analysis and authorized isolated environments. Do not connect simulator control interfaces or replay historical traffic onto production control networks. Treat software from external sources as untrusted until reviewed.
