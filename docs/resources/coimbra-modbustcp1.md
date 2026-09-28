# University of Coimbra ICS_PCAPS MODBUSTCP#1

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R20  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Modbus TCP SCADA testbed under flooding and DDoS conditions (University of Coimbra CyberSec) |
| Device types | Modbus TCP master/slaves (per archive folder names); attacker hosts |
| Protocol coverage | Modbus TCP; TCP SYN and ICMP flood traffic |
| Protocol evidence | Archive folder names (modbusQueryFlooding, modbusQuery2Flooding, pingFloodDDoS, tcpSYNFloodDDoS); three zips integrity-tested; inner pcaps not individually verified |
| PCAP availability | Three GitHub release archives: 670 MB + 195 MB + 224 MB packed, about 4.5 GB unpacked (166 + 37 + 37 entries) |
| Other data formats | None documented |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | Scenario-level labels by folder and file name (attack type, duration); no per-packet labels |
| Topology / configuration | None found in release |
| License / terms | No license file in repository or release |
| Redistribution gate | Permission required |
| Access / release caveat | Public download; no reuse grant; large volume |
| Network realism | Testbed traffic under volumetric attack |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Flooding captures are volumetric; benign baseline share per archive not characterized |
| Participant difficulty | Intermediate |
| Organizer effort | Intermediate |
| Build-a-thon suitability | DoS/flood detection tuning, Modbus availability-impact exercises, large-capture handling |
| Adoption action | Permission required |

## Sources and provenance

[S41](../reference/sources.md#s41), [S42](../reference/sources.md#s42)

### Recorded primary addresses

- [Primary source 1](https://github.com/tjcruz-dei/ICS_PCAPS/releases/tag/MODBUSTCP%231)
- [Primary source 2](https://github.com/tjcruz-dei/ICS_PCAPS)

### Recorded rights addresses

- [Rights source 1](https://github.com/tjcruz-dei/ICS_PCAPS)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
