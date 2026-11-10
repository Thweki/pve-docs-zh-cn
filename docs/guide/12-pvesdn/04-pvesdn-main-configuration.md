# 12.4. 配置概述 <a href="#pvesdn_main_configuration" id="pvesdn_main_configuration"></a>

在数据中心级别的 Web UI 中进行配置，分为以下部分：

- SDN：在此可查看当前活动 SDN 状态的概览，并将所有待处理更改应用到整个集群。
- [区域](06-pvesdn-config-zone.md)：创建和管理虚拟隔离的网络区域
- [VNet](07-pvesdn-config-vnet.md)：创建虚拟网桥并管理子网

“选项”类别允许添加和管理 SDN 设置中使用的其他服务。

- [控制器](09-pvesdn-config-controllers.md)：用于控制复杂设置中的三层路由
- [DHCP](14-pvesdn-config-dhcp.md)：为区域定义 DHCP 服务器，自动在 IPAM 中为客户机分配 IP，并通过 DHCP 将其租给客户机。
- [IPAM](12-pvesdn-config-ipam.md)：启用客户机的外部 IP 地址管理
- [DNS](13-pvesdn-config-dns.md)：定义 DNS 服务器集成，用于注册虚拟客户机的主机名和 IP 地址

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
