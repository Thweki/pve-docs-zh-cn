# pve-firewall(8)

## 名称 <a href="#chapter_pve_firewall" id="chapter_pve_firewall"></a>

pve-firewall \- PVE 防火墙守护进程

## 概要 <a href="#synopsis" id="synopsis"></a>

### <strong>pve-firewall</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pve-firewall" id="cli_pve-firewall"></a>

### <strong>pve-firewall compile</strong> <a href="#cli_pve-firewall_compile" id="cli_pve-firewall_compile"></a>

编译并打印防火墙规则。这对测试很有用。

### <strong>pve-firewall help</strong> `[OPTIONS]` <a href="#cli_pve-firewall_help" id="cli_pve-firewall_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pve-firewall localnet</strong> <a href="#cli_pve-firewall_localnet" id="cli_pve-firewall_localnet"></a>

打印本地网络信息。

### <strong>pve-firewall restart</strong> <a href="#cli_pve-firewall_restart" id="cli_pve-firewall_restart"></a>

重启 Proxmox VE 防火墙服务。

### <strong>pve-firewall simulate</strong> `[OPTIONS]` <a href="#cli_pve-firewall_simulate" id="cli_pve-firewall_simulate"></a>

模拟防火墙规则。此操作不模拟内核<em>路由</em>表，而是简单假定可以从源区域路由到目标区域。

**`--dest` `<string>`**

目标 IP 地址。

**`--dport` `<integer>`**

目标端口。

**`--from` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` （<em>默认值 \=</em> `outside`）**

源区域。

**`--protocol` `(tcp|udp)` （<em>默认值 \=</em> `tcp`）**

协议。

**`--source` `<string>`**

源 IP 地址。

**`--sport` `<integer>`**

源端口。

**`--to` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` （<em>默认值 \=</em> `host`）**

目标区域。

**`--verbose` `<boolean>`（<em>默认值 \=</em> `0`）**

详细输出。

### <strong>pve-firewall start</strong> `[OPTIONS]` <a href="#cli_pve-firewall_start" id="cli_pve-firewall_start"></a>

启动 Proxmox VE 防火墙服务。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pve-firewall status</strong> <a href="#cli_pve-firewall_status" id="cli_pve-firewall_status"></a>

获取防火墙状态。

### <strong>pve-firewall stop</strong> <a href="#cli_pve-firewall_stop" id="cli_pve-firewall_stop"></a>

停止 Proxmox VE 防火墙服务。注意，停止操作会主动移除所有与 Proxmox VE 相关的 iptable 规则，可能使宿主机失去保护。

## 描述 <a href="#description" id="description"></a>

Proxmox VE 防火墙提供了一种简单的方法来保护您的 IT 基础设施。可以为集群内的所有宿主机设置防火墙规则，或为虚拟机和容器定义规则。防火墙宏、安全组、IP 集合和别名等功能有助于简化此任务。

所有配置都存储在集群文件系统中，而基于 `iptables` 的防火墙服务在每个集群节点上运行，因此可在虚拟机之间提供完全隔离。此系统的分布式特性还提供了远高于集中式防火墙方案的带宽。

防火墙完全支持 IPv4 和 IPv6。IPv6 支持完全透明，默认会对两种协议的流量进行过滤。因此无需为 IPv6 维护另一套规则。

## 方向与区域 <a href="#directions_amp_zones" id="directions_amp_zones"></a>

Proxmox VE 防火墙将网络分成多个逻辑区域。可以独立为每个区域定义规则。根据区域不同，可以为传入、传出或转发流量定义规则。

### 方向 <a href="#directions" id="directions"></a>

为区域定义规则时，有 3 种方向可选：

**传入**

到达区域的流量。

**传出**

离开区域的流量。

**转发**

经过区域的流量。在宿主机区域中，这可以是路由流量（宿主机充当网关或执行 NAT 时）。在 VNet 级别，这会影响经过 VNet 的所有流量，包括往返于桥接网络接口的流量。

{% hint style="warning" %}
目前只有使用新的[基于 nftables 的 proxmox-firewall](#pve_firewall_nft)，才能为转发流量创建规则。标准的 `pve-firewall` 会忽略所有转发规则，这些规则不会产生任何效果！
{% endhint %}

### 区域 <a href="#zones" id="zones"></a>

可以为 3 种不同区域定义防火墙规则：

**宿主机**

往返于宿主机的流量，或由宿主机转发的流量。可以在数据中心级别或宿主机级别为此区域定义规则。宿主机级别规则优先于数据中心级别规则。

**虚拟机**

往返于虚拟机或容器的流量。不能为转发流量定义规则，只能为传入/传出流量定义规则。

**VNet**

经过 SDN VNet 的流量，可以是客户机之间，或宿主机与客户机之间的双向流量。由于这些流量始终是转发流量，因此只能创建方向为转发的规则。

{% hint style="warning" %}
目前只有使用新的[基于 nftables 的 proxmox-firewall](#pve_firewall_nft)，才能创建 VNet 级别的规则。标准的 `pve-firewall` 会忽略所有 VNet 级别的规则，这些规则不会产生任何效果！
{% endhint %}

## 配置文件 <a href="#configuration_files" id="configuration_files"></a>

所有与防火墙相关的配置都存储在 proxmox 集群文件系统中。因此这些文件会自动分发到所有集群节点，更改时 `pve-firewall` 服务会自动更新底层 `iptables` 规则。

可以使用 GUI 配置所有内容（例如 <strong>数据中心</strong> → <strong>防火墙</strong>，或 <strong>节点</strong> → <strong>防火墙</strong>），也可以使用惯用编辑器直接编辑配置文件。

防火墙配置文件包含由键值对组成的节。以 `#` 开头的行和空行被视为注释。节以标题行开始，其中节名称用 `[` 和 `]` 括起。

### 集群范围的设置 <a href="#pve_firewall_cluster_wide_setup" id="pve_firewall_cluster_wide_setup"></a>

集群范围的防火墙配置存储在：

```text
/etc/pve/firewall/cluster.fw
```

配置可包含以下节：

**`[OPTIONS]`**

用于设置集群范围的防火墙选项。

**`ebtables`：`<boolean>`（<em>默认值 \=</em> `1`）**

在整个集群中启用 ebtables 规则。

**`enable`：`<integer> (0 - N)`（<em>默认值 \=</em> `0`）**

在整个集群中启用或禁用防火墙。

**`log_ratelimit`: `[enable=]<1|0> [,burst=<integer>] [,rate=<rate>]`**

日志速率限制设置

**`burst`\=`<integer> (0 - N)`（<em>默认值 \=</em> `5`）**

应用速率限制之前始终记录的初始突发数据包数量

**`enable`\=`<boolean>`（<em>默认值 \=</em> `1`）**

启用或禁用日志速率限制

**`rate`\=`<rate>`（<em>默认值 \=</em> `1/second`）**

突发令牌桶的补充频率

**`policy_forward`: `<ACCEPT | DROP>`**

转发策略。

**`policy_in`: `<ACCEPT | DROP | REJECT>`**

传入策略。

**`policy_out`: `<ACCEPT | DROP | REJECT>`**

传出策略。

**`[RULES]`**

本节包含适用于所有节点的集群范围防火墙规则。

**`[IPSET <name>]`**

集群范围的 IP 集合定义。

**`[GROUP <name>]`**

集群范围的安全组定义。

**`[ALIASES]`**

集群范围的别名定义。

#### 启用防火墙 <a href="#enabling_the_firewall" id="enabling_the_firewall"></a>

默认情况下防火墙完全禁用，因此需要在此设置 enable 选项：

```text
[OPTIONS]
# enable firewall (cluster-wide setting, default is disabled)
enable: 1
```

{% hint style="warning" %}
启用防火墙后，默认会阻止发往所有宿主机的流量，但对从本地网络发往 WebUI、SSH 和其他重要服务的流量有一些例外。默认防火墙规则的完整列表参见 xref:pve\_firewall\_default\_rules。
{% endhint %}

如果还运行了其他通过网络通信的服务，需要单独允许这些服务。某些常见服务已有可用的 `macros`。

如果希望远程管理 Proxmox VE 宿主机，需要创建规则，允许从这些远程 IP 发往 Web GUI（端口 8006）的流量。您可能还希望允许 ssh（端口 22），以及 SPICE（端口 3128）。

{% hint style="success" %}
启用防火墙之前，请先与其中一台 Proxmox VE 宿主机建立 SSH 连接。这样，即使出现问题，仍可访问宿主机。
{% endhint %}

为简化此任务，可以改为创建名为“management”的 IPSet，并将所有远程 IP 添加到其中。这将创建从远程访问 GUI 所需的所有防火墙规则。

### 宿主机特定配置 <a href="#pve_firewall_host_specific_configuration" id="pve_firewall_host_specific_configuration"></a>

宿主机相关配置从以下位置读取：

```text
/etc/pve/nodes/<nodename>/host.fw
```

如果希望覆盖 `cluster.fw` 配置中的规则，此功能很有用。还可以增加日志详细程度，并设置 netfilter 相关选项。配置可包含以下节：

**`[OPTIONS]`**

用于设置宿主机相关的防火墙选项。

**`enable`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用宿主机防火墙规则。

**`log_level_forward`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

转发流量的日志级别。

**`log_level_in`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传入流量的日志级别。

**`log_level_out`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传出流量的日志级别。

**`log_nf_conntrack`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用 conntrack 信息日志记录。

**`ndp`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用 NDP（邻居发现协议）。

**`nf_conntrack_allow_invalid`：`<boolean>`（<em>默认值 \=</em> `0`）**

在连接跟踪中允许无效数据包。

**`nf_conntrack_helpers`：`<string>`（<em>默认值 \=</em> \`\`）**

为特定协议启用 conntrack 辅助模块。支持的协议：amanda、ftp、irc、netbios-ns、pptp、sane、sip、snmp、tftp

**`nf_conntrack_max`：`<integer> (32768 - N)`（<em>默认值 \=</em> `262144`）**

跟踪连接的最大数量。

**`nf_conntrack_tcp_timeout_established`：`<integer> (7875 - N)`（<em>默认值 \=</em> `432000`）**

Conntrack 已建立连接的超时。

**`nf_conntrack_tcp_timeout_syn_recv`：`<integer> (30 - 60)`（<em>默认值 \=</em> `60`）**

Conntrack syn recv 超时。

**`nftables`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用基于 nftables 的防火墙（技术预览）

**`nosmurfs`: `<boolean>`**

启用 SMURFS 过滤器。

**`protection_synflood`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用 SYN 洪泛防护

**`protection_synflood_burst`：`<integer>`（<em>默认值 \=</em> `1000`）**

按源 IP 设置 SYN 洪泛防护的突发速率。

**`protection_synflood_rate`：`<integer>`（<em>默认值 \=</em> `200`）**

按源 IP 设置 SYN 洪泛防护速率，单位为 syn/sec。

**`smurf_log_level`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

SMURFS 过滤器的日志级别。

**`tcp_flags_log_level`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

非法 TCP 标志过滤器的日志级别。

**`tcpflags`：`<boolean>`（<em>默认值 \=</em> `0`）**

过滤非法的 TCP 标志组合。

**`[RULES]`**

本节包含宿主机特定的防火墙规则。

### 虚拟机/容器配置 <a href="#pve_firewall_vm_container_configuration" id="pve_firewall_vm_container_configuration"></a>

虚拟机防火墙配置从以下位置读取：

```text
/etc/pve/firewall/<VMID>.fw
```

并包含以下数据：

**`[OPTIONS]`**

用于设置虚拟机/容器相关的防火墙选项。

**`dhcp`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用 DHCP。

**`enable`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用/禁用防火墙规则。

**`ipfilter`: `<boolean>`**

启用默认 IP 过滤器。这等同于为每个接口添加一个空的 ipfilter-net\<id\> ipset。此类 ipset 隐含合理的默认限制，例如将 IPv6 链路本地地址限制为从接口 MAC 地址推导的地址。对于容器，将隐式添加已配置的 IP 地址。

**`log_level_in`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传入流量的日志级别。

**`log_level_out`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传出流量的日志级别。

**`macfilter`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用/禁用 MAC 地址过滤器。

**`ndp`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用 NDP（邻居发现协议）。

**`policy_in`: `<ACCEPT | DROP | REJECT>`**

传入策略。

**`policy_out`: `<ACCEPT | DROP | REJECT>`**

传出策略。

**`radv`: `<boolean>`**

允许发送路由器通告。

**`[RULES]`**

本节包含虚拟机/容器防火墙规则。

**`[IPSET <name>]`**

IP 集合定义。

**`[ALIASES]`**

IP 别名定义。

#### 为虚拟机和容器启用防火墙 <a href="#enabling_the_firewall_for_vms_and_containers" id="enabling_the_firewall_for_vms_and_containers"></a>

每个虚拟网络设备都有自己的防火墙启用标志。因此可以选择性地为每个接口启用防火墙。除全局防火墙 `enable` 选项外，还必须启用此标志。

### VNet 配置 <a href="#pve_firewall_vnet_configuration" id="pve_firewall_vnet_configuration"></a>

VNet 相关配置从以下位置读取：

```text
/etc/pve/sdn/firewall/<vnet_name>.fw
```

这可用于在 VNet 级别全局设置防火墙配置，无需为 VNet 内每台虚拟机单独设置防火墙规则。由于没有传入或传出流量的概念，因此只能包含 `FORWARD` 方向的规则。这会影响从一个网桥端口到另一个端口的所有流量，包括宿主机接口。

{% hint style="warning" %}
此功能目前仅适用于新的[基于 nftables 的 proxmox-firewall](#pve_firewall_nft)
{% endhint %}

由于经过 `FORWARD` 链的流量是双向的，如果希望流量双向通过，就需要为两个方向创建规则。例如，如果应允许特定宿主机的 HTTP 流量，则需要创建以下规则：

```text
FORWARD ACCEPT -dest 10.0.0.1 -dport 80
FORWARD ACCEPT -source 10.0.0.1 -sport 80
```

**`[OPTIONS]`**

用于设置 VNet 相关的防火墙选项。

**`enable`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用/禁用防火墙规则。

**`log_level_forward`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

转发流量的日志级别。

**`policy_forward`: `<ACCEPT | DROP>`**

转发策略。

**`[RULES]`**

本节包含 VNet 特定的防火墙规则。

## 防火墙规则 <a href="#firewall_rules" id="firewall_rules"></a>

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

限制数据包目标地址。可以引用单个 IP 地址、IP 集合（<em>\+ipsetname</em>）或 IP 别名定义。也可以指定地址范围，例如 <em>20.34.101.207-201.3.9.99</em>，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混合 IPv4 和 IPv6 地址。

**`--dport` `<string>`**

限制 TCP/UDP 目标端口。可以使用服务名称或普通数字（0-65535），如 <em>/etc/services</em> 中所定义。端口范围可以使用 <em>\\d\+:\\d\+</em> 指定，例如 <em>80:85</em>，也可以使用逗号分隔的列表匹配多个端口或范围。

**`--icmp-type` `<string>`**

指定 icmp-type。仅当 proto 等于 <em>icmp</em> 或 <em>icmpv6</em>/<em>ipv6-icmp</em> 时有效。

**`--iface` `<string>`**

网络接口名称。对于虚拟机和容器，必须使用网络配置键名称（<em>net\\d\+</em>）。宿主机相关规则可以使用任意字符串。

**`--log` `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

防火墙规则的日志级别。

**`--proto` `<string>`**

IP 协议。可以使用协议名称（<em>tcp</em>/<em>udp</em>）或普通数字，如 <em>/etc/protocols</em> 中所定义。

**`--source` `<string>`**

限制数据包源地址。可以引用单个 IP 地址、IP 集合（<em>\+ipsetname</em>）或 IP 别名定义。也可以指定地址范围，例如 <em>20.34.101.207-201.3.9.99</em>，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混合 IPv4 和 IPv6 地址。

**`--sport` `<string>`**

限制 TCP/UDP 源端口。可以使用服务名称或普通数字（0-65535），如 <em>/etc/services</em> 中所定义。端口范围可以使用 <em>\\d\+:\\d\+</em> 指定，例如 <em>80:85</em>，也可以使用逗号分隔的列表匹配多个端口或范围。

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

## 安全组 <a href="#pve_firewall_security_groups" id="pve_firewall_security_groups"></a>

安全组是在集群级别定义的规则集合，可用于所有虚拟机的规则中。例如，可以定义名为“webserver”的组，包含开放 <em>http</em> 和 <em>https</em> 端口的规则。

```text
# /etc/pve/firewall/cluster.fw

[group webserver]
IN  ACCEPT -p tcp -dport 80
IN  ACCEPT -p tcp -dport 443
```

然后，可将此组添加到虚拟机的防火墙中

```text
# /etc/pve/firewall/<VMID>.fw

[RULES]
GROUP webserver
```

## IP 别名 <a href="#pve_firewall_ip_aliases" id="pve_firewall_ip_aliases"></a>

IP 别名允许将网络的 IP 地址与名称关联。随后可以在以下位置引用这些名称：

- 在 IP 集合定义中
- 在防火墙规则的 `source` 和 `dest` 属性中

### 标准 IP 别名 `local_network` <a href="#standard_ip_alias_span_class_monospaced_local_network_span" id="standard_ip_alias_span_class_monospaced_local_network_span"></a>

此别名自动定义。请使用以下命令查看分配的值：

```text
# pve-firewall localnet
local hostname: example
local IP address: 192.168.2.100
network auto detect: 192.168.0.0/20
using detected local_network: 192.168.0.0/20
```

防火墙会使用此别名自动设置规则，允许集群通信所需的全部流量（corosync、API、SSH）。

用户可以在 `cluster.fw` 别名节中覆盖这些值。如果在公共网络上使用单台宿主机，最好显式指定本地 IP 地址

```text
#  /etc/pve/firewall/cluster.fw
[ALIASES]
local_network 1.2.3.4 # use the single IP address
```

## IP 集合 <a href="#pve_firewall_ip_sets" id="pve_firewall_ip_sets"></a>

IP 集合可用于定义网络和宿主机组。可以在防火墙规则的 `source` 和 `dest` 属性中使用“\+name”引用它们。

以下示例允许来自 `management` IP 集合的 HTTP 流量。

```text
IN HTTP(ACCEPT) -source +management
```

### 标准 IP 集合 `management` <a href="#standard_ip_set_span_class_monospaced_management_span" id="standard_ip_set_span_class_monospaced_management_span"></a>

此 IP 集合仅适用于宿主机防火墙（不适用于虚拟机防火墙）。允许这些 IP 执行常规管理任务（Proxmox VE GUI、VNC、SPICE、SSH）。

本地集群网络会自动添加到此 IP 集合（别名 `cluster_network`），以启用宿主机之间的集群通信。（组播、ssh 等）

```text
# /etc/pve/firewall/cluster.fw

[IPSET management]
192.168.2.10
192.168.2.10/24
```

### 标准 IP 集合 `blacklist` <a href="#standard_ip_set_span_class_monospaced_blacklist_span" id="standard_ip_set_span_class_monospaced_blacklist_span"></a>

来自这些 IP 的流量会被每台宿主机和虚拟机的防火墙丢弃。

```text
# /etc/pve/firewall/cluster.fw

[IPSET blacklist]
77.240.159.182
213.87.123.0/24
```

### 标准 IP 集合 `ipfilter-net*` <a href="#pve_firewall_ipfilter_section" id="pve_firewall_ipfilter_section"></a>

这些过滤器属于虚拟机的网络接口，主要用于防止 IP 欺骗。如果某接口存在此类集合，则任何源 IP 不匹配其接口对应 ipfilter 集合的传出流量都会被丢弃。

对于已配置 IP 地址的容器，如果这些集合存在（或通过全局 `IP Filter` 选项，在虚拟机防火墙的 <strong>选项</strong> 选项卡中激活），则会隐式包含关联的 IP 地址。

对于虚拟机和容器，它们还会隐式包含由 MAC 推导的标准 IPv6 链路本地地址，以便邻居发现协议能够工作。

```text
/etc/pve/firewall/<VMID>.fw

[IPSET ipfilter-net0] # only allow specified IPs on net0
192.168.2.10
```

## 服务和命令 <a href="#pve_firewall_services_commands" id="pve_firewall_services_commands"></a>

防火墙在每个节点上运行两个服务守护进程：

- pvefw-logger：NFLOG 守护进程（ulogd 的替代品）。
- pve-firewall：更新 iptables 规则

还有一个名为 `pve-firewall` 的 CLI 命令，可用于启动和停止防火墙服务：

```text
# pve-firewall start
# pve-firewall stop
```

要获取状态，请使用：

```text
# pve-firewall status
```

上述命令会读取并编译所有防火墙规则，因此如果防火墙配置包含任何错误，您将看到警告。

如果希望查看生成的 iptables 规则，可以使用：

```text
# iptables-save
```

## 默认防火墙规则 <a href="#pve_firewall_default_rules" id="pve_firewall_default_rules"></a>

默认防火墙配置会过滤以下流量：

### 数据中心入站/出站 DROP/REJECT <a href="#datacenter_incoming_outgoing_drop_reject" id="datacenter_incoming_outgoing_drop_reject"></a>

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

其余流量分别被丢弃或拒绝，并记录日志。具体行为可能因 <strong>防火墙</strong> → <strong>选项</strong> 中启用的附加选项而异，例如 NDP、SMURFS 和 TCP 标志过滤。

<a id="pve_firewall_iptables_inspect"></a>



请检查以下命令的输出：

```text
 # iptables-save
```

系统命令，以查看系统中生效的防火墙链和规则。此输出也包含在 `System Report` 中，可通过 Web GUI 中节点的订阅选项卡或 `pvereport` 命令行工具访问。

### VM/CT 入站/出站 DROP/REJECT <a href="#vm_ct_incoming_outgoing_drop_reject" id="vm_ct_incoming_outgoing_drop_reject"></a>

这会丢弃或拒绝发往虚拟机的所有流量，但根据设置的配置，对 DHCP、NDP、路由器通告、MAC 和 IP 过滤存在一些例外。丢弃/拒绝数据包的规则继承自数据中心，而宿主机所接受的传入/传出流量的例外不适用。

同样，可以使用 [iptables-save（见上文）](#datacenter_incoming_outgoing_drop_reject) 查看所有已应用的规则和链。

## 防火墙规则日志记录 <a href="#logging_of_firewall_rules" id="logging_of_firewall_rules"></a>

默认情况下，防火墙规则过滤流量的所有日志记录均已禁用。要启用日志记录，必须设置入站和/或出站流量的 `loglevel`，其位置为<strong>防火墙</strong> → <strong>选项</strong>。可以分别为宿主机以及虚拟机/容器防火墙设置。这样会启用 Proxmox VE 标准防火墙规则的日志记录，并可在<strong>防火墙</strong> → <strong>日志</strong>中查看输出。此外，标准规则只会记录部分被丢弃或拒绝的数据包（参见[默认防火墙规则](#pve_firewall_default_rules)）。

`loglevel` 不影响记录多少被过滤的流量。它会更改作为前缀附加到日志输出的 `LOGID`，以便过滤和后续处理。

`loglevel` 是以下标志之一：

<table id="pve_firewall_log_levels">


<thead>
<tr>
<th>loglevel</th>
<th>LOGID</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>nolog</p></td>
<td><p> — </p></td>
</tr>
<tr>
<td><p>emerg</p></td>
<td><p>0</p></td>
</tr>
<tr>
<td><p>alert</p></td>
<td><p>1</p></td>
</tr>
<tr>
<td><p>crit</p></td>
<td><p>2</p></td>
</tr>
<tr>
<td><p>err</p></td>
<td><p>3</p></td>
</tr>
<tr>
<td><p>warning</p></td>
<td><p>4</p></td>
</tr>
<tr>
<td><p>notice</p></td>
<td><p>5</p></td>
</tr>
<tr>
<td><p>info</p></td>
<td><p>6</p></td>
</tr>
<tr>
<td><p>debug</p></td>
<td><p>7</p></td>
</tr>
</tbody>
</table>

典型的防火墙日志输出如下所示：

```text
VMID LOGID CHAIN TIMESTAMP POLICY: PACKET_DETAILS
```

对于宿主机防火墙，`VMID` 等于 0。

### 用户定义防火墙规则的日志记录 <a href="#logging_of_user_defined_firewall_rules" id="logging_of_user_defined_firewall_rules"></a>

要记录被用户定义防火墙规则过滤的数据包，可以为每条规则单独设置 log-level 参数。这支持精细的日志记录，并且独立于在 <strong>防火墙</strong> → <strong>选项</strong> 中为标准规则定义的日志级别。

每条规则的 `loglevel` 可以在创建或修改规则时通过 Web UI 轻松定义或更改，也可以通过相应的 `pvesh` API 调用设置。

此外，还可以通过防火墙配置文件设置日志级别，方法是在选定规则后附加 `-log <loglevel>`（参见[可用的日志级别](#logging_of_firewall_rules)）。

例如，以下两项等价：

```text
IN REJECT -p icmp -log nolog
IN REJECT -p icmp
```

而

```text
IN REJECT -p icmp -log debug
```

会生成标记为 `debug` 级别的日志输出。

## 提示与技巧 <a href="#tips_and_tricks" id="tips_and_tricks"></a>

### 如何允许 FTP <a href="#how_to_allow_ftp" id="how_to_allow_ftp"></a>

FTP 是一种旧式协议，使用端口 21 及若干其他动态端口。因此需要一条接受端口 21 的规则。此外，需要加载 `ip_conntrack_ftp` 模块。请运行：

```text
modprobe ip_conntrack_ftp
```

并将 `ip_conntrack_ftp` 添加到 `/etc/modules`（以便重启后仍然有效）。

### Suricata IPS 集成 <a href="#suricata_ips_integration" id="suricata_ips_integration"></a>

如果希望使用 [Suricata IPS](https://suricata.io/)（入侵防御系统），这是可行的。

只有防火墙 ACCEPT 的数据包才会转发到 IPS。

防火墙拒绝/丢弃的数据包不会进入 IPS。

在 proxmox 宿主机上安装 suricata：

```text
# apt-get install suricata
# modprobe nfnetlink_queue
```

不要忘记将 `nfnetlink_queue` 添加到 `/etc/modules`，以便下次重启时生效。

然后，使用以下命令为特定虚拟机启用 IPS：

```text
# /etc/pve/firewall/<VMID>.fw

[OPTIONS]
ips: 1
ips_queues: 0
```

`ips_queues` 会为此虚拟机绑定特定的 cpu 队列。

可用队列定义在

```text
# /etc/default/suricata
NFQUEUE=0
```

## 关于 IPv6 的说明 <a href="#notes_on_ipv6" id="notes_on_ipv6"></a>

防火墙包含一些 IPv6 特定选项。需要注意，IPv6 不再使用 ARP 协议，而是使用 NDP（邻居发现协议）。NDP 在 IP 层工作，因此需要 IP 地址才能成功。为此，使用从接口 MAC 地址推导的链路本地地址。默认情况下，在宿主机和虚拟机级别均启用 `NDP` 选项，以允许发送和接收邻居发现（NDP）数据包。

除邻居发现外，NDP 还用于其他一些功能，例如自动配置和通告路由器。

默认允许虚拟机发送路由器请求消息（以查询路由器）并接收路由器通告数据包。这允许它们使用无状态自动配置。另一方面，除非设置“允许路由器通告”（`radv: 1`）选项，否则虚拟机不能将自身通告为路由器。

对于 NDP 所需的链路本地地址，还可以启用“IP 过滤器”（`ipfilter: 1`）选项，其效果等同于为虚拟机的每个网络接口添加一个包含相应链路本地地址的 `ipfilter-net*` ipset。（详情请参阅[标准 IP 集合 `ipfilter-net*`](#pve_firewall_ipfilter_section)章节。）

## Proxmox VE 使用的端口 <a href="#ports_used_by_proxmox_ve" id="ports_used_by_proxmox_ve"></a>

- Web 界面：8006（TCP，基于 TLS 的 HTTP/1.1）
- VNC Web 控制台：5900-5999（TCP，WebSocket）
- SPICE 代理：3128（TCP）
- sshd（用于集群操作）：22（TCP）
- rpcbind：111（UDP）
- sendmail：25（TCP，传出）
- corosync 集群流量：5405-5412 UDP
- 在线迁移（虚拟机内存和本地磁盘数据）：60000-60050（TCP）

## nftables <a href="#pve_firewall_nft" id="pve_firewall_nft"></a>

作为 `pve-firewall` 的替代，我们提供 `proxmox-firewall`，它是 Proxmox VE 防火墙的一种实现，基于较新的 [nftables](https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F) 而非 iptables。

{% hint style="warning" %}
`proxmox-firewall` 目前处于技术预览阶段。可能存在错误或与原有防火墙不兼容的情况。目前不适用于生产环境。
{% endhint %}

此实现使用相同的配置文件和配置格式，因此切换时可以使用旧配置。它提供完全相同的功能，但有以下例外：

- 使用 Linux 网桥时，不会创建额外的防火墙网桥（fwbrX）。使用 OVS 网桥的客户机接口仍会有防火墙网桥。
- 目前无法对客户机流量使用 REJECT（流量将被丢弃）。
- 使用 `NDP`、`Router Advertisement` 或 `DHCP` 选项将 <strong>始终</strong> 创建防火墙规则，无论默认策略如何。
- 即使连接存在 conntrack 表条目，也会评估客户机防火墙规则。

### 安装与使用 <a href="#installation_and_usage" id="installation_and_usage"></a>

安装 `proxmox-firewall` 软件包：

```text
apt install proxmox-firewall
```

通过宿主机上的 Web UI（宿主机 \> 防火墙 \> 选项 \> nftables）启用 nftables 后端，或在宿主机配置文件（`/etc/pve/nodes/<node_name>/host.fw`）中启用：

```text
[OPTIONS]

nftables: 1
```

{% hint style="info" %}
启用/禁用 `proxmox-firewall` 后，需要重启所有正在运行的虚拟机和容器，旧/新防火墙才能正常工作。
{% endhint %}

设置 `nftables` 配置键后，新的 `proxmox-firewall` 服务将接管。可以通过检查 `proxmox-firewall` 的 systemctl 状态来确认新服务是否工作：

```text
systemctl status proxmox-firewall
```

也可以检查生成的规则集。更多相关信息请参阅[实用命令](#pve_firewall_nft_helpful_commands)章节。还应检查 `pve-firewall` 是否不再生成 iptables 规则，相关命令请参阅[服务和命令](#pve_firewall_services_commands)章节。

只需将配置值重新设为 0 / No，即可切换回旧防火墙。

### 使用 <a href="#usage" id="usage"></a>

`proxmox-firewall` 将创建两个由 `proxmox-firewall` 服务管理的表：`proxmox-firewall` 和 `proxmox-firewall-guests`。如果希望创建位于 Proxmox VE 防火墙配置之外的自定义规则，可以创建自己的表来管理自定义防火墙规则。`proxmox-firewall` 只会操作自身生成的表，因此可以通过添加自己的表，轻松扩展和修改 `proxmox-firewall` 的行为。

基于 nftables 的防火墙不使用 `pve-firewall` 命令，而是使用 `proxmox-firewall`。它是一个 systemd 服务，因此可以通过 `systemctl` 启动和停止：

```text
systemctl start proxmox-firewall
systemctl stop proxmox-firewall
```

停止防火墙服务会移除所有生成的规则。

要查询防火墙状态，可以查询 systemctl 服务的状态：

```text
systemctl status proxmox-firewall
```

### 实用命令 <a href="#pve_firewall_nft_helpful_commands" id="pve_firewall_nft_helpful_commands"></a>

可以通过以下命令检查生成的规则集：

```text
nft list ruleset
```

如果要调试 `proxmox-firewall`，可以通过 `compile` 子命令转储防火墙生成的命令。此外，设置 PVE\_LOG 环境变量会将日志输出打印到 STDERR，这有助于调试生成 nftables 规则集时出现的问题：

```text
PVE_LOG=trace /usr/libexec/proxmox/proxmox-firewall compile > firewall.json
```

nftables 规则集由包含在 proxmox-firewall 二进制程序中的骨架规则集，以及从防火墙配置生成的规则组成。可以通过 `skeleton` 子命令获取基础规则集：

```text
/usr/libexec/proxmox/proxmox-firewall skeleton
```

这两个命令的输出都可以直接通过管道传给 `nft` 可执行文件。以下命令将从头重新创建整个 nftables 规则集：

```text
/usr/libexec/proxmox/proxmox-firewall skeleton | nft -f -
/usr/libexec/proxmox/proxmox-firewall compile | nft -j -f -
```

如果希望在防火墙守护进程运行时获得详细输出，也可以编辑 systemctl 服务：

```text
systemctl edit proxmox-firewall
```

然后需要为 `PVE_LOG` 环境变量添加覆盖设置：

```text
[Service]
Environment="PVE_LOG=trace"
```

这会在很短时间内生成大量日志，因此仅用于调试目的。其他详细程度较低的日志级别为 `info` 和 `debug`。

为调试防火墙规则，跟踪数据包经过不同链的流程可能很有帮助。为要跟踪的数据包将 `nftrace` 设为 1 即可实现。建议不要为 <strong>所有</strong> 数据包设置此标志，以下示例仅检查 ICMP 数据包。

```text
#!/usr/sbin/nft -f
table bridge tracebridge
delete table bridge tracebridge

table bridge tracebridge {
    chain trace {
        meta l4proto icmp meta nftrace set 1
    }

    chain prerouting {
        type filter hook prerouting priority -350; policy accept;
        jump trace
    }

    chain postrouting {
        type filter hook postrouting priority -350; policy accept;
        jump trace
    }
}
```

保存此文件，将其设为可执行文件，然后运行一次，即会创建相应的跟踪链。随后可通过 Proxmox VE Web UI（防火墙 \> 日志）或 `nft monitor trace` 查看跟踪输出。

上述示例跟踪所有网桥上的流量，客户机流量通常从这里经过。如果要检查宿主机流量，请在 `inet` 表中创建这些链，而不是 `bridge` 表。

{% hint style="info" %}
请注意，这可能生成 <strong>大量</strong> 无用日志，并显著降低网络协议栈的性能。
{% endhint %}

可以运行以下命令移除跟踪规则：

```text
nft delete table bridge tracebridge
```

## 宏定义 <a href="#macro_definitions" id="macro_definitions"></a>

<table>
<tr>
<td><em>Amanda</em> <br/></td>
<td>
<p>Amanda 备份</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>10080</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>10080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Auth</em> <br/></td>
<td>
<p>Auth（identd）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>113</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BGP</em> <br/></td>
<td>
<p>边界网关协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>179</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BitTorrent</em> <br/></td>
<td>
<p>BitTorrent 3.1 及更早版本的 BitTorrent 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6881:6889</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>6881</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BitTorrent32</em> <br/></td>
<td>
<p>BitTorrent 3.2 及更高版本的 BitTorrent 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6881:6999</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>6881</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>CVS</em> <br/></td>
<td>
<p>并发版本系统 pserver 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2401</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Ceph</em> <br/></td>
<td>
<p>Ceph 存储集群流量（Ceph 监视器、OSD 和 MDS 守护进程）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6789</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3300</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6800:7300</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Citrix</em> <br/></td>
<td>
<p>Citrix/ICA 流量（ICA、ICA Browser、CGP）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1494</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1604</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2598</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DAAP</em> <br/></td>
<td>
<p>数字音频访问协议流量（iTunes、Rythmbox 守护进程）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3689</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3689</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DCC</em> <br/></td>
<td>
<p>分布式校验和交换中心垃圾邮件过滤机制</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6277</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DHCPfwd</em> <br/></td>
<td>
<p>转发的 DHCP 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>67:68</p></td>
<td><p>67:68</p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DHCPv6</em> <br/></td>
<td>
<p>DHCPv6 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>546:547</p></td>
<td><p>546:547</p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DNS</em> <br/></td>
<td>
<p>域名系统流量（upd 和 tcp）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>53</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>53</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Distcc</em> <br/></td>
<td>
<p>分布式编译器服务</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3632</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>FTP</em> <br/></td>
<td>
<p>文件传输协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>21</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Finger</em> <br/></td>
<td>
<p>Finger 协议（RFC 742）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>79</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>GNUnet</em> <br/></td>
<td>
<p>GNUnet 安全点对点网络流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2086</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>2086</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1080</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>GRE</em> <br/></td>
<td>
<p>通用路由封装隧道协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>47</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Git</em> <br/></td>
<td>
<p>Git 分布式版本控制流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>9418</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HKP</em> <br/></td>
<td>
<p>OpenPGP HTTP 密钥服务器协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>11371</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HTTP</em> <br/></td>
<td>
<p>超文本传输协议（WWW）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>80</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HTTPS</em> <br/></td>
<td>
<p>通过 SSL 传输的超文本传输协议（WWW）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>443</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>ICPV2</em> <br/></td>
<td>
<p>互联网缓存协议 V2（Squid）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3130</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>ICQ</em> <br/></td>
<td>
<p>AOL Instant Messenger 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5190</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IMAP</em> <br/></td>
<td>
<p>互联网消息访问协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>143</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IMAPS</em> <br/></td>
<td>
<p>通过 SSL 传输的互联网消息访问协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>993</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPIP</em> <br/></td>
<td>
<p>IPIP 封装流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>94</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsec</em> <br/></td>
<td>
<p>IPsec 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p>500</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>50</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsecah</em> <br/></td>
<td>
<p>IPsec 认证（AH）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p>500</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>51</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsecnat</em> <br/></td>
<td>
<p>IPsec 流量和 Nat-Traversal</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>4500</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>50</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IRC</em> <br/></td>
<td>
<p>互联网中继聊天流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6667</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Jetdirect</em> <br/></td>
<td>
<p>HP Jetdirect 打印</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>9100</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>L2TP</em> <br/></td>
<td>
<p>第 2 层隧道协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1701</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>LDAP</em> <br/></td>
<td>
<p>轻量级目录访问协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>389</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>LDAPS</em> <br/></td>
<td>
<p>安全轻量级目录访问协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>636</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MDNS</em> <br/></td>
<td>
<p>多播 DNS</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5353</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MSNP</em> <br/></td>
<td>
<p>Microsoft 通知协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1863</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MSSQL</em> <br/></td>
<td>
<p>Microsoft SQL Server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1433</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Mail</em> <br/></td>
<td>
<p>邮件流量（SMTP、SMTPS、Submission）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>25</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>465</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>587</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Munin</em> <br/></td>
<td>
<p>Munin 网络资源监控流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>4949</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MySQL</em> <br/></td>
<td>
<p>MySQL 服务器</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3306</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NNTP</em> <br/></td>
<td>
<p>NNTP 流量（Usenet）。</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>119</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NNTPS</em> <br/></td>
<td>
<p>加密的 NNTP 流量（Usenet）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>563</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NTP</em> <br/></td>
<td>
<p>网络时间协议（ntpd）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>123</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NeighborDiscovery</em> <br/></td>
<td>
<p>IPv6 邻居请求、邻居通告和路由器通告</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>router-solicitation</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>router-advertisement</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>neighbor-solicitation</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>neighbor-advertisement</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>OSPF</em> <br/></td>
<td>
<p>OSPF 多播流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>89</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>OpenVPN</em> <br/></td>
<td>
<p>OpenVPN 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1194</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PCA</em> <br/></td>
<td>
<p>Symantec PCAnywere (tm)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5632</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5631</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PMG</em> <br/></td>
<td>
<p>Proxmox Mail Gateway Web 界面</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>8006</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>POP3</em> <br/></td>
<td>
<p>POP3 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>110</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>POP3S</em> <br/></td>
<td>
<p>加密的 POP3 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>995</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PPtP</em> <br/></td>
<td>
<p>点对点隧道协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>47</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1723</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Ping</em> <br/></td>
<td>
<p>ICMP 回显请求</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>icmp</p></td>
<td><p>echo-request</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PostgreSQL</em> <br/></td>
<td>
<p>PostgreSQL 服务器</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5432</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Printer</em> <br/></td>
<td>
<p>行式打印机协议打印</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>515</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RDP</em> <br/></td>
<td>
<p>Microsoft 远程桌面协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3389</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RIP</em> <br/></td>
<td>
<p>路由信息协议（双向）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>520</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RNDC</em> <br/></td>
<td>
<p>BIND 远程管理协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>953</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Razor</em> <br/></td>
<td>
<p>Razor 反垃圾邮件系统</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2703</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Rdate</em> <br/></td>
<td>
<p>远程时间获取（rdate）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>37</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Rsync</em> <br/></td>
<td>
<p>Rsync 服务器</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>873</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SANE</em> <br/></td>
<td>
<p>SANE 网络扫描</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6566</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMB</em> <br/></td>
<td>
<p>Microsoft SMB 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>135,445</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>137:139</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1024:65535</p></td>
<td><p>137</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>135,139,445</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMBswat</em> <br/></td>
<td>
<p>Samba Web 管理工具</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>901</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMTP</em> <br/></td>
<td>
<p>简单邮件传输协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>25</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMTPS</em> <br/></td>
<td>
<p>加密的简单邮件传输协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>465</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SNMP</em> <br/></td>
<td>
<p>简单网络管理协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>161:162</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>161</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SPAMD</em> <br/></td>
<td>
<p>Spam Assassin SPAMD 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>783</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SPICEproxy</em> <br/></td>
<td>
<p>Proxmox VE SPICE 显示代理流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3128</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SSH</em> <br/></td>
<td>
<p>安全 Shell 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>22</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SVN</em> <br/></td>
<td>
<p>Subversion 服务器（svnserve）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3690</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SixXS</em> <br/></td>
<td>
<p>SixXS IPv6 部署和隧道代理</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3874</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3740</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>41</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5072,8374</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Squid</em> <br/></td>
<td>
<p>Squid Web 代理流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3128</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Submission</em> <br/></td>
<td>
<p>邮件消息提交流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>587</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Syslog</em> <br/></td>
<td>
<p>Syslog 协议（RFC 5424）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>514</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>514</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>TFTP</em> <br/></td>
<td>
<p>简单文件传输协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>69</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Telnet</em> <br/></td>
<td>
<p>Telnet 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>23</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Telnets</em> <br/></td>
<td>
<p>通过 SSL 传输的 Telnet</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>992</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Time</em> <br/></td>
<td>
<p>RFC 868 时间协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>37</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Trcrt</em> <br/></td>
<td>
<p>Traceroute（最多 30 跳）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>33434:33524</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmp</p></td>
<td><p>echo-request</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>VNC</em> <br/></td>
<td>
<p>VNC 显示器 0 - 99 的 VNC 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5900:5999</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>VNCL</em> <br/></td>
<td>
<p>从 Vncservers 到处于监听模式的 Vncviewers 的 VNC 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5500</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Web</em> <br/></td>
<td>
<p>WWW 流量（HTTP 和 HTTPS）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>80</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>443</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Webcache</em> <br/></td>
<td>
<p>Web 缓存/代理流量（端口 8080）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>8080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Webmin</em> <br/></td>
<td>
<p>Webmin 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>10000</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Whois</em> <br/></td>
<td>
<p>Whois（nicname，RFC 3912）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>43</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-firewall.8.html) · 版本 9.2.13 · 非官方中文翻译。
