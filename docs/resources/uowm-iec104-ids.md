# UOWM IEC 60870-5-104 Intrusion Detection Dataset

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Baseline imported from the 2026-09-27 research workbook. Review dates and source statements are inherited; this import did not revalidate upstream pages, inspect dataset binaries, run testbeds, or grant redistribution permission.

**Identifier:** R21  
**Record type:** Dataset / capture  
**Review status:** added_after_local_verification  
**Inherited review date:** 2026-09-28

[Catalog index](../master-matrix.md) · [Glossary](../reference/glossary.md)

## Assessment fields

| Field | Recorded assessment |
| --- | --- |
| Category | Dataset / capture |
| Sector / process | Emulated IEC 104 substation: five virtual RTUs (IEC TestServer), two physical RTUs, one MTU/HMI (QTester104), three attacker hosts |
| Device types | RTUs (virtual and physical), MTU/HMI workstation, Kali attackers |
| Protocol coverage | IEC 60870-5-104 |
| Protocol evidence | Zenodo record documents per-entity pcap plus CICFlowMeter and IEC 104 flow CSVs per attack; 13 archives MD5-verified against record; inner files not individually verified |
| PCAP availability | 12 attack archives (7z, 69 to 107 MB each) plus balanced CSV archive; Zenodo direct download |
| Other data formats | Labelled CICFlowMeter TCP/IP flow CSVs and IEC 104 flow-statistics CSVs; attack diagrams; ReadMe PDF |
| Physical-process ground truth | No physical-process measurements supplied; captures are network-only |
| Attack labels / semantics | Twelve labelled attacks: unauthorized C_CI/C_SC/C_SE/C_RD/C_RP commands, MITM drop, and six command-flood DoS variants; labels at flow level |
| Topology / configuration | Topology described in record (7 entities, HMI, 3 attackers) |
| License / terms | Creative Commons Attribution 4.0 (Zenodo record license field); citation to IEEE TII 2022 paper requested |
| Redistribution gate | Attribution / review |
| Access / release caveat | Public download; attribution and citation required |
| Network realism | Emulated RTUs with real attack tooling (Metasploit, j60870, Ettercap) |
| Process realism | No independent process truth; realism limited to protocol exchanges |
| Operational realism caveat | Two-hour and four-hour attack windows; benign share per capture not characterized here |
| Participant difficulty | Intermediate–advanced |
| Organizer effort | Intermediate |
| Build-a-thon suitability | IEC 104 command-injection and flood detection, flow-feature ML/IDS training, MITM drop analysis |
| Adoption action | Curate & validate |

## Sources and provenance

[S43](../reference/sources.md#s43)

### Recorded primary addresses

- [Primary source 1](https://zenodo.org/records/7108614)

### Recorded rights addresses

- [Rights source 1](https://zenodo.org/records/7108614)

These references preserve the earlier review trail. A catalog entry is not evidence of permission, packet-level validation, or a successfully running environment.
