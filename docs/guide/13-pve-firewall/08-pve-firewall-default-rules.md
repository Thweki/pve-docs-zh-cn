# 13.8. 默认防火墙规则 <a href="#pve_firewall_default_rules" id="pve_firewall_default_rules"></a>

默认防火墙配置会过滤以下流量：

## 13.8.1. 数据中心传入/传出 DROP/REJECT <a href="#datacenter_incoming_outgoing_drop_reject" id="datacenter_incoming_outgoing_drop_reject"></a>

如果防火墙的传入或传出策略设为 DROP 或 REJECT，仍会为集群中所有 Proxmox VE 宿主机允许以下流量：

- 通过回环接口的流量
- 已建立的连接
- 使用 IGMP 协议的流量
- 从管理主机到端口 8006 的 TCP 流量，以允许访问 Web 界面
- 从管理主机到端口范围 5900 至 5999 的 TCP 流量，以允许 VNC Web 控制台流量
- 从管理主机到端口 3128 的 TCP 流量，用于连接 SPICE 代理
- 从管理主机到端口 22 的 TCP 流量，以允许 ssh 访问
- 从管理主机到端口范围 60000 至 60050 的 TCP 流量，以允许迁移流量
- 集群网络中到端口 5405-5412 的 UDP 流量，用于 corosync
- 集群网络中的 UDP 组播流量
- 类型为 3（目标不可达）、4（拥塞控制）或 11（超时）的 ICMP 流量

以下流量会被丢弃，但即使启用了日志记录也不会被记录：

- 连接状态无效的 TCP 连接
- 与 corosync 无关的广播、组播和任播流量，即未通过端口 5405-5412 的流量
- 到端口 43 的 TCP 流量
- 到端口 135 和 445 的 UDP 流量
- 到端口范围 137 至 139 的 UDP 流量
- 从源端口 137 到端口范围 1024 至 65535 的 UDP 流量
- 到端口 1900 的 UDP 流量
- 到端口 135、139 和 445 的 TCP 流量
- 源自源端口 53 的 UDP 流量

其余流量分别被丢弃或拒绝，并记录日志。具体行为可能因 **防火墙** → **选项** 中启用的附加选项而异，例如 NDP、SMURFS 和 TCP 标志过滤。

<a id="pve_firewall_iptables_inspect"></a>



请检查以下命令的输出：

```text
 # iptables-save
```

系统命令，以查看系统中生效的防火墙链和规则。此输出也包含在 `System Report` 中，可通过 Web GUI 中节点的订阅选项卡或 `pvereport` 命令行工具访问。

## 13.8.2. 虚拟机/容器传入/传出 DROP/REJECT <a href="#vm_ct_incoming_outgoing_drop_reject" id="vm_ct_incoming_outgoing_drop_reject"></a>

这会丢弃或拒绝发往虚拟机的所有流量，但根据设置的配置，对 DHCP、NDP、路由器通告、MAC 和 IP 过滤存在一些例外。丢弃/拒绝数据包的规则继承自数据中心，而宿主机所接受的传入/传出流量的例外不适用。

同样，可以使用 [iptables-save（见上文）](#datacenter_incoming_outgoing_drop_reject) 检查应用的所有规则和链。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
