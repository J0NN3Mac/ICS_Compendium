# Release Notes

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

## GRFICSv3 — Current default branch, not commit-pinned

| Field | Recorded content |
| --- | --- |
| Resource | GRFICSv3 |
| Release / edition | Current default branch, not commit-pinned |
| Data / event content | Containerized chemical-process environment |
| PCAP status | Generate |
| Critical handling note | Bundled PLC is not automatically standalone OpenPLC v4. Configured 100 ms polling is not a measured capture property |
| Freeze recommendation | Pin repository commit, image digests, controller logic, seed and capture vantage |

Sources: [source 1](https://github.com/Fortiphyd/GRFICSv3), [source 2](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/plc/mbconfig.cfg), [source 3](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/docker-compose.yml)

## OpenPLC — Standalone runtime v4

| Field | Recorded content |
| --- | --- |
| Resource | OpenPLC |
| Release / edition | Standalone runtime v4 |
| Data / event content | Headless runtime; plugin-oriented protocol support |
| PCAP status | Generate |
| Critical handling note | Version 4 has a different architecture and MIT runtime license; legacy docs may refer to another runtime |
| Freeze recommendation | Record runtime, editor and plugin versions separately |

Sources: [source 1](https://github.com/Autonomy-Logic/openplc-runtime), [source 2](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf), [source 3](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/LICENSE)

## SWaT — A1 / A2: December 2015 collection and normal-file update

| Field | Recorded content |
| --- | --- |
| Resource | SWaT |
| Release / edition | A1 / A2: December 2015 collection and normal-file update |
| Data / event content | Normal + attacked process/network data; later normal-file edit removes an initial tank-drain segment |
| PCAP status | Network data described; inspect exact distributed files |
| Critical handling note | Retain version information: deleting a benign startup/drain segment changes the definition of normal |
| Freeze recommendation | Use exact file version; validate labels and event count from accompanying release documentation |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/)

## SWaT — A6: December 2019

| Field | Recorded content |
| --- | --- |
| Resource | SWaT |
| Release / edition | A6: December 2019 |
| Data / event content | PCAP and historian CSV; three normal hours, one attack hour and six described attacks |
| PCAP status | Explicitly available by request |
| Critical handling note | Good candidate for manageable integrated exercises, subject to no-sharing terms |
| Freeze recommendation | Request written event permission and exact file manifest before selection |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

## SWaT + WADI — December 18–22, 2023 joint collection

| Field | Recorded content |
| --- | --- |
| Resource | SWaT + WADI |
| Release / edition | December 18–22, 2023 joint collection |
| Data / event content | 105 hours: five closed-loop and 100 crossover; no attacks |
| PCAP status | Both provide PCAP + historian |
| Critical handling note | Approximately 429 GB SWaT + 335 GB WADI; derived network-flow data incomplete |
| Freeze recommendation | Select synchronized excerpts and preserve start/end timestamps and source-file IDs |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/)

## SWaT — December 2023 identifier discrepancy

| Field | Recorded content |
| --- | --- |
| Resource | SWaT |
| Release / edition | December 2023 identifier discrepancy |
| Data / event content | Characteristics page uses A9; summary lists A10 for this acquisition |
| PCAP status | Date-based collection known; edition ID unresolved |
| Critical handling note | Do not silently choose an ID or combine unrelated November 2022 / December 2023 files |
| Freeze recommendation | Resolve edition ID with owner; refer to acquisition dates meanwhile |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/summary-of-available-datasets/)

## SWaT — A11 February 2026; A12 March 2026

| Field | Recorded content |
| --- | --- |
| Resource | SWaT |
| Release / edition | A11 February 2026; A12 March 2026 |
| Data / event content | Listed in owner summary; detailed contents not established in reviewed characteristics page |
| PCAP status | Unverified |
| Critical handling note | Do not assume attacked traffic, protocols, tags or PCAP formats from older releases |
| Freeze recommendation | Treat as discovery entries until release-specific documentation and permission obtained |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/summary-of-available-datasets/)

## WADI — A1: October 2017

| Field | Recorded content |
| --- | --- |
| Resource | WADI |
| Release / edition | A1: October 2017 |
| Data / event content | Fourteen normal days, two attacked days, 123 sensor/actuator channels and 15 attacks |
| PCAP status | Not confirmed in distributed A1 package |
| Critical handling note | Physical CSV is useful but not evidence of an available attacked PCAP |
| Freeze recommendation | Obtain complete release manifest before assigning a packet-analysis challenge |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/)

## WADI — A2: corrected 2017-data release

| Field | Recorded content |
| --- | --- |
| Resource | WADI |
| Release / edition | A2: corrected 2017-data release |
| Data / event content | Normal values filtered; attack dates corrected; -1 denotes attack and +1 denotes normal |
| PCAP status | Not confirmed |
| Critical handling note | Label polarity differs from common 0/1 schemas; preserve a documented conversion |
| Freeze recommendation | Normalize labels explicitly; preserve original label column separately |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/)

## WADI — A3: December 2023

| Field | Recorded content |
| --- | --- |
| Resource | WADI |
| Release / edition | A3: December 2023 |
| Data / event content | Attack-free PCAP + historian; part of synchronized joint SWaT/WADI run |
| PCAP status | Explicitly available by request |
| Critical handling note | Do not attach 2017 attack labels to these 2023 traces |
| Freeze recommendation | Use as normal baseline / cross-system modeling, not as attacked network ground truth |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

## HAI — 20.07 and 21.03

| Field | Recorded content |
| --- | --- |
| Resource | HAI |
| Release / edition | 20.07 and 21.03 |
| Data / event content | Process time series; release-dependent signal set and process/global attack flags |
| PCAP status | None described |
| Critical handling note | Time continuity applies within a CSV file, not automatically across all files |
| Freeze recommendation | Keep file/run boundaries; choose a single version for a benchmark |

Sources: [source 1](https://github.com/icsdataset/hai)

## HAI — 22.04

| Field | Recorded content |
| --- | --- |
| Resource | HAI |
| Release / edition | 22.04 |
| Data / event content | Process time series; per-process attack flags removed |
| PCAP status | None described |
| Critical handling note | Use global flag and provided attack-target context; download actual Git LFS objects |
| Freeze recommendation | Check schema and label availability before writing loaders |

Sources: [source 1](https://github.com/icsdataset/hai)

## HAI / HAIEnd — 23.05

| Field | Recorded content |
| --- | --- |
| Resource | HAI / HAIEnd |
| Release / edition | 23.05 |
| Data / event content | Paired process and internal boiler-control values from the same experiments |
| PCAP status | None described |
| Critical handling note | Simultaneous collection improves context, not raw packet coverage; license notices conflict |
| Freeze recommendation | Align by verified timestamps and run IDs; resolve license before redistribution |

Sources: [source 1](https://github.com/icsdataset/hai)

## IEC61850SecurityDataset — Published synthesized substation scenarios

| Field | Recorded content |
| --- | --- |
| Resource | IEC61850SecurityDataset |
| Release / edition | Published synthesized substation scenarios |
| Data / event content | Normal, legitimate disturbances and attack PCAPNG; per-device CSV and configuration |
| PCAP status | Provided |
| Critical handling note | Attack CSV is reused normal baseline, not post-attack measured response |
| Freeze recommendation | Retain scenario/frame annotations and clearly label truth limitations |

Sources: [source 1](https://github.com/smartgridadsc/IEC61850SecurityDataset)

## KNX — 2020 baseline + merged attack sessions

| Field | Recorded content |
| --- | --- |
| Resource | KNX |
| Release / edition | 2020 baseline + merged attack sessions |
| Data / event content | Real-home bus captures plus enriched metadata |
| PCAP status | Provided |
| Critical handling note | Attack-session timestamps modified for insertion; Target includes system responses |
| Freeze recommendation | Preserve original ordering/context and document label semantics |

Sources: [source 1](https://github.com/vgraveto/knx-datasets)

## 4SICS — October 20–22, 2015

| Field | Recorded content |
| --- | --- |
| Resource | 4SICS |
| Release / edition | October 20–22, 2015 |
| Data / event content | Three heterogeneous conference-lab captures |
| PCAP status | Provided |
| Critical handling note | Mixed testing/attack activity; no assertion that a whole file is benign |
| Freeze recommendation | Curate short explained segments after protocol, privacy and timing validation |

Sources: [source 1](https://www.netresec.com/?page=PCAP4SICS)

## S4x15 — January 2015

| Field | Recorded content |
| --- | --- |
| Resource | S4x15 |
| Release / edition | January 2015 |
| Data / event content | Eight per-device / host capture files |
| PCAP status | Provided |
| Critical handling note | Cross-file timeline and duplicate traffic require inspection; no complete label set established |
| Freeze recommendation | Resolve rights, inspect clocks/capture vantage, then author an event key |

Sources: [source 1](https://www.netresec.com/?page=DigitalBond_S4)

## NIST SP 800-82 — Revision 3 final; Revision 4 initial public draft

| Field | Recorded content |
| --- | --- |
| Resource | NIST SP 800-82 |
| Release / edition | Revision 3 final; Revision 4 initial public draft |
| Data / event content | Final guidance plus September 21, 2026 draft |
| PCAP status | Not applicable |
| Critical handling note | Draft is not final. Comment deadline listed as November 30, 2026 |
| Freeze recommendation | Baseline on Revision 3; track draft additions separately |

Sources: [source 1](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [source 2](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)

## MITRE ATT&CK — Website version 19.2 at review

| Field | Recorded content |
| --- | --- |
| Resource | MITRE ATT&CK |
| Release / edition | Website version 19.2 at review |
| Data / event content | Versioned ICS knowledge-base collection |
| PCAP status | Not applicable |
| Critical handling note | Technique identifiers / definitions can change; website version does not substitute for file hash |
| Freeze recommendation | Pin exact STIX bundle, collection version, date and hash |

Sources: [source 1](https://github.com/mitre-attack/attack-stix-data), [source 2](https://attack.mitre.org/resources/versions/)

