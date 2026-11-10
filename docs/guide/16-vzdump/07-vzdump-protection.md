# 16.7. 备份保护 <a href="#vzdump_protection" id="vzdump_protection"></a>

可以将备份标记为 `protected`，以防止将其移除。尝试通过 Proxmox VE 的 UI、CLI 或 API 移除受保护备份会失败。不过，此保护由 Proxmox VE 而非文件系统强制实施，这意味着任何对底层备份存储具有写入权限的人仍可手动移除备份文件本身。

{% hint style="info" %}
受保护备份会被清理操作忽略，也不计入保留设置。
{% endhint %}

对于基于文件系统的存储，通过哨兵文件 `<backup-name>.protected` 实现保护。对于 Proxmox Backup Server，由服务器端处理（自 Proxmox Backup Server 2.1 版本起提供）。

使用存储选项 `max-protected-backups` 控制存储上每个客户机允许的受保护备份数量。使用 `-1` 表示无限制。具有 `Datastore.Allocate` 权限的用户默认无限制，其他用户默认为 `5`。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
