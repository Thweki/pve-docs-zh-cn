# 12.7. VNet <a href="#pvesdn_config_vnet" id="pvesdn_config_vnet"></a>

通过 SDN GUI 创建虚拟网络（VNet）后，每个节点上都会出现同名的本地网络接口。要将客户机连接到 VNet，请将该接口分配给客户机，并相应设置 IP 地址。

根据区域的不同，这些选项具有不同含义，本文档相应区域的章节中进行了说明。

{% hint style="warning" %}
目前，某些选项可能在特定区域中无效或无法工作。
{% endhint %}

VNet 配置选项：

**ID**

标识 VNet 的 ID，最多 8 个字符

**别名**

更具描述性的标识符。作为别名分配给接口。可选

**区域**

此 VNet 关联的区域

**标签**

唯一的 VLAN 或 VXLAN ID

**VLAN 感知**

在接口上启用 vlan-aware 选项，允许在客户机中配置。

**隔离端口**

为此接口的所有客户机端口设置隔离标志，但不对接口本身设置。这意味着客户机只能向非隔离的网桥端口发送流量，也就是网桥本身。要使此设置生效，需要重启受影响的客户机。

{% hint style="info" %}
端口隔离仅在每台宿主机本地生效。使用 [VNET 防火墙](15-pvesdn-firewall-integration.md) 进一步隔离 VNET 内跨节点的流量。例如，默认 DROP，仅允许从 IP 子网到网关及反向的流量。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
