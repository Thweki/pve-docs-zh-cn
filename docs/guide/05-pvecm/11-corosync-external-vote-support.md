# 5.11. Corosync External Vote Support <a href="#_corosync_external_vote_support" id="_corosync_external_vote_support"></a>

本节介绍在 Proxmox VE 集群中部署外部投票器的一种方法。配置后，集群可以承受更多节点故障，同时不破坏集群通信的安全属性。

要实现这一点，需要两个服务：

- 一个在每个 Proxmox VE 节点上运行的 QDevice 守护进程
- 一个在独立服务器上运行的外部投票守护进程

因此，即使在较小的部署中（例如 2\+1 个节点），也可以实现更高的可用性。

## 5.11.1. QDevice Technical Overview <a href="#_qdevice_technical_overview" id="_qdevice_technical_overview"></a>

Corosync 仲裁设备（QDevice）是在每个集群节点上运行的守护进程。它根据在外部运行的第三方仲裁器的决定，为集群的仲裁子系统提供配置数量的选票。其主要用途是使集群能够承受比标准仲裁规则所允许的更多的节点故障。这是安全的，因为外部设备可以看到所有节点，因此可以只选择一组节点并将选票投给该组。只有在该组节点获得第三方选票后能够（再次）达到仲裁时，才会这样做。

目前，仅支持将 *QDevice Net* 用作第三方仲裁器。这个守护进程会在能够通过网络访问某个集群分区的成员时，向该分区提供选票。它在任何时候都只会向集群的一个分区投票。它旨在支持多个集群，几乎无需配置，也无需维护状态。新集群会得到动态处理，并且运行 QDevice 的宿主机上不需要配置文件。

对外部宿主机的唯一要求是，它需要能够通过网络访问集群，并且有可用的 corosync-qnetd 软件包。我们为基于 Debian 的宿主机提供软件包，其他 Linux 发行版也应能通过各自的软件包管理器获得相应软件包。

{% hint style="info" %}
与 corosync 本身不同，QDevice 通过 TCP/IP 连接到集群。该守护进程也可以在集群的 LAN 之外运行，并且不受 corosync 的低延迟要求限制。
{% endhint %}

## 5.11.2. Supported Setups <a href="#_supported_setups" id="_supported_setups"></a>

对于节点数为偶数的集群，我们支持使用 QDevice；如果双节点集群需要提供更高的可用性，我们也建议使用 QDevice。对于节点数为奇数的集群，我们目前不鼓励使用 QDevice。原因在于 QDevice 为每种集群类型提供的票数不同。节点数为偶数的集群会获得额外的一票，这只会提高可用性，因为如果 QDevice 本身发生故障，您的处境与完全没有 QDevice 时相同。

另一方面，对于节点数为奇数的集群，QDevice 提供 *(N-1)* 票——其中 *N* 对应集群节点数。这种不同的行为是合理的；如果它只有额外的一票，集群可能会陷入脑裂。该算法允许除一个节点之外的所有节点（自然也包括 QDevice 本身）发生故障。然而，这有两个缺点：

- 如果 QNet 守护进程本身发生故障，则不能再有任何其他节点发生故障，否则集群会立即失去仲裁。例如，在一个有 15 个节点的集群中，可以有 7 个节点发生故障，之后集群才会失去仲裁。但是，如果此处配置了 QDevice 且其本身发生故障，则 15 个节点中**任何一个节点**都不得发生故障。在这种情况下，QDevice 几乎相当于单点故障。
- 起初，除一个节点和 QDevice 之外的所有节点都可能发生故障，这听起来很有前景，但这可能导致 HA 服务大规模恢复，从而使仅剩的单个节点过载。此外，如果只有 *((N-1)/2)* 个或更少的节点保持在线，Ceph 服务器将停止提供服务。

如果您了解这些缺点和影响，可以自行决定是否要在节点数为奇数的集群配置中使用该技术。

## 5.11.3. QDevice-Net Setup <a href="#_qdevice_net_setup" id="_qdevice_net_setup"></a>

我们建议以非特权用户身份运行任何为 corosync-qdevice 提供投票的守护进程。Proxmox VE 和 Debian 提供的软件包已按此方式配置。守护进程与集群之间的流量必须加密，以确保 QDevice 安全地集成到 Proxmox VE 中。

首先，在您的外部服务器上安装 *corosync-qnetd* 软件包

```text
external# apt install corosync-qnetd
```

并在所有集群节点上安装 *corosync-qdevice* 软件包

```text
pve# apt install corosync-qdevice
```

完成此操作后，确保集群中的所有节点都在线。

现在，您可以在其中一个 Proxmox VE 节点上运行以下命令来设置 QDevice：

```text
pve# pvecm qdevice setup <QDEVICE-IP>
```

集群的 SSH 密钥将自动复制到 QDevice。

{% hint style="info" %}
请确保在外部服务器上为 root 用户设置基于密钥的访问，或者在设置阶段暂时允许 root 用户使用密码登录。如果在此阶段收到 *Host key verification failed.* 之类的错误，运行 `pvecm updatecerts` 可能会解决该问题。
{% endhint %}

所有步骤成功完成后，您将看到“Done”。您可以使用以下命令验证 QDevice 是否已设置：

```text
pve# pvecm status

...

Votequorum information
~~~~~~~~~~~~~~~~~~~~~
Expected votes:   3
Highest expected: 3
Total votes:      3
Quorum:           2
Flags:            Quorate Qdevice

Membership information
~~~~~~~~~~~~~~~~~~~~~~
    Nodeid      Votes    Qdevice Name
    0x00000001      1    A,V,NMW 192.168.22.180 (local)
    0x00000002      1    A,V,NMW 192.168.22.181
    0x00000000      1            Qdevice
```

### QDevice Status Flags <a href="#pvecm_qdevice_status_flags" id="pvecm_qdevice_status_flags"></a>

如上所示，QDevice 的状态输出通常包含三列：

- `A` / `NA`: Alive or Not Alive. Indicates if the communication to the external `corosync-qnetd` daemon works.
- `V` / `NV`: If the QDevice will cast a vote for the node. In a split-brain situation, where the corosync connection between the nodes is down, but they both can still communicate with the external `corosync-qnetd` daemon, only one node will get the vote.
- `MW` / `NMW`: Master wins (`MV`) or not (`NMW`). Default is `NMW`, see [\[1\]](#note-34613a5d-1).
- `NR`: QDevice is not registered.

{% hint style="info" %}
如果您的 QDevice 被列为 `Not Alive`（在上面的输出中为 `NA`），请确保可以通过 TCP/IP 访问外部服务器的端口 `5403`（qnetd 服务器的默认端口）！
{% endhint %}

## 5.11.4. Frequently Asked Questions <a href="#_frequently_asked_questions" id="_frequently_asked_questions"></a>

### Tie Breaking <a href="#_tie_breaking" id="_tie_breaking"></a>

在出现平局时，如果两个大小相同的集群分区彼此不可见，但都能看到 QDevice，则 QDevice 会选择节点 ID 最低的分区，并向其提供一票。可以使用配置选项 `tie_breaker` 调整此行为（更多信息请参阅 `man corosync-qdevice`），并且需要在所有节点上重启 `corosync-qdevice.service`。

### Possible Negative Implications <a href="#_possible_negative_implications" id="_possible_negative_implications"></a>

对于节点数为偶数的集群，使用 QDevice 不会产生负面影响。如果它无法正常工作，则与完全没有 QDevice 相同。

### Adding/Deleting Nodes After QDevice Setup <a href="#_adding_deleting_nodes_after_qdevice_setup" id="_adding_deleting_nodes_after_qdevice_setup"></a>

如果您想在配置了 QDevice 的集群中添加新节点或删除现有节点，需要先移除 QDevice。之后，您可以正常添加或删除节点。一旦集群再次具有偶数个节点，您就可以按照前面的说明重新设置 QDevice。

### Removing the QDevice <a href="#_removing_the_qdevice" id="_removing_the_qdevice"></a>

如果您使用官方 `pvecm` 工具添加了 QDevice，可以通过运行以下命令将其移除：

```text
pve# pvecm qdevice remove
```

## 注释

### 注释 1 <a href="#note-34613a5d-1" id="note-34613a5d-1"></a>

`votequorum_qdevice_master_wins` manual page [https://manpages.debian.org/stable/libvotequorum-dev/votequorum\_qdevice\_master\_wins.3.en.html](https://manpages.debian.org/stable/libvotequorum-dev/votequorum_qdevice_master_wins.3.en.html)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
