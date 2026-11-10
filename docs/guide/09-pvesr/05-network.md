# 9.5. 网络 <a href="#network" id="network"></a>

默认情况下，复制流量与客户机迁移流量使用同一网络。如果未设置迁移网络，则复制流量会转而默认使用管理网络。

要为复制流量使用不同的网络，请配置 `Replication Network`（在 Web 界面的 `Datacenter -> Options ->
Replication Settings` 下），或设置 `replication` 属性（位于 `datacenter.cfg` 文件中）：

```text
# use dedicated replication network
replication: secure,network=10.1.2.0/24
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
