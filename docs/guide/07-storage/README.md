# 7. Proxmox VE Storage <a href="#chapter_storage" id="chapter_storage"></a>

The Proxmox VE storage model is very flexible. Virtual machine images can either be stored on one or several local storages, or on shared storage like NFS or iSCSI (NAS, SAN). There are no limits, and you may configure as many storage pools as you like. You can use all storage technologies available for Debian Linux.

One major benefit of storing VMs on shared storage is the ability to live-migrate running machines without any downtime, as all nodes in the cluster have direct access to VM disk images. There is no need to copy VM image data, so live migration is very fast in that case.

The storage library (package `libpve-storage-perl`) uses a flexible plugin system to provide a common interface to all storage types. This can be easily adopted to include further storage types in the future.

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
