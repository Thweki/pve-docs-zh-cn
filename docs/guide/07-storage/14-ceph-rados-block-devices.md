# 7.14. Ceph RADOS Block Devices (RBD) <a href="#ceph_rados_block_devices" id="ceph_rados_block_devices"></a>

Storage pool type: `rbd`

[Ceph](https://ceph.com) is a distributed object store and file system designed to provide excellent performance, reliability and scalability. RADOS block devices implement a feature rich block level storage, and you get the following advantages:

- thin provisioning
- resizable volumes
- distributed and redundant (striped over multiple OSDs)
- full snapshot and clone capabilities
- self healing
- no single point of failure
- scalable to the exabyte level
- kernel and user space implementation available

{% hint style="info" %}
For smaller deployments, it is also possible to run Ceph services directly on your Proxmox VE nodes. Recent hardware has plenty of CPU power and RAM, so running storage services and VMs on same node is possible.
{% endhint %}

## 7.14.1. Configuration <a href="#storage_rbd_config" id="storage_rbd_config"></a>

This backend supports the common storage properties `nodes`, `disable`, `content`, and the following `rbd` specific properties:

**monhost**

List of monitor daemon IPs. Optional, only needed if Ceph is not running on the Proxmox VE cluster. With `monhost` set, Proxmox VE treats the cluster as external and keeps a separate key copy for this storage, even if the monitors belong to the Ceph cluster of this Proxmox VE cluster.

**pool**

Ceph pool name.

**username**

Ceph client ID. Optional, defaults to `admin`. Use only the ID without the `client.` prefix.

**krbd**

Enforce access to rados block devices through the krbd kernel module. Optional.

{% hint style="info" %}
Containers will use `krbd` independent of the option value.
{% endhint %}

**Configuration Example for an external Ceph cluster (`/etc/pve/storage.cfg`)**

```text
rbd: ceph-external
        monhost 10.1.1.20 10.1.1.21 10.1.1.22
        pool ceph-external
        content images
        username pve-rbd
```

{% hint style="success" %}
You can use the `rbd` utility to do low-level management tasks.
{% endhint %}

## 7.14.2. Authentication <a href="#storage_rbd_auth" id="storage_rbd_auth"></a>

{% hint style="info" %}
If Ceph is installed locally on the Proxmox VE cluster, the following is done automatically when adding the storage.
{% endhint %}

If you use `cephx` authentication, which is enabled by default, provide a keyring from the external Ceph cluster. Obtain or create a dedicated identity with only the capabilities required for this storage, as described in Ceph User Management.<a id="_footnote_cephusermgmt"></a>  
[[Ceph User Management](https://docs.ceph.com/en/tentacle/rados/operations/user-management/)]  
 The example below uses `client.pve-rbd`; do not copy `client.admin` to a storage client.

Copy the keyring to one Proxmox VE node:

```text
# scp <external-ceph-server>:/etc/ceph/ceph.client.pve-rbd.keyring /root/rbd.keyring
```

Then pass that file and the identity without its `client.` prefix to `pvesm`:

```text
# pvesm add rbd <name> --monhost "10.1.1.20 10.1.1.21 10.1.1.22" \
    --pool ceph-external --content images --username pve-rbd \
    --keyring /root/rbd.keyring
```

After `pvesm` succeeds, remove `/root/rbd.keyring` because it contains the key in plain text.

When configuring an external RBD storage via the GUI, you can copy and paste the keyring into the appropriate field.

The keyring will be stored at

```text
# /etc/pve/priv/ceph/<STORAGE_ID>.keyring
```

If the external cluster rotates this identity, replace the stored keyring before refreshing its consumers. The local cephx migration helper never rotates keys of external clusters.

## 7.14.3. Ceph client configuration (optional) <a href="#_ceph_client_configuration_optional" id="_ceph_client_configuration_optional"></a>

Connecting to an external Ceph storage doesn’t always allow setting client-specific options in the config DB on the external cluster. You can add a `ceph.conf` beside the Ceph keyring to change the Ceph client configuration for the storage.

The ceph.conf needs to have the same name as the storage.

```text
# /etc/pve/priv/ceph/<STORAGE_ID>.conf
```

See the RBD configuration reference   
[RBD configuration reference [https://docs.ceph.com/en/tentacle/rbd/rbd-config-ref/](https://docs.ceph.com/en/tentacle/rbd/rbd-config-ref/)]  
 for possible settings.

{% hint style="info" %}
Do not change these settings lightly. Proxmox VE is merging the <STORAGE_ID>.conf with the storage configuration.
{% endhint %}

## 7.14.4. Storage Features <a href="#_storage_features_10" id="_storage_features_10"></a>

The `rbd` backend is a block level storage, and implements full snapshot and clone functionality.

<table>
<caption>Table 13. Storage features for backend <code>rbd</code></caption>





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
<td><p>images rootdir</p></td>
<td><p>raw</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
