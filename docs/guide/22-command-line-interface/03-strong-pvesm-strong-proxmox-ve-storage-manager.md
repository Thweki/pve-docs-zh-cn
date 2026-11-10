# 22.3. **pvesm** \- Proxmox VE 存储管理器 <a href="#strong_pvesm_strong_proxmox_ve_storage_manager" id="strong_pvesm_strong_proxmox_ve_storage_manager"></a>

## **pvesm** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesm" id="cli_pvesm"></a>

## **pvesm add** `<type> <storage>` `[OPTIONS]` <a href="#cli_pvesm_add" id="cli_pvesm_add"></a>

创建新存储。

**`<type>`: `<btrfs | cephfs | cifs | dir | esxi | iscsi | iscsidirect | lvm | lvmthin | nfs | pbs | rbd | zfs | zfspool>`**

存储类型。

**`<storage>`: `<storage ID>`**

存储标识符。

**`--authsupported` `<string>`**

支持的认证方式。

**`--base` `<string>`**

基础卷。此卷会自动激活。

**`--blocksize` `<a power of 2 with optional k or m suffix>`**

ZFS 块大小

**`--bwlimit` `[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]`**

设置各种操作的 I/O 带宽限制（单位为 KiB/s）。

**`--comstar_hg` `<string>`**

comstar 视图的宿主机组

**`--comstar_tg` `<string>`**

comstar 视图的目标组

**`--content` `<string>`**

允许的内容类型。

{% hint style="info" %}
值 *rootdir* 用于容器，值 *images* 用于虚拟机。
{% endhint %}

**`--content-dirs` `<string>`**

覆盖默认内容类型目录的设置。

**`--create-base-path` `<boolean>`（*默认值 \=* `yes`）**

如果基础目录不存在，则创建它。

**`--create-subdirs` `<boolean>`（*默认值 \=* `yes`）**

使用默认结构填充目录。

**`--data-pool` `<string>`**

数据池（仅用于纠删码）

**`--datastore` `<string>`**

Proxmox Backup Server 数据存储名称。

**`--disable` `<boolean>`**

用于禁用存储的标志。

**`--domain` `<string>`**

CIFS 域。

**`--encryption-key` `a file containing an encryption key, or the special value "autogen"`**

加密密钥。使用 *autogen* 自动生成一个不带口令的密钥。

**`--export` `<string>`**

NFS 导出路径。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--format` `<qcow2 | raw | subvol | vmdk>`**

默认镜像格式。

**`--fs-name` `<string>`**

Ceph 文件系统名称。

**`--fuse` `<boolean>`**

通过 FUSE 挂载 CephFS。

**`--is_mountpoint` `<string>`（*默认值 \=* `no`）**

将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是在此字段中使用目标路径的简写方式。

**`--iscsiprovider` `<string>`**

iscsi 提供程序

**`--keyring` `file containing the keyring to authenticate in the Ceph cluster`**

客户端密钥环内容（用于外部集群）。

**`--krbd` `<boolean>`（*默认值 \=* `0`）**

始终通过 krbd 内核模块访问 rbd。

**`--lio_tpg` `<string>`**

Linux LIO 目标的目标门户组

**`--master-pubkey` `a file containing a PEM-formatted master public key`**

经过 Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。

**`--max-protected-backups` `<integer> (-1 - N)`（*默认值 \=* `Unlimited for users with Datastore.Allocate privilege, 5 for other users`）**

每个客户机受保护备份的最大数量。使用 *-1* 表示不限制。

**`--mkdir` `<boolean>`（*默认值 \=* `yes`）**

如果目录不存在，则创建它并填充默认子目录。注意：已弃用，请改用 *create-base-path* 和 *create-subdirs* 选项。

**`--monhost` `<string>`**

监视器的 IP 地址（用于外部集群）。

**`--mountpoint` `<string>`**

挂载点

**`--namespace` `<string>`**

命名空间。

**`--nocow` `<boolean>`（*默认值 \=* `0`）**

在文件上设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。只有当数据安全性要求不高于单个采用 ext4 格式、底层没有 raid 系统的磁盘时，才应使用此选项。

**`--nodes` `<string>`**

适用此存储配置的节点列表。

**`--nowritecache` `<boolean>`**

禁用目标上的写入缓存

**`--options` `<string>`**

NFS/CIFS 挂载选项（参见 *man nfs* 或 *man mount.cifs*）

**`--password` `<password>`**

访问共享/数据存储的密码。

**`--path` `<string>`**

文件系统路径。

**`--pool` `<string>`**

池。

**`--port` `<integer> (1 - 65535)`**

使用此端口连接存储，代替默认端口（例如用于 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 *options* 选项，通过挂载选项配置端口。

**`--portal` `<string>`**

iSCSI 门户（IP 或 DNS 名称，可选端口）。

**`--preallocation` `<falloc | full | metadata | off>` （*默认值 \=* `metadata`）**

raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 *metadata* 会导致 preallocation\=off。

**`--prune-backups` `[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]`**

保留选项按时间间隔由短到长依次处理，最先处理的是 --keep-last。每个选项覆盖特定的时间段。我们将该时间段内的备份称为被此选项覆盖。下一个选项不会处理已经覆盖的备份，而只考虑更旧的备份。

**`--saferemove` `<boolean>`**

移除 LV 时将数据清零。

**`--saferemove-stepsize` `<1 | 16 | 2 | 32 | 4 | 8>` （*默认值 \=* `32`）**

擦除步长，单位为 MiB。将限制为存储支持的最大值。

**`--saferemove_throughput` `<string>`**

擦除吞吐量（cstream -t 参数值）。

**`--server` `<string>`**

服务器 IP 或 DNS 名称。

**`--share` `<string>`**

CIFS 共享。

**`--shared` `<boolean>`**

表示这是一个在所有节点（或 *nodes* 选项列出的所有节点）上具有相同内容的单一存储。它不会让本地存储的内容自动可供其他节点访问，只是将已共享的存储标记为共享！

**`--skip-cert-verification` `<boolean>` （*默认值 \=* `false`）**

禁用 TLS 证书验证，仅应在完全可信的网络上启用！

**`--smbversion` `<2.0 | 2.1 | 3 | 3.0 | 3.11 | default>` （*默认值 \=* `default`）**

SMB 协议版本。如果未设置，则为 *default*，协商使用客户端和服务器均支持的最高 SMB2\+ 版本。

**`--snapshot-as-volume-chain` `<boolean>` （*默认值 \=* `0`）**

启用通过卷后备链创建与存储厂商无关的快照的支持。

**`--sparse` `<boolean>`**

使用稀疏卷

**`--subdir` `<string>`**

要挂载的子目录。

**`--tagged_only` `<boolean>`**

仅列出带有 *pve-vm-ID* 标签的逻辑卷。

**`--target` `<string>`**

iSCSI 目标端。

**`--thinpool` `<string>`**

LVM 精简池的 LV 名称。

**`--username` `<string>`**

RBD ID。

**`--vgname` `<string>`**

卷组名称。

**`--zfs-base-path` `<string>`**

用于查找所创建 ZFS 块设备的基础路径。如果未指定，将在创建期间自动设置。通常为 */dev/zvol*。

## **pvesm alloc** `<storage> <vmid> <filename> <size>` `[OPTIONS]` <a href="#cli_pvesm_alloc" id="cli_pvesm_alloc"></a>

分配磁盘镜像。

**`<storage>`: `<storage ID>`**

存储标识符。

**`<vmid>`: `<integer> (100 - 999999999)`**

指定所属虚拟机

**`<filename>`: `<string>`**

要创建的文件名称。

**`<size>`: `\d+[MG]?`**

大小，单位为千字节（1024 字节）。可选后缀 *M*（兆字节，1024K）和 *G*（吉字节，1024M）

**`--format` `<qcow2 | raw | subvol | vmdk>`**

镜像的格式。

{% hint style="info" %}
需要选项：`size`
{% endhint %}

## **pvesm apiinfo** <a href="#cli_pvesm_apiinfo" id="cli_pvesm_apiinfo"></a>

返回 APIVER 和 APIAGE。

## **pvesm cifsscan** <a href="#cli_pvesm_cifsscan" id="cli_pvesm_cifsscan"></a>

*pvesm scan cifs* 的别名。

## **pvesm export** `<volume> <format> <filename>` `[OPTIONS]` <a href="#cli_pvesm_export" id="cli_pvesm_export"></a>

内部用于导出卷。

**`<volume>`: `<string>`**

卷标识符

**`<format>`: `<btrfs | qcow2+size | raw+size | tar+size | vmdk+size | zfs>`**

导出流格式

**`<filename>`: `<string>`**

目标文件名

**`--base` `(?^i:[a-z0-9_\-]{1,40})`**

增量流起始快照

**`--snapshot` `(?^i:[a-z0-9_\-]{1,40})`**

要导出的快照

**`--snapshot-list` `<string>`**

要传输的快照有序列表

**`--with-snapshots` `<boolean>` （*默认值 \=* `0`）**

是否在流中包含中间快照

## **pvesm extractconfig** `<volume>` <a href="#cli_pvesm_extractconfig" id="cli_pvesm_extractconfig"></a>

从 vzdump 备份归档中提取配置。

**`<volume>`: `<string>`**

卷标识符

## **pvesm free** `<volume>` `[OPTIONS]` <a href="#cli_pvesm_free" id="cli_pvesm_free"></a>

删除卷

**`<volume>`: `<string>`**

卷标识符

**`--delay` `<integer> (1 - 30)`**

等待任务完成的时间。如果任务在该时间内完成，则返回 *null*。

**`--storage` `<storage ID>`**

存储标识符。

## **pvesm help** `[OPTIONS]` <a href="#cli_pvesm_help" id="cli_pvesm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvesm import** `<volume> <format> <filename>` `[OPTIONS]` <a href="#cli_pvesm_import" id="cli_pvesm_import"></a>

内部用于导入卷。

**`<volume>`: `<string>`**

卷标识符

**`<format>`: `<btrfs | qcow2+size | raw+size | tar+size | vmdk+size | zfs>`**

导入流格式

**`<filename>`: `<string>`**

源文件名。对于 *\-*，使用 stdin；tcp://\<IP-or-CIDR\> 格式允许使用 TCP 连接，unix://PATH-TO-SOCKET 格式允许使用 UNIX 套接字作为输入。其他情况下，将该文件视为普通文件。

**`--allow-rename` `<boolean>` （*默认值 \=* `0`）**

如果请求的卷 ID 已存在，则选择新的卷 ID，而不是抛出错误。

**`--base` `(?^i:[a-z0-9_\-]{1,40})`**

增量流的基础快照

**`--delete-snapshot` `(?^i:[a-z0-9_\-]{1,80})`**

成功时要删除的快照

**`--snapshot` `(?^i:[a-z0-9_\-]{1,40})`**

如果流包含快照，则为当前状态快照

**`--with-snapshots` `<boolean>` （*默认值 \=* `0`）**

流是否包含中间快照

## **pvesm iscsiscan** <a href="#cli_pvesm_iscsiscan" id="cli_pvesm_iscsiscan"></a>

*pvesm scan iscsi* 的别名。

## **pvesm list** `<storage>` `[OPTIONS]` <a href="#cli_pvesm_list" id="cli_pvesm_list"></a>

列出存储内容。

**`<storage>`: `<storage ID>`**

存储标识符。

**`--content` `<string>`**

仅列出此类型的内容。

**`--vmid` `<integer> (100 - 999999999)`**

仅列出此虚拟机的镜像

## **pvesm lvmscan** <a href="#cli_pvesm_lvmscan" id="cli_pvesm_lvmscan"></a>

*pvesm scan lvm* 的别名。

## **pvesm lvmthinscan** <a href="#cli_pvesm_lvmthinscan" id="cli_pvesm_lvmthinscan"></a>

*pvesm scan lvmthin* 的别名。

## **pvesm nfsscan** <a href="#cli_pvesm_nfsscan" id="cli_pvesm_nfsscan"></a>

*pvesm scan nfs* 的别名。

## **pvesm path** `<volume>` <a href="#cli_pvesm_path" id="cli_pvesm_path"></a>

获取指定卷的文件系统路径

**`<volume>`: `<string>`**

卷标识符

## **pvesm prune-backups** `<storage>` `[OPTIONS]` <a href="#cli_pvesm_prune-backups" id="cli_pvesm_prune-backups"></a>

清理备份。只考虑使用标准命名规则的备份。如果未指定任何保留选项，则使用存储配置中的保留选项。

**`<storage>`: `<storage ID>`**

存储标识符。

**`--dry-run` `<boolean>`**

仅显示将要清理的内容，不执行任何删除。

**`--keep-all` `<boolean>`**

保留所有备份。为 true 时与其他选项冲突。

**`--keep-daily` `<N>`**

保留最近 \<N\> 个不同日期的备份。如果同一天有多个备份，只保留最新的。

**`--keep-hourly` `<N>`**

保留最近 \<N\> 个不同小时的备份。如果同一小时有多个备份，只保留最新的。

**`--keep-last` `<N>`**

保留最后 \<N\> 个备份。

**`--keep-monthly` `<N>`**

保留最近 \<N\> 个不同月份的备份。如果同一个月有多个备份，只保留最新的。

**`--keep-weekly` `<N>`**

保留最近 \<N\> 个不同周的备份。如果同一周有多个备份，则只保留最新的备份。

**`--keep-yearly` `<N>`**

保留最近 \<N\> 个不同年份的备份。如果同一年有多个备份，则只保留最新的备份。

**`--type` `<lxc | qemu>`**

为 *qemu* 或 *lxc*。仅考虑此类型客户机的备份。

**`--vmid` `<integer> (100 - 999999999)`**

仅考虑此客户机的备份。

## **pvesm remove** `<storage>` <a href="#cli_pvesm_remove" id="cli_pvesm_remove"></a>

删除存储配置。

**`<storage>`: `<storage ID>`**

存储标识符。

## **pvesm scan cifs** `<server>` `[OPTIONS]` <a href="#cli_pvesm_scan_cifs" id="cli_pvesm_scan_cifs"></a>

扫描远程 CIFS 服务器。

**`<server>`: `<string>`**

服务器地址（名称或 IP）。

**`--domain` `<string>`**

SMB 域（工作组）。

**`--password` `<password>`**

用户密码。

**`--username` `<string>`**

用户名。

## **pvesm scan iscsi** `<portal>` <a href="#cli_pvesm_scan_iscsi" id="cli_pvesm_scan_iscsi"></a>

扫描远程 iSCSI 服务器。

**`<portal>`: `<string>`**

iSCSI 门户（IP 或 DNS 名称，可选端口）。

## **pvesm scan lvm** <a href="#cli_pvesm_scan_lvm" id="cli_pvesm_scan_lvm"></a>

列出本地 LVM 卷组。

## **pvesm scan lvmthin** `<vg>` <a href="#cli_pvesm_scan_lvmthin" id="cli_pvesm_scan_lvmthin"></a>

列出本地 LVM 精简池。

**`<vg>`: `[a-zA-Z0-9\.\+\_][a-zA-Z0-9\.\+\_\-]+`**

没有可用的说明

## **pvesm scan nfs** `<server>` <a href="#cli_pvesm_scan_nfs" id="cli_pvesm_scan_nfs"></a>

扫描远程 NFS 服务器。

**`<server>`: `<string>`**

服务器地址（名称或 IP）。

## **pvesm scan pbs** `<server> <username> --password <string>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesm_scan_pbs" id="cli_pvesm_scan_pbs"></a>

扫描远程 Proxmox Backup Server。

**`<server>`: `<string>`**

服务器地址（名称或 IP）。

**`<username>`: `<string>`**

用户名或 API 令牌 ID。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--password` `<string>`**

用户密码或 API 令牌密钥。

**`--port` `<integer> (1 - 65535)` （*默认值 \=* `8007`）**

可选端口。

## **pvesm scan zfs** <a href="#cli_pvesm_scan_zfs" id="cli_pvesm_scan_zfs"></a>

扫描本地节点的 zfs 池列表。

## **pvesm set** `<storage>` `[OPTIONS]` <a href="#cli_pvesm_set" id="cli_pvesm_set"></a>

更新存储配置。

**`<storage>`: `<storage ID>`**

存储标识符。

**`--blocksize` `<a power of 2 with optional k or m suffix>`**

ZFS 块大小

**`--bwlimit` `[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]`**

设置各种操作的 I/O 带宽限制（单位为 KiB/s）。

**`--comstar_hg` `<string>`**

comstar 视图的宿主机组

**`--comstar_tg` `<string>`**

comstar 视图的目标组

**`--content` `<string>`**

允许的内容类型。

{% hint style="info" %}
值 *rootdir* 用于容器，值 *images* 用于虚拟机。
{% endhint %}

**`--content-dirs` `<string>`**

覆盖默认内容类型目录的设置。

**`--create-base-path` `<boolean>`（*默认值 \=* `yes`）**

如果基础目录不存在，则创建它。

**`--create-subdirs` `<boolean>`（*默认值 \=* `yes`）**

使用默认结构填充目录。

**`--data-pool` `<string>`**

数据池（仅用于纠删码）

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

用于禁用存储的标志。

**`--domain` `<string>`**

CIFS 域。

**`--encryption-key` `a file containing an encryption key, or the special value "autogen"`**

加密密钥。使用 *autogen* 自动生成一个不带口令的密钥。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--format` `<qcow2 | raw | subvol | vmdk>`**

默认镜像格式。

**`--fs-name` `<string>`**

Ceph 文件系统名称。

**`--fuse` `<boolean>`**

通过 FUSE 挂载 CephFS。

**`--is_mountpoint` `<string>`（*默认值 \=* `no`）**

将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是在此字段中使用目标路径的简写方式。

**`--keyring` `file containing the keyring to authenticate in the Ceph cluster`**

客户端密钥环内容（用于外部集群）。

**`--krbd` `<boolean>`（*默认值 \=* `0`）**

始终通过 krbd 内核模块访问 rbd。

**`--lio_tpg` `<string>`**

Linux LIO 目标的目标门户组

**`--master-pubkey` `a file containing a PEM-formatted master public key`**

经过 Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。

**`--max-protected-backups` `<integer> (-1 - N)`（*默认值 \=* `Unlimited for users with Datastore.Allocate privilege, 5 for other users`）**

每个客户机受保护备份的最大数量。使用 *-1* 表示不限制。

**`--mkdir` `<boolean>`（*默认值 \=* `yes`）**

如果目录不存在，则创建它并填充默认子目录。注意：已弃用，请改用 *create-base-path* 和 *create-subdirs* 选项。

**`--monhost` `<string>`**

监视器的 IP 地址（用于外部集群）。

**`--mountpoint` `<string>`**

挂载点

**`--namespace` `<string>`**

命名空间。

**`--nocow` `<boolean>`（*默认值 \=* `0`）**

在文件上设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。只有当数据安全性要求不高于单个采用 ext4 格式、底层没有 raid 系统的磁盘时，才应使用此选项。

**`--nodes` `<string>`**

适用此存储配置的节点列表。

**`--nowritecache` `<boolean>`**

禁用目标上的写入缓存

**`--options` `<string>`**

NFS/CIFS 挂载选项（参见 *man nfs* 或 *man mount.cifs*）

**`--password` `<password>`**

访问共享/数据存储的密码。

**`--pool` `<string>`**

池。

**`--port` `<integer> (1 - 65535)`**

使用此端口连接存储，代替默认端口（例如用于 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 *options* 选项，通过挂载选项配置端口。

**`--preallocation` `<falloc | full | metadata | off>` （*默认值 \=* `metadata`）**

raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 *metadata* 会导致 preallocation\=off。

**`--prune-backups` `[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]`**

保留选项按时间间隔由短到长依次处理，最先处理的是 --keep-last。每个选项覆盖特定的时间段。我们将该时间段内的备份称为被此选项覆盖。下一个选项不会处理已经覆盖的备份，而只考虑更旧的备份。

**`--saferemove` `<boolean>`**

移除 LV 时将数据清零。

**`--saferemove-stepsize` `<1 | 16 | 2 | 32 | 4 | 8>` （*默认值 \=* `32`）**

擦除步长，单位为 MiB。将限制为存储支持的最大值。

**`--saferemove_throughput` `<string>`**

擦除吞吐量（cstream -t 参数值）。

**`--server` `<string>`**

服务器 IP 或 DNS 名称。

**`--shared` `<boolean>`**

表示这是一个在所有节点（或 *nodes* 选项列出的所有节点）上具有相同内容的单一存储。它不会让本地存储的内容自动可供其他节点访问，只是将已共享的存储标记为共享！

**`--skip-cert-verification` `<boolean>` （*默认值 \=* `false`）**

禁用 TLS 证书验证，仅应在完全可信的网络上启用！

**`--smbversion` `<2.0 | 2.1 | 3 | 3.0 | 3.11 | default>` （*默认值 \=* `default`）**

SMB 协议版本。如果未设置，则为 *default*，协商使用客户端和服务器均支持的最高 SMB2\+ 版本。

**`--snapshot-as-volume-chain` `<boolean>` （*默认值 \=* `0`）**

启用通过卷后备链创建与存储厂商无关的快照的支持。

**`--sparse` `<boolean>`**

使用稀疏卷

**`--subdir` `<string>`**

要挂载的子目录。

**`--tagged_only` `<boolean>`**

仅列出带有 *pve-vm-ID* 标签的逻辑卷。

**`--username` `<string>`**

RBD ID。

**`--zfs-base-path` `<string>`**

用于查找所创建 ZFS 块设备的基础路径。如果未指定，将在创建期间自动设置。通常为 */dev/zvol*。

## **pvesm status** `[OPTIONS]` <a href="#cli_pvesm_status" id="cli_pvesm_status"></a>

获取所有数据存储的状态。

**`--content` `<string>`**

仅列出支持此内容类型的存储。

**`--enabled` `<boolean>` （*默认值 \=* `0`）**

仅列出已启用的存储（配置中未禁用）。

**`--format` `<boolean>` （*默认值 \=* `0`）**

包含格式信息

**`--storage` `<storage ID>`**

仅列出指定存储的状态

**`--target` `<string>`**

如果 target 与 *node* 不同，则只列出其内容可由此 *node* 和指定的 *target* 节点访问的共享存储。

## **pvesm zfsscan** <a href="#cli_pvesm_zfsscan" id="cli_pvesm_zfsscan"></a>

*pvesm scan zfs* 的别名。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
