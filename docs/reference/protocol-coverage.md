# Protocol Coverage

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

Evidence codes are defined in [the glossary](glossary.md). No cell is a claim of newly decoded traffic.

| ID | Resource | Modbus | CIP / EtherNet/IP | S7comm | PROFINET | DNP3 | IEC 60870-5-104 | OPC UA | IEC 61850 GOOSE | IEC 61850 MMS | IEC 61850 Sampled Values | BACnet | KNX | EtherCAT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | GRFICSv3 | Configured | — | — | — | Bundled only | — | — | — | — | — | — | — | — |
| R02 | OpenPLC v4 | Plugin | — | Plugin | — | — | — | Plugin | — | — | — | — | — | Plugin |
| R03 | Conpot | Emulated | Emulated | Emulated | — | — | Emulated | — | — | — | — | Emulated | — | — |
| R04 | SWaT | — | Lab | — | — | — | — | — | — | — | — | — | — | — |
| R05 | WADI | Lab | Lab | — | — | — | — | — | — | — | — | — | — | — |
| R06 | HAI / HAIEnd | — | — | — | — | — | — | Acquisition | — | — | — | — | — | — |
| R07 | IEC61850SecurityDataset | — | — | — | — | — | — | — | Dataset | — | — | — | — | — |
| R08 | KNX contextual dataset | — | — | — | — | — | — | — | — | — | — | — | Dataset | — |
| R09 | 4SICS | Candidate | — | Candidate | — | Candidate | — | — | — | — | — | — | — | — |
| R10 | S4x15 | Unverified | Unverified | — | — | — | — | — | — | — | — | Named file | — | — |
| R11 | NIST SP 800-82 | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference |
| R12 | MITRE ATT&CK for ICS | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference | Reference |

## Interpretation by resource

### R01 — GRFICSv3

Configured Modbus process path. Bundled DNP3 configuration does not establish active traffic.

Sources: [source 1](https://github.com/Fortiphyd/GRFICSv3), [source 2](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/plc/mbconfig.cfg), [source 3](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/docker-compose.yml)

### R02 — OpenPLC v4

Plugin entries are capabilities to configure and validate; no capture supplied.

Sources: [source 1](https://github.com/Autonomy-Logic/openplc-runtime), [source 2](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf)

### R03 — Conpot

Template-dependent endpoint service implementations; not full industrial or cyclic-process fidelity.

Sources: [source 1](https://github.com/mushorg/conpot), [source 2](https://conpot.readthedocs.io/en/latest/)

### R04 — SWaT

Owner lab architecture establishes EtherNet/IP; decode the exact permitted release to confirm packet mix.

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/), [source 2](https://www.sutd.edu.sg/itrust/swat/)

### R05 — WADI

Lab protocols; raw captures confirmed for attack-free December 2023 release, not automatically A1/A2.

Sources: [source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/), [source 2](https://www.sutd.edu.sg/itrust/wadi/)

### R06 — HAI / HAIEnd

Gateway acquisition uses OPC UA, but published CSV is not OPC UA packet evidence.

Sources: [source 1](https://github.com/icsdataset/hai)

### R07 — IEC61850SecurityDataset

GOOSE explicitly documented in PCAPNG. No claim of full IEC 61850 stack coverage.

Sources: [source 1](https://github.com/smartgridadsc/IEC61850SecurityDataset)

### R08 — KNX contextual dataset

Twisted-pair bus telegrams; inspect link type before treating as Ethernet KNXnet/IP.

Sources: [source 1](https://github.com/vgraveto/knx-datasets)

### R09 — 4SICS

Candidate services from inventory/ports, not a decoded packet-protocol inventory.

Sources: [source 1](https://www.netresec.com/?page=PCAP4SICS)

### R10 — S4x15

BACnet capture names are explicit. Do not infer PLC wire protocols from vendor names alone.

Sources: [source 1](https://www.netresec.com/?page=DigitalBond_S4)

### R11 — NIST SP 800-82

Reference means architectural/protocol context only; this row contributes no packet coverage.

Sources: [source 1](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [source 2](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)

### R12 — MITRE ATT&CK for ICS

Taxonomy does not constitute protocol traffic, implementation support or observed event labels.

Sources: [source 1](https://attack.mitre.org/matrices/ics/), [source 2](https://github.com/mitre-attack/attack-stix-data)

