# Gap Register

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

## G01 — Synchronized packets + independent process truth + operator intent

| Field | Recorded content |
| --- | --- |
| Gap ID | G01 |
| Gap within selected corpus | Synchronized packets + independent process truth + operator intent |
| Current evidence / partial coverage | SWaT offers packet/process pairs behind access restrictions; GRFICS can generate a joint record; other datasets omit parts |
| Why it matters | A decoded write does not establish the physical consequence or whether it was authorized |
| Action to close gap | Instrument one canonical simulator with separate state, controller readings, HMI events and exact event labels |
| Priority | Critical |
| Validation evidence required | Common timebase; tag map; simulator state; captures; operator/maintenance log; honest truth provenance |

Sources: [source 1](https://github.com/Fortiphyd/GRFICSv3), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 3](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/), [source 4](https://github.com/smartgridadsc/IEC61850SecurityDataset)

## G02 — Benign rare operations and equipment faults

| Field | Recorded content |
| --- | --- |
| Gap ID | G02 |
| Gap within selected corpus | Benign rare operations and equipment faults |
| Current evidence / partial coverage | IEC collection includes legitimate electrical disturbances; conference traffic is not clean operational labeling |
| Why it matters | Maintenance, restart, link failure and sensor failure can resemble attacks |
| Action to close gap | Generate labeled startup, shutdown, maintenance, device fault and communication-loss scenarios alongside attacks |
| Priority | High |
| Validation evidence required | Same process under benign and malicious cases; documented authorization and outcomes |

Sources: [source 1](https://github.com/smartgridadsc/IEC61850SecurityDataset), [source 2](https://www.netresec.com/?page=PCAP4SICS), [source 3](https://www.netresec.com/?page=DigitalBond_S4)

## G03 — EtherNet/IP explicit messaging versus cyclic I/O

| Field | Recorded content |
| --- | --- |
| Gap ID | G03 |
| Gap within selected corpus | EtherNet/IP explicit messaging versus cyclic I/O |
| Current evidence / partial coverage | SWaT/WADI document EtherNet/IP but exact release capture mix not decoded; Conpot provides service emulation |
| Why it matters | Service support alone does not establish authentic cyclic I/O timing or process coupling |
| Action to close gap | Inspect permitted traces and create explicit-message plus cyclic-I/O benchmark scenarios where supported |
| Priority | High |
| Validation evidence required | Decoded services, connection parameters, capture vantage and measured cadence |

Sources: [source 1](https://www.sutd.edu.sg/itrust/swat/), [source 2](https://www.sutd.edu.sg/itrust/wadi/), [source 3](https://conpot.readthedocs.io/en/latest/)

## G04 — PROFINET real-time and discovery / alarm traffic

| Field | Recorded content |
| --- | --- |
| Gap ID | G04 |
| Gap within selected corpus | PROFINET real-time and discovery / alarm traffic |
| Current evidence / partial coverage | No validated PROFINET packet corpus identified in this selected set; S7comm does not imply PROFINET coverage |
| Why it matters | Controller application traffic and real-time I/O teach different communication patterns |
| Action to close gap | Add a documented isolated controller / I/O capture or a separately licensed dataset |
| Priority | High |
| Validation evidence required | Layer-2 dissections, topology, update intervals, alarms and benign operational labels |

Sources: [source 1](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf), [source 2](https://conpot.readthedocs.io/en/latest/), [source 3](https://www.netresec.com/?page=PCAP4SICS)

## G05 — DNP3 and IEC 60870-5-104 with physical context

| Field | Recorded content |
| --- | --- |
| Gap ID | G05 |
| Gap within selected corpus | DNP3 and IEC 60870-5-104 with physical context |
| Current evidence / partial coverage | 4SICS inventories DNP3 services; Conpot documents IEC 104 emulation; neither establishes rich labeled process truth |
| Why it matters | Utility event reporting and control sequences require context beyond port discovery |
| Action to close gap | Seek a permitted utility dataset or build a controlled outstation/process simulation |
| Priority | High |
| Validation evidence required | Actual protocol objects/events, synchronized physical state and operator authorization |

Sources: [source 1](https://www.netresec.com/?page=PCAP4SICS), [source 2](https://conpot.readthedocs.io/en/latest/)

## G06 — OPC UA subscriptions and secure modes

| Field | Recorded content |
| --- | --- |
| Gap ID | G06 |
| Gap within selected corpus | OPC UA subscriptions and secure modes |
| Current evidence / partial coverage | OpenPLC lists an OPC UA plugin; HAI uses acquisition through an OPC UA gateway but distributes CSV |
| Why it matters | Process data does not expose session, subscription or encrypted-traffic behavior |
| Action to close gap | Generate secure and deliberately transparent lab profiles with known sampling/subscription parameters |
| Priority | High |
| Validation evidence required | Pinned security settings; capture visibility limits; publish/sampling rates and application logs |

Sources: [source 1](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf), [source 2](https://github.com/icsdataset/hai)

## G07 — IEC 61850 beyond GOOSE

| Field | Recorded content |
| --- | --- |
| Gap ID | G07 |
| Gap within selected corpus | IEC 61850 beyond GOOSE |
| Current evidence / partial coverage | Selected substation corpus establishes GOOSE only |
| Why it matters | MMS and Sampled Values are different aspects of substation communication |
| Action to close gap | Add separately documented and licensed MMS / Sampled Values material rather than marking the family fully covered |
| Priority | Medium |
| Validation evidence required | Protocol-level proof, IED configuration, process context and rights |

Sources: [source 1](https://github.com/smartgridadsc/IEC61850SecurityDataset)

## G08 — Safety-system track

| Field | Recorded content |
| --- | --- |
| Gap ID | G08 |
| Gap within selected corpus | Safety-system track |
| Current evidence / partial coverage | No dedicated safety-system dataset established among the 12 core families |
| Why it matters | Safety logic, safety state and ordinary process control should not be conflated |
| Action to close gap | Maintain as a separate future acquisition / simulation track |
| Priority | Medium |
| Validation evidence required | Safety-specific device/state documentation, synthetic safety cases and controlled permissions |

Sources: [source 1](https://github.com/Fortiphyd/GRFICSv3), [source 2](https://github.com/Autonomy-Logic/openplc-runtime), [source 3](https://github.com/mushorg/conpot), [source 4](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 5](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/), [source 6](https://github.com/icsdataset/hai), [source 7](https://github.com/smartgridadsc/IEC61850SecurityDataset), [source 8](https://github.com/vgraveto/knx-datasets), [source 9](https://www.netresec.com/?page=PCAP4SICS), [source 10](https://www.netresec.com/?page=DigitalBond_S4)

## G09 — Production-like human and maintenance context

| Field | Recorded content |
| --- | --- |
| Gap ID | G09 |
| Gap within selected corpus | Production-like human and maintenance context |
| Current evidence / partial coverage | Most resources expose packets or tags, not complete operator actions, change tickets and maintenance windows |
| Why it matters | The same protocol-valid action can be permitted or unauthorized depending on context |
| Action to close gap | Author benign and unauthorized variants using identical command types with different context |
| Priority | High |
| Validation evidence required | Operator event ledger, authority/maintenance context, alarm acknowledgements and device state |

Sources: [source 1](https://github.com/Fortiphyd/GRFICSv3), [source 2](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 3](https://github.com/icsdataset/hai), [source 4](https://www.netresec.com/?page=PCAP4SICS)

## G10 — Release integrity, labels and replay-quality checks

| Field | Recorded content |
| --- | --- |
| Gap ID | G10 |
| Gap within selected corpus | Release integrity, labels and replay-quality checks |
| Current evidence / partial coverage | WADI label polarity, KNX response labels, IEC baseline CSV and SWaT edition IDs require special treatment |
| Why it matters | Bad labels or mismatched releases can make an otherwise polished challenge unsound |
| Action to close gap | Keep file hashes, schema versions, known issues, label semantics, capture metadata and split manifests |
| Priority | Critical |
| Validation evidence required | File-level manifest, checksums, packet completeness, clocks and reproducible answer key |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/), [source 2](https://github.com/vgraveto/knx-datasets), [source 3](https://github.com/smartgridadsc/IEC61850SecurityDataset), [source 4](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 5](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/summary-of-available-datasets/)

## G11 — Redistributable corporate event bundle

| Field | Recorded content |
| --- | --- |
| Gap ID | G11 |
| Gap within selected corpus | Redistributable corporate event bundle |
| Current evidence / partial coverage | SWaT/WADI restrict onward sharing; HAI has conflicting notices; IEC and S4x15 lack a confirmed broad grant |
| Why it matters | Publicly downloadable material cannot automatically be placed on an internal or public event server |
| Action to close gap | Clear rights early; publish only permitted curated datasets and clean self-generated traces |
| Priority | Critical |
| Validation evidence required | Stored license snapshots / grants, attribution bundle and explicit participant access model |

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/), [source 2](https://github.com/icsdataset/hai), [source 3](https://github.com/smartgridadsc/IEC61850SecurityDataset), [source 4](https://www.netresec.com/?page=DigitalBond_S4)

## G12 — Modern versus legacy network coverage

| Field | Recorded content |
| --- | --- |
| Gap ID | G12 |
| Gap within selected corpus | Modern versus legacy network coverage |
| Current evidence / partial coverage | 4SICS and S4x15 are 2015 lab collections; newer generators support contemporary experiment design |
| Why it matters | Historical authenticity should not be mistaken for a current production reference architecture |
| Action to close gap | Pair historical exercises with a version-pinned modern synthetic plant and explain differences |
| Priority | Medium |
| Validation evidence required | Architecture version, component inventory and explicit scope of what the scenario represents |

Sources: [source 1](https://www.netresec.com/?page=PCAP4SICS), [source 2](https://www.netresec.com/?page=DigitalBond_S4), [source 3](https://github.com/Fortiphyd/GRFICSv3), [source 4](https://github.com/Autonomy-Logic/openplc-runtime)

