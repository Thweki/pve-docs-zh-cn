# 1.4. High Availability Cluster <a href="#_high_availability_cluster" id="_high_availability_cluster"></a>

A multi-node Proxmox VE HA cluster enables highly available virtual machines and containers. The integrated [High Availability (HA) manager](../15-ha-manager/README.md#chapter_ha_manager) automatically detects node failures using watchdog-based fencing and restarts affected services on healthy nodes. No external tools like Pacemaker are needed—the HA stack ships with Proxmox VE and is configured entirely through the web interface or command line.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
