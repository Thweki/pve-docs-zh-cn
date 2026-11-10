# 12.1. 简介 <a href="#pvesdn_overview" id="pvesdn_overview"></a>

Proxmox VE SDN 使用灵活的软件控制配置，实现虚拟客户机网络的隔离和精细控制。

隔离通过 **区域**、虚拟网络（**VNet**）和 **子网** 管理。区域是独立的虚拟隔离网络区域。VNet 是属于某个区域的虚拟网络。子网是 VNet 内的一个 IP 地址范围。

根据区域类型的不同，网络具有不同的行为，并提供特定的功能、优势和限制。

SDN 的用例包括各个节点上隔离的私有网络，以及跨不同地点的多个 PVE 集群的复杂覆盖网络。

在集群范围的数据中心 SDN 管理界面中配置 VNet 后，它会作为普通 Linux 网桥在每个节点本地可用，可分配给虚拟机和容器。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
