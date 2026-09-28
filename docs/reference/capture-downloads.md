# Capture download register

> Generated from `catalog/`. Edit the canonical records, then run `python3 scripts/generate.py`.

Direct addresses of the packet-capture files and capture archives that the catalogued resources publish. Each address was located from the resource's own landing page or repository tree and checked with a ranged HTTP GET of the first 16 bytes or by full download: the recorded status, total size and detected format come from that check. Archive entries (zip, 7z) and gzip-wrapped files must be unpacked to obtain captures. No capture is stored in this repository; see [DATA_POLICY.md](../../DATA_POLICY.md). Rerun `python3 scripts/check_links.py` to revalidate. A working link is not a redistribution permission: apply the gate in [rights and access](rights-and-access.md) before sharing any file onward.

**Provenance:** Direct capture-file addresses located on 2026-09-28 from each resource's published landing page or repository tree. Every address was checked with a ranged HTTP GET of the first 16 bytes; status, total size and the capture magic number were recorded. No file was downloaded in full, inspected packet by packet, or redistributed. Entries C42 onward (added 2026-09-28) were verified by full download: size compared to the upstream tree or record, capture magic number checked, and SHA-256 recorded locally; archives were integrity-tested (zip) or MD5-matched to the publisher (7z).

## Summary by resource

| ID | Resource | Files | Total size (MB) | Redistribution gate | Landing page |
| --- | --- | --- | --- | --- | --- |
| R07 | [IEC61850SecurityDataset](../resources/iec61850.md) | 14 | 103.6 | Permission required | [open](https://github.com/smartgridadsc/IEC61850SecurityDataset) |
| R08 | [KNX contextual datasets](../resources/knx.md) | 16 | 279.2 | Attribution / review | [open](https://github.com/vgraveto/knx-datasets) |
| R09 | [4SICS ICS Lab captures](../resources/4sics.md) | 3 | 374.9 | Attribution / review | [open](https://www.netresec.com/?page=PCAP4SICS) |
| R10 | [Digital Bond S4x15 ICS Village captures](../resources/s4x15.md) | 8 | 41.4 | Permission required | [open](https://www.netresec.com/?page=DigitalBond_S4) |
| R13 | [ITI ICS-Security-Tools capture collection](../resources/iti-ics-security-tools.md) | 378 | 121.0 | Attribution / review | [open](https://github.com/ITI/ICS-Security-Tools) |
| R14 | [Lemay & Fernandez Modbus dataset (CSET 2016)](../resources/lemay-cset2016-modbus.md) | 11 | 84.5 | Permission required | [open](https://github.com/antoine-lemay/Modbus_dataset) |
| R15 | [gymgit S7comm client/PLC captures](../resources/gymgit-s7-pcaps.md) | 21 | 29.2 | Attribution / review | [open](https://github.com/gymgit/s7-pcaps) |
| R16 | [EmreEkin ICS-Pcaps protocol sampler](../resources/emreekin-ics-pcaps.md) | 241 | 274.3 | Permission required | [open](https://github.com/EmreEkin/ICS-Pcaps) |
| R17 | [ICS CTF traffic (Modbus/TCP and S7comm)](../resources/ctf-ics-traffic.md) | 1 | 48.6 | Permission required | [open](https://github.com/NewBee119/ctf_ics_traffic) |
| R18 | [ControlThings ct-samples protocol captures](../resources/controlthings-ct-samples.md) | 111 | 205.3 | Attribution / review | [open](https://github.com/ControlThings-io/ct-samples) |
| R19 | [Nozomi tricotools TRITON/TriStation capture](../resources/nozomi-tricotools-triton.md) | 1 | 0.2 | Attribution / review | [open](https://github.com/NozomiNetworks/tricotools) |
| R20 | [University of Coimbra ICS_PCAPS MODBUSTCP#1](../resources/coimbra-modbustcp1.md) | 3 | 1088.5 | Permission required | [open](https://github.com/tjcruz-dei/ICS_PCAPS/releases/tag/MODBUSTCP%231) |
| R21 | [UOWM IEC 60870-5-104 Intrusion Detection Dataset](../resources/uowm-iec104-ids.md) | 13 | 1086.8 | Attribution / review | [open](https://zenodo.org/records/7108614) |

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

## R13 — ITI ICS-Security-Tools capture collection

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R13.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C42 | [bro/modbus/fuzz-72.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/modbus/fuzz-72.pcap) | bro | 2,907 | pcap | 200 | 2026-09-28 |  |
| C43 | [bro/modbus/modbusSmall.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/modbus/modbusSmall.pcap) | bro | 14,878 | pcap | 200 | 2026-09-28 |  |
| C44 | [bro/modbus/modbusBig.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/modbus/modbusBig.pcap) | bro | 1,188,656 | pcap | 200 | 2026-09-28 |  |
| C45 | [bro/modbus/modbus.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/modbus/modbus.pcap) | bro | 9,297,319 | pcap | 200 | 2026-09-28 |  |
| C46 | [bro/modbus/fuzz-1011.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/modbus/fuzz-1011.pcap) | bro | 1,167 | pcap | 200 | 2026-09-28 |  |
| C47 | [bro/dnp3/dnp3_del_measure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_del_measure.pcap) | bro | 804 | pcap | 200 | 2026-09-28 |  |
| C48 | [bro/dnp3/dnp3_write.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_write.pcap) | bro | 808 | pcap | 200 | 2026-09-28 |  |
| C49 | [bro/dnp3/dnp3.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3.pcap) | bro | 18,790 | pcap | 200 | 2026-09-28 |  |
| C50 | [bro/dnp3/dnp3_rec_time.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_rec_time.pcap) | bro | 798 | pcap | 200 | 2026-09-28 |  |
| C51 | [bro/dnp3/dnp3_file_del.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_file_del.pcap) | bro | 920 | pcap | 200 | 2026-09-28 |  |
| C52 | [bro/dnp3/dnp3_file_write.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_file_write.pcap) | bro | 2,868 | pcap | 200 | 2026-09-28 |  |
| C53 | [bro/dnp3/dnp3_read.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_read.pcap) | bro | 928 | pcap | 200 | 2026-09-28 |  |
| C54 | [bro/dnp3/dnp3_read_p20001.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_read_p20001.pcap) | bro | 928 | pcap | 200 | 2026-09-28 |  |
| C55 | [bro/dnp3/dnp3_select_operate.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_select_operate.pcap) | bro | 1,120 | pcap | 200 | 2026-09-28 |  |
| C56 | [bro/dnp3/dnp3_en_spon.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_en_spon.pcap) | bro | 807 | pcap | 200 | 2026-09-28 |  |
| C57 | [bro/dnp3/dnp3_link_only.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_link_only.pcap) | bro | 6,907 | pcap | 200 | 2026-09-28 |  |
| C58 | [bro/dnp3/dnp3_file_read.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/bro/dnp3/dnp3_file_read.pcap) | bro | 3,489 | pcap | 200 | 2026-09-28 |  |
| C59 | [IEC61850/piccolo.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/piccolo.pcap) | IEC61850 | 838 | pcap | 200 | 2026-09-28 |  |
| C60 | [IEC61850/m-send-req.mms.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/m-send-req.mms.pcap) | IEC61850 | 24,777 | pcap | 200 | 2026-09-28 |  |
| C61 | [IEC61850/8d7c7db0-9804-012b-b2a6-0016cb8cea27.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/8d7c7db0-9804-012b-b2a6-0016cb8cea27.pcap) | IEC61850 | 54,287 | pcap | 200 | 2026-09-28 |  |
| C62 | [IEC61850/Sample_File_MMS_and_GOOSE.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/Sample_File_MMS_and_GOOSE.pcap) | IEC61850 | 43,379 | pcap | 200 | 2026-09-28 |  |
| C63 | [IEC61850/MMS - Specific Commands/mms-resumeRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-resumeRequest.pcap) | IEC61850 | 1,577 | pcap | 200 | 2026-09-28 |  |
| C64 | [IEC61850/MMS - Specific Commands/iec61850_read.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/iec61850_read.pcap) | IEC61850 | 1,915 | pcap | 200 | 2026-09-28 |  |
| C65 | [IEC61850/MMS - Specific Commands/mms-confirmedRequestPDU.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-confirmedRequestPDU.pcap) | IEC61850 | 1,548 | pcap | 200 | 2026-09-28 |  |
| C66 | [IEC61850/MMS - Specific Commands/mms-killRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-killRequest.pcap) | IEC61850 | 1,577 | pcap | 200 | 2026-09-28 |  |
| C67 | [IEC61850/MMS - Specific Commands/iec61850_get_name_list.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/iec61850_get_name_list.pcap) | IEC61850 | 1,905 | pcap | 200 | 2026-09-28 |  |
| C68 | [IEC61850/MMS - Specific Commands/mms-initiateDownloadSequence.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-initiateDownloadSequence.pcap) | IEC61850 | 1,905 | pcap | 200 | 2026-09-28 |  |
| C69 | [IEC61850/MMS - Specific Commands/mms-deleteProgramInvocation.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-deleteProgramInvocation.pcap) | IEC61850 | 1,576 | pcap | 200 | 2026-09-28 |  |
| C70 | [IEC61850/MMS - Specific Commands/iec61850_release.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/iec61850_release.pcap) | IEC61850 | 1,568 | pcap | 200 | 2026-09-28 |  |
| C71 | [IEC61850/MMS - Specific Commands/iec61850_get_variable_access_attributes.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/iec61850_get_variable_access_attributes.pcap) | IEC61850 | 1,902 | pcap | 200 | 2026-09-28 |  |
| C72 | [IEC61850/MMS - Specific Commands/mms-startRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-startRequest.pcap) | IEC61850 | 1,906 | pcap | 200 | 2026-09-28 |  |
| C73 | [IEC61850/MMS - Specific Commands/mms-initiateUploadSequence.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-initiateUploadSequence.pcap) | IEC61850 | 1,572 | pcap | 200 | 2026-09-28 |  |
| C74 | [IEC61850/MMS - Specific Commands/mms-resetRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-resetRequest.pcap) | IEC61850 | 1,577 | pcap | 200 | 2026-09-28 |  |
| C75 | [IEC61850/MMS - Specific Commands/mms-cancelRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-cancelRequest.pcap) | IEC61850 | 1,546 | pcap | 200 | 2026-09-28 |  |
| C76 | [IEC61850/MMS - Specific Commands/mms-terminateUploadSequence.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-terminateUploadSequence.pcap) | IEC61850 | 1,884 | pcap | 200 | 2026-09-28 |  |
| C77 | [IEC61850/MMS - Specific Commands/mms-getAlarmSummary.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-getAlarmSummary.pcap) | IEC61850 | 1,557 | pcap | 200 | 2026-09-28 |  |
| C78 | [IEC61850/MMS - Specific Commands/iec61850_write.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/iec61850_write.pcap) | IEC61850 | 1,913 | pcap | 200 | 2026-09-28 |  |
| C79 | [IEC61850/MMS - Specific Commands/mms-stopRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-stopRequest.pcap) | IEC61850 | 1,906 | pcap | 200 | 2026-09-28 |  |
| C80 | [IEC61850/MMS - Specific Commands/mms-getDomainAttributes.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-getDomainAttributes.pcap) | IEC61850 | 1,568 | pcap | 200 | 2026-09-28 |  |
| C81 | [IEC61850/MMS - Specific Commands/mms-relinquishControl.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-relinquishControl.pcap) | IEC61850 | 1,881 | pcap | 200 | 2026-09-28 |  |
| C82 | [IEC61850/MMS - Specific Commands/mms-takeControl.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-takeControl.pcap) | IEC61850 | 1,881 | pcap | 200 | 2026-09-28 |  |
| C83 | [IEC61850/MMS - Specific Commands/mms-readRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/MMS%20-%20Specific%20Commands/mms-readRequest.pcap) | IEC61850 | 1,277 | pcap | 200 | 2026-09-28 |  |
| C84 | [IEC61850/GOOSE/GOOSE.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/GOOSE/GOOSE.pcap) | IEC61850 | 1,420 | pcap | 200 | 2026-09-28 |  |
| C85 | [IEC61850/GOOSE/GOOSE_DEMO.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/GOOSE/GOOSE_DEMO.pcap) | IEC61850 | 166 | pcap | 200 | 2026-09-28 |  |
| C86 | [IEC61850/GOOSE/Sample_File_GOOSE.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC61850/GOOSE/Sample_File_GOOSE.pcap) | IEC61850 | 117,736 | pcap | 200 | 2026-09-28 |  |
| C87 | [modicon/modicon_test.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/modicon/modicon_test.pcap) | modicon | 32,126 | pcap | 200 | 2026-09-28 |  |
| C88 | [quickdraw/CL5000EIP-Software Upload Failure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Software%20Upload%20Failure.pcap) | quickdraw | 15,878 | pcap | 200 | 2026-09-28 |  |
| C89 | [quickdraw/CL5000EIP-Change Port Configuration Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Change%20Port%20Configuration%20Attempt.pcap) | quickdraw | 4,094,337 | pcap | 200 | 2026-09-28 |  |
| C90 | [quickdraw/dnp3_test_data_part2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/dnp3_test_data_part2.pcap) | quickdraw | 2,976 | pcap | 200 | 2026-09-28 |  |
| C91 | [quickdraw/CL5000EIP-Software Download.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Software%20Download.pcap) | quickdraw | 147,121 | pcap | 200 | 2026-09-28 |  |
| C92 | [quickdraw/modbus_test_data_part2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/modbus_test_data_part2.pcap) | quickdraw | 27,764 | pcap | 200 | 2026-09-28 |  |
| C93 | [quickdraw/CL5000EIP-Change Time Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Change%20Time%20Attempt.pcap) | quickdraw | 115,764 | pcap | 200 | 2026-09-28 |  |
| C94 | [quickdraw/CL5000EIP-Firmware Change Failure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Firmware%20Change%20Failure.pcap) | quickdraw | 3,101,211 | pcap | 200 | 2026-09-28 |  |
| C95 | [quickdraw/CL5000EIP-Unlock PLC Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Unlock%20PLC%20Attempt.pcap) | quickdraw | 1,132,704 | pcap | 200 | 2026-09-28 |  |
| C96 | [quickdraw/CL5000EIP-Firmware Change.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Firmware%20Change.pcap) | quickdraw | 3,114,279 | pcap | 200 | 2026-09-28 |  |
| C97 | [quickdraw/CL5000EIP-Change Date Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Change%20Date%20Attempt.pcap) | quickdraw | 57,778 | pcap | 200 | 2026-09-28 |  |
| C98 | [quickdraw/CL5000EIP-Remote Mode Change Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Remote%20Mode%20Change%20Attempt.pcap) | quickdraw | 130,854 | pcap | 200 | 2026-09-28 |  |
| C99 | [quickdraw/CL5000EIP-Software Download Failure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Software%20Download%20Failure.pcap) | quickdraw | 7,333 | pcap | 200 | 2026-09-28 |  |
| C100 | [quickdraw/CL5000EIP-Software Upload.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Software%20Upload.pcap) | quickdraw | 129,648 | pcap | 200 | 2026-09-28 |  |
| C101 | [quickdraw/CL5000EIP-Reboot or Restart.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Reboot%20or%20Restart.pcap) | quickdraw | 147,121 | pcap | 200 | 2026-09-28 |  |
| C102 | [quickdraw/CL5000EIP-Lock PLC Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Lock%20PLC%20Attempt.pcap) | quickdraw | 1,132,704 | pcap | 200 | 2026-09-28 |  |
| C103 | [quickdraw/CL5000EIP-View Device Status.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-View%20Device%20Status.pcap) | quickdraw | 2,389 | pcap | 200 | 2026-09-28 |  |
| C104 | [quickdraw/CL5000EIP-IP Address Change Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-IP%20Address%20Change%20Attempt.pcap) | quickdraw | 2,078,478 | pcap | 200 | 2026-09-28 |  |
| C105 | [quickdraw/CL5000EIP-Control Protocol Change Attempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/CL5000EIP-Control%20Protocol%20Change%20Attempt.pcap) | quickdraw | 663,995 | pcap | 200 | 2026-09-28 |  |
| C106 | [quickdraw/modbus_test_data_part1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/modbus_test_data_part1.pcap) | quickdraw | 10,181 | pcap | 200 | 2026-09-28 |  |
| C107 | [quickdraw/dnp3_test_data_part1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/quickdraw/dnp3_test_data_part1.pcap) | quickdraw | 15,838 | pcap | 200 | 2026-09-28 |  |
| C108 | [openics/MODBUS-TestDataPart1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/MODBUS-TestDataPart1.pcap) | openics | 10,181 | pcap | 200 | 2026-09-28 |  |
| C109 | [openics/EIP-LockPLCAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-LockPLCAttempt.pcap) | openics | 1,132,704 | pcap | 200 | 2026-09-28 |  |
| C110 | [openics/DNP3-SelectOperate.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-SelectOperate.pcap) | openics | 936 | pcap | 200 | 2026-09-28 |  |
| C111 | [openics/DNP3-TestDataPart1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-TestDataPart1.pcap) | openics | 15,838 | pcap | 200 | 2026-09-28 |  |
| C112 | [openics/DNP3-WriteRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-WriteRequest.pcap) | openics | 962 | pcap | 200 | 2026-09-28 |  |
| C113 | [openics/DNP3-Write.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-Write.pcap) | openics | 610 | pcap | 200 | 2026-09-28 |  |
| C114 | [openics/EIP-ControlProtocolChangeAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-ControlProtocolChangeAttempt.pcap) | openics | 663,995 | pcap | 200 | 2026-09-28 |  |
| C115 | [openics/EIP-SoftwareDownloadFailure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-SoftwareDownloadFailure.pcap) | openics | 7,333 | pcap | 200 | 2026-09-28 |  |
| C116 | [openics/EIP-IPAddressChangeAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-IPAddressChangeAttempt.pcap) | openics | 2,078,478 | pcap | 200 | 2026-09-28 |  |
| C117 | [openics/EIP-RebootorRestart.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-RebootorRestart.pcap) | openics | 147,121 | pcap | 200 | 2026-09-28 |  |
| C118 | [openics/EIP-ChangePortConfigurationAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-ChangePortConfigurationAttempt.pcap) | openics | 4,094,337 | pcap | 200 | 2026-09-28 |  |
| C119 | [openics/EIP-ViewDeviceStatus.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-ViewDeviceStatus.pcap) | openics | 2,389 | pcap | 200 | 2026-09-28 |  |
| C120 | [openics/EIP-UnlockPLCAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-UnlockPLCAttempt.pcap) | openics | 1,132,704 | pcap | 200 | 2026-09-28 |  |
| C121 | [openics/EIP-SoftwareUpload.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-SoftwareUpload.pcap) | openics | 129,648 | pcap | 200 | 2026-09-28 |  |
| C122 | [openics/DNP3-RequestLink.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-RequestLink.pcap) | openics | 880 | pcap | 200 | 2026-09-28 |  |
| C123 | [openics/EIP-FirmwareChangeFailure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-FirmwareChangeFailure.pcap) | openics | 3,101,211 | pcap | 200 | 2026-09-28 |  |
| C124 | [openics/DNP3-Malformed.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-Malformed.pcap) | openics | 21,136 | pcap | 200 | 2026-09-28 |  |
| C125 | [openics/DNP3-Read.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-Read.pcap) | openics | 603 | pcap | 200 | 2026-09-28 |  |
| C126 | [openics/EIP-RemoteModeChangeAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-RemoteModeChangeAttempt.pcap) | openics | 130,854 | pcap | 200 | 2026-09-28 |  |
| C127 | [openics/EIP-FirmwareChange.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-FirmwareChange.pcap) | openics | 3,114,279 | pcap | 200 | 2026-09-28 |  |
| C128 | [openics/EIP-SoftwareUploadFailure.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-SoftwareUploadFailure.pcap) | openics | 15,878 | pcap | 200 | 2026-09-28 |  |
| C129 | [openics/DNP3-RequestLinkStatus.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-RequestLinkStatus.pcap) | openics | 604 | pcap | 200 | 2026-09-28 |  |
| C130 | [openics/EIP-ChangeTimeAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-ChangeTimeAttempt.pcap) | openics | 115,764 | pcap | 200 | 2026-09-28 |  |
| C131 | [openics/DNP3-ReadRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-ReadRequest.pcap) | openics | 1,096 | pcap | 200 | 2026-09-28 |  |
| C132 | [openics/EIP-ChangeDateAttempt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-ChangeDateAttempt.pcap) | openics | 57,778 | pcap | 200 | 2026-09-28 |  |
| C133 | [openics/EIP-SoftwareDownload.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/EIP-SoftwareDownload.pcap) | openics | 147,121 | pcap | 200 | 2026-09-28 |  |
| C134 | [openics/DNP3-TestDataPart2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-TestDataPart2.pcap) | openics | 2,976 | pcap | 200 | 2026-09-28 |  |
| C135 | [openics/DNP3-SelectOperateRequest.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/DNP3-SelectOperateRequest.pcap) | openics | 880 | pcap | 200 | 2026-09-28 |  |
| C136 | [openics/MODBUS-TestDataPart2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/openics/MODBUS-TestDataPart2.pcap) | openics | 27,764 | pcap | 200 | 2026-09-28 |  |
| C137 | [OPC/opc-ua-ap-method-wireshark-freeze.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/OPC/opc-ua-ap-method-wireshark-freeze.pcap) | OPC | 46,516 | pcap | 200 | 2026-09-28 |  |
| C138 | [C37.118/C37.118_2PMUsInSync_TCP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37.118_2PMUsInSync_TCP.pcap) | C37.118 | 476,901 | pcap | 200 | 2026-09-28 |  |
| C139 | [C37.118/C37.118_1PMU_TCP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37.118_1PMU_TCP.pcap) | C37.118 | 48,034 | pcap | 200 | 2026-09-28 |  |
| C140 | [C37.118/C37.118_1PMU_UDP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37.118_1PMU_UDP.pcap) | C37.118 | 38,496 | pcap | 200 | 2026-09-28 |  |
| C141 | [C37.118/C37.118_4in1PMU_TCP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37.118_4in1PMU_TCP.pcap) | C37.118 | 691,380 | pcap | 200 | 2026-09-28 |  |
| C142 | [C37.118/C37118/c37_1100_clean_tcp.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37118/c37_1100_clean_tcp.pcap) | C37.118 | 103,638 | pcap | 200 | 2026-09-28 |  |
| C143 | [C37.118/C37118/c37_pmu_unclean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37118/c37_pmu_unclean.pcap) | C37.118 | 1,047,452 | pcap | 200 | 2026-09-28 |  |
| C144 | [C37.118/C37118/c37_pmu_clean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37118/c37_pmu_clean.pcap) | C37.118 | 1,027,958 | pcap | 200 | 2026-09-28 |  |
| C145 | [C37.118/C37118/c37118_1100_unclean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37118/c37118_1100_unclean.pcap) | C37.118 | 339,269 | pcap | 200 | 2026-09-28 |  |
| C146 | [C37.118/C37118/c37_1100_fullclean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/C37.118/C37118/c37_1100_fullclean.pcap) | C37.118 | 83,308 | pcap | 200 | 2026-09-28 |  |
| C147 | [fox/fox_info.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/fox/fox_info.pcap) | fox | 1,954 | pcap | 200 | 2026-09-28 |  |
| C148 | [ModbusTCP/modbus_test_data_part2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/ModbusTCP/modbus_test_data_part2.pcap) | ModbusTCP | 27,764 | pcap | 200 | 2026-09-28 |  |
| C149 | [ModbusTCP/mb2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/ModbusTCP/mb2.pcap) | ModbusTCP | 1,965,376 | pcap | 200 | 2026-09-28 |  |
| C150 | [ModbusTCP/ModbusTCP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/ModbusTCP/ModbusTCP.pcap) | ModbusTCP | 1,478,608 | pcap | 200 | 2026-09-28 |  |
| C151 | [ModbusTCP/modbus_test_data_part1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/ModbusTCP/modbus_test_data_part1.pcap) | ModbusTCP | 10,181 | pcap | 200 | 2026-09-28 |  |
| C152 | [ModbusTCP/Modbus/modbus_test_2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/ModbusTCP/Modbus/modbus_test_2.pcap) | ModbusTCP | 421,622 | pcap | 200 | 2026-09-28 |  |
| C153 | [ModbusTCP/Modbus/modbus_test.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/ModbusTCP/Modbus/modbus_test.pcap) | ModbusTCP | 197,847 | pcap | 200 | 2026-09-28 |  |
| C154 | [BACnet/bacnet_test.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/BACnet/bacnet_test.pcap) | BACnet | 1,956 | pcap | 200 | 2026-09-28 |  |
| C155 | [profinet/Profinet_Failed.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/profinet/Profinet_Failed.pcap) | profinet | 8,965 | pcap | 200 | 2026-09-28 |  |
| C156 | [profinet/profinet.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/profinet/profinet.pcap) | profinet | 572 | pcap | 200 | 2026-09-28 |  |
| C157 | [profinet/profinet-wireshark-bug.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/profinet/profinet-wireshark-bug.pcap) | profinet | 450 | pcap | 200 | 2026-09-28 |  |
| C158 | [profinet/PROFINET-RT-DCP/PROFINET-RT.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/profinet/PROFINET-RT-DCP/PROFINET-RT.pcap) | profinet | 1,032 | pcap | 200 | 2026-09-28 |  |
| C159 | [profinet/PROFINET-RT-DCP/ChangeIPUsingDCP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/profinet/PROFINET-RT-DCP/ChangeIPUsingDCP.pcap) | profinet | 532 | pcap | 200 | 2026-09-28 |  |
| C160 | [IEC60870-5-104/090813_diverse.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC60870-5-104/090813_diverse.pcap) | IEC60870-5-104 | 13,952 | pcap | 200 | 2026-09-28 |  |
| C161 | [IEC60870-5-104/JavaRMI_and_IEC_Misc.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC60870-5-104/JavaRMI_and_IEC_Misc.pcap) | IEC60870-5-104 | 28,889 | pcap | 200 | 2026-09-28 |  |
| C162 | [IEC60870-5-104/TestDissectIec104.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/IEC60870-5-104/TestDissectIec104.pcap) | IEC60870-5-104 | 11,409 | pcap | 200 | 2026-09-28 |  |
| C163 | [CIP/cip_only.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/CIP/cip_only.pcap) | CIP | 2,721,649 | pcap | 200 | 2026-09-28 |  |
| C164 | [CIP/cip_unclean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/CIP/cip_unclean.pcap) | CIP | 5,710,324 | pcap | 200 | 2026-09-28 |  |
| C165 | [EthernetIP/cip-multiple-1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/cip-multiple-1.pcap) | EthernetIP | 304 | pcap | 200 | 2026-09-28 |  |
| C166 | [EthernetIP/enip_test.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/enip_test.pcap) | EthernetIP | 925 | pcap | 200 | 2026-09-28 |  |
| C167 | [EthernetIP/cip_start_plc.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/cip_start_plc.pcap) | EthernetIP | 146 | pcap | 200 | 2026-09-28 |  |
| C168 | [EthernetIP/cip-eth-set-2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/cip-eth-set-2.pcap) | EthernetIP | 138 | pcap | 200 | 2026-09-28 |  |
| C169 | [EthernetIP/cip_stop_plc.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/cip_stop_plc.pcap) | EthernetIP | 146 | pcap | 200 | 2026-09-28 |  |
| C170 | [EthernetIP/cip-multiple-2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/cip-multiple-2.pcap) | EthernetIP | 387 | pcap | 200 | 2026-09-28 |  |
| C171 | [EthernetIP/cip_unlock_cpu.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/cip_unlock_cpu.pcap) | EthernetIP | 150 | pcap | 200 | 2026-09-28 |  |
| C172 | [EthernetIP/EthernetIP-CIP.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/EthernetIP/EthernetIP-CIP.pcap) | EthernetIP | 2,084,906 | pcap | 200 | 2026-09-28 |  |
| C173 | [MELSEC/melsoft_variant_clean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_variant_clean.pcap) | MELSEC | 3,454,610 | pcap | 200 | 2026-09-28 |  |
| C174 | [MELSEC/melsoft_tcp_2_159_pkt.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_tcp_2_159_pkt.pcap) | MELSEC | 6,435,431 | pcap | 200 | 2026-09-28 |  |
| C175 | [MELSEC/melsoft_UDP_clean_3.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_UDP_clean_3.pcap) | MELSEC | 403,399 | pcap | 200 | 2026-09-28 |  |
| C176 | [MELSEC/melsoft_UDP_clean_2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_UDP_clean_2.pcap) | MELSEC | 71,702 | pcap | 200 | 2026-09-28 |  |
| C177 | [MELSEC/melsoft_UDP_unclean_1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_UDP_unclean_1.pcap) | MELSEC | 483,274 | pcap | 200 | 2026-09-28 |  |
| C178 | [MELSEC/melsoft_test.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_test.pcap) | MELSEC | 5,976,923 | pcap | 200 | 2026-09-28 |  |
| C179 | [MELSEC/melsoft_UDP_clean_1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_UDP_clean_1.pcap) | MELSEC | 403,399 | pcap | 200 | 2026-09-28 |  |
| C180 | [MELSEC/melsoft_129_clean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/MELSEC/melsoft_129_clean.pcap) | MELSEC | 331,776 | pcap | 200 | 2026-09-28 |  |
| C181 | [s7/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync_FehlerbeiMW100.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync_FehlerbeiMW100.pcapng) | s7 | 18,488 | pcapng | 200 | 2026-09-28 |  |
| C182 | [s7/snap7_s300_everything.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/snap7_s300_everything.pcapng) | s7 | 8,260 | pcap | 200 | 2026-09-28 |  |
| C183 | [s7/wincc_s300_setup-alarm-read_2.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/wincc_s300_setup-alarm-read_2.pcapng) | s7 | 63,830 | pcap | 200 | 2026-09-28 |  |
| C184 | [s7/tia_s300_updateFirmware_2.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/tia_s300_updateFirmware_2.pcapng) | s7 | 14,266,140 | pcap | 200 | 2026-09-28 |  |
| C185 | [s7/S7-1511-opc-request-all-types.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7-1511-opc-request-all-types.pcap) | s7 | 10,270 | pcap | 200 | 2026-09-28 |  |
| C186 | [s7/tia_s300_goOnline.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/tia_s300_goOnline.pcapng) | s7 | 62,240 | pcap | 200 | 2026-09-28 |  |
| C187 | [s7/s7-1200-hmi.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7-1200-hmi.pcap) | s7 | 11,559 | pcap | 200 | 2026-09-28 |  |
| C188 | [s7/S7-1511_db3_var1_HMI.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7-1511_db3_var1_HMI.pcap) | s7 | 7,334 | pcap | 200 | 2026-09-28 |  |
| C189 | [s7/s7comm_reading_setting_plc_time.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7comm_reading_setting_plc_time.pcap) | s7 | 5,355 | pcap | 200 | 2026-09-28 |  |
| C190 | [s7/s7comm_downloading_block_db1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7comm_downloading_block_db1.pcap) | s7 | 9,523 | pcap | 200 | 2026-09-28 |  |
| C191 | [s7/step7_s300_stop.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_stop.pcapng) | s7 | 431 | pcap | 200 | 2026-09-28 |  |
| C192 | [s7/step7_s300_readDiagData.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_readDiagData.pcapng) | s7 | 73,759 | pcap | 200 | 2026-09-28 |  |
| C193 | [s7/step7_s300_copyRamToRom.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_copyRamToRom.pcapng) | s7 | 219 | pcap | 200 | 2026-09-28 |  |
| C194 | [s7/s7comm_program_blocklist_onlineview.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7comm_program_blocklist_onlineview.pcap) | s7 | 13,981 | pcap | 200 | 2026-09-28 |  |
| C195 | [s7/wincc_s300_setup-alarm-read.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/wincc_s300_setup-alarm-read.pcapng) | s7 | 24,442 | pcap | 200 | 2026-09-28 |  |
| C196 | [s7/tia_s300_updateFirmware.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/tia_s300_updateFirmware.pcapng) | s7 | 14,266,140 | pcap | 200 | 2026-09-28 |  |
| C197 | [s7/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync.pcapng) | s7 | 19,948 | pcapng | 200 | 2026-09-28 |  |
| C198 | [s7/tia_s300_flashLed.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/tia_s300_flashLed.pcapng) | s7 | 484 | pcap | 200 | 2026-09-28 |  |
| C199 | [s7/snap7_s300_readVar.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/snap7_s300_readVar.pcapng) | s7 | 220 | pcap | 200 | 2026-09-28 |  |
| C200 | [s7/step7_s300_download.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_download.pcapng) | s7 | 13,005 | pcap | 200 | 2026-09-28 |  |
| C201 | [s7/snap7_s300_stop.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/snap7_s300_stop.pcapng) | s7 | 217 | pcap | 200 | 2026-09-28 |  |
| C202 | [s7/s7comm_varservice_libnodavedemo.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7comm_varservice_libnodavedemo.pcap) | s7 | 2,846 | pcap | 200 | 2026-09-28 |  |
| C203 | [s7/snap7_s300_setupCommunication.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/snap7_s300_setupCommunication.pcapng) | s7 | 216 | pcap | 200 | 2026-09-28 |  |
| C204 | [s7/step7_s300_readVarTab.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_readVarTab.pcapng) | s7 | 56,508 | pcap | 200 | 2026-09-28 |  |
| C205 | [s7/wincc_s300_setup-alarm-read-write.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/wincc_s300_setup-alarm-read-write.pcapng) | s7 | 21,368 | pcap | 200 | 2026-09-28 |  |
| C206 | [s7/S7-1511_db2_var1_HMI.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7-1511_db2_var1_HMI.pcap) | s7 | 6,024 | pcapng | 200 | 2026-09-28 |  |
| C207 | [s7/step7_s300_rwVarTab.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_rwVarTab.pcapng) | s7 | 2,638 | pcap | 200 | 2026-09-28 |  |
| C208 | [s7/wincc_s400_production.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/wincc_s400_production.pcapng) | s7 | 294,072 | pcap | 200 | 2026-09-28 |  |
| C209 | [s7/tia_s300_downloadOb1.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/tia_s300_downloadOb1.pcapng) | s7 | 14,297 | pcap | 200 | 2026-09-28 |  |
| C210 | [s7/tia_s300_downloadHwConfig.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/tia_s300_downloadHwConfig.pcapng) | s7 | 18,792 | pcap | 200 | 2026-09-28 |  |
| C211 | [s7/S7-1511_db6w0_HMI.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7-1511_db6w0_HMI.pcap) | s7 | 3,396 | pcapng | 200 | 2026-09-28 |  |
| C212 | [s7/S7-1200-Uploading-OB1-TIAV12.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7-1200-Uploading-OB1-TIAV12.pcap) | s7 | 19,895 | pcap | 200 | 2026-09-28 |  |
| C213 | [s7/step7_s300_AuthPassword.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/step7_s300_AuthPassword.pcapng) | s7 | 722 | pcap | 200 | 2026-09-28 |  |
| C214 | [s7/s7comm_reading_plc_status.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7comm_reading_plc_status.pcap) | s7 | 25,112 | pcap | 200 | 2026-09-28 |  |
| C215 | [s7/s7comm_varservice_libnodavedemo_bench.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/s7comm_varservice_libnodavedemo_bench.pcap) | s7 | 1,566,710 | pcap | 200 | 2026-09-28 |  |
| C216 | [s7/S7Comm/wrapup.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7Comm/wrapup.pcapng) | s7 | 1,161,168 | pcapng | 200 | 2026-09-28 |  |
| C217 | [s7/S7Comm/s7comm_clean.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/s7/S7Comm/s7comm_clean.pcap) | s7 | 542,294 | pcap | 200 | 2026-09-28 |  |
| C218 | [beckoff/invokeid12.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/invokeid12.pcapng) | beckoff | 12,320 | pcapng | 200 | 2026-09-28 |  |
| C219 | [beckoff/beckoffiplinktc2.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/beckoffiplinktc2.pcapng) | beckoff | 22,852 | pcapng | 200 | 2026-09-28 |  |
| C220 | [beckoff/beckoffiplinktc.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/beckoffiplinktc.pcapng) | beckoff | 17,332 | pcapng | 200 | 2026-09-28 |  |
| C221 | [beckoff/addroute.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/addroute.pcapng) | beckoff | 31,160 | pcapng | 200 | 2026-09-28 |  |
| C222 | [beckoff/addroute1.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/addroute1.pcapng) | beckoff | 16,656 | pcapng | 200 | 2026-09-28 |  |
| C223 | [beckoff/beckoffaddroute.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/beckoffaddroute.pcapng) | beckoff | 32,724 | pcapng | 200 | 2026-09-28 |  |
| C224 | [beckoff/beckoffiplinktc3.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/beckoffiplinktc3.pcapng) | beckoff | 46,592 | pcapng | 200 | 2026-09-28 |  |
| C225 | [beckoff/beckofflink.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/beckofflink.pcapng) | beckoff | 17,276 | pcapng | 200 | 2026-09-28 |  |
| C226 | [beckoff/addrouteuse444444444.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/addrouteuse444444444.pcapng) | beckoff | 57,432 | pcapng | 200 | 2026-09-28 |  |
| C227 | [beckoff/beckoffiplink.pcapng](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/beckoff/beckoffiplink.pcapng) | beckoff | 837,140 | pcapng | 200 | 2026-09-28 |  |
| C228 | [Zigbee/control4-sample.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/Zigbee/control4-sample.pcap) | Zigbee | 21,369 | pcap | 200 | 2026-09-28 |  |
| C229 | [hart/hart_ip.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/hart/hart_ip.pcap) | hart | 11,932 | pcapng | 200 | 2026-09-28 |  |
| C230 | [omron/omron_test.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/omron/omron_test.pcap) | omron | 1,582 | pcap | 200 | 2026-09-28 |  |
| C231 | [Combined/Plant1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/Combined/Plant1.pcap) | Combined | 7,684,492 | pcap | 200 | 2026-09-28 |  |
| C232 | [dnp3/read_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/read_and_response.pcap) | dnp3 | 1,254 | pcap | 200 | 2026-09-28 |  |
| C233 | [dnp3/select_operate_and_responses.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/select_operate_and_responses.pcap) | dnp3 | 1,044 | pcap | 200 | 2026-09-28 |  |
| C234 | [dnp3/direct_operate_no_ack_crob.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/direct_operate_no_ack_crob.pcap) | dnp3 | 129 | pcap | 200 | 2026-09-28 |  |
| C235 | [dnp3/dnp3_test_data_part2.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/dnp3_test_data_part2.pcap) | dnp3 | 2,976 | pcap | 200 | 2026-09-28 |  |
| C236 | [dnp3/unsolcited_response_and_confirm.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/unsolcited_response_and_confirm.pcap) | dnp3 | 722 | pcap | 200 | 2026-09-28 |  |
| C237 | [dnp3/write_iin_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/write_iin_and_response.pcap) | dnp3 | 798 | pcap | 200 | 2026-09-28 |  |
| C238 | [dnp3/warm_restart_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/warm_restart_and_response.pcap) | dnp3 | 792 | pcap | 200 | 2026-09-28 |  |
| C239 | [dnp3/cold_restart_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/cold_restart_and_response.pcap) | dnp3 | 792 | pcap | 200 | 2026-09-28 |  |
| C240 | [dnp3/file_delete.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/file_delete.pcap) | dnp3 | 347 | pcap | 200 | 2026-09-28 |  |
| C241 | [dnp3/directoperate_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/directoperate_and_response.pcap) | dnp3 | 832 | pcap | 200 | 2026-09-28 |  |
| C242 | [dnp3/immediate_freeze.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/immediate_freeze.pcap) | dnp3 | 275 | pcap | 200 | 2026-09-28 |  |
| C243 | [dnp3/auth_control_challenge_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/auth_control_challenge_response.pcap) | dnp3 | 534 | pcap | 200 | 2026-09-28 |  |
| C244 | [dnp3/disable_unsolcited_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/disable_unsolcited_and_response.pcap) | dnp3 | 801 | pcap | 200 | 2026-09-28 |  |
| C245 | [dnp3/enable_unsolicited_and_response.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/enable_unsolicited_and_response.pcap) | dnp3 | 801 | pcap | 200 | 2026-09-28 |  |
| C246 | [dnp3/direct_operate_analog_output.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/direct_operate_analog_output.pcap) | dnp3 | 119 | pcap | 200 | 2026-09-28 |  |
| C247 | [dnp3/serial_time_sync.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/serial_time_sync.pcap) | dnp3 | 460 | pcap | 200 | 2026-09-28 |  |
| C248 | [dnp3/lan_time_sync.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/lan_time_sync.pcap) | dnp3 | 454 | pcap | 200 | 2026-09-28 |  |
| C249 | [dnp3/file_read.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/file_read.pcap) | dnp3 | 784 | pcap | 200 | 2026-09-28 |  |
| C250 | [dnp3/file_write.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/file_write.pcap) | dnp3 | 775 | pcap | 200 | 2026-09-28 |  |
| C251 | [dnp3/assign_class.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/assign_class.pcap) | dnp3 | 278 | pcap | 200 | 2026-09-28 |  |
| C252 | [dnp3/file_list_directory.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/file_list_directory.pcap) | dnp3 | 3,156 | pcap | 200 | 2026-09-28 |  |
| C253 | [dnp3/dataset_exchange.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/dataset_exchange.pcap) | dnp3 | 1,048 | pcap | 200 | 2026-09-28 |  |
| C254 | [dnp3/auth_change_session_keys.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/auth_change_session_keys.pcap) | dnp3 | 838 | pcap | 200 | 2026-09-28 |  |
| C255 | [dnp3/write_binary_output.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/write_binary_output.pcap) | dnp3 | 115 | pcap | 200 | 2026-09-28 |  |
| C256 | [dnp3/dnp3_test_data_part1.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/dnp3_test_data_part1.pcap) | dnp3 | 15,838 | pcap | 200 | 2026-09-28 |  |
| C257 | [dnp3/write_vto_empty_string.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/write_vto_empty_string.pcap) | dnp3 | 2,542 | pcap | 200 | 2026-09-28 |  |
| C258 | [dnp3/direct_operate_crob_malform_but_good_crc.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/direct_operate_crob_malform_but_good_crc.pcap) | dnp3 | 129 | pcap | 200 | 2026-09-28 |  |
| C259 | [dnp3/operate_aggressive_mode.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/operate_aggressive_mode.pcap) | dnp3 | 348 | pcap | 200 | 2026-09-28 |  |
| C260 | [dnp3/full_exchange.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/full_exchange.pcap) | dnp3 | 2,118 | pcap | 200 | 2026-09-28 |  |
| C261 | [dnp3/opendnp3-3/conformance/8.4.3.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.3.2.3/dump.pcap) | dnp3 | 613 | pcap | 200 | 2026-09-28 |  |
| C262 | [dnp3/opendnp3-3/conformance/8.7.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.7.2.2/dump.pcap) | dnp3 | 1,449 | pcap | 200 | 2026-09-28 |  |
| C263 | [dnp3/opendnp3-3/conformance/8.5.6.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.6.2/dump.pcap) | dnp3 | 3,157 | pcap | 200 | 2026-09-28 |  |
| C264 | [dnp3/opendnp3-3/conformance/8.4.1.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.2/dump.pcap) | dnp3 | 1,044 | pcap | 200 | 2026-09-28 |  |
| C265 | [dnp3/opendnp3-3/conformance/8.6.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.2.2/dump.pcap) | dnp3 | 1,290 | pcap | 200 | 2026-09-28 |  |
| C266 | [dnp3/opendnp3-3/conformance/8.4.1.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.5/dump.pcap) | dnp3 | 1,044 | pcap | 200 | 2026-09-28 |  |
| C267 | [dnp3/opendnp3-3/conformance/6.5.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.5.2/dump.pcap) | dnp3 | 1,015 | pcap | 200 | 2026-09-28 |  |
| C268 | [dnp3/opendnp3-3/conformance/8.4.2.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.2.2.3/dump.pcap) | dnp3 | 760 | pcap | 200 | 2026-09-28 |  |
| C269 | [dnp3/opendnp3-3/conformance/6.1.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.1.2/dump.pcap) | dnp3 | 7,763 | pcap | 200 | 2026-09-28 |  |
| C270 | [dnp3/opendnp3-3/conformance/8.2.5.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.5.2.2/dump.pcap) | dnp3 | 2,008 | pcap | 200 | 2026-09-28 |  |
| C271 | [dnp3/opendnp3-3/conformance/8.18.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.18.2.2/dump.pcap) | dnp3 | 787 | pcap | 200 | 2026-09-28 |  |
| C272 | [dnp3/opendnp3-3/conformance/8.4.3.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.3.2.2/dump.pcap) | dnp3 | 613 | pcap | 200 | 2026-09-28 |  |
| C273 | [dnp3/opendnp3-3/conformance/8.20.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.20.2/dump.pcap) | dnp3 | 1,225 | pcap | 200 | 2026-09-28 |  |
| C274 | [dnp3/opendnp3-3/conformance/8.4.2.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.2.2.2/dump.pcap) | dnp3 | 760 | pcap | 200 | 2026-09-28 |  |
| C275 | [dnp3/opendnp3-3/conformance/8.19.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.19.2.2/dump.pcap) | dnp3 | 1,509 | pcap | 200 | 2026-09-28 |  |
| C276 | [dnp3/opendnp3-3/conformance/8.4.1.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.4/dump.pcap) | dnp3 | 1,044 | pcap | 200 | 2026-09-28 |  |
| C277 | [dnp3/opendnp3-3/conformance/8.4.1.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.3/dump.pcap) | dnp3 | 760 | pcap | 200 | 2026-09-28 |  |
| C278 | [dnp3/opendnp3-3/conformance/8.22.2.15/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.15/dump.pcap) | dnp3 | 1,496 | pcap | 200 | 2026-09-28 |  |
| C279 | [dnp3/opendnp3-3/conformance/7.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/7.2/dump.pcap) | dnp3 | 1,015 | pcap | 200 | 2026-09-28 |  |
| C280 | [dnp3/opendnp3-3/conformance/8.22.2.12/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.12/dump.pcap) | dnp3 | 1,462 | pcap | 200 | 2026-09-28 |  |
| C281 | [dnp3/opendnp3-3/conformance/8.21.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.21.2.2/dump.pcap) | dnp3 | 743 | pcap | 200 | 2026-09-28 |  |
| C282 | [dnp3/opendnp3-3/conformance/8.15.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.15.2/dump.pcap) | dnp3 | 3,782 | pcap | 200 | 2026-09-28 |  |
| C283 | [dnp3/opendnp3-3/conformance/8.22.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.3/dump.pcap) | dnp3 | 1,584 | pcap | 200 | 2026-09-28 |  |
| C284 | [dnp3/opendnp3-3/conformance/8.2.3.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.3.2.3/dump.pcap) | dnp3 | 623 | pcap | 200 | 2026-09-28 |  |
| C285 | [dnp3/opendnp3-3/conformance/8.22.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.4/dump.pcap) | dnp3 | 1,586 | pcap | 200 | 2026-09-28 |  |
| C286 | [dnp3/opendnp3-3/conformance/8.23.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.23.2.4/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C287 | [dnp3/opendnp3-3/conformance/8.2.2.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.2.2.3/dump.pcap) | dnp3 | 780 | pcap | 200 | 2026-09-28 |  |
| C288 | [dnp3/opendnp3-3/conformance/8.23.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.23.2.3/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C289 | [dnp3/opendnp3-3/conformance/8.14.2.14/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.14/dump.pcap) | dnp3 | 1,891 | pcap | 200 | 2026-09-28 |  |
| C290 | [dnp3/opendnp3-3/conformance/8.6.6.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.6.2.3/dump.pcap) | dnp3 | 4,114 | pcap | 200 | 2026-09-28 |  |
| C291 | [dnp3/opendnp3-3/conformance/6.6.3.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.3.2/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C292 | [dnp3/opendnp3-3/conformance/8.2.1.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.5/dump.pcap) | dnp3 | 1,084 | pcap | 200 | 2026-09-28 |  |
| C293 | [dnp3/opendnp3-3/conformance/8.2.1.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.2/dump.pcap) | dnp3 | 1,084 | pcap | 200 | 2026-09-28 |  |
| C294 | [dnp3/opendnp3-3/conformance/8.6.6.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.6.2.4/dump.pcap) | dnp3 | 2,805 | pcap | 200 | 2026-09-28 |  |
| C295 | [dnp3/opendnp3-3/conformance/8.14.2.13/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.13/dump.pcap) | dnp3 | 1,889 | pcap | 200 | 2026-09-28 |  |
| C296 | [dnp3/opendnp3-3/conformance/8.2.3.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.3.2.2/dump.pcap) | dnp3 | 623 | pcap | 200 | 2026-09-28 |  |
| C297 | [dnp3/opendnp3-3/conformance/8.22.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.5/dump.pcap) | dnp3 | 1,744 | pcap | 200 | 2026-09-28 |  |
| C298 | [dnp3/opendnp3-3/conformance/8.22.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.2/dump.pcap) | dnp3 | 1,719 | pcap | 200 | 2026-09-28 |  |
| C299 | [dnp3/opendnp3-3/conformance/8.22.2.13/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.13/dump.pcap) | dnp3 | 1,889 | pcap | 200 | 2026-09-28 |  |
| C300 | [dnp3/opendnp3-3/conformance/8.22.2.14/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.14/dump.pcap) | dnp3 | 1,891 | pcap | 200 | 2026-09-28 |  |
| C301 | [dnp3/opendnp3-3/conformance/6.6.3.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.3.4/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C302 | [dnp3/opendnp3-3/conformance/8.2.1.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.3/dump.pcap) | dnp3 | 780 | pcap | 200 | 2026-09-28 |  |
| C303 | [dnp3/opendnp3-3/conformance/8.14.2.12/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.12/dump.pcap) | dnp3 | 1,462 | pcap | 200 | 2026-09-28 |  |
| C304 | [dnp3/opendnp3-3/conformance/8.6.6.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.6.2.2/dump.pcap) | dnp3 | 4,114 | pcap | 200 | 2026-09-28 |  |
| C305 | [dnp3/opendnp3-3/conformance/8.14.2.15/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.15/dump.pcap) | dnp3 | 1,496 | pcap | 200 | 2026-09-28 |  |
| C306 | [dnp3/opendnp3-3/conformance/8.2.1.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.4/dump.pcap) | dnp3 | 1,084 | pcap | 200 | 2026-09-28 |  |
| C307 | [dnp3/opendnp3-3/conformance/6.6.3.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.3.3/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C308 | [dnp3/opendnp3-3/conformance/8.23.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.23.2.2/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C309 | [dnp3/opendnp3-3/conformance/8.4.1.2.12/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.12/dump.pcap) | dnp3 | 1,332 | pcap | 200 | 2026-09-28 |  |
| C310 | [dnp3/opendnp3-3/conformance/8.2.2.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.2.2.2/dump.pcap) | dnp3 | 780 | pcap | 200 | 2026-09-28 |  |
| C311 | [dnp3/opendnp3-3/conformance/8.5.3.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.3.2.2/dump.pcap) | dnp3 | 1,875 | pcap | 200 | 2026-09-28 |  |
| C312 | [dnp3/opendnp3-3/conformance/8.6.1.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.1.2/dump.pcap) | dnp3 | 1,021 | pcap | 200 | 2026-09-28 |  |
| C313 | [dnp3/opendnp3-3/conformance/8.13.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.13.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C314 | [dnp3/opendnp3-3/conformance/8.6.5.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.5.3/dump.pcap) | dnp3 | 1,171 | pcap | 200 | 2026-09-28 |  |
| C315 | [dnp3/opendnp3-3/conformance/8.6.5.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.5.4/dump.pcap) | dnp3 | 4,049 | pcap | 200 | 2026-09-28 |  |
| C316 | [dnp3/opendnp3-3/conformance/8.7.1.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.7.1.2/dump.pcap) | dnp3 | 1,302 | pcap | 200 | 2026-09-28 |  |
| C317 | [dnp3/opendnp3-3/conformance/8.5.2.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.2.2.2/dump.pcap) | dnp3 | 1,859 | pcap | 200 | 2026-09-28 |  |
| C318 | [dnp3/opendnp3-3/conformance/8.5.1.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.1.2/dump.pcap) | dnp3 | 1,015 | pcap | 200 | 2026-09-28 |  |
| C319 | [dnp3/opendnp3-3/conformance/8.5.3.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.3.2.4/dump.pcap) | dnp3 | 1,919 | pcap | 200 | 2026-09-28 |  |
| C320 | [dnp3/opendnp3-3/conformance/8.5.3.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.3.2.3/dump.pcap) | dnp3 | 1,877 | pcap | 200 | 2026-09-28 |  |
| C321 | [dnp3/opendnp3-3/conformance/8.11.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.11.2.1/dump.pcap) | dnp3 | 2,966 | pcap | 200 | 2026-09-28 |  |
| C322 | [dnp3/opendnp3-3/conformance/8.5.2.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.2.2.3/dump.pcap) | dnp3 | 1,861 | pcap | 200 | 2026-09-28 |  |
| C323 | [dnp3/opendnp3-3/conformance/8.5.2.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.2.2.4/dump.pcap) | dnp3 | 1,879 | pcap | 200 | 2026-09-28 |  |
| C324 | [dnp3/opendnp3-3/conformance/8.11.2.6/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.11.2.6/dump.pcap) | dnp3 | 1,589 | pcap | 200 | 2026-09-28 |  |
| C325 | [dnp3/opendnp3-3/conformance/8.6.5.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.5.2/dump.pcap) | dnp3 | 1,694 | pcap | 200 | 2026-09-28 |  |
| C326 | [dnp3/opendnp3-3/conformance/6.6.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.2.1/dump.pcap) | dnp3 | 1,957 | pcap | 200 | 2026-09-28 |  |
| C327 | [dnp3/opendnp3-3/conformance/8.5.5.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.5.2.2/dump.pcap) | dnp3 | 1,645 | pcap | 200 | 2026-09-28 |  |
| C328 | [dnp3/opendnp3-3/conformance/8.2.1.2.12/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.12/dump.pcap) | dnp3 | 1,392 | pcap | 200 | 2026-09-28 |  |
| C329 | [dnp3/opendnp3-3/conformance/8.2.1.2.15/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.15/dump.pcap) | dnp3 | 1,392 | pcap | 200 | 2026-09-28 |  |
| C330 | [dnp3/opendnp3-3/conformance/8.14.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C331 | [dnp3/opendnp3-3/conformance/8.16.1.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.1.2.3/dump.pcap) | dnp3 | 743 | pcap | 200 | 2026-09-28 |  |
| C332 | [dnp3/opendnp3-3/conformance/8.14.2.6/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.6/dump.pcap) | dnp3 | 1,444 | pcap | 200 | 2026-09-28 |  |
| C333 | [dnp3/opendnp3-3/conformance/8.16.2.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.2.2.2/dump.pcap) | dnp3 | 1,975 | pcap | 200 | 2026-09-28 |  |
| C334 | [dnp3/opendnp3-3/conformance/8.14.2.8/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.8/dump.pcap) | dnp3 | 1,861 | pcap | 200 | 2026-09-28 |  |
| C335 | [dnp3/opendnp3-3/conformance/8.16.2.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.2.2.5/dump.pcap) | dnp3 | 1,382 | pcap | 200 | 2026-09-28 |  |
| C336 | [dnp3/opendnp3-3/conformance/8.5.4.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.4.2.2/dump.pcap) | dnp3 | 1,875 | pcap | 200 | 2026-09-28 |  |
| C337 | [dnp3/opendnp3-3/conformance/8.2.1.2.14/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.14/dump.pcap) | dnp3 | 1,392 | pcap | 200 | 2026-09-28 |  |
| C338 | [dnp3/opendnp3-3/conformance/8.3.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.3.2/dump.pcap) | dnp3 | 1,108 | pcap | 200 | 2026-09-28 |  |
| C339 | [dnp3/opendnp3-3/conformance/8.2.1.2.13/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.13/dump.pcap) | dnp3 | 1,392 | pcap | 200 | 2026-09-28 |  |
| C340 | [dnp3/opendnp3-3/conformance/8.12.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.12.2/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C341 | [dnp3/opendnp3-3/conformance/8.14.2.9/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.9/dump.pcap) | dnp3 | 1,464 | pcap | 200 | 2026-09-28 |  |
| C342 | [dnp3/opendnp3-3/conformance/8.17.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.17.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C343 | [dnp3/opendnp3-3/conformance/8.5.4.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.4.2.3/dump.pcap) | dnp3 | 1,877 | pcap | 200 | 2026-09-28 |  |
| C344 | [dnp3/opendnp3-3/conformance/8.16.2.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.2.2.4/dump.pcap) | dnp3 | 1,701 | pcap | 200 | 2026-09-28 |  |
| C345 | [dnp3/opendnp3-3/conformance/8.16.2.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.2.2.3/dump.pcap) | dnp3 | 1,656 | pcap | 200 | 2026-09-28 |  |
| C346 | [dnp3/opendnp3-3/conformance/8.5.4.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.4.2.4/dump.pcap) | dnp3 | 1,919 | pcap | 200 | 2026-09-28 |  |
| C347 | [dnp3/opendnp3-3/conformance/8.14.2.7/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.7/dump.pcap) | dnp3 | 1,859 | pcap | 200 | 2026-09-28 |  |
| C348 | [dnp3/opendnp3-3/conformance/8.16.1.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.1.2.2/dump.pcap) | dnp3 | 1,106 | pcap | 200 | 2026-09-28 |  |
| C349 | [dnp3/opendnp3-3/conformance/8.4.1.2.6/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.6/dump.pcap) | dnp3 | 1,048 | pcap | 200 | 2026-09-28 |  |
| C350 | [dnp3/opendnp3-3/conformance/8.4.1.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.1/dump.pcap) | dnp3 | 1,052 | pcap | 200 | 2026-09-28 |  |
| C351 | [dnp3/opendnp3-3/conformance/6.7.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.7.2/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C352 | [dnp3/opendnp3-3/conformance/8.4.1.2.8/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.8/dump.pcap) | dnp3 | 1,332 | pcap | 200 | 2026-09-28 |  |
| C353 | [dnp3/opendnp3-3/conformance/8.4.4.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.4.2/dump.pcap) | dnp3 | 2,116 | pcap | 200 | 2026-09-28 |  |
| C354 | [dnp3/opendnp3-3/conformance/8.6.4.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.4.3/dump.pcap) | dnp3 | 1,516 | pcap | 200 | 2026-09-28 |  |
| C355 | [dnp3/opendnp3-3/conformance/8.4.1.2.9/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.9/dump.pcap) | dnp3 | 1,332 | pcap | 200 | 2026-09-28 |  |
| C356 | [dnp3/opendnp3-3/conformance/8.4.2.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.2.2.1/dump.pcap) | dnp3 | 756 | pcap | 200 | 2026-09-28 |  |
| C357 | [dnp3/opendnp3-3/conformance/8.19.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.19.2.1/dump.pcap) | dnp3 | 1,894 | pcap | 200 | 2026-09-28 |  |
| C358 | [dnp3/opendnp3-3/conformance/8.4.1.2.7/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.7/dump.pcap) | dnp3 | 760 | pcap | 200 | 2026-09-28 |  |
| C359 | [dnp3/opendnp3-3/conformance/8.6.4.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.4.2/dump.pcap) | dnp3 | 1,516 | pcap | 200 | 2026-09-28 |  |
| C360 | [dnp3/opendnp3-3/conformance/8.18.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.18.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C361 | [dnp3/opendnp3-3/conformance/8.2.5.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.5.2.1/dump.pcap) | dnp3 | 2,932 | pcap | 200 | 2026-09-28 |  |
| C362 | [dnp3/opendnp3-3/conformance/8.4.3.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.3.2.1/dump.pcap) | dnp3 | 611 | pcap | 200 | 2026-09-28 |  |
| C363 | [dnp3/opendnp3-3/conformance/6.3.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.3.2/dump.pcap) | dnp3 | 988 | pcap | 200 | 2026-09-28 |  |
| C364 | [dnp3/opendnp3-3/conformance/8.9.1.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.9.1.2/dump.pcap) | dnp3 | 8,207 | pcap | 200 | 2026-09-28 |  |
| C365 | [dnp3/opendnp3-3/conformance/8.2.1.2.8/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.8/dump.pcap) | dnp3 | 1,084 | pcap | 200 | 2026-09-28 |  |
| C366 | [dnp3/opendnp3-3/conformance/8.4.1.2.10/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.10/dump.pcap) | dnp3 | 1,332 | pcap | 200 | 2026-09-28 |  |
| C367 | [dnp3/opendnp3-3/conformance/8.2.1.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.1/dump.pcap) | dnp3 | 1,092 | pcap | 200 | 2026-09-28 |  |
| C368 | [dnp3/opendnp3-3/conformance/8.14.2.10/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.10/dump.pcap) | dnp3 | 1,881 | pcap | 200 | 2026-09-28 |  |
| C369 | [dnp3/opendnp3-3/conformance/8.2.1.2.6/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.6/dump.pcap) | dnp3 | 1,084 | pcap | 200 | 2026-09-28 |  |
| C370 | [dnp3/opendnp3-3/conformance/6.6.3.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.3.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C371 | [dnp3/opendnp3-3/conformance/8.2.4.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.4.2/dump.pcap) | dnp3 | 2,472 | pcap | 200 | 2026-09-28 |  |
| C372 | [dnp3/opendnp3-3/conformance/8.22.2.11/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.11/dump.pcap) | dnp3 | 1,883 | pcap | 200 | 2026-09-28 |  |
| C373 | [dnp3/opendnp3-3/conformance/8.22.2.9/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.9/dump.pcap) | dnp3 | 1,464 | pcap | 200 | 2026-09-28 |  |
| C374 | [dnp3/opendnp3-3/conformance/8.21.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.21.2.1/dump.pcap) | dnp3 | 1,090 | pcap | 200 | 2026-09-28 |  |
| C375 | [dnp3/opendnp3-3/conformance/8.22.2.7/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.7/dump.pcap) | dnp3 | 1,859 | pcap | 200 | 2026-09-28 |  |
| C376 | [dnp3/opendnp3-3/conformance/8.6.6.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.6.2.1/dump.pcap) | dnp3 | 2,805 | pcap | 200 | 2026-09-28 |  |
| C377 | [dnp3/opendnp3-3/conformance/8.2.1.2.7/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.7/dump.pcap) | dnp3 | 1,084 | pcap | 200 | 2026-09-28 |  |
| C378 | [dnp3/opendnp3-3/conformance/8.14.2.11/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.11/dump.pcap) | dnp3 | 1,883 | pcap | 200 | 2026-09-28 |  |
| C379 | [dnp3/opendnp3-3/conformance/8.8.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.8.2/dump.pcap) | dnp3 | 1,571 | pcap | 200 | 2026-09-28 |  |
| C380 | [dnp3/opendnp3-3/conformance/8.2.1.2.9/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.9/dump.pcap) | dnp3 | 1,088 | pcap | 200 | 2026-09-28 |  |
| C381 | [dnp3/opendnp3-3/conformance/8.4.1.2.11/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.4.1.2.11/dump.pcap) | dnp3 | 1,332 | pcap | 200 | 2026-09-28 |  |
| C382 | [dnp3/opendnp3-3/conformance/8.2.2.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.2.2.1/dump.pcap) | dnp3 | 780 | pcap | 200 | 2026-09-28 |  |
| C383 | [dnp3/opendnp3-3/conformance/8.23.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.23.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C384 | [dnp3/opendnp3-3/conformance/8.22.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C385 | [dnp3/opendnp3-3/conformance/8.2.3.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.3.2.1/dump.pcap) | dnp3 | 621 | pcap | 200 | 2026-09-28 |  |
| C386 | [dnp3/opendnp3-3/conformance/8.22.2.6/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.6/dump.pcap) | dnp3 | 1,444 | pcap | 200 | 2026-09-28 |  |
| C387 | [dnp3/opendnp3-3/conformance/8.22.2.10/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.10/dump.pcap) | dnp3 | 1,881 | pcap | 200 | 2026-09-28 |  |
| C388 | [dnp3/opendnp3-3/conformance/8.22.2.8/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.22.2.8/dump.pcap) | dnp3 | 1,861 | pcap | 200 | 2026-09-28 |  |
| C389 | [dnp3/opendnp3-3/conformance/8.11.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.11.2.3/dump.pcap) | dnp3 | 2,061 | pcap | 200 | 2026-09-28 |  |
| C390 | [dnp3/opendnp3-3/conformance/8.5.2.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.2.2.1/dump.pcap) | dnp3 | 1,444 | pcap | 200 | 2026-09-28 |  |
| C391 | [dnp3/opendnp3-3/conformance/8.11.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.11.2.4/dump.pcap) | dnp3 | 2,061 | pcap | 200 | 2026-09-28 |  |
| C392 | [dnp3/opendnp3-3/conformance/6.4.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.4.2/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C393 | [dnp3/opendnp3-3/conformance/8.5.3.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.3.2.1/dump.pcap) | dnp3 | 1,456 | pcap | 200 | 2026-09-28 |  |
| C394 | [dnp3/opendnp3-3/conformance/8.6.3.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.6.3.2/dump.pcap) | dnp3 | 1,290 | pcap | 200 | 2026-09-28 |  |
| C395 | [dnp3/opendnp3-3/conformance/8.13.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.13.2.2/dump.pcap) | dnp3 | 1,090 | pcap | 200 | 2026-09-28 |  |
| C396 | [dnp3/opendnp3-3/conformance/8.11.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.11.2.5/dump.pcap) | dnp3 | 10,834 | pcap | 200 | 2026-09-28 |  |
| C397 | [dnp3/opendnp3-3/conformance/8.11.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.11.2.2/dump.pcap) | dnp3 | 2,025 | pcap | 200 | 2026-09-28 |  |
| C398 | [dnp3/opendnp3-3/conformance/8.13.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.13.2.3/dump.pcap) | dnp3 | 743 | pcap | 200 | 2026-09-28 |  |
| C399 | [dnp3/opendnp3-3/conformance/8.14.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.5/dump.pcap) | dnp3 | 1,744 | pcap | 200 | 2026-09-28 |  |
| C400 | [dnp3/opendnp3-3/conformance/8.14.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.2/dump.pcap) | dnp3 | 1,719 | pcap | 200 | 2026-09-28 |  |
| C401 | [dnp3/opendnp3-3/conformance/8.17.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.17.2.3/dump.pcap) | dnp3 | 1,875 | pcap | 200 | 2026-09-28 |  |
| C402 | [dnp3/opendnp3-3/conformance/8.5.4.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.4.2.1/dump.pcap) | dnp3 | 1,456 | pcap | 200 | 2026-09-28 |  |
| C403 | [dnp3/opendnp3-3/conformance/8.17.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.17.2.4/dump.pcap) | dnp3 | 1,877 | pcap | 200 | 2026-09-28 |  |
| C404 | [dnp3/opendnp3-3/conformance/8.16.2.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.2.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C405 | [dnp3/opendnp3-3/conformance/6.6.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.2.5/dump.pcap) | dnp3 | 1,203 | pcap | 200 | 2026-09-28 |  |
| C406 | [dnp3/opendnp3-3/conformance/6.6.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.2.2/dump.pcap) | dnp3 | 1,681 | pcap | 200 | 2026-09-28 |  |
| C407 | [dnp3/opendnp3-3/conformance/8.5.5.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.5.5.2.1/dump.pcap) | dnp3 | 1,104 | pcap | 200 | 2026-09-28 |  |
| C408 | [dnp3/opendnp3-3/conformance/8.9.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.9.2.2/dump.pcap) | dnp3 | 11,761 | pcap | 200 | 2026-09-28 |  |
| C409 | [dnp3/opendnp3-3/conformance/8.2.1.2.11/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.11/dump.pcap) | dnp3 | 1,392 | pcap | 200 | 2026-09-28 |  |
| C410 | [dnp3/opendnp3-3/conformance/8.17.2.5/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.17.2.5/dump.pcap) | dnp3 | 1,784 | pcap | 200 | 2026-09-28 |  |
| C411 | [dnp3/opendnp3-3/conformance/8.17.2.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.17.2.2/dump.pcap) | dnp3 | 1,894 | pcap | 200 | 2026-09-28 |  |
| C412 | [dnp3/opendnp3-3/conformance/8.14.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.3/dump.pcap) | dnp3 | 1,584 | pcap | 200 | 2026-09-28 |  |
| C413 | [dnp3/opendnp3-3/conformance/8.14.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.14.2.4/dump.pcap) | dnp3 | 1,586 | pcap | 200 | 2026-09-28 |  |
| C414 | [dnp3/opendnp3-3/conformance/8.16.1.2.1/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.16.1.2.1/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C415 | [dnp3/opendnp3-3/conformance/8.2.1.2.10/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.2.1.2.10/dump.pcap) | dnp3 | 780 | pcap | 200 | 2026-09-28 |  |
| C416 | [dnp3/opendnp3-3/conformance/8.10.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.10.2/dump.pcap) | dnp3 | 24 | pcap | 200 | 2026-09-28 |  |
| C417 | [dnp3/opendnp3-3/conformance/6.6.2.3/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.2.3/dump.pcap) | dnp3 | 756 | pcap | 200 | 2026-09-28 |  |
| C418 | [dnp3/opendnp3-3/conformance/6.6.2.4/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/6.6.2.4/dump.pcap) | dnp3 | 1,020 | pcap | 200 | 2026-09-28 |  |
| C419 | [dnp3/opendnp3-3/conformance/8.1.2/dump.pcap](https://raw.githubusercontent.com/ITI/ICS-Security-Tools/master/pcaps/dnp3/opendnp3-3/conformance/8.1.2/dump.pcap) | dnp3 | 770 | pcap | 200 | 2026-09-28 |  |

## R14 — Lemay & Fernandez Modbus dataset (CSET 2016)

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R14.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C420 | [CnC_uploading_exe_modbus_6RTU_with_operate.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/CnC_uploading_exe_modbus_6RTU_with_operate.pcap) | root | 183,387 | pcap | 200 | 2026-09-28 |  |
| C421 | [run1_6rtu(1).pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/run1_6rtu%281%29.pcap) | root | 17,172,222 | pcap | 200 | 2026-09-28 |  |
| C422 | [Modbus_polling_only_6RTU(2).pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/Modbus_polling_only_6RTU%282%29.pcap) | root | 4,374,471 | pcap | 200 | 2026-09-28 |  |
| C423 | [run1_12rtu(1).pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/run1_12rtu%281%29.pcap) | root | 20,004,864 | pcap | 200 | 2026-09-28 |  |
| C424 | [exploit_ms08_netapi_modbus_6RTU_with_operate.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/exploit_ms08_netapi_modbus_6RTU_with_operate.pcap) | root | 1,158,798 | pcap | 200 | 2026-09-28 |  |
| C425 | [moving_two_files_modbus_6RTU.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/moving_two_files_modbus_6RTU.pcap) | root | 253,317 | pcap | 200 | 2026-09-28 |  |
| C426 | [run11.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/run11.pcap) | root | 7,149,218 | pcap | 200 | 2026-09-28 |  |
| C427 | [send_a_fake_command_modbus_6RTU_with_operate.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/send_a_fake_command_modbus_6RTU_with_operate.pcap) | root | 836,520 | pcap | 200 | 2026-09-28 |  |
| C428 | [characterization_modbus_6RTU_with_operate.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/characterization_modbus_6RTU_with_operate.pcap) | root | 958,347 | pcap | 200 | 2026-09-28 |  |
| C429 | [run1_3rtu_2s.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/run1_3rtu_2s.pcap) | root | 25,225,413 | pcap | 200 | 2026-09-28 |  |
| C430 | [run8.pcap](https://raw.githubusercontent.com/antoine-lemay/Modbus_dataset/master/run8.pcap) | root | 7,190,064 | pcap | 200 | 2026-09-28 |  |

## R15 — gymgit S7comm client/PLC captures

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R15.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C431 | [snap7_s300_everything.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/snap7_s300_everything.pcapng) | root | 8,260 | pcap | 200 | 2026-09-28 |  |
| C432 | [wincc_s300_setup-alarm-read_2.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/wincc_s300_setup-alarm-read_2.pcapng) | root | 63,830 | pcap | 200 | 2026-09-28 |  |
| C433 | [tia_s300_updateFirmware_2.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/tia_s300_updateFirmware_2.pcapng) | root | 14,266,140 | pcap | 200 | 2026-09-28 |  |
| C434 | [tia_s300_goOnline.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/tia_s300_goOnline.pcapng) | root | 62,240 | pcap | 200 | 2026-09-28 |  |
| C435 | [step7_s300_stop.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_stop.pcapng) | root | 431 | pcap | 200 | 2026-09-28 |  |
| C436 | [step7_s300_readDiagData.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_readDiagData.pcapng) | root | 73,759 | pcap | 200 | 2026-09-28 |  |
| C437 | [step7_s300_copyRamToRom.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_copyRamToRom.pcapng) | root | 219 | pcap | 200 | 2026-09-28 |  |
| C438 | [wincc_s300_setup-alarm-read.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/wincc_s300_setup-alarm-read.pcapng) | root | 24,442 | pcap | 200 | 2026-09-28 |  |
| C439 | [tia_s300_updateFirmware.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/tia_s300_updateFirmware.pcapng) | root | 14,266,140 | pcap | 200 | 2026-09-28 |  |
| C440 | [tia_s300_flashLed.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/tia_s300_flashLed.pcapng) | root | 484 | pcap | 200 | 2026-09-28 |  |
| C441 | [snap7_s300_readVar.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/snap7_s300_readVar.pcapng) | root | 220 | pcap | 200 | 2026-09-28 |  |
| C442 | [step7_s300_download.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_download.pcapng) | root | 13,005 | pcap | 200 | 2026-09-28 |  |
| C443 | [snap7_s300_stop.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/snap7_s300_stop.pcapng) | root | 217 | pcap | 200 | 2026-09-28 |  |
| C444 | [snap7_s300_setupCommunication.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/snap7_s300_setupCommunication.pcapng) | root | 216 | pcap | 200 | 2026-09-28 |  |
| C445 | [step7_s300_readVarTab.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_readVarTab.pcapng) | root | 56,508 | pcap | 200 | 2026-09-28 |  |
| C446 | [wincc_s300_setup-alarm-read-write.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/wincc_s300_setup-alarm-read-write.pcapng) | root | 21,368 | pcap | 200 | 2026-09-28 |  |
| C447 | [step7_s300_rwVarTab.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_rwVarTab.pcapng) | root | 2,638 | pcap | 200 | 2026-09-28 |  |
| C448 | [wincc_s400_production.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/wincc_s400_production.pcapng) | root | 294,072 | pcap | 200 | 2026-09-28 |  |
| C449 | [tia_s300_downloadOb1.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/tia_s300_downloadOb1.pcapng) | root | 14,297 | pcap | 200 | 2026-09-28 |  |
| C450 | [tia_s300_downloadHwConfig.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/tia_s300_downloadHwConfig.pcapng) | root | 18,792 | pcap | 200 | 2026-09-28 |  |
| C451 | [step7_s300_AuthPassword.pcapng](https://raw.githubusercontent.com/gymgit/s7-pcaps/master/step7_s300_AuthPassword.pcapng) | root | 722 | pcap | 200 | 2026-09-28 |  |

## R16 — EmreEkin ICS-Pcaps protocol sampler

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R16.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C452 | [IEC60870-104/iec104_baselines.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/iec104_baselines.pcap) | IEC60870-104 | 8,304 | pcap | 200 | 2026-09-28 |  |
| C453 | [IEC60870-104/104IPValue.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/104IPValue.pcap) | IEC60870-104 | 42,118 | pcap | 200 | 2026-09-28 |  |
| C454 | [IEC60870-104/iec104.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/iec104.pcap) | IEC60870-104 | 10,135 | pcap | 200 | 2026-09-28 |  |
| C455 | [IEC60870-104/64.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/64.pcap) | IEC60870-104 | 5,886 | pcap | 200 | 2026-09-28 |  |
| C456 | [IEC60870-104/33.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/33.pcap) | IEC60870-104 | 2,863 | pcap | 200 | 2026-09-28 |  |
| C457 | [IEC60870-104/63.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/63.pcap) | IEC60870-104 | 5,608 | pcap | 200 | 2026-09-28 |  |
| C458 | [IEC60870-104/59.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/59.pcap) | IEC60870-104 | 5,673 | pcap | 200 | 2026-09-28 |  |
| C459 | [IEC60870-104/62.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/62.pcap) | IEC60870-104 | 7,552 | pcap | 200 | 2026-09-28 |  |
| C460 | [IEC60870-104/104deneme.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/104deneme.pcap) | IEC60870-104 | 90,336 | pcap | 200 | 2026-09-28 |  |
| C461 | [IEC60870-104/63_1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/63_1.pcap) | IEC60870-104 | 7,604 | pcap | 200 | 2026-09-28 |  |
| C462 | [IEC60870-104/104pcap.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/104pcap.pcap) | IEC60870-104 | 13,952 | pcap | 200 | 2026-09-28 |  |
| C463 | [IEC60870-104/104deneme2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/104deneme2.pcap) | IEC60870-104 | 22,710 | pcap | 200 | 2026-09-28 |  |
| C464 | [IEC60870-104/61.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/61.pcap) | IEC60870-104 | 6,884 | pcap | 200 | 2026-09-28 |  |
| C465 | [IEC60870-104/IEC1044.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/IEC1044.pcap) | IEC60870-104 | 584 | pcapng | 200 | 2026-09-28 |  |
| C466 | [IEC60870-104/Logfile IEC104.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/Logfile%20IEC104.pcap) | IEC60870-104 | 1,695 | pcap | 200 | 2026-09-28 |  |
| C467 | [IEC60870-104/60.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/60.pcap) | IEC60870-104 | 4,017 | pcap | 200 | 2026-09-28 |  |
| C468 | [IEC60870-104/58_59.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/58_59.pcap) | IEC60870-104 | 9,448 | pcap | 200 | 2026-09-28 |  |
| C469 | [IEC60870-104/104LocalValue.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/104LocalValue.pcap) | IEC60870-104 | 30,381 | pcap | 200 | 2026-09-28 |  |
| C470 | [IEC60870-104/50.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC60870-104/50.pcap) | IEC60870-104 | 4,962 | pcap | 200 | 2026-09-28 |  |
| C471 | [IEC61850/mms1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/mms1.pcap) | IEC61850 | 220,739 | pcap | 200 | 2026-09-28 |  |
| C472 | [IEC61850/iedscout.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/iedscout.pcap) | IEC61850 | 279,844 | pcapng | 200 | 2026-09-28 |  |
| C473 | [IEC61850/iec61850.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/iec61850.pcap) | IEC61850 | 1,915 | pcap | 200 | 2026-09-28 |  |
| C474 | [IEC61850/IEC61850_SV.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/IEC61850_SV.pcap) | IEC61850 | 1,444 | pcap | 200 | 2026-09-28 |  |
| C475 | [IEC61850/GOOSE.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/GOOSE.pcap) | IEC61850 | 278 | gzip | 200 | 2026-09-28 | Upstream file is gzip-compressed despite .pcap name; decompress before use |
| C476 | [IEC61850/pres1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/pres1.pcap) | IEC61850 | 60,940 | pcapng | 200 | 2026-09-28 |  |
| C477 | [IEC61850/pres.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/pres.pcap) | IEC61850 | 25,944 | pcapng | 200 | 2026-09-28 |  |
| C478 | [IEC61850/mmsy.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/mmsy.pcap) | IEC61850 | 340,364 | pcapng | 200 | 2026-09-28 |  |
| C479 | [IEC61850/setvalue.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/setvalue.pcap) | IEC61850 | 1,916 | pcap | 200 | 2026-09-28 |  |
| C480 | [IEC61850/mmsgoose.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/mmsgoose.pcap) | IEC61850 | 43,379 | pcap | 200 | 2026-09-28 |  |
| C481 | [IEC61850/mmsy1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/mmsy1.pcap) | IEC61850 | 349,760 | pcapng | 200 | 2026-09-28 |  |
| C482 | [IEC61850/samplegoose.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/samplegoose.pcap) | IEC61850 | 117,736 | pcap | 200 | 2026-09-28 |  |
| C483 | [IEC61850/9-2-sv.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/9-2-sv.pcap) | IEC61850 | 13,684 | pcap | 200 | 2026-09-28 |  |
| C484 | [IEC61850/gooseind1_7.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/gooseind1_7.pcap) | IEC61850 | 13,640 | pcapng | 200 | 2026-09-28 |  |
| C485 | [IEC61850/mms2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/mms2.pcap) | IEC61850 | 1,406,725 | pcap | 200 | 2026-09-28 |  |
| C486 | [IEC61850/Substation/wamp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/wamp.pcap) | IEC61850 | 145,658 | pcap | 200 | 2026-09-28 |  |
| C487 | [IEC61850/Substation/simens_merge.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/simens_merge.pcap) | IEC61850 | 151,656 | pcap | 200 | 2026-09-28 |  |
| C488 | [IEC61850/Substation/circuit.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/circuit.pcap) | IEC61850 | 1,287,952 | pcap | 200 | 2026-09-28 |  |
| C489 | [IEC61850/Substation/ABB3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/ABB3.pcap) | IEC61850 | 1,334,381 | pcap | 200 | 2026-09-28 |  |
| C490 | [IEC61850/Substation/ABB2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/ABB2.pcap) | IEC61850 | 1,329,584 | pcapng | 200 | 2026-09-28 |  |
| C491 | [IEC61850/Substation/ABB1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/ABB1.pcap) | IEC61850 | 1,319,528 | pcapng | 200 | 2026-09-28 |  |
| C492 | [IEC61850/Substation/simens.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/IEC61850/Substation/simens.pcap) | IEC61850 | 154,324 | pcapng | 200 | 2026-09-28 |  |
| C493 | [CDP/cdp1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CDP/cdp1.pcap) | CDP | 340 | pcap | 200 | 2026-09-28 |  |
| C494 | [CDP/cdp_v2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CDP/cdp_v2.pcap) | CDP | 1,948 | pcap | 200 | 2026-09-28 |  |
| C495 | [RTSP/RTSP-2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/RTSP/RTSP-2.pcap) | RTSP | 46,011 | pcap | 200 | 2026-09-28 |  |
| C496 | [RTSP/rtsp_play.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/RTSP/rtsp_play.pcap) | RTSP | 2,721 | pcap | 200 | 2026-09-28 |  |
| C497 | [RTSP/rtsp_ping.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/RTSP/rtsp_ping.pcap) | RTSP | 2,698 | pcap | 200 | 2026-09-28 |  |
| C498 | [SNMP/snmp-get-next.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp-get-next.pcap) | SNMP | 214 | pcap | 200 | 2026-09-28 |  |
| C499 | [SNMP/snmp-ipv4.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp-ipv4.pcap) | SNMP | 458,544 | pcap | 200 | 2026-09-28 |  |
| C500 | [SNMP/snmp_usm.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp_usm.pcap) | SNMP | 34,608 | pcap | 200 | 2026-09-28 |  |
| C501 | [SNMP/snmp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp.pcap) | SNMP | 11,929 | pcap | 200 | 2026-09-28 |  |
| C502 | [SNMP/snmp-get-bulk.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp-get-bulk.pcap) | SNMP | 214 | pcap | 200 | 2026-09-28 |  |
| C503 | [SNMP/SNMPv3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/SNMPv3.pcap) | SNMP | 1,377 | pcap | 200 | 2026-09-28 |  |
| C504 | [SNMP/snmp-v3-get-next.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp-v3-get-next.pcap) | SNMP | 661 | pcap | 200 | 2026-09-28 |  |
| C505 | [SNMP/SNMP_NTP_SysLog_00000_20060404163209.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/SNMP_NTP_SysLog_00000_20060404163209.pcap) | SNMP | 144,585 | pcap | 200 | 2026-09-28 |  |
| C506 | [SNMP/snmp-ipv6.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/snmp-ipv6.pcap) | SNMP | 392,742 | pcap | 200 | 2026-09-28 |  |
| C507 | [SNMP/SNMPv2c_get_requests.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/SNMP/SNMPv2c_get_requests.pcap) | SNMP | 894 | pcap | 200 | 2026-09-28 |  |
| C508 | [NetBIOS/NBTokenRing.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/NetBIOS/NBTokenRing.pcap) | NetBIOS | 2,306 | pcap | 200 | 2026-09-28 |  |
| C509 | [NetBIOS/LANtastic1_00028_20100407020810.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/NetBIOS/LANtastic1_00028_20100407020810.pcap) | NetBIOS | 94,702 | pcap | 200 | 2026-09-28 |  |
| C510 | [NetBIOS/Misc_NetBIOS_Traffic.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/NetBIOS/Misc_NetBIOS_Traffic.pcap) | NetBIOS | 68,425 | pcap | 200 | 2026-09-28 |  |
| C511 | [NetBIOS/netbios-ipx.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/NetBIOS/netbios-ipx.pcap) | NetBIOS | 366 | pcap | 200 | 2026-09-28 |  |
| C512 | [NetBIOS/LANtastic1_00027_20100407020716.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/NetBIOS/LANtastic1_00027_20100407020716.pcap) | NetBIOS | 196,628 | pcap | 200 | 2026-09-28 |  |
| C513 | [NetBIOS/Snagate.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/NetBIOS/Snagate.pcap) | NetBIOS | 13,573 | pcap | 200 | 2026-09-28 |  |
| C514 | [LLDP/lldp.minimal.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LLDP/lldp.minimal.pcap) | LLDP | 104 | pcap | 200 | 2026-09-28 |  |
| C515 | [LLDP/LLDP.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LLDP/LLDP.pcap) | LLDP | 4,108 | pcap | 200 | 2026-09-28 |  |
| C516 | [LLDP/lldpmed_civicloc.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LLDP/lldpmed_civicloc.pcap) | LLDP | 308 | pcap | 200 | 2026-09-28 |  |
| C517 | [LLDP/simens.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LLDP/simens.pcap) | LLDP | 251,828 | pcapng | 200 | 2026-09-28 |  |
| C518 | [LLDP/lldp.detailed.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LLDP/lldp.detailed.pcap) | LLDP | 303 | pcap | 200 | 2026-09-28 |  |
| C519 | [BacNET/BACnet-exception-schedule-property-1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnet-exception-schedule-property-1.pcap) | BacNET | 492 | pcapng | 200 | 2026-09-28 |  |
| C520 | [BacNET/bacnet-services.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet-services.pcap) | BacNET | 649,998 | pcap | 200 | 2026-09-28 |  |
| C521 | [BacNET/bacnet_test.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet_test.pcap) | BacNET | 1,956 | pcap | 200 | 2026-09-28 |  |
| C522 | [BacNET/BACnetARRAY-elements.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnetARRAY-elements.pcap) | BacNET | 3,339 | pcap | 200 | 2026-09-28 |  |
| C523 | [BacNET/BACnetARRAY-element-0.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnetARRAY-element-0.pcap) | BacNET | 495 | pcap | 200 | 2026-09-28 |  |
| C524 | [BacNET/bacnet-ip.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet-ip.pcap) | BacNET | 69,015 | pcap | 200 | 2026-09-28 |  |
| C525 | [BacNET/bacnet-arcnet.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet-arcnet.pcap) | BacNET | 22,743 | pcap | 200 | 2026-09-28 |  |
| C526 | [BacNET/mstp_20090227094623.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/mstp_20090227094623.pcap) | BacNET | 23,982 | pcap | 200 | 2026-09-28 |  |
| C527 | [BacNET/bacnet-properties.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet-properties.pcap) | BacNET | 251,735 | pcap | 200 | 2026-09-28 |  |
| C528 | [BacNET/bacnet-ethernet-device.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet-ethernet-device.pcap) | BacNET | 10,713 | pcap | 200 | 2026-09-28 |  |
| C529 | [BacNET/BACnetIP-MSTP-Mix.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnetIP-MSTP-Mix.pcap) | BacNET | 118,053 | pcap | 200 | 2026-09-28 |  |
| C530 | [BacNET/bacnet-ethernet.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/bacnet-ethernet.pcap) | BacNET | 56,636 | pcap | 200 | 2026-09-28 |  |
| C531 | [BacNET/BACnetL_SchedRPM.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnetL_SchedRPM.pcap) | BacNET | 596 | pcapng | 200 | 2026-09-28 |  |
| C532 | [BacNET/BACnet-MSTP-SNAP-Mixed.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnet-MSTP-SNAP-Mixed.pcap) | BacNET | 113,787 | pcap | 200 | 2026-09-28 |  |
| C533 | [BacNET/BACnetDeviceObjectReference.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnetDeviceObjectReference.pcap) | BacNET | 582 | pcap | 200 | 2026-09-28 |  |
| C534 | [BacNET/BACnet-exception-schedule-property-2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnet-exception-schedule-property-2.pcap) | BacNET | 504 | pcapng | 200 | 2026-09-28 |  |
| C535 | [BacNET/BACnet-BBMD-on-same-subnet.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BacNET/BACnet-BBMD-on-same-subnet.pcap) | BacNET | 1,298 | pcap | 200 | 2026-09-28 |  |
| C536 | [EIGRP/EIGRP_Neighbors.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/EIGRP/EIGRP_Neighbors.pcap) | EIGRP | 1,304 | pcap | 200 | 2026-09-28 |  |
| C537 | [Profinet/pro5.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro5.pcap) | Profinet | 1,032 | pcap | 200 | 2026-09-28 |  |
| C538 | [Profinet/pro.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro.pcap) | Profinet | 783 | pcap | 200 | 2026-09-28 |  |
| C539 | [Profinet/pro4.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro4.pcap) | Profinet | 8,965 | pcap | 200 | 2026-09-28 |  |
| C540 | [Profinet/pro3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro3.pcap) | Profinet | 572 | pcap | 200 | 2026-09-28 |  |
| C541 | [Profinet/pro2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro2.pcap) | Profinet | 211 | pcap | 200 | 2026-09-28 |  |
| C542 | [Profinet/pro1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro1.pcap) | Profinet | 532 | pcap | 200 | 2026-09-28 |  |
| C543 | [Profinet/pro6.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Profinet/pro6.pcap) | Profinet | 450 | pcap | 200 | 2026-09-28 |  |
| C544 | [EtherCat/valve.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/EtherCat/valve.pcap) | EtherCat | 8,772,488 | pcapng | 200 | 2026-09-28 |  |
| C545 | [EtherCat/ethercat.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/EtherCat/ethercat.pcap) | EtherCat | 157,462 | pcap | 200 | 2026-09-28 |  |
| C546 | [OPC-UA/OPC_Server.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OPC-UA/OPC_Server.pcap) | OPC-UA | 3,548 | pcap | 200 | 2026-09-28 |  |
| C547 | [OPC-UA/opycua_share.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OPC-UA/opycua_share.pcap) | OPC-UA | 1,232 | pcap | 200 | 2026-09-28 |  |
| C548 | [OPC-UA/opc.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OPC-UA/opc.pcap) | OPC-UA | 46,516 | pcap | 200 | 2026-09-28 |  |
| C549 | [CIP/CIPvalue.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CIP/CIPvalue.pcap) | CIP | 3,183,533 | pcap | 200 | 2026-09-28 |  |
| C550 | [CIP/CIP.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CIP/CIP.pcap) | CIP | 7,684,492 | pcap | 200 | 2026-09-28 |  |
| C551 | [CIP/specialCIP.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CIP/specialCIP.pcap) | CIP | 29,825 | pcap | 200 | 2026-09-28 |  |
| C552 | [CIP/cip_only.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CIP/cip_only.pcap) | CIP | 2,721,649 | pcap | 200 | 2026-09-28 |  |
| C553 | [CIP/ENIP_CIP-CM.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CIP/ENIP_CIP-CM.pcap) | CIP | 2,850 | pcap | 200 | 2026-09-28 |  |
| C554 | [AMQP/pkts.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/AMQP/pkts.pcap) | AMQP | 4,490 | pcap | 200 | 2026-09-28 |  |
| C555 | [AMQP/AMQP_Sample.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/AMQP/AMQP_Sample.pcap) | AMQP | 4,727 | pcap | 200 | 2026-09-28 |  |
| C556 | [AMQP/amqp_gssapi.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/AMQP/amqp_gssapi.pcap) | AMQP | 3,984,108 | pcap | 200 | 2026-09-28 |  |
| C557 | [Malware/ICMP_over_L2TPv3_Pseudowire.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Malware/ICMP_over_L2TPv3_Pseudowire.pcap) | Malware | 5,402 | pcap | 200 | 2026-09-28 |  |
| C558 | [Malware/malware_exec.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Malware/malware_exec.pcap) | Malware | 174,052 | pcapng | 200 | 2026-09-28 |  |
| C559 | [Malware/4SICS-GeekLounge-151020.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Malware/4SICS-GeekLounge-151020.pcap) | Malware | 25,711,082 | pcap | 200 | 2026-09-28 |  |
| C560 | [STP/stp2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/STP/stp2.pcap) | STP | 2,304 | pcap | 200 | 2026-09-28 |  |
| C561 | [STP/stp1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/STP/stp1.pcap) | STP | 2,304 | pcap | 200 | 2026-09-28 |  |
| C562 | [PowerlinkEPL/eplexample.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/PowerlinkEPL/eplexample.pcap) | PowerlinkEPL | 130,748 | pcap | 200 | 2026-09-28 |  |
| C563 | [PowerlinkEPL/epl_v1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/PowerlinkEPL/epl_v1.pcap) | PowerlinkEPL | 6,864 | pcap | 200 | 2026-09-28 |  |
| C564 | [PowerlinkEPL/epl.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/PowerlinkEPL/epl.pcap) | PowerlinkEPL | 5,252 | pcap | 200 | 2026-09-28 |  |
| C565 | [S7COMM/s3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s3.pcap) | S7COMM | 25,112 | pcap | 200 | 2026-09-28 |  |
| C566 | [S7COMM/ıcs.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/%C4%B1cs.pcap) | S7COMM | 33,554,432 | pcapng | 200 | 2026-09-28 |  |
| C567 | [S7COMM/s2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s2.pcap) | S7COMM | 13,981 | pcap | 200 | 2026-09-28 |  |
| C568 | [S7COMM/s71.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s71.pcap) | S7COMM | 6,856,479 | pcap | 200 | 2026-09-28 |  |
| C569 | [S7COMM/s5.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s5.pcap) | S7COMM | 2,846 | pcap | 200 | 2026-09-28 |  |
| C570 | [S7COMM/s7edit.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s7edit.pcap) | S7COMM | 25,711,082 | pcap | 200 | 2026-09-28 |  |
| C571 | [S7COMM/s4.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s4.pcap) | S7COMM | 5,355 | pcap | 200 | 2026-09-28 |  |
| C572 | [S7COMM/1-S7comm-VarService-Read-DB1DBD0.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/1-S7comm-VarService-Read-DB1DBD0.pcap) | S7COMM | 3,469 | pcap | 200 | 2026-09-28 |  |
| C573 | [S7COMM/S7.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/S7.pcap) | S7COMM | 48,588,976 | pcapng | 200 | 2026-09-28 |  |
| C574 | [S7COMM/s73.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s73.pcap) | S7COMM | 15,376,579 | pcap | 200 | 2026-09-28 |  |
| C575 | [S7COMM/s72.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s72.pcap) | S7COMM | 24,963,345 | pcap | 200 | 2026-09-28 |  |
| C576 | [S7COMM/s6.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s6.pcap) | S7COMM | 1,566,710 | pcap | 200 | 2026-09-28 |  |
| C577 | [S7COMM/icss7.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/icss7.pcap) | S7COMM | 906,880 | pcap | 200 | 2026-09-28 |  |
| C578 | [S7COMM/2-S7comm-VarService-CyclicData-1s.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/2-S7comm-VarService-CyclicData-1s.pcap) | S7COMM | 72,518 | pcap | 200 | 2026-09-28 |  |
| C579 | [S7COMM/s1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s1.pcap) | S7COMM | 9,523 | pcap | 200 | 2026-09-28 |  |
| C580 | [S7COMM/s7soru.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/S7COMM/s7soru.pcap) | S7COMM | 906,880 | pcap | 200 | 2026-09-28 |  |
| C581 | [RTPS/rtps_cooked.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/RTPS/rtps_cooked.pcap) | RTPS | 3,800 | pcapng | 200 | 2026-09-28 |  |
| C582 | [RTPS/rtps.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/RTPS/rtps.pcap) | RTPS | 242,762 | pcap | 200 | 2026-09-28 |  |
| C583 | [RTPS/LocalCapture_ShapeDemo.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/RTPS/LocalCapture_ShapeDemo.pcap) | RTPS | 304,408 | pcapng | 200 | 2026-09-28 |  |
| C584 | [Ultimate/TheUltimate.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Ultimate/TheUltimate.pcap) | Ultimate | 7,088,184 | pcapng | 200 | 2026-09-28 |  |
| C585 | [HTTP/http-chunked-gzip.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HTTP/http-chunked-gzip.pcap) | HTTP | 29,517 | pcap | 200 | 2026-09-28 |  |
| C586 | [HTTP/http_gzip.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HTTP/http_gzip.pcap) | HTTP | 1,707 | pcap | 200 | 2026-09-28 |  |
| C587 | [HTTP/Safari-Array-Integer-Overflow-PoC.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HTTP/Safari-Array-Integer-Overflow-PoC.pcap) | HTTP | 29,346 | pcap | 200 | 2026-09-28 |  |
| C588 | [HTTP/frozenyogurtposrevelsystems.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HTTP/frozenyogurtposrevelsystems.pcap) | HTTP | 3,260 | pcap | 200 | 2026-09-28 |  |
| C589 | [HTTP/http.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HTTP/http.pcap) | HTTP | 25,803 | pcap | 200 | 2026-09-28 |  |
| C590 | [LonTalk/Lon.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LonTalk/Lon.pcap) | LonTalk | 1,062,555 | pcap | 200 | 2026-09-28 |  |
| C591 | [DHCP/dhcp_server.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/dhcp_server.pcap) | DHCP | 1,458 | pcap | 200 | 2026-09-28 |  |
| C592 | [DHCP/PRIV_bootp-both_overload.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/PRIV_bootp-both_overload.pcap) | DHCP | 364 | pcap | 200 | 2026-09-28 |  |
| C593 | [DHCP/dhcp-discover.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/dhcp-discover.pcap) | DHCP | 649 | pcap | 200 | 2026-09-28 |  |
| C594 | [DHCP/dhcp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/dhcp.pcap) | DHCP | 1,400 | pcap | 200 | 2026-09-28 |  |
| C595 | [DHCP/dhcp-relay-serverside.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/dhcp-relay-serverside.pcap) | DHCP | 2,388 | pcap | 200 | 2026-09-28 |  |
| C596 | [DHCP/dhcp-auth.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/dhcp-auth.pcap) | DHCP | 265 | gzip | 200 | 2026-09-28 | Upstream file is gzip-compressed despite .pcap name; decompress before use |
| C597 | [DHCP/dhcp_client.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/dhcp_client.pcap) | DHCP | 1,458 | pcap | 200 | 2026-09-28 |  |
| C598 | [DHCP/PRIV_bootp-both_overload_empty-no_end.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DHCP/PRIV_bootp-both_overload_empty-no_end.pcap) | DHCP | 364 | pcap | 200 | 2026-09-28 |  |
| C599 | [BOOTP/DHCP.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BOOTP/DHCP.pcap) | BOOTP | 1,906 | pcap | 200 | 2026-09-28 |  |
| C600 | [BOOTP/bootp-both.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BOOTP/bootp-both.pcap) | BOOTP | 364 | pcap | 200 | 2026-09-28 |  |
| C601 | [BOOTP/dhcp-auth1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BOOTP/dhcp-auth1.pcap) | BOOTP | 265 | gzip | 200 | 2026-09-28 | Upstream file is gzip-compressed despite .pcap name; decompress before use |
| C602 | [BOOTP/bootpbot.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BOOTP/bootpbot.pcap) | BOOTP | 364 | pcap | 200 | 2026-09-28 |  |
| C603 | [BOOTP/dhcp-auth.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BOOTP/dhcp-auth.pcap) | BOOTP | 458 | pcap | 200 | 2026-09-28 |  |
| C604 | [BOOTP/packet.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BOOTP/packet.pcap) | BOOTP | 691,181 | pcap | 200 | 2026-09-28 |  |
| C605 | [COTP/cotp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/cotp.pcap) | COTP | 541,172 | pcap | 200 | 2026-09-28 |  |
| C606 | [COTP/iec61850_release.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/iec61850_release.pcap) | COTP | 1,568 | pcap | 200 | 2026-09-28 |  |
| C607 | [COTP/pro4.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/pro4.pcap) | COTP | 8,965 | pcap | 200 | 2026-09-28 |  |
| C608 | [COTP/OPC_Server.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/OPC_Server.pcap) | COTP | 3,548 | pcap | 200 | 2026-09-28 |  |
| C609 | [COTP/CotpAnalog.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/CotpAnalog.pcap) | COTP | 41,509 | pcap | 200 | 2026-09-28 |  |
| C610 | [COTP/stp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/stp.pcap) | COTP | 5,520 | pcapng | 200 | 2026-09-28 |  |
| C611 | [COTP/cip_cotp_proces.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/cip_cotp_proces.pcap) | COTP | 1,588,319 | pcap | 200 | 2026-09-28 |  |
| C612 | [COTP/cotprevize.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/COTP/cotprevize.pcap) | COTP | 519,968 | pcapng | 200 | 2026-09-28 |  |
| C613 | [Zigbee/zigbee3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbee3.pcap) | Zigbee | 58,287 | pcap | 200 | 2026-09-28 |  |
| C614 | [Zigbee/zigbee2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbee2.pcap) | Zigbee | 58,287 | pcap | 200 | 2026-09-28 |  |
| C615 | [Zigbee/zigbee5.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbee5.pcap) | Zigbee | 1,502 | gzip | 200 | 2026-09-28 | Upstream file is gzip-compressed despite .pcap name; decompress before use |
| C616 | [Zigbee/zigbee4.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbee4.pcap) | Zigbee | 58,177 | pcap | 200 | 2026-09-28 |  |
| C617 | [Zigbee/multihop_nd_aug5.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/multihop_nd_aug5.pcap) | Zigbee | 2,098 | pcap | 200 | 2026-09-28 |  |
| C618 | [Zigbee/zigbee.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbee.pcap) | Zigbee | 2,063 | pcap | 200 | 2026-09-28 |  |
| C619 | [Zigbee/zigbee1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbee1.pcap) | Zigbee | 58,641 | pcap | 200 | 2026-09-28 |  |
| C620 | [Zigbee/zigbec.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Zigbee/zigbec.pcap) | Zigbee | 21,369 | pcap | 200 | 2026-09-28 |  |
| C621 | [CANopen/CANopen.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CANopen/CANopen.pcap) | CANopen | 1,060 | pcap | 200 | 2026-09-28 |  |
| C622 | [OMRON/omron3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OMRON/omron3.pcap) | OMRON | 20,831 | pcap | 200 | 2026-09-28 |  |
| C623 | [OMRON/omron.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OMRON/omron.pcap) | OMRON | 20,831 | pcap | 200 | 2026-09-28 |  |
| C624 | [OMRON/omron2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OMRON/omron2.pcap) | OMRON | 8,506 | pcap | 200 | 2026-09-28 |  |
| C625 | [OMRON/omron1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OMRON/omron1.pcap) | OMRON | 8,177 | pcap | 200 | 2026-09-28 |  |
| C626 | [OMRON/omrontest.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/OMRON/omrontest.pcap) | OMRON | 1,582 | pcap | 200 | 2026-09-28 |  |
| C627 | [ARP/arp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/ARP/arp.pcap) | ARP | 184 | pcap | 200 | 2026-09-28 |  |
| C628 | [MQTT/mqtt.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MQTT/mqtt.pcap) | MQTT | 1,813 | pcap | 200 | 2026-09-28 |  |
| C629 | [MQTT/mqtt.example.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MQTT/mqtt.example.pcap) | MQTT | 1,506 | pcap | 200 | 2026-09-28 |  |
| C630 | [MQTT/mqtt_user_credentials.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MQTT/mqtt_user_credentials.pcap) | MQTT | 4,276 | pcap | 200 | 2026-09-28 |  |
| C631 | [HPSW/hp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HPSW/hp.pcap) | HPSW | 270 | pcap | 200 | 2026-09-28 |  |
| C632 | [DICOM/dicom_association.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DICOM/dicom_association.pcap) | DICOM | 18,977 | pcap | 200 | 2026-09-28 |  |
| C633 | [DICOM/DICOM.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DICOM/DICOM.pcap) | DICOM | 2,802 | pcap | 200 | 2026-09-28 |  |
| C634 | [MODBUS/modbus-encapsulated-transport.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/modbus-encapsulated-transport.pcap) | MODBUS | 606 | pcap | 200 | 2026-09-28 |  |
| C635 | [MODBUS/FC1-permit.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/FC1-permit.pcap) | MODBUS | 3,138 | pcap | 200 | 2026-09-28 |  |
| C636 | [MODBUS/modbus_test_data_part2.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/modbus_test_data_part2.pcap) | MODBUS | 27,764 | pcap | 200 | 2026-09-28 |  |
| C637 | [MODBUS/modbus-read-write-multiple-registers.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/modbus-read-write-multiple-registers.pcap) | MODBUS | 614 | pcap | 200 | 2026-09-28 |  |
| C638 | [MODBUS/Modbus.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/Modbus.pcap) | MODBUS | 8,337 | pcap | 200 | 2026-09-28 |  |
| C639 | [MODBUS/crash.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/crash.pcap) | MODBUS | 722 | pcap | 200 | 2026-09-28 |  |
| C640 | [MODBUS/modbus_test_data_part1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/modbus_test_data_part1.pcap) | MODBUS | 10,181 | pcap | 200 | 2026-09-28 |  |
| C641 | [MODBUS/modbus-mask-write-register.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/MODBUS/modbus-mask-write-register.pcap) | MODBUS | 612 | pcap | 200 | 2026-09-28 |  |
| C642 | [DNP3/dnp3_write.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3_write.pcap) | DNP3 | 610 | pcap | 200 | 2026-09-28 |  |
| C643 | [DNP3/dnpanalogIN.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpanalogIN.pcap) | DNP3 | 5,677 | pcap | 200 | 2026-09-28 |  |
| C644 | [DNP3/dnp3.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3.pcap) | DNP3 | 18,790 | pcap | 200 | 2026-09-28 |  |
| C645 | [DNP3/DNP3ValueAnalog.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/DNP3ValueAnalog.pcap) | DNP3 | 13,321 | pcap | 200 | 2026-09-28 |  |
| C646 | [DNP3/dnpbinaryOut.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpbinaryOut.pcap) | DNP3 | 5,413 | pcap | 200 | 2026-09-28 |  |
| C647 | [DNP3/warmrestart.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/warmrestart.pcap) | DNP3 | 792 | pcap | 200 | 2026-09-28 |  |
| C648 | [DNP3/dnp3_read.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3_read.pcap) | DNP3 | 603 | pcap | 200 | 2026-09-28 |  |
| C649 | [DNP3/DNP3ValueBinary.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/DNP3ValueBinary.pcap) | DNP3 | 5,135 | pcap | 200 | 2026-09-28 |  |
| C650 | [DNP3/dnpDobleIN.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpDobleIN.pcap) | DNP3 | 12,503 | pcap | 200 | 2026-09-28 |  |
| C651 | [DNP3/dnpCounter.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpCounter.pcap) | DNP3 | 10,743 | pcap | 200 | 2026-09-28 |  |
| C652 | [DNP3/dnp3_select_operate.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3_select_operate.pcap) | DNP3 | 936 | pcap | 200 | 2026-09-28 |  |
| C653 | [DNP3/dnpbinaryIN.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpbinaryIN.pcap) | DNP3 | 5,947 | pcap | 200 | 2026-09-28 |  |
| C654 | [DNP3/dnp3value.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3value.pcap) | DNP3 | 142,014 | pcap | 200 | 2026-09-28 |  |
| C655 | [DNP3/dnpVırtOutput.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpV%C4%B1rtOutput.pcap) | DNP3 | 3,120 | pcap | 200 | 2026-09-28 |  |
| C656 | [DNP3/dnp3_test_data_part1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3_test_data_part1.pcap) | DNP3 | 15,838 | pcap | 200 | 2026-09-28 |  |
| C657 | [DNP3/binaryoutSelectOp.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/binaryoutSelectOp.pcap) | DNP3 | 2,581 | pcap | 200 | 2026-09-28 |  |
| C658 | [DNP3/dnp3dataset_capturerem_to_cite_the_paper.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnp3dataset_capturerem_to_cite_the_paper.pcap) | DNP3 | 2,721,421 | pcap | 200 | 2026-09-28 |  |
| C659 | [DNP3/dnpOcteString.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpOcteString.pcap) | DNP3 | 10,896 | pcap | 200 | 2026-09-28 |  |
| C660 | [DNP3/dnpanalogOut.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/DNP3/dnpanalogOut.pcap) | DNP3 | 18,884 | pcap | 200 | 2026-09-28 |  |
| C661 | [HART_IP/hart_ip.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/HART_IP/hart_ip.pcap) | HART_IP | 11,932 | pcapng | 200 | 2026-09-28 |  |
| C662 | [LocalPCAP/enip.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/enip.pcap) | LocalPCAP | 540,000 | pcap | 200 | 2026-09-28 |  |
| C663 | [LocalPCAP/plc1.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/plc1.pcap) | LocalPCAP | 46,527 | pcap | 200 | 2026-09-28 |  |
| C664 | [LocalPCAP/104value.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/104value.pcap) | LocalPCAP | 30,381 | pcap | 200 | 2026-09-28 |  |
| C665 | [LocalPCAP/plc.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/plc.pcap) | LocalPCAP | 65,069 | pcap | 200 | 2026-09-28 |  |
| C666 | [LocalPCAP/similator.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/similator.pcap) | LocalPCAP | 822,134 | pcap | 200 | 2026-09-28 |  |
| C667 | [LocalPCAP/CotpAnalog.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/CotpAnalog.pcap) | LocalPCAP | 41,509 | pcap | 200 | 2026-09-28 |  |
| C668 | [LocalPCAP/ReadCoil.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/ReadCoil.pcap) | LocalPCAP | 7,101 | pcap | 200 | 2026-09-28 |  |
| C669 | [LocalPCAP/ModbusFloat.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/ModbusFloat.pcap) | LocalPCAP | 9,383 | pcap | 200 | 2026-09-28 |  |
| C670 | [LocalPCAP/modbusAnalog.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/modbusAnalog.pcap) | LocalPCAP | 37,818 | pcap | 200 | 2026-09-28 |  |
| C671 | [LocalPCAP/vinci104.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/vinci104.pcap) | LocalPCAP | 814,160 | pcap | 200 | 2026-09-28 |  |
| C672 | [LocalPCAP/104ikiIP.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/104ikiIP.pcap) | LocalPCAP | 42,118 | pcap | 200 | 2026-09-28 |  |
| C673 | [LocalPCAP/ICSHoneypod.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/ICSHoneypod.pcap) | LocalPCAP | 20,344,752 | pcap | 200 | 2026-09-28 |  |
| C674 | [LocalPCAP/hmı.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/hm%C4%B1.pcap) | LocalPCAP | 1,044,048 | pcap | 200 | 2026-09-28 |  |
| C675 | [LocalPCAP/İllegalFunction.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/%C4%B0llegalFunction.pcap) | LocalPCAP | 9,258 | pcap | 200 | 2026-09-28 |  |
| C676 | [LocalPCAP/cip_cotp_proces.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/cip_cotp_proces.pcap) | LocalPCAP | 1,588,319 | pcap | 200 | 2026-09-28 |  |
| C677 | [LocalPCAP/WriteMultipleCoil.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/LocalPCAP/WriteMultipleCoil.pcap) | LocalPCAP | 4,072 | pcap | 200 | 2026-09-28 |  |
| C678 | [CoAP/post.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CoAP/post.pcap) | CoAP | 960 | pcap | 200 | 2026-09-28 |  |
| C679 | [CoAP/coap23.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CoAP/coap23.pcap) | CoAP | 492 | pcapng | 200 | 2026-09-28 |  |
| C680 | [CoAP/coap.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CoAP/coap.pcap) | CoAP | 538 | pcap | 200 | 2026-09-28 |  |
| C681 | [CoAP/coap45.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CoAP/coap45.pcap) | CoAP | 4,692 | pcap | 200 | 2026-09-28 |  |
| C682 | [CoAP/coap12.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CoAP/coap12.pcap) | CoAP | 110 | pcap | 200 | 2026-09-28 |  |
| C683 | [CoAP/seperate.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/CoAP/seperate.pcap) | CoAP | 492 | pcap | 200 | 2026-09-28 |  |
| C684 | [BSAAP/Paging_Request.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BSAAP/Paging_Request.pcap) | BSAAP | 4,307 | pcap | 200 | 2026-09-28 |  |
| C685 | [BSAAP/raaw-call.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BSAAP/raaw-call.pcap) | BSAAP | 46,200 | pcap | 200 | 2026-09-28 |  |
| C686 | [BSAAP/bssmap_bsc_invoke_trace.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/BSAAP/bssmap_bsc_invoke_trace.pcap) | BSAAP | 156 | pcap | 200 | 2026-09-28 |  |
| C687 | [Ethernet_IP/ControlLogix_FactoryTalk_HMI.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Ethernet_IP/ControlLogix_FactoryTalk_HMI.pcap) | Ethernet_IP | 99,802 | pcap | 200 | 2026-09-28 |  |
| C688 | [Ethernet_IP/mb.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Ethernet_IP/mb.pcap) | Ethernet_IP | 7,684,492 | pcap | 200 | 2026-09-28 |  |
| C689 | [Ethernet_IP/ControlLogix_Logix5000_download_upload_run.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Ethernet_IP/ControlLogix_Logix5000_download_upload_run.pcap) | Ethernet_IP | 80,790 | pcap | 200 | 2026-09-28 |  |
| C690 | [Ethernet_IP/EthernetIP-CIP.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Ethernet_IP/EthernetIP-CIP.pcap) | Ethernet_IP | 2,084,906 | pcap | 200 | 2026-09-28 |  |
| C691 | [Ethernet_IP/ENIP_CIP-CM.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Ethernet_IP/ENIP_CIP-CM.pcap) | Ethernet_IP | 2,850 | pcap | 200 | 2026-09-28 |  |
| C692 | [Mergecap/kokteyl.pcap](https://raw.githubusercontent.com/EmreEkin/ICS-Pcaps/master/Mergecap/kokteyl.pcap) | Mergecap | 109,128 | pcapng | 200 | 2026-09-28 |  |

## R17 — ICS CTF traffic (Modbus/TCP and S7comm)

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R17.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C693 | [ics.pcapng](https://raw.githubusercontent.com/NewBee119/ctf_ics_traffic/master/ics.pcapng) | root | 48,588,976 | pcapng | 200 | 2026-09-28 |  |

## R18 — ControlThings ct-samples protocol captures

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R18.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C694 | [SBus/SBus-Ethernet/SBus-Ethernet.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/SBus/SBus-Ethernet/SBus-Ethernet.pcap) | SBus | 66,825 | pcap | 200 | 2026-09-28 |  |
| C695 | [IEC61850/piccolo.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/piccolo.pcap) | IEC61850 | 838 | pcap | 200 | 2026-09-28 |  |
| C696 | [IEC61850/m-send-req.mms.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/m-send-req.mms.pcap) | IEC61850 | 24,777 | pcap | 200 | 2026-09-28 |  |
| C697 | [IEC61850/8d7c7db0-9804-012b-b2a6-0016cb8cea27.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/8d7c7db0-9804-012b-b2a6-0016cb8cea27.pcap) | IEC61850 | 54,287 | pcap | 200 | 2026-09-28 |  |
| C698 | [IEC61850/Sample_File_MMS_and_GOOSE.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/Sample_File_MMS_and_GOOSE.pcap) | IEC61850 | 43,379 | pcap | 200 | 2026-09-28 |  |
| C699 | [IEC61850/MMS - Specific Commands/mms-resumeRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-resumeRequest.pcap) | IEC61850 | 1,577 | pcap | 200 | 2026-09-28 |  |
| C700 | [IEC61850/MMS - Specific Commands/iec61850_read.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/iec61850_read.pcap) | IEC61850 | 1,915 | pcap | 200 | 2026-09-28 |  |
| C701 | [IEC61850/MMS - Specific Commands/mms-confirmedRequestPDU.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-confirmedRequestPDU.pcap) | IEC61850 | 1,548 | pcap | 200 | 2026-09-28 |  |
| C702 | [IEC61850/MMS - Specific Commands/mms-killRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-killRequest.pcap) | IEC61850 | 1,577 | pcap | 200 | 2026-09-28 |  |
| C703 | [IEC61850/MMS - Specific Commands/iec61850_get_name_list.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/iec61850_get_name_list.pcap) | IEC61850 | 1,905 | pcap | 200 | 2026-09-28 |  |
| C704 | [IEC61850/MMS - Specific Commands/mms-initiateDownloadSequence.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-initiateDownloadSequence.pcap) | IEC61850 | 1,905 | pcap | 200 | 2026-09-28 |  |
| C705 | [IEC61850/MMS - Specific Commands/mms-deleteProgramInvocation.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-deleteProgramInvocation.pcap) | IEC61850 | 1,576 | pcap | 200 | 2026-09-28 |  |
| C706 | [IEC61850/MMS - Specific Commands/iec61850_release.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/iec61850_release.pcap) | IEC61850 | 1,568 | pcap | 200 | 2026-09-28 |  |
| C707 | [IEC61850/MMS - Specific Commands/iec61850_get_variable_access_attributes.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/iec61850_get_variable_access_attributes.pcap) | IEC61850 | 1,902 | pcap | 200 | 2026-09-28 |  |
| C708 | [IEC61850/MMS - Specific Commands/mms-startRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-startRequest.pcap) | IEC61850 | 1,906 | pcap | 200 | 2026-09-28 |  |
| C709 | [IEC61850/MMS - Specific Commands/mms-initiateUploadSequence.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-initiateUploadSequence.pcap) | IEC61850 | 1,572 | pcap | 200 | 2026-09-28 |  |
| C710 | [IEC61850/MMS - Specific Commands/mms-resetRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-resetRequest.pcap) | IEC61850 | 1,577 | pcap | 200 | 2026-09-28 |  |
| C711 | [IEC61850/MMS - Specific Commands/mms-cancelRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-cancelRequest.pcap) | IEC61850 | 1,546 | pcap | 200 | 2026-09-28 |  |
| C712 | [IEC61850/MMS - Specific Commands/mms-terminateUploadSequence.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-terminateUploadSequence.pcap) | IEC61850 | 1,884 | pcap | 200 | 2026-09-28 |  |
| C713 | [IEC61850/MMS - Specific Commands/mms-getAlarmSummary.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-getAlarmSummary.pcap) | IEC61850 | 1,557 | pcap | 200 | 2026-09-28 |  |
| C714 | [IEC61850/MMS - Specific Commands/iec61850_write.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/iec61850_write.pcap) | IEC61850 | 1,913 | pcap | 200 | 2026-09-28 |  |
| C715 | [IEC61850/MMS - Specific Commands/mms-stopRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-stopRequest.pcap) | IEC61850 | 1,906 | pcap | 200 | 2026-09-28 |  |
| C716 | [IEC61850/MMS - Specific Commands/mms-getDomainAttributes.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-getDomainAttributes.pcap) | IEC61850 | 1,568 | pcap | 200 | 2026-09-28 |  |
| C717 | [IEC61850/MMS - Specific Commands/mms-relinquishControl.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-relinquishControl.pcap) | IEC61850 | 1,881 | pcap | 200 | 2026-09-28 |  |
| C718 | [IEC61850/MMS - Specific Commands/mms-takeControl.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-takeControl.pcap) | IEC61850 | 1,881 | pcap | 200 | 2026-09-28 |  |
| C719 | [IEC61850/MMS - Specific Commands/mms-readRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/MMS%20-%20Specific%20Commands/mms-readRequest.pcap) | IEC61850 | 1,277 | pcap | 200 | 2026-09-28 |  |
| C720 | [IEC61850/GOOSE/GOOSE.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/GOOSE/GOOSE.pcap) | IEC61850 | 1,420 | pcap | 200 | 2026-09-28 |  |
| C721 | [IEC61850/GOOSE/GOOSE_DEMO.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/GOOSE/GOOSE_DEMO.pcap) | IEC61850 | 166 | pcap | 200 | 2026-09-28 |  |
| C722 | [IEC61850/GOOSE/Sample_File_GOOSE.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/GOOSE/Sample_File_GOOSE.pcap) | IEC61850 | 117,736 | pcap | 200 | 2026-09-28 |  |
| C723 | [IEC61850/GOOSE/GE - Multilin UR - Digital Protection Relay/Routable-GOOSE.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/GOOSE/GE%20-%20Multilin%20UR%20-%20Digital%20Protection%20Relay/Routable-GOOSE.pcap) | IEC61850 | 3,745 | pcap | 200 | 2026-09-28 |  |
| C724 | [IEC61850/GOOSE/GE - Multilin UR - Digital Protection Relay/GOOSE and MMS.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC61850/GOOSE/GE%20-%20Multilin%20UR%20-%20Digital%20Protection%20Relay/GOOSE%20and%20MMS.pcapng) | IEC61850 | 1,139,812 | pcapng | 200 | 2026-09-28 |  |
| C725 | [DLMS-COSEM/Matousp PCAPs/data2.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data2.pcapng) | DLMS-COSEM | 37,884 | pcapng | 200 | 2026-09-28 |  |
| C726 | [DLMS-COSEM/Matousp PCAPs/data6.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data6.pcapng) | DLMS-COSEM | 36,396 | pcapng | 200 | 2026-09-28 |  |
| C727 | [DLMS-COSEM/Matousp PCAPs/DLMS_list.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/DLMS_list.pcap) | DLMS-COSEM | 1,551 | pcap | 200 | 2026-09-28 |  |
| C728 | [DLMS-COSEM/Matousp PCAPs/DLMSDirector.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/DLMSDirector.pcap) | DLMS-COSEM | 150,687 | pcap | 200 | 2026-09-28 |  |
| C729 | [DLMS-COSEM/Matousp PCAPs/data4.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data4.pcapng) | DLMS-COSEM | 36,492 | pcapng | 200 | 2026-09-28 |  |
| C730 | [DLMS-COSEM/Matousp PCAPs/DLMS_profile.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/DLMS_profile.pcap) | DLMS-COSEM | 1,613 | pcap | 200 | 2026-09-28 |  |
| C731 | [DLMS-COSEM/Matousp PCAPs/data1.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data1.pcapng) | DLMS-COSEM | 4,264 | pcapng | 200 | 2026-09-28 |  |
| C732 | [DLMS-COSEM/Matousp PCAPs/data3.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data3.pcapng) | DLMS-COSEM | 37,884 | pcapng | 200 | 2026-09-28 |  |
| C733 | [DLMS-COSEM/Matousp PCAPs/data7.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data7.pcapng) | DLMS-COSEM | 35,756 | pcapng | 200 | 2026-09-28 |  |
| C734 | [DLMS-COSEM/Matousp PCAPs/original_data.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/original_data.pcapng) | DLMS-COSEM | 26,780 | pcapng | 200 | 2026-09-28 |  |
| C735 | [DLMS-COSEM/Matousp PCAPs/XmlDemo.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/XmlDemo.pcap) | DLMS-COSEM | 11,181 | pcap | 200 | 2026-09-28 |  |
| C736 | [DLMS-COSEM/Matousp PCAPs/dlms.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/dlms.pcap) | DLMS-COSEM | 6,627 | pcap | 200 | 2026-09-28 |  |
| C737 | [DLMS-COSEM/Matousp PCAPs/data5.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DLMS-COSEM/Matousp%20PCAPs/data5.pcapng) | DLMS-COSEM | 36,396 | pcapng | 200 | 2026-09-28 |  |
| C738 | [C12.22/C12.22_over_IPv4.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/C12.22/C12.22_over_IPv4.pcap) | C12.22 | 372 | pcap | 200 | 2026-09-28 |  |
| C739 | [C12.22/C12.22_over_ipv6.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/C12.22/C12.22_over_ipv6.pcap) | C12.22 | 1,443 | pcap | 200 | 2026-09-28 |  |
| C740 | [OPC/OPC UA/opc-ua-ap-method.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/OPC/OPC%20UA/opc-ua-ap-method.pcap) | OPC | 46,516 | pcap | 200 | 2026-09-28 |  |
| C741 | [C37.118/C37.118_2PMUsInSync_TCP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/C37.118/C37.118_2PMUsInSync_TCP.pcap) | C37.118 | 476,901 | pcap | 200 | 2026-09-28 |  |
| C742 | [C37.118/C37.118_1PMU_TCP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/C37.118/C37.118_1PMU_TCP.pcap) | C37.118 | 48,034 | pcap | 200 | 2026-09-28 |  |
| C743 | [C37.118/C37.118_1PMU_UDP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/C37.118/C37.118_1PMU_UDP.pcap) | C37.118 | 38,496 | pcap | 200 | 2026-09-28 |  |
| C744 | [C37.118/C37.118_4in1PMU_TCP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/C37.118/C37.118_4in1PMU_TCP.pcap) | C37.118 | 691,380 | pcap | 200 | 2026-09-28 |  |
| C745 | [BACnet/bacnet-arcnet.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-arcnet.cap) | BACnet | 22,743 | pcap | 200 | 2026-09-28 |  |
| C746 | [BACnet/bacnet-ip.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-ip.cap) | BACnet | 69,015 | pcap | 200 | 2026-09-28 |  |
| C747 | [BACnet/BACnetL_SchedRPM.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnetL_SchedRPM.pcapng) | BACnet | 596 | pcapng | 200 | 2026-09-28 |  |
| C748 | [BACnet/BACnetIP-MSTP-Mix.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnetIP-MSTP-Mix.cap) | BACnet | 118,053 | pcap | 200 | 2026-09-28 |  |
| C749 | [BACnet/BACnet-exception-schedule-property-2.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnet-exception-schedule-property-2.pcapng) | BACnet | 504 | pcapng | 200 | 2026-09-28 |  |
| C750 | [BACnet/bacnet-services.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-services.cap) | BACnet | 649,998 | pcap | 200 | 2026-09-28 |  |
| C751 | [BACnet/bacnet-ethernet-device.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-ethernet-device.cap) | BACnet | 10,713 | pcap | 200 | 2026-09-28 |  |
| C752 | [BACnet/bacnet-stack-services.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-stack-services.cap) | BACnet | 14,514 | pcap | 200 | 2026-09-28 |  |
| C753 | [BACnet/BACnet-MSTP-SNAP-Mixed.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnet-MSTP-SNAP-Mixed.cap) | BACnet | 113,787 | pcap | 200 | 2026-09-28 |  |
| C754 | [BACnet/BACnetARRAY-element-0.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnetARRAY-element-0.cap) | BACnet | 495 | pcap | 200 | 2026-09-28 |  |
| C755 | [BACnet/bacnet-properties.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-properties.cap) | BACnet | 251,735 | pcap | 200 | 2026-09-28 |  |
| C756 | [BACnet/bacnet-ethernet.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/bacnet-ethernet.cap) | BACnet | 56,636 | pcap | 200 | 2026-09-28 |  |
| C757 | [BACnet/BACnet-BBMD-on-same-subnet.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnet-BBMD-on-same-subnet.cap) | BACnet | 1,298 | pcap | 200 | 2026-09-28 |  |
| C758 | [BACnet/BACnetDeviceObjectReference.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnetDeviceObjectReference.pcap) | BACnet | 582 | pcap | 200 | 2026-09-28 |  |
| C759 | [BACnet/BACnetARRAY-elements.cap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnetARRAY-elements.cap) | BACnet | 3,339 | pcap | 200 | 2026-09-28 |  |
| C760 | [BACnet/BACnet-exception-schedule-property-1.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/BACnet/BACnet-exception-schedule-property-1.pcapng) | BACnet | 492 | pcapng | 200 | 2026-09-28 |  |
| C761 | [PROFINET/PROFINET-DCP/ChangeIPUsingDCP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/PROFINET/PROFINET-DCP/ChangeIPUsingDCP.pcap) | PROFINET | 532 | pcap | 200 | 2026-09-28 |  |
| C762 | [EtherCAT/EtherCAT.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/EtherCAT/EtherCAT.pcap) | EtherCAT | 157,462 | pcap | 200 | 2026-09-28 |  |
| C763 | [EthernetIP/Plant1_EthernetIP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/EthernetIP/Plant1_EthernetIP.pcap) | EthernetIP | 2,084,906 | pcap | 200 | 2026-09-28 |  |
| C764 | [S7comm/s7comm_reading_setting_plc_time.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/s7comm_reading_setting_plc_time.pcap) | S7comm | 5,355 | pcap | 200 | 2026-09-28 |  |
| C765 | [S7comm/s7comm_downloading_block_db1.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/s7comm_downloading_block_db1.pcap) | S7comm | 9,523 | pcap | 200 | 2026-09-28 |  |
| C766 | [S7comm/s7comm_program_blocklist_onlineview.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/s7comm_program_blocklist_onlineview.pcap) | S7comm | 13,981 | pcap | 200 | 2026-09-28 |  |
| C767 | [S7comm/s7comm_varservice_libnodavedemo.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/s7comm_varservice_libnodavedemo.pcap) | S7comm | 2,846 | pcap | 200 | 2026-09-28 |  |
| C768 | [S7comm/Plant1_S7comm.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Plant1_S7comm.pcap) | S7comm | 2,186,947 | pcap | 200 | 2026-09-28 |  |
| C769 | [S7comm/s7comm_reading_plc_status.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/s7comm_reading_plc_status.pcap) | S7comm | 25,112 | pcap | 200 | 2026-09-28 |  |
| C770 | [S7comm/s7comm_varservice_libnodavedemo_bench.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/s7comm_varservice_libnodavedemo_bench.pcap) | S7comm | 1,566,710 | pcap | 200 | 2026-09-28 |  |
| C771 | [S7comm/Other_Captures/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync_FehlerbeiMW100.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync_FehlerbeiMW100.pcapng) | S7comm | 18,488 | pcapng | 200 | 2026-09-28 |  |
| C772 | [S7comm/Other_Captures/S7-1511-opc-request-all-types.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/S7-1511-opc-request-all-types.pcap) | S7comm | 10,270 | pcap | 200 | 2026-09-28 |  |
| C773 | [S7comm/Other_Captures/OPC_Server.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/OPC_Server.pcap) | S7comm | 3,548 | pcap | 200 | 2026-09-28 |  |
| C774 | [S7comm/Other_Captures/s7-1200-hmi.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/s7-1200-hmi.pcap) | S7comm | 11,559 | pcap | 200 | 2026-09-28 |  |
| C775 | [S7comm/Other_Captures/S7-1511_db3_var1_HMI.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/S7-1511_db3_var1_HMI.pcap) | S7comm | 7,334 | pcap | 200 | 2026-09-28 |  |
| C776 | [S7comm/Other_Captures/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/V13_1200_TP1200sim_MW100_Int_SPS_5s_MW102_Int_SPS_10s_MW102_ab_1000_Timer_sync.pcapng) | S7comm | 19,948 | pcapng | 200 | 2026-09-28 |  |
| C777 | [S7comm/Other_Captures/S7-1511_db2_var1_HMI.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/S7-1511_db2_var1_HMI.pcap) | S7comm | 6,024 | pcapng | 200 | 2026-09-28 |  |
| C778 | [S7comm/Other_Captures/S7-1511_db6w0_HMI.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/S7-1511_db6w0_HMI.pcap) | S7comm | 3,396 | pcapng | 200 | 2026-09-28 |  |
| C779 | [S7comm/Other_Captures/S7-1200-Uploading-OB1-TIAV12.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/S7comm/Other_Captures/S7-1200-Uploading-OB1-TIAV12.pcap) | S7comm | 19,895 | pcap | 200 | 2026-09-28 |  |
| C780 | [J1939/scapy_uds_scan-TP_DSC_SA.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/J1939/scapy_uds_scan-TP_DSC_SA.pcapng) | J1939 | 182,764 | pcapng | 200 | 2026-09-28 |  |
| C781 | [MirroredBits/MirroredBits.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/MirroredBits/MirroredBits.pcap) | MirroredBits | 441,347 | pcap | 200 | 2026-09-28 |  |
| C782 | [Zigbee/control4-sample.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Zigbee/control4-sample.pcap) | Zigbee | 21,369 | pcap | 200 | 2026-09-28 |  |
| C783 | [Zigbee/zigbee-join-authenticate.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Zigbee/zigbee-join-authenticate.pcap) | Zigbee | 2,822 | pcap | 200 | 2026-09-28 |  |
| C784 | [Zigbee/lightswitch.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Zigbee/lightswitch.pcap) | Zigbee | 80 | pcap | 200 | 2026-09-28 |  |
| C785 | [Zigbee/intermatic-outletswitch-R1.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Zigbee/intermatic-outletswitch-R1.pcap) | Zigbee | 310 | pcap | 200 | 2026-09-28 |  |
| C786 | [HART/HART-IP/hart_ip.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/HART/HART-IP/hart_ip.pcap) | HART | 11,932 | pcapng | 200 | 2026-09-28 |  |
| C787 | [Combined/SANS_HolidayHack_2013.pcap](https://media.githubusercontent.com/media/ControlThings-io/ct-samples/master/Protocols/Combined/SANS_HolidayHack_2013.pcap) | Combined | 168,000,883 | pcap | 200 | 2026-09-28 | Git LFS object; raw URL returns a pointer |
| C788 | [Combined/Plant1.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Combined/Plant1.pcap) | Combined | 7,684,492 | pcap | 200 | 2026-09-28 |  |
| C789 | [Combined/Plant1.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Combined/Plant1.pcapng) | Combined | 8,654,740 | pcapng | 200 | 2026-09-28 |  |
| C790 | [IEC60870/IEC-5-104/090813_diverse.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC60870/IEC-5-104/090813_diverse.pcap) | IEC60870 | 13,952 | pcap | 200 | 2026-09-28 |  |
| C791 | [IEC60870/IEC-5-104/JavaRMI_and_IEC_Misc.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC60870/IEC-5-104/JavaRMI_and_IEC_Misc.pcap) | IEC60870 | 28,889 | pcap | 200 | 2026-09-28 |  |
| C792 | [IEC60870/IEC-5-104/TestDissectIec104.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/IEC60870/IEC-5-104/TestDissectIec104.pcap) | IEC60870 | 11,409 | pcap | 200 | 2026-09-28 |  |
| C793 | [Modbus/ModbusTCP/Plant1_ModbusTCP.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Modbus/ModbusTCP/Plant1_ModbusTCP.pcap) | Modbus | 1,478,608 | pcap | 200 | 2026-09-28 |  |
| C794 | [Modbus/ModbusTCP/Modbus_Firmware_Update.pcapng](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/Modbus/ModbusTCP/Modbus_Firmware_Update.pcapng) | Modbus | 5,093,700 | pcapng | 200 | 2026-09-28 |  |
| C795 | [DNP3/dnp3_request_link_status.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/dnp3_request_link_status.pcap) | DNP3 | 604 | pcap | 200 | 2026-09-28 |  |
| C796 | [DNP3/DNP3RequestLink.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/DNP3RequestLink.pcap) | DNP3 | 880 | pcap | 200 | 2026-09-28 |  |
| C797 | [DNP3/dnp3_write.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/dnp3_write.pcap) | DNP3 | 610 | pcap | 200 | 2026-09-28 |  |
| C798 | [DNP3/DNP3SelectOperateRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/DNP3SelectOperateRequest.pcap) | DNP3 | 880 | pcap | 200 | 2026-09-28 |  |
| C799 | [DNP3/dnp_malformed.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/dnp_malformed.pcap) | DNP3 | 21,136 | pcap | 200 | 2026-09-28 |  |
| C800 | [DNP3/DNP3ReadRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/DNP3ReadRequest.pcap) | DNP3 | 1,096 | pcap | 200 | 2026-09-28 |  |
| C801 | [DNP3/dnp3_read.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/dnp3_read.pcap) | DNP3 | 603 | pcap | 200 | 2026-09-28 |  |
| C802 | [DNP3/dnp3_select_operate.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/dnp3_select_operate.pcap) | DNP3 | 936 | pcap | 200 | 2026-09-28 |  |
| C803 | [DNP3/DNP3WriteRequest.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DNP3/DNP3WriteRequest.pcap) | DNP3 | 962 | pcap | 200 | 2026-09-28 |  |
| C804 | [DoIP/hohohouds_solve.public.pcap](https://raw.githubusercontent.com/ControlThings-io/ct-samples/master/Protocols/DoIP/hohohouds_solve.public.pcap) | DoIP | 2,930,885 | pcap | 200 | 2026-09-28 |  |

## R19 — Nozomi tricotools TRITON/TriStation capture

Host: GitHub raw. Rights: [rights and access](rights-and-access.md) entry R19.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C805 | [malware_exec.pcap](https://raw.githubusercontent.com/NozomiNetworks/tricotools/master/malware_exec.pcap) | root | 174,052 | pcapng | 200 | 2026-09-28 |  |

## R20 — University of Coimbra ICS_PCAPS MODBUSTCP#1

Host: GitHub release asset. Rights: [rights and access](rights-and-access.md) entry R20.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C806 | [captures2.zip](https://github.com/tjcruz-dei/ICS_PCAPS/releases/download/MODBUSTCP%231/captures2.zip) | MODBUSTCP#1 release | 194,810,610 | zip | 200 | 2026-09-28 | Archive; unpack to obtain pcaps |
| C807 | [captures3.zip](https://github.com/tjcruz-dei/ICS_PCAPS/releases/download/MODBUSTCP%231/captures3.zip) | MODBUSTCP#1 release | 224,051,839 | zip | 200 | 2026-09-28 | Archive; unpack to obtain pcaps |
| C808 | [captures1_v2.zip](https://github.com/tjcruz-dei/ICS_PCAPS/releases/download/MODBUSTCP%231/captures1_v2.zip) | MODBUSTCP#1 release | 669,680,240 | zip | 200 | 2026-09-28 | Archive; unpack to obtain pcaps |

## R21 — UOWM IEC 60870-5-104 Intrusion Detection Dataset

Host: Zenodo. Rights: [rights and access](rights-and-access.md) entry R21.

| Capture ID | File | Group / scenario | Size (bytes) | Format | HTTP | Checked | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C809 | [20200425_UOWM_IEC104_Dataset_m_sp_na_1_DoS.7z](https://zenodo.org/api/records/7108614/files/20200425_UOWM_IEC104_Dataset_m_sp_na_1_DoS.7z/content) | m_sp_na_1_DoS | 69,419,855 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C810 | [20200426_UOWM_IEC104_Dataset_c_ci_na_1.7z](https://zenodo.org/api/records/7108614/files/20200426_UOWM_IEC104_Dataset_c_ci_na_1.7z/content) | c_ci_na_1 | 71,204,475 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C811 | [20200426_UOWM_IEC104_Dataset_c_ci_na_1_DoS.7z](https://zenodo.org/api/records/7108614/files/20200426_UOWM_IEC104_Dataset_c_ci_na_1_DoS.7z/content) | c_ci_na_1_DoS | 76,189,847 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C812 | [20200427_UOWM_IEC104_Dataset_c_se_na_1.7z](https://zenodo.org/api/records/7108614/files/20200427_UOWM_IEC104_Dataset_c_se_na_1.7z/content) | c_se_na_1 | 81,958,663 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C813 | [20200428_UOWM_IEC104_Dataset_c_sc_na_1.7z](https://zenodo.org/api/records/7108614/files/20200428_UOWM_IEC104_Dataset_c_sc_na_1.7z/content) | c_sc_na_1 | 82,660,522 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C814 | [20200428_UOWM_IEC104_Dataset_c_se_na_1_DoS.7z](https://zenodo.org/api/records/7108614/files/20200428_UOWM_IEC104_Dataset_c_se_na_1_DoS.7z/content) | c_se_na_1_DoS | 80,825,143 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C815 | [20200429_UOWM_IEC104_Dataset_c_sc_na_1_DoS.7z](https://zenodo.org/api/records/7108614/files/20200429_UOWM_IEC104_Dataset_c_sc_na_1_DoS.7z/content) | c_sc_na_1_DoS | 88,345,077 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C816 | [20200605_UOWM_IEC104_Dataset_c_rd_na_1.7z](https://zenodo.org/api/records/7108614/files/20200605_UOWM_IEC104_Dataset_c_rd_na_1.7z/content) | c_rd_na_1 | 104,566,361 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C817 | [20200605_UOWM_IEC104_Dataset_c_rd_na_1_DoS.7z](https://zenodo.org/api/records/7108614/files/20200605_UOWM_IEC104_Dataset_c_rd_na_1_DoS.7z/content) | c_rd_na_1_DoS | 106,622,557 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C818 | [20200606_UOWM_IEC104_Dataset_c_rp_na_1.7z](https://zenodo.org/api/records/7108614/files/20200606_UOWM_IEC104_Dataset_c_rp_na_1.7z/content) | c_rp_na_1 | 107,022,556 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C819 | [20200606_UOWM_IEC104_Dataset_c_rp_na_1_DoS.7z](https://zenodo.org/api/records/7108614/files/20200606_UOWM_IEC104_Dataset_c_rp_na_1_DoS.7z/content) | c_rp_na_1_DoS | 104,302,179 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C820 | [20200608_UOWM_IEC104_Dataset_mitm_drop.7z](https://zenodo.org/api/records/7108614/files/20200608_UOWM_IEC104_Dataset_mitm_drop.7z/content) | mitm_drop | 102,319,063 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |
| C821 | [Balanced_IEC104_Train_Test_CSV_Files.7z](https://zenodo.org/api/records/7108614/files/Balanced_IEC104_Train_Test_CSV_Files.7z/content) | Balanced train/test CSV | 11,375,113 | 7z | 200 | 2026-09-28 | 7z archive of per-entity pcaps and labelled CSVs |

