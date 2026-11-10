# 8.11. Cephx Authentication <a href="#pveceph_cephx_how_it_works" id="pveceph_cephx_how_it_works"></a>

Cephx   
[Cephx authorization and authentication protocol [https://docs.ceph.com/en/tentacle/dev/cephx_protocol/](https://docs.ceph.com/en/tentacle/dev/cephx_protocol/)]  
 protects access to a Ceph cluster.

Every Ceph service and client, including storage consumers and tools, authenticates to a monitor as a Ceph user, such as `client.admin` or `osd.3`, with that user’s long-term secret key. The monitor then issues temporary credentials called tickets:

<table>


<thead>
<tr>
<th>Term</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>User key</p></td>
<td><p>Long-term secret used by a client or Ceph service to authenticate to a monitor.</p></td>
</tr>
<tr>
<td><p>Monitor ticket</p></td>
<td><p>Lets an authenticated Ceph user request tickets for Ceph services.</p></td>
</tr>
<tr>
<td><p>Service ticket</p></td>
<td><p>Grants temporary access to an OSD, manager, or metadata server.</p></td>
</tr>
<tr>
<td><p>Rotating service key</p></td>
<td><p>Lets Ceph services validate service tickets. Monitors replace these keys automatically.</p></td>
</tr>
</tbody>
</table>

A running client usually reads its user key only when it starts. Updating a saved key or keyring file does not update that process. Existing tickets and connections can also remain usable for some time. A key rotation must therefore account for running and temporarily disconnected clients.

## 8.11.1. Keyring Locations <a href="#pveceph_keyrings" id="pveceph_keyrings"></a>

The authoritative `client.admin` keyring in a Proxmox VE Ceph cluster is `/etc/pve/priv/ceph.client.admin.keyring`, not the copy in `/etc/ceph`. The [Proxmox cluster file system (pmxcfs)](../06-pmxcfs/README.md#chapter_pmxcfs) synchronizes it to every node. Credentials for managed Ceph storages are below `/etc/pve/priv/ceph/`.

Keyrings below `/var/lib/ceph` belong to one Ceph service and are local to its node. `/etc/pve/priv/ceph.mon.keyring` contains both the shared `mon.` key and `client.admin`. Always merge updates into this file instead of overwriting it. `pveceph mon create` uses its `mon.` entry when it initializes a monitor.

## 8.11.2. Encrypted OSD Lockbox Keys <a href="#pveceph_cephx_lockbox" id="pveceph_cephx_lockbox"></a>

Each encrypted OSD uses a dedicated Ceph user named `client.osd-lockbox.<UUID>`. Its authentication key is called the lockbox key. It is not the disk-encryption key itself: it lets the OSD retrieve that key from Ceph and unlock its storage when it starts. Ceph and the OSD’s block device must contain matching copies of the lockbox key.

{% hint style="warning" %}
Never rotate a lockbox key with `ceph auth` alone. Use the migration helper, which verifies the OSD identity and updates both copies together.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
