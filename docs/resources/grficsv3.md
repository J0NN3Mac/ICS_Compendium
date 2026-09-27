# Graphical Realism Framework for Industrial Control Simulations version 3 (GRFICSv3)

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R01  
**Record type:** Generator  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Generator |
| Sector / process | Chemical-process simulation |
| Device types | Programmable Logic Controller (PLC); Human-Machine Interface (HMI); engineering station; simulated process devices; firewall and monitoring |
| Protocol coverage | Modbus over Transmission Control Protocol (Modbus TCP) is configured; other bundled services require validation |
| Protocol evidence | Configuration verified; no generated capture inspected |
| PCAP availability | Generate locally; not a packaged labeled PCAP dataset |
| Other data formats | Simulator state and component logs; export/instrumentation required |
| Physical-process ground truth | Simulated dynamic process; export the simulator state separately from potentially manipulated controller readings |
| Attack labels / semantics | No ready-made event ground truth; author scenario IDs, start/end times and affected tags |
| Topology / configuration | Compose segmentation, addresses and device configuration supplied |
| License / terms | GNU General Public License version 3 (GPL-3.0) repository; dependencies may differ |
| Redistribution gate | Own-output review |
| Access / release caveat | Public code; pin commit and images. Bundled PLC runtime is not necessarily standalone OpenPLC v4 |
| Network realism | Real protocol implementations in virtual lab; fidelity requires capture validation |
| Process realism | Dynamic simulation; not measurements from a physical production plant |
| Operational realism caveat | Rare operator, maintenance and fault events must be deliberately scripted |
| Participant difficulty | Intermediate |
| Organizer effort | Advanced |
| Build-a-thon suitability | Core custom cyber-physical track: synchronized PCAP, process values, events and answer keys |
| Adoption action | Build & validate |

## Sources and provenance

[S01](../reference/sources.md#s01), [S02](../reference/sources.md#s02), [S03](../reference/sources.md#s03), [S04](../reference/sources.md#s04)

### Recorded primary addresses

- [Primary source 1](https://github.com/Fortiphyd/GRFICSv3)
- [Primary source 2](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/plc/mbconfig.cfg)
- [Primary source 3](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/docker-compose.yml)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/Fortiphyd/GRFICSv3/main/LICENSE)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
