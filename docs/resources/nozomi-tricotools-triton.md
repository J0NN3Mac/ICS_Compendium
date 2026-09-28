# Nozomi tricotools TRITON/TriStation capture

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R19  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Safety instrumented system (Triconex) engineering protocol; TRITON malware execution demonstration |
| Device types | Triconex safety controller (emulated/lab), engineering workstation |
| Protocol coverage | TriStation (proprietary, UDP 1502) |
| Protocol evidence | Repository states capture is of TRITON execution; one file verified by magic number; dissector and honeypot tooling accompany it |
| PCAP availability | One pcap file, 0.5 MB; GitHub raw |
| Other data formats | Wireshark TriStation dissector (Lua), honeypot script |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | Single malicious-session capture; no benign baseline |
| Topology / configuration | None |
| License / terms | BSD 3-Clause (repository LICENSE) |
| Redistribution gate | Attribution / review |
| Access / release caveat | Public download; BSD attribution required |
| Network realism | Lab reproduction of real malware protocol behavior |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | One session only; not representative of normal TriStation engineering traffic volumes |
| Participant difficulty | Advanced |
| Organizer effort | Low |
| Build-a-thon suitability | Safety-system attack walkthrough, custom dissector exercise, TRITON detection logic |
| Adoption action | Curate & validate |

## Sources and provenance

[S39](../reference/sources.md#s39), [S40](../reference/sources.md#s40)

### Recorded primary addresses

- [Primary source 1](https://github.com/NozomiNetworks/tricotools)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/NozomiNetworks/tricotools/master/LICENSE)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
