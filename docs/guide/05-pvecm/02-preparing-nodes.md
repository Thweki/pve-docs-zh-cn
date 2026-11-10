# 5.2. 准备节点 <a href="#_preparing_nodes" id="_preparing_nodes"></a>

首先，在所有节点上安装 Proxmox VE。确保每个节点在安装时都使用最终的主机名和 IP 配置。创建集群后，无法更改主机名和 IP。

虽然在 `/etc/hosts` 中引用所有节点名称及其 IP（或通过其他方式使其名称可解析）很常见，但集群运行并不需要这样做。不过，这样做可能很有用，因为随后可以使用更容易记住的节点名称，通过 SSH 从一个节点连接到另一个节点（另请参见[链路地址类型](08-pvecm-cluster-network.md#pvecm_corosync_addresses)）。请注意，我们始终建议在集群配置中通过节点的 IP 地址来引用节点。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
