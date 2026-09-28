# Conpot

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R03  
**Record type:** Generator  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Generator |
| Sector / process | Industrial-service emulation; generic industrial / building / utility endpoints |
| Device types | Emulated PLC or industrial service endpoints; no physical plant |
| Protocol coverage | Template-dependent Modbus, S7comm, EtherNet/IP, BACnet, IEC 60870-5-104 and meter protocols |
| Protocol evidence | Documented emulated services; do not assume full vendor stack or cyclic I/O |
| PCAP availability | Generate locally; runtime logs are not packet captures |
| Other data formats | Service interaction logs and templates |
| Physical-process ground truth | No physical-process ground truth out of the box |
| Attack labels / semantics | No inherent validated attack labels; requests and service logs need interpretation |
| Topology / configuration | Endpoint templates supplied; multi-host topology is user-built |
| License / terms | GNU General Public License version 2 (GPL-2.0) repository |
| Redistribution gate | Own-output review |
| Access / release caveat | Public code; capture only authorized isolated-lab interactions |
| Network realism | Useful endpoint/service behavior; limited fidelity compared with real controllers |
| Process realism | Low: no causal process model |
| Operational realism caveat | Not suitable alone as a clean, authentic production baseline |
| Participant difficulty | Beginner–intermediate |
| Organizer effort | Intermediate |
| Build-a-thon suitability | Introductory discovery, parsing and service-fingerprinting track |
| Adoption action | Build & validate |

## Sources and provenance

[S08](../reference/sources.md#s08), [S09](../reference/sources.md#s09), [S10](../reference/sources.md#s10)

### Recorded primary addresses

- [Primary source 1](https://github.com/mushorg/conpot)
- [Primary source 2](https://conpot.readthedocs.io/en/latest/)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/mushorg/conpot/main/LICENSE.txt)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
