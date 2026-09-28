# EmreEkin ICS-Pcaps protocol sampler

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R16  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Aggregated OT and IT protocol samples of mixed origin, organized by protocol folder |
| Device types | Unspecified; folder names only (DNP3, IEC 61850, IEC 104, BACnet, S7comm, Modbus, PROFINET, OMRON, EtherNet/IP, Zigbee, plus IT protocols) |
| Protocol coverage | DNP3, IEC 61850, IEC 60870-5-104, BACnet, S7comm, Modbus, PROFINET, OMRON FINS, EtherNet/IP/CIP, COTP, Zigbee, CoAP; IT protocols (DHCP, SNMP, HTTP, LLDP, NetBIOS) |
| Protocol evidence | Folder labels only; 241 files verified by magic number; four files were gzip-wrapped; seven DNP3 LFS objects are missing upstream (404) and duplicate OpenICS files in R13 |
| PCAP availability | 241 usable capture files, 276 MB; GitHub raw (seven listed DNP3 files unavailable) |
| Other data formats | None |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | None; sampler only |
| Topology / configuration | None |
| License / terms | No license file; origin of individual captures not documented |
| Redistribution gate | Permission required |
| Access / release caveat | Public download; mixed and undocumented provenance makes redistribution rights unclear |
| Network realism | Unknown per file; many appear to be short protocol samples |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Provenance is undocumented; prefer R13 or R18 where the same capture exists with a license |
| Participant difficulty | Beginner |
| Organizer effort | Low |
| Build-a-thon suitability | Protocol identification drills; dissector exercises |
| Adoption action | Permission required |

## Sources and provenance

[S35](../reference/sources.md#s35)

### Recorded primary addresses

- [Primary source 1](https://github.com/EmreEkin/ICS-Pcaps)

### Recorded rights addresses

- [Rights source 1](https://github.com/EmreEkin/ICS-Pcaps)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
