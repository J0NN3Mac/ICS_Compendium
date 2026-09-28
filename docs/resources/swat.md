# Secure Water Treatment (SWaT)

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R04  
**Record type:** Dataset / capture  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Six-stage physical water-treatment testbed |
| Device types | PLCs; remote Input/Output (I/O); HMI; Supervisory Control and Data Acquisition (SCADA); historian; pumps, valves and sensors |
| Protocol coverage | EtherNet/IP documented for lab; exact per-edition wire inventory still needs decoding |
| Protocol evidence | Owner testbed architecture; not a full packet-level verification |
| PCAP availability | Request-gated; A6 explicitly includes PCAP + historian. Availability varies by edition |
| Other data formats | Historian comma-separated values (CSV); labels and attack descriptions, edition-dependent |
| Physical-process ground truth | Measured laboratory telemetry; not automatically independent truth during sensor manipulation |
| Attack labels / semantics | Attack windows / labels in attacked releases; A6 has six documented attacks; December 2023 release is attack-free |
| Topology / configuration | Owner physical and network diagrams; exact per-release asset/tag mapping must be checked |
| License / terms | Custom iTrust terms; attribution, publication notice and requester disclosure |
| Redistribution gate | Permission required |
| Access / release caveat | No private or public onward sharing. A6 is a manageable candidate; newer 2026 releases need content review |
| Network realism | Authentic industrial devices and lab communications |
| Process realism | High physical-lab fidelity; scale and operating modes differ from production |
| Operational realism caveat | Do not mix release identities, attack labels or normal periods across editions |
| Participant difficulty | Intermediate–advanced |
| Organizer effort | Intermediate–advanced |
| Build-a-thon suitability | Strong integrated packet/process investigation after written team/event permission |
| Adoption action | Permission required |

## Sources and provenance

[S11](../reference/sources.md#s11), [S12](../reference/sources.md#s12), [S16](../reference/sources.md#s16), [S15](../reference/sources.md#s15)

### Recorded primary addresses

- [Primary source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/swat/)
- [Primary source 2](https://www.sutd.edu.sg/itrust/swat/)
- [Primary source 3](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/summary-of-available-datasets/)

### Recorded rights addresses

- [Rights source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
