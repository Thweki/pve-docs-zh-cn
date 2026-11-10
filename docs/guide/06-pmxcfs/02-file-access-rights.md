# 6.2. File Access Rights <a href="#_file_access_rights" id="_file_access_rights"></a>

所有文件和目录的所有者均为用户 `root`，所属组均为 `www-data`。只有 root 拥有写权限，但 `www-data` 组可以读取大多数文件。以下路径下的文件只能由 root 访问：

```text
/etc/pve/priv/
/etc/pve/nodes/${NAME}/priv/
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
