# 7.17. ZFS over ISCSI Backend <a href="#storage_zfs" id="storage_zfs"></a>

Storage pool type: `zfs`

This backend accesses a remote machine having a ZFS pool as storage and an iSCSI target implementation via `ssh`. For each guest disk it creates a ZVOL and, exports it as iSCSI LUN. This LUN is used by Proxmox VE for the guest disk.

The following iSCSI target implementations are supported:

- LIO (Linux)
- IET (Linux)
- ISTGT (FreeBSD)
- Comstar (Solaris)

{% hint style="info" %}
This plugin needs a ZFS capable remote storage appliance, you cannot use it to create a ZFS Pool on a regular Storage Appliance/SAN
{% endhint %}

## 7.17.1. Configuration <a href="#_configuration_11" id="_configuration_11"></a>

In order to use the ZFS over iSCSI plugin you need to configure the remote machine (target) to accept `ssh` connections from the Proxmox VE node. Proxmox VE connects to the target for creating the ZVOLs and exporting them via iSCSI. Authentication is done through a ssh-key (without password protection) stored in `/etc/pve/priv/zfs/<target_ip>_id_rsa`

The following steps create a ssh-key and distribute it to the storage machine with IP 192.0.2.1:

```text
mkdir /etc/pve/priv/zfs
ssh-keygen -f /etc/pve/priv/zfs/192.0.2.1_id_rsa
ssh-copy-id -i /etc/pve/priv/zfs/192.0.2.1_id_rsa.pub root@192.0.2.1
ssh -i /etc/pve/priv/zfs/192.0.2.1_id_rsa root@192.0.2.1
```

The backend supports the common storage properties `content`, `nodes`, `disable`, and the following ZFS over ISCSI specific properties:

**pool**

The ZFS pool/filesystem on the iSCSI target. All allocations are done within that pool.

**portal**

iSCSI portal (IP or DNS name with optional port).

**target**

iSCSI target.

**iscsiprovider**

The iSCSI target implementation used on the remote machine

**comstar_tg**

target group for comstar views.

**comstar_hg**

host group for comstar views.

**lio_tpg**

target portal group for Linux LIO targets

**nowritecache**

disable write caching on the target

**blocksize**

Set ZFS blocksize parameter.

**sparse**

Use ZFS thin-provisioning. A sparse volume is a volume whose reservation is not equal to the volume size.

**Configuration Examples (`/etc/pve/storage.cfg`)**

```text
zfs: lio
   blocksize 4k
   iscsiprovider LIO
   pool tank
   portal 192.0.2.111
   target iqn.2003-01.org.linux-iscsi.lio.x8664:sn.xxxxxxxxxxxx
   content images
   lio_tpg tpg1
   sparse 1

zfs: solaris
   blocksize 4k
   target iqn.2010-08.org.illumos:02:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:tank1
   pool tank
   iscsiprovider comstar
   portal 192.0.2.112
   content images

zfs: freebsd
   blocksize 4k
   target iqn.2007-09.jp.ne.peach.istgt:tank1
   pool tank
   iscsiprovider istgt
   portal 192.0.2.113
   content images

zfs: iet
   blocksize 4k
   target iqn.2001-04.com.example:tank1
   pool tank
   iscsiprovider iet
   portal 192.0.2.114
   content images
```

## 7.17.2. Storage Features <a href="#_storage_features_12" id="_storage_features_12"></a>

The ZFS over iSCSI plugin provides a shared storage, which is capable of snapshots. You need to make sure that the ZFS appliance does not become a single point of failure in your deployment.

<table>
<caption>Table 15. Storage features for backend <code>iscsi</code></caption>





<thead>
<tr>
<th>Content types</th>
<th>Image formats</th>
<th>Shared</th>
<th>Snapshots</th>
<th>Clones</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images</p></td>
<td><p>raw</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
<td><p>no</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
