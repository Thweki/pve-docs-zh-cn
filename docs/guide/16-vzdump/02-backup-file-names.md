# 16.2. 备份文件名 <a href="#backup_file_names" id="backup_file_names"></a>

较新版本的 vzdump 将客户机类型和备份时间编码到文件名中，例如

```text
vzdump-lxc-105-2009_10_09-11_04_43.tar
```

这样就可以在同一目录中存储多个备份。可以使用各种保留选项限制保留的备份数量，参见下文 [备份保留](06-vzdump-retention.md) 一节。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
