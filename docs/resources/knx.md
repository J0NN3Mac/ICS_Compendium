# KNX contextual datasets

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R08  
**Record type:** Dataset / capture  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Real residential building automation |
| Device types | Motion, temperature and light sensors; lighting/blind/heating actuators; touch panels and alarms |
| Protocol coverage | KNX twisted-pair bus telegrams; do not assume KNXnet/IP Ethernet framing |
| Protocol evidence | Owner describes bus capture; capture link type still needs file inspection |
| PCAP availability | Provided PCAP plus enriched CSV |
| Other data formats | Engineering context: source/destination, location, function, values and Target field |
| Physical-process ground truth | Real installation context and observations; no separate synchronized physical historian established |
| Attack labels / semantics | Target=1 includes attacks AND system responses. Captured attack sessions are merged into baseline with modified timestamps |
| Topology / configuration | Engineering-tool metadata and device context; not a full conventional IP topology |
| License / terms | MIT repository license; review external mirror terms separately |
| Redistribution gate | Attribution / review |
| Access / release caveat | Public repository; privacy review for occupancy/location patterns before distribution |
| Network realism | Real bus traffic, with reconstructed attack chronology |
| Process realism | Real installation observations; no independent physical oracle |
| Operational realism caveat | Mixed timeline is not an uninterrupted natural attack recording |
| Participant difficulty | Intermediate |
| Organizer effort | Intermediate |
| Build-a-thon suitability | Strong contextual detection and semantic-decoder track after notice/privacy checks |
| Adoption action | Curate & validate |

## Sources and provenance

[S19](../reference/sources.md#s19), [S20](../reference/sources.md#s20)

### Recorded primary addresses

- [Primary source 1](https://github.com/vgraveto/knx-datasets)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/LICENSE)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
