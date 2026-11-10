# 13.5. IP Aliases <a href="#pve_firewall_ip_aliases" id="pve_firewall_ip_aliases"></a>

IP Aliases allow you to associate IP addresses of networks with a name. You can then refer to those names:

- inside IP set definitions
- in `source` and `dest` properties of firewall rules

## 13.5.1. Standard IP Alias `local_network` <a href="#_standard_ip_alias_span_class_monospaced_local_network_span" id="_standard_ip_alias_span_class_monospaced_local_network_span"></a>

This alias is automatically defined. Please use the following command to see assigned values:

```text
# pve-firewall localnet
local hostname: example
local IP address: 192.168.2.100
network auto detect: 192.168.0.0/20
using detected local_network: 192.168.0.0/20
```

The firewall automatically sets up rules to allow everything needed for cluster communication (corosync, API, SSH) using this alias.

The user can overwrite these values in the `cluster.fw` alias section. If you use a single host on a public network, it is better to explicitly assign the local IP address

```text
#  /etc/pve/firewall/cluster.fw
[ALIASES]
local_network 1.2.3.4 # use the single IP address
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
