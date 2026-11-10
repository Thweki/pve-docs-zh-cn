# 12.4. Configuration Overview <a href="#pvesdn_main_configuration" id="pvesdn_main_configuration"></a>

Configuration is done at the web UI at datacenter level, separated into the following sections:

- SDN: Here you get an overview of the current active SDN state, and you can apply all pending changes to the whole cluster.
- [Zones](06-pvesdn-config-zone.md#pvesdn_config_zone): Create and manage the virtually separated network zones
- [VNets](07-pvesdn-config-vnet.md#pvesdn_config_vnet): Create virtual network bridges and manage subnets

The Options category allows adding and managing additional services to be used in your SDN setup.

- [Controllers](09-pvesdn-config-controllers.md#pvesdn_config_controllers): For controlling layer 3 routing in complex setups
- [DHCP](14-pvesdn-config-dhcp.md#pvesdn_config_dhcp): Define a DHCP server for a zone that automatically allocates IPs for guests in the IPAM and leases them to the guests via DHCP.
- [IPAM](12-pvesdn-config-ipam.md#pvesdn_config_ipam): Enables external for IP address management for guests
- [DNS](13-pvesdn-config-dns.md#pvesdn_config_dns): Define a DNS server integration for registering virtual guests' hostname and IP addresses

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
