# 12.9. 控制器 <a href="#pvesdn_config_controllers" id="pvesdn_config_controllers"></a>

某些区域实现了分离的控制平面和数据平面，需要外部控制器管理 VNet 的控制平面。

目前，仅 `EVPN` 区域需要外部控制器。

## 12.9.1. EVPN 控制器 <a href="#pvesdn_controller_plugin_evpn" id="pvesdn_controller_plugin_evpn"></a>

`EVPN` 区域需要外部控制器管理控制平面。EVPN 控制器插件配置 Free Range Routing（frr）路由器。

要启用 EVPN 控制器，需要在每个节点上启用 FRR，参见 [安装 FRRouting](03-pvesdn-installation.md#pvesdn_install_frrouting)。

EVPN 控制器配置选项：

**ASN 编号**

唯一的 BGP ASN 编号。强烈建议使用私有 ASN 编号（64512 – 65534、4200000000 – 4294967294），否则可能意外破坏全局路由。在同一节点上配置的每个 EVPN 控制器必须配置相同的 ASN。

**SDN 网络结构**

包含 EVPN 区域中所有节点的 [网络结构](10-pvesdn-config-fabrics.md)。将用作底层网络。

**对等方**

属于 EVPN 区域的所有节点的 IP 列表。（也可以是外部节点或路由反射器服务器）

**节点**

应激活此控制器的节点列表。可用于仅在特定节点上配置 EVPN 对等会话。

**对等组名称**

EVPN 控制器默认使用对等组名称 *VTEP*。定义多个 EVPN 控制器时，每个额外的控制器都需要指定用于 FRR 配置的自定义对等组名称。

**BGP 模式**

允许手动配置 BGP 会话类型。*auto* 模式保留 SDN 协议栈的旧行为：除非配置了 BGP 控制器，否则 EVPN 控制器使用 iBGP。如果配置了 BGP 控制器，EVPN 控制器将复用 BGP 控制器的 BGP 会话。通过此选项，可以手动覆盖 BGP 会话类型，从而显式配置应与 EVPN 控制器建立的 BGP 会话类型。

**ebgp-multihop**

如果对等方不直接连接或使用回环，增加到达对等方的跳数。（仅适用于 BGP 模式 *external*）。

### ASN <a href="#asn" id="asn"></a>

每个路由器只能属于一个自治系统，因此给定节点上的所有 iBGP 会话（无论地址族如何）都需要配置相同的 ASN。任何包含两个不同 ASN 的 iBGP 会话的配置都会被拒绝并引发错误，因为按定义，同一个 BGP 实例不可能具有两个 ASN 不同的 iBGP 会话，一个实例只能具有一个本地 ASN。

FRR 实例的本地 ASN 根据 SDN 控制器中的设置自动推导：

如果仅存在 BGP 或 EVPN 控制器（但并非两者都存在），则使用相应控制器的 ASN。

出于向后兼容的考虑，SDN 协议栈会检查是否存在处于 auto 模式的 EVPN 控制器。如果存在 BGP 控制器，则无论如何都将使用 BGP 控制器的 ASN。

否则，如果配置了 EVPN 控制器，则使用 EVPN 控制器的 ASN；否则使用 BGP 控制器的 ASN。

SDN 协议栈在 FRR 配置中将 local-as 指令与 `no-prepend
replace-as` 选项结合使用，以处理配置中的多个 ASN 编号。当 BGP 和 EVPN 控制器配置了不同的 ASN 且禁用了 auto 模式时，就属于此情况。

### VTEP IP 自动生成 <a href="#vtep_ip_auto_generation" id="vtep_ip_auto_generation"></a>

区域的 VXLAN 设备的 VTEP IP 会根据 EVPN 区域中定义的（主）控制器自动推导：

如果使用带有回环接口的 BGP 或 IS-IS 控制器，则将回环接口的 IP 用作 VTEP IP。

如果控制器的对等方列表包含节点本地配置的 IP，则将此 IP 用作 VTEP IP。

否则，EVPN 控制器会检查默认路由表中到第一个对等方 IP 的路由，并将路由表中指定的源 IP 地址用作 VTEP IP。如果路由通过网络结构等方式动态通告，可能会导致问题。在这种情况下，应用 EVPN 控制器配置时，内核路由表必须包含所需条目。

## 12.9.2. BGP 控制器 <a href="#pvesdn_controller_plugin_bgp" id="pvesdn_controller_plugin_bgp"></a>

区域不直接使用 BGP 控制器。可以使用它配置 FRR 来管理 BGP 对等方。

对于 BGP-EVPN，可用它为每个节点定义不同的 ASN，从而实现 EBGP。也可用它向外部 BGP 对等方导出 EVPN 路由。

{% hint style="info" %}
默认情况下，简单的全网状 EVPN 不需要定义 BGP 控制器。
{% endhint %}

BGP 控制器配置选项：

**节点**

此 BGP 控制器所在的节点

**ASN 编号**

唯一的 BGP ASN 编号。强烈建议使用范围为（64512 \- 65534）或（4200000000 \- 4294967294）的私有 ASN 编号，否则可能意外破坏全局路由。

**对等方**

希望通过底层 BGP 网络与之通信的对等方 IP 地址列表。

**EBGP**

如果对等方的 remote-AS 不同，此选项将启用 EBGP。

**回环接口**

将回环或 dummy 接口用作 EVPN 网络的源（用于多路径）。

**ebgp-multihop**

如果对等方不直接连接或使用回环，增加到达对等方的跳数。

**bgp-multipath-as-path-relax**

如果对等方具有不同的 ASN，允许 ECMP。

## 12.9.3. ISIS 控制器 <a href="#pvesdn_controller_plugin_isis" id="pvesdn_controller_plugin_isis"></a>

区域不直接使用 ISIS 控制器。可以使用它配置 FRR，将 EVPN 路由导出到 ISIS 域。

ISIS 控制器配置选项：

**节点**

此 ISIS 控制器所在的节点。

**域**

唯一的 ISIS 域。

**网络实体名称**

标识此节点的唯一 ISIS 网络地址。

**接口**

ISIS 使用的物理接口列表。

**回环**

将回环或 dummy 接口用作 EVPN 网络的源（用于多路径）。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
