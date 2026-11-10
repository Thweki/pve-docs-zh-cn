# 13.10. Tips and Tricks <a href="#_tips_and_tricks" id="_tips_and_tricks"></a>

## 13.10.1. How to allow FTP <a href="#_how_to_allow_ftp" id="_how_to_allow_ftp"></a>

FTP is an old style protocol which uses port 21 and several other dynamic ports. So you need a rule to accept port 21\. In addition, you need to load the `ip_conntrack_ftp` module. So please run:

```text
modprobe ip_conntrack_ftp
```

and add `ip_conntrack_ftp` to `/etc/modules` (so that it works after a reboot).

## 13.10.2. Suricata IPS integration <a href="#_suricata_ips_integration" id="_suricata_ips_integration"></a>

If you want to use the [Suricata IPS](https://suricata.io/) (Intrusion Prevention System), it’s possible.

Packets will be forwarded to the IPS only after the firewall ACCEPTed them.

Rejected/Dropped firewall packets don’t go to the IPS.

Install suricata on proxmox host:

```text
# apt-get install suricata
# modprobe nfnetlink_queue
```

Don’t forget to add `nfnetlink_queue` to `/etc/modules` for next reboot.

Then, enable IPS for a specific VM with:

```text
# /etc/pve/firewall/<VMID>.fw

[OPTIONS]
ips: 1
ips_queues: 0
```

`ips_queues` will bind a specific cpu queue for this VM.

Available queues are defined in

```text
# /etc/default/suricata
NFQUEUE=0
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
