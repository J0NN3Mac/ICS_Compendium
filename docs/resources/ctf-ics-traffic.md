# ICS CTF traffic (Modbus/TCP and S7comm)

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R17  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Capture-the-flag exercise traffic; scenario details in Chinese README with helper scripts |
| Device types | Unspecified PLC/HMI emulation |
| Protocol coverage | Modbus TCP and S7comm per README |
| Protocol evidence | README statement; one 49 MB pcapng verified by magic number; helper scripts included |
| PCAP availability | One pcapng file, 49 MB; GitHub raw |
| Other data formats | Python analysis scripts (packet parsing, decoding attempts, format transfer) |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | CTF challenge framing; flags embedded in traffic per README; no formal attack labels |
| Topology / configuration | None |
| License / terms | No license file |
| Redistribution gate | Permission required |
| Access / release caveat | Public download; no reuse grant |
| Network realism | Synthetic CTF traffic |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Puzzle traffic, not operational baseline |
| Participant difficulty | Intermediate |
| Organizer effort | Low |
| Build-a-thon suitability | Scored CTF-style packet forensics |
| Adoption action | Permission required |

## Sources and provenance

[S36](../reference/sources.md#s36)

### Recorded primary addresses

- [Primary source 1](https://github.com/NewBee119/ctf_ics_traffic)

### Recorded rights addresses

- [Rights source 1](https://github.com/NewBee119/ctf_ics_traffic)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
