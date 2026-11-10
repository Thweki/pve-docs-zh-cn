# 5.4. 向集群添加节点 <a href="#pvecm_join_node_to_cluster" id="pvecm_join_node_to_cluster"></a>

{% hint style="danger" %}
加入集群时，`/etc/pve` 中的所有现有配置都会被覆盖。特别是，加入的节点不能包含任何客户机，否则客户机 ID 可能会冲突，并且该节点将继承集群的存储配置。作为变通方法，要加入包含现有客户机的节点，可以为每个客户机创建备份（使用 `vzdump`），并在加入后以不同的 ID 恢复。如果节点的存储布局不同，则需要重新添加该节点的存储，并调整每个存储的节点限制，以反映该存储实际在哪些节点上可用。
{% endhint %}

## 5.4.1. 通过 GUI 将节点加入集群 <a href="#_join_node_to_cluster_via_gui" id="_join_node_to_cluster_via_gui"></a>

[![screenshot/gui-cluster-join-information.png](../../assets/screenshot-gui-cluster-join-information-png-9984deb0957b.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cluster-join-information.png)

登录现有集群节点的 Web 界面。在 *数据中心 → 集群* 下，点击顶部的 **加入信息** 按钮。然后，点击 **复制信息** 按钮。或者，手动复制 *信息* 字段中的字符串。

[![screenshot/gui-cluster-join.png](../../assets/screenshot-gui-cluster-join-png-312c75a66075.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cluster-join.png)

接下来，登录要添加的节点的 Web 界面。在 *数据中心 → 集群* 下，点击 **加入集群**。在 *信息* 字段中填入之前复制的 *加入信息* 文本。加入集群所需的大多数设置都会自动填写。出于安全原因，必须手动输入集群密码。

{% hint style="info" %}
要手动输入所有必需数据，可以取消选中 *辅助加入* 复选框。
{% endhint %}

点击 **加入** 按钮后，集群加入过程将立即开始。节点加入集群后，其当前节点证书将被替换为由集群证书颁发机构（CA）签发的证书。这意味着当前会话将在几秒后停止工作。随后，您可能需要强制重新加载 Web 界面，并使用集群凭据重新登录。

现在，您的节点应显示在 *数据中心 → 集群* 下。

## 5.4.2. 通过命令行将节点加入集群 <a href="#_join_node_to_cluster_via_command_line" id="_join_node_to_cluster_via_command_line"></a>

通过 `ssh` 登录要加入现有集群的节点。

```text
 # pvecm add IP-ADDRESS-CLUSTER
```

对于 `IP-ADDRESS-CLUSTER`，请使用现有集群节点的 IP 或主机名。建议使用 IP 地址（参见[链路地址类型](08-pvecm-cluster-network.md#pvecm_corosync_addresses)）。

默认情况下，`pvecm add` 会使用现有集群节点的 API 进行身份验证，提示输入该节点的 `root@pam` 密码，并验证其 SHA-256 证书指纹。此默认流程不需要 SSH 密码身份验证，因此管理员可以保留 `PasswordAuthentication no` 设置（位于 `sshd_config` 中）。

传递 `--use_ssh` 可回退到传统的基于 SSH 的加入方式，该方式使用 `ssh-copy-id` 将现有集群的 root 密钥合并到新节点。该流程确实需要在现有节点上进行 root SSH 登录（使用密码或密钥）。

要检查集群的状态，请使用：

```text
 # pvecm status
```

**添加 4 个节点后的集群状态**

```text
 # pvecm status
Cluster information
~~~~~~~~~~~~~~~~~~~
Name:             prod-central
Config Version:   3
Transport:        knet
Secure auth:      on

Quorum information
~~~~~~~~~~~~~~~~~~
Date:             Tue Sep 14 11:06:47 2021
Quorum provider:  corosync_votequorum
Nodes:            4
Node ID:          0x00000001
Ring ID:          1.1a8
Quorate:          Yes

Votequorum information
~~~~~~~~~~~~~~~~~~~~~~
Expected votes:   4
Highest expected: 4
Total votes:      4
Quorum:           3
Flags:            Quorate

Membership information
~~~~~~~~~~~~~~~~~~~~~~
    Nodeid      Votes Name
0x00000001          1 192.168.15.91
0x00000002          1 192.168.15.92 (local)
0x00000003          1 192.168.15.93
0x00000004          1 192.168.15.94
```

如果您只需要所有节点的列表，请使用：

```text
 # pvecm nodes
```

**列出集群中的节点**

```text
 # pvecm nodes

Membership information
~~~~~~~~~~~~~~~~~~~~~~
    Nodeid      Votes Name
         1          1 hp1
         2          1 hp2 (local)
         3          1 hp3
         4          1 hp4
```

## 5.4.3. 使用独立集群网络添加节点 <a href="#pvecm_adding_nodes_with_separated_cluster_network" id="pvecm_adding_nodes_with_separated_cluster_network"></a>

向使用独立集群网络的集群添加节点时，需要使用 *link0* 参数设置节点在该网络上的地址：

```text
# pvecm add IP-ADDRESS-CLUSTER --link0 LOCAL-IP-ADDRESS-LINK0
```

如果要使用 Kronosnet 传输层内置的[冗余](09-pvecm-redundancy.md)，还需使用 *link1* 参数。

使用 GUI 时，可以从相应的 *Link X* 字段中选择正确的接口，这些字段位于 **集群加入** 对话框中。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
