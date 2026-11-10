# 5.13. 集群冷启动 <a href="#cluster_cold_start" id="cluster_cold_start"></a>

显然，当所有节点都离线时，集群不具备仲裁。这是断电后的常见情况。

{% hint style="info" %}
使用不间断电源（“UPS”，也称为“电池备份”）来避免这种状态始终是个好主意，尤其是在您需要 HA 时。
{% endhint %}

节点启动时，`pve-guests` 服务会启动并等待仲裁。达到仲裁后，它会启动所有设置了 `onboot` 标志的客户机。

当您开启节点时，或在断电后恢复供电时，某些节点很可能会比其他节点启动得更快。请注意，客户机的启动会延迟，直到达到仲裁要求为止。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
