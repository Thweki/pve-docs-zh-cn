# 6.4. File System Layout <a href="#_file_system_layout" id="_file_system_layout"></a>

The file system is mounted at:

```text
/etc/pve
```

## 6.4.1. Files <a href="#_files" id="_files"></a>

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

## 6.4.2. Symbolic links <a href="#_symbolic_links" id="_symbolic_links"></a>

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

## 6.4.3. Special status files for debugging (JSON) <a href="#_special_status_files_for_debugging_json" id="_special_status_files_for_debugging_json"></a>

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

## 6.4.4. Enable/Disable debugging <a href="#_enable_disable_debugging" id="_enable_disable_debugging"></a>

You can enable verbose syslog messages with:

```text
echo "1" >/etc/pve/.debug
```

And disable verbose syslog messages with:

```text
echo "0" >/etc/pve/.debug
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
