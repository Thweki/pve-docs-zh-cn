# 13.6. IP Sets <a href="#pve_firewall_ip_sets" id="pve_firewall_ip_sets"></a>

IP sets can be used to define groups of networks and hosts. You can refer to them with ‘\+name\` in the firewall rules’ `source` and `dest` properties.

The following example allows HTTP traffic from the `management` IP set.

```text
IN HTTP(ACCEPT) -source +management
```

## 13.6.1. Standard IP set `management` <a href="#_standard_ip_set_span_class_monospaced_management_span" id="_standard_ip_set_span_class_monospaced_management_span"></a>

This IP set applies only to host firewalls (not VM firewalls). Those IPs are allowed to do normal management tasks (Proxmox VE GUI, VNC, SPICE, SSH).

The local cluster network is automatically added to this IP set (alias `cluster_network`), to enable inter-host cluster communication. (multicast,ssh,…)

```text
# /etc/pve/firewall/cluster.fw

[IPSET management]
192.168.2.10
192.168.2.10/24
```

## 13.6.2. Standard IP set `blacklist` <a href="#_standard_ip_set_span_class_monospaced_blacklist_span" id="_standard_ip_set_span_class_monospaced_blacklist_span"></a>

Traffic from these IPs is dropped by every host’s and VM’s firewall.

```text
# /etc/pve/firewall/cluster.fw

[IPSET blacklist]
77.240.159.182
213.87.123.0/24
```

## 13.6.3. Standard IP set `ipfilter-net*` <a href="#pve_firewall_ipfilter_section" id="pve_firewall_ipfilter_section"></a>

These filters belong to a VM’s network interface and are mainly used to prevent IP spoofing. If such a set exists for an interface then any outgoing traffic with a source IP not matching its interface’s corresponding ipfilter set will be dropped.

For containers with configured IP addresses these sets, if they exist (or are activated via the general `IP Filter` option in the VM’s firewall’s **options** tab), implicitly contain the associated IP addresses.

For both virtual machines and containers they also implicitly contain the standard MAC-derived IPv6 link-local address in order to allow the neighbor discovery protocol to work.

```text
/etc/pve/firewall/<VMID>.fw

[IPSET ipfilter-net0] # only allow specified IPs on net0
192.168.2.10
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
