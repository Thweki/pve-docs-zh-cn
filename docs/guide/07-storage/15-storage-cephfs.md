# 7.15. Ceph Filesystem (CephFS) <a href="#storage_cephfs" id="storage_cephfs"></a>

Storage pool type: `cephfs`

CephFS implements a POSIX-compliant filesystem, using a [Ceph](https://ceph.com) storage cluster to store its data. As CephFS builds upon Ceph, it shares most of its properties. This includes redundancy, scalability, self-healing, and high availability.

{% hint style="success" %}
Proxmox VE can [manage Ceph setups](../08-pveceph/README.md#chapter_pveceph), which makes configuring a CephFS storage easier. As modern hardware offers a lot of processing power and RAM, running storage services and VMs on same node is possible without a significant performance impact.
{% endhint %}

To use the CephFS storage plugin, you must replace the stock Debian Ceph client, by adding our [Ceph repository](../03-system-administration/01-sysadmin-package-repositories.md#sysadmin_package_repositories_ceph). Once added, run `apt update`, followed by `apt dist-upgrade`, in order to get the newest packages.

{% hint style="warning" %}
Please ensure that there are no other Ceph repositories configured. Otherwise the installation will fail or there will be mixed package versions on the node, leading to unexpected behavior.
{% endhint %}

## 7.15.1. Configuration <a href="#storage_cephfs_config" id="storage_cephfs_config"></a>

This backend supports the common storage properties `nodes`, `disable`, `content`, as well as the following `cephfs` specific properties:

**fs-name**

Name of the Ceph FS.

**monhost**

List of monitor daemon addresses. Optional, only needed if Ceph is not running on the Proxmox VE cluster. With `monhost` set, Proxmox VE treats the cluster as external and keeps a separate key copy for this storage, even if the monitors belong to the Ceph cluster of this Proxmox VE cluster.

**path**

The local mount point. Optional, defaults to `/mnt/pve/<STORAGE_ID>/`.

**username**

Ceph client ID. Optional, defaults to `admin`. Use only the ID without the `client.` prefix.

**subdir**

CephFS subdirectory to mount. Optional, defaults to `/`.

**fuse**

Access CephFS through FUSE, instead of the kernel client. Optional, defaults to `0`.

**Configuration example for an external Ceph cluster (`/etc/pve/storage.cfg`)**

```text
cephfs: cephfs-external
        monhost 10.1.1.20 10.1.1.21 10.1.1.22
        path /mnt/pve/cephfs-external
        content backup
        username pve-cephfs
        fs-name cephfs
```

{% hint style="info" %}
Don’t forget to set up the client’s secret key file, if cephx was not disabled.
{% endhint %}

## 7.15.2. Authentication <a href="#storage_cephfs_auth" id="storage_cephfs_auth"></a>

{% hint style="info" %}
If Ceph is installed locally on the Proxmox VE cluster, the following is done automatically when adding the storage.
{% endhint %}

If you use `cephx` authentication, which is enabled by default, provide the secret of a dedicated identity with only the capabilities required for this storage. Obtain or create the identity as described in Ceph User Management.  
[\[cephusermgmt\]](14-ceph-rados-block-devices.md#_footnote_cephusermgmt)  
 The example below uses `client.pve-cephfs`; do not use `client.admin` for a storage client.

Export the bare key through SSH to one Proxmox VE node:

```text
# ssh root@<external-ceph-server> \
    'ceph auth get-key client.pve-cephfs' > /root/cephfs.secret
```

Then pass that file and the identity without its `client.` prefix to `pvesm`:

```text
# pvesm add cephfs <name> --monhost "10.1.1.20 10.1.1.21 10.1.1.22" \
    --fs-name cephfs --content backup --username pve-cephfs \
    --keyring /root/cephfs.secret
```

After `pvesm` succeeds, remove `/root/cephfs.secret` because it contains the key in plain text.

When configuring an external CephFS storage in the web interface, paste the secret into the appropriate field. CephFS uses the bare key, not the RBD keyring format with a `[client.<USER>]` section. Proxmox VE stores the secret at `/etc/pve/priv/ceph/<STORAGE_ID>.secret`.

If the external cluster rotates this identity, replace the stored secret before remounting the storage. The local cephx migration helper never rotates keys of external clusters.

## 7.15.3. Storage Features <a href="#_storage_features_11" id="_storage_features_11"></a>

The `cephfs` backend is a POSIX-compliant filesystem, on top of a Ceph cluster.

<table>
<caption>Table 14. Storage features for backend <code>cephfs</code></caption>





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
<td><p>vztmpl iso backup snippets</p></td>
<td><p>none</p></td>
<td><p>yes</p></td>
<td><p>yes<sup>[1]</sup></p></td>
<td><p>no</p></td>
</tr>
</tbody>
</table>

\[1\] While no known bugs exist, snapshots are not yet guaranteed to be stable, as they lack sufficient testing.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
