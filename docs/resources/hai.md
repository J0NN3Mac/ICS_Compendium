# Hardware-in-the-Loop-based Augmented ICS (HAI) / HAIEnd

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R06  
**Record type:** Dataset / capture  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Boiler, turbine, water treatment and simulated power generation |
| Device types | GE and Emerson Distributed Control Systems (DCSs); Siemens PLCs; remote I/O; OPC UA gateway; hardware-in-the-loop simulator |
| Protocol coverage | OPC UA acquisition documented; released CSV does not establish packet-level protocol coverage |
| Protocol evidence | Acquisition architecture only; no raw protocol capture in described release |
| PCAP availability | No PCAP in described repository dataset releases |
| Other data formats | Compressed CSV time series; HAIEnd internal boiler-control points; NetworkX graphs |
| Physical-process ground truth | Measured lab variables coupled to Hardware-in-the-Loop (HIL) simulation |
| Attack labels / semantics | Global attack flag; per-process flags removed from 22.04. HAIEnd 23.05 collected alongside HAI 23.05 |
| Topology / configuration | Published control/process graphs and linked technical manual; not a packet-level topology audit |
| License / terms | Conflicting notices: CC BY-SA 4.0 in license section; CC BY 4.0 in metadata |
| Redistribution gate | License clarification |
| Access / release caveat | Public downloads; Git Large File Storage needed from 22.04; preserve file/run boundaries |
| Network realism | Not assessable from process-only CSV |
| Process realism | High lab/HIL value for coupled-variable analysis; not wholly physical production |
| Operational realism caveat | Labels and signal sets vary by release; avoid random row splits that leak adjacent time periods |
| Participant difficulty | Intermediate–advanced |
| Organizer effort | Intermediate |
| Build-a-thon suitability | Process-anomaly and explainable-detection track; not packet forensics |
| Adoption action | License clarification |

## Sources and provenance

[S17](../reference/sources.md#s17)

### Recorded primary addresses

- [Primary source 1](https://github.com/icsdataset/hai)

### Recorded rights addresses

- [Rights source 1](https://github.com/icsdataset/hai)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
