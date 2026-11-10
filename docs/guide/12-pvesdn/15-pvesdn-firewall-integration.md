# 12.15. 防火墙集成 <a href="#pvesdn_firewall_integration" id="pvesdn_firewall_integration"></a>

SDN 通过自动生成 IPSet 与 Proxmox VE 防火墙集成，这些 IPSet 随后可在防火墙规则的源/目标字段中引用。VNet 和 IPAM 条目会自动执行此操作。

## 12.15.1. VNet 与子网 <a href="#vnets_and_subnets" id="vnets_and_subnets"></a>

防火墙会为每个 VNet 在 SDN 作用域中自动生成以下 IPSet：

**`vnet-all`**

包含 VNet 中所有子网的 CIDR

**`vnet-gateway`**

包含 VNet 中所有子网网关的 IP

**`vnet-no-gateway`**

包含 VNet 中所有子网的 CIDR，但不包括网关

**`vnet-dhcp`**

包含 VNet 中子网配置的所有 DHCP 范围

更改配置时，IPSet 会自动更新，因此更改子网配置时无需更新防火墙规则。

### Simple 区域示例 <a href="#simple_zone_example" id="simple_zone_example"></a>

假设 VNet 及其包含的子网配置如下：

```text
# /etc/pve/sdn/vnets.cfg

vnet: vnet0
        zone simple

# /etc/pve/sdn/subnets.cfg

subnet: simple-192.0.2.0-24
        vnet vnet0
        dhcp-range start-address=192.0.2.100,end-address=192.0.2.199
        gateway 192.0.2.1

subnet: simple-2001:db8::-64
        vnet vnet0
        dhcp-range start-address=2001:db8::1000,end-address=2001:db8::1999
        gateway 2001:db8::1
```

在此示例中，我们在 VNet `vnet0` 中配置了 IPv4 子网，IP 范围为 *192.0.2.0/24*，网关为 *192.0.2.1*，DHCP 范围为 *192.0.2.100* \- *192.0.2.199*。

此外，我们还配置了 IPv6 子网，IP 范围为 *2001:db8::/64*，网关为 *2001:db8::1*，DHCP 范围为 *2001:db8::1000* \- *2001:db8::1999*。

vnet0 对应的自动生成 IPSet 将包含以下元素：

**`vnet0-all`**

- *192.0.2.0/24*
- *2001:db8::/64*

**`vnet0-gateway`**

- *192.0.2.1*
- *2001:db8::1*

**`vnet0-no-gateway`**

- *192.0.2.0/24*
- *2001:db8::/64*
- *!192.0.2.1*
- *!2001:db8::1*

**`vnet0-dhcp`**

- *192.0.2.100 \- 192.0.2.199*
- *2001:db8::1000 \- 2001:db8::1999*

## 12.15.2. IPAM <a href="#ipam" id="ipam"></a>

如果使用内置的 PVE IPAM，防火墙会为 IPAM 中有条目的每个客户机自动生成一个 IPSet。ID 为 100 的客户机对应的 IPSet 为 `guest-ipam-100`。其中包含所有 IPAM 条目的所有 IP 地址。因此，如果客户机 100 属于多个 VNet，则 IPSet 将包含 **所有** VNet 中的 IP。

添加/更新/删除条目时，相应的 IPSet 也会同步更新。

{% hint style="warning" %}
如果移除了某客户机的所有条目，但仍有防火墙规则引用自动生成的 IPSet，则防火墙将无法更新规则集，因为它引用了不存在的 IPSet。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
