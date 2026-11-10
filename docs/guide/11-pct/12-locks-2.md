# 11.12. Locks <a href="#_locks_2" id="_locks_2"></a>

容器迁移、快照和备份（`vzdump`）会设置锁，以防止在受影响的容器上并发执行不兼容的操作。有时你需要手动删除此类锁（例如，断电后）。

```text
# pct unlock <CTID>
```

{% hint style="danger" %}
只有确定设置该锁的操作已不再运行时，才能这样做。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
