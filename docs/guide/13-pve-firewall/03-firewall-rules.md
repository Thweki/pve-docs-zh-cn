# 13.3. 防火墙规则 <a href="#firewall_rules" id="firewall_rules"></a>

防火墙规则由方向（`IN`、`OUT` 或 `FORWARD`）和操作（`ACCEPT`、`DENY`、`REJECT`）组成。也可以指定宏名称。宏包含预定义的规则和选项集合。可以在规则前添加 `|` 来禁用规则。

**防火墙规则语法**

```text
[RULES]

DIRECTION ACTION [OPTIONS]
|DIRECTION ACTION [OPTIONS] # disabled rule

DIRECTION MACRO(ACTION) [OPTIONS] # use predefined macro
```

以下选项可用于细化规则匹配。

**`--dest` `<string>`**

限制数据包目标地址。可以引用单个 IP 地址、IP 集合（*\+ipsetname*）或 IP 别名定义。也可以指定地址范围，例如 *20.34.101.207-201.3.9.99*，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混合 IPv4 和 IPv6 地址。

**`--dport` `<string>`**

限制 TCP/UDP 目标端口。可以使用服务名称或普通数字（0-65535），如 */etc/services* 中所定义。端口范围可以使用 *\\d\+:\\d\+* 指定，例如 *80:85*，也可以使用逗号分隔的列表匹配多个端口或范围。

**`--icmp-type` `<string>`**

指定 icmp-type。仅当 proto 等于 *icmp* 或 *icmpv6*/*ipv6-icmp* 时有效。

**`--iface` `<string>`**

网络接口名称。对于虚拟机和容器，必须使用网络配置键名称（*net\\d\+*）。宿主机相关规则可以使用任意字符串。

**`--log` `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

防火墙规则的日志级别。

**`--proto` `<string>`**

IP 协议。可以使用协议名称（*tcp*/*udp*）或普通数字，如 */etc/protocols* 中所定义。

**`--source` `<string>`**

限制数据包源地址。可以引用单个 IP 地址、IP 集合（*\+ipsetname*）或 IP 别名定义。也可以指定地址范围，例如 *20.34.101.207-201.3.9.99*，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混合 IPv4 和 IPv6 地址。

**`--sport` `<string>`**

限制 TCP/UDP 源端口。可以使用服务名称或普通数字（0-65535），如 */etc/services* 中所定义。端口范围可以使用 *\\d\+:\\d\+* 指定，例如 *80:85*，也可以使用逗号分隔的列表匹配多个端口或范围。

以下是一些示例：

```text
[RULES]
IN SSH(ACCEPT) -i net0
IN SSH(ACCEPT) -i net0 # a comment
IN SSH(ACCEPT) -i net0 -source 192.168.2.192 # only allow SSH from 192.168.2.192
IN SSH(ACCEPT) -i net0 -source 10.0.0.1-10.0.0.10 # accept SSH for IP range
IN SSH(ACCEPT) -i net0 -source 10.0.0.1,10.0.0.2,10.0.0.3 #accept ssh for IP list
IN SSH(ACCEPT) -i net0 -source +mynetgroup # accept ssh for ipset mynetgroup
IN SSH(ACCEPT) -i net0 -source myserveralias #accept ssh for alias myserveralias

|IN SSH(ACCEPT) -i net0 # disabled rule

IN  DROP # drop all incoming packages
OUT ACCEPT # accept all outgoing packages
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
