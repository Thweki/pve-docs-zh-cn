# 13.1. Directions \& Zones <a href="#_directions_amp_zones" id="_directions_amp_zones"></a>

The Proxmox VE firewall groups the network into multiple logical zones. You can define rules for each zone independently. Depending on the zone, you can define rules for incoming, outgoing or forwarded traffic.

## 13.1.1. Directions <a href="#_directions" id="_directions"></a>

There are 3 directions that you can choose from when defining rules for a zone:

**In**

Traffic that is arriving in a zone.

**Out**

Traffic that is leaving a zone.

**Forward**

Traffic that is passing through a zone. In the host zone this can be routed traffic (when the host is acting as a gateway or performing NAT). At a VNet-level this affects all traffic that is passing by a VNet, including traffic from/to bridged network interfaces.

{% hint style="warning" %}
Creating rules for forwarded traffic is currently only possible when using the new [nftables-based proxmox-firewall](13-pve-firewall-nft.md#pve_firewall_nft). Any forward rules will be ignored by the stock `pve-firewall` and have no effect!
{% endhint %}

## 13.1.2. Zones <a href="#_zones" id="_zones"></a>

There are 3 different zones that you can define firewall rules for:

**Host**

Traffic going from/to a host, or traffic that is forwarded by a host. You can define rules for this zone either at the datacenter level or at the host level. Rules at host level take precedence over rules at datacenter level.

**VM**

Traffic going from/to a VM or CT. You cannot define rules for forwarded traffic, only for incoming / outgoing traffic.

**VNet**

Traffic passing through a SDN VNet, either from guest to guest or from host to guest and vice-versa. Since this traffic is always forwarded traffic, it is only possible to create rules with direction forward.

{% hint style="warning" %}
Creating rules on a VNet-level is currently only possible when using the new [nftables-based proxmox-firewall](13-pve-firewall-nft.md#pve_firewall_nft). Any VNet-level rules will be ignored by the stock `pve-firewall` and have no effect!
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
