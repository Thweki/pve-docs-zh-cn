# 12.6. Zones <a href="#pvesdn_config_zone" id="pvesdn_config_zone"></a>

A zone defines a virtually separated network. Zones are restricted to specific nodes and assigned permissions, in order to restrict users to a certain zone and its contained VNets.

Different technologies can be used for separation:

- Simple: Isolated Bridge. A simple layer 3 routing bridge (NAT)
- VLAN: Virtual LANs are the classic method of subdividing a LAN
- QinQ: Stacked VLAN (formally known as `IEEE 802.1ad`)
- VXLAN: Layer 2 VXLAN network via a UDP tunnel
- EVPN (BGP EVPN): VXLAN with BGP to establish Layer 3 routing

## 12.6.1. Common Options <a href="#pvesdn_config_common_options" id="pvesdn_config_common_options"></a>

The following options are available for all zone types:

**Nodes**

The nodes which the zone and associated VNets should be deployed on.

**IPAM**

Use an IP Address Management (IPAM) tool to manage IPs in the zone. Optional, defaults to `pve`.

**DNS**

DNS API server. Optional.

**ReverseDNS**

Reverse DNS API server. Optional.

**DNSZone**

DNS domain name. Used to register hostnames, such as `<hostname>.<domain>`. The DNS zone must already exist on the DNS server. Optional.

## 12.6.2. Simple Zones <a href="#pvesdn_zone_plugin_simple" id="pvesdn_zone_plugin_simple"></a>

This is the simplest plugin. It will create an isolated VNet bridge. This bridge is not linked to a physical interface, and VM traffic is only local on each the node. It can be used in NAT or routed setups.

## 12.6.3. VLAN Zones <a href="#pvesdn_zone_plugin_vlan" id="pvesdn_zone_plugin_vlan"></a>

The VLAN plugin uses an existing local Linux or OVS bridge to connect to the node’s physical interface. It uses VLAN tagging defined in the VNet to isolate the network segments. This allows connectivity of VMs between different nodes.

VLAN zone configuration options:

**Bridge**

The local bridge or OVS switch, already configured on **each** node that allows node-to-node connection.

## 12.6.4. QinQ Zones <a href="#pvesdn_zone_plugin_qinq" id="pvesdn_zone_plugin_qinq"></a>

QinQ also known as VLAN stacking, that uses multiple layers of VLAN tags for isolation. The QinQ zone defines the outer VLAN tag (the *Service VLAN*) whereas the inner VLAN tag is defined by the VNet.

{% hint style="info" %}
Your physical network switches must support stacked VLANs for this configuration.
{% endhint %}

QinQ zone configuration options:

**Bridge**

A local, VLAN-aware bridge that is already configured on each local node

**Service VLAN**

The main VLAN tag of this zone

**Service VLAN Protocol**

Allows you to choose between an 802.1q (default) or 802.1ad service VLAN type.

**MTU**

Due to the double stacking of tags, you need 4 more bytes for QinQ VLANs. For example, you must reduce the MTU to `1496` if you physical interface MTU is `1500`.

## 12.6.5. VXLAN Zones <a href="#pvesdn_zone_plugin_vxlan" id="pvesdn_zone_plugin_vxlan"></a>

The VXLAN plugin establishes a tunnel (overlay) on top of an existing network (underlay). This encapsulates layer 2 Ethernet frames within layer 4 UDP datagrams using the default destination port `4789`.

You have to configure the underlay network yourself to enable UDP connectivity between all peers.

You can, for example, create a VXLAN overlay network on top of public internet, appearing to the VMs as if they share the same local Layer 2 network.

{% hint style="warning" %}
VXLAN on its own does does not provide any encryption. When joining multiple sites via VXLAN, make sure to establish a secure connection between the site, for example by using a site-to-site VPN.
{% endhint %}

VXLAN zone configuration options:

**Peers Address List**

A list of IP addresses of each node in the VXLAN zone. This can be external nodes reachable at this IP address. All nodes in the cluster need to be mentioned here.

**SDN Fabric**

Instead of manually defining all the peers, use a [Fabric](10-pvesdn-config-fabrics.md) for automatically generating the peer list.

**MTU**

Because VXLAN encapsulation uses 50 bytes, the MTU needs to be 50 bytes lower than the outgoing physical interface.

## 12.6.6. EVPN Zones <a href="#pvesdn_zone_plugin_evpn" id="pvesdn_zone_plugin_evpn"></a>

The EVPN zone creates a routable Layer 3 network, capable of spanning across multiple clusters. This is achieved by establishing a VPN and utilizing BGP as the routing protocol.

The VNet of EVPN can have an anycast IP address and/or MAC address. The bridge IP is the same on each node, meaning a virtual guest can use this address as gateway.

Routing can work across VNets from different zones through a VRF (Virtual Routing and Forwarding) interface.

EVPN zone configuration options:

**VRF VXLAN ID**

A VXLAN-ID used for dedicated routing interconnect between VNets. It must be different than the VXLAN-ID of the VNets.

**Primay Controller**

The primary EVPN-controller to use for this zone. The primary controller is used for auto-deriving the VTEP IPs, based on the peer definition. For more information see the [controller section](09-pvesdn-config-controllers.md#pvesdn_controller_plugin_evpn).

**Addtional Controllers**

Additional EVPN controllers to use for this zone. Controllers listed here will announce the L2VPN EVPN routes for this zone.

**VNet MAC Address**

Anycast MAC address that gets assigned to all VNets in this zone. Will be auto-generated if not defined.

**Exit Nodes**

Nodes that shall be configured as exit gateways from the EVPN network, through the real network. The configured nodes will announce a default route in the EVPN network. Optional.

**Primary Exit Node**

If you use multiple exit nodes, force traffic through this primary exit node, instead of load-balancing on all nodes. Optional but necessary if you want to use SNAT or if your upstream router doesn’t support ECMP.

**Exit Nodes Local Routing**

This is a special option if you need to reach a VM/CT service from an exit node. (By default, the exit nodes only allow forwarding traffic between real network and EVPN network). Optional.

**Advertise Subnets**

Announce the full subnet in the EVPN network. If you have silent VMs/CTs (for example, if you have multiple IPs and the anycast gateway doesn’t see traffic from these IPs, the IP addresses won’t be able to be reached inside the EVPN network). Optional.

**Disable ARP ND Suppression**

Don’t suppress ARP or ND (Neighbor Discovery) packets. This is required if you use floating IPs in your VMs (IP and MAC addresses are being moved between systems). Optional.

**Route-target Import**

Allows you to import a list of external EVPN route targets. Used for cross-DC or different EVPN network interconnects. Optional.

**MTU**

Because VXLAN encapsulation uses 50 bytes, the MTU needs to be 50 bytes less than the maximal MTU of the outgoing physical interface. Optional, defaults to 1450\.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
