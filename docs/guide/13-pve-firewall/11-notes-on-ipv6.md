# 13.11. 关于 IPv6 的说明 <a href="#notes_on_ipv6" id="notes_on_ipv6"></a>

防火墙包含一些 IPv6 特定选项。需要注意，IPv6 不再使用 ARP 协议，而是使用 NDP（邻居发现协议）。NDP 在 IP 层工作，因此需要 IP 地址才能成功。为此，使用从接口 MAC 地址推导的链路本地地址。默认情况下，在宿主机和虚拟机级别均启用 `NDP` 选项，以允许发送和接收邻居发现（NDP）数据包。

除邻居发现外，NDP 还用于其他一些功能，例如自动配置和通告路由器。

默认允许虚拟机发送路由器请求消息（以查询路由器）并接收路由器通告数据包。这允许它们使用无状态自动配置。另一方面，除非设置“允许路由器通告”（`radv: 1`）选项，否则虚拟机不能将自身通告为路由器。

对于 NDP 所需的链路本地地址，还可以启用“IP 过滤器”（`ipfilter: 1`）选项，其效果等同于为虚拟机的每个网络接口添加一个 `ipfilter-net*` ipset，其中包含相应的链路本地地址。（详情参见 [标准 IP 集合 `ipfilter-net*`](06-pve-firewall-ip-sets.md#pve_firewall_ipfilter_section) 一节。）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
