# 12.15. Firewall Integration <a href="#pvesdn_firewall_integration" id="pvesdn_firewall_integration"></a>

SDN integrates with the Proxmox VE firewall by automatically generating IPSets which can then be referenced in the source / destination fields of firewall rules. This happens automatically for VNets and IPAM entries.

## 12.15.1. VNets and Subnets <a href="#_vnets_and_subnets" id="_vnets_and_subnets"></a>

The firewall automatically generates the following IPSets in the SDN scope for every VNet:

**`vnet-all`**

Contains the CIDRs of all subnets in a VNet

**`vnet-gateway`**

Contains the IPs of the gateways of all subnets in a VNet

**`vnet-no-gateway`**

Contains the CIDRs of all subnets in a VNet, but excludes the gateways

**`vnet-dhcp`**

Contains all DHCP ranges configured in the subnets in a VNet

When making changes to your configuration, the IPSets update automatically, so you do not have to update your firewall rules when changing the configuration of your Subnets.

### Simple Zone Example <a href="#_simple_zone_example" id="_simple_zone_example"></a>

Assuming the configuration below for a VNet and its contained subnets:

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

In this example we configured an IPv4 subnet in the VNet `vnet0`, with *192.0.2.0/24* as its IP Range, *192.0.2.1* as the gateway and the DHCP range is *192.0.2.100* \- *192.0.2.199*.

Additionally we configured an IPv6 subnet with *2001:db8::/64* as the IP range, *2001:db8::1* as the gateway and a DHCP range of *2001:db8::1000* \- *2001:db8::1999*.

The respective auto-generated IPsets for vnet0 would then contain the following elements:

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

## 12.15.2. IPAM <a href="#_ipam" id="_ipam"></a>

If you are using the built-in PVE IPAM, then the firewall automatically generates an IPset for every guest that has entries in the IPAM. The respective IPset for a guest with ID 100 would be `guest-ipam-100`. It contains all IP addresses from all IPAM entries. So if guest 100 is member of multiple VNets, then the IPset would contain the IPs from **all** VNets.

When entries get added / updated / deleted, then the respective IPSets will be updated accordingly.

{% hint style="warning" %}
When removing all entries for a guest and there are firewall rules still referencing the auto-generated IPSet then the firewall will fail to update the ruleset, since it references a non-existing IPSet.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
