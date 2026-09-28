# Change log

## 2026-09-28 — nine capture resources added (R13–R21)

Added resource records, source-register entries (S31–S43), rights, protocol-coverage and release-note rows for nine publicly hosted capture sources: ITI ICS-Security-Tools (R13), Lemay & Fernandez CSET 2016 Modbus (R14), gymgit S7comm captures (R15), EmreEkin ICS-Pcaps (R16), ICS CTF traffic (R17), ControlThings ct-samples (R18), Nozomi tricotools TRITON (R19), University of Coimbra MODBUSTCP#1 (R20) and the UOWM IEC 60870-5-104 IDS dataset (R21). Assessments come from local verification on 2026-09-28: every file was downloaded, checked by magic number, size-matched to the upstream tree or record, and hashed; archives were integrity-tested or MD5-matched to the publisher. Added 780 capture-register entries (C42–C821). The register schema now admits zip, 7z and gzip entries and `check_links.py` recognizes their magic numbers. Rights gates are set per what each source states; five of the nine publish no license and remain permission-required.

## 2026-09-28 — capture download register added

Added `catalog/capture-downloads.json`: 41 direct addresses for the packet captures published by 4SICS (R09, 3 files), S4x15 (R10, 8 files), IEC61850SecurityDataset (R07, 14 files) and the KNX contextual dataset (R08, 16 files). Every address was checked on 2026-09-28 with a ranged HTTP GET of the first 16 bytes; status, total size and the capture magic number were recorded. Observed: four S4x15 files named `.pcap` are pcapng inside. Generated `docs/reference/capture-downloads.md` and `data/exports/capture-downloads.csv`; extended `validate.py` with structural checks for the register; added `scripts/check_links.py` for live revalidation; added four unit tests. No capture file is stored in the repository and no redistribution permission is implied by a working address.

## 2026-09-28 — content and software licensing

Adopted CC BY-SA 4.0 for original educational content and catalog material, and Apache 2.0 for original software, as authorized by the project owner. Added full standard license texts, explicit scope, J0NN3Mac attribution, software NOTICE, author credit, third-party exclusions, directory notices, and contribution terms. Replaced the bootstrap's pending-license guidance.

Licensing does not change the research records, external dataset terms, or frozen matrix files. Added local license-integrity checks; no upstream permissions or dataset validation are implied.

## 2026-09-27 — imported onto review branch

Inspected the live repository `J0NN3Mac/ICS_Compendium` (default branch `main`, one commit, README only, no license file). Created `bootstrap/compendium-foundation` from `main` and merged the prepared package selectively. The original README tagline was preserved as the subtitle; no other existing content was replaced. Local checks (generate, validate, unit tests, generate --check) passed inside the repository before commit. Published as commit `8dc5a3e2051b1dc71888c359a9acdbd629b4332f` on `bootstrap/compendium-foundation` and opened as [pull request #1](https://github.com/J0NN3Mac/ICS_Compendium/pull/1) against `main` on 2026-09-27, pending review. Not merged by the import.

## 2026-09-27 — local bootstrap prepared

Imported the original matrix artifacts without modification. Added canonical resource and source records, supporting tables, user-nominated seed addresses, generated resource cards and exports, proposed contribution/data policies, intake/scenario templates, and local structural tests.

No upstream sources revalidated during packaging. No raw datasets downloaded. No simulator deployed. No permission requested or granted. No remote repository change made.
