# 3\. 宿主机系统管理 <a href="#chapter_system_administration" id="chapter_system_administration"></a>

以下各节将重点介绍常见的虚拟化任务，并说明 Proxmox VE 在宿主机管理方面的特定事项。

Proxmox VE 基于 [Debian GNU/Linux](https://www.debian.org/)，并通过额外的软件仓库提供 Proxmox VE 相关软件包。这意味着可以使用全系列的 Debian 软件包，包括安全更新和错误修复。Proxmox VE 提供自己基于 Ubuntu 内核的 Linux 内核。该内核启用了所有必要的虚拟化和容器功能，并包含 [ZFS](https://zfsonlinux.org) 和若干额外的硬件驱动程序。

对于以下各节未涉及的其他主题，请参阅 Debian 文档。[Debian Administrator's Handbook](https://debian-handbook.info/get) 可在线获取，其中全面介绍了 Debian 操作系统（见 [\[Hertzog13\]](../21-bibliography/README.md#Hertzog13)）。

## 本章内容

- [3.1. 软件包仓库](01-sysadmin-package-repositories.md)
- [3.2. 系统软件更新](02-system-software-updates.md)
- [3.3. 固件更新](03-chapter-firmware-updates.md)
- [3.4. 网络配置](04-sysadmin-network-configuration.md)
- [3.5. 时间同步](05-time-synchronization.md)
- [3.6. 外部指标服务器](06-external-metric-server.md)
- [3.7. 磁盘健康监控](07-disk-health-monitoring.md)
- [3.8. 逻辑卷管理器（LVM）](08-chapter-lvm.md)
- [3.9. Linux 上的 ZFS](09-chapter-zfs.md)
- [3.10. BTRFS](10-chapter-btrfs.md)
- [3.11. Proxmox 节点管理](11-proxmox-node-management.md)
- [3.12. 证书管理](12-sysadmin-certificate-management.md)
- [3.13. 宿主机引导加载程序](13-sysboot.md)
- [3.14. 内核同页合并（KSM）](14-kernel-samepage-merging.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
