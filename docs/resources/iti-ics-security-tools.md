# ITI ICS-Security-Tools capture collection

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R13  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Community-assembled multi-vendor captures; lab, conformance and test-tree provenance varies by subfolder |
| Device types | Mixed: DNP3 outstations/masters, Siemens S7, Modbus TCP devices, IEC 104 and IEC 61850 endpoints, EtherNet/IP, C37.118 PMUs, PROFINET, DLMS/COSEM meters, Zigbee (per folder READMEs) |
| Protocol coverage | DNP3 (incl. OpenDNP3 3.0 conformance set), S7comm, Modbus TCP, IEC 60870-5-104, IEC 61850, EtherNet/IP/CIP, C37.118, PROFINET, DLMS-COSEM, Zigbee; OpenICS and QuickDraw parser test data |
| Protocol evidence | Folder labels and per-folder READMEs; 378 files verified as libpcap/pcapng by magic number on 2026-09-28; payloads not decoded per protocol by this catalog |
| PCAP availability | 378 capture files, 121 MB, downloadable individually over GitHub raw; no LFS |
| Other data formats | Wireshark dissector reference table, OpenDNP3 conformance report, OPC specifications, DLMS security review |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | No per-packet attack labels; some folders (QuickDraw, firewall-test DNP3) are synthetic test cases by design |
| Topology / configuration | Per-folder READMEs only; no unified topology |
| License / terms | Creative Commons Attribution 4.0 (repository LICENSE.md); individual captures may carry upstream credits noted in folder READMEs |
| Redistribution gate | Attribution / review |
| Access / release caveat | Public download; attribution required; check folder READMEs for third-party origin before redistribution |
| Network realism | Heterogeneous: some authentic lab traffic, some hand-built parser/firewall test cases |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Do not present parser test cases as production traffic; many files are minimal single-function exchanges |
| Participant difficulty | Beginner–intermediate |
| Organizer effort | Low |
| Build-a-thon suitability | Protocol dissection drills, parser and IDS signature testing, broad protocol survey |
| Adoption action | Curate & validate |

## Sources and provenance

[S31](../reference/sources.md#s31), [S32](../reference/sources.md#s32)

### Recorded primary addresses

- [Primary source 1](https://github.com/ITI/ICS-Security-Tools/tree/master/pcaps)

### Recorded rights addresses

- [Rights source 1](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/LICENSE.md)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
