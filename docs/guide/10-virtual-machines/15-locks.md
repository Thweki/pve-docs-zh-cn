# 10.15. Locks <a href="#_locks" id="_locks"></a>

Online migrations, snapshots and backups (`vzdump`) set a lock to prevent incompatible concurrent actions on the affected VMs. Sometimes you need to remove such a lock manually (for example after a power failure).

```text
# qm unlock <vmid>
```

{% hint style="danger" %}
Only do that if you are sure the action which set the lock is no longer running.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
