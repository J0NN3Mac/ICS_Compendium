# ControlThings ct-samples protocol captures

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R18  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Training samples curated by ControlThings I/O for protocol analysis courses; mixed lab and public-event origin |
| Device types | Per folder: IEC 61850 IEDs, S7 PLCs, BACnet controllers, DLMS/COSEM meters, DNP3, C37.118 PMUs, IEC 104, Modbus, ANSI C12.22, SBus, Zigbee |
| Protocol coverage | IEC 61850, S7comm, BACnet, DLMS-COSEM, DNP3, Zigbee, C37.118, IEC 60870-5-104, Modbus, C12.22, SBus; a combined SANS Holiday Hack 2013 capture |
| Protocol evidence | Folder labels; 111 files verified by magic number; SANS_HolidayHack_2013.pcap (168 MB) retrieved from GitHub LFS |
| PCAP availability | 111 capture files, 205 MB; GitHub raw plus one LFS object |
| Other data formats | Course materials elsewhere in repository (not imported) |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | No attack labels; Combined/ folder holds event captures |
| Topology / configuration | None |
| License / terms | GNU GPL v3 (repository LICENSE); applicability of a software license to capture data is ambiguous |
| Redistribution gate | Attribution / review |
| Access / release caveat | Public download; GPL-3.0 terms apply as stated; clarify intent for data files before redistribution |
| Network realism | Mixed authentic and training-built samples |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Samples are chosen for teaching clarity, not operational representativeness |
| Participant difficulty | Beginner–intermediate |
| Organizer effort | Low |
| Build-a-thon suitability | Protocol analysis coursework, dissector drills, meter-protocol exposure (DLMS, C12.22) |
| Adoption action | Curate & validate |

## Sources and provenance

[S37](../reference/sources.md#s37), [S38](../reference/sources.md#s38)

### Recorded primary addresses

- [Primary source 1](https://github.com/ControlThings-io/ct-samples/tree/master/Protocols)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/LICENSE)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
