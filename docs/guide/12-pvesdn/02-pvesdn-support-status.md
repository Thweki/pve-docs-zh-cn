# 12.2. 支持状态 <a href="#pvesdn_support_status" id="pvesdn_support_status"></a>

## 12.2.1. 历史 <a href="#history" id="history"></a>

Proxmox VE SDN 协议栈自 2019 年起作为实验性功能提供，并一直由众多开发者和用户持续改进和测试。在 Proxmox VE 6.2 中集成到 Web 界面，标志着迈向更广泛集成的重要里程碑。在 Proxmox VE 7 发布周期中，增加了许多改进和功能。根据用户反馈，可以看出基本设计选择及其实现相当可靠、稳定。因此，将其标记为“实验性”已不能准确反映 SDN 协议栈的状态。在 Proxmox VE 8 中，决定将网络和接口管理提升为 Proxmox VE 访问控制栈的核心组件，为全面集成 SDN 功能奠定基础。在 Proxmox VE 8.1 中实现了两个主要里程碑：首先，在 IP 地址管理（IPAM）功能中加入了 DHCP 集成；其次，现在默认安装 SDN 集成。

## 12.2.2. 当前状态 <a href="#current_status" id="current_status"></a>

SDN 安装各层的当前支持状态如下：

- 核心 SDN 包括 VNet 管理及其与 Proxmox VE 协议栈的集成，已获得完全支持。
- IPAM（包括虚拟客户机的 DHCP 管理）处于技术预览阶段。
- 通过 FRRouting 的复杂路由和控制器集成处于技术预览阶段。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
