# 22.6. **pveceph** \- Manage CEPH Services on Proxmox VE Nodes <a href="#_strong_pveceph_strong_manage_ceph_services_on_proxmox_ve_nodes" id="_strong_pveceph_strong_manage_ceph_services_on_proxmox_ve_nodes"></a>

<a id="cli_pveceph"></a>



**pveceph** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pveceph_auth_status"></a>



**pveceph auth status** `[FORMAT_OPTIONS]`

Show cephx key ciphers and aes256k migration prerequisites.

<a id="cli_pveceph_createmgr"></a>



**pveceph createmgr**

An alias for *pveceph mgr create*.

<a id="cli_pveceph_createmon"></a>



**pveceph createmon**

An alias for *pveceph mon create*.

<a id="cli_pveceph_createosd"></a>



**pveceph createosd**

An alias for *pveceph osd create*.

<a id="cli_pveceph_createpool"></a>



**pveceph createpool**

An alias for *pveceph pool create*.

<a id="cli_pveceph_destroymgr"></a>



**pveceph destroymgr**

An alias for *pveceph mgr destroy*.

<a id="cli_pveceph_destroymon"></a>



**pveceph destroymon**

An alias for *pveceph mon destroy*.

<a id="cli_pveceph_destroyosd"></a>



**pveceph destroyosd**

An alias for *pveceph osd destroy*.

<a id="cli_pveceph_destroypool"></a>



**pveceph destroypool**

An alias for *pveceph pool destroy*.

<a id="cli_pveceph_fs_create"></a>



**pveceph fs create** `[OPTIONS]`

Create a Ceph filesystem

**`--add-storage` `<boolean>` (*default \=* `0`)**

Configure the created CephFS as storage for this cluster.

**`--name` `(?^:^[^:/\s]+$)` (*default \=* `cephfs`)**

The ceph filesystem name.

**`--pg_num` `<integer> (8 - 32768)` (*default \=* `128`)**

Number of placement groups for the backing data pool. The metadata pool will use a quarter of this.

<a id="cli_pveceph_fs_destroy"></a>



**pveceph fs destroy** `<name>` `[OPTIONS]`

Destroy a Ceph filesystem. Refuses if any PVE storage entry of type *cephfs* still references the filesystem and is not disabled. Optionally also removes the storage entries and/or the underlying metadata and data pools.

**`<name>`: `<string>`**

The Ceph filesystem name.

**`--remove-pools` `<boolean>` (*default \=* `0`)**

Remove the metadata and data pools used by this filesystem.

**`--remove-storages` `<boolean>` (*default \=* `0`)**

Remove pveceph-managed storages configured for this filesystem.

<a id="cli_pveceph_help"></a>



**pveceph help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pveceph_init"></a>



**pveceph init** `[OPTIONS]`

Create the initial Ceph default configuration and set up symlinks. Idempotent on re-call: if a \[global\] section already exists in ceph.conf, the existing fsid / auth / pool defaults are preserved and most parameters are silently ignored.

**`--cluster-network` `<string>`**

Declare a separate cluster network, OSDs will route heartbeat, object replication and recovery traffic over it

{% hint style="info" %}
Requires option(s): `network`
{% endhint %}

**`--disable_cephx` `<boolean>` (*default \=* `0`)**

Disable cephx authentication.

{% hint style="warning" %}
cephx is a security feature protecting against man-in-the-middle attacks. Only consider disabling cephx if your network is private!
{% endhint %}

**`--min_size` `<integer> (1 - 7)` (*default \=* `2`)**

Minimum number of available replicas per object to allow I/O

**`--network` `<string>`**

Use specific network for all ceph related traffic

**`--pg_bits` `<integer> (6 - 14)` (*default \=* `6`)**

Placement group bits, used to specify the default number of placement groups.

Depreacted. This setting was deprecated in recent Ceph versions.

**`--size` `<integer> (1 - 7)` (*default \=* `3`)**

Targeted number of replicas per object

<a id="cli_pveceph_install"></a>



**pveceph install** `[OPTIONS]`

Install ceph related packages.

**`--allow-experimental` `<boolean>` (*default \=* `0`)**

Allow experimental versions. Use with care!

**`--repository` `<enterprise | manual | no-subscription | test>` (*default \=* `enterprise`)**

Ceph repository to use. The *manual* option will not configure any repositories. Use it if the host cannot access the public repositories, for example if Proxmox Offline Mirror is used. A repository that contains the Ceph packages for the version needs to be manually configured before starting the installation!

**`--version` `<squid | tentacle>` (*default \=* `tentacle`)**

Ceph version to install.

<a id="cli_pveceph_lspools"></a>



**pveceph lspools**

An alias for *pveceph pool ls*.

<a id="cli_pveceph_mds_create"></a>



**pveceph mds create** `[OPTIONS]`

Create Ceph Metadata Server (MDS)

**`--hotstandby` `<boolean>` (*default \=* `0`)**

Determines whether a ceph-mds daemon should poll and replay the log of an active MDS. Faster switch on MDS failure, but needs more idle resources. Deprecated: the setting was removed in Ceph 14.1.1.

**`--name` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` (*default \=* `nodename`)**

The ID for the mds, when omitted the same as the nodename

<a id="cli_pveceph_mds_destroy"></a>



**pveceph mds destroy** `<name>`

Destroy Ceph Metadata Server

**`<name>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

The name (ID) of the mds

<a id="cli_pveceph_mgr_create"></a>



**pveceph mgr create** `[OPTIONS]`

Create Ceph Manager

**`--id` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` (*default \=* `nodename`)**

The ID for the manager, when omitted the same as the nodename.

<a id="cli_pveceph_mgr_destroy"></a>



**pveceph mgr destroy** `<id>`

Destroy Ceph Manager.

**`<id>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

The ID of the manager

<a id="cli_pveceph_mon_create"></a>



**pveceph mon create** `[OPTIONS]`

Create a Ceph Monitor. Also auto-creates a Manager for the first monitor.

**`--mon-address` `<string>`**

Overwrites autodetected monitor IP address(es). Must be in the public network(s) of Ceph.

**`--monid` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` (*default \=* `nodename`)**

The ID for the monitor, when omitted the same as the nodename.

<a id="cli_pveceph_mon_destroy"></a>



**pveceph mon destroy** `<monid>`

Destroy a Ceph Monitor. Refuses to remove the last monitor of the cluster. Does not destroy any Manager on the same node; use

**`<monid>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

Monitor ID

<a id="cli_pveceph_osd_create"></a>



**pveceph osd create** `<dev>` `[OPTIONS]`

Create OSD

**`<dev>`: `<string>`**

Block device name.

**`--crush-device-class` `<string>`**

Set the device class of the OSD in crush.

**`--db_dev` `<string>`**

Block device name for block.db.

**`--db_dev_size` `<number> (1 - N)`**

Size in GiB for block.db.

{% hint style="info" %}
Requires option(s): `db_dev`
{% endhint %}

**`--encrypted` `<boolean>` (*default \=* `0`)**

Enables encryption of the OSD.

**`--osds-per-device` `<integer> (1 - N)`**

OSD services per physical device. Only useful for fast NVMe devices to utilize their performance better. Mutually exclusive with *db\_dev* and *wal\_dev*.

**`--wal_dev` `<string>`**

Block device name for block.wal.

**`--wal_dev_size` `<number> (0.5 - N)`**

Size in GiB for block.wal.

{% hint style="info" %}
Requires option(s): `wal_dev`
{% endhint %}

<a id="cli_pveceph_osd_destroy"></a>



**pveceph osd destroy** `<osdid>` `[OPTIONS]`

Destroy OSD

**`<osdid>`: `<integer>`**

OSD ID

**`--cleanup` `<boolean>` (*default \=* `0`)**

If set, also destroy the underlying logical volumes via *ceph-volume lvm zap --destroy*, remove the volume group’s physical volume with pvremove, and wipe any journal/block.db/block.wal partitions left over from filestore OSDs. Without this flag the LVs and partitions are left intact for inspection.

<a id="cli_pveceph_osd_details"></a>



**pveceph osd details** `<osdid>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Get OSD details.

**`<osdid>`: `<string>`**

ID of the OSD

**`--verbose` `<boolean>` (*default \=* `0`)**

Print verbose information, same as json-pretty output format.

<a id="cli_pveceph_pool_create"></a>



**pveceph pool create** `<name>` `[OPTIONS]`

Create Ceph pool

**`<name>`: `(?^:^[^:/\s]+$)`**

The name of the pool. It must be unique.

**`--add_storages` `<boolean>` (*default \=* `0`)**

Configure VM and CT storage using the new pool. Defaults to false for replicated pools and to true for erasure-coded pools (since EC pools are typically only useful when wired up to storage).

**`--application` `<cephfs | rbd | rgw>` (*default \=* `rbd`)**

The application of the pool.

**`--crush_rule` `<string>`**

The rule to use for mapping object placement in the cluster.

**`--erasure-coding` `k=<integer> ,m=<integer> [,device-class=<class>] [,failure-domain=<domain>] [,profile=<profile>]`**

Create an erasure coded pool for RBD with an accompaning replicated pool for metadata storage. With EC, the common ceph options *size*, *min\_size* and *crush\_rule* parameters will be applied to the metadata pool.

**`--min_size` `<integer> (1 - 7)` (*default \=* `2`)**

Minimum number of replicas per object

**`--pg_autoscale_mode` `<off | on | warn>` (*default \=* `warn`)**

The automatic PG scaling mode of the pool.

**`--pg_num` `<integer> (1 - 32768)` (*default \=* `128`)**

Number of placement groups.

**`--pg_num_min` `<integer> (-N - 32768)`**

Minimal number of placement groups.

**`--size` `<integer> (1 - 7)` (*default \=* `3`)**

Number of replicas per object

**`--target_size` `^(\d+(\.\d+)?)([KMGT])?$`**

The estimated target size of the pool for the PG autoscaler.

**`--target_size_ratio` `<number>`**

The estimated target ratio of the pool for the PG autoscaler.

<a id="cli_pveceph_pool_destroy"></a>



**pveceph pool destroy** `<name>` `[OPTIONS]`

Destroy pool

**`<name>`: `<string>`**

The name of the pool. It must be unique.

**`--force` `<boolean>` (*default \=* `0`)**

If true, destroys pool even if in use

**`--remove_ecprofile` `<boolean>` (*default \=* `1`)**

Remove the erasure code profile. Defaults to true, if applicable.

**`--remove_storages` `<boolean>` (*default \=* `0`)**

Remove all pveceph-managed storages configured for this pool

<a id="cli_pveceph_pool_get"></a>



**pveceph pool get** `<name>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Show the current pool status.

**`<name>`: `<string>`**

The name of the pool. It must be unique.

**`--verbose` `<boolean>` (*default \=* `0`)**

If enabled, will display additional data(eg. statistics).

<a id="cli_pveceph_pool_ls"></a>



**pveceph pool ls** `[FORMAT_OPTIONS]`

List all pools and their settings (which are settable by the POST/PUT endpoints).

<a id="cli_pveceph_pool_set"></a>



**pveceph pool set** `<name>` `[OPTIONS]`

Change POOL settings

**`<name>`: `(?^:^[^:/\s]+$)`**

The name of the pool. It must be unique.

**`--application` `<cephfs | rbd | rgw>`**

The application of the pool.

**`--crush_rule` `<string>`**

The rule to use for mapping object placement in the cluster.

**`--min_size` `<integer> (1 - 7)`**

Minimum number of replicas per object

**`--pg_autoscale_mode` `<off | on | warn>`**

The automatic PG scaling mode of the pool.

**`--pg_num` `<integer> (1 - 32768)`**

Number of placement groups.

**`--pg_num_min` `<integer> (-N - 32768)`**

Minimal number of placement groups.

**`--size` `<integer> (1 - 7)`**

Number of replicas per object

**`--target_size` `^(\d+(\.\d+)?)([KMGT])?$`**

The estimated target size of the pool for the PG autoscaler.

**`--target_size_ratio` `<number>`**

The estimated target ratio of the pool for the PG autoscaler.

<a id="cli_pveceph_purge"></a>



**pveceph purge** `[OPTIONS]`

Destroy ceph related data and configuration files.

**`--crash` `<boolean>`**

Additionally purge Ceph crash logs, /var/lib/ceph/crash.

**`--logs` `<boolean>`**

Additionally purge Ceph logs, /var/log/ceph.

<a id="cli_pveceph_start"></a>



**pveceph start** `[OPTIONS]`

Start ceph services.

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` (*default \=* `ceph.target`)**

Ceph service name.

<a id="cli_pveceph_status"></a>



**pveceph status**

Get Ceph Status.

<a id="cli_pveceph_stop"></a>



**pveceph stop** `[OPTIONS]`

Stop ceph services.

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` (*default \=* `ceph.target`)**

Ceph service name.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
