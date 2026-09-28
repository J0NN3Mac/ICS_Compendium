# OpenPLC Runtime v4

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R02  
**Record type:** Generator  
**Review status:** imported_documentation_review  
**Inherited review date:** 2026-09-27

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Generator |
| Sector / process | User-defined industrial process |
| Device types | Software PLC; physical or virtual inputs/outputs; external HMI and plant supplied by builder |
| Protocol coverage | Modbus master/slave, Open Platform Communications Unified Architecture (OPC UA), S7comm and EtherCAT plugins listed |
| Protocol evidence | Plugin manifest verified; feature support is not proof of configured, captured traffic |
| PCAP availability | Generate locally with clients and capture point |
| Other data formats | Controller variables and runtime logs; user must export |
| Physical-process ground truth | None inherent; attach a physical process or simulation |
| Attack labels / semantics | No dataset labels; event oracle must be authored |
| Topology / configuration | Runtime configuration supplied; plant network, tag map and physical model are user-defined |
| License / terms | MIT license for current runtime; editor/plugins/dependencies and legacy versions need separate checks |
| Redistribution gate | Own-output review |
| Access / release caveat | Public code; headless version 4 differs from older web-based versions |
| Network realism | Controller implementation; depends on plugin configuration and clients |
| Process realism | None standalone; entirely integration-dependent |
| Operational realism caveat | A functioning controller is not a complete operating plant |
| Participant difficulty | Intermediate |
| Organizer effort | Advanced |
| Build-a-thon suitability | Builder track for protocol clients, controller instrumentation and custom process integration |
| Adoption action | Build & validate |

## Sources and provenance

[S05](../reference/sources.md#s05), [S06](../reference/sources.md#s06), [S07](../reference/sources.md#s07)

### Recorded primary addresses

- [Primary source 1](https://github.com/Autonomy-Logic/openplc-runtime)
- [Primary source 2](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/plugins_default.conf)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/Autonomy-Logic/openplc-runtime/main/LICENSE)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
