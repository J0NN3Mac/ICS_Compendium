# Lemay & Fernandez Modbus dataset (CSET 2016)

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R14  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Small SCADA sandbox: Modbus TCP master polling 3, 6 or 12 emulated RTUs; IT-side host compromise scenarios |
| Device types | Emulated RTUs (Modbus TCP), Windows master station, attacker host |
| Protocol coverage | Modbus TCP; IT protocols during exploitation (SMB, C2) |
| Protocol evidence | README scenario descriptions; 11 root-level pcaps verified by magic number; 8 zip archives (channel_* captures) not opened by this catalog |
| PCAP availability | 11 pcap files (85 MB) plus 8 zip archives at repository root; GitHub raw |
| Other data formats | None documented beyond README |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | Scenario-level labels via file names (polling-only baseline, MS08-067 exploit, C2 upload, fake command, file moves); no per-packet labels |
| Topology / configuration | README describes RTU counts and polling intervals; no diagram |
| License / terms | No license file found in repository tree; academic citation requested (CSET 2016) |
| Redistribution gate | Permission required |
| Access / release caveat | Public download; no explicit reuse grant; contact authors before bundling into commercial training |
| Network realism | Emulated lab traffic with real exploitation tooling |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Baselines are short and low-diversity; do not treat polling-only capture as a production baseline |
| Participant difficulty | Beginner–intermediate |
| Organizer effort | Low |
| Build-a-thon suitability | IT-to-OT pivot investigation, Modbus write detection, baseline versus attack comparison |
| Adoption action | Permission required |

## Sources and provenance

[S33](../reference/sources.md#s33)

### Recorded primary addresses

- [Primary source 1](https://github.com/antoine-lemay/Modbus_dataset)

### Recorded rights addresses

- [Rights source 1](https://github.com/antoine-lemay/Modbus_dataset)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
