# 9.5. Network <a href="#_network" id="_network"></a>

By default, replication traffic will go through the same network as the guest migration traffic. If the migration network is not set, this will in turn default to the management network.

To use a different network for the replication traffic, configure the `Replication Network` in the web interface under `Datacenter -> Options ->
Replication Settings` or set the `replication` property in the `datacenter.cfg` file:

```text
# use dedicated replication network
replication: secure,network=10.1.2.0/24
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
