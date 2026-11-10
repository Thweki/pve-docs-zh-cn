# pmxcfs(8)

## 名称 <a href="#chapter_pmxcfs" id="chapter_pmxcfs"></a>

pmxcfs \- Proxmox 集群文件系统

## 概要 <a href="#_synopsis" id="_synopsis"></a>

**pmxcfs** `[OPTIONS]`

帮助选项：

**`-h`, `--help`**

显示帮助选项

应用程序选项：

**`-d`, `--debug`**

启用调试消息

**`-f`, `--foreground`**

不要将服务器守护进程化

**`-l`, `--local`**

强制使用本地模式（忽略 corosync.conf，强制仲裁）

通常使用 systemd 工具集启动和管理此服务。该服务称为 *pve-cluster*。

```text
systemctl start pve-cluster
```

```text
systemctl stop pve-cluster
```

```text
systemctl status pve-cluster
```

## 描述 <a href="#_description" id="_description"></a>

Proxmox 集群文件系统（“pmxcfs”）是一种数据库驱动的文件系统，用于存储配置文件，并通过 `corosync` 实时复制到所有集群节点。我们使用它来存储所有与 Proxmox VE 相关的配置文件。

尽管文件系统将所有数据存储在磁盘上的持久化数据库中，但 RAM 中也保留了一份数据副本。这限制了其最大容量，目前为 128 MiB。但这仍足以存储数千台虚拟机的配置。

该系统具有以下优点：

- 将所有配置实时无缝复制到所有节点
- 提供强一致性检查，避免 VM ID 重复
- 节点失去仲裁时为只读状态
- 自动将 corosync 集群配置更新到所有节点
- 包含分布式锁机制

## POSIX 兼容性 <a href="#_posix_compatibility" id="_posix_compatibility"></a>

该文件系统基于 FUSE，因此其行为类似于 POSIX。但有些功能并未实现，因为我们不需要它们：

- 只能创建普通文件和目录，不能创建符号链接，……
- 不能重命名非空目录（因为这样可以更容易地保证 VMID 的唯一性）。
- 不能更改文件权限（权限基于路径）
- `O_EXCL` 创建操作不是原子的（与旧版 NFS 类似）
- `O_TRUNC` 创建操作不是原子的（FUSE 限制）

## 文件访问权限 <a href="#_file_access_rights" id="_file_access_rights"></a>

所有文件和目录的所有者均为用户 `root`，所属组均为 `www-data`。只有 root 拥有写权限，但 `www-data` 组可以读取大多数文件。以下路径下的文件只能由 root 访问：

```text
/etc/pve/priv/
/etc/pve/nodes/${NAME}/priv/
```

## 技术 <a href="#_technology" id="_technology"></a>

我们使用 [Corosync Cluster Engine](https://www.corosync.org) 进行集群通信，并使用 [SQlite](https://www.sqlite.org) 作为数据库文件。该文件系统使用 [FUSE](https://github.com/libfuse/libfuse) 在用户空间中实现。

## 文件系统布局 <a href="#_file_system_layout" id="_file_system_layout"></a>

该文件系统挂载于：

```text
/etc/pve
```

### 文件 <a href="#_files" id="_files"></a>

<table>


<tbody>
<tr>
<td><p><code>authkey.pub</code></p></td>
<td><p>票据系统使用的公钥</p></td>
</tr>
<tr>
<td><p><code>ceph.conf</code></p></td>
<td><p>Ceph 配置文件（注意：/etc/ceph/ceph.conf 是指向此文件的符号链接）</p></td>
</tr>
<tr>
<td><p><code>corosync.conf</code></p></td>
<td><p>Corosync 集群配置文件（在 Proxmox VE 4.x 之前，此文件称为 cluster.conf）</p></td>
</tr>
<tr>
<td><p><code>datacenter.cfg</code></p></td>
<td><p>Proxmox VE 全数据中心范围的配置（键盘布局、代理等）</p></td>
</tr>
<tr>
<td><p><code>domains.cfg</code></p></td>
<td><p>Proxmox VE 身份验证域</p></td>
</tr>
<tr>
<td><p><code>firewall/cluster.fw</code></p></td>
<td><p>应用于所有节点的防火墙配置</p></td>
</tr>
<tr>
<td><p><code>firewall/&lt;NAME&gt;.fw</code></p></td>
<td><p>各个节点的防火墙配置</p></td>
</tr>
<tr>
<td><p><code>firewall/&lt;VMID&gt;.fw</code></p></td>
<td><p>VM 和容器的防火墙配置</p></td>
</tr>
<tr>
<td><p><code>ha/crm_commands</code></p></td>
<td><p>显示 CRM 当前正在执行的 HA 操作</p></td>
</tr>
<tr>
<td><p><code>ha/manager_status</code></p></td>
<td><p>有关集群中 HA 服务的 JSON 格式信息</p></td>
</tr>
<tr>
<td><p><code>ha/resources.cfg</code></p></td>
<td><p>高可用性管理的资源及其当前状态</p></td>
</tr>
<tr>
<td><p><code>ha/rules.cfg</code></p></td>
<td><p>用于约束 HA 管理器调度 HA 资源的规则</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/config</code></p></td>
<td><p>节点特定配置</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/lxc/&lt;VMID&gt;.conf</code></p></td>
<td><p>LXC 容器的 VM 配置数据</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/openvz/</code></p></td>
<td><p>在 Proxmox VE 4.0 之前，用于容器配置数据（已弃用，即将移除）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pve-ssl.key</code></p></td>
<td><p><code>pve-ssl.pem</code> 的 SSL 私钥</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pve-ssl.pem</code></p></td>
<td><p>Web 服务器的 SSL 公共证书（由集群 CA 签名）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pveproxy-ssl.key</code></p></td>
<td><p><code>pveproxy-ssl.pem</code> 的 SSL 私钥（可选）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pveproxy-ssl.pem</code></p></td>
<td><p>Web 服务器的 SSL 公共证书（链）（可选，用于覆盖 <code>pve-ssl.pem</code>）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/qemu-server/&lt;VMID&gt;.conf</code></p></td>
<td><p>KVM VM 的 VM 配置数据</p></td>
</tr>
<tr>
<td><p><code>priv/authkey.key</code></p></td>
<td><p>票据系统使用的私钥</p></td>
</tr>
<tr>
<td><p><code>priv/authorized_keys</code></p></td>
<td><p>用于身份验证的集群成员 SSH 密钥</p></td>
</tr>
<tr>
<td><p><code>priv/ceph*</code></p></td>
<td><p>Ceph 身份验证密钥及相关权限</p></td>
</tr>
<tr>
<td><p><code>priv/known_hosts</code></p></td>
<td><p>用于验证的集群成员 SSH 密钥</p></td>
</tr>
<tr>
<td><p><code>priv/lock/*</code></p></td>
<td><p>各种服务使用的锁文件，以确保集群范围操作的安全</p></td>
</tr>
<tr>
<td><p><code>priv/pve-root-ca.key</code></p></td>
<td><p>集群 CA 的私钥</p></td>
</tr>
<tr>
<td><p><code>priv/shadow.cfg</code></p></td>
<td><p>PVE Realm 用户的 shadow 密码文件</p></td>
</tr>
<tr>
<td><p><code>priv/storage/&lt;STORAGE-ID&gt;.pw</code></p></td>
<td><p>以明文形式包含某个存储的密码</p></td>
</tr>
<tr>
<td><p><code>priv/tfa.cfg</code></p></td>
<td><p>Base64 编码的双因素身份验证配置</p></td>
</tr>
<tr>
<td><p><code>priv/token.cfg</code></p></td>
<td><p>所有 API 令牌的密钥</p></td>
</tr>
<tr>
<td><p><code>pve-root-ca.pem</code></p></td>
<td><p>集群 CA 的公共证书</p></td>
</tr>
<tr>
<td><p><code>pve-www.key</code></p></td>
<td><p>用于生成 CSRF 令牌的私钥</p></td>
</tr>
<tr>
<td><p><code>sdn/*</code></p></td>
<td><p>软件定义网络（SDN）的共享配置文件</p></td>
</tr>
<tr>
<td><p><code>status.cfg</code></p></td>
<td><p>Proxmox VE 外部指标服务器配置</p></td>
</tr>
<tr>
<td><p><code>storage.cfg</code></p></td>
<td><p>Proxmox VE 存储配置</p></td>
</tr>
<tr>
<td><p><code>user.cfg</code></p></td>
<td><p>Proxmox VE 访问控制配置（用户/组/……）</p></td>
</tr>
<tr>
<td><p><code>virtual-guest/cpu-models.conf</code></p></td>
<td><p>用于存储自定义 CPU 模型</p></td>
</tr>
<tr>
<td><p><code>vzdump.cron</code></p></td>
<td><p>集群范围的 vzdump 备份任务计划</p></td>
</tr>
</tbody>
</table>

### 符号链接 <a href="#_symbolic_links" id="_symbolic_links"></a>

集群文件系统中的某些目录使用符号链接，以指向节点自身的配置文件。因此，下表中所指向的文件在集群的每个节点上分别对应不同的文件。

<table>


<tbody>
<tr>
<td><p><code>local</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;</code></p></td>
</tr>
<tr>
<td><p><code>lxc</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;/lxc/</code></p></td>
</tr>
<tr>
<td><p><code>openvz</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;/openvz/</code> (deprecated, removed soon)</p></td>
</tr>
<tr>
<td><p><code>qemu-server</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;/qemu-server/</code></p></td>
</tr>
</tbody>
</table>

### 用于调试的特殊状态文件（JSON） <a href="#_special_status_files_for_debugging_json" id="_special_status_files_for_debugging_json"></a>

<table>


<tbody>
<tr>
<td><p><code>.version</code></p></td>
<td><p>文件版本（用于检测文件修改）</p></td>
</tr>
<tr>
<td><p><code>.members</code></p></td>
<td><p>集群成员信息</p></td>
</tr>
<tr>
<td><p><code>.vmlist</code></p></td>
<td><p>所有 VM 的列表</p></td>
</tr>
<tr>
<td><p><code>.clusterlog</code></p></td>
<td><p>集群日志（最后 50 条）</p></td>
</tr>
<tr>
<td><p><code>.rrd</code></p></td>
<td><p>RRD 数据（最新条目）</p></td>
</tr>
</tbody>
</table>

### 启用/禁用调试 <a href="#_enable_disable_debugging" id="_enable_disable_debugging"></a>

可以使用以下命令启用详细的 syslog 消息：

```text
echo "1" >/etc/pve/.debug
```

并使用以下命令禁用详细的 syslog 消息：

```text
echo "0" >/etc/pve/.debug
```

## 恢复 <a href="#_recovery" id="_recovery"></a>

如果您的 Proxmox VE 宿主机出现严重问题，例如硬件故障，复制 pmxcfs 数据库文件 `/var/lib/pve-cluster/config.db` 并将其移动到新的 Proxmox VE 宿主机可能会有所帮助。在新宿主机上（未运行任何内容），您需要停止 `pve-cluster` 服务并替换 `config.db` 文件（所需权限为 `0600`）。随后，根据丢失的 Proxmox VE 宿主机调整 `/etc/hostname` 和 `/etc/hosts`，然后重新启动并检查（也不要忘记您的 VM/CT 数据）。

### 移除集群配置 <a href="#_remove_cluster_configuration" id="_remove_cluster_configuration"></a>

建议的方法是在将节点从集群中移除后重新安装该节点。这可确保所有集群/SSH 密钥以及任何共享配置数据均被销毁。

在某些情况下，您可能希望在不重新安装的情况下将节点恢复为本地模式，[不重装而分离节点](pvecm-1.md#pvecm_separate_node_without_reinstall)中对此进行了说明

### 从故障节点恢复/迁移客户机 <a href="#_recovering_moving_guests_from_failed_nodes" id="_recovering_moving_guests_from_failed_nodes"></a>

对于 `nodes/<NAME>/qemu-server/`（VM）和 `nodes/<NAME>/lxc/`（容器）中的客户机配置文件，Proxmox VE 将包含这些文件的节点 `<NAME>` 视为相应客户机的所有者。这一概念使得我们可以使用本地锁，而不是开销较大的集群范围锁，以防止并发更改客户机配置。

因此，如果客户机的所属节点发生故障（例如由于断电、隔离事件等），则无法进行常规迁移（即使所有磁盘都位于共享存储上），因为无法获得（离线）所属节点上的这种本地锁。对于由 HA 管理的客户机，这不是问题，因为 Proxmox VE 的高可用性栈包含必要的（集群范围）锁和看门狗功能，可确保客户机从被隔离的节点正确、自动地恢复。

如果非 HA 管理的客户机只有共享磁盘（并且没有其他仅在故障节点上可用的本地资源），则只需将客户机配置文件从 `/etc/pve/` 中故障节点的目录移动到在线节点的目录，即可手动恢复（这会更改客户机的逻辑所有者或位置）。

例如，在集群的任何成员节点上以 root 身份运行以下命令，即可将 ID 为 `100` 的 VM 从离线的 `node1` 恢复到另一个节点 `node2`：

```text
mv /etc/pve/nodes/node1/qemu-server/100.conf /etc/pve/nodes/node2/qemu-server/
```

{% hint style="warning" %}
在以这种方式手动恢复客户机之前，请务必确保故障源节点确实已关机/隔离。否则，`mv` 命令会违反 Proxmox VE 的锁定原则，可能产生意想不到的后果。
{% endhint %}

{% hint style="warning" %}
具有本地磁盘（或其他仅在离线节点上可用的本地资源）的客户机无法通过这种方式恢复。请等待故障节点重新加入集群，或从备份中恢复此类客户机。
{% endhint %}

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pmxcfs.8.html) · 版本 9.2.13 · 非官方中文翻译。
