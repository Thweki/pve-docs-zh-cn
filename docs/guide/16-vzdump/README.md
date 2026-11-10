# 16. Backup and Restore <a href="#chapter_vzdump" id="chapter_vzdump"></a>

Backups are a requirement for any sensible IT deployment, and Proxmox VE provides a fully integrated solution, using the capabilities of each storage and each guest system type. This allows the system administrator to fine tune via the `mode` option between consistency of the backups and downtime of the guest system.

Proxmox VE backups are always full backups - containing the VM/CT configuration and all data. Backups can be started via the GUI or via the `vzdump` command-line tool.

**Backup Storage**

Before a backup can run, a backup storage must be defined. Refer to the [storage documentation](../07-storage/README.md#chapter_storage) on how to add a storage. It can either be a Proxmox Backup Server storage, where backups are stored as de-duplicated chunks and metadata, or a file-level storage, where backups are stored as regular files. Using Proxmox Backup Server on a dedicated host is recommended, because of its advanced features. Using an NFS server is a good alternative. In both cases, you might want to save those backups later to a tape drive, for off-site archiving.

**Scheduled Backup**

Backup jobs can be scheduled so that they are executed automatically on specific days and times, for selectable nodes and guest systems. See the [Backup Jobs](05-vzdump-jobs.md#vzdump_jobs) section for more.

## 本章内容

- [16.1. Backup Modes](01-backup-modes.md)
- [16.2. Backup File Names](02-backup-file-names.md)
- [16.3. Backup File Compression](03-backup-file-compression.md)
- [16.4. Backup Encryption](04-backup-encryption.md)
- [16.5. Backup Jobs](05-vzdump-jobs.md)
- [16.6. Backup Retention](06-vzdump-retention.md)
- [16.7. Backup Protection](07-vzdump-protection.md)
- [16.8. Backup Notes](08-vzdump-notes.md)
- [16.9. Restore](09-vzdump-restore.md)
- [16.10. Configuration](10-vzdump-configuration.md)
- [16.11. Hook Scripts](11-hook-scripts.md)
- [16.12. File Exclusions](12-file-exclusions.md)
- [16.13. Examples](13-examples-10.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
