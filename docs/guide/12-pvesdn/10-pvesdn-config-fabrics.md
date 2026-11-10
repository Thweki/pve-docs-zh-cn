# 12.10. Fabrics <a href="#pvesdn_config_fabrics" id="pvesdn_config_fabrics"></a>

[![screenshot/gui-datacenter-fabrics-overview.png](../../assets/screenshot-gui-datacenter-fabrics-overview-png-c99a393b26d1.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-fabrics-overview.png)

Fabrics in Proxmox VE SDN provide automated routing between nodes in a cluster. They simplify the configuration of underlay networks between nodes to form the foundation for SDN deployments.

They automatically configure routing protocols on your physical network interfaces to establish connectivity between nodes in the cluster. This creates a resilient, auto-configuring network fabric that adapts to changes in network topology. These fabrics can be used as a full-mesh network for Ceph or in the EVPN controller and VXLAN zone.

## 12.10.1. Installation <a href="#_installation" id="_installation"></a>

The FRR implementations of OpenFabric and OSPF are used, so first ensure that the `frr` and `frr-pythontools` packages are installed:

```text
apt update
apt install frr frr-pythontools
```

## 12.10.2. Permissions <a href="#_permissions_2" id="_permissions_2"></a>

To view the configuration of an SDN fabric users need SDN.Audit or SDN.Allocate permissions. To create or modify a fabric configuration, users need SDN.Allocate permissions. To view the configuration of a node, users need the Sys.Audit or Sys.Modify permissions. When adding or updating nodes within a fabric, additional Sys.Modify permission for the specific node is required, since this operation involves writing to the node’s /etc/network/interfaces file.

## 12.10.3. Configuration <a href="#_configuration_13" id="_configuration_13"></a>

To create a Fabric, head over to Datacenter→SDN→Fabrics and click "Add Fabric". After selecting the preferred protocol, the fabric is created. With the "+" button you can select the nodes which you want to add to the fabric, you also have to select the interfaces used to communicate with the other nodes.

### Loopback Prefix <a href="#_loopback_prefix" id="_loopback_prefix"></a>

You can specify a CIDR network range (e.g., 192.0.2.0/24) as a loopback prefix for the fabric. When configured, the system will automatically verify that all router-IDs are contained within this prefix. This ensures consistency in your addressing scheme and helps prevent addressing conflicts or errors.

### Router-ID Selection <a href="#_router_id_selection" id="_router_id_selection"></a>

Each node in a fabric needs a unique router-ID, which is an IPv4 address in dotted decimal notation (e.g., 192.0.2.1). In OpenFabric this can also be an IPv6 address in the typical hexadecimal representation separated by colons (e.g., 2001:db8::1428:57ab). A dummy interface with the router-ID as address will automatically be created and will act as a loopback interface for the fabric (it’s also passive by default).

### RouteMaps <a href="#_routemaps" id="_routemaps"></a>

For every fabric, an access-list and a route-map are automatically created. These configure the router to rewrite the source address of outgoing packets. When you communicate with another node (for example, by pinging it), this ensures that traffic originates from the local dummy interface’s IP address rather than from the physical interface. This provides consistent routing behavior and proper source address selection throughout the fabric.

### Notes on IPv6 <a href="#pvesdn_config_fabrics_ipv6" id="pvesdn_config_fabrics_ipv6"></a>

IPv6 is currently only usable on OpenFabric fabrics. These IPv6 Fabrics need global IPv6 forwarding enabled on all nodes contained in the fabric. Without IPv6 forwarding, non-full-mesh fabrics won’t work because the transit nodes don’t forward packets to the outer nodes. Currently there isn’t an easy way to enable IPv6 forwarding per-interface like with IPv4, so it has to be enabled globally. This can be accomplished by appending this line:

```text
post-up sysctl -w net.ipv6.conf.all.forwarding=1
```

to a fabric interface in the `/etc/network/interfaces` file. This will enable IPv6 forwarding globally once that interface comes up. Note that this affects how your interfaces handle automatic IPv6 setup (SLAAC), Neighbour Advertisements, Router Solicitations, and Router Advertisements. More details here: [https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt) under `net.ipv6.conf.all.forwarding`.

## 12.10.4. OpenFabric <a href="#pvesdn_openfabric" id="pvesdn_openfabric"></a>

OpenFabric is a routing protocol specifically designed for data center fabrics. It’s based on IS-IS and optimized for the spine-leaf topology common in data centers.

[![screenshot/gui-datacenter-create-fabric-openfabric.png](../../assets/screenshot-gui-datacenter-create-fabric-openfabric-png-2d126fc4d343.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-fabric-openfabric.png)

Configuration options:

### On the Fabric <a href="#pvesdn_openfabric_fabric" id="pvesdn_openfabric_fabric"></a>

**Name**

This is the name of the OpenFabric fabric and can be at most 8 characters long.

**IPv4 Prefix**

IPv4 CIDR network range (e.g., 192.0.2.0/24) used to verify that all router-IDs in the fabric are contained within this prefix.

**IPv6 Prefix**

IPv6 CIDR network range (e.g., 2001:db8::/64) used to verify that all router-IDs in the fabric are contained within this prefix.

{% hint style="warning" %}
For IPv6 fabrics to work, global forwarding needs to be enabled on all nodes. Check [Notes on IPv6](#pvesdn_config_fabrics_ipv6) for how to do it and additional info.
{% endhint %}

**Hello Interval**

Controls how frequently (in seconds) hello packets are sent to discover and maintain connections with neighboring nodes. Lower values detect failures faster but increase network traffic. This option is global on the fabric, meaning every interface on every node in this fabric will inherit this hello-interval property. The default value is 3 seconds.

**CSNP Interval**

Sets how frequently (in seconds) the node synchronizes its routing database with neighbors. Lower values keep the network topology information more quickly in sync but increase network traffic. This option is global on the fabric, meaning every interface on every node in this fabric will inherit this property. The default value is 10 seconds.

### On the Node <a href="#pvesdn_openfabric_node" id="pvesdn_openfabric_node"></a>

[![screenshot/gui-datacenter-create-node-openfabric.png](../../assets/screenshot-gui-datacenter-create-node-openfabric-png-576369f483c5.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-node-openfabric.png)

Options that are available on every node that is part of a fabric:

**Node**

Select the node which will be added to the fabric. Only nodes that currently are in the cluster will be shown.

**IPv4**

A unique IPv4 address used to generate the OpenFabric Network Entity Title (NET). Each node in the same fabric must have a different Router-ID, while a single node must use the same NET address across all fabrics (If this is not given Proxmox VE will automatically choose one and ensure that the configuration is valid).

**IPv6**

A unique IPv6 address used to generate the OpenFabric Network Entity Title (NET). Each node in the same fabric must have a different Router-ID, while a single node must use the same NET address across all fabrics. If a IPv4 and IPv6 address is configured, the IPv4 one will be used to derive the NET.

{% hint style="warning" %}
When using IPv6 addresses, the last 3 segments are used to generate the NET. Ensure these segments differ between nodes.
{% endhint %}

**Interfaces**

Specify the interfaces used to establish peering connections with other OpenFabric nodes. Preferably select interfaces without pre-assigned IP addresses, then configure addresses in the IPv4/IPv6 column if needed. A dummy "loopback" interface with the router-id is automatically created.

### On The Interface <a href="#_on_the_interface" id="_on_the_interface"></a>

The following optional parameters can be configured per interface when enabling the additional columns:

**IP**

A IPv4 that should get automatically configured on this interface. Must include the netmask (e.g. /31)

**IPv6**

A IPv6 that should get automatically configured on this interface. Must include the netmask (e.g. /127).

**Hello Multiplier**

Defines how many missed hello packets constitute a failed connection. Higher values make the connection more resilient to packet loss but slow down failure detection. The default value is 10.

{% hint style="warning" %}
When you remove an interface with an entry in `/etc/network/interfaces` that has `manual` set, then the IP will not get removed on applying the SDN configuration.
{% endhint %}

## 12.10.5. OSPF <a href="#pvesdn_ospf" id="pvesdn_ospf"></a>

OSPF (Open Shortest Path First) is a widely-used link-state routing protocol that efficiently calculates the shortest path for routing traffic through IP networks.

[![screenshot/gui-datacenter-create-fabric-ospf.png](../../assets/screenshot-gui-datacenter-create-fabric-ospf-png-80bda2875d3b.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-fabric-ospf.png)

Configuration options:

### On the Fabric <a href="#pvesdn_ospf_fabric" id="pvesdn_ospf_fabric"></a>

**IPv4 Prefix**

IPv4 CIDR network range (e.g., 192.0.2.0/24) used to verify that all router-IDs in the fabric are contained within this prefix.

**Area**

This specifies the OSPF area identifier, which can be either a 32-bit signed integer or an IP address. Areas are a way to organize and structure OSPF networks hierarchically, with Area 0 (or 0.0.0.0) serving as the backbone area.

**Redistribute**

Optional list of source protocols whose routes are imported into OSPF. Each entry picks a source (`bgp`, `connected`, `kernel` or `static`) and may additionally reference a [route map](11-pvesdn-config-route-filtering.md#pvesdn_config_route_maps) to filter or transform routes before they are advertised. Useful for example to leak BGP fabric routes into OSPF, or to advertise locally connected networks without configuring them per interface.

### On the Node <a href="#pvesdn_ospf_node" id="pvesdn_ospf_node"></a>

[![screenshot/gui-datacenter-create-node-ospf.png](../../assets/screenshot-gui-datacenter-create-node-ospf-png-66f01ebaaa66.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-node-ospf.png)

Options that are available on every node that is part of a fabric:

**Node**

Select the node which will be added to the fabric. Only nodes that are currently in the cluster will be shown.

**IPv4**

A unique Router-ID used to identify this router within the OSPF network. Each node in the same fabric must have a different Router-ID.

**Interfaces**

Specify the interfaces used to establish peering connections with other OSPF nodes. Preferably select interfaces without pre-assigned IP addresses, then configure addresses in the IPv4 column if needed. A dummy "loopback" interface with the router-id is automatically created.

### On The Interface <a href="#_on_the_interface_2" id="_on_the_interface_2"></a>

The following optional parameter can be configured per interface:

**IP**

A IPv4 that should get automatically configured on this interface. Must include the netmask (e.g. /31)

{% hint style="warning" %}
When you remove an interface with an entry in `/etc/network/interfaces` that has `manual` set, then the IP will not get removed on applying the SDN configuration.
{% endhint %}

{% hint style="info" %}
The dummy interface will automatically be configured as `passive`. Every interface which doesn’t have an ip-address configured will be treated as a `point-to-point` link.
{% endhint %}

## 12.10.6. WireGuard <a href="#pvesdn_wireguard" id="pvesdn_wireguard"></a>

WireGuard can be used for establishing a VPN between Proxmox VE nodes and / or external nodes. It does not provide dynamic routing by itself, but can be used in conjunction with dynamic routing protocols operating on layer 3 and above (OSPF, BGP) to provide a dynamically routed, encrypted transport, for example to carry EVPN or VXLAN traffic.

{% hint style="info" %}
In order to use WireGuard, the package `wireguard-tools` needs to be installed.
{% endhint %}

Configuration options:

### On the Fabric <a href="#pvesdn_wireguard_fabric" id="pvesdn_wireguard_fabric"></a>

**Name**

This is the name of the WireGuard fabric and can be at most 8 characters long.

**Persistent Keepalive**

If this is set, then WireGuard will send an empty authenticated packet every N seconds to each configured peer. This can help keeping connections alive when using stateful firewalls or NAT.

### On the Node <a href="#pvesdn_wireguard_node" id="pvesdn_wireguard_node"></a>

There are two types of nodes: internal and external. Internal nodes are Proxmox VE nodes, external nodes everything else. They are essentially reusable peer definitions that can be used across the whole cluster.

**Internal**

**Endpoint**

This is the IP or hostname that other Proxmox VE nodes should use for connecting to this Proxmox VE node (e.g. `192.0.2.1` / `2001:db8::1`). This is used together with the *Listen Port* configured on the separate interfaces for constructing the actual endpoint. For instance, if a node has the IP `192.0.2.1` as an *Endpoint* and an interface `wg0` with *Listen Port* `51820` configured, then other nodes will use `192.0.2.1:51820` as endpoint for connecting to this node.

**Allowed IPs**

A comma-separated list of CIDRs (for example `198.51.100.0/24`, or `0.0.0.0/0` to tunnel all IPv4 traffic). When selecting this node as a peer on other nodes, the list is used as the `AllowedIPs` setting in the WireGuard peer configuration, that is, both the source filter for incoming traffic and the routing destination for outgoing traffic to this node.

**External**

**Name**

The name of the external node.

**Public Key**

The public key used by the external node.

**Endpoint**

The IP or hostname together with the port that other nodes use to connect to this external peer (e.g. `192.0.2.1:51820`). If an endpoint uses an IPv6 address, then the address needs to be enclosed in square brackets (e.g. `[2001:db8::1]:51820`).

**Allowed IPs**

A comma-separated list of CIDRs (for example `198.51.100.0/24`, or `0.0.0.0/0` to tunnel all IPv4 traffic). When selecting this node as a peer on other nodes, the list is used as the `AllowedIPs` setting in the WireGuard peer configuration, that is, both the source filter for incoming traffic and the routing destination for outgoing traffic to this node.

### On The Interface <a href="#pvesdn_wireguard_interface" id="pvesdn_wireguard_interface"></a>

**Name**

The name of the network interface on the Linux host. One to eight characters that must start with an alphanumeric character; the remaining characters may be alphanumeric or hyphens.

**IP**

The IPv4 address in CIDR notation that should be configured on this interface (for example `198.51.100.1/24`).

**IPv6**

The IPv6 address in CIDR notation that should be configured on this interface (for example `2001:db8::1/64`).

**Listen Port**

The listening port for this interface.

**Peers**

A list of peers that should be configured for that interface. All nodes that are part of the fabric can be selected as peers - the peer definition will be auto-generated from the configuration in the node.

When defining an interface, Proxmox VE automatically generates a private key for it in `/etc/pve/priv/wg-keys.cfg` upon saving the interface, and stores the matching public key alongside the interface in the fabric configuration so it can be shown in the Web UI when editing the node. Removing an interface from a node removes the corresponding private key from `wg-keys.cfg` as part of the same API call.

The fabric automatically generates routes through the WireGuard interface for every peer’s allowed IPs. For example, if interface wg0 has two peers with `198.51.100.0/24` and `203.0.113.0/24` as allowed IPs, then routes for both subnets are created. If the peer references the interface of a Proxmox VE node, that interface’s configured IP address is additionally added as a host route to the allowed IPs (for example, a peer node configured with `192.0.2.10/24` gets `192.0.2.10/32` added).

### On The Peer <a href="#pvesdn_wireguard_peer" id="pvesdn_wireguard_peer"></a>

**Skip Route Generation**

The fabric will autogenerate routes in the kernel routing table for all allowed IPs of a peer. By setting this option, no routes will be inserted into the kernel routing table.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
