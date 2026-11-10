# 12.14. DHCP <a href="#pvesdn_config_dhcp" id="pvesdn_config_dhcp"></a>

The DHCP plugin in Proxmox VE SDN can be used to automatically deploy a DHCP server for a Zone. It provides DHCP for all Subnets in a Zone that have a DHCP range configured. Currently the only available backend plugin for DHCP is the dnsmasq plugin.

The DHCP plugin works by allocating an IP in the IPAM plugin configured in the Zone when adding a new network interface to a VM/CT. You can find more information on how to configure an IPAM in the [respective section of our documentation](12-pvesdn-config-ipam.md#pvesdn_config_ipam).

When the VM starts, a mapping for the MAC address and IP gets created in the DHCP plugin of the zone. When the network interfaces is removed or the VM/CT are destroyed, then the entry in the IPAM and the DHCP server are deleted as well.

{% hint style="info" %}
Some features (adding/editing/removing IP mappings) are currently only available when using the [PVE IPAM plugin](12-pvesdn-config-ipam.md#pvesdn_ipam_plugin_pveipam).
{% endhint %}

## 12.14.1. Configuration <a href="#_configuration_14" id="_configuration_14"></a>

You can enable automatic DHCP for a zone in the Web UI via the Zones panel and enabling DHCP in the advanced options of a zone.

{% hint style="info" %}
Currently only Simple Zones have support for automatic DHCP
{% endhint %}

After automatic DHCP has been enabled for a Zone, DHCP Ranges need to be configured for the subnets in a Zone. In order to that, go to the Vnets panel and select the Subnet for which you want to configure DHCP ranges. In the edit dialogue you can configure DHCP ranges in the respective Tab. Alternatively you can set DHCP ranges for a Subnet via the following CLI command:

```text
pvesh set /cluster/sdn/vnets/<vnet>/subnets/<subnet>
 -dhcp-range start-address=10.0.1.100,end-address=10.0.1.200
 -dhcp-range start-address=10.0.2.100,end-address=10.0.2.200
```

You also need to have a gateway configured for the subnet \- otherwise automatic DHCP will not work.

The DHCP plugin will then allocate IPs in the IPAM only in the configured ranges.

Do not forget to follow the installation steps for the [dnsmasq DHCP plugin](03-pvesdn-installation.md#pvesdn_install_dhcp_ipam) as well.

## 12.14.2. Plugins <a href="#_plugins" id="_plugins"></a>

### Dnsmasq Plugin <a href="#_dnsmasq_plugin" id="_dnsmasq_plugin"></a>

Currently this is the only DHCP plugin and therefore the plugin that gets used when you enable DHCP for a zone.

**Installation**

For installation see the [DHCP IPAM](03-pvesdn-installation.md#pvesdn_install_dhcp_ipam) section.

**Configuration**

The plugin will create a new systemd service for each zone that dnsmasq gets deployed to. The name for the service is `dnsmasq@<zone>`. The lifecycle of this service is managed by the DHCP plugin.

The plugin automatically generates the following configuration files in the folder `/etc/dnsmasq.d/<zone>`:

**`00-default.conf`**

This contains the default global configuration for a dnsmasq instance.

**`10-<zone>-<subnet_cidr>.conf`**

This file configures specific options for a subnet, such as the DNS server that should get configured via DHCP.

**`10-<zone>-<subnet_cidr>.ranges.conf`**

This file configures the DHCP ranges for the dnsmasq instance.

**`ethers`**

This file contains the MAC-address and IP mappings from the IPAM plugin. In order to override those mappings, please use the respective IPAM plugin rather than editing this file, as it will get overwritten by the dnsmasq plugin.

You must not edit any of the above files, since they are managed by the DHCP plugin. In order to customize the dnsmasq configuration you can create additional files (e.g. `90-custom.conf`) in the configuration folder \- they will not get changed by the dnsmasq DHCP plugin.

Configuration files are read in order, so you can control the order of the configuration directives by naming your custom configuration files appropriately.

DHCP leases are stored in the file `/var/lib/misc/dnsmasq.<zone>.leases`.

When using the PVE IPAM plugin, you can update, create and delete DHCP leases. For more information please consult the documentation of [the PVE IPAM plugin](12-pvesdn-config-ipam.md#pvesdn_ipam_plugin_pveipam). Changing DHCP leases is currently not supported for the other IPAM plugins.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
