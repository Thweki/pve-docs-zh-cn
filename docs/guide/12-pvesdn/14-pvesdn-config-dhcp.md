# 12.14. DHCP <a href="#pvesdn_config_dhcp" id="pvesdn_config_dhcp"></a>

Proxmox VE SDN 中的 DHCP 插件可用于自动为区域部署 DHCP 服务器。它为区域中所有配置了 DHCP 范围的子网提供 DHCP。目前唯一可用的 DHCP 后端插件是 dnsmasq 插件。

DHCP 插件的工作方式是：向虚拟机/容器添加新网络接口时，在区域中配置的 IPAM 插件中分配 IP。有关如何配置 IPAM 的更多信息，请参阅 [文档中的相应章节](12-pvesdn-config-ipam.md)。

虚拟机启动时，会在该区域的 DHCP 插件中创建 MAC 地址与 IP 的映射。移除网络接口或销毁虚拟机/容器时，也会删除 IPAM 和 DHCP 服务器中的条目。

{% hint style="info" %}
某些功能（添加/编辑/移除 IP 映射）目前仅在使用 [PVE IPAM 插件](12-pvesdn-config-ipam.md#pvesdn_ipam_plugin_pveipam) 时可用。
{% endhint %}

## 12.14.1. 配置 <a href="#configuration_14" id="configuration_14"></a>

可以在 Web UI 中通过区域面板，并在区域的高级选项中启用 DHCP，来为区域启用自动 DHCP。

{% hint style="info" %}
目前仅 Simple 区域支持自动 DHCP
{% endhint %}

为区域启用自动 DHCP 后，需要为区域中的子网配置 DHCP 范围。为此，进入 VNet 面板并选择要配置 DHCP 范围的子网。在编辑对话框的相应选项卡中，可以配置 DHCP 范围。也可以通过以下 CLI 命令为子网设置 DHCP 范围：

```text
pvesh set /cluster/sdn/vnets/<vnet>/subnets/<subnet>
 -dhcp-range start-address=10.0.1.100,end-address=10.0.1.200
 -dhcp-range start-address=10.0.2.100,end-address=10.0.2.200
```

还需要为子网配置网关，否则自动 DHCP 将无法工作。

DHCP 插件随后仅在配置的范围内通过 IPAM 分配 IP。

不要忘记同时按照 [dnsmasq DHCP 插件](03-pvesdn-installation.md#pvesdn_install_dhcp_ipam) 的安装步骤操作。

## 12.14.2. 插件 <a href="#plugins" id="plugins"></a>

### Dnsmasq 插件 <a href="#dnsmasq_plugin" id="dnsmasq_plugin"></a>

目前这是唯一的 DHCP 插件，因此在为区域启用 DHCP 时会使用此插件。

**安装**

有关安装，请参阅 [DHCP IPAM](03-pvesdn-installation.md#pvesdn_install_dhcp_ipam) 一节。

**配置**

该插件会为部署 dnsmasq 的每个区域创建一个新的 systemd 服务。服务名称为 `dnsmasq@<zone>`。此服务的生命周期由 DHCP 插件管理。

该插件会在文件夹 `/etc/dnsmasq.d/<zone>` 中自动生成以下配置文件：

**`00-default.conf`**

其中包含 dnsmasq 实例的默认全局配置。

**`10-<zone>-<subnet_cidr>.conf`**

此文件配置子网的特定选项，例如应通过 DHCP 配置的 DNS 服务器。

**`10-<zone>-<subnet_cidr>.ranges.conf`**

此文件配置 dnsmasq 实例的 DHCP 范围。

**`ethers`**

此文件包含 IPAM 插件提供的 MAC 地址和 IP 映射。要覆盖这些映射，请使用相应的 IPAM 插件，不要编辑此文件，因为它会被 dnsmasq 插件覆盖。

不得编辑以上任何文件，因为它们由 DHCP 插件管理。要自定义 dnsmasq 配置，可以在配置文件夹中创建其他文件（例如 `90-custom.conf`），dnsmasq DHCP 插件不会修改这些文件。

配置文件按顺序读取，因此可以通过适当命名自定义配置文件来控制配置指令的顺序。

DHCP 租约存储在文件 `/var/lib/misc/dnsmasq.<zone>.leases` 中。

使用 PVE IPAM 插件时，可以更新、创建和删除 DHCP 租约。更多信息请查阅 [PVE IPAM 插件](12-pvesdn-config-ipam.md#pvesdn_ipam_plugin_pveipam) 文档。其他 IPAM 插件目前不支持更改 DHCP 租约。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
