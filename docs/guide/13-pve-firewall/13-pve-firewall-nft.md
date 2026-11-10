# 13.13. nftables <a href="#pve_firewall_nft" id="pve_firewall_nft"></a>

作为 `pve-firewall` 的替代，我们提供 `proxmox-firewall`，它是 Proxmox VE 防火墙的一种实现，基于较新的 [nftables](https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F) 而非 iptables。

{% hint style="warning" %}
`proxmox-firewall` 目前处于技术预览阶段。可能存在错误或与原有防火墙不兼容的情况。目前不适用于生产环境。
{% endhint %}

此实现使用相同的配置文件和配置格式，因此切换时可以使用旧配置。它提供完全相同的功能，但有以下例外：

- 使用 Linux 网桥时，不会创建额外的防火墙网桥（fwbrX）。使用 OVS 网桥的客户机接口仍会有防火墙网桥。
- 目前无法对客户机流量使用 REJECT（流量将被丢弃）。
- 使用 `NDP`、`Router Advertisement` 或 `DHCP` 选项将 **始终** 创建防火墙规则，无论默认策略如何。
- 即使连接存在 conntrack 表条目，也会评估客户机防火墙规则。

## 13.13.1. 安装与使用 <a href="#installation_and_usage" id="installation_and_usage"></a>

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

也可以检查生成的规则集。更多信息请参阅 [实用命令](#pve_firewall_nft_helpful_commands) 一节。还应检查 `pve-firewall` 是否已停止生成 iptables 规则，相关命令可在 [服务与命令](07-pve-firewall-services-commands.md) 一节中找到。

只需将配置值重新设为 0 / No，即可切换回旧防火墙。

## 13.13.2. 使用 <a href="#usage" id="usage"></a>

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

## 13.13.3. 实用命令 <a href="#pve_firewall_nft_helpful_commands" id="pve_firewall_nft_helpful_commands"></a>

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

为调试防火墙规则，跟踪数据包经过不同链的流程可能很有帮助。为要跟踪的数据包将 `nftrace` 设为 1 即可实现。建议不要为 **所有** 数据包设置此标志，以下示例仅检查 ICMP 数据包。

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
请注意，这可能生成 **大量** 无用日志，并显著降低网络协议栈的性能。
{% endhint %}

可以运行以下命令移除跟踪规则：

```text
nft delete table bridge tracebridge
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
