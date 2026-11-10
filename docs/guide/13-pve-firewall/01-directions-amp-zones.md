# 13.1. 方向与区域 <a href="#directions_amp_zones" id="directions_amp_zones"></a>

Proxmox VE 防火墙将网络分成多个逻辑区域。可以独立为每个区域定义规则。根据区域不同，可以为传入、传出或转发流量定义规则。

## 13.1.1. 方向 <a href="#directions" id="directions"></a>

为区域定义规则时，有 3 种方向可选：

**传入**

到达区域的流量。

**传出**

离开区域的流量。

**转发**

经过区域的流量。在宿主机区域中，这可以是路由流量（宿主机充当网关或执行 NAT 时）。在 VNet 级别，这会影响经过 VNet 的所有流量，包括往返于桥接网络接口的流量。

{% hint style="warning" %}
目前只有使用新的 [基于 nftables 的 proxmox-firewall](13-pve-firewall-nft.md) 时才能创建转发流量规则。标准的 `pve-firewall` 会忽略所有转发规则，这些规则不会产生任何效果！
{% endhint %}

## 13.1.2. 区域 <a href="#zones" id="zones"></a>

可以为 3 种不同区域定义防火墙规则：

**宿主机**

往返于宿主机的流量，或由宿主机转发的流量。可以在数据中心级别或宿主机级别为此区域定义规则。宿主机级别规则优先于数据中心级别规则。

**虚拟机**

往返于虚拟机或容器的流量。不能为转发流量定义规则，只能为传入/传出流量定义规则。

**VNet**

经过 SDN VNet 的流量，可以是客户机之间，或宿主机与客户机之间的双向流量。由于这些流量始终是转发流量，因此只能创建方向为转发的规则。

{% hint style="warning" %}
目前只有使用新的 [基于 nftables 的 proxmox-firewall](13-pve-firewall-nft.md) 时才能在 VNet 级别创建规则。标准的 `pve-firewall` 会忽略所有 VNet 级别规则，这些规则不会产生任何效果！
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
