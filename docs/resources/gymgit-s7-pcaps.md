# gymgit S7comm client/PLC captures

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R15  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Bench captures between engineering clients (STEP 7 5.5, TIA Portal v13, Snap7 client, WinCC Advanced) and S7-300/S7-400 PLCs |
| Device types | Siemens S7-300 and S7-400 PLCs; Windows engineering workstations |
| Protocol coverage | S7comm (incl. authentication, firmware update, block upload/download per README) |
| Protocol evidence | README function list; 21 files verified by magic number; IPs rewritten by author (tcprewrite) |
| PCAP availability | 21 pcap files, 29 MB; GitHub raw |
| Other data formats | None |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | Per-file function labels via names; no attack labels (benign engineering operations) |
| Topology / configuration | README only |
| License / terms | No license file; README states captures were created for public use |
| Redistribution gate | Attribution / review |
| Access / release caveat | Public download; author statement contemplates public use but is not a formal license |
| Network realism | Authentic engineering-session traffic with addresses rewritten |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Security-critical functions (password, firmware) are benign operator actions here, not attacks |
| Participant difficulty | Intermediate |
| Organizer effort | Low |
| Build-a-thon suitability | S7comm function decoding, engineering-workstation behavior baselining, detection of block/firmware writes |
| Adoption action | Curate & validate |

## Sources and provenance

[S34](../reference/sources.md#s34)

### Recorded primary addresses

- [Primary source 1](https://github.com/gymgit/s7-pcaps)

### Recorded rights addresses

- [Rights source 1](https://github.com/gymgit/s7-pcaps)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
