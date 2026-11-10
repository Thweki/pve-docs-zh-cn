# 22.6. **pveceph** \- 管理 Proxmox VE 节点上的 CEPH 服务 <a href="#strong_pveceph_strong_manage_ceph_services_on_proxmox_ve_nodes" id="strong_pveceph_strong_manage_ceph_services_on_proxmox_ve_nodes"></a>

## **pveceph** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveceph" id="cli_pveceph"></a>

## **pveceph auth status** `[FORMAT_OPTIONS]` <a href="#cli_pveceph_auth_status" id="cli_pveceph_auth_status"></a>

显示 cephx 密钥密码算法和 aes256k 迁移先决条件。

## **pveceph createmgr** <a href="#cli_pveceph_createmgr" id="cli_pveceph_createmgr"></a>

*pveceph mgr create* 的别名。

## **pveceph createmon** <a href="#cli_pveceph_createmon" id="cli_pveceph_createmon"></a>

*pveceph mon create* 的别名。

## **pveceph createosd** <a href="#cli_pveceph_createosd" id="cli_pveceph_createosd"></a>

*pveceph osd create* 的别名。

## **pveceph createpool** <a href="#cli_pveceph_createpool" id="cli_pveceph_createpool"></a>

*pveceph pool create* 的别名。

## **pveceph destroymgr** <a href="#cli_pveceph_destroymgr" id="cli_pveceph_destroymgr"></a>

*pveceph mgr destroy* 的别名。

## **pveceph destroymon** <a href="#cli_pveceph_destroymon" id="cli_pveceph_destroymon"></a>

*pveceph mon destroy* 的别名。

## **pveceph destroyosd** <a href="#cli_pveceph_destroyosd" id="cli_pveceph_destroyosd"></a>

*pveceph osd destroy* 的别名。

## **pveceph destroypool** <a href="#cli_pveceph_destroypool" id="cli_pveceph_destroypool"></a>

*pveceph pool destroy* 的别名。

## **pveceph fs create** `[OPTIONS]` <a href="#cli_pveceph_fs_create" id="cli_pveceph_fs_create"></a>

创建 Ceph 文件系统

**`--add-storage` `<boolean>` （*默认值 \=* `0`）**

将创建的 CephFS 配置为此集群的存储。

**`--name` `(?^:^[^:/\s]+$)` （*默认值 \=* `cephfs`）**

ceph 文件系统名称。

**`--pg_num` `<integer> (8 - 32768)` （*默认值 \=* `128`）**

后端数据池的放置组数量。元数据池将使用此数量的四分之一。

## **pveceph fs destroy** `<name>` `[OPTIONS]` <a href="#cli_pveceph_fs_destroy" id="cli_pveceph_fs_destroy"></a>

销毁 Ceph 文件系统。如果任何类型为 *cephfs* 的 PVE 存储条目仍引用该文件系统且未禁用，则拒绝操作。还可以选择移除存储条目和/或底层元数据池及数据池。

**`<name>`: `<string>`**

Ceph 文件系统名称。

**`--remove-pools` `<boolean>` （*默认值 \=* `0`）**

移除此文件系统使用的元数据池和数据池。

**`--remove-storages` `<boolean>` （*默认值 \=* `0`）**

移除为此文件系统配置的、由 pveceph 管理的存储。

## **pveceph help** `[OPTIONS]` <a href="#cli_pveceph_help" id="cli_pveceph_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pveceph init** `[OPTIONS]` <a href="#cli_pveceph_init" id="cli_pveceph_init"></a>

创建初始的 Ceph 默认配置并设置符号链接。重复调用具有幂等性：如果 ceph.conf 中已存在 \[global\] 部分，则保留现有的 fsid / auth / pool 默认值，并静默忽略大多数参数。

**`--cluster-network` `<string>`**

声明单独的集群网络，OSD 将通过此网络传输心跳、对象复制和恢复流量

{% hint style="info" %}
需要选项：`network`
{% endhint %}

**`--disable_cephx` `<boolean>` （*默认值 \=* `0`）**

禁用 cephx 认证。

{% hint style="warning" %}
cephx 是防止中间人攻击的安全功能。只有在网络为私有网络时才考虑禁用 cephx！
{% endhint %}

**`--min_size` `<integer> (1 - 7)` （*默认值 \=* `2`）**

允许 I/O 所需的每个对象的最少可用副本数量

**`--network` `<string>`**

对所有 ceph 相关流量使用指定网络

**`--pg_bits` `<integer> (6 - 14)` （*默认值 \=* `6`）**

放置组位数，用于指定默认放置组数量。

已弃用。近期 Ceph 版本中已弃用此设置。

**`--size` `<integer> (1 - 7)` （*默认值 \=* `3`）**

每个对象的目标副本数量

## **pveceph install** `[OPTIONS]` <a href="#cli_pveceph_install" id="cli_pveceph_install"></a>

安装 ceph 相关软件包。

**`--allow-experimental` `<boolean>` （*默认值 \=* `0`）**

允许实验性版本。请谨慎使用！

**`--repository` `<enterprise | manual | no-subscription | test>` （*默认值 \=* `enterprise`）**

使用的 Ceph 仓库。*manual* 选项不会配置任何仓库。如果宿主机无法访问公共仓库，例如使用 Proxmox Offline Mirror 时，请使用此选项。开始安装之前，需要手动配置包含相应版本 Ceph 软件包的仓库！

**`--version` `<squid | tentacle>` （*默认值 \=* `tentacle`）**

要安装的 Ceph 版本。

## **pveceph lspools** <a href="#cli_pveceph_lspools" id="cli_pveceph_lspools"></a>

*pveceph pool ls* 的别名。

## **pveceph mds create** `[OPTIONS]` <a href="#cli_pveceph_mds_create" id="cli_pveceph_mds_create"></a>

创建 Ceph 元数据服务器（MDS）

**`--hotstandby` `<boolean>` （*默认值 \=* `0`）**

确定 ceph-mds 守护进程是否应轮询并重放活动 MDS 的日志。这可以在 MDS 故障时更快地切换，但需要更多空闲资源。已弃用：此设置已在 Ceph 14.1.1 中移除。

**`--name` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` （*默认值 \=* `nodename`）**

mds 的 ID，省略时与节点名称相同

## **pveceph mds destroy** `<name>` <a href="#cli_pveceph_mds_destroy" id="cli_pveceph_mds_destroy"></a>

销毁 Ceph 元数据服务器

**`<name>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

mds 的名称（ID）

## **pveceph mgr create** `[OPTIONS]` <a href="#cli_pveceph_mgr_create" id="cli_pveceph_mgr_create"></a>

创建 Ceph 管理器

**`--id` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` （*默认值 \=* `nodename`）**

管理器的 ID，省略时与节点名称相同。

## **pveceph mgr destroy** `<id>` <a href="#cli_pveceph_mgr_destroy" id="cli_pveceph_mgr_destroy"></a>

销毁 Ceph 管理器。

**`<id>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

管理器的 ID

## **pveceph mon create** `[OPTIONS]` <a href="#cli_pveceph_mon_create" id="cli_pveceph_mon_create"></a>

创建 Ceph 监视器。对于首个监视器，还会自动创建管理器。

**`--mon-address` `<string>`**

覆盖自动检测的监视器 IP 地址。必须位于 Ceph 的公共网络中。

**`--monid` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` （*默认值 \=* `nodename`）**

监视器的 ID，省略时与节点名称相同。

## **pveceph mon destroy** `<monid>` <a href="#cli_pveceph_mon_destroy" id="cli_pveceph_mon_destroy"></a>

销毁 Ceph 监视器。拒绝移除集群中的最后一个监视器。不会销毁同一节点上的任何管理器；请使用

**`<monid>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

监视器 ID

## **pveceph osd create** `<dev>` `[OPTIONS]` <a href="#cli_pveceph_osd_create" id="cli_pveceph_osd_create"></a>

创建 OSD

**`<dev>`: `<string>`**

块设备名称。

**`--crush-device-class` `<string>`**

设置 OSD 在 crush 中的设备类别。

**`--db_dev` `<string>`**

block.db 的块设备名称。

**`--db_dev_size` `<number> (1 - N)`**

block.db 的大小，单位为 GiB。

{% hint style="info" %}
需要选项：`db_dev`
{% endhint %}

**`--encrypted` `<boolean>` （*默认值 \=* `0`）**

启用 OSD 加密。

**`--osds-per-device` `<integer> (1 - N)`**

每个物理设备上的 OSD 服务数量。仅对高速 NVMe 设备有用，可更好地利用其性能。与 *db\_dev* 和 *wal\_dev* 互斥。

**`--wal_dev` `<string>`**

block.wal 的块设备名称。

**`--wal_dev_size` `<number> (0.5 - N)`**

block.wal 的大小，单位为 GiB。

{% hint style="info" %}
需要选项：`wal_dev`
{% endhint %}

## **pveceph osd destroy** `<osdid>` `[OPTIONS]` <a href="#cli_pveceph_osd_destroy" id="cli_pveceph_osd_destroy"></a>

销毁 OSD

**`<osdid>`: `<integer>`**

OSD ID

**`--cleanup` `<boolean>` （*默认值 \=* `0`）**

如果设置，还会通过 *ceph-volume lvm zap --destroy* 销毁底层逻辑卷，使用 pvremove 移除卷组的物理卷，并擦除 filestore OSD 遗留的任何 journal/block.db/block.wal 分区。如果不设置此标志，LV 和分区将保持原样，以供检查。

## **pveceph osd details** `<osdid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveceph_osd_details" id="cli_pveceph_osd_details"></a>

获取 OSD 详细信息。

**`<osdid>`: `<string>`**

OSD 的 ID

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

打印详细信息，与 json-pretty 输出格式相同。

## **pveceph pool create** `<name>` `[OPTIONS]` <a href="#cli_pveceph_pool_create" id="cli_pveceph_pool_create"></a>

创建 Ceph 池

**`<name>`: `(?^:^[^:/\s]+$)`**

池的名称。必须唯一。

**`--add_storages` `<boolean>` （*默认值 \=* `0`）**

使用新池配置虚拟机和容器存储。对于复制池默认为 false，对于纠删码池默认为 true（因为 EC 池通常只有连接到存储后才有用）。

**`--application` `<cephfs | rbd | rgw>` （*默认值 \=* `rbd`）**

池的应用。

**`--crush_rule` `<string>`**

用于映射集群中对象放置位置的规则。

**`--erasure-coding` `k=<integer> ,m=<integer> [,device-class=<class>] [,failure-domain=<domain>] [,profile=<profile>]`**

为 RBD 创建纠删码池，同时创建用于元数据存储的配套复制池。使用 EC 时，常见 ceph 选项 *size*、*min\_size* 和 *crush\_rule* 参数将应用于元数据池。

**`--min_size` `<integer> (1 - 7)` （*默认值 \=* `2`）**

每个对象的最少副本数量

**`--pg_autoscale_mode` `<off | on | warn>` （*默认值 \=* `warn`）**

池的自动 PG 扩缩模式。

**`--pg_num` `<integer> (1 - 32768)` （*默认值 \=* `128`）**

放置组数量。

**`--pg_num_min` `<integer> (-N - 32768)`**

放置组的最少数量。

**`--size` `<integer> (1 - 7)` （*默认值 \=* `3`）**

每个对象的副本数量

**`--target_size` `^(\d+(\.\d+)?)([KMGT])?$`**

用于 PG 自动扩缩器的池预计目标大小。

**`--target_size_ratio` `<number>`**

用于 PG 自动扩缩器的池预计目标比例。

## **pveceph pool destroy** `<name>` `[OPTIONS]` <a href="#cli_pveceph_pool_destroy" id="cli_pveceph_pool_destroy"></a>

销毁池

**`<name>`: `<string>`**

池的名称。必须唯一。

**`--force` `<boolean>`（*默认 \=* `0`）**

如果为 true，即使池正在使用也将其销毁

**`--remove_ecprofile` `<boolean>` （*默认值 \=* `1`）**

移除纠删码配置文件。在适用情况下默认为 true。

**`--remove_storages` `<boolean>` （*默认值 \=* `0`）**

移除为此池配置的、由 pveceph 管理的所有存储

## **pveceph pool get** `<name>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveceph_pool_get" id="cli_pveceph_pool_get"></a>

显示池的当前状态。

**`<name>`: `<string>`**

池的名称。必须唯一。

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

如果启用，将显示额外数据（例如统计信息）。

## **pveceph pool ls** `[FORMAT_OPTIONS]` <a href="#cli_pveceph_pool_ls" id="cli_pveceph_pool_ls"></a>

列出所有池及其设置（可通过 POST/PUT 端点设置的选项）。

## **pveceph pool set** `<name>` `[OPTIONS]` <a href="#cli_pveceph_pool_set" id="cli_pveceph_pool_set"></a>

更改 POOL 设置

**`<name>`: `(?^:^[^:/\s]+$)`**

池的名称。必须唯一。

**`--application` `<cephfs | rbd | rgw>`**

池的应用。

**`--crush_rule` `<string>`**

用于映射集群中对象放置位置的规则。

**`--min_size` `<integer> (1 - 7)`**

每个对象的最少副本数量

**`--pg_autoscale_mode` `<off | on | warn>`**

池的自动 PG 扩缩模式。

**`--pg_num` `<integer> (1 - 32768)`**

放置组数量。

**`--pg_num_min` `<integer> (-N - 32768)`**

放置组的最少数量。

**`--size` `<integer> (1 - 7)`**

每个对象的副本数量

**`--target_size` `^(\d+(\.\d+)?)([KMGT])?$`**

用于 PG 自动扩缩器的池预计目标大小。

**`--target_size_ratio` `<number>`**

用于 PG 自动扩缩器的池预计目标比例。

## **pveceph purge** `[OPTIONS]` <a href="#cli_pveceph_purge" id="cli_pveceph_purge"></a>

销毁 ceph 相关数据和配置文件。

**`--crash` `<boolean>`**

同时清除 Ceph 崩溃日志，/var/lib/ceph/crash.

**`--logs` `<boolean>`**

同时清除 Ceph 日志，/var/log/ceph.

## **pveceph start** `[OPTIONS]` <a href="#cli_pveceph_start" id="cli_pveceph_start"></a>

启动 ceph 服务。

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` （*默认值 \=* `ceph.target`）**

Ceph 服务名称。

## **pveceph status** <a href="#cli_pveceph_status" id="cli_pveceph_status"></a>

获取 Ceph 状态。

## **pveceph stop** `[OPTIONS]` <a href="#cli_pveceph_stop" id="cli_pveceph_stop"></a>

停止 ceph 服务。

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` （*默认值 \=* `ceph.target`）**

Ceph 服务名称。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
