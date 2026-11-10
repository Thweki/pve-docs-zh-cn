# 1.5. 灵活的网络 <a href="#_flexible_networking" id="_flexible_networking"></a>

Proxmox VE 使用网桥网络模型。所有虚拟机都可以共享一个网桥，就好像每台客户机的虚拟网线都插入了同一台交换机。为将虚拟机连接到外部网络，可将网桥接入物理网卡，并为其分配 TCP/IP 配置。

为了进一步提高灵活性，系统还提供虚拟局域网（VLAN、IEEE 802.1q）以及网络绑定/聚合功能，使您能够为 Proxmox VE 宿主机构建复杂而灵活的虚拟网络，并充分发挥 Linux 网络堆栈的强大功能。

对于大型或多租户环境，[软件定义网络（SDN）](../12-pvesdn/README.md)堆栈提供基于区域的网络隔离，并支持 VXLAN 和 EVPN 等协议。SDN 已完全集成到 Web 界面中，并默认安装。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
