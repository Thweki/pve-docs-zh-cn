# 1.3. 集成备份与恢复 <a href="#_integrated_backup_and_restore" id="_integrated_backup_and_restore"></a>

集成的备份工具（`vzdump`）可为运行中的容器和 KVM 客户机创建一致性快照。它会创建包含虚拟机或容器数据（包括配置文件）的归档文件。

此外，[Proxmox Backup Server 集成](../07-storage/08-storage-pbs.md#storage_pbs)提供了高级功能，包括将完整备份与数据去重相结合、执行客户端加密、备份到磁带或 S3 对象存储，以及与异地的其他 Proxmox Backup Server 安装实例同步。

KVM 在线备份适用于所有存储类型，包括位于 NFS、CIFS、iSCSI LUN 和 Ceph RBD 上的虚拟机镜像。该备份格式经过优化，可使用稀疏文件、乱序数据和最小化 I/O 高效存储虚拟机备份。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
