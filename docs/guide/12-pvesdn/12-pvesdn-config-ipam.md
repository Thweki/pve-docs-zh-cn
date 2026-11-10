# 12.12. IPAM <a href="#pvesdn_config_ipam" id="pvesdn_config_ipam"></a>

IP Address Management (IPAM) tools manage the IP addresses of clients on the network. SDN in Proxmox VE uses IPAM for example to find free IP addresses for new guests.

A single IPAM instance can be associated with one or more zones.

## 12.12.1. PVE IPAM Plugin <a href="#pvesdn_ipam_plugin_pveipam" id="pvesdn_ipam_plugin_pveipam"></a>

The default built-in IPAM for your Proxmox VE cluster.

You can inspect the current status of the PVE IPAM Plugin via the IPAM panel in the SDN section of the datacenter configuration. This UI can be used to create, update and delete IP mappings. This is particularly convenient in conjunction with the [DHCP feature](14-pvesdn-config-dhcp.md#pvesdn_config_dhcp).

If you are using DHCP, you can use the IPAM panel to create or edit leases for specific VMs, which enables you to change the IPs allocated via DHCP. When editing an IP of a VM that is using DHCP you must make sure to force the guest to acquire a new DHCP leases. This can usually be done by reloading the network stack of the guest or rebooting it.

## 12.12.2. NetBox IPAM Plugin <a href="#pvesdn_ipam_plugin_netbox" id="pvesdn_ipam_plugin_netbox"></a>

[NetBox](https://github.com/netbox-community/netbox) is an open-source IP Address Management (IPAM) and datacenter infrastructure management (DCIM) tool.

To integrate NetBox with Proxmox VE SDN, create an API token in NetBox as described here: [https://docs.netbox.dev/en/stable/integrations/rest-api/#tokens](https://docs.netbox.dev/en/stable/integrations/rest-api/#tokens)

The NetBox configuration properties are:

**URL**

The NetBox REST API endpoint: `http://yournetbox.domain.com/api`

**Token**

An API access token

**Fingerprint**

The SHA-256 fingerprint of the NetBox API. Can be retrieved with `openssl x509 -in /etc/ssl/certs/netbox.crt -noout -fingerprint -sha256` when using the default certificate.

## 12.12.3. phpIPAM Plugin <a href="#pvesdn_ipam_plugin_phpipam" id="pvesdn_ipam_plugin_phpipam"></a>

In [phpIPAM](https://phpipam.net/) you need to create an "application" and add an API token with admin privileges to the application.

The phpIPAM configuration properties are:

**URL**

The REST-API endpoint: `http://phpipam.domain.com/api/<appname>/`

**Token**

An API access token

**Section**

An integer ID. Sections are a group of subnets in phpIPAM. Default installations use `sectionid=1` for customers.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
