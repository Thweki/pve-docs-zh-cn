# 5.9. Corosync 冗余 <a href="#pvecm_redundancy" id="pvecm_redundancy"></a>

Corosync 默认通过其集成的 Kronosnet 层支持冗余网络（旧版 udp/udpu 传输不支持此功能）。要启用该功能，可以通过 *--linkX* 参数（属于 `pvecm`）、在 GUI 中设置为 **Link 1**（创建集群或添加新节点时），或者通过指定多个 *ringX\_addr*（位于 `corosync.conf` 中）来指定多个链路地址。

{% hint style="info" %}
为提供有效的故障切换，每条链路都应使用独立的物理网络连接。
{% endhint %}

以下示例假设每个集群节点都配置了一个 10.10.10.0/25 中的静态地址和一个 10.20.20.0/25 中的静态地址。

链路根据优先级设置使用。您可以在对应的接口小节中设置 *knet\_link\_priority* 来配置此优先级（该小节位于 `corosync.conf`），或者，最好在创建集群时使用 *priority* 参数，并通过 `pvecm` 执行创建操作：

```text
 # pvecm create CLUSTERNAME --link0 10.10.10.1,priority=15 --link1 10.20.20.1,priority=20
```

这将使 *link1* 被优先使用，因为它的优先级更高。

如果未手动配置优先级（或两条链路的优先级相同），链路将按其编号顺序使用，编号越小，优先级越高。

即使所有链路都正常工作，也只有优先级最高的链路会承载 corosync 流量。链路优先级不能混合，这意味着优先级不同的链路将无法相互通信。

由于除非所有更高优先级的链路都发生故障，否则较低优先级的链路不会承载流量，因此，将用于其他任务（虚拟机、存储等）的网络指定为低优先级链路是一种有用的策略。在最坏的情况下，延迟较高或较为拥塞的连接可能也比完全没有连接要好。

## 5.9.1. 向现有集群添加冗余链路 <a href="#_adding_redundant_links_to_an_existing_cluster" id="_adding_redundant_links_to_an_existing_cluster"></a>

要向运行中的配置添加新链路，首先请查看如何[编辑 corosync.conf 文件](12-corosync-configuration.md#pvecm_edit_corosync_conf)。

然后，将新的 *ringX\_addr* 添加到 `nodelist` 小节中的每个节点。确保所有添加该条目的节点都使用相同的 *X*，并且该编号在每个节点内都是唯一的。

Lastly, add a new *interface*, as shown below, to your `totem` section, replacing *X* with the link number chosen above.

假设您添加了一条编号为 1 的链路，新配置文件可能如下所示：

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
    ring1_addr: 10.20.20.2
  }

  node {
    name: tre
    nodeid: 3
    quorum_votes: 1
    ring0_addr: 10.10.10.3
    ring1_addr: 10.20.20.3
  }

  node {
    name: uno
    nodeid: 1
    quorum_votes: 1
    ring0_addr: 10.10.10.1
    ring1_addr: 10.20.20.1
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
  interface {
    linknumber: 1
  }
}
```

按照[编辑 corosync.conf 文件](12-corosync-configuration.md#pvecm_edit_corosync_conf)的最后步骤操作后，新链路即会启用。应该无需重启。您可以使用以下命令检查 corosync 是否已加载新链路：

```text
journalctl -b -u corosync
```

最好在其中一个节点上暂时断开旧链路来测试新链路，并确保其状态在断开期间仍保持在线：

```text
pvecm status
```

如果您看到集群状态正常，则表示新链路正在使用中。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
