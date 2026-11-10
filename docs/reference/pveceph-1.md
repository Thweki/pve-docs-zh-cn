# pveceph(1)

## 名称 <a href="#chapter_pveceph" id="chapter_pveceph"></a>

pveceph - Manage Ceph Services on Proxmox VE Nodes

## 概要 <a href="#_synopsis" id="_synopsis"></a>

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

**`--add-storage` `<boolean>` (*default =* `0`)**

Configure the created CephFS as storage for this cluster.

**`--name` `(?^:^[^:/\s]+$)` (*default =* `cephfs`)**

The ceph filesystem name.

**`--pg_num` `<integer> (8 - 32768)` (*default =* `128`)**

Number of placement groups for the backing data pool. The metadata pool will use a quarter of this.

<a id="cli_pveceph_fs_destroy"></a>



**pveceph fs destroy** `<name>` `[OPTIONS]`

Destroy a Ceph filesystem. Refuses if any PVE storage entry of type *cephfs* still references the filesystem and is not disabled. Optionally also removes the storage entries and/or the underlying metadata and data pools.

**`<name>`: `<string>`**

The Ceph filesystem name.

**`--remove-pools` `<boolean>` (*default =* `0`)**

Remove the metadata and data pools used by this filesystem.

**`--remove-storages` `<boolean>` (*default =* `0`)**

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

Create the initial Ceph default configuration and set up symlinks. Idempotent on re-call: if a [global] section already exists in ceph.conf, the existing fsid / auth / pool defaults are preserved and most parameters are silently ignored.

**`--cluster-network` `<string>`**

Declare a separate cluster network, OSDs will route heartbeat, object replication and recovery traffic over it

{% hint style="info" %}
Requires option(s): `network`
{% endhint %}

**`--disable_cephx` `<boolean>` (*default =* `0`)**

Disable cephx authentication.

{% hint style="warning" %}
cephx is a security feature protecting against man-in-the-middle attacks. Only consider disabling cephx if your network is private!
{% endhint %}

**`--min_size` `<integer> (1 - 7)` (*default =* `2`)**

Minimum number of available replicas per object to allow I/O

**`--network` `<string>`**

Use specific network for all ceph related traffic

**`--pg_bits` `<integer> (6 - 14)` (*default =* `6`)**

Placement group bits, used to specify the default number of placement groups.

Depreacted. This setting was deprecated in recent Ceph versions.

**`--size` `<integer> (1 - 7)` (*default =* `3`)**

Targeted number of replicas per object

<a id="cli_pveceph_install"></a>



**pveceph install** `[OPTIONS]`

Install ceph related packages.

**`--allow-experimental` `<boolean>` (*default =* `0`)**

Allow experimental versions. Use with care!

**`--repository` `<enterprise | manual | no-subscription | test>` (*default =* `enterprise`)**

Ceph repository to use. The *manual* option will not configure any repositories. Use it if the host cannot access the public repositories, for example if Proxmox Offline Mirror is used. A repository that contains the Ceph packages for the version needs to be manually configured before starting the installation!

**`--version` `<squid | tentacle>` (*default =* `tentacle`)**

Ceph version to install.

<a id="cli_pveceph_lspools"></a>



**pveceph lspools**

An alias for *pveceph pool ls*.

<a id="cli_pveceph_mds_create"></a>



**pveceph mds create** `[OPTIONS]`

Create Ceph Metadata Server (MDS)

**`--hotstandby` `<boolean>` (*default =* `0`)**

Determines whether a ceph-mds daemon should poll and replay the log of an active MDS. Faster switch on MDS failure, but needs more idle resources. Deprecated: the setting was removed in Ceph 14.1.1.

**`--name` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` (*default =* `nodename`)**

The ID for the mds, when omitted the same as the nodename

<a id="cli_pveceph_mds_destroy"></a>



**pveceph mds destroy** `<name>`

Destroy Ceph Metadata Server

**`<name>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

The name (ID) of the mds

<a id="cli_pveceph_mgr_create"></a>



**pveceph mgr create** `[OPTIONS]`

Create Ceph Manager

**`--id` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` (*default =* `nodename`)**

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

**`--monid` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` (*default =* `nodename`)**

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

**`--encrypted` `<boolean>` (*default =* `0`)**

Enables encryption of the OSD.

**`--osds-per-device` `<integer> (1 - N)`**

OSD services per physical device. Only useful for fast NVMe devices to utilize their performance better. Mutually exclusive with *db_dev* and *wal_dev*.

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

**`--cleanup` `<boolean>` (*default =* `0`)**

If set, also destroy the underlying logical volumes via *ceph-volume lvm zap --destroy*, remove the volume group’s physical volume with pvremove, and wipe any journal/block.db/block.wal partitions left over from filestore OSDs. Without this flag the LVs and partitions are left intact for inspection.

<a id="cli_pveceph_osd_details"></a>



**pveceph osd details** `<osdid>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Get OSD details.

**`<osdid>`: `<string>`**

ID of the OSD

**`--verbose` `<boolean>`（*默认值 =* `0`）**

Print verbose information, same as json-pretty output format.

<a id="cli_pveceph_pool_create"></a>



**pveceph pool create** `<name>` `[OPTIONS]`

Create Ceph pool

**`<name>`: `(?^:^[^:/\s]+$)`**

The name of the pool. It must be unique.

**`--add_storages` `<boolean>` (*default =* `0`)**

Configure VM and CT storage using the new pool. Defaults to false for replicated pools and to true for erasure-coded pools (since EC pools are typically only useful when wired up to storage).

**`--application` `<cephfs | rbd | rgw>` (*default =* `rbd`)**

The application of the pool.

**`--crush_rule` `<string>`**

The rule to use for mapping object placement in the cluster.

**`--erasure-coding` `k=<integer> ,m=<integer> [,device-class=<class>] [,failure-domain=<domain>] [,profile=<profile>]`**

Create an erasure coded pool for RBD with an accompaning replicated pool for metadata storage. With EC, the common ceph options *size*, *min_size* and *crush_rule* parameters will be applied to the metadata pool.

**`--min_size` `<integer> (1 - 7)` (*default =* `2`)**

Minimum number of replicas per object

**`--pg_autoscale_mode` `<off | on | warn>` (*default =* `warn`)**

The automatic PG scaling mode of the pool.

**`--pg_num` `<integer> (1 - 32768)` (*default =* `128`)**

Number of placement groups.

**`--pg_num_min` `<integer> (-N - 32768)`**

Minimal number of placement groups.

**`--size` `<integer> (1 - 7)` (*default =* `3`)**

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

**`--force` `<boolean>`（*默认 =* `0`）**

If true, destroys pool even if in use

**`--remove_ecprofile` `<boolean>` (*default =* `1`)**

Remove the erasure code profile. Defaults to true, if applicable.

**`--remove_storages` `<boolean>` (*default =* `0`)**

Remove all pveceph-managed storages configured for this pool

<a id="cli_pveceph_pool_get"></a>



**pveceph pool get** `<name>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Show the current pool status.

**`<name>`: `<string>`**

The name of the pool. It must be unique.

**`--verbose` `<boolean>`（*默认值 =* `0`）**

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

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` (*default =* `ceph.target`)**

Ceph service name.

<a id="cli_pveceph_status"></a>



**pveceph status**

Get Ceph Status.

<a id="cli_pveceph_stop"></a>



**pveceph stop** `[OPTIONS]`

Stop ceph services.

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` (*default =* `ceph.target`)**

Ceph service name.

## 描述 <a href="#_description" id="_description"></a>

[![screenshot/gui-ceph-status-dashboard.png](../assets/screenshot-gui-ceph-status-dashboard-png-35c265732db2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-status-dashboard.png)

Proxmox VE unifies your compute and storage systems, that is, you can use the same physical nodes within a cluster for both computing (processing VMs and containers) and replicated storage. The traditional silos of compute and storage resources can be wrapped up into a single hyper-converged appliance. Separate storage networks (SANs) and connections via network attached storage (NAS) disappear. With the integration of Ceph, an open source software-defined storage platform, Proxmox VE has the ability to run and manage Ceph storage directly on the hypervisor nodes.

Ceph is a distributed object store and file system designed to provide excellent performance, reliability and scalability.

**Some advantages of Ceph on Proxmox VE are:**

- Easy setup and management via CLI and GUI
- Thin provisioning
- Snapshot support
- Self healing
- Scalable to the exabyte level
- Provides block, file system, and object storage
- Setup pools with different performance and redundancy characteristics
- Data is replicated, making it fault tolerant
- Runs on commodity hardware
- No need for hardware RAID controllers
- Open source

For small to medium-sized deployments, it is possible to install a Ceph server for using RADOS Block Devices (RBD) or CephFS directly on your Proxmox VE cluster nodes (see [Ceph RADOS Block Devices (RBD)](pvesm-1.md#ceph_rados_block_devices)). Recent hardware has a lot of CPU power and RAM, so running storage services and virtual guests on the same node is possible.

To simplify management, Proxmox VE provides you native integration to install and manage [Ceph](http://ceph.com) services on Proxmox VE nodes either via the built-in web interface, or using the *pveceph* command line tool.

## Terminology <a href="#_terminology" id="_terminology"></a>

**Ceph consists of multiple Daemons, for use as an RBD storage:**

- Ceph Monitor (ceph-mon, or MON)
- Ceph Manager (ceph-mgr, or MGR)
- Ceph Metadata Service (ceph-mds, or MDS)
- Ceph Object Storage Daemon (ceph-osd, or OSD)

{% hint style="success" %}
We highly recommend to get familiar with Ceph   
[Ceph intro [https://docs.ceph.com/en/tentacle/start/](https://docs.ceph.com/en/tentacle/start/)]  
, its architecture   
[Ceph architecture [https://docs.ceph.com/en/tentacle/architecture/](https://docs.ceph.com/en/tentacle/architecture/)]  
 and vocabulary   
[Ceph glossary [https://docs.ceph.com/en/tentacle/glossary](https://docs.ceph.com/en/tentacle/glossary)]  
.
{% endhint %}

## Recommendations for a Healthy Ceph Cluster <a href="#_recommendations_for_a_healthy_ceph_cluster" id="_recommendations_for_a_healthy_ceph_cluster"></a>

To build a hyper-converged Proxmox + Ceph Cluster, you must use at least three (preferably) identical servers for the setup.

Check also the recommendations from [Ceph’s website](https://docs.ceph.com/en/tentacle/start/hardware-recommendations/).

{% hint style="info" %}
The recommendations below should be seen as a rough guidance for choosing hardware. Therefore, it is still essential to adapt it to your specific needs. You should test your setup and monitor health and performance continuously.
{% endhint %}

<a id="pve_ceph_recommendation_cpu"></a>



**CPU**

Ceph services can be classified into two categories:

- Intensive CPU usage, benefiting from high CPU base frequencies and multiple cores. Members of that category are:

  - Object Storage Daemon (OSD) services
  - Meta Data Service (MDS) used for CephFS
- Moderate CPU usage, not needing multiple CPU cores. These are:

  - Monitor (MON) services
  - Manager (MGR) services

As a simple rule of thumb, you should assign at least one CPU core (or thread) to each Ceph service to provide the minimum resources required for stable and durable Ceph performance.

For example, if you plan to run a Ceph monitor, a Ceph manager and 6 Ceph OSDs services on a node you should reserve 8 CPU cores purely for Ceph when targeting basic and stable performance.

Note that an OSD’s CPU usage depends mostly on the disk’s performance. The higher the possible IOPS (**IO** **O**perations per **S**econd) of a disk, the more CPU can be utilized by an OSD service. For modern enterprise SSD disks, like NVMes that can permanently sustain a high IOPS load over 100’000 with sub millisecond latency, each OSD can use multiple CPU threads, e.g., four to six CPU threads utilized per NVMe backed OSD is likely for very high performance disks.

<a id="pve_ceph_recommendation_memory"></a>



**Memory**

Especially in a hyper-converged setup, the memory consumption needs to be carefully planned out and monitored. In addition to the predicted memory usage of virtual machines and containers, you must also account for having enough memory available for Ceph to provide excellent and stable performance.

While usage may be less under normal conditions, it will consume more memory during critical operations, such as recovery, rebalancing, or backfilling. That means you should avoid maxing out your available memory already on regular operation, but rather leave some headroom to cope with outages.

The current recommendation is to [configure](#pve_ceph_configuration) OSDs with at least **8 GiB of memory** for good performance. The OSD daemon requires 4 GiB by default.

{% hint style="info" %}
Total memory consumption is primarily determined by the number of OSD daemons. However, for critical operations, all Ceph services may require additional memory.
{% endhint %}

<a id="pve_ceph_recommendation_network"></a>



**Network**

We recommend a network bandwidth of at least 10 Gbps, or more, to be used exclusively for Ceph traffic. A meshed network setup   
[Full Mesh Network for Ceph [https://pve.proxmox.com/wiki/Full_Mesh_Network_for_Ceph_Server](https://pve.proxmox.com/wiki/Full_Mesh_Network_for_Ceph_Server)]  
 is also an option for three to five node clusters, if there are no 10+ Gbps switches available.

{% hint style="warning" %}
The volume of traffic, especially during recovery, will interfere with other services on the same network, especially the latency sensitive Proxmox VE corosync cluster stack can be affected, resulting in possible loss of cluster quorum. Moving the Ceph traffic to dedicated and physical separated networks will avoid such interference, not only for corosync, but also for the networking services provided by any virtual guests.
{% endhint %}

For estimating your bandwidth needs, you need to take the performance of your disks into account.. While a single HDD might not saturate a 1 Gb link, multiple HDD OSDs per node can already saturate 10 Gbps too. If modern NVMe-attached SSDs are used, a single one can already saturate 10 Gbps of bandwidth, or more. For such high-performance setups we recommend at least a 25 Gpbs, while even 40 Gbps or 100+ Gbps might be required to utilize the full performance potential of the underlying disks.

If unsure, we recommend using three (physical) separate networks for high-performance setups:

- one very high bandwidth (25+ Gbps) network for Ceph (internal) cluster traffic.
- one high bandwidth (10+ Gpbs) network for Ceph (public) traffic between the ceph server and ceph client storage traffic. Depending on your needs this can also be used to host the virtual guest traffic and the VM live-migration traffic.
- one medium bandwidth (1 Gbps) exclusive for the latency sensitive corosync cluster communication.

If a firewall is enabled you will have to open the ports used by Ceph, the easiest way to do this is to use a firewall `macro`.

<a id="pve_ceph_recommendation_disk"></a>



**Disks**

When planning the size of your Ceph cluster, it is important to take the recovery time into consideration. Especially with small clusters, recovery might take long. It is recommended that you use SSDs instead of HDDs in small setups to reduce recovery time, minimizing the likelihood of a subsequent failure event during recovery.

In general, SSDs will provide more IOPS than spinning disks. With this in mind, in addition to the higher cost, it may make sense to implement a [class based](#pve_ceph_device_classes) separation of pools. Another way to speed up OSDs is to use a faster disk as a journal or DB/**W**rite-**A**head-**L**og device, see [creating Ceph OSDs](#pve_ceph_osds). If a faster disk is used for multiple OSDs, a proper balance between OSD and WAL / DB (or journal) disk must be selected, otherwise the faster disk becomes the bottleneck for all linked OSDs.

Aside from the disk type, Ceph performs best with an evenly sized, and an evenly distributed amount of disks per node. For example, 4 x 500 GB disks within each node is better than a mixed setup with a single 1 TB and three 250 GB disk.

You also need to balance OSD count and single OSD capacity. More capacity allows you to increase storage density, but it also means that a single OSD failure forces Ceph to recover more data at once.

<a id="pve_ceph_recommendation_raid"></a>



**Avoid RAID**

As Ceph handles data object redundancy and multiple parallel writes to disks (OSDs) on its own, using a RAID controller normally doesn’t improve performance or availability. On the contrary, Ceph is designed to handle whole disks on its own, without any abstraction in between. RAID controllers are not designed for the Ceph workload and may complicate things and sometimes even reduce performance, as their write and caching algorithms may interfere with the ones from Ceph.

{% hint style="warning" %}
Avoid RAID controllers. Use host bus adapter (HBA) instead.
{% endhint %}

## Initial Ceph Installation & Configuration <a href="#pve_ceph_install_wizard" id="pve_ceph_install_wizard"></a>

### Using the Web-based Wizard <a href="#_using_the_web_based_wizard" id="_using_the_web_based_wizard"></a>

[![screenshot/gui-node-ceph-install.png](../assets/screenshot-gui-node-ceph-install-png-146fee5f8339.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-install.png)

With Proxmox VE you have the benefit of an easy to use installation wizard for Ceph. Click on one of your cluster nodes and navigate to the Ceph section in the menu tree. If Ceph is not already installed, you will see a prompt offering to do so.

The wizard is divided into multiple sections, where each needs to finish successfully, in order to use Ceph.

First you need to choose which Ceph version you want to install. Prefer the one from your other nodes, or the newest if this is the first node you install Ceph.

After starting the installation, the wizard will download and install all the required packages from Proxmox VE’s Ceph repository.

[![screenshot/gui-node-ceph-install-wizard-step0.png](../assets/screenshot-gui-node-ceph-install-wizard-step0-png-41f18d5b8097.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-install-wizard-step0.png)

After finishing the installation step, you will need to create a configuration. This step is only needed once per cluster, as this configuration is distributed automatically to all remaining cluster members through Proxmox VE’s clustered [configuration file system (pmxcfs)](pmxcfs-8.md#chapter_pmxcfs).

The configuration step includes the following settings:

<a id="pve_ceph_wizard_networks"></a>



- **Public Network:** This network will be used for public storage communication (e.g., for virtual machines using a Ceph RBD backed disk, or a CephFS mount), and communication between the different Ceph services. This setting is required.   
   Separating your Ceph traffic from the Proxmox VE cluster communication (corosync), and possibly the front-facing (public) networks of your virtual guests, is highly recommended. Otherwise, Ceph’s high-bandwidth IO-traffic could cause interference with other low-latency dependent services.
- **Cluster Network:** Specify to separate the [OSD](#pve_ceph_osds) replication and heartbeat traffic as well. This setting is optional.   
   Using a physically separated network is recommended, as it will relieve the Ceph public and the virtual guests network, while also providing a significant Ceph performance improvements.   
   The Ceph cluster network can be configured and moved to another physically separated network at a later time.

[![screenshot/gui-node-ceph-install-wizard-step2.png](../assets/screenshot-gui-node-ceph-install-wizard-step2-png-8fdd1bc317bd.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-install-wizard-step2.png)

You have two more options which are considered advanced and therefore should only be changed if you know what you are doing.

- **Number of replicas**: Defines how often an object is replicated.
- **Minimum replicas**: Defines the minimum number of required replicas for I/O to be marked as complete.

Additionally, you need to choose your first monitor node. This step is required.

That’s it. You should now see a success page as the last step, with further instructions on how to proceed. Your system is now ready to start using Ceph. To get started, you will need to create some additional [monitors](#pve_ceph_monitors), [OSDs](#pve_ceph_osds) and at least one [pool](#pve_ceph_pools).

The rest of this chapter will guide you through getting the most out of your Proxmox VE based Ceph setup. This includes the aforementioned tips and more, such as [CephFS](#pveceph_fs), which is a helpful addition to your new Ceph cluster.

### CLI Installation of Ceph Packages <a href="#pve_ceph_install" id="pve_ceph_install"></a>

Alternatively to the recommended Proxmox VE Ceph installation wizard available in the web interface, you can use the following CLI command on each node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph install
```

This sets up an `apt` package repository in `/etc/apt/sources.list.d/ceph.sources` and installs the required software.

### Initial Ceph configuration via CLI <a href="#_initial_ceph_configuration_via_cli" id="_initial_ceph_configuration_via_cli"></a>

Use the Proxmox VE Ceph installation wizard (recommended) or run the following command on one node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph init --network 10.10.10.0/24
```

This creates an initial configuration at `/etc/pve/ceph.conf` with a dedicated network for Ceph. This file is automatically distributed to all Proxmox VE nodes, using [pmxcfs](pmxcfs-8.md#chapter_pmxcfs). The command also creates a symbolic link at `/etc/ceph/ceph.conf`, which points to that file. Thus, you can simply run Ceph commands without the need to specify a configuration file.

## Ceph Monitor <a href="#pve_ceph_monitors" id="pve_ceph_monitors"></a>

[![screenshot/gui-ceph-monitor.png](../assets/screenshot-gui-ceph-monitor-png-5183f95d9815.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-monitor.png)

The Ceph Monitor (MON)   
[Ceph Monitor [https://docs.ceph.com/en/tentacle/rados/configuration/mon-config-ref/](https://docs.ceph.com/en/tentacle/rados/configuration/mon-config-ref/)]  
 maintains a master copy of the cluster map. For high availability, you need at least 3 monitors. One monitor will already be installed if you used the installation wizard. You won’t need more than 3 monitors, as long as your cluster is small to medium-sized. Only really large clusters will require more than this.

### Create Monitors <a href="#pveceph_create_mon" id="pveceph_create_mon"></a>

On each node where you want to place a monitor (three monitors are recommended), create one by using the *Ceph → Monitor* tab in the GUI or run:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mon create
```

### Destroy Monitors <a href="#pveceph_destroy_mon" id="pveceph_destroy_mon"></a>

To remove a Ceph Monitor via the GUI, first select a node in the tree view and go to the **Ceph → Monitor** panel. Select the MON and click the **Destroy** button.

To remove a Ceph Monitor via the CLI, first connect to the node on which the MON is running. Then execute the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mon destroy
```

{% hint style="info" %}
At least three Monitors are needed for quorum.
{% endhint %}

## Ceph Manager <a href="#pve_ceph_manager" id="pve_ceph_manager"></a>

The Manager daemon runs alongside the monitors. It provides an interface to monitor the cluster. Since the release of Ceph luminous, at least one ceph-mgr   
[Ceph Manager [https://docs.ceph.com/en/tentacle/mgr/](https://docs.ceph.com/en/tentacle/mgr/)]  
 daemon is required.

### Create Manager <a href="#pveceph_create_mgr" id="pveceph_create_mgr"></a>

Multiple Managers can be installed, but only one Manager is active at any given time.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mgr create
```

{% hint style="info" %}
It is recommended to install the Ceph Manager on the monitor nodes. For high availability install more then one manager.
{% endhint %}

### Destroy Manager <a href="#pveceph_destroy_mgr" id="pveceph_destroy_mgr"></a>

To remove a Ceph Manager via the GUI, first select a node in the tree view and go to the **Ceph → Monitor** panel. Select the Manager and click the **Destroy** button.

To remove a Ceph Monitor via the CLI, first connect to the node on which the Manager is running. Then execute the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mgr destroy
```

{% hint style="info" %}
While a manager is not a hard-dependency, it is crucial for a Ceph cluster, as it handles important features like PG-autoscaling, device health monitoring, telemetry and more.
{% endhint %}

## Ceph OSDs <a href="#pve_ceph_osds" id="pve_ceph_osds"></a>

[![screenshot/gui-ceph-osd-status.png](../assets/screenshot-gui-ceph-osd-status-png-eb5fb509c420.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-osd-status.png)

Ceph **O**bject **S**torage **D**aemons store objects for Ceph over the network. It is recommended to use one OSD per physical disk.

### Create OSDs <a href="#pve_ceph_osd_create" id="pve_ceph_osd_create"></a>

You can create an OSD either via the Proxmox VE web interface or via the CLI using `pveceph`. For example:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph osd create /dev/sd[X]
```

{% hint style="success" %}
We recommend a Ceph cluster with at least three nodes and at least 12 OSDs, evenly distributed among the nodes.
{% endhint %}

If the disk was in use before (for example, for ZFS or as an OSD) you first need to zap all traces of that usage. To remove the partition table, boot sector and any other OSD leftover, you can use the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph-volume lvm zap /dev/sd[X] --destroy
```

{% hint style="warning" %}
The above command will destroy all data on the disk!
{% endhint %}

**Ceph Bluestore**

Starting with the Ceph Kraken release, a new Ceph OSD storage type was introduced called Bluestore   
[Ceph Bluestore [https://ceph.com/community/new-luminous-bluestore/](https://ceph.com/community/new-luminous-bluestore/)]  
. This is the default when creating OSDs since Ceph Luminous.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph osd create /dev/sd[X]
```

**Block.db and block.wal**

If you want to use a separate DB/WAL device for your OSDs, you can specify it through the *-db_dev* and *-wal_dev* options. The WAL is placed with the DB, if not specified separately.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph osd create /dev/sd[X] -db_dev /dev/sd[Y] -wal_dev /dev/sd[Z]
```

You can directly choose the size of those with the *-db_size* and *-wal_size* parameters respectively. If they are not given, the following values (in order) will be used:

- bluestore_block_{db,wal}_size from Ceph configuration…

  - … database, section *osd*
  - … database, section *global*
  - … file, section *osd*
  - … file, section *global*
- 10% (DB)/1% (WAL) of OSD size

{% hint style="info" %}
The DB stores BlueStore’s internal metadata, and the WAL is BlueStore’s internal journal or write-ahead log. It is recommended to use a fast SSD or NVRAM for better performance.
{% endhint %}

**Ceph Filestore**

Before Ceph Luminous, Filestore was used as the default storage type for Ceph OSDs. Starting with Ceph Nautilus, Proxmox VE does not support creating such OSDs with *pveceph* anymore. If you still want to create filestore OSDs, use *ceph-volume* directly.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph-volume lvm create --filestore --data /dev/sd[X] --journal /dev/sd[Y]
```

### Destroy OSDs <a href="#pve_ceph_osd_destroy" id="pve_ceph_osd_destroy"></a>

If you experience problems with an OSD or its disk, try to [troubleshoot](#pve_ceph_mon_and_ts) them first to decide if a [replacement](#pve_ceph_osd_replace) is needed.

To destroy an OSD, navigate to the *<Node> → Ceph → OSD* panel or use the mentioned CLI commands on the node where the OSD is located.

1. Make sure the cluster has enough space to handle the removal of the OSD. In the *Ceph → OSD* panel,if the to-be destroyed OSD is still `up` and `in` (non-zero value at `AVAIL`), make sure that all OSDs have their `Used (%)` value well below the `nearfull_ratio` of default `85%`.

   This way you can reduce the risk from the upcoming rebalancing, which may cause OSDs to run full and thereby blocking I/O on Ceph pools.

   Use the following command to get the same information on the CLI:

   Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

   ```text
   ceph osd df tree
   ```
2. If the to-be destroyed OSD is not `out` yet, select the OSD and click on **Out**. This will exclude it from data distribution and start a rebalance.

   The following command does the same:

   Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

   ```text
   ceph osd out <id>
   ```
3. If you can, wait until Ceph has finished the rebalance to always have enough replicas. The OSD will be empty; once it is, it will show *0 PGs*.
4. Click on **Stop**. If stopping is not safe yet, a warning will appear, and you should click on **Cancel**. Try it again in a few moments.

   The following commands can be used to check if it is safe to stop and stop the OSD:

   Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

   ```text
   ceph osd ok-to-stop <id>
   pveceph stop --service osd.<id>
   ```
5. Finally:

   To remove the OSD from Ceph and delete all disk data, first click on **More → Destroy**. Enable the cleanup option to clean up the partition table and other structures. This makes it possible to immediately reuse the disk in Proxmox VE. Then, click on **Remove**.

   The CLI command to destroy the OSD is:

   Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

   ```text
   pveceph osd destroy <id> [--cleanup]
   ```

## Ceph Configuration <a href="#pve_ceph_configuration" id="pve_ceph_configuration"></a>

Ceph daemon and clients pull their configuration from one or more sources   
[Ceph config sources [https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#config-sources](https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#config-sources)]  
. In Proxmox VE, a minimal ceph.conf file is used to hold bootstrap settings. Most of the configuration is held in the central configuration database maintained by the MON services.

To persistently change configuration values use the following commands   
[Ceph MON DB commands [https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#commands](https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#commands)]  
:

<table>


<tbody>
<tr>
<td><p><code>ceph config dump</code></p></td>
<td><p>Show all configuration option(s)</p></td>
</tr>
<tr>
<td><p><code>ceph config get &lt;who&gt; &lt;name&gt;</code></p></td>
<td><p>Show configuration option(s) for an entity</p></td>
</tr>
<tr>
<td><p><code>ceph config set &lt;who&gt; &lt;name&gt; &lt;value&gt;</code></p></td>
<td><p>Set a configuration option for one or more entities</p></td>
</tr>
<tr>
<td><p><code>ceph config rm &lt;who&gt; &lt;name&gt;</code></p></td>
<td><p>Clear a configuration option for one or more entities</p></td>
</tr>
</tbody>
</table>

**Example for increasing the osd_memory_target for all OSD daemons**

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph config set osd osd_memory_target 8G
```

{% hint style="info" %}
If an option exists in a local configuration file, the configuration in the MON DB will be ignored because it has a lower precedence.
{% endhint %}

## Ceph Pools <a href="#pve_ceph_pools" id="pve_ceph_pools"></a>

[![screenshot/gui-ceph-pools.png](../assets/screenshot-gui-ceph-pools-png-4290e2ffb7bf.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-pools.png)

A pool is a logical group for storing objects. It holds a collection of objects, known as **P**lacement **G**roups (`PG`, `pg_num`).

### Create and Edit Pools <a href="#_create_and_edit_pools" id="_create_and_edit_pools"></a>

You can create and edit pools from the command line or the web interface of any Proxmox VE host under **Ceph → Pools**.

When no options are given, we set a default of **128 PGs**, a **size of 3 replicas** and a **min_size of 2 replicas**, to ensure no data loss occurs if any OSD fails.

{% hint style="warning" %}
**Do not set a min_size of 1**. A replicated pool with min_size of 1 allows I/O on an object when it has only 1 replica, which could lead to data loss, incomplete PGs or unfound objects.
{% endhint %}

It is advised that you either enable the PG-Autoscaler or calculate the PG number based on your setup. You can find the formula and the PG calculator   
[PG calculator [https://web.archive.org/web/20210301111112/http://ceph.com/pgcalc/](https://web.archive.org/web/20210301111112/http://ceph.com/pgcalc/)]  
 online. From Ceph Nautilus onward, you can change the number of PGs <a id="_footnote_placement_groups"></a>  
[Placement Groups [https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/](https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/)]  
 after the setup.

The PG autoscaler <a id="_footnote_autoscaler"></a>  
[Automated Scaling [https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/#automated-scaling](https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/#automated-scaling)]  
 can automatically scale the PG count for a pool in the background. Setting the `Target Size` or `Target Ratio` advanced parameters helps the PG-Autoscaler to make better decisions.

**Example for creating a pool over the CLI**

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool create <pool-name> --add_storages
```

{% hint style="success" %}
If you would also like to automatically define a storage for your pool, keep the ‘Add as Storage’ checkbox checked in the web interface, or use the command-line option *--add_storages* at pool creation.
{% endhint %}

#### Pool Options <a href="#_pool_options" id="_pool_options"></a>

[![screenshot/gui-ceph-pool-create.png](../assets/screenshot-gui-ceph-pool-create-png-020d880342d1.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-pool-create.png)

The following options are available on pool creation, and partially also when editing a pool.

**Name**

The name of the pool. This must be unique and can’t be changed afterwards.

**Size**

The number of replicas per object. Ceph always tries to have this many copies of an object. Default: `3`.

**PG Autoscale Mode**

The automatic PG scaling mode   
[[autoscaler]](#_footnote_autoscaler)  
 of the pool. If set to `warn`, it produces a warning message when a pool has a non-optimal PG count. Default: `warn`.

**Add as Storage**

Configure a VM or container storage using the new pool. Default: `true` (only visible on creation).

**Advanced Options**

**Min. Size**

The minimum number of replicas per object. Ceph will reject I/O on the pool if a PG has less than this many replicas. Default: `2`.

**Crush Rule**

The rule to use for mapping object placement in the cluster. These rules define how data is placed within the cluster. See [Ceph CRUSH & device classes](#pve_ceph_device_classes) for information on device-based rules.

**# of PGs**

The number of placement groups   
[[placement_groups]](#_footnote_placement_groups)  
 that the pool should have at the beginning. Default: `128`.

**Target Ratio**

The ratio of data that is expected in the pool. The PG autoscaler uses the ratio relative to other ratio sets. It takes precedence over the `target size` if both are set.

**Target Size**

The estimated amount of data expected in the pool. The PG autoscaler uses this size to estimate the optimal PG count.

**Min. # of PGs**

The minimum number of placement groups. This setting is used to fine-tune the lower bound of the PG count for that pool. The PG autoscaler will not merge PGs below this threshold.

Further information on Ceph pool handling can be found in the Ceph pool operation   
[Ceph pool operation [https://docs.ceph.com/en/tentacle/rados/operations/pools/](https://docs.ceph.com/en/tentacle/rados/operations/pools/)]  
 manual.

### Erasure Coded Pools <a href="#pve_ceph_ec_pools" id="pve_ceph_ec_pools"></a>

Erasure coding (EC) is a form of ‘forward error correction’ codes that allows to recover from a certain amount of data loss. Erasure coded pools can offer more usable space compared to replicated pools, but they do that for the price of performance.

For comparison: in classic, replicated pools, multiple replicas of the data are stored (`size`) while in erasure coded pool, data is split into `k` data chunks with additional `m` coding (checking) chunks. Those coding chunks can be used to recreate data should data chunks be missing.

The number of coding chunks, `m`, defines how many OSDs can be lost without losing any data. The total amount of objects stored is `k + m`.

#### Creating EC Pools <a href="#_creating_ec_pools" id="_creating_ec_pools"></a>

Erasure coded (EC) pools can be created with the `pveceph` CLI tooling. Planning an EC pool needs to account for the fact, that they work differently than replicated pools.

The default `min_size` of an EC pool depends on the `m` parameter. If `m = 1`, the `min_size` of the EC pool will be `k`. The `min_size` will be `k + 1` if `m > 1`. The Ceph documentation recommends a conservative `min_size` of `k + 2`   
[Ceph Erasure Coded Pool Recovery [https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-coded-pool-recovery](https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-coded-pool-recovery)]  
.

If there are less than `min_size` OSDs available, any IO to the pool will be blocked until there are enough OSDs available again.

{% hint style="info" %}
When planning an erasure coded pool, keep an eye on the `min_size` as it defines how many OSDs need to be available. Otherwise, IO will be blocked.
{% endhint %}

For example, an EC pool with `k = 2` and `m = 1` will have `size = 3`, `min_size = 2` and will stay operational if one OSD fails. If the pool is configured with `k = 2`, `m = 2`, it will have a `size = 4` and `min_size = 3` and stay operational if one OSD is lost.

To create a new EC pool, run the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool create <pool-name> --erasure-coding k=2,m=1
```

Optional parameters are `failure-domain` and `device-class`. If you need to change any EC profile settings used by the pool, you will have to create a new pool with a new profile.

This will create a new EC pool plus the needed replicated pool to store the RBD omap and other metadata. In the end, there will be a `<pool name>-data` and `<pool name>-metadata` pool. The default behavior is to create a matching storage configuration as well. If that behavior is not wanted, you can disable it by providing the `--add_storages 0` parameter. When configuring the storage configuration manually, keep in mind that the `data-pool` parameter needs to be set. Only then will the EC pool be used to store the data objects. For example:

{% hint style="info" %}
The optional parameters `--size`, `--min_size` and `--crush_rule` will be used for the replicated metadata pool, but not for the erasure coded data pool. If you need to change the `min_size` on the data pool, you can do it later. The `size` and `crush_rule` parameters cannot be changed on erasure coded pools.
{% endhint %}

If there is a need to further customize the EC profile, you can do so by creating it with the Ceph tools directly   
[Ceph Erasure Code Profile [https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-code-profiles](https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-code-profiles)]  
, and specify the profile to use with the `profile` parameter.

For example:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool create <pool-name> --erasure-coding profile=<profile-name>
```

#### FastEC (`allow_ec_optimizations`) <a href="#_fastec_span_class_monospaced_allow_ec_optimizations_span" id="_fastec_span_class_monospaced_allow_ec_optimizations_span"></a>

Ceph Tentacle introduces a new erasure coding I/O path called FastEC, enabled per pool via the `allow_ec_optimizations` flag. FastEC adds partial reads and partial writes on EC pools, substantially improving small random I/O performance — the dominant access pattern of virtual machine disk I/O. Upstream recommends it for RBD and CephFS backed storage   
[Ceph Erasure Code [https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/](https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/)]  
.

FastEC has four requirements that the Ceph monitor enforces:

- the pool must be erasure coded;
- the cluster must be at `require_osd_release` tentacle or later;
- the erasure code profile must use a plugin and technique combination that supports the optimized EC path:

  <table>



  <thead>
  <tr>
  <th>Plugin</th>
  <th>Technique</th>
  <th>FastEC</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><p><code>isa</code></p></td>
  <td><p><code>reed_sol_van</code></p></td>
  <td><p>yes</p></td>
  </tr>
  <tr>
  <td><p><code>isa</code></p></td>
  <td><p><code>cauchy</code></p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>jerasure</code></p></td>
  <td><p><code>reed_sol_van</code></p></td>
  <td><p>yes</p></td>
  </tr>
  <tr>
  <td><p><code>jerasure</code></p></td>
  <td><p>all others</p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>lrc</code></p></td>
  <td><p>(any)</p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>shec</code></p></td>
  <td><p>(any)</p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>clay</code></p></td>
  <td><p>(any)</p></td>
  <td><p>no</p></td>
  </tr>
  </tbody>
  </table>
- the pool’s stripe unit must be a multiple of 4096 bytes. The default stripe unit satisfies this, so this is only relevant for pools created with a custom `stripe_unit` in their erasure code profile.

If any precondition is not met, `ceph osd pool set <pool>-data allow_ec_optimizations 1` fails with a descriptive error — no silent degradation.

`pveceph` does not set the plugin or technique explicitly when creating an EC profile — both are seeded from the monitor’s `osd_pool_default_erasure_code_profile` option (`reed_sol_van` by default on both Squid and Tentacle). The technique requirement is therefore satisfied out of the box unless the operator has overridden this setting. Verify with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph config get mon osd_pool_default_erasure_code_profile
```

If the output shows a technique other than `reed_sol_van`, either update the cluster-wide default or create a compatible profile explicitly and pass it via the `profile` property when creating the pool (see above).

Check the cluster release with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd dump | grep require_osd_release
```

If this reports a release older than `tentacle`, run `ceph osd require-osd-release tentacle` after all OSDs have been upgraded.

{% hint style="warning" %}
`allow_ec_optimizations` is a one-way switch. Once enabled on a pool, the Ceph monitor refuses to clear the flag again, so rolling back requires draining and recreating the pool. Enable it only after validating that FastEC works for your workload on a test pool.
{% endhint %}

##### Enabling FastEC on a pool <a href="#_enabling_fastec_on_a_pool" id="_enabling_fastec_on_a_pool"></a>

FastEC is enabled per pool via the `ceph` CLI. It can be set on both new and existing (populated) pools. No data migration or re-encoding takes place; only pool metadata changes.

To enable FastEC on a pool, run the following command against the data pool (typically named `<pool-name>-data`):

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd pool set <pool-name>-data allow_ec_optimizations 1
```

Verify the result with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd pool get <pool-name>-data allow_ec_optimizations
```

The same command reports the current state for any EC pool, which is useful when auditing a cluster.

When the flag is set on a populated pool, be aware of the following:

- **Primary re-election.** FastEC marks data shards 1 through k-1 as non-primary, so PGs whose primary was on one of those shards will re-peer. This is a normal peering event and causes a brief I/O pause per affected PG.
- **Scrub interaction.** Re-peering cancels any in-flight scrub on affected PGs. Those PGs will need to be re-scrubbed after peering completes.

#### Adding EC Pools as Storage <a href="#_adding_ec_pools_as_storage" id="_adding_ec_pools_as_storage"></a>

You can add an already existing EC pool as storage to Proxmox VE. It works the same way as adding an `RBD` pool but requires the extra `data-pool` option.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pvesm add rbd <storage-name> --pool <replicated-pool> --data-pool <ec-pool>
```

{% hint style="success" %}
Do not forget to add the `keyring` and `monhost` option for any external Ceph clusters, not managed by the local Proxmox VE cluster.
{% endhint %}

### Destroy Pools <a href="#_destroy_pools" id="_destroy_pools"></a>

To destroy a pool via the GUI, select a node in the tree view and go to the **Ceph → Pools** panel. Select the pool to destroy and click the **Destroy** button. To confirm the destruction of the pool, you need to enter the pool name.

Run the following command to destroy a pool. Specify the *-remove_storages* to also remove the associated storage.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool destroy <name>
```

{% hint style="info" %}
Pool deletion runs in the background and can take some time. You will notice the data usage in the cluster decreasing throughout this process.
{% endhint %}

### PG Autoscaler <a href="#_pg_autoscaler" id="_pg_autoscaler"></a>

The PG autoscaler allows the cluster to consider the amount of (expected) data stored in each pool and to choose the appropriate pg_num values automatically. It is available since Ceph Nautilus.

You may need to activate the PG autoscaler module before adjustments can take effect.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph mgr module enable pg_autoscaler
```

The autoscaler is configured on a per pool basis and has the following modes:

<table>
<tr>
<td>warn <br/></td>
<td>
<p>A health warning is issued if the suggested <code>pg_num</code> value differs too much from the current value.</p>
</td>
</tr>
<tr>
<td>on <br/></td>
<td>
<p>The <code>pg_num</code> is adjusted automatically with no need for any manual interaction.</p>
</td>
</tr>
<tr>
<td>off <br/></td>
<td>
<p>No automatic <code>pg_num</code> adjustments are made, and no warning will be issued if the PG count is not optimal.</p>
</td>
</tr>
</table>

The scaling factor can be adjusted to facilitate future data storage with the `target_size`, `target_size_ratio` and the `pg_num_min` options.

{% hint style="warning" %}
By default, the autoscaler considers tuning the PG count of a pool if it is off by a factor of 3. This will lead to a considerable shift in data placement and might introduce a high load on the cluster.
{% endhint %}

You can find a more in-depth introduction to the PG autoscaler on Ceph’s Blog - [New in Nautilus: PG merging and autotuning](https://ceph.io/rados/new-in-nautilus-pg-merging-and-autotuning/).

## Ceph CRUSH & Device Classes <a href="#pve_ceph_device_classes" id="pve_ceph_device_classes"></a>

[![screenshot/gui-ceph-config.png](../assets/screenshot-gui-ceph-config-png-b4544eca3b00.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-config.png)

The   
[[https://ceph.com/assets/pdfs/weil-crush-sc06.pdf](https://ceph.com/assets/pdfs/weil-crush-sc06.pdf)]  
 (**C**ontrolled **R**eplication **U**nder **S**calable **H**ashing) algorithm is at the foundation of Ceph.

CRUSH calculates where to store and retrieve data from. This has the advantage that no central indexing service is needed. CRUSH works using a map of OSDs, buckets (device locations) and rulesets (data replication) for pools.

{% hint style="info" %}
Further information can be found in the Ceph documentation, under the section CRUSH map   
[CRUSH map [https://docs.ceph.com/en/tentacle/rados/operations/crush-map/](https://docs.ceph.com/en/tentacle/rados/operations/crush-map/)]  
.
{% endhint %}

This map can be altered to reflect different replication hierarchies. The object replicas can be separated (e.g., failure domains), while maintaining the desired distribution.

A common configuration is to use different classes of disks for different Ceph pools. For this reason, Ceph introduced device classes with luminous, to accommodate the need for easy ruleset generation.

The device classes can be seen in the *ceph osd tree* output. These classes represent their own root bucket, which can be seen with the below command.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd crush tree --show-shadow
```

Example output form the above command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ID  CLASS WEIGHT  TYPE NAME
-16  nvme 2.18307 root default~nvme
-13  nvme 0.72769     host sumi1~nvme
 12  nvme 0.72769         osd.12
-14  nvme 0.72769     host sumi2~nvme
 13  nvme 0.72769         osd.13
-15  nvme 0.72769     host sumi3~nvme
 14  nvme 0.72769         osd.14
 -1       7.70544 root default
 -3       2.56848     host sumi1
 12  nvme 0.72769         osd.12
 -5       2.56848     host sumi2
 13  nvme 0.72769         osd.13
 -7       2.56848     host sumi3
 14  nvme 0.72769         osd.14
```

To instruct a pool to only distribute objects on a specific device class, you first need to create a ruleset for the device class:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd crush rule create-replicated <rule-name> <root> <failure-domain> <class>
```

<table>


<tbody>
<tr>
<td><p>&lt;rule-name&gt;</p></td>
<td><p>name of the rule, to connect with a pool (seen in GUI &amp; CLI)</p></td>
</tr>
<tr>
<td><p>&lt;root&gt;</p></td>
<td><p>which crush root it should belong to (default Ceph root "default")</p></td>
</tr>
<tr>
<td><p>&lt;failure-domain&gt;</p></td>
<td><p>at which failure-domain the objects should be distributed (usually host)</p></td>
</tr>
<tr>
<td><p>&lt;class&gt;</p></td>
<td><p>what type of OSD backing store to use (e.g., nvme, ssd, hdd)</p></td>
</tr>
</tbody>
</table>

Once the rule is in the CRUSH map, you can tell a pool to use the ruleset.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd pool set <pool-name> crush_rule <rule-name>
```

{% hint style="success" %}
If the pool already contains objects, these must be moved accordingly. Depending on your setup, this may introduce a big performance impact on your cluster. As an alternative, you can create a new pool and move disks separately.
{% endhint %}

{% hint style="warning" %}
When using the PG autoscaler, all pools in the cluster are required to use CRUSH rules of the same kind, either all specifying a device class, or none. Otherwise the autoscaler will skip the affected pools and their `pg_num` will not be adjusted.
{% endhint %}

## Cephx Authentication <a href="#pveceph_cephx_how_it_works" id="pveceph_cephx_how_it_works"></a>

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

### Keyring Locations <a href="#pveceph_keyrings" id="pveceph_keyrings"></a>

The authoritative `client.admin` keyring in a Proxmox VE Ceph cluster is `/etc/pve/priv/ceph.client.admin.keyring`, not the copy in `/etc/ceph`. The [Proxmox cluster file system (pmxcfs)](pmxcfs-8.md#chapter_pmxcfs) synchronizes it to every node. Credentials for managed Ceph storages are below `/etc/pve/priv/ceph/`.

Keyrings below `/var/lib/ceph` belong to one Ceph service and are local to its node. `/etc/pve/priv/ceph.mon.keyring` contains both the shared `mon.` key and `client.admin`. Always merge updates into this file instead of overwriting it. `pveceph mon create` uses its `mon.` entry when it initializes a monitor.

### Encrypted OSD Lockbox Keys <a href="#pveceph_cephx_lockbox" id="pveceph_cephx_lockbox"></a>

Each encrypted OSD uses a dedicated Ceph user named `client.osd-lockbox.<UUID>`. Its authentication key is called the lockbox key. It is not the disk-encryption key itself: it lets the OSD retrieve that key from Ceph and unlock its storage when it starts. Ceph and the OSD’s block device must contain matching copies of the lockbox key.

{% hint style="warning" %}
Never rotate a lockbox key with `ceph auth` alone. Use the migration helper, which verifies the OSD identity and updates both copies together.
{% endhint %}

## Ceph Client <a href="#_ceph_client" id="_ceph_client"></a>

[![screenshot/gui-ceph-log.png](../assets/screenshot-gui-ceph-log-png-45dce0bd0f84.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-log.png)

Add an [RBD storage](pvesm-1.md#ceph_rados_block_devices) in the web interface to use a Ceph pool for virtual machine and container disks. For an external cluster, follow the [authentication instructions](pvesm-1.md#storage_rbd_auth) to configure a dedicated Ceph user and its keyring.

## CephFS <a href="#pveceph_fs" id="pveceph_fs"></a>

Ceph also provides a filesystem, which runs on top of the same object storage as RADOS block devices do. A **M**eta**d**ata **S**erver (`MDS`) is used to map the RADOS backed objects to files and directories, allowing Ceph to provide a POSIX-compliant, replicated filesystem. This allows you to easily configure a clustered, highly available, shared filesystem. Ceph’s Metadata Servers guarantee that files are evenly distributed over the entire Ceph cluster. As a result, even cases of high load will not overwhelm a single host, which can be an issue with traditional shared filesystem approaches, for example `NFS`.

[![screenshot/gui-node-ceph-cephfs-panel.png](../assets/screenshot-gui-node-ceph-cephfs-panel-png-51eb3988f01e.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-cephfs-panel.png)

Proxmox VE supports both creating a hyper-converged CephFS and using an existing [CephFS as storage](pvesm-1.md#storage_cephfs) to save backups, ISO files, and container templates.

### Metadata Server (MDS) <a href="#pveceph_fs_mds" id="pveceph_fs_mds"></a>

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
[Configuring multiple active MDS daemons [https://docs.ceph.com/en/tentacle/cephfs/multimds/](https://docs.ceph.com/en/tentacle/cephfs/multimds/)]

### Create CephFS <a href="#pveceph_fs_create" id="pveceph_fs_create"></a>

With Proxmox VE’s integration of CephFS, you can easily create a CephFS using the web interface, CLI or an external API interface. Some prerequisites are required for this to work:

**Prerequisites for a successful CephFS setup:**

- [Install Ceph packages](#pve_ceph_install) - if this was already done some time ago, you may want to rerun it on an up-to-date system to ensure that all CephFS related packages get installed.
- [Setup Monitors](#pve_ceph_monitors)
- [Setup your OSDs](#pve_ceph_monitors)
- [Setup at least one MDS](#pveceph_fs_mds)

After this is complete, you can simply create a CephFS through either the Web GUI’s `Node -> CephFS` panel or the command-line tool `pveceph`, for example:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph fs create --pg_num 128 --add-storage
```

This creates a CephFS named *cephfs*, using a pool for its data named *cephfs_data* with *128* placement groups and a pool for its metadata named *cephfs_metadata* with one quarter of the data pool’s placement groups (`32`). Check the [Proxmox VE managed Ceph pool chapter](#pve_ceph_pools) or visit the Ceph documentation for more information regarding an appropriate placement group number (`pg_num`) for your setup   
[[placement_groups]](#_footnote_placement_groups)  
. Additionally, the *--add-storage* parameter will add the CephFS to the Proxmox VE storage configuration after it has been created successfully.

### Destroy CephFS <a href="#_destroy_cephfs" id="_destroy_cephfs"></a>

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

## Ceph Maintenance <a href="#_ceph_maintenance" id="_ceph_maintenance"></a>

### Replace OSDs <a href="#pve_ceph_osd_replace" id="pve_ceph_osd_replace"></a>

With the following steps you can replace the disk of an OSD, which is one of the most common maintenance tasks in Ceph. If there is a problem with an OSD while its disk still seems to be healthy, read the [troubleshooting](#pve_ceph_mon_and_ts) section first.

1. If the disk failed, get a [recommended](#pve_ceph_recommendation_disk) replacement disk of the same type and size.
2. [Destroy](#pve_ceph_osd_destroy) the OSD in question.
3. Detach the old disk from the server and attach the new one.
4. [Create](#pve_ceph_osd_create) the OSD again.
5. After automatic rebalancing, the cluster status should switch back to `HEALTH_OK`. Any still listed crashes can be acknowledged by running the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph crash archive-all
```

### Trim/Discard <a href="#_trim_discard" id="_trim_discard"></a>

It is good practice to run *fstrim* (discard) regularly on VMs and containers. This releases data blocks that the filesystem isn’t using anymore. It reduces data usage and resource load. Most modern operating systems issue such discard commands to their disks regularly. You only need to ensure that the Virtual Machines enable the [disk discard option](qm-1.md#qm_hard_disk_discard).

### Scrub & Deep Scrub <a href="#pveceph_scrub" id="pveceph_scrub"></a>

Ceph ensures data integrity by *scrubbing* placement groups. Ceph checks every object in a PG for its health. There are two forms of Scrubbing, daily cheap metadata checks and weekly deep data checks. The weekly deep scrub reads the objects and uses checksums to ensure data integrity. If a running scrub interferes with business (performance) needs, you can adjust the time when scrubs   
[Ceph scrubbing [https://docs.ceph.com/en/tentacle/rados/configuration/osd-config-ref/#scrubbing](https://docs.ceph.com/en/tentacle/rados/configuration/osd-config-ref/#scrubbing)]  
 are executed.

### Mute a Health Check <a href="#pveceph_mute_health_check" id="pveceph_mute_health_check"></a>

Muting a health check keeps it visible but excludes it from the overall health status, making new problems easier to notice. Ceph continues evaluating the check. Use a duration so that a deferred warning returns automatically, for example after two weeks:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph health mute <CHECK> 2w
```

In the web interface, expand the check under **Datacenter → Ceph**, click *Mute*, and set a duration. The check stays in the list, marked as muted; use *Unmute* in the same place to restore it earlier.

By default, a mute clears when more items become affected. Enable *Keep Mute*, or add `--sticky` to the command, only if the check should stay muted in that case. This does not change the duration: a timed sticky mute still expires.

{% hint style="info" %}
Muting does not resolve the condition. You accept its risk for as long as the mute lasts.
{% endhint %}

### Migrate Cephx Keys from `aes` to `aes256k` <a href="#pveceph_cephx_migration" id="pveceph_cephx_migration"></a>

This section explains how to migrate the cluster-owned keys and the keys of compatible Ceph users from `aes` to `aes256k`. For an explanation of Ceph users, tickets, and key storage, see [Cephx Authentication](#pveceph_cephx_how_it_works).

#### Why the Health Checks Appear <a href="#_why_the_health_checks_appear" id="_why_the_health_checks_appear"></a>

Ceph Squid 19.2.6 and Ceph Tentacle 20.2.4 add health checks for keys and temporary access credentials that use the older `aes` encryption method. The checks can therefore appear directly after an upgrade even if the cluster worked without warnings before. The older method is affected by [*CVE-2025-30156*](https://docs.ceph.com/en/latest/security/CVE-2025-30156). See the upstream release announcement for background   
[Ceph: Squid v19.2.6 and Tentacle v20.2.4 released [https://ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/](https://ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/)]  
.

Two checks set the cluster status to *HEALTH_ERR*. This does not mean that storage access or a Ceph service has failed. Follow the steps below to migrate to `aes256k` and, when all clients support it, disable the vulnerable method.

#### Migration Steps <a href="#pveceph_cephx_migration_helper" id="pveceph_cephx_migration_helper"></a>

The migration helper checks the cluster, rotates keys, and resumes interrupted work. Review each dry run before applying its plan; add `--verbose` for full node, keyring, and device inventories and inspection diagnostics.

Reruns do not rotate completed keys again. After each run, invoke the helper without options to check the current state and follow the next steps it prints.

**Before You Begin**

- Upgrade `pve-manager` to 9.2.19 or newer and install the latest Ceph packages on every node. Staged client-key rotation requires Ceph 19.2.6-pve3, 20.2.4-pve3, or newer on every monitor.
- Then complete the rolling restart of all Ceph services.
- Resolve health warnings and errors not listed in [Health Check Reference](#pveceph_cephx_health_check_reference). Ensure every node is reachable over SSH.
- Run the helper as `root` on one node only. Do not start another migration, a rolling restart, or change Ceph keys with other tools while it runs. The helper’s lock does not block direct Ceph authentication commands.
- If Cephx is disabled on this cluster, follow [Clusters with Cephx Disabled](#pveceph_cephx_disabled) instead.

##### 1. Migrate the Cluster-Owned Keys <a href="#_1_migrate_the_cluster_owned_keys" id="_1_migrate_the_cluster_owned_keys"></a>

Review the cluster-owned migration in the default dry-run mode:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys --rotate-cluster-keys
```

If the plan reports no blocker, apply the same selection:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys --rotate-cluster-keys --apply
```

The helper rotates the manager, metadata server, OSD, monitor, bootstrap, crash, and [encrypted OSD lockbox keys](#pveceph_cephx_lockbox). It restarts services one at a time when needed, including monitors. Storage-user keys and `client.admin` stay unchanged, existing tickets remain valid, and the old cipher stays enabled.

After Ceph updates its health status, the two error-severity checks clear. The warning about rotating service keys can remain for a few hours while old rotating keys expire. You do not need to wait for this warning to clear before continuing with the migration.

##### 2. Migrate the Keys of Compatible Ceph Users <a href="#pveceph_cephx_migration_clients" id="pveceph_cephx_migration_clients"></a>

<a id="pveceph_cipher_support"></a>



**Check compatibility**

Several workloads can share one Ceph user. Migrate its key only when every client supports `aes256k`, including disconnected and external clients. Ceph programs from the updated Proxmox VE packages support it; kernel clients require a **running** kernel version 7.0 or newer.

<table>


<tbody>
<tr>
<td><p>Virtual machine with RBD disks</p></td>
<td><p>Userspace, unless <code>krbd</code> is enabled.</p></td>
</tr>
<tr>
<td><p>Container on RBD</p></td>
<td><p>Always the kernel client.</p></td>
</tr>
<tr>
<td><p>CephFS mount</p></td>
<td><p>Kernel, unless <code>fuse</code> is enabled.</p></td>
</tr>
</tbody>
</table>

Check external systems too. If any affected client is incompatible or unknown, leave its user’s key unchanged and postpone this step.

**Stage the keys**

Use `--rotate-all-storage-keys` for the dedicated users of managed local RBD and CephFS storages, together with `--rotate-admin-key` for `client.admin`, which the command line and storages without their own user share. Every client of these users is affected; storages of external clusters are excluded.

The helper stages each new key and writes it to the managed keyring and secret files. Both keys remain valid until confirmation, allowing clients to refresh before the old key is retired. If a monitor cannot keep both keys valid, the helper refuses staging and names the monitor to update or restart.

Review the combined plan:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys \
    --rotate-all-storage-keys --rotate-admin-key
```

If the plan reports no blocker, apply it:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys \
    --rotate-all-storage-keys --rotate-admin-key --apply
```

While a key is staged, do not add or downgrade monitors or change that user’s keys with other tools. Its `AUTH_INSECURE_CLIENT_KEY_TYPE` warning remains until confirmation makes the new key current and invalidates the old one.

<a id="pveceph_cephx_refresh_clients"></a>



**Refresh Clients**

- Live-migrate affected virtual machines in the web interface, or stop and start them. A guest reboot is not enough.
- Stop and start affected containers and other RBD clients.
- Let backups, restores, disk imports, and clones on Ceph storage finish before confirmation; these operations can retain the key they started with.
- The helper refreshes idle CephFS mounts and leaves busy or unresponsive mounts alone. Once nothing uses them, rerun the helper with `--apply` to retry the outstanding mounts. If your virtual machines have ISOs from a CephFS mount attached, you may have to detach the ISOs or migrate affected virtual machines to a different node to be able to refresh the CephFS mount on that node.
- For clients outside Proxmox VE, distribute the staged credential from the [managed key files](#pveceph_cephx_external_copies), then restart or remount those clients.

The helper reports sessions that may still hold an old key. Client hints are host-wide, not session attribution or a complete workload inventory. Sockets without an owning process are listed separately. Check disconnected clients and external key copies yourself.

##### 3. Finish or Pause the Migration <a href="#pveceph_cephx_finish" id="pveceph_cephx_finish"></a>

Run a final dry run to check for remaining old-key sessions. It offers a confirmation command when its observed checks pass, but cannot verify disconnected clients or external key copies for you.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys
```

{% hint style="warning" %}
Clients that still need an old key or cipher cannot authenticate after this step. Existing IO can appear to work until a reconnect and then fail. Do not use `--force` to bypass a blocker.
{% endhint %}

After checking disconnected clients and external copies, run the exact command the dry run prints. When every rotation is ready and no key needs the old cipher, it will print the options `--apply --confirm-all-clients-refreshed
--restrict-ciphers`.

If any client remains incompatible, keep its key unchanged and the old cipher enabled rather than restricting it. You can [mute the remaining warnings](#pveceph_mute_health_check) while waiting for those clients to upgrade.

Use `pveceph auth status` for current and pending key ciphers, as `ceph auth ls` does not list pending keys.

{% hint style="info" %}
`/etc/pve/priv/cephx-key-migration.json` records progress and contains secret old keys. Protect it and keep it until the migration is complete and every client has been refreshed. Deleting it earlier loses the records needed to resume.
{% endhint %}

#### Additional Migration Details <a href="#_additional_migration_details" id="_additional_migration_details"></a>

##### Health Check Reference <a href="#pveceph_cephx_health_check_reference" id="pveceph_cephx_health_check_reference"></a>

<table>



<thead>
<tr>
<th>Health check</th>
<th>Meaning</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>AUTH_INSECURE_SERVICE_KEY_TYPE</code></p></td>
<td><p>A Ceph service key uses the old cipher.</p></td>
<td><p>Run the cluster-owned migration. This check has error severity.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_SERVICE_TICKETS</code></p></td>
<td><p>Monitors issue service tickets with the old cipher.</p></td>
<td><p>Run the cluster-owned migration. This check has error severity.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_CLIENT_KEY_TYPE</code></p></td>
<td><p>The active key of a Ceph user uses the old cipher. A staged user stays listed until its rotation is confirmed.</p></td>
<td><p>Rotate the keys of compatible users and confirm them, or mute the warning.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_ROTATING_SERVICE_KEY_TYPE</code></p></td>
<td><p>A rotating service key uses the old cipher.</p></td>
<td><p>Continue the migration; old rotating keys expire automatically and do not prevent final cipher restriction.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_KEYS_ALLOWED</code></p></td>
<td><p>Monitors accept the old cipher.</p></td>
<td><p>Finish the migration, or mute the warning while old clients remain.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_KEYS_CREATABLE</code></p></td>
<td><p>Monitors can create old-cipher keys.</p></td>
<td><p>Finish the migration, or mute the warning while old clients remain.</p></td>
</tr>
</tbody>
</table>

##### Clusters with Cephx Disabled <a href="#pveceph_cephx_disabled" id="pveceph_cephx_disabled"></a>

Ceph evaluates these health checks from the stored keys and cipher settings, also when Cephx is disabled, that is, when `auth_cluster_required`, `auth_service_required`, and `auth_client_required` are set to `none`. Disabling Cephx therefore does not clear them, and changing the authentication method interrupts existing clients, which need a restart or remount afterwards.

On a cluster with Cephx disabled:

1. Run the helper without options and apply its plan. It migrates the manager, metadata server, and OSD keys, restarting services one at a time when needed, and switches the service tickets to the new cipher. This clears both error-severity checks. If an old `mon.` key is stored in the authentication database, the helper instead refuses and asks you to migrate that key first.
2. Optionally, migrate the bootstrap and crash keys with `--rotate-client-keys`.
3. Mute the remaining warnings without a duration. While Cephx is disabled, the helper does not migrate the keys of other Ceph users, as their clients do not authenticate with Cephx:

   Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

   ```text
   ceph health mute AUTH_INSECURE_CLIENT_KEY_TYPE --sticky
   ceph health mute AUTH_INSECURE_KEYS_ALLOWED --sticky
   ceph health mute AUTH_INSECURE_KEYS_CREATABLE --sticky
   ```

Do not restrict the allowed ciphers or forbid creating old-cipher keys by hand while the preferred cipher is still `aes`, as creating keys then fails.

Before you enable Cephx again, unmute these checks and make sure that every monitor, Ceph service, and client still has a key file matching the authentication database. Restart the monitors first, then all other Ceph services, and restart or remount the clients. Then run the migration as described in [Migration Steps](#pveceph_cephx_migration_helper).

##### Staged Keys and Confirmation <a href="#pveceph_cephx_staged_keys" id="pveceph_cephx_staged_keys"></a>

The helper disables automatic promotion of pending client keys so that the monitors keep both credentials valid. An older monitor would promote a staged key on its first use and end the grace period for the whole cluster. The helper therefore stages only when every monitor supports the feature and checks this again on every run.

With `--apply`, `--confirm-all-clients-refreshed` makes every staged key current and invalidates its previous key. The initial check refuses the entire batch if any open rotation is not ready. The helper then rechecks each key before retiring its old credential. If a client returns during the batch, completed rotations stay committed and the blocked key stays staged. To confirm ready users separately, use `--confirm-clients-refreshed <USER>` with `--apply`.

Ceph 19.2.6-pve4 and 20.2.4-pve4 or newer monitors can identify each session’s key, allowing refreshed clients to stay connected during forward or rollback confirmation. Upgrade and restart older monitors to use this feature. Without key identification, every visible client of that user must disconnect before confirmation; upgrading is preferable for a shared user such as `client.admin`.

##### Key Copies for External Clients <a href="#pveceph_cephx_external_copies" id="pveceph_cephx_external_copies"></a>

For an external client of the local cluster, copy the staged credential from the managed file for its Ceph user:

- RBD keyring: `/etc/pve/priv/ceph/<STORAGE_ID>.keyring`
- CephFS bare secret: `/etc/pve/priv/ceph/<STORAGE_ID>.secret`
- Administrative keyring: `/etc/pve/priv/ceph.client.admin.keyring`

Use the credential for that user, not `client.admin` as a substitute. Transfer it securely and update every saved copy before refreshing the client. Storage backed by an external cluster is different: the helper never rotates that cluster’s keys. Follow its administrator’s key-rotation procedure.

A storage with `monhost` set counts as external even if its monitors belong to the local cluster, so the helper does not update its key copy. If that copy holds the key of a Ceph user you migrate, update it with the staged key of the same user before confirming, or with the restored key before confirming a rollback. The helper refuses to retire a key it finds in a storage key copy; verify copies it cannot check yourself.

The helper lists local users not managed by Proxmox VE separately. Follow their client’s supported rotation procedure, or leave their keys unchanged and keep the old cipher enabled.

##### Roll Back a Staged Client Key <a href="#pveceph_cephx_rollback" id="pveceph_cephx_rollback"></a>

To return a staged user to its current key:

1. Run the helper with `--abort-staged-key <USER> --apply`. It restores the current key to every managed copy while both credentials remain valid.
2. Refresh all clients back to that key, including disconnected clients and external key copies. The helper retries managed CephFS mounts as during forward migration.
3. Run the helper with `--confirm-abort-clients-refreshed <USER> --apply` to retire the staged key. The helper refuses if monitor session collection is incomplete, a visible session uses the staged key, its key is unknown, or a storage key copy still holds the staged key.

##### Emergency Cipher Override <a href="#_emergency_cipher_override" id="_emergency_cipher_override"></a>

Monitors normally use the `auth_allowed_ciphers` list stored in the MonMap to decide which key ciphers may authenticate. The local startup option `mon_auth_emergency_allowed_ciphers` replaces that list for a monitor. It can temporarily allow the cipher of an existing administrative key after an incorrect restriction locked administrators out   
[Ceph: Emergency Allowed Ciphers [https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#emergency-allowed-ciphers](https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#emergency-allowed-ciphers)]  
.

Ceph raises `AUTH_EMERGENCY_CIPHERS_SET` while this override is configured. The helper refuses the final restriction because changing the MonMap would not take effect. Use the override only to recover access, then repair the normal configuration, remove it from `/etc/pve/ceph.conf`, and restart every monitor before the final dry run.

##### Interrupted Runs and Manual Fallback <a href="#_interrupted_runs_and_manual_fallback" id="_interrupted_runs_and_manual_fallback"></a>

After an interruption, run the helper without options once the affected nodes are reachable. Unfinished key updates can resume while their daemons are stopped. Keep the journal unchanged and follow the printed next steps rather than starting a manual rotation. Check the affected nodes and service logs rather than assuming a down daemon’s key needs repair.

If the helper still cannot proceed, install the latest `pve-manager` and retry. Contact Proxmox support before editing the journal or keyrings, or before using the upstream Cephx key migration procedure   
[Ceph documentation: [https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#cephx-upgrade](https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#cephx-upgrade)]  
. That procedure changes the Ceph authentication database, but does not account for these Proxmox VE details:

- Ensure every managed key copy below `/etc/pve/priv` and `/var/lib/ceph` contains the key that Ceph accepts. Merge changes into `/etc/pve/priv/ceph.mon.keyring`; never overwrite it.
- Update an encrypted OSD’s lockbox key in both the authentication database and its block-device LVM tag. Its temporary keyring is not the persistent copy.
- Refresh every client before invalidating its previous Ceph user key.
- Rotate `client.admin` last and prepare an independently tested recovery user before changing it.

Use manual key-rotation or cipher-restriction commands only with a complete, tested recovery plan that covers every item above.

### Shutdown Proxmox VE + Ceph HCI Cluster <a href="#pveceph_shutdown" id="pveceph_shutdown"></a>

To shut down the whole Proxmox VE + Ceph cluster, first stop all Ceph clients. These will mainly be VMs and containers. If you have additional clients that might access a Ceph FS or an installed RADOS GW, stop these as well. Highly available guests will switch their state to *stopped* when powered down via the Proxmox VE tooling.

Once all clients, VMs and containers are off or not accessing the Ceph cluster anymore, verify that the Ceph cluster is in a healthy state. Either via the Web UI or the CLI:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph -s
```

In order to not cause any recovery during the shut down and later power on phases, enable the *noout* OSD flag. Either in the **Ceph → OSD** panel behind the **Manage Global Flags** button or the CLI:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd set noout
```

Start powering down your nodes without a monitor (MON). After these nodes are down, continue by shutting down nodes with monitors on them.

When powering on the cluster, start the nodes with monitors (MONs) first. Once all nodes are up and running, confirm that all Ceph services are up and running. In the end, the only warning you should see for Ceph is that the *noout* flag is still set. You can disable it via the web UI or via the CLI:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd unset noout
```

You can now start up the guests. Highly available guests will change their state to *started* when they power on.

### Network Changes <a href="#pveceph_network_change" id="pveceph_network_change"></a>

It is possible to change the networks used by Ceph in a HCI setup without any downtime if **both the old and new networks can be configured at the same time**.

The procedure differs depending on which network you want to change.

{% hint style="info" %}
A word of caution! It is critical that the change of the used networks by Ceph is being done carefully. Otherwise it could lead to a broken Ceph cluster with downtime to get it back into a working state! We recommend doing a trial run of the procedure in a (virtual) test cluster before changing the production infrastructure.
{% endhint %}

After the new network has been configured on all hosts, make sure you test it before proceeding with the changes. One way is to ping all hosts on the new network. If you use a large MTU, make sure to also test that it works. For example by sending ping packets that will result in a final packet at the max MTU size.

To test an MTU of 9000, you will need the following packet sizes:

{% hint style="info" %}
We assume a simple network configuration. In more complicated setups, you might need to configure a lower MTU to account for any headers that might be added once a packet leaves the host.
{% endhint %}

<table>
<tr>
<td>IPv4 <br/></td>
<td>
<p>The overhead of IP and ICMP is <em>28</em> bytes; the resulting packet size for the ping then is <em>8972</em> bytes.</p>
</td>
</tr>
<tr>
<td>IPv6 <br/></td>
<td>
<p>The overhead is <em>48</em> bytes and the resulting packet size is <em>8952</em> bytes.</p>
</td>
</tr>
</table>

The resulting ping command will look like this for an IPv4:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ping -M do -s 8972 {target IP}
```

When you are switching between IPv4 and IPv6 networks, you need to make sure that the following options in the `ceph.conf` file are correctly set to `true` or `false`. These config options configure if Ceph services should bind to IPv4 or IPv6 addresses.

```text
ms_bind_ipv4 = true
ms_bind_ipv6 = false
```

#### Change the Ceph Public Network <a href="#pveceph_network_change_public" id="pveceph_network_change_public"></a>

The Ceph Public network is the main communication channel in a Ceph cluster between the different services and clients (for example, a VM). Changing it to a different network is not as simple as changing the Ceph Cluster network. The main reason is that besides the configuration in the `ceph.conf` file, the Ceph MONs (monitors) have an internal configuration where they keep track of all the other MONs that are part of the cluster, the *monmap*.

Therefore, the procedure to change the Ceph Public network is a bit more involved:

1. Change `public_network` in the `/etc/pve/ceph.conf` file (do not change any other value)
2. Restart non MON services: OSDs, MGRs and MDS on one host
3. Wait until Ceph is back to *HEALTH_OK*
4. Verify services are using the new network
5. Continue restarting services on the next host
6. Destroy one MON
7. Recreate MON
8. Wait until Ceph is back to *HEALTH_OK*
9. Continue destroying and recreating MONs

You first need to edit the `/etc/pve/ceph.conf` file. Change the `public_network` line to match the new subnet.

```text
public_network = 10.9.9.30/24
```

{% hint style="warning" %}
Do not change the `mon_host` line or any `[mon.HOSTNAME]` sections. These will be updated automatically when the MONs are destroyed and recreated.
{% endhint %}

{% hint style="info" %}
Don’t worry if the host bits (for example, the last octet) are set by default, the netmask in CIDR notation defines the network part.
{% endhint %}

After you have changed the network, you need to restart the non MON services in the cluster for the changes to take effect. Do so one node at a time! To restart all non MON services on one node, you can use the following commands on that node. Ceph has `systemd` targets for each type of service.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
systemctl restart ceph-osd.target
systemctl restart ceph-mgr.target
systemctl restart ceph-mds.target
```

{% hint style="info" %}
You will only have MDS daemons (Metadata Servers) if you use CephFS.
{% endhint %}

{% hint style="info" %}
After the first OSD service got restarted, the GUI will complain that the OSD is not reachable anymore. This is not an issue; VMs can still reach them. The reason for the message is that the MGR service cannot reach the OSD anymore. The error will vanish after the MGR services get restarted.
{% endhint %}

{% hint style="warning" %}
Do not restart OSDs on multiple hosts at the same time. Chances are that for some PGs (placement groups), 2 out of the (default) 3 replicas will be down. This will result in I/O being halted until the minimum required number (`min_size`) of replicas is available again.
{% endhint %}

To verify that the services are listening on the new network, you can run the following command on each node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ss -tulpn | grep ceph
```

{% hint style="info" %}
Since OSDs will also listen on the Ceph Cluster network, expect to see that network too in the output of `ss -tulpn`.
{% endhint %}

Once the Ceph cluster is back in a fully healthy state (*HEALTH_OK*), and the services are listening on the new network, continue to restart the services on the host.

The last services that need to be moved to the new network are the Ceph MONs themselves. The easiest way is to destroy and recreate each monitor one by one. This way, any mention of it in the `ceph.conf` and the monitor internal `monmap` is handled automatically.

Destroy the first MON and create it again. Wait a few moments before you continue on to the next MON in the cluster, and make sure the cluster reports *HEALTH_OK* before proceeding.

Once all MONs are recreated, you can verify that any mention of MONs in the `ceph.conf` file references the new network. That means mainly the `mon_host` line and the `[mon.HOSTNAME]` sections.

One final `ss -tulpn | grep ceph` should show that the old network is not used by any Ceph service anymore.

#### Change the Ceph Cluster Network <a href="#pveceph_network_change_cluster" id="pveceph_network_change_cluster"></a>

The Ceph Cluster network is used for the replication traffic between the OSDs. Therefore, it can be beneficial to place it on its own fast physical network.

The overall procedure is:

1. Change `cluster_network` in the `/etc/pve/ceph.conf` file
2. Restart OSDs on one host
3. Wait until Ceph is back to *HEALTH_OK*
4. Verify OSDs are using the new network
5. Continue restarting OSDs on the next host

You first need to edit the `/etc/pve/ceph.conf` file. Change the `cluster_network` line to match the new subnet.

```text
cluster_network = 10.9.9.30/24
```

{% hint style="info" %}
Don’t worry if the host bits (for example, the last octet) are set by default; the netmask in CIDR notation defines the network part.
{% endhint %}

After you have changed the network, you need to restart the OSDs in the cluster for the changes to take effect. Do so one node at a time! To restart all OSDs on one node, you can use the following command on the CLI on that node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
systemctl restart ceph-osd.target
```

{% hint style="warning" %}
Do not restart OSDs on multiple hosts at the same time. Chances are that for some PGs (placement groups), 2 out of the (default) 3 replicas will be down. This will result in I/O being halted until the minimum required number (`min_size`) of replicas is available again.
{% endhint %}

To verify that the OSD services are listening on the new network, you can either check the **OSD Details → Network** tab in the **Ceph → OSD** panel or by running the following command on the host:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ss -tulpn | grep ceph-osd
```

{% hint style="info" %}
Since OSDs will also listen on the Ceph Public network, expect to see that network too in the output of `ss -tulpn`.
{% endhint %}

Once the Ceph cluster is back in a fully healthy state (*HEALTH_OK*), and the OSDs are listening on the new network, continue to restart the OSDs on the next host.

## Ceph Monitoring and Troubleshooting <a href="#pve_ceph_mon_and_ts" id="pve_ceph_mon_and_ts"></a>

It is important to continuously monitor the health of a Ceph deployment from the beginning, either by using the Ceph tools or by accessing the status through the Proxmox VE [API](https://pve.proxmox.com/pve-docs/api-viewer/index.html).

The following Ceph commands can be used to see if the cluster is healthy (*HEALTH_OK*), if there are warnings (*HEALTH_WARN*), or even errors (*HEALTH_ERR*). If the cluster is in an unhealthy state, the status commands below will also give you an overview of the current events and actions to take. To stop their execution, press CTRL-C.

Continuously watch the cluster status:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
watch ceph --status
```

Print the cluster status once (not being updated) and continuously append lines of status events:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph --watch
```

### Troubleshooting <a href="#pve_ceph_ts" id="pve_ceph_ts"></a>

This section includes frequently used troubleshooting information. More information can be found on the official Ceph website under Troubleshooting   
[Ceph troubleshooting [https://docs.ceph.com/en/tentacle/rados/troubleshooting/](https://docs.ceph.com/en/tentacle/rados/troubleshooting/)]  
.

<a id="pve_ceph_ts_logs"></a>



**Relevant Logs on Affected Node**

- Disk Health Monitoring
- *System → System Log* or via the CLI, for example of the last 2 days:

  Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

  ```text
  journalctl --since "2 days ago"
  ```
- IPMI and RAID controller logs

Ceph service crashes can be listed and viewed in detail by running the following commands:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph crash ls
ceph crash info <crash_id>
```

Crashes marked as new can be acknowledged by running:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph crash archive-all
```

To get a more detailed view, every Ceph service has a log file under `/var/log/ceph/`. If more detail is required, the log level can be adjusted   
[Ceph log and debugging [https://docs.ceph.com/en/tentacle/rados/troubleshooting/log-and-debug/](https://docs.ceph.com/en/tentacle/rados/troubleshooting/log-and-debug/)]  
.

<a id="pve_ceph_ts_causes"></a>



**Common Causes of Ceph Problems**

- Network problems like congestion, a faulty switch, a shut down interface or a blocking firewall. Check whether all Proxmox VE nodes are reliably reachable on the [corosync cluster network](pvecm-1.md#pvecm_cluster_network) and on the [Ceph public and cluster network](#pve_ceph_install_wizard).
- Disk or connection parts which are:

  - defective
  - not firmly mounted
  - lacking I/O performance under higher load (e.g. when using HDDs, consumer hardware or [inadvisable RAID controllers](#pve_ceph_recommendation_raid))
- Not fulfilling the [recommendations](#_recommendations_for_a_healthy_ceph_cluster) for a healthy Ceph cluster.

<a id="pve_ceph_ts_problems"></a>



**Common Ceph Problems**

****

**OSDs `down`/crashed**

A faulty OSD will be reported as `down` and mostly (auto) `out` 10 minutes later. Depending on the cause, it can also automatically become `up` and `in` again. To try a manual activation via web interface, go to *Any node → Ceph → OSD*, select the OSD and click on **Start**, **In** and **Reload**. When using the shell, run following command on the affected node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph-volume lvm activate --all
```

To activate a failed OSD, it may be necessary to [safely reboot](ha-manager-1.md#ha_manager_node_maintenance) the respective node or, as a last resort, to [recreate or replace](#pve_ceph_osd_replace) the OSD.

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pveceph.1.html) · 版本 9.2.13 · 非官方中文翻译。
