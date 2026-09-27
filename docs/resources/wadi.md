# Water Distribution (WADI)

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R05  
**Record type:** Dataset / capture  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Physical water-distribution testbed |
| Device types | PLCs; remote I/O; Remote Terminal Units (RTUs); gateways; SCADA; historian; tanks, pumps and valves |
| Protocol coverage | EtherNet/IP and Modbus documented for lab; per-edition packet inventory unverified |
| Protocol evidence | Owner architecture, not evidence that every protocol appears in every release |
| PCAP availability | Confirmed for A3 December 2023, attack-free. Raw PCAP not confirmed in A1/A2 packages |
| Other data formats | Sensor/actuator CSV; 123 channels in A1; historian synchronized with A3 PCAP |
| Physical-process ground truth | Measured physical distribution process; sensor telemetry is not necessarily independent truth |
| Attack labels / semantics | A1 has 15 attacks; corrected A2 uses -1=attack, +1=normal. A3 has no attacks |
| Topology / configuration | Owner process and network diagrams; exact capture vantage and tag dictionary need release inspection |
| License / terms | Same custom iTrust terms as SWaT |
| Redistribution gate | Permission required |
| Access / release caveat | A3 alone is approximately 335 GB; never align 2017 attacks with 2023 PCAP as one incident |
| Network realism | Authentic physical-lab traffic |
| Process realism | High physical-lab fidelity |
| Operational realism caveat | Large normal-only capture is not a labeled network attack corpus |
| Participant difficulty | Advanced |
| Organizer effort | Advanced |
| Build-a-thon suitability | Baseline learning and cross-system process modeling; attacked process-only track using A1/A2 |
| Adoption action | Permission required |

## Sources and provenance

[S13](../reference/sources.md#s13), [S14](../reference/sources.md#s14), [S16](../reference/sources.md#s16), [S15](../reference/sources.md#s15)

### Recorded primary addresses

- [Primary source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/)
- [Primary source 2](https://www.sutd.edu.sg/itrust/wadi/)
- [Primary source 3](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/summary-of-available-datasets/)

### Recorded rights addresses

- [Rights source 1](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
