# 8.13. CephFS <a href="#pveceph_fs" id="pveceph_fs"></a>

Ceph also provides a filesystem, which runs on top of the same object storage as RADOS block devices do. A **M**eta**d**ata **S**erver (`MDS`) is used to map the RADOS backed objects to files and directories, allowing Ceph to provide a POSIX-compliant, replicated filesystem. This allows you to easily configure a clustered, highly available, shared filesystem. Ceph’s Metadata Servers guarantee that files are evenly distributed over the entire Ceph cluster. As a result, even cases of high load will not overwhelm a single host, which can be an issue with traditional shared filesystem approaches, for example `NFS`.

[![screenshot/gui-node-ceph-cephfs-panel.png](../../assets/screenshot-gui-node-ceph-cephfs-panel-png-51eb3988f01e.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-cephfs-panel.png)

Proxmox VE supports both creating a hyper-converged CephFS and using an existing [CephFS as storage](../07-storage/15-storage-cephfs.md#storage_cephfs) to save backups, ISO files, and container templates.

## 8.13.1. Metadata Server (MDS) <a href="#pveceph_fs_mds" id="pveceph_fs_mds"></a>

CephFS needs at least one Metadata Server to be configured and running, in order to function. You can create an MDS through the Proxmox VE web GUI’s `Node
-> CephFS` panel or from the command line with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mds create
```

Multiple metadata servers can be created in a cluster, but with the default settings, only one can be active at a time. If an MDS or its node becomes unresponsive (or crashes), another `standby` MDS will get promoted to `active`. You can speed up the handover between the active and standby MDS by using the *hotstandby* parameter option on creation, or if you have already created it you may set/add:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
mds standby replay = true
```

in the respective MDS section of `/etc/pve/ceph.conf`. With this enabled, the specified MDS will remain in a `warm` state, polling the active one, so that it can take over faster in case of any issues.

{% hint style="info" %}
This active polling will have an additional performance impact on your system and the active `MDS`.
{% endhint %}

**Multiple Active MDS**

Since Luminous (12.2.x) you can have multiple active metadata servers running at once, but this is normally only useful if you have a high amount of clients running in parallel. Otherwise the `MDS` is rarely the bottleneck in a system. If you want to set this up, please refer to the Ceph documentation.   
\[Configuring multiple active MDS daemons [https://docs.ceph.com/en/tentacle/cephfs/multimds/](https://docs.ceph.com/en/tentacle/cephfs/multimds/)\]

## 8.13.2. Create CephFS <a href="#pveceph_fs_create" id="pveceph_fs_create"></a>

With Proxmox VE’s integration of CephFS, you can easily create a CephFS using the web interface, CLI or an external API interface. Some prerequisites are required for this to work:

**Prerequisites for a successful CephFS setup:**

- [Install Ceph packages](04-pve-ceph-install-wizard.md#pve_ceph_install) \- if this was already done some time ago, you may want to rerun it on an up-to-date system to ensure that all CephFS related packages get installed.
- [Setup Monitors](05-pve-ceph-monitors.md#pve_ceph_monitors)
- [Setup your OSDs](05-pve-ceph-monitors.md#pve_ceph_monitors)
- [Setup at least one MDS](#pveceph_fs_mds)

After this is complete, you can simply create a CephFS through either the Web GUI’s `Node -> CephFS` panel or the command-line tool `pveceph`, for example:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph fs create --pg_num 128 --add-storage
```

This creates a CephFS named *cephfs*, using a pool for its data named *cephfs\_data* with *128* placement groups and a pool for its metadata named *cephfs\_metadata* with one quarter of the data pool’s placement groups (`32`). Check the [Proxmox VE managed Ceph pool chapter](09-pve-ceph-pools.md#pve_ceph_pools) or visit the Ceph documentation for more information regarding an appropriate placement group number (`pg_num`) for your setup   
[\[placement\_groups\]](09-pve-ceph-pools.md#_footnote_placement_groups)  
. Additionally, the *--add-storage* parameter will add the CephFS to the Proxmox VE storage configuration after it has been created successfully.

## 8.13.3. Destroy CephFS <a href="#_destroy_cephfs" id="_destroy_cephfs"></a>

{% hint style="warning" %}
Destroying a CephFS will render all of its data unusable. This cannot be undone!
{% endhint %}

To completely and gracefully remove a CephFS, the following steps are necessary:

- Disconnect every non-Proxmox VE client (e.g. unmount the CephFS in guests).
- Disable all related CephFS Proxmox VE storage entries (to prevent it from being automatically mounted).
- Remove all used resources from guests (e.g. ISOs) that are on the CephFS you want to destroy.
- Unmount the CephFS storages on all cluster nodes manually with

  Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

  ```text
  umount /mnt/pve/<STORAGE-NAME>
  ```

  Where `<STORAGE-NAME>` is the name of the CephFS storage in your Proxmox VE.
- Now make sure that no metadata server (`MDS`) is running for that CephFS, either by stopping or destroying them. This can be done through the web interface or via the command-line interface, for the latter you would issue the following command:

  Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

  ```text
  pveceph stop --service mds.NAME
  ```

  to stop them, or

  Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

  ```text
  pveceph mds destroy NAME
  ```

  to destroy them.

  Note that standby servers will automatically be promoted to active when an active `MDS` is stopped or removed, so it is best to first stop all standby servers.
- Now you can destroy the CephFS with

  Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

  ```text
  pveceph fs destroy NAME --remove-storages --remove-pools
  ```

  This will automatically destroy the underlying Ceph pools as well as remove the storages from pve config.

After these steps, the CephFS should be completely removed and if you have other CephFS instances, the stopped metadata servers can be started again to act as standbys.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
