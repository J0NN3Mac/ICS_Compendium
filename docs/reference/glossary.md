# Glossary

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

| Term | Shorthand / category | Meaning / handling rule |
| --- | --- | --- |
| Supervisory Control and Data Acquisition | SCADA | Supervisory monitoring and control; not necessarily the controller's local control loop. |
| Industrial Control System | ICS | Control systems used to monitor or operate industrial processes. |
| Operational Technology | OT | Systems interacting with physical processes; not synonymous with ordinary enterprise networking. |
| Packet capture | PCAP | Captured packets. PCAPNG means PCAP Next Generation container format. |
| Programmable Logic Controller | PLC | Controller executing control logic; not automatically a complete process simulator. |
| Human-Machine Interface | HMI | Operator interface for status, alarms and permitted commands. |
| Remote Terminal Unit | RTU | Remote telemetry/control device. |
| Input/Output | I/O | Signals linking controller logic to sensors and actuators. |
| Distributed Control System | DCS | Industrial control platform; distinct from raw packet data. |
| Intelligent Electronic Device | IED | Protection/control device, commonly in electrical systems. |
| Hardware-in-the-Loop | HIL | Real control hardware coupled to a simulated process or system. |
| Capture-the-Flag | CTF | Challenge format; the presence of CTF traffic does not provide complete labels. |
| Transmission Control Protocol | TCP | Transport used by Modbus TCP and other applications. |
| Internet Protocol | IP | Network-layer protocol; some industrial traffic is non-IP Ethernet or fieldbus. |
| Common Industrial Protocol | CIP | Industrial application protocol used over EtherNet/IP; explicit and implicit traffic are not interchangeable. |
| Open Platform Communications Unified Architecture | OPC UA | Industrial information and service framework; gateway-acquired CSV is not a packet trace. |
| Distributed Network Protocol 3 | DNP3 | Utility-oriented telemetry and control protocol. |
| International Electrotechnical Commission | IEC | Standards body; relevant families include IEC 60870-5-104 and IEC 61850. |
| Generic Object Oriented Substation Event | GOOSE | IEC 61850 event messaging present in the selected substation dataset. |
| Manufacturing Message Specification | MMS | A separate substation communication component; not confirmed by GOOSE-only coverage. |
| Building Automation and Control Networks | BACnet | Building-automation protocol family. |
| PROFINET | PROFINET | Industrial Ethernet protocol family; do not infer coverage from Siemens S7comm. |
| KNX | KNX | Building-control standard / brand; the selected capture describes twisted-pair bus telegrams. |
| Ethernet for Control Automation Technology | EtherCAT | Industrial Ethernet fieldbus; listed OpenPLC plugin is not an existing labeled corpus. |
| Comma-separated values | CSV | Tabular values; may contain sensor data or packet-derived features, not necessarily original packets. |
| Structured Threat Information Expression | STIX | Machine-readable knowledge format; ATT&CK provides STIX 2.1 collections. |
| National Institute of Standards and Technology / Special Publication | NIST / SP | NIST SP 800-82 is guidance, not a packet dataset. |
| Adversarial Tactics, Techniques, and Common Knowledge | ATT&CK | MITRE behavior knowledge base; mapping requires evidence. |
| GNU General Public License | GPL | Software copyleft license; inspect version and obligations for each component. |
| Creative Commons Attribution / Attribution-ShareAlike | CC BY / CC BY-SA | Different content-license obligations; HAI lists conflicting notices. |
| MIT license | MIT | Permissive software/content license notice; retain copyright and permission text. |
| Git Large File Storage | Git LFS | Mechanism used by newer HAI releases to retrieve actual large files. |
| Physical-process ground truth | Definition | Measured or simulated process state with provenance. A potentially manipulated sensor value is not an independent oracle. |
| Network realism | Assessment | Qualitative judgment of actual device traffic, implemented protocol behavior and emulation limitations; no numerical benchmark score. |
| Process realism | Assessment | Distinguish real laboratory process, HIL-augmented process, simulation, baseline values and absent physical context. |
| Participant difficulty | Assessment | Beginner: guided discovery; intermediate: protocol/context analysis; advanced: multi-stream causal analysis and modeling. |
| Organizer effort | Assessment | Low: reference preparation; intermediate: data/label curation; advanced: integration, instrumentation or large synchronized releases. Not a time estimate. |
| Suitability | Assessment | Proposed learning role based on documented strengths and limitations, not a tested event-readiness certification. |
| Configured / Plugin / Emulated | Protocol legend | Documented generator behavior or capability; must be run and captured before claiming active wire coverage. |
| Lab / Acquisition | Protocol legend | Protocol in the documented testbed or collection path; does not prove it is in a distributed PCAP. |
| Dataset / Named file | Protocol legend | Owner explicitly describes protocol traces / uses a protocol-specific filename. Binary QA remains outstanding. |
| Candidate / Unverified / Bundled only | Protocol legend | Discovery or configuration evidence only; do not count as validated protocol coverage. |
| Reference / — | Protocol legend | Reference contributes no packet coverage. Dash means not established in this review, not proof of absence. |
| Verification scope | Review boundary | Primary documentation, license and configuration review only. No full PCAP archive audit, runtime benchmark or permission request was performed. |
