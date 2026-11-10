# 13.6. IP 集合 <a href="#pve_firewall_ip_sets" id="pve_firewall_ip_sets"></a>

IP 集合可用于定义网络和宿主机组。可以在防火墙规则的 `source` 和 `dest` 属性中使用“\+name”引用它们。

以下示例允许来自 `management` IP 集合的 HTTP 流量。

```text
IN HTTP(ACCEPT) -source +management
```

## 13.6.1. 标准 IP 集合 `management` <a href="#standard_ip_set_span_class_monospaced_management_span" id="standard_ip_set_span_class_monospaced_management_span"></a>

此 IP 集合仅适用于宿主机防火墙（不适用于虚拟机防火墙）。允许这些 IP 执行常规管理任务（Proxmox VE GUI、VNC、SPICE、SSH）。

本地集群网络会自动添加到此 IP 集合（别名 `cluster_network`），以启用宿主机之间的集群通信。（组播、ssh 等）

```text
# /etc/pve/firewall/cluster.fw

[IPSET management]
192.168.2.10
192.168.2.10/24
```

## 13.6.2. 标准 IP 集合 `blacklist` <a href="#standard_ip_set_span_class_monospaced_blacklist_span" id="standard_ip_set_span_class_monospaced_blacklist_span"></a>

来自这些 IP 的流量会被每台宿主机和虚拟机的防火墙丢弃。

```text
# /etc/pve/firewall/cluster.fw

[IPSET blacklist]
77.240.159.182
213.87.123.0/24
```

## 13.6.3. 标准 IP 集合 `ipfilter-net*` <a href="#pve_firewall_ipfilter_section" id="pve_firewall_ipfilter_section"></a>

这些过滤器属于虚拟机的网络接口，主要用于防止 IP 欺骗。如果某接口存在此类集合，则任何源 IP 不匹配其接口对应 ipfilter 集合的传出流量都会被丢弃。

对于已配置 IP 地址的容器，如果这些集合存在（或通过全局 `IP Filter` 选项，在虚拟机防火墙的 **选项** 选项卡中激活），则会隐式包含关联的 IP 地址。

对于虚拟机和容器，它们还会隐式包含由 MAC 推导的标准 IPv6 链路本地地址，以便邻居发现协议能够工作。

```text
/etc/pve/firewall/<VMID>.fw

[IPSET ipfilter-net0] # only allow specified IPs on net0
192.168.2.10
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
