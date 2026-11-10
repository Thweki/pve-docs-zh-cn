# 12.8. Subnets <a href="#pvesdn_config_subnet" id="pvesdn_config_subnet"></a>

A subnet define a specific IP range, described by the CIDR network address. Each VNet, can have one or more subnets.

A subnet can be used to:

- Restrict the IP addresses you can define on a specific VNet
- Assign routes/gateways on a VNet in layer 3 zones
- Enable SNAT on a VNet in layer 3 zones
- Auto assign IPs on virtual guests (VM or CT) through IPAM plugins
- DNS registration through DNS plugins

If an IPAM server is associated with the subnet zone, the subnet prefix will be automatically registered in the IPAM.

Subnet configuration options:

**ID**

A CIDR network address, for example 10.0.0.0/8

**Gateway**

The IP address of the network’s default gateway. On layer 3 zones (Simple/EVPN plugins), it will be deployed on the VNet.

**SNAT**

Enable Source NAT which allows VMs from inside a VNet to connect to the outside network by forwarding the packets to the nodes outgoing interface. On EVPN zones, forwarding is done on EVPN gateway-nodes. Optional.

**DNS Zone Prefix**

Add a prefix to the domain registration, like \<hostname\>.prefix.\<domain\> Optional.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
