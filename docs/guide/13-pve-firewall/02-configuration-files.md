# 13.2. 配置文件 <a href="#configuration_files" id="configuration_files"></a>

所有与防火墙相关的配置都存储在 proxmox 集群文件系统中。因此这些文件会自动分发到所有集群节点，更改时 `pve-firewall` 服务会自动更新底层 `iptables` 规则。

可以使用 GUI 配置所有内容（例如 **数据中心** → **防火墙**，或 **节点** → **防火墙**），也可以使用惯用编辑器直接编辑配置文件。

防火墙配置文件包含由键值对组成的节。以 `#` 开头的行和空行被视为注释。节以标题行开始，其中节名称用 `[` 和 `]` 括起。

## 13.2.1. 集群范围的设置 <a href="#pve_firewall_cluster_wide_setup" id="pve_firewall_cluster_wide_setup"></a>

集群范围的防火墙配置存储在：

```text
/etc/pve/firewall/cluster.fw
```

配置可包含以下节：

**`[OPTIONS]`**

用于设置集群范围的防火墙选项。

**`ebtables`：`<boolean>`（*默认值 \=* `1`）**

在整个集群中启用 ebtables 规则。

**`enable`：`<integer> (0 - N)`（*默认值 \=* `0`）**

在整个集群中启用或禁用防火墙。

**`log_ratelimit`: `[enable=]<1|0> [,burst=<integer>] [,rate=<rate>]`**

日志速率限制设置

**`burst`\=`<integer> (0 - N)`（*默认值 \=* `5`）**

应用速率限制之前始终记录的初始突发数据包数量

**`enable`\=`<boolean>`（*默认值 \=* `1`）**

启用或禁用日志速率限制

**`rate`\=`<rate>`（*默认值 \=* `1/second`）**

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

### 启用防火墙 <a href="#enabling_the_firewall" id="enabling_the_firewall"></a>

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

## 13.2.2. 宿主机特定配置 <a href="#pve_firewall_host_specific_configuration" id="pve_firewall_host_specific_configuration"></a>

宿主机相关配置从以下位置读取：

```text
/etc/pve/nodes/<nodename>/host.fw
```

如果希望覆盖 `cluster.fw` 配置中的规则，此功能很有用。还可以增加日志详细程度，并设置 netfilter 相关选项。配置可包含以下节：

**`[OPTIONS]`**

用于设置宿主机相关的防火墙选项。

**`enable`：`<boolean>`（*默认值 \=* `1`）**

启用宿主机防火墙规则。

**`log_level_forward`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

转发流量的日志级别。

**`log_level_in`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传入流量的日志级别。

**`log_level_out`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传出流量的日志级别。

**`log_nf_conntrack`：`<boolean>`（*默认值 \=* `0`）**

启用 conntrack 信息日志记录。

**`ndp`：`<boolean>`（*默认值 \=* `1`）**

启用 NDP（邻居发现协议）。

**`nf_conntrack_allow_invalid`：`<boolean>`（*默认值 \=* `0`）**

在连接跟踪中允许无效数据包。

**`nf_conntrack_helpers`：`<string>`（*默认值 \=* \`\`）**

为特定协议启用 conntrack 辅助模块。支持的协议：amanda、ftp、irc、netbios-ns、pptp、sane、sip、snmp、tftp

**`nf_conntrack_max`：`<integer> (32768 - N)`（*默认值 \=* `262144`）**

跟踪连接的最大数量。

**`nf_conntrack_tcp_timeout_established`：`<integer> (7875 - N)`（*默认值 \=* `432000`）**

Conntrack 已建立连接的超时。

**`nf_conntrack_tcp_timeout_syn_recv`：`<integer> (30 - 60)`（*默认值 \=* `60`）**

Conntrack syn recv 超时。

**`nftables`：`<boolean>`（*默认值 \=* `0`）**

启用基于 nftables 的防火墙（技术预览）

**`nosmurfs`: `<boolean>`**

启用 SMURFS 过滤器。

**`protection_synflood`：`<boolean>`（*默认值 \=* `0`）**

启用 SYN 洪泛防护

**`protection_synflood_burst`：`<integer>`（*默认值 \=* `1000`）**

按源 IP 设置 SYN 洪泛防护的突发速率。

**`protection_synflood_rate`：`<integer>`（*默认值 \=* `200`）**

按源 IP 设置 SYN 洪泛防护速率，单位为 syn/sec。

**`smurf_log_level`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

SMURFS 过滤器的日志级别。

**`tcp_flags_log_level`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

非法 TCP 标志过滤器的日志级别。

**`tcpflags`：`<boolean>`（*默认值 \=* `0`）**

过滤非法的 TCP 标志组合。

**`[RULES]`**

本节包含宿主机特定的防火墙规则。

## 13.2.3. 虚拟机/容器配置 <a href="#pve_firewall_vm_container_configuration" id="pve_firewall_vm_container_configuration"></a>

虚拟机防火墙配置从以下位置读取：

```text
/etc/pve/firewall/<VMID>.fw
```

并包含以下数据：

**`[OPTIONS]`**

用于设置虚拟机/容器相关的防火墙选项。

**`dhcp`：`<boolean>`（*默认值 \=* `0`）**

启用 DHCP。

**`enable`：`<boolean>`（*默认值 \=* `0`）**

启用/禁用防火墙规则。

**`ipfilter`: `<boolean>`**

启用默认 IP 过滤器。这等同于为每个接口添加一个空的 ipfilter-net\<id\> ipset。此类 ipset 隐含合理的默认限制，例如将 IPv6 链路本地地址限制为从接口 MAC 地址推导的地址。对于容器，将隐式添加已配置的 IP 地址。

**`log_level_in`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传入流量的日志级别。

**`log_level_out`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

传出流量的日志级别。

**`macfilter`：`<boolean>`（*默认值 \=* `1`）**

启用/禁用 MAC 地址过滤器。

**`ndp`：`<boolean>`（*默认值 \=* `1`）**

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

### 为虚拟机和容器启用防火墙 <a href="#enabling_the_firewall_for_vms_and_containers" id="enabling_the_firewall_for_vms_and_containers"></a>

每个虚拟网络设备都有自己的防火墙启用标志。因此可以选择性地为每个接口启用防火墙。除全局防火墙 `enable` 选项外，还必须启用此标志。

## 13.2.4. VNet 配置 <a href="#pve_firewall_vnet_configuration" id="pve_firewall_vnet_configuration"></a>

VNet 相关配置从以下位置读取：

```text
/etc/pve/sdn/firewall/<vnet_name>.fw
```

这可用于在 VNet 级别全局设置防火墙配置，无需为 VNet 内每台虚拟机单独设置防火墙规则。由于没有传入或传出流量的概念，因此只能包含 `FORWARD` 方向的规则。这会影响从一个网桥端口到另一个端口的所有流量，包括宿主机接口。

{% hint style="warning" %}
此功能目前仅适用于新的 [基于 nftables 的 proxmox-firewall](13-pve-firewall-nft.md)
{% endhint %}

由于经过 `FORWARD` 链的流量是双向的，如果希望流量双向通过，就需要为两个方向创建规则。例如，如果应允许特定宿主机的 HTTP 流量，则需要创建以下规则：

```text
FORWARD ACCEPT -dest 10.0.0.1 -dport 80
FORWARD ACCEPT -source 10.0.0.1 -sport 80
```

**`[OPTIONS]`**

用于设置 VNet 相关的防火墙选项。

**`enable`：`<boolean>`（*默认值 \=* `0`）**

启用/禁用防火墙规则。

**`log_level_forward`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

转发流量的日志级别。

**`policy_forward`: `<ACCEPT | DROP>`**

转发策略。

**`[RULES]`**

本节包含 VNet 特定的防火墙规则。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
