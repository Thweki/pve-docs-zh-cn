# 5.13. Cluster Cold Start <a href="#_cluster_cold_start" id="_cluster_cold_start"></a>

It is obvious that a cluster is not quorate when all nodes are offline. This is a common case after a power failure.

{% hint style="info" %}
It is always a good idea to use an uninterruptible power supply (“UPS”, also called “battery backup”) to avoid this state, especially if you want HA.
{% endhint %}

On node startup, the `pve-guests` service is started and waits for quorum. Once quorate, it starts all guests which have the `onboot` flag set.

When you turn on nodes, or when power comes back after power failure, it is likely that some nodes will boot faster than others. Please keep in mind that guest startup is delayed until you reach quorum.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
