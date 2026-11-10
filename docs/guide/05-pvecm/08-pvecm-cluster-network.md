# 5.8. 集群网络 <a href="#pvecm_cluster_network" id="pvecm_cluster_network"></a>

集群网络是集群的核心。通过它发送的所有消息都必须按照各自的顺序可靠地传递到所有节点。在 Proxmox VE 中，这部分由 corosync 完成，它是一种高性能、低开销的高可用性开发工具包的实现。它服务于我们的去中心化配置文件系统（`pmxcfs`）。

## 5.8.1. 网络要求 <a href="#pvecm_cluster_network_requirements" id="pvecm_cluster_network_requirements"></a>

Proxmox VE 集群栈要求所有节点之间具有延迟低于 5 毫秒的可靠网络（LAN 性能），才能稳定运行。虽然在节点数量较少的配置中，延迟较高的网络*可能*也能正常工作，但这并无保证；当节点超过三个且延迟高于约 10 ms 时，能正常工作的可能性就相当低。

该网络不应被其他成员大量使用，因为虽然 corosync 不会占用太多带宽，但它对延迟抖动很敏感；理想情况下，corosync 应在物理隔离的独立网络中运行。尤其不要让 corosync 和存储共用网络（除非在[冗余](09-pvecm-redundancy.md)配置中将其作为可能的低优先级后备方案）。

在建立集群之前，检查网络是否适合此用途是一种良好做法。为确保节点能够在集群网络上相互连接，可以使用 `ping` 工具测试它们之间的连通性。

如果启用了 Proxmox VE 防火墙，将自动生成 corosync 的 ACCEPT 规则，无需手动操作。

{% hint style="info" %}
Corosync 在 3.0 版之前使用组播（该版本随 Proxmox VE 6.0 引入）。新版本依赖 [Kronosnet](https://kronosnet.org/) 进行集群通信，而目前它仅支持常规 UDP 单播。
{% endhint %}

{% hint style="danger" %}
您仍然可以通过将传输方式设置为 `udp` 或 `udpu`，在 [corosync.conf](12-corosync-configuration.md#pvecm_edit_corosync_conf) 中启用组播或传统单播，但请注意，这将禁用所有加密和冗余支持。因此不建议这样做。
{% endhint %}

## 5.8.2. 在绑定接口上运行 Corosync <a href="#pvecm_corosync_over_bonds" id="pvecm_corosync_over_bonds"></a>

### 建议 <a href="#recommendations" id="recommendations"></a>

我们建议为主要 Corosync 链路至少使用一个专用物理 NIC，请参阅[要求](01-pvecm-cluster-requirements.md)。[绑定](../03-system-administration/04-sysadmin-network-configuration.md#sysadmin_network_bond)可用作附加链路，以提高冗余性。**每当将绑定用于 Corosync 流量时**，都适用以下注意事项：

- 在某些故障场景中，绑定模式 **active-backup** 可能无法提供预期的冗余，详情请见下文。
- 我们**不建议**将绑定模式 **balance-rr**、**balance-xor**、**balance-tlb** 或 **balance-alb** 用于 Corosync 流量。已知它们在某些故障场景中会引发问题，详情请见下文。
- **IEEE 802.3ad (LACP)**：如果将 LACP 绑定用于 corosync 流量，我们强烈建议设置 `bond-lacp-rate fast`，并且 **Proxmox VE** 节点和**交换机**两端都要设置！使用默认设置 `bond-lacp-rate slow` 时，已知此模式在某些故障场景中会引发问题，详情请见下文。

### 背景 <a href="#background" id="background"></a>

在某些故障场景中，使用 [绑定](../03-system-administration/04-sysadmin-network-configuration.md#sysadmin_network_bond) 作为 Corosync 链路可能会引发问题。考虑这样一种故障场景：绑定中的一个接口发生故障并停止传输数据包，但其链路状态仍为 up，并且没有其他可用的 Corosync 链路。在这种情况下，某些绑定模式可能导致非对称连接状态，使集群节点只能与不同的其他节点子集通信。受影响的是提供负载均衡的绑定模式，因为这些模式可能仍会尝试通过故障接口发送一部分数据包。在非对称连接的情况下，Corosync 可能无法在集群中形成稳定的仲裁。如果这种状态持续存在且启用了 HA，即使绑定没有任何问题的节点也可能自我隔离。在最坏的情况下，整个集群都可能自我隔离。

在上述故障场景中，绑定模式 **active-backup** **不会**导致非对称连接。但是，发生接口故障的绑定可能无法切换到备份链路。该节点可能会与集群失去连接，并在启用 HA 时自我隔离。

在上述故障场景中，绑定模式 **balance-rr**、**balance-xor**、**balance\_tlb** 或 **balance-alb** 可能导致非对称连接，如果启用了 HA，这可能会导致意外隔离。

绑定模式 **IEEE 802.3ad (LACP)** 在上述故障场景中可能导致非对称连接，但能从此状态恢复，因为绑定的两端（Proxmox VE 节点和交换机）在绑定接口连续未收到三个 LACPDU 时，都可以停止使用该接口。不过，默认设置下每 30 秒才发送一次 LACPDU，导致故障切换时间达到 90 秒。此时间过长，因为带有 HA 资源的节点在约一分钟没有稳定仲裁后就会自行隔离。如果使用 LACP 绑定传输 corosync 流量，建议设置 `bond-lacp-rate fast`，且在 **Proxmox VE** 节点和 **交换机** 上都设置！在一端设置此选项会要求另一端每秒发送一个 LACPDU。两端都设置此选项可将上述场景中的故障切换时间缩短为 3 秒，从而避免隔离。

## 5.8.3. 独立集群网络 <a href="#separate_cluster_network" id="separate_cluster_network"></a>

创建集群时不指定任何参数，corosync 集群网络通常会与 Web 界面和虚拟机的网络共用。根据您的设置，甚至存储流量也可能通过同一网络发送。建议更改这种情况，因为 corosync 是对时间要求严格的实时应用程序。

### 设置新网络 <a href="#setting_up_a_new_network" id="setting_up_a_new_network"></a>

首先，您必须设置一个新的网络接口。该接口应位于物理上独立的网络中。请确保您的网络符合[集群网络要求](#pvecm_cluster_network_requirements)。

### 在创建集群时分离 <a href="#separate_on_cluster_creation" id="separate_on_cluster_creation"></a>

这可以通过 *linkX* 参数实现，该参数属于用于创建新集群的 *pvecm create* 命令。

如果您已额外设置了一个网卡，并为其配置了静态地址 10.10.10.1/25，且希望通过此接口发送和接收所有集群通信，请执行：

```text
pvecm create test --link0 10.10.10.1
```

要检查一切是否正常工作，请执行：

```text
systemctl status corosync
```

然后，按照上述说明[添加使用独立集群网络的节点](04-pvecm-join-node-to-cluster.md#pvecm_adding_nodes_with_separated_cluster_network)。

### 创建集群后分离 <a href="#pvecm_separate_cluster_net_after_creation" id="pvecm_separate_cluster_net_after_creation"></a>

如果您已经创建了集群，并希望在不重建整个集群的情况下将其通信切换到另一个网络，可以执行此操作。此更改可能导致集群短暂失去仲裁，因为各节点必须重启 corosync，并逐一在新网络上启动。

首先，请查看如何[编辑 corosync.conf 文件](12-corosync-configuration.md#pvecm_edit_corosync_conf)。然后打开该文件，您应该会看到类似以下内容：

```text
logging {
  debug: off
  to_syslog: yes
}

nodelist {

  node {
    name: due
    nodeid: 2
    quorum_votes: 1
    ring0_addr: due
  }

  node {
    name: tre
    nodeid: 3
    quorum_votes: 1
    ring0_addr: tre
  }

  node {
    name: uno
    nodeid: 1
    quorum_votes: 1
    ring0_addr: uno
  }

}

quorum {
  provider: corosync_votequorum
}

totem {
  cluster_name: testcluster
  config_version: 3
  ip_version: ipv4-6
  secauth: on
  version: 2
  interface {
    linknumber: 0
  }

}
```

{% hint style="info" %}
`ringX_addr` 实际上指定的是一个 corosync **链路地址**。“ring”这一名称是旧版 corosync 的遗留，为保持向后兼容而保留。
{% endhint %}

首先要做的是在节点条目中添加 *name* 属性（如果尚未看到它们）。这些属性**必须**与节点名称匹配。

然后，将所有节点的 *ring0\_addr* 属性中的地址全部替换为新地址。此处可以直接使用 IP 地址或主机名。如果使用主机名，请确保所有节点都能解析它们（另请参阅[链路地址类型](#pvecm_corosync_addresses)）。

在此示例中，我们要将集群通信切换到 10.10.10.0/25 网络，因此分别更改每个节点的 *ring0\_addr*。

{% hint style="info" %}
完全相同的过程也可用于更改其他 *ringX\_addr* 值。但是，我们建议每次只更改一个链路地址，这样在出现问题时更容易恢复。
{% endhint %}

增加 *config\_version* 属性后，新配置文件应如下所示：

```text
logging {
  debug: off
  to_syslog: yes
}

nodelist {

  node {
    name: due
    nodeid: 2
    quorum_votes: 1
    ring0_addr: 10.10.10.2
  }

  node {
    name: tre
    nodeid: 3
    quorum_votes: 1
    ring0_addr: 10.10.10.3
  }

  node {
    name: uno
    nodeid: 1
    quorum_votes: 1
    ring0_addr: 10.10.10.1
  }

}

quorum {
  provider: corosync_votequorum
}

totem {
  cluster_name: testcluster
  config_version: 4
  ip_version: ipv4-6
  secauth: on
  version: 2
  interface {
    linknumber: 0
  }

}
```

然后，最后检查所有更改的信息是否正确，确认后保存，并再次按照[编辑 corosync.conf 文件](12-corosync-configuration.md#pvecm_edit_corosync_conf)一节的说明使其生效。

这些更改将实时应用，因此并非必须重启 corosync。如果您还更改了其他设置，或发现 corosync 报告问题，可以选择触发重启。

在单个节点上执行：

```text
systemctl restart corosync
```

现在检查一切是否正常：

```text
systemctl status corosync
```

如果 corosync 重新开始工作，也请在所有其他节点上重启它。随后，这些节点将在新网络上逐一加入集群成员关系。

## 5.8.4. Corosync 地址 <a href="#pvecm_corosync_addresses" id="pvecm_corosync_addresses"></a>

corosync 链路地址（为保持向后兼容，使用 *ringX\_addr* 在 `corosync.conf` 中表示）可通过两种方式指定：

- **IPv4/v6 地址**可直接使用。建议使用这种方式，因为此类地址是静态的，通常不会被随意更改。
- **主机名**将通过 `getaddrinfo` 解析，这意味着默认情况下，如果 IPv6 地址可用，将优先使用它们（另请参阅 `man gai.conf`）。将现有集群升级到 IPv6 时，尤其要记住这一点。

{% hint style="danger" %}
应谨慎使用主机名，因为无需改动 corosync 或其所在节点，就可以更改主机名解析到的地址；这可能导致在更改地址时未考虑其对 corosync 的影响。
{% endhint %}

如果倾向使用主机名，建议为 corosync 专门使用一个独立的静态主机名。此外，请确保集群中的每个节点都能正确解析所有主机名。

自 Proxmox VE 5.1 起，虽然仍支持主机名，但会在输入时解析主机名，并且仅将解析得到的 IP 保存到配置中。

在较早版本中加入集群的节点，很可能仍在 `corosync.conf` 中使用未解析的主机名。如上所述，将其替换为 IP 或独立主机名可能是个不错的主意。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
