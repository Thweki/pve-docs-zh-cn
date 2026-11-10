# 10.15. 锁 <a href="#locks" id="locks"></a>

在线迁移、快照和备份（`vzdump`）会设置锁，以防止在受影响的虚拟机上同时执行不兼容的操作。有时需要手动移除此类锁（例如断电后）。

```text
# qm unlock <vmid>
```

{% hint style="danger" %}
只有在确定设置该锁的操作已停止运行时，才执行此操作。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
