# 16\. 备份与恢复 <a href="#chapter_vzdump" id="chapter_vzdump"></a>

任何合理的 IT 部署都需要备份，Proxmox VE 利用各存储和各客户机系统类型的能力，提供完全集成的解决方案。这允许系统管理员通过 `mode` 选项在备份一致性与客户机系统停机时间之间进行微调。

Proxmox VE 备份始终是完整备份，包含虚拟机/容器配置和全部数据。可通过 GUI 或 `vzdump` 命令行工具启动备份。

**备份存储**

运行备份前，必须定义备份存储。有关如何添加存储，请参阅 [存储文档](../07-storage/README.md)。它可以是 Proxmox Backup Server 存储，备份以去重数据块和元数据的形式存储；也可以是文件级存储，备份以普通文件形式存储。建议在专用宿主机上使用 Proxmox Backup Server，因为它具有高级功能。使用 NFS 服务器是很好的替代方案。在这两种情况下，您可能希望以后将这些备份保存到磁带机，进行异地归档。

**计划备份**

可以安排备份作业，使其在指定日期和时间对选定的节点和客户机系统自动执行。更多信息请参阅 [备份作业](05-vzdump-jobs.md) 一节。

## 本章内容

- [16.1. 备份模式](01-backup-modes.md)
- [16.2. 备份文件名](02-backup-file-names.md)
- [16.3. 备份文件压缩](03-backup-file-compression.md)
- [16.4. 备份加密](04-backup-encryption.md)
- [16.5. 备份作业](05-vzdump-jobs.md)
- [16.6. 备份保留](06-vzdump-retention.md)
- [16.7. 备份保护](07-vzdump-protection.md)
- [16.8. 备份备注](08-vzdump-notes.md)
- [16.9. 恢复](09-vzdump-restore.md)
- [16.10. 配置](10-vzdump-configuration.md)
- [16.11. 钩子脚本](11-hook-scripts.md)
- [16.12. 文件排除](12-file-exclusions.md)
- [16.13. 示例](13-examples-10.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
