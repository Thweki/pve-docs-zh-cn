# 13.5. IP 别名 <a href="#pve_firewall_ip_aliases" id="pve_firewall_ip_aliases"></a>

IP 别名允许将网络的 IP 地址与名称关联。随后可以在以下位置引用这些名称：

- 在 IP 集合定义中
- 在防火墙规则的 `source` 和 `dest` 属性中

## 13.5.1. 标准 IP 别名 `local_network` <a href="#standard_ip_alias_span_class_monospaced_local_network_span" id="standard_ip_alias_span_class_monospaced_local_network_span"></a>

此别名自动定义。请使用以下命令查看分配的值：

```text
# pve-firewall localnet
local hostname: example
local IP address: 192.168.2.100
network auto detect: 192.168.0.0/20
using detected local_network: 192.168.0.0/20
```

防火墙会使用此别名自动设置规则，允许集群通信所需的全部流量（corosync、API、SSH）。

用户可以在 `cluster.fw` 别名节中覆盖这些值。如果在公共网络上使用单台宿主机，最好显式指定本地 IP 地址

```text
#  /etc/pve/firewall/cluster.fw
[ALIASES]
local_network 1.2.3.4 # use the single IP address
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
