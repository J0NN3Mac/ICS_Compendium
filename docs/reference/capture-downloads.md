# Capture download register

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Direct addresses of the packet-capture files that the catalogued resources publish. Each address was located from the resource's own landing page or repository tree and checked with a ranged HTTP GET of the first 16 bytes: the recorded status, total size and detected format come from that check. No capture is stored in this repository; see [DATA_POLICY.md](../../DATA_POLICY.md). Rerun `python3 scripts/check_links.py` to revalidate. A working link is not a redistribution permission: apply the gate in [rights and access](rights-and-access.md) before sharing any file onward.

**Provenance:** Direct capture-file addresses located on 2026-09-28 from each resource's published landing page or repository tree. Every address was checked with a ranged HTTP GET of the first 16 bytes; status, total size and the capture magic number were recorded. No file was downloaded in full, inspected packet by packet, or redistributed.

## Summary by resource

| ID | Resource | Files | Total size (MB) | Redistribution gate | Landing page |
| --- | --- | --- | --- | --- | --- |
| R07 | [IEC61850SecurityDataset](../resources/iec61850.md) | 14 | 103.6 | Permission required | [open](https://github.com/smartgridadsc/IEC61850SecurityDataset) |
| R08 | [KNX contextual datasets](../resources/knx.md) | 16 | 279.2 | Attribution / review | [open](https://github.com/vgraveto/knx-datasets) |
| R09 | [4SICS ICS Lab captures](../resources/4sics.md) | 3 | 374.9 | Attribution / review | [open](https://www.netresec.com/?page=PCAP4SICS) |
| R10 | [Digital Bond S4x15 ICS Village captures](../resources/s4x15.md) | 8 | 41.4 | Permission required | [open](https://www.netresec.com/?page=DigitalBond_S4) |

## R07 — IEC61850SecurityDataset

Host: GitHub raw (smartgridadsc/IEC61850SecurityDataset, branch master). Rights: [rights and access](rights-and-access.md) entry R07.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C12 | [Attack/CompositeAttack.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/CompositeAttack.pcapng) | Attack: composite | 7,192,780 | pcapng | 206 | 2026-09-28 |  |
| C13 | [Attack/Data Manipulation (DM)/AS1.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Data%20Manipulation%20%28DM%29/AS1.pcapng) | Attack: data manipulation AS1 | 7,477,360 | pcapng | 206 | 2026-09-28 |  |
| C14 | [Attack/Data Manipulation (DM)/AS2.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Data%20Manipulation%20%28DM%29/AS2.pcapng) | Attack: data manipulation AS2 | 7,620,760 | pcapng | 206 | 2026-09-28 |  |
| C15 | [Attack/Data Manipulation (DM)/AS3.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Data%20Manipulation%20%28DM%29/AS3.pcapng) | Attack: data manipulation AS3 | 6,323,868 | pcapng | 206 | 2026-09-28 |  |
| C16 | [Attack/Denial of Service (DoS)/AS1.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Denial%20of%20Service%20%28DoS%29/AS1.pcapng) | Attack: denial of service AS1 | 9,341,496 | pcapng | 206 | 2026-09-28 |  |
| C17 | [Attack/Message Suppression (MS)/AS1.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Message%20Suppression%20%28MS%29/AS1.pcapng) | Attack: message suppression AS1 | 7,179,740 | pcapng | 206 | 2026-09-28 |  |
| C18 | [Attack/Message Suppression (MS)/AS2.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Message%20Suppression%20%28MS%29/AS2.pcapng) | Attack: message suppression AS2 | 7,592,628 | pcapng | 206 | 2026-09-28 |  |
| C19 | [Attack/Message Suppression (MS)/AS3.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Message%20Suppression%20%28MS%29/AS3.pcapng) | Attack: message suppression AS3 | 7,824,296 | pcapng | 206 | 2026-09-28 |  |
| C20 | [Attack/Message Suppression (MS)/AS4.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Attack/Message%20Suppression%20%28MS%29/AS4.pcapng) | Attack: message suppression AS4 | 7,472,636 | pcapng | 206 | 2026-09-28 |  |
| C21 | [Disturbance/Breaker Failure/BreakFailure.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Disturbance/Breaker%20Failure/BreakFailure.pcapng) | Disturbance: breaker failure | 7,403,928 | pcapng | 206 | 2026-09-28 |  |
| C22 | [Disturbance/Busbar Protection/BusbarProtection.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Disturbance/Busbar%20Protection/BusbarProtection.pcapng) | Disturbance: busbar protection | 6,932,212 | pcapng | 206 | 2026-09-28 |  |
| C23 | [Disturbance/Under frequency/UnderFrequency.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Disturbance/Under%20frequency/UnderFrequency.pcapng) | Disturbance: under-frequency | 6,978,048 | pcapng | 206 | 2026-09-28 |  |
| C24 | [Normal/No_Variable_Loading/Normal.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Normal/No_Variable_Loading/Normal.pcapng) | Normal: no variable loading | 7,052,508 | pcapng | 206 | 2026-09-28 |  |
| C25 | [Normal/Variable_Loading/VariableLoad.pcapng](https://raw.githubusercontent.com/smartgridadsc/IEC61850SecurityDataset/master/Normal/Variable_Loading/VariableLoad.pcapng) | Normal: variable loading | 7,213,244 | pcapng | 206 | 2026-09-28 |  |

## R08 — KNX contextual datasets

Host: GitHub raw (vgraveto/knx-datasets, branch main). Rights: [rights and access](rights-and-access.md) entry R08.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C26 | [Dataset/Original/all_KNX.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/Original/all_KNX.pcapng) | Original capture | 16,714,700 | pcapng | 206 | 2026-09-28 |  |
| C27 | [Dataset/DI/all_KNX_DI.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/DI/all_KNX_DI.pcapng) | DI variant | 17,084,060 | pcapng | 206 | 2026-09-28 |  |
| C28 | [Dataset/LS/all_KNX_LS.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/LS/all_KNX_LS.pcapng) | LS variant | 16,781,468 | pcapng | 206 | 2026-09-28 |  |
| C29 | [Dataset/MI/HR/all_KNX_MI_HR.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/HR/all_KNX_MI_HR.pcapng) | MI/HR variant | 17,374,700 | pcapng | 206 | 2026-09-28 |  |
| C30 | [Dataset/IC/all_KNX_IC_decimal_1.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/IC/all_KNX_IC_decimal_1.pcapng) | IC decimal 1 | 16,881,812 | pcapng | 206 | 2026-09-28 |  |
| C31 | [Dataset/IC/all_KNX_IC_decimal_5.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/IC/all_KNX_IC_decimal_5.pcapng) | IC decimal 5 | 17,550,348 | pcapng | 206 | 2026-09-28 |  |
| C32 | [Dataset/IC/all_KNX_IC_decimal_10.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/IC/all_KNX_IC_decimal_10.pcapng) | IC decimal 10 | 18,386,084 | pcapng | 206 | 2026-09-28 |  |
| C33 | [Dataset/IC/all_KNX_IC_hexadecimal_1.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/IC/all_KNX_IC_hexadecimal_1.pcapng) | IC hexadecimal 1 | 16,881,812 | pcapng | 206 | 2026-09-28 |  |
| C34 | [Dataset/IC/all_KNX_IC_hexadecimal_5.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/IC/all_KNX_IC_hexadecimal_5.pcapng) | IC hexadecimal 5 | 17,550,348 | pcapng | 206 | 2026-09-28 |  |
| C35 | [Dataset/IC/all_KNX_IC_hexadecimal_10.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/IC/all_KNX_IC_hexadecimal_10.pcapng) | IC hexadecimal 10 | 18,386,040 | pcapng | 206 | 2026-09-28 |  |
| C36 | [Dataset/MI/SR/all_KNX_MI_SR_decimal_1.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/SR/all_KNX_MI_SR_decimal_1.pcapng) | MI/SR decimal 1 | 16,881,812 | pcapng | 206 | 2026-09-28 |  |
| C37 | [Dataset/MI/SR/all_KNX_MI_SR_decimal_5.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/SR/all_KNX_MI_SR_decimal_5.pcapng) | MI/SR decimal 5 | 17,550,392 | pcapng | 206 | 2026-09-28 |  |
| C38 | [Dataset/MI/SR/all_KNX_MI_SR_decimal_10.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/SR/all_KNX_MI_SR_decimal_10.pcapng) | MI/SR decimal 10 | 18,386,128 | pcapng | 206 | 2026-09-28 |  |
| C39 | [Dataset/MI/SR/all_KNX_MI_SR_hexadecimal_1.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/SR/all_KNX_MI_SR_hexadecimal_1.pcapng) | MI/SR hexadecimal 1 | 16,881,812 | pcapng | 206 | 2026-09-28 |  |
| C40 | [Dataset/MI/SR/all_KNX_MI_SR_hexadecimal_5.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/SR/all_KNX_MI_SR_hexadecimal_5.pcapng) | MI/SR hexadecimal 5 | 17,550,392 | pcapng | 206 | 2026-09-28 |  |
| C41 | [Dataset/MI/SR/all_KNX_MI_SR_hexadecimal_10.pcapng](https://raw.githubusercontent.com/vgraveto/knx-datasets/main/Dataset/MI/SR/all_KNX_MI_SR_hexadecimal_10.pcapng) | MI/SR hexadecimal 10 | 18,386,128 | pcapng | 206 | 2026-09-28 |  |

## R09 — 4SICS ICS Lab captures

Host: Netresec public share (Nextcloud). Rights: [rights and access](rights-and-access.md) entry R09.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | [4SICS-GeekLounge-151020.pcap](https://share.netresec.com/s/xYj2qCNbsLEAd6M/download/4SICS-GeekLounge-151020.pcap) | 4SICS Geek Lounge 2015-10-20 | 25,711,082 | pcap | 206 | 2026-09-28 |  |
| C02 | [4SICS-GeekLounge-151021.pcap](https://share.netresec.com/s/camL59aoxbCRyyZ/download/4SICS-GeekLounge-151021.pcap) | 4SICS Geek Lounge 2015-10-21 | 139,998,821 | pcap | 206 | 2026-09-28 |  |
| C03 | [4SICS-GeekLounge-151022.pcap](https://share.netresec.com/s/gw6Y2QzJHqDD5pr/download/4SICS-GeekLounge-151022.pcap) | 4SICS Geek Lounge 2015-10-22 | 209,236,002 | pcap | 206 | 2026-09-28 |  |

## R10 — Digital Bond S4x15 ICS Village captures

Host: Netresec public share (Nextcloud). Rights: [rights and access](rights-and-access.md) entry R10.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C04 | [Advantech.pcap](https://share.netresec.com/s/3jAPdoBzRsG8NLo/download/Advantech.pcap) | Advantech PLC | 40,229 | pcap | 206 | 2026-09-28 |  |
| C05 | [BACnet_FIU.pcap](https://share.netresec.com/s/At9EfzR6SKP8E8j/download/BACnet_FIU.pcap) | BACnet Internet | 10,740,128 | pcapng | 206 | 2026-09-28 | File name says .pcap but content is pcapng; use a pcapng-aware reader. |
| C06 | [BACnet_Host.pcap](https://share.netresec.com/s/D2r6eBMbHPwWD7X/download/BACnet_Host.pcap) | BACnet corporate zone | 1,827,202 | pcap | 206 | 2026-09-28 |  |
| C07 | [MicroLogix56.pcap](https://share.netresec.com/s/ikw3mbzkyx52SP9/download/MicroLogix56.pcap) | MicroLogix | 10,126,480 | pcapng | 206 | 2026-09-28 | File name says .pcap but content is pcapng; use a pcapng-aware reader. |
| C08 | [Modicon.pcap](https://share.netresec.com/s/GByJiszxbqQXCnj/download/Modicon.pcap) | Modicon PLC | 883,249 | pcap | 206 | 2026-09-28 |  |
| C09 | [WinXP.pcap](https://share.netresec.com/s/4mBsCaxMmBrHtAH/download/WinXP.pcap) | Windows XP | 3,392,686 | pcap | 206 | 2026-09-28 |  |
| C10 | [iFix_Client86.pcap](https://share.netresec.com/s/n6it55pewtQQPCt/download/iFix_Client86.pcap) | iFix client | 988,148 | pcapng | 206 | 2026-09-28 | File name says .pcap but content is pcapng; use a pcapng-aware reader. |
| C11 | [iFix_Server119.pcap](https://share.netresec.com/s/PwEtpcxTKpLBLzB/download/iFix_Server119.pcap) | iFix server | 13,451,008 | pcapng | 206 | 2026-09-28 | File name says .pcap but content is pcapng; use a pcapng-aware reader. |

