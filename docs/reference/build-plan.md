# Build Plan

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

## KNX — Contextual protocol analysis

| Field | Recorded content |
| --- | --- |
| Phase | 1 — curate |
| Resources | KNX |
| Track / learning objective | Contextual protocol analysis |
| Participant level | Intermediate |
| Organizer effort | Intermediate |
| Proposed exercise | Decode telegram values and distinguish abnormal commands from their downstream system responses |
| Required inputs / preparation | PCAP/CSV alignment, engineering dictionary, Target semantics, notices, privacy screening and answer key |
| Release gate | Confirm link type; retain MIT notice; document reconstructed chronology |

Sources: [source 1](https://github.com/vgraveto/knx-datasets), [source 2](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/LICENSE)

## 4SICS — Asset discovery and mixed-traffic triage

| Field | Recorded content |
| --- | --- |
| Phase | 1 — curate |
| Resources | 4SICS |
| Track / learning objective | Asset discovery and mixed-traffic triage |
| Participant level | Beginner–intermediate |
| Organizer effort | Intermediate |
| Proposed exercise | Build an asset inventory from a short trace and identify evidence of unusual communication |
| Required inputs / preparation | Decode protocol inventory; select coherent excerpt; document capture vantage; author labels; preserve credit |
| Release gate | Do not call the complete conference trace benign; meet host attribution statement |

Sources: [source 1](https://www.netresec.com/?page=PCAP4SICS)

## GRFICSv3 — Integrated packet / process causality

| Field | Recorded content |
| --- | --- |
| Phase | 1 — build |
| Resources | GRFICSv3 |
| Track / learning objective | Integrated packet / process causality |
| Participant level | Intermediate |
| Organizer effort | Advanced |
| Proposed exercise | Explain a simulated setpoint change using a request, controller state, evolving process values and an alarm |
| Required inputs / preparation | Pinned simulator, isolated network, controller logic, tag map, process-state export, PCAP and synchronized event oracle |
| Release gate | Functional and realism validation; own-output rights review; no connection to real OT |

Sources: [source 1](https://github.com/Fortiphyd/GRFICSv3), [source 2](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/plc/mbconfig.cfg), [source 3](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/docker-compose.yml), [source 4](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/LICENSE)

## OpenPLC v4 — Controller and protocol developer track

| Field | Recorded content |
| --- | --- |
| Phase | 2 — build |
| Resources | OpenPLC v4 |
| Track / learning objective | Controller and protocol developer track |
| Participant level | Intermediate |
| Organizer effort | Advanced |
| Proposed exercise | Build a read-only client / telemetry exporter and verify command-versus-measurement distinctions |
| Required inputs / preparation | Pinned runtime/plugin, supplied process model, client, tag map and integration tests |
| Release gate | Validate actual selected plugin behavior; separate component and captured-output licenses |

Sources: [source 1](https://github.com/Autonomy-Logic/openplc-runtime), [source 2](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf), [source 3](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/LICENSE)

## Conpot — Service discovery and protocol parsers

| Field | Recorded content |
| --- | --- |
| Phase | 2 — build |
| Resources | Conpot |
| Track / learning objective | Service discovery and protocol parsers |
| Participant level | Beginner–intermediate |
| Organizer effort | Intermediate |
| Proposed exercise | Classify industrial endpoint services and compare service emulation with a real process-backed device |
| Required inputs / preparation | Chosen templates, authorized client interactions, local capture, emulator-fidelity notes |
| Release gate | Do not present a honeypot as a physically coherent plant |

Sources: [source 1](https://github.com/mushorg/conpot), [source 2](https://conpot.readthedocs.io/en/latest/), [source 3](https://raw.githubusercontent.com/mushorg/conpot/main/LICENSE.txt)

## HAI / HAIEnd — Time-series anomaly detection

| Field | Recorded content |
| --- | --- |
| Phase | 2 — conditional |
| Resources | HAI / HAIEnd |
| Track / learning objective | Time-series anomaly detection |
| Participant level | Intermediate–advanced |
| Organizer effort | Intermediate |
| Proposed exercise | Detect an event and explain which coupled variables changed before and after the labeled interval |
| Required inputs / preparation | One release, explicit train/test time boundaries, hidden test labels, event-aware scoring and signal dictionary |
| Release gate | Resolve conflicting license notices; do not add invented packets or random-row train/test leakage |

Sources: [source 1](https://github.com/icsdataset/hai)

## SWaT A6 — Industrial incident reconstruction

| Field | Recorded content |
| --- | --- |
| Phase | 2 — conditional |
| Resources | SWaT A6 |
| Track / learning objective | Industrial incident reconstruction |
| Participant level | Intermediate–advanced |
| Organizer effort | Intermediate–advanced |
| Proposed exercise | Correlate an authorized excerpt of packet activity with historian behavior and documented incident times |
| Required inputs / preparation | Written team/event permission, exact release files, capture-point/timebase check, tag dictionary and answer key |
| Release gate | No private/public onward sharing without authorization |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 2](https://www.sutd.edu.sg/itrust/swat/), [source 3](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

## WADI A3 / joint December 2023 — Normal baselines and coupled plants

| Field | Recorded content |
| --- | --- |
| Phase | 3 — conditional |
| Resources | WADI A3 / joint December 2023 |
| Track / learning objective | Normal baselines and coupled plants |
| Participant level | Advanced |
| Organizer effort | Advanced |
| Proposed exercise | Model normal process/network relationships between treatment and distribution |
| Required inputs / preparation | Permission, selected synchronized subset, storage plan, timing checks and known sensor-quality caveats |
| Release gate | No attack labels for this release; never attach A1 attack events to A3 packets |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/), [source 3](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

## IEC61850SecurityDataset — Electrical protection / disturbance triage

| Field | Recorded content |
| --- | --- |
| Phase | 3 — conditional |
| Resources | IEC61850SecurityDataset |
| Track / learning objective | Electrical protection / disturbance triage |
| Participant level | Intermediate–advanced |
| Organizer effort | Intermediate |
| Proposed exercise | Distinguish a legitimate electrical disturbance from inconsistent GOOSE state/event behavior |
| Required inputs / preparation | Owner permission, substation diagram, IED configuration, frame/time annotations and separate truth-status fields |
| Release gate | Do not claim attack CSV proves physical attack effects |

Sources: [source 1](https://github.com/smartgridadsc/IEC61850SecurityDataset)

## S4x15 — Historical multi-host CTF reconstruction

| Field | Recorded content |
| --- | --- |
| Phase | 3 — conditional |
| Resources | S4x15 |
| Track / learning objective | Historical multi-host CTF reconstruction |
| Participant level | Intermediate |
| Organizer effort | Intermediate–advanced |
| Proposed exercise | Reconstruct relationships among controller, HMI and workstation captures |
| Required inputs / preparation | Owner rights clarification, cross-file timestamp/deduplication checks and instructor-curated event key |
| Release gate | Hosting permission is not automatically downstream redistribution permission |

Sources: [source 1](https://www.netresec.com/?page=DigitalBond_S4)

## NIST + MITRE — Architecture, evidence and scenario vocabulary

| Field | Recorded content |
| --- | --- |
| Phase | All phases |
| Resources | NIST + MITRE |
| Track / learning objective | Architecture, evidence and scenario vocabulary |
| Participant level | Foundational–advanced |
| Organizer effort | Low–intermediate |
| Proposed exercise | Explain the operational impact and attach supported technique mappings to evidence |
| Required inputs / preparation | Revision 3 baseline, clearly labeled draft notes, pinned ATT&CK collection, notices and scoring rubric |
| Release gate | A technique mapping is not a proof that an event occurred |

Sources: [source 1](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [source 2](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd), [source 3](https://attack.mitre.org/matrices/ics/), [source 4](https://github.com/mitre-attack/attack-stix-data), [source 5](https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/LICENSE.txt)

