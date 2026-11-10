# pmxcfs(8)

## 名称 <a href="#chapter_pmxcfs" id="chapter_pmxcfs"></a>

pmxcfs - Proxmox 集群文件系统

## 概要 <a href="#_synopsis" id="_synopsis"></a>

**pmxcfs** `[OPTIONS]`

帮助选项：

**`-h`, `--help`**

显示帮助选项

应用程序选项：

**`-d`, `--debug`**

Turn on debug messages

**`-f`, `--foreground`**

Do not daemonize server

**`-l`, `--local`**

Force local mode (ignore corosync.conf, force quorum)

This service is usually started and managed using systemd toolset. The service is called *pve-cluster*.

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

The Proxmox Cluster file system (“pmxcfs”) is a database-driven file system for storing configuration files, replicated in real time to all cluster nodes using `corosync`. We use this to store all Proxmox VE related configuration files.

Although the file system stores all data inside a persistent database on disk, a copy of the data resides in RAM. This imposes restrictions on the maximum size, which is currently 128 MiB. This is still enough to store the configuration of several thousand virtual machines.

This system provides the following advantages:

- Seamless replication of all configuration to all nodes in real time
- Provides strong consistency checks to avoid duplicate VM IDs
- Read-only when a node loses quorum
- Automatic updates of the corosync cluster configuration to all nodes
- Includes a distributed locking mechanism

## POSIX Compatibility <a href="#_posix_compatibility" id="_posix_compatibility"></a>

The file system is based on FUSE, so the behavior is POSIX like. But some feature are simply not implemented, because we do not need them:

- You can just generate normal files and directories, but no symbolic links, …
- You can’t rename non-empty directories (because this makes it easier to guarantee that VMIDs are unique).
- You can’t change file permissions (permissions are based on paths)
- `O_EXCL` creates were not atomic (like old NFS)
- `O_TRUNC` creates are not atomic (FUSE restriction)

## File Access Rights <a href="#_file_access_rights" id="_file_access_rights"></a>

All files and directories are owned by user `root` and have group `www-data`. Only root has write permissions, but group `www-data` can read most files. Files below the following paths are only accessible by root:

```text
/etc/pve/priv/
/etc/pve/nodes/${NAME}/priv/
```

## Technology <a href="#_technology" id="_technology"></a>

We use the [Corosync Cluster Engine](https://www.corosync.org) for cluster communication, and [SQlite](https://www.sqlite.org) for the database file. The file system is implemented in user space using [FUSE](https://github.com/libfuse/libfuse).

## File System Layout <a href="#_file_system_layout" id="_file_system_layout"></a>

The file system is mounted at:

```text
/etc/pve
```

### Files <a href="#_files" id="_files"></a>

<table>


<tbody>
<tr>
<td><p><code>authkey.pub</code></p></td>
<td><p>Public key used by the ticket system</p></td>
</tr>
<tr>
<td><p><code>ceph.conf</code></p></td>
<td><p>Ceph configuration file (note: /etc/ceph/ceph.conf is a symbolic link to this)</p></td>
</tr>
<tr>
<td><p><code>corosync.conf</code></p></td>
<td><p>Corosync cluster configuration file (prior to Proxmox VE 4.x, this file was called cluster.conf)</p></td>
</tr>
<tr>
<td><p><code>datacenter.cfg</code></p></td>
<td><p>Proxmox VE datacenter-wide configuration (keyboard layout, proxy, …)</p></td>
</tr>
<tr>
<td><p><code>domains.cfg</code></p></td>
<td><p>Proxmox VE authentication domains</p></td>
</tr>
<tr>
<td><p><code>firewall/cluster.fw</code></p></td>
<td><p>Firewall configuration applied to all nodes</p></td>
</tr>
<tr>
<td><p><code>firewall/&lt;NAME&gt;.fw</code></p></td>
<td><p>Firewall configuration for individual nodes</p></td>
</tr>
<tr>
<td><p><code>firewall/&lt;VMID&gt;.fw</code></p></td>
<td><p>Firewall configuration for VMs and containers</p></td>
</tr>
<tr>
<td><p><code>ha/crm_commands</code></p></td>
<td><p>Displays HA operations that are currently being carried out by the CRM</p></td>
</tr>
<tr>
<td><p><code>ha/manager_status</code></p></td>
<td><p>JSON-formatted information regarding HA services on the cluster</p></td>
</tr>
<tr>
<td><p><code>ha/resources.cfg</code></p></td>
<td><p>Resources managed by high availability, and their current state</p></td>
</tr>
<tr>
<td><p><code>ha/rules.cfg</code></p></td>
<td><p>Rules putting constraints on the HA manager’s scheduling of HA resources</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/config</code></p></td>
<td><p>Node-specific configuration</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/lxc/&lt;VMID&gt;.conf</code></p></td>
<td><p>VM configuration data for LXC containers</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/openvz/</code></p></td>
<td><p>Prior to Proxmox VE 4.0, used for container configuration data (deprecated, removed soon)</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pve-ssl.key</code></p></td>
<td><p>Private SSL key for <code>pve-ssl.pem</code></p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pve-ssl.pem</code></p></td>
<td><p>Public SSL certificate for web server (signed by cluster CA)</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pveproxy-ssl.key</code></p></td>
<td><p>Private SSL key for <code>pveproxy-ssl.pem</code> (optional)</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pveproxy-ssl.pem</code></p></td>
<td><p>Public SSL certificate (chain) for web server (optional override for <code>pve-ssl.pem</code>)</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/qemu-server/&lt;VMID&gt;.conf</code></p></td>
<td><p>VM configuration data for KVM VMs</p></td>
</tr>
<tr>
<td><p><code>priv/authkey.key</code></p></td>
<td><p>Private key used by ticket system</p></td>
</tr>
<tr>
<td><p><code>priv/authorized_keys</code></p></td>
<td><p>SSH keys of cluster members for authentication</p></td>
</tr>
<tr>
<td><p><code>priv/ceph*</code></p></td>
<td><p>Ceph authentication keys and associated capabilities</p></td>
</tr>
<tr>
<td><p><code>priv/known_hosts</code></p></td>
<td><p>SSH keys of the cluster members for verification</p></td>
</tr>
<tr>
<td><p><code>priv/lock/*</code></p></td>
<td><p>Lock files used by various services to ensure safe cluster-wide operations</p></td>
</tr>
<tr>
<td><p><code>priv/pve-root-ca.key</code></p></td>
<td><p>Private key of cluster CA</p></td>
</tr>
<tr>
<td><p><code>priv/shadow.cfg</code></p></td>
<td><p>Shadow password file for PVE Realm users</p></td>
</tr>
<tr>
<td><p><code>priv/storage/&lt;STORAGE-ID&gt;.pw</code></p></td>
<td><p>Contains the password of a storage in plain text</p></td>
</tr>
<tr>
<td><p><code>priv/tfa.cfg</code></p></td>
<td><p>Base64-encoded two-factor authentication configuration</p></td>
</tr>
<tr>
<td><p><code>priv/token.cfg</code></p></td>
<td><p>API token secrets of all tokens</p></td>
</tr>
<tr>
<td><p><code>pve-root-ca.pem</code></p></td>
<td><p>Public certificate of cluster CA</p></td>
</tr>
<tr>
<td><p><code>pve-www.key</code></p></td>
<td><p>Private key used for generating CSRF tokens</p></td>
</tr>
<tr>
<td><p><code>sdn/*</code></p></td>
<td><p>Shared configuration files for Software Defined Networking (SDN)</p></td>
</tr>
<tr>
<td><p><code>status.cfg</code></p></td>
<td><p>Proxmox VE external metrics server configuration</p></td>
</tr>
<tr>
<td><p><code>storage.cfg</code></p></td>
<td><p>Proxmox VE storage configuration</p></td>
</tr>
<tr>
<td><p><code>user.cfg</code></p></td>
<td><p>Proxmox VE access control configuration (users/groups/…)</p></td>
</tr>
<tr>
<td><p><code>virtual-guest/cpu-models.conf</code></p></td>
<td><p>For storing custom CPU models</p></td>
</tr>
<tr>
<td><p><code>vzdump.cron</code></p></td>
<td><p>Cluster-wide vzdump backup-job schedule</p></td>
</tr>
</tbody>
</table>

### Symbolic links <a href="#_symbolic_links" id="_symbolic_links"></a>

Certain directories within the cluster file system use symbolic links, in order to point to a node’s own configuration files. Thus, the files pointed to in the table below refer to different files on each node of the cluster.

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

### Special status files for debugging (JSON) <a href="#_special_status_files_for_debugging_json" id="_special_status_files_for_debugging_json"></a>

<table>


<tbody>
<tr>
<td><p><code>.version</code></p></td>
<td><p>File versions (to detect file modifications)</p></td>
</tr>
<tr>
<td><p><code>.members</code></p></td>
<td><p>Info about cluster members</p></td>
</tr>
<tr>
<td><p><code>.vmlist</code></p></td>
<td><p>List of all VMs</p></td>
</tr>
<tr>
<td><p><code>.clusterlog</code></p></td>
<td><p>Cluster log (last 50 entries)</p></td>
</tr>
<tr>
<td><p><code>.rrd</code></p></td>
<td><p>RRD data (most recent entries)</p></td>
</tr>
</tbody>
</table>

### Enable/Disable debugging <a href="#_enable_disable_debugging" id="_enable_disable_debugging"></a>

You can enable verbose syslog messages with:

```text
echo "1" >/etc/pve/.debug
```

And disable verbose syslog messages with:

```text
echo "0" >/etc/pve/.debug
```

## Recovery <a href="#_recovery" id="_recovery"></a>

If you have major problems with your Proxmox VE host, for example hardware issues, it could be helpful to copy the pmxcfs database file `/var/lib/pve-cluster/config.db`, and move it to a new Proxmox VE host. On the new host (with nothing running), you need to stop the `pve-cluster` service and replace the `config.db` file (required permissions `0600`). Following this, adapt `/etc/hostname` and `/etc/hosts` according to the lost Proxmox VE host, then reboot and check (and don’t forget your VM/CT data).

### Remove Cluster Configuration <a href="#_remove_cluster_configuration" id="_remove_cluster_configuration"></a>

The recommended way is to reinstall the node after you remove it from your cluster. This ensures that all secret cluster/ssh keys and any shared configuration data is destroyed.

In some cases, you might prefer to put a node back to local mode without reinstalling, which is described in [Separate A Node Without Reinstalling](pvecm-1.md#pvecm_separate_node_without_reinstall)

### Recovering/Moving Guests from Failed Nodes <a href="#_recovering_moving_guests_from_failed_nodes" id="_recovering_moving_guests_from_failed_nodes"></a>

For the guest configuration files in `nodes/<NAME>/qemu-server/` (VMs) and `nodes/<NAME>/lxc/` (containers), Proxmox VE sees the containing node `<NAME>` as the owner of the respective guest. This concept enables the usage of local locks instead of expensive cluster-wide locks for preventing concurrent guest configuration changes.

As a consequence, if the owning node of a guest fails (for example, due to a power outage, fencing event, etc.), a regular migration is not possible (even if all the disks are located on shared storage), because such a local lock on the (offline) owning node is unobtainable. This is not a problem for HA-managed guests, as Proxmox VE’s High Availability stack includes the necessary (cluster-wide) locking and watchdog functionality to ensure correct and automatic recovery of guests from fenced nodes.

If a non-HA-managed guest has only shared disks (and no other local resources which are only available on the failed node), a manual recovery is possible by simply moving the guest configuration file from the failed node’s directory in `/etc/pve/` to an online node’s directory (which changes the logical owner or location of the guest).

For example, recovering the VM with ID `100` from an offline `node1` to another node `node2` works by running the following command as root on any member node of the cluster:

```text
mv /etc/pve/nodes/node1/qemu-server/100.conf /etc/pve/nodes/node2/qemu-server/
```

{% hint style="warning" %}
Before manually recovering a guest like this, make absolutely sure that the failed source node is really powered off/fenced. Otherwise Proxmox VE’s locking principles are violated by the `mv` command, which can have unexpected consequences.
{% endhint %}

{% hint style="warning" %}
Guests with local disks (or other local resources which are only available on the offline node) are not recoverable like this. Either wait for the failed node to rejoin the cluster or restore such guests from backups.
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
