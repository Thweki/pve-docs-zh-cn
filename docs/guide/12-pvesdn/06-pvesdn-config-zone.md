# 12.6. 区域 <a href="#pvesdn_config_zone" id="pvesdn_config_zone"></a>

区域定义一个虚拟隔离的网络。区域被限制到特定节点并分配权限，以便将用户限制在某个区域及其中包含的 VNet 内。

可使用不同技术实现隔离：

- Simple：隔离的网桥。一个简单的三层路由网桥（NAT）
- VLAN：虚拟局域网是细分局域网的传统方法
- QinQ：堆叠 VLAN（正式名称为 `IEEE 802.1ad`）
- VXLAN：通过 UDP 隧道建立的二层 VXLAN 网络
- EVPN（BGP EVPN）：结合 BGP 的 VXLAN，用于建立三层路由

## 12.6.1. 通用选项 <a href="#pvesdn_config_common_options" id="pvesdn_config_common_options"></a>

以下选项适用于所有区域类型：

**节点**

应部署该区域及相关 VNet 的节点。

**IPAM**

使用 IP 地址管理（IPAM）工具管理区域中的 IP。可选，默认为 `pve`。

**DNS**

DNS API 服务器。可选。

**ReverseDNS**

反向 DNS API 服务器。可选。

**DNSZone**

DNS 域名。用于注册主机名，例如 `<hostname>.<domain>`。DNS 区域必须已存在于 DNS 服务器上。可选。

## 12.6.2. Simple 区域 <a href="#pvesdn_zone_plugin_simple" id="pvesdn_zone_plugin_simple"></a>

这是最简单的插件。它会创建一个隔离的 VNet 网桥。此网桥不连接物理接口，虚拟机流量仅在各节点本地流通。可用于 NAT 或路由设置。

## 12.6.3. VLAN 区域 <a href="#pvesdn_zone_plugin_vlan" id="pvesdn_zone_plugin_vlan"></a>

VLAN 插件使用现有的本地 Linux 或 OVS 网桥连接节点的物理接口。它使用 VNet 中定义的 VLAN 标签隔离网段。这可实现不同节点之间的虚拟机连接。

VLAN 区域配置选项：

**网桥**

本地网桥或 OVS 交换机，已在 **每个** 节点上配置，允许节点间连接。

## 12.6.4. QinQ 区域 <a href="#pvesdn_zone_plugin_qinq" id="pvesdn_zone_plugin_qinq"></a>

QinQ 又称 VLAN 堆叠，使用多层 VLAN 标签进行隔离。QinQ 区域定义外层 VLAN 标签（*服务 VLAN*），而内层 VLAN 标签由 VNet 定义。

{% hint style="info" %}
物理网络交换机必须支持堆叠 VLAN 才能使用此配置。
{% endhint %}

QinQ 区域配置选项：

**网桥**

已在每个本地节点上配置的、支持 VLAN 感知的本地网桥

**服务 VLAN**

此区域的主 VLAN 标签

**服务 VLAN 协议**

允许选择 802.1q（默认）或 802.1ad 服务 VLAN 类型。

**MTU**

由于标签双层堆叠，QinQ VLAN 需要额外 4 字节。例如，必须将 MTU 减小为 `1496`，如果物理接口 MTU 为 `1500`。

## 12.6.5. VXLAN 区域 <a href="#pvesdn_zone_plugin_vxlan" id="pvesdn_zone_plugin_vxlan"></a>

VXLAN 插件在现有网络（底层网络）上建立隧道（覆盖网络）。它将二层以太网帧封装在四层 UDP 数据报中，使用默认目标端口 `4789`。

必须自行配置底层网络，以实现所有对等方之间的 UDP 连接。

例如，可以在公共互联网上创建 VXLAN 覆盖网络，使虚拟机看起来就像共享同一个本地二层网络。

{% hint style="warning" %}
VXLAN 本身不提供任何加密。通过 VXLAN 连接多个站点时，务必在站点之间建立安全连接，例如使用站点到站点 VPN。
{% endhint %}

VXLAN 区域配置选项：

**对等方地址列表**

VXLAN 区域中每个节点的 IP 地址列表。可以是通过此 IP 地址可达的外部节点。此处必须列出集群中的所有节点。

**SDN 网络结构**

使用 [网络结构](10-pvesdn-config-fabrics.md) 自动生成对等方列表，以替代手动定义所有对等方。

**MTU**

由于 VXLAN 封装占用 50 字节，MTU 需要比传出物理接口低 50 字节。

## 12.6.6. EVPN 区域 <a href="#pvesdn_zone_plugin_evpn" id="pvesdn_zone_plugin_evpn"></a>

EVPN 区域创建可跨多个集群的可路由三层网络。这通过建立 VPN 并使用 BGP 作为路由协议来实现。

EVPN 的 VNet 可具有任播 IP 地址和/或 MAC 地址。各节点的网桥 IP 相同，因此虚拟客户机可将此地址用作网关。

路由可通过 VRF（虚拟路由与转发）接口跨不同区域的 VNet 工作。

EVPN 区域配置选项：

**VRF VXLAN ID**

用于 VNet 之间专用路由互联的 VXLAN-ID。必须与 VNet 的 VXLAN-ID 不同。

**主控制器**

此区域使用的主 EVPN 控制器。主控制器用于根据对等方定义自动推导 VTEP IP。更多信息请参阅 [控制器一节](09-pvesdn-config-controllers.md#pvesdn_controller_plugin_evpn)。

**其他控制器**

此区域使用的其他 EVPN 控制器。此处列出的控制器会通告此区域的 L2VPN EVPN 路由。

**VNet MAC 地址**

分配给此区域所有 VNet 的任播 MAC 地址。如果未定义，将自动生成。

**出口节点**

应配置为从 EVPN 网络通过实际网络出去的出口网关的节点。配置的节点会在 EVPN 网络中通告默认路由。可选。

**主出口节点**

如果使用多个出口节点，强制流量通过此主出口节点，而非在所有节点上进行负载均衡。可选，但如果要使用 SNAT 或上游路由器不支持 ECMP，则必须设置。

**出口节点本地路由**

如果需要从出口节点访问虚拟机/容器服务，可使用此特殊选项。（默认情况下，出口节点仅允许在实际网络与 EVPN 网络之间转发流量。）可选。

**通告子网**

在 EVPN 网络中通告整个子网。如果存在静默的虚拟机/容器（例如有多个 IP，而任播网关看不到这些 IP 的流量，则这些 IP 地址将无法在 EVPN 网络内部访问）。可选。

**禁用 ARP ND 抑制**

不抑制 ARP 或 ND（邻居发现）数据包。如果在虚拟机中使用浮动 IP（IP 和 MAC 地址在系统之间移动），则需要此选项。可选。

**导入路由目标**

允许导入外部 EVPN 路由目标列表。用于跨数据中心或不同 EVPN 网络的互联。可选。

**MTU**

由于 VXLAN 封装占用 50 字节，MTU 需要比传出物理接口的最大 MTU 低 50 字节。可选，默认为 1450。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
