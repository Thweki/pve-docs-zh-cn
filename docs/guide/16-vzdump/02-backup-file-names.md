# 16.2. Backup File Names <a href="#_backup_file_names" id="_backup_file_names"></a>

Newer versions of vzdump encode the guest type and the backup time into the filename, for example

```text
vzdump-lxc-105-2009_10_09-11_04_43.tar
```

That way it is possible to store several backup in the same directory. You can limit the number of backups that are kept with various retention options, see the [Backup Retention](06-vzdump-retention.md#vzdump_retention) section below.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
