# 1.2. Flexible Storage <a href="#_flexible_storage" id="_flexible_storage"></a>

Proxmox VE 的存储模型非常灵活。虚拟机镜像可以存储在一个或多个本地存储上，也可以存储在 NFS 或 SAN 等共享存储上。您可以根据需要配置任意数量的存储定义，并使用 Debian GNU/Linux 可用的所有存储技术。

将虚拟机存储在共享存储上的一个主要优势是，可以在线迁移正在运行的虚拟机而不会造成任何停机，因为集群中的所有节点都可以直接访问虚拟机磁盘镜像。

支持以下网络存储类型：

- LVM 组（以 iSCSI 目标作为网络后端）
- iSCSI 目标
- iSCSI LUN（直接使用）
- NFS 共享
- CIFS 共享
- Ceph RBD
- CephFS
- Proxmox Backup Server

支持以下本地存储类型：

- LVM 组（本地后端设备，如块设备、光纤通道设备和 DRBD）
- 目录（在现有文件系统上存储）
- ZFS

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
