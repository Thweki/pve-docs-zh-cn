# 6.2. File Access Rights <a href="#_file_access_rights" id="_file_access_rights"></a>

All files and directories are owned by user `root` and have group `www-data`. Only root has write permissions, but group `www-data` can read most files. Files below the following paths are only accessible by root:

```text
/etc/pve/priv/
/etc/pve/nodes/${NAME}/priv/
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
