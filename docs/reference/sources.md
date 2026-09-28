# Primary-source register

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

## S01

**Resource:** GRFICSv3  
**Source type:** Project README  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/Fortiphyd/GRFICSv3)

Containerized chemical-process lab, components, network layout and setup; documentation, not a runtime test.

## S02

**Resource:** GRFICSv3  
**Source type:** Modbus device configuration  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/plc/mbconfig.cfg)

Six simulated process devices; Modbus TCP port 502; configured polling period 100 ms, not measured timing.

## S03

**Resource:** GRFICSv3  
**Source type:** Compose configuration  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/docker-compose.yml)

Services, segmentation and exposed ports. Exposed ports are not proof of active protocol traffic.

## S04

**Resource:** GRFICSv3  
**Source type:** Repository license  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/LICENSE)

GNU General Public License version 3; check bundled components separately.

## S05

**Resource:** OpenPLC  
**Source type:** Runtime v4 README  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/Autonomy-Logic/openplc-runtime)

Standalone headless runtime v4; do not conflate with the legacy runtime bundled in other projects.

## S06

**Resource:** OpenPLC  
**Source type:** Plugin manifest  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf)

Modbus master/slave, OPC UA, S7comm and EtherCAT plugin entries; configuration support, not inspected wire traffic.

## S07

**Resource:** OpenPLC  
**Source type:** Runtime license  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/LICENSE)

MIT license for this runtime repository; other versions, editor and dependencies may differ.

## S08

**Resource:** Conpot  
**Source type:** Project README  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/mushorg/conpot)

Industrial endpoint honeypot; templates and deployment. Not a physics simulator.

## S09

**Resource:** Conpot  
**Source type:** Protocol documentation  
**Inherited review date:** 2026-09-27

[Open original source](https://conpot.readthedocs.io/en/latest/)

Protocol implementations are template-dependent; no claim of full vendor stack fidelity.

## S10

**Resource:** Conpot  
**Source type:** Repository license  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/mushorg/conpot/main/LICENSE.txt)

GNU General Public License version 2; source license does not automatically license all captured content.

## S11

**Resource:** SWaT  
**Source type:** Dataset characteristics  
**Inherited review date:** 2026-09-27

[Open original source](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/)

Edition-specific network/process data and attack descriptions; A6 explicitly provides PCAP and historian CSV.

## S12

**Resource:** SWaT  
**Source type:** Physical testbed  
**Inherited review date:** 2026-09-27

[Open original source](https://www.sutd.edu.sg/itrust/swat/)

Six-stage physical plant, devices, diagrams and EtherNet/IP architecture.

## S13

**Resource:** WADI  
**Source type:** Dataset characteristics  
**Inherited review date:** 2026-09-27

[Open original source](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/)

A1/A2 process data; A3 December 2023 synchronized PCAP and historian data without attacks.

## S14

**Resource:** WADI  
**Source type:** Physical testbed  
**Inherited review date:** 2026-09-27

[Open original source](https://www.sutd.edu.sg/itrust/wadi/)

Water distribution plant, industrial controllers, remote units, gateways, EtherNet/IP and Modbus architecture.

## S15

**Resource:** SWaT / WADI  
**Source type:** iTrust dataset terms  
**Inherited review date:** 2026-09-27

[Open original source](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

No private or public onward sharing; credit, publication notification and requester disclosure requirements.

## S16

**Resource:** SWaT / WADI  
**Source type:** Release summary  
**Inherited review date:** 2026-09-27

[Open original source](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/summary-of-available-datasets/)

Additional SWaT 2026 releases listed; December 2023 SWaT identifier conflicts with characteristics page.

## S17

**Resource:** HAI / HAIEnd  
**Source type:** Dataset README and metadata  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/icsdataset/hai)

CSV time series, hardware-in-the-loop testbed, labels, versions, graphs; CC BY-SA 4.0 prose versus CC BY 4.0 metadata.

## S18

**Resource:** IEC 61850  
**Source type:** Dataset README and file tree  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/smartgridadsc/IEC61850SecurityDataset)

Synthesized GOOSE PCAPNG, per-device CSV and configuration; attack CSV reuses baseline. No explicit license found in reviewed tree.

## S19

**Resource:** KNX  
**Source type:** Dataset README  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/vgraveto/knx-datasets)

Real-home KNX bus captures and contextual CSV; captured attacks merged into baseline with modified times; Target label includes responses.

## S20

**Resource:** KNX  
**Source type:** Repository license  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/LICENSE)

MIT license. External mirrors/package terms must be checked separately.

## S21

**Resource:** 4SICS  
**Source type:** Host download / attribution page  
**Inherited review date:** 2026-09-27

[Open original source](https://www.netresec.com/?page=PCAP4SICS)

Three 2015 lab PCAPs, inventory and layout; credit CS3Sthlm and link Netresec for redistribution or training.

## S22

**Resource:** S4x15  
**Source type:** Host download page  
**Inherited review date:** 2026-09-27

[Open original source](https://www.netresec.com/?page=DigitalBond_S4)

Eight 2015 CTF PCAPs and network diagram. Hosting permission is described, but broad downstream redistribution grant not found.

## S23

**Resource:** NIST SP 800-82  
**Source type:** Revision 3 final  
**Inherited review date:** 2026-09-27

[Open original source](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

Stable final Operational Technology security guidance; not a packet dataset.

## S24

**Resource:** NIST SP 800-82  
**Source type:** Revision 4 initial public draft  
**Inherited review date:** 2026-09-27

[Open original source](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)

Draft released September 21, 2026; track separately from final guidance.

## S25

**Resource:** NIST  
**Source type:** Publication reuse policy  
**Inherited review date:** 2026-09-27

[Open original source](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications)

Technical-publication reuse policy; attribution and third-party material exceptions.

## S26

**Resource:** MITRE ATT&CK for ICS  
**Source type:** ICS matrix  
**Inherited review date:** 2026-09-27

[Open original source](https://attack.mitre.org/matrices/ics/)

Behavior taxonomy and scenario mapping; not packet or process observations.

## S27

**Resource:** MITRE ATT&CK  
**Source type:** Structured data repository  
**Inherited review date:** 2026-09-27

[Open original source](https://github.com/mitre-attack/attack-stix-data)

STIX 2.1 collections; version-pinned machine-readable knowledge base.

## S28

**Resource:** MITRE ATT&CK  
**Source type:** Data license  
**Inherited review date:** 2026-09-27

[Open original source](https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/LICENSE.txt)

Research, development and commercial reuse permitted subject to notices and license.

## S29

**Resource:** MITRE ATT&CK  
**Source type:** Versions  
**Inherited review date:** 2026-09-27

[Open original source](https://attack.mitre.org/resources/versions/)

Current website version 19.2 at review; pin the exact ICS data release for an event.

## S30

**Resource:** MITRE ATT&CK  
**Source type:** Legal and branding  
**Inherited review date:** 2026-09-27

[Open original source](https://attack.mitre.org/resources/legal-and-branding/)

Attribution and trademark guidance; do not imply endorsement.

