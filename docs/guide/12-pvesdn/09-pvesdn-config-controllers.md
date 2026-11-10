# 12.9. Controllers <a href="#pvesdn_config_controllers" id="pvesdn_config_controllers"></a>

Some zones implement a separated control and data plane that require an external controller to manage the VNet’s control plane.

Currently, only the `EVPN` zone requires an external controller.

## 12.9.1. EVPN Controller <a href="#pvesdn_controller_plugin_evpn" id="pvesdn_controller_plugin_evpn"></a>

The `EVPN`, zone requires an external controller to manage the control plane. The EVPN controller plugin configures the Free Range Routing (frr) router.

To enable the EVPN controller, you need to enable FRR on every node, see [install FRRouting](03-pvesdn-installation.md#pvesdn_install_frrouting).

EVPN controller configuration options:

**ASN \#**

A unique BGP ASN number. It’s highly recommended to use a private ASN number (64512 – 65534, 4200000000 – 4294967294), as otherwise you could end up breaking global routing by mistake. Every EVPN controller configured on a node must have the same ASN configured.

**SDN Fabric**

A [Fabric](10-pvesdn-config-fabrics.md) that contains all the nodes part of the EVPN zone. Will be used as the underlay network.

**Peers**

An IP list of all nodes that are part of the EVPN zone. (could also be external nodes or route reflector servers)

**Nodes**

A list of nodes where this controller should be active. This can be used to configure EVPN peering sessions on specific nodes only.

**Peer Group Name**

EVPN controllers use the peer group name *VTEP* by default. When defining multiple EVPN controllers, each additional controller needs to specify a custom peer group name to be used in the FRR configuration.

**BGP Mode**

Allows configuring the type of BGP session manually. The *auto* mode preserves the old behavior of the SDN stack: EVPN controllers were iBGP, unless there was a BGP controller configured. In that case the EVPN controller re-used the BGP session from the BGP controller. With this option, the type of BGP session can be overridden manually \- allowing for explicitly configuring the type of BGP session that should be established with the EVPN controller.

**ebgp-multihop**

Increase the number of hops to reach peers, in case they are not directly connected or they use loopback. (only for BGP Mode *external*).

### ASN <a href="#_asn" id="_asn"></a>

Every router can be member of exactly one Autonomous System, so any iBGP sessions on a given node (irregardless of address family) need to have the same ASN configured. Any configuration that has two iBGP sessions with different ASNs is rejected and an error thrown, since it is by definition not possible to have two iBGP sessions with different ASNs on the same BGP instance, as one instance can only have one local ASN.

The local ASN of the FRR instance is auto-derived based on the settings in the SDN controllers:

If only a BGP or EVPN controller exists (but not both), then the respective ASN from the controller is used.

For backwards-compatibility reasons, the SDN stack checks if there are any EVPN controllers in auto mode. If a BGP controller exists, then the ASN from the BGP controller will be used in any case.

Otherwise, if an EVPN controller is configured, then the ASN from the EVPN controller is used \- otherwise the ASN from the BGP controller.

The SDN stack utilizes the local-as directive together with the `no-prepend
replace-as` option in the FRR configuration for handling multiple ASN numbers in the configuration. This is the case when the BGP and EVPN controller have different ASNs configured and auto mode is disabled.

### VTEP IP auto-generation <a href="#_vtep_ip_auto_generation" id="_vtep_ip_auto_generation"></a>

The VTEP IPs for the VXLAN devices of a zone will be auto-derived based on the (primary) controller defined in the EVPN zone:

If a BGP or IS-IS controller with a loopback interface is used, then the IP from the loopback interface will be used as VTEP IP.

If the peer list of the controller contains an IP that is locally configured on the node, then this IP will be used as VTEP IP.

Otherwise, the EVPN controller will check the route in the default routing table for the first peer IP and use the source IP address specified in the routing table as VTEP IP. This can cause issues if the route gets announced dynamically e.g. via a fabric. In that case it is necessary for the kernel routing table to contain the required entry when applying the configuration for the EVPN controller.

## 12.9.2. BGP Controller <a href="#pvesdn_controller_plugin_BGP" id="pvesdn_controller_plugin_BGP"></a>

The BGP controller is not used directly by a zone. You can use it to configure FRR to manage BGP peers.

For BGP-EVPN, it can be used to define a different ASN by node, so doing EBGP. It can also be used to export EVPN routes to an external BGP peer.

{% hint style="info" %}
By default, for a simple full mesh EVPN, you don’t need to define a BGP controller.
{% endhint %}

BGP controller configuration options:

**Node**

The node of this BGP controller

**ASN \#**

A unique BGP ASN number. It’s highly recommended to use a private ASN number in the range (64512 \- 65534\) or (4200000000 \- 4294967294), as otherwise you could break global routing by mistake.

**Peer**

A list of peer IP addresses you want to communicate with using the underlying BGP network.

**EBGP**

If your peer’s remote-AS is different, this enables EBGP.

**Loopback Interface**

Use a loopback or dummy interface as the source of the EVPN network (for multipath).

**ebgp-multihop**

Increase the number of hops to reach peers, in case they are not directly connected or they use loopback.

**bgp-multipath-as-path-relax**

Allow ECMP if your peers have different ASN.

## 12.9.3. ISIS Controller <a href="#pvesdn_controller_plugin_ISIS" id="pvesdn_controller_plugin_ISIS"></a>

The ISIS controller is not used directly by a zone. You can use it to configure FRR to export EVPN routes to an ISIS domain.

ISIS controller configuration options:

**Node**

The node of this ISIS controller.

**Domain**

A unique ISIS domain.

**Network Entity Title**

A Unique ISIS network address that identifies this node.

**Interfaces**

A list of physical interface(s) used by ISIS.

**Loopback**

Use a loopback or dummy interface as the source of the EVPN network (for multipath).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
