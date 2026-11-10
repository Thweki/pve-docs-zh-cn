# 7\. Proxmox VE Storage <a href="#chapter_storage" id="chapter_storage"></a>

Proxmox VE 存储模型非常灵活。虚拟机镜像可以存储在一个或多个本地存储上，也可以存储在 NFS 或 iSCSI（NAS、SAN）等共享存储上。没有任何限制，您可以根据需要配置任意数量的存储池。您可以使用 Debian Linux 可用的所有存储技术。

将 VM 存储在共享存储上的一个主要好处是，可以在线迁移正在运行的机器而无需任何停机，因为集群中的所有节点都可以直接访问 VM 磁盘镜像。无需复制 VM 镜像数据，因此在这种情况下在线迁移速度非常快。

存储库（软件包 `libpve-storage-perl`）使用灵活的插件系统，为所有存储类型提供通用接口。可以轻松地对其进行扩展，以便将来支持更多存储类型。

## 本章内容

- [7.1. Storage Types](01-storage-types.md)
- [7.2. Storage Configuration](02-storage-configuration.md)
- [7.3. Volumes](03-volumes.md)
- [7.4. Using the Command-line Interface](04-using-the-command-line-interface.md)
- [7.5. Directory Backend](05-storage-directory.md)
- [7.6. NFS Backend](06-storage-nfs.md)
- [7.7. CIFS Backend](07-storage-cifs.md)
- [7.8. Proxmox Backup Server](08-storage-pbs.md)
- [7.9. Local ZFS Pool Backend](09-storage-zfspool.md)
- [7.10. LVM Backend](10-storage-lvm.md)
- [7.11. LVM thin Backend](11-storage-lvmthin.md)
- [7.12. Open-iSCSI initiator](12-storage-open-iscsi.md)
- [7.13. User Mode iSCSI Backend](13-storage-iscsidirect.md)
- [7.14. Ceph RADOS Block Devices (RBD)](14-ceph-rados-block-devices.md)
- [7.15. Ceph Filesystem (CephFS)](15-storage-cephfs.md)
- [7.16. BTRFS Backend](16-storage-btrfs.md)
- [7.17. ZFS over ISCSI Backend](17-storage-zfs.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
