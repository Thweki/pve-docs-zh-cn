# 12.7. VNets <a href="#pvesdn_config_vnet" id="pvesdn_config_vnet"></a>

After creating a virtual network (VNet) through the SDN GUI, a local network interface with the same name is available on each node. To connect a guest to the VNet, assign the interface to the guest and set the IP address accordingly.

Depending on the zone, these options have different meanings and are explained in the respective zone section in this document.

{% hint style="warning" %}
In the current state, some options may have no effect or won’t work in certain zones.
{% endhint %}

VNet configuration options:

**ID**

An up to 8 character ID to identify a VNet

**Alias**

More descriptive identifier. Assigned as an alias on the interface. Optional

**Zone**

The associated zone for this VNet

**Tag**

The unique VLAN or VXLAN ID

**VLAN Aware**

Enables vlan-aware option on the interface, enabling configuration in the guest.

**Isolate Ports**

Sets the isolated flag for all guest ports of this interface, but not for the interface itself. This means guests can only send traffic to non-isolated bridge-ports, which is the bridge itself. In order for this setting to take effect, you need to restart the affected guest.

{% hint style="info" %}
Port isolation is local to each host. Use the [VNET Firewall](15-pvesdn-firewall-integration.md#pvesdn_firewall_integration) to further isolate traffic in the VNET across nodes. For example, DROP by default and only allow traffic from the IP subnet to the gateway and vice versa.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
