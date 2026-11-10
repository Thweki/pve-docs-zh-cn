# 9.5. Network <a href="#_network" id="_network"></a>

默认情况下，复制流量与客户机迁移流量使用同一网络。如果未设置迁移网络，则复制流量会转而默认使用管理网络。

To use a different network for the replication traffic, configure the `Replication Network` in the web interface under `Datacenter -> Options ->
Replication Settings` or set the `replication` property in the `datacenter.cfg` file:

```text
# use dedicated replication network
replication: secure,network=10.1.2.0/24
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
