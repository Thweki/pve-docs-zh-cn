# 22\. 附录 A：命令行接口 <a href="#command_line_interface" id="command_line_interface"></a>

## 22.1. 常规 <a href="#cli_general" id="cli_general"></a>

关于选项在历史上不统一的大小写风格，请参阅[配置文件相关章节](../24-configuration-files-2/README.md#configuration_files_casing)。

## 22.2. 输出格式选项 `[FORMAT_OPTIONS]` <a href="#output_format_options_span_class_monospaced_format_options_span" id="output_format_options_span_class_monospaced_format_options_span"></a>

可以使用 `--output-format` 参数指定输出格式。默认格式 <em>text</em> 使用 ASCII 字符画为表格绘制美观的边框。此外，还会将某些值转换为易于阅读的文本，例如：

- Unix 纪元时间显示为 ISO 8601 日期字符串。
- 时长显示为周/天/小时/分钟/秒的数量，即 `1d 5h`。
- 字节大小值包含单位（`B`、`KiB`、`MiB`、`GiB`、`TiB`、`PiB`）。
- 小数显示为百分比，即 1.0 显示为 100%。

还可以使用选项 `--quiet` 完全禁止输出。

**`--human-readable` `<boolean>`（<em>默认值 \=</em> `1`）**

调用输出渲染函数，生成易于阅读的文本。

**`--noborder` `<boolean>`（<em>默认值 \=</em> `0`）**

不绘制边框（适用于 <em>text</em> 格式）。

**`--noheader` `<boolean>`（<em>默认值 \=</em> `0`）**

不显示列标题（适用于 <em>text</em> 格式）。

**`--output-format` `<json | json-pretty | text | yaml>`（<em>默认值 \=</em> `text`）**

输出格式。

**`--quiet` `<boolean>`**

禁止打印结果。

## 22.3. <strong>pvesm</strong> \- Proxmox VE 存储管理器 <a href="#strong_pvesm_strong_proxmox_ve_storage_manager" id="strong_pvesm_strong_proxmox_ve_storage_manager"></a>

### <strong>pvesm</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesm" id="cli_pvesm"></a>

### <strong>pvesm add</strong> `<type> <storage>` `[OPTIONS]` <a href="#cli_pvesm_add" id="cli_pvesm_add"></a>

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
值 <em>rootdir</em> 用于容器，值 <em>images</em> 用于虚拟机。
{% endhint %}

**`--content-dirs` `<string>`**

覆盖默认内容类型目录的设置。

**`--create-base-path` `<boolean>`（<em>默认值 \=</em> `yes`）**

如果基础目录不存在，则创建它。

**`--create-subdirs` `<boolean>`（<em>默认值 \=</em> `yes`）**

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

加密密钥。使用 <em>autogen</em> 自动生成一个不带口令的密钥。

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

**`--is_mountpoint` `<string>`（<em>默认值 \=</em> `no`）**

将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是在此字段中使用目标路径的简写方式。

**`--iscsiprovider` `<string>`**

iscsi 提供程序

**`--keyring` `file containing the keyring to authenticate in the Ceph cluster`**

客户端密钥环内容（用于外部集群）。

**`--krbd` `<boolean>`（<em>默认值 \=</em> `0`）**

始终通过 krbd 内核模块访问 rbd。

**`--lio_tpg` `<string>`**

Linux LIO 目标的目标门户组

**`--master-pubkey` `a file containing a PEM-formatted master public key`**

经过 Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。

**`--max-protected-backups` `<integer> (-1 - N)`（<em>默认值 \=</em> `Unlimited for users with Datastore.Allocate privilege, 5 for other users`）**

每个客户机受保护备份的最大数量。使用 <em>-1</em> 表示不限制。

**`--mkdir` `<boolean>`（<em>默认值 \=</em> `yes`）**

如果目录不存在，则创建它并填充默认子目录。注意：已弃用，请改用 <em>create-base-path</em> 和 <em>create-subdirs</em> 选项。

**`--monhost` `<string>`**

监视器的 IP 地址（用于外部集群）。

**`--mountpoint` `<string>`**

挂载点

**`--namespace` `<string>`**

命名空间。

**`--nocow` `<boolean>`（<em>默认值 \=</em> `0`）**

在文件上设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。只有当数据安全性要求不高于单个采用 ext4 格式、底层没有 raid 系统的磁盘时，才应使用此选项。

**`--nodes` `<string>`**

适用此存储配置的节点列表。

**`--nowritecache` `<boolean>`**

禁用目标上的写入缓存

**`--options` `<string>`**

NFS/CIFS 挂载选项（参见 <em>man nfs</em> 或 <em>man mount.cifs</em>）

**`--password` `<password>`**

访问共享/数据存储的密码。

**`--path` `<string>`**

文件系统路径。

**`--pool` `<string>`**

池。

**`--port` `<integer> (1 - 65535)`**

使用此端口连接存储，代替默认端口（例如用于 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 <em>options</em> 选项，通过挂载选项配置端口。

**`--portal` `<string>`**

iSCSI 门户（IP 或 DNS 名称，可选端口）。

**`--preallocation` `<falloc | full | metadata | off>` （<em>默认值 \=</em> `metadata`）**

raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 <em>metadata</em> 会导致 preallocation\=off。

**`--prune-backups` `[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]`**

保留选项按时间间隔由短到长依次处理，最先处理的是 --keep-last。每个选项覆盖特定的时间段。我们将该时间段内的备份称为被此选项覆盖。下一个选项不会处理已经覆盖的备份，而只考虑更旧的备份。

**`--saferemove` `<boolean>`**

移除 LV 时将数据清零。

**`--saferemove-stepsize` `<1 | 16 | 2 | 32 | 4 | 8>` （<em>默认值 \=</em> `32`）**

擦除步长，单位为 MiB。将限制为存储支持的最大值。

**`--saferemove_throughput` `<string>`**

擦除吞吐量（cstream -t 参数值）。

**`--server` `<string>`**

服务器 IP 或 DNS 名称。

**`--share` `<string>`**

CIFS 共享。

**`--shared` `<boolean>`**

表示这是一个在所有节点（或 <em>nodes</em> 选项列出的所有节点）上具有相同内容的单一存储。它不会让本地存储的内容自动可供其他节点访问，只是将已共享的存储标记为共享！

**`--skip-cert-verification` `<boolean>` （<em>默认值 \=</em> `false`）**

禁用 TLS 证书验证，仅应在完全可信的网络上启用！

**`--smbversion` `<2.0 | 2.1 | 3 | 3.0 | 3.11 | default>` （<em>默认值 \=</em> `default`）**

SMB 协议版本。如果未设置，则为 <em>default</em>，协商使用客户端和服务器均支持的最高 SMB2\+ 版本。

**`--snapshot-as-volume-chain` `<boolean>` （<em>默认值 \=</em> `0`）**

启用通过卷后备链创建与存储厂商无关的快照的支持。

**`--sparse` `<boolean>`**

使用稀疏卷

**`--subdir` `<string>`**

要挂载的子目录。

**`--tagged_only` `<boolean>`**

仅列出带有 <em>pve-vm-ID</em> 标签的逻辑卷。

**`--target` `<string>`**

iSCSI 目标端。

**`--thinpool` `<string>`**

LVM 精简池的 LV 名称。

**`--username` `<string>`**

RBD ID。

**`--vgname` `<string>`**

卷组名称。

**`--zfs-base-path` `<string>`**

用于查找所创建 ZFS 块设备的基础路径。如果未指定，将在创建期间自动设置。通常为 <em>/dev/zvol</em>。

### <strong>pvesm alloc</strong> `<storage> <vmid> <filename> <size>` `[OPTIONS]` <a href="#cli_pvesm_alloc" id="cli_pvesm_alloc"></a>

分配磁盘镜像。

**`<storage>`: `<storage ID>`**

存储标识符。

**`<vmid>`: `<integer> (100 - 999999999)`**

指定所属虚拟机

**`<filename>`: `<string>`**

要创建的文件名称。

**`<size>`: `\d+[MG]?`**

大小，单位为千字节（1024 字节）。可选后缀 <em>M</em>（兆字节，1024K）和 <em>G</em>（吉字节，1024M）

**`--format` `<qcow2 | raw | subvol | vmdk>`**

镜像的格式。

{% hint style="info" %}
需要选项：`size`
{% endhint %}

### <strong>pvesm apiinfo</strong> <a href="#cli_pvesm_apiinfo" id="cli_pvesm_apiinfo"></a>

返回 APIVER 和 APIAGE。

### <strong>pvesm cifsscan</strong> <a href="#cli_pvesm_cifsscan" id="cli_pvesm_cifsscan"></a>

<em>pvesm scan cifs</em> 的别名。

### <strong>pvesm export</strong> `<volume> <format> <filename>` `[OPTIONS]` <a href="#cli_pvesm_export" id="cli_pvesm_export"></a>

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

**`--with-snapshots` `<boolean>` （<em>默认值 \=</em> `0`）**

是否在流中包含中间快照

### <strong>pvesm extractconfig</strong> `<volume>` <a href="#cli_pvesm_extractconfig" id="cli_pvesm_extractconfig"></a>

从 vzdump 备份归档中提取配置。

**`<volume>`: `<string>`**

卷标识符

### <strong>pvesm free</strong> `<volume>` `[OPTIONS]` <a href="#cli_pvesm_free" id="cli_pvesm_free"></a>

删除卷

**`<volume>`: `<string>`**

卷标识符

**`--delay` `<integer> (1 - 30)`**

等待任务完成的时间。如果任务在该时间内完成，则返回 <em>null</em>。

**`--storage` `<storage ID>`**

存储标识符。

### <strong>pvesm help</strong> `[OPTIONS]` <a href="#cli_pvesm_help" id="cli_pvesm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvesm import</strong> `<volume> <format> <filename>` `[OPTIONS]` <a href="#cli_pvesm_import" id="cli_pvesm_import"></a>

内部用于导入卷。

**`<volume>`: `<string>`**

卷标识符

**`<format>`: `<btrfs | qcow2+size | raw+size | tar+size | vmdk+size | zfs>`**

导入流格式

**`<filename>`: `<string>`**

源文件名。对于 <em>\-</em>，使用 stdin；tcp://\<IP-or-CIDR\> 格式允许使用 TCP 连接，unix://PATH-TO-SOCKET 格式允许使用 UNIX 套接字作为输入。其他情况下，将该文件视为普通文件。

**`--allow-rename` `<boolean>` （<em>默认值 \=</em> `0`）**

如果请求的卷 ID 已存在，则选择新的卷 ID，而不是抛出错误。

**`--base` `(?^i:[a-z0-9_\-]{1,40})`**

增量流的基础快照

**`--delete-snapshot` `(?^i:[a-z0-9_\-]{1,80})`**

成功时要删除的快照

**`--snapshot` `(?^i:[a-z0-9_\-]{1,40})`**

如果流包含快照，则为当前状态快照

**`--with-snapshots` `<boolean>` （<em>默认值 \=</em> `0`）**

流是否包含中间快照

### <strong>pvesm iscsiscan</strong> <a href="#cli_pvesm_iscsiscan" id="cli_pvesm_iscsiscan"></a>

<em>pvesm scan iscsi</em> 的别名。

### <strong>pvesm list</strong> `<storage>` `[OPTIONS]` <a href="#cli_pvesm_list" id="cli_pvesm_list"></a>

列出存储内容。

**`<storage>`: `<storage ID>`**

存储标识符。

**`--content` `<string>`**

仅列出此类型的内容。

**`--vmid` `<integer> (100 - 999999999)`**

仅列出此虚拟机的镜像

### <strong>pvesm lvmscan</strong> <a href="#cli_pvesm_lvmscan" id="cli_pvesm_lvmscan"></a>

<em>pvesm scan lvm</em> 的别名。

### <strong>pvesm lvmthinscan</strong> <a href="#cli_pvesm_lvmthinscan" id="cli_pvesm_lvmthinscan"></a>

<em>pvesm scan lvmthin</em> 的别名。

### <strong>pvesm nfsscan</strong> <a href="#cli_pvesm_nfsscan" id="cli_pvesm_nfsscan"></a>

<em>pvesm scan nfs</em> 的别名。

### <strong>pvesm path</strong> `<volume>` <a href="#cli_pvesm_path" id="cli_pvesm_path"></a>

获取指定卷的文件系统路径

**`<volume>`: `<string>`**

卷标识符

### <strong>pvesm prune-backups</strong> `<storage>` `[OPTIONS]` <a href="#cli_pvesm_prune-backups" id="cli_pvesm_prune-backups"></a>

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

为 <em>qemu</em> 或 <em>lxc</em>。仅考虑此类型客户机的备份。

**`--vmid` `<integer> (100 - 999999999)`**

仅考虑此客户机的备份。

### <strong>pvesm remove</strong> `<storage>` <a href="#cli_pvesm_remove" id="cli_pvesm_remove"></a>

删除存储配置。

**`<storage>`: `<storage ID>`**

存储标识符。

### <strong>pvesm scan cifs</strong> `<server>` `[OPTIONS]` <a href="#cli_pvesm_scan_cifs" id="cli_pvesm_scan_cifs"></a>

扫描远程 CIFS 服务器。

**`<server>`: `<string>`**

服务器地址（名称或 IP）。

**`--domain` `<string>`**

SMB 域（工作组）。

**`--password` `<password>`**

用户密码。

**`--username` `<string>`**

用户名。

### <strong>pvesm scan iscsi</strong> `<portal>` <a href="#cli_pvesm_scan_iscsi" id="cli_pvesm_scan_iscsi"></a>

扫描远程 iSCSI 服务器。

**`<portal>`: `<string>`**

iSCSI 门户（IP 或 DNS 名称，可选端口）。

### <strong>pvesm scan lvm</strong> <a href="#cli_pvesm_scan_lvm" id="cli_pvesm_scan_lvm"></a>

列出本地 LVM 卷组。

### <strong>pvesm scan lvmthin</strong> `<vg>` <a href="#cli_pvesm_scan_lvmthin" id="cli_pvesm_scan_lvmthin"></a>

列出本地 LVM 精简池。

**`<vg>`: `[a-zA-Z0-9\.\+\_][a-zA-Z0-9\.\+\_\-]+`**

没有可用的说明

### <strong>pvesm scan nfs</strong> `<server>` <a href="#cli_pvesm_scan_nfs" id="cli_pvesm_scan_nfs"></a>

扫描远程 NFS 服务器。

**`<server>`: `<string>`**

服务器地址（名称或 IP）。

### <strong>pvesm scan pbs</strong> `<server> <username> --password <string>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesm_scan_pbs" id="cli_pvesm_scan_pbs"></a>

扫描远程 Proxmox Backup Server。

**`<server>`: `<string>`**

服务器地址（名称或 IP）。

**`<username>`: `<string>`**

用户名或 API 令牌 ID。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--password` `<string>`**

用户密码或 API 令牌密钥。

**`--port` `<integer> (1 - 65535)` （<em>默认值 \=</em> `8007`）**

可选端口。

### <strong>pvesm scan zfs</strong> <a href="#cli_pvesm_scan_zfs" id="cli_pvesm_scan_zfs"></a>

扫描本地节点的 zfs 池列表。

### <strong>pvesm set</strong> `<storage>` `[OPTIONS]` <a href="#cli_pvesm_set" id="cli_pvesm_set"></a>

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
值 <em>rootdir</em> 用于容器，值 <em>images</em> 用于虚拟机。
{% endhint %}

**`--content-dirs` `<string>`**

覆盖默认内容类型目录的设置。

**`--create-base-path` `<boolean>`（<em>默认值 \=</em> `yes`）**

如果基础目录不存在，则创建它。

**`--create-subdirs` `<boolean>`（<em>默认值 \=</em> `yes`）**

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

加密密钥。使用 <em>autogen</em> 自动生成一个不带口令的密钥。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--format` `<qcow2 | raw | subvol | vmdk>`**

默认镜像格式。

**`--fs-name` `<string>`**

Ceph 文件系统名称。

**`--fuse` `<boolean>`**

通过 FUSE 挂载 CephFS。

**`--is_mountpoint` `<string>`（<em>默认值 \=</em> `no`）**

将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是在此字段中使用目标路径的简写方式。

**`--keyring` `file containing the keyring to authenticate in the Ceph cluster`**

客户端密钥环内容（用于外部集群）。

**`--krbd` `<boolean>`（<em>默认值 \=</em> `0`）**

始终通过 krbd 内核模块访问 rbd。

**`--lio_tpg` `<string>`**

Linux LIO 目标的目标门户组

**`--master-pubkey` `a file containing a PEM-formatted master public key`**

经过 Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。

**`--max-protected-backups` `<integer> (-1 - N)`（<em>默认值 \=</em> `Unlimited for users with Datastore.Allocate privilege, 5 for other users`）**

每个客户机受保护备份的最大数量。使用 <em>-1</em> 表示不限制。

**`--mkdir` `<boolean>`（<em>默认值 \=</em> `yes`）**

如果目录不存在，则创建它并填充默认子目录。注意：已弃用，请改用 <em>create-base-path</em> 和 <em>create-subdirs</em> 选项。

**`--monhost` `<string>`**

监视器的 IP 地址（用于外部集群）。

**`--mountpoint` `<string>`**

挂载点

**`--namespace` `<string>`**

命名空间。

**`--nocow` `<boolean>`（<em>默认值 \=</em> `0`）**

在文件上设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。只有当数据安全性要求不高于单个采用 ext4 格式、底层没有 raid 系统的磁盘时，才应使用此选项。

**`--nodes` `<string>`**

适用此存储配置的节点列表。

**`--nowritecache` `<boolean>`**

禁用目标上的写入缓存

**`--options` `<string>`**

NFS/CIFS 挂载选项（参见 <em>man nfs</em> 或 <em>man mount.cifs</em>）

**`--password` `<password>`**

访问共享/数据存储的密码。

**`--pool` `<string>`**

池。

**`--port` `<integer> (1 - 65535)`**

使用此端口连接存储，代替默认端口（例如用于 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 <em>options</em> 选项，通过挂载选项配置端口。

**`--preallocation` `<falloc | full | metadata | off>` （<em>默认值 \=</em> `metadata`）**

raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 <em>metadata</em> 会导致 preallocation\=off。

**`--prune-backups` `[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]`**

保留选项按时间间隔由短到长依次处理，最先处理的是 --keep-last。每个选项覆盖特定的时间段。我们将该时间段内的备份称为被此选项覆盖。下一个选项不会处理已经覆盖的备份，而只考虑更旧的备份。

**`--saferemove` `<boolean>`**

移除 LV 时将数据清零。

**`--saferemove-stepsize` `<1 | 16 | 2 | 32 | 4 | 8>` （<em>默认值 \=</em> `32`）**

擦除步长，单位为 MiB。将限制为存储支持的最大值。

**`--saferemove_throughput` `<string>`**

擦除吞吐量（cstream -t 参数值）。

**`--server` `<string>`**

服务器 IP 或 DNS 名称。

**`--shared` `<boolean>`**

表示这是一个在所有节点（或 <em>nodes</em> 选项列出的所有节点）上具有相同内容的单一存储。它不会让本地存储的内容自动可供其他节点访问，只是将已共享的存储标记为共享！

**`--skip-cert-verification` `<boolean>` （<em>默认值 \=</em> `false`）**

禁用 TLS 证书验证，仅应在完全可信的网络上启用！

**`--smbversion` `<2.0 | 2.1 | 3 | 3.0 | 3.11 | default>` （<em>默认值 \=</em> `default`）**

SMB 协议版本。如果未设置，则为 <em>default</em>，协商使用客户端和服务器均支持的最高 SMB2\+ 版本。

**`--snapshot-as-volume-chain` `<boolean>` （<em>默认值 \=</em> `0`）**

启用通过卷后备链创建与存储厂商无关的快照的支持。

**`--sparse` `<boolean>`**

使用稀疏卷

**`--subdir` `<string>`**

要挂载的子目录。

**`--tagged_only` `<boolean>`**

仅列出带有 <em>pve-vm-ID</em> 标签的逻辑卷。

**`--username` `<string>`**

RBD ID。

**`--zfs-base-path` `<string>`**

用于查找所创建 ZFS 块设备的基础路径。如果未指定，将在创建期间自动设置。通常为 <em>/dev/zvol</em>。

### <strong>pvesm status</strong> `[OPTIONS]` <a href="#cli_pvesm_status" id="cli_pvesm_status"></a>

获取所有数据存储的状态。

**`--content` `<string>`**

仅列出支持此内容类型的存储。

**`--enabled` `<boolean>` （<em>默认值 \=</em> `0`）**

仅列出已启用的存储（配置中未禁用）。

**`--format` `<boolean>` （<em>默认值 \=</em> `0`）**

包含格式信息

**`--storage` `<storage ID>`**

仅列出指定存储的状态

**`--target` `<string>`**

如果 target 与 <em>node</em> 不同，则只列出其内容可由此 <em>node</em> 和指定的 <em>target</em> 节点访问的共享存储。

### <strong>pvesm zfsscan</strong> <a href="#cli_pvesm_zfsscan" id="cli_pvesm_zfsscan"></a>

<em>pvesm scan zfs</em> 的别名。

## 22.4. <strong>pvesubscription</strong> \- Proxmox VE 订阅管理器 <a href="#strong_pvesubscription_strong_proxmox_ve_subscription_manager" id="strong_pvesubscription_strong_proxmox_ve_subscription_manager"></a>

### <strong>pvesubscription</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesubscription" id="cli_pvesubscription"></a>

### <strong>pvesubscription delete</strong> <a href="#cli_pvesubscription_delete" id="cli_pvesubscription_delete"></a>

删除此节点的订阅密钥。

### <strong>pvesubscription get</strong> <a href="#cli_pvesubscription_get" id="cli_pvesubscription_get"></a>

读取订阅信息。

### <strong>pvesubscription help</strong> `[OPTIONS]` <a href="#cli_pvesubscription_help" id="cli_pvesubscription_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvesubscription set</strong> `<key>` <a href="#cli_pvesubscription_set" id="cli_pvesubscription_set"></a>

设置订阅密钥。

**`<key>`: `\s*pve([1248])([cbsp])-(arm-)?[0-9a-f]{10}\s*`**

Proxmox VE 订阅密钥

### <strong>pvesubscription set-offline-key</strong> `<data>` <a href="#cli_pvesubscription_set-offline-key" id="cli_pvesubscription_set-offline-key"></a>

仅供内部使用！要设置离线密钥，请改用 proxmox-offline-mirror-helper 软件包。

**`<data>`: `<string>`**

已签名的订阅信息数据块

### <strong>pvesubscription update</strong> `[OPTIONS]` <a href="#cli_pvesubscription_update" id="cli_pvesubscription_update"></a>

更新订阅信息。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

始终连接服务器，即使本地缓存仍有效。

## 22.5. <strong>pveperf</strong> \- Proxmox VE 基准测试脚本 <a href="#strong_pveperf_strong_proxmox_ve_benchmark_script" id="strong_pveperf_strong_proxmox_ve_benchmark_script"></a>

<strong>pveperf</strong> `[PATH]`

## 22.6. <strong>pveceph</strong> \- 管理 Proxmox VE 节点上的 CEPH 服务 <a href="#strong_pveceph_strong_manage_ceph_services_on_proxmox_ve_nodes" id="strong_pveceph_strong_manage_ceph_services_on_proxmox_ve_nodes"></a>

### <strong>pveceph</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveceph" id="cli_pveceph"></a>

### <strong>pveceph auth status</strong> `[FORMAT_OPTIONS]` <a href="#cli_pveceph_auth_status" id="cli_pveceph_auth_status"></a>

显示 cephx 密钥密码算法和 aes256k 迁移先决条件。

### <strong>pveceph createmgr</strong> <a href="#cli_pveceph_createmgr" id="cli_pveceph_createmgr"></a>

<em>pveceph mgr create</em> 的别名。

### <strong>pveceph createmon</strong> <a href="#cli_pveceph_createmon" id="cli_pveceph_createmon"></a>

<em>pveceph mon create</em> 的别名。

### <strong>pveceph createosd</strong> <a href="#cli_pveceph_createosd" id="cli_pveceph_createosd"></a>

<em>pveceph osd create</em> 的别名。

### <strong>pveceph createpool</strong> <a href="#cli_pveceph_createpool" id="cli_pveceph_createpool"></a>

<em>pveceph pool create</em> 的别名。

### <strong>pveceph destroymgr</strong> <a href="#cli_pveceph_destroymgr" id="cli_pveceph_destroymgr"></a>

<em>pveceph mgr destroy</em> 的别名。

### <strong>pveceph destroymon</strong> <a href="#cli_pveceph_destroymon" id="cli_pveceph_destroymon"></a>

<em>pveceph mon destroy</em> 的别名。

### <strong>pveceph destroyosd</strong> <a href="#cli_pveceph_destroyosd" id="cli_pveceph_destroyosd"></a>

<em>pveceph osd destroy</em> 的别名。

### <strong>pveceph destroypool</strong> <a href="#cli_pveceph_destroypool" id="cli_pveceph_destroypool"></a>

<em>pveceph pool destroy</em> 的别名。

### <strong>pveceph fs create</strong> `[OPTIONS]` <a href="#cli_pveceph_fs_create" id="cli_pveceph_fs_create"></a>

创建 Ceph 文件系统

**`--add-storage` `<boolean>` （<em>默认值 \=</em> `0`）**

将创建的 CephFS 配置为此集群的存储。

**`--name` `(?^:^[^:/\s]+$)` （<em>默认值 \=</em> `cephfs`）**

ceph 文件系统名称。

**`--pg_num` `<integer> (8 - 32768)` （<em>默认值 \=</em> `128`）**

后端数据池的放置组数量。元数据池将使用此数量的四分之一。

### <strong>pveceph fs destroy</strong> `<name>` `[OPTIONS]` <a href="#cli_pveceph_fs_destroy" id="cli_pveceph_fs_destroy"></a>

销毁 Ceph 文件系统。如果任何类型为 <em>cephfs</em> 的 PVE 存储条目仍引用该文件系统且未禁用，则拒绝操作。还可以选择移除存储条目和/或底层元数据池及数据池。

**`<name>`: `<string>`**

Ceph 文件系统名称。

**`--remove-pools` `<boolean>` （<em>默认值 \=</em> `0`）**

移除此文件系统使用的元数据池和数据池。

**`--remove-storages` `<boolean>` （<em>默认值 \=</em> `0`）**

移除为此文件系统配置的、由 pveceph 管理的存储。

### <strong>pveceph help</strong> `[OPTIONS]` <a href="#cli_pveceph_help" id="cli_pveceph_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pveceph init</strong> `[OPTIONS]` <a href="#cli_pveceph_init" id="cli_pveceph_init"></a>

创建初始的 Ceph 默认配置并设置符号链接。重复调用具有幂等性：如果 ceph.conf 中已存在 \[global\] 部分，则保留现有的 fsid / auth / pool 默认值，并静默忽略大多数参数。

**`--cluster-network` `<string>`**

声明单独的集群网络，OSD 将通过此网络传输心跳、对象复制和恢复流量

{% hint style="info" %}
需要选项：`network`
{% endhint %}

**`--disable_cephx` `<boolean>` （<em>默认值 \=</em> `0`）**

禁用 cephx 认证。

{% hint style="warning" %}
cephx 是防止中间人攻击的安全功能。只有在网络为私有网络时才考虑禁用 cephx！
{% endhint %}

**`--min_size` `<integer> (1 - 7)` （<em>默认值 \=</em> `2`）**

允许 I/O 所需的每个对象的最少可用副本数量

**`--network` `<string>`**

对所有 ceph 相关流量使用指定网络

**`--pg_bits` `<integer> (6 - 14)` （<em>默认值 \=</em> `6`）**

放置组位数，用于指定默认放置组数量。

已弃用。近期 Ceph 版本中已弃用此设置。

**`--size` `<integer> (1 - 7)` （<em>默认值 \=</em> `3`）**

每个对象的目标副本数量

### <strong>pveceph install</strong> `[OPTIONS]` <a href="#cli_pveceph_install" id="cli_pveceph_install"></a>

安装 ceph 相关软件包。

**`--allow-experimental` `<boolean>` （<em>默认值 \=</em> `0`）**

允许实验性版本。请谨慎使用！

**`--repository` `<enterprise | manual | no-subscription | test>` （<em>默认值 \=</em> `enterprise`）**

使用的 Ceph 仓库。<em>manual</em> 选项不会配置任何仓库。如果宿主机无法访问公共仓库，例如使用 Proxmox Offline Mirror 时，请使用此选项。开始安装之前，需要手动配置包含相应版本 Ceph 软件包的仓库！

**`--version` `<squid | tentacle>` （<em>默认值 \=</em> `tentacle`）**

要安装的 Ceph 版本。

### <strong>pveceph lspools</strong> <a href="#cli_pveceph_lspools" id="cli_pveceph_lspools"></a>

<em>pveceph pool ls</em> 的别名。

### <strong>pveceph mds create</strong> `[OPTIONS]` <a href="#cli_pveceph_mds_create" id="cli_pveceph_mds_create"></a>

创建 Ceph 元数据服务器（MDS）

**`--hotstandby` `<boolean>` （<em>默认值 \=</em> `0`）**

确定 ceph-mds 守护进程是否应轮询并重放活动 MDS 的日志。这可以在 MDS 故障时更快地切换，但需要更多空闲资源。已弃用：此设置已在 Ceph 14.1.1 中移除。

**`--name` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` （<em>默认值 \=</em> `nodename`）**

mds 的 ID，省略时与节点名称相同

### <strong>pveceph mds destroy</strong> `<name>` <a href="#cli_pveceph_mds_destroy" id="cli_pveceph_mds_destroy"></a>

销毁 Ceph 元数据服务器

**`<name>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

mds 的名称（ID）

### <strong>pveceph mgr create</strong> `[OPTIONS]` <a href="#cli_pveceph_mgr_create" id="cli_pveceph_mgr_create"></a>

创建 Ceph 管理器

**`--id` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` （<em>默认值 \=</em> `nodename`）**

管理器的 ID，省略时与节点名称相同。

### <strong>pveceph mgr destroy</strong> `<id>` <a href="#cli_pveceph_mgr_destroy" id="cli_pveceph_mgr_destroy"></a>

销毁 Ceph 管理器。

**`<id>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

管理器的 ID

### <strong>pveceph mon create</strong> `[OPTIONS]` <a href="#cli_pveceph_mon_create" id="cli_pveceph_mon_create"></a>

创建 Ceph 监视器。对于首个监视器，还会自动创建管理器。

**`--mon-address` `<string>`**

覆盖自动检测的监视器 IP 地址。必须位于 Ceph 的公共网络中。

**`--monid` `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?` （<em>默认值 \=</em> `nodename`）**

监视器的 ID，省略时与节点名称相同。

### <strong>pveceph mon destroy</strong> `<monid>` <a href="#cli_pveceph_mon_destroy" id="cli_pveceph_mon_destroy"></a>

销毁 Ceph 监视器。拒绝移除集群中的最后一个监视器。不会销毁同一节点上的任何管理器；请使用

**`<monid>`: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`**

监视器 ID

### <strong>pveceph osd create</strong> `<dev>` `[OPTIONS]` <a href="#cli_pveceph_osd_create" id="cli_pveceph_osd_create"></a>

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

**`--encrypted` `<boolean>` （<em>默认值 \=</em> `0`）**

启用 OSD 加密。

**`--osds-per-device` `<integer> (1 - N)`**

每个物理设备上的 OSD 服务数量。仅对高速 NVMe 设备有用，可更好地利用其性能。与 <em>db\_dev</em> 和 <em>wal\_dev</em> 互斥。

**`--wal_dev` `<string>`**

block.wal 的块设备名称。

**`--wal_dev_size` `<number> (0.5 - N)`**

block.wal 的大小，单位为 GiB。

{% hint style="info" %}
需要选项：`wal_dev`
{% endhint %}

### <strong>pveceph osd destroy</strong> `<osdid>` `[OPTIONS]` <a href="#cli_pveceph_osd_destroy" id="cli_pveceph_osd_destroy"></a>

销毁 OSD

**`<osdid>`: `<integer>`**

OSD ID

**`--cleanup` `<boolean>` （<em>默认值 \=</em> `0`）**

如果设置，还会通过 <em>ceph-volume lvm zap --destroy</em> 销毁底层逻辑卷，使用 pvremove 移除卷组的物理卷，并擦除 filestore OSD 遗留的任何 journal/block.db/block.wal 分区。如果不设置此标志，LV 和分区将保持原样，以供检查。

### <strong>pveceph osd details</strong> `<osdid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveceph_osd_details" id="cli_pveceph_osd_details"></a>

获取 OSD 详细信息。

**`<osdid>`: `<string>`**

OSD 的 ID

**`--verbose` `<boolean>`（<em>默认值 \=</em> `0`）**

打印详细信息，与 json-pretty 输出格式相同。

### <strong>pveceph pool create</strong> `<name>` `[OPTIONS]` <a href="#cli_pveceph_pool_create" id="cli_pveceph_pool_create"></a>

创建 Ceph 池

**`<name>`: `(?^:^[^:/\s]+$)`**

池的名称。必须唯一。

**`--add_storages` `<boolean>` （<em>默认值 \=</em> `0`）**

使用新池配置虚拟机和容器存储。对于复制池默认为 false，对于纠删码池默认为 true（因为 EC 池通常只有连接到存储后才有用）。

**`--application` `<cephfs | rbd | rgw>` （<em>默认值 \=</em> `rbd`）**

池的应用。

**`--crush_rule` `<string>`**

用于映射集群中对象放置位置的规则。

**`--erasure-coding` `k=<integer> ,m=<integer> [,device-class=<class>] [,failure-domain=<domain>] [,profile=<profile>]`**

为 RBD 创建纠删码池，同时创建用于元数据存储的配套复制池。使用 EC 时，常见 ceph 选项 <em>size</em>、<em>min\_size</em> 和 <em>crush\_rule</em> 参数将应用于元数据池。

**`--min_size` `<integer> (1 - 7)` （<em>默认值 \=</em> `2`）**

每个对象的最少副本数量

**`--pg_autoscale_mode` `<off | on | warn>` （<em>默认值 \=</em> `warn`）**

池的自动 PG 扩缩模式。

**`--pg_num` `<integer> (1 - 32768)` （<em>默认值 \=</em> `128`）**

放置组数量。

**`--pg_num_min` `<integer> (-N - 32768)`**

放置组的最少数量。

**`--size` `<integer> (1 - 7)` （<em>默认值 \=</em> `3`）**

每个对象的副本数量

**`--target_size` `^(\d+(\.\d+)?)([KMGT])?$`**

用于 PG 自动扩缩器的池预计目标大小。

**`--target_size_ratio` `<number>`**

用于 PG 自动扩缩器的池预计目标比例。

### <strong>pveceph pool destroy</strong> `<name>` `[OPTIONS]` <a href="#cli_pveceph_pool_destroy" id="cli_pveceph_pool_destroy"></a>

销毁池

**`<name>`: `<string>`**

池的名称。必须唯一。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

如果为 true，即使池正在使用也将其销毁

**`--remove_ecprofile` `<boolean>` （<em>默认值 \=</em> `1`）**

移除纠删码配置文件。在适用情况下默认为 true。

**`--remove_storages` `<boolean>` （<em>默认值 \=</em> `0`）**

移除为此池配置的、由 pveceph 管理的所有存储

### <strong>pveceph pool get</strong> `<name>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveceph_pool_get" id="cli_pveceph_pool_get"></a>

显示池的当前状态。

**`<name>`: `<string>`**

池的名称。必须唯一。

**`--verbose` `<boolean>`（<em>默认值 \=</em> `0`）**

如果启用，将显示额外数据（例如统计信息）。

### <strong>pveceph pool ls</strong> `[FORMAT_OPTIONS]` <a href="#cli_pveceph_pool_ls" id="cli_pveceph_pool_ls"></a>

列出所有池及其设置（可通过 POST/PUT 端点设置的选项）。

### <strong>pveceph pool set</strong> `<name>` `[OPTIONS]` <a href="#cli_pveceph_pool_set" id="cli_pveceph_pool_set"></a>

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

### <strong>pveceph purge</strong> `[OPTIONS]` <a href="#cli_pveceph_purge" id="cli_pveceph_purge"></a>

销毁 ceph 相关数据和配置文件。

**`--crash` `<boolean>`**

同时清除 Ceph 崩溃日志，/var/lib/ceph/crash.

**`--logs` `<boolean>`**

同时清除 Ceph 日志，/var/log/ceph.

### <strong>pveceph start</strong> `[OPTIONS]` <a href="#cli_pveceph_start" id="cli_pveceph_start"></a>

启动 ceph 服务。

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` （<em>默认值 \=</em> `ceph.target`）**

Ceph 服务名称。

### <strong>pveceph status</strong> <a href="#cli_pveceph_status" id="cli_pveceph_status"></a>

获取 Ceph 状态。

### <strong>pveceph stop</strong> `[OPTIONS]` <a href="#cli_pveceph_stop" id="cli_pveceph_stop"></a>

停止 ceph 服务。

**`--service` `(ceph|mon|mds|osd|mgr)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)?` （<em>默认值 \=</em> `ceph.target`）**

Ceph 服务名称。

## 22.7. <strong>pvenode</strong> \- Proxmox VE 节点管理 <a href="#strong_pvenode_strong_proxmox_ve_node_management" id="strong_pvenode_strong_proxmox_ve_node_management"></a>

### <strong>pvenode</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvenode" id="cli_pvenode"></a>

### <strong>pvenode acme account deactivate</strong> `[<name>]` <a href="#cli_pvenode_acme_account_deactivate" id="cli_pvenode_acme_account_deactivate"></a>

在 CA 处停用现有 ACME 账户。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

### <strong>pvenode acme account info</strong> `[<name>]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_account_info" id="cli_pvenode_acme_account_info"></a>

返回现有 ACME 账户信息。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

### <strong>pvenode acme account list</strong> <a href="#cli_pvenode_acme_account_list" id="cli_pvenode_acme_account_list"></a>

ACMEAccount 索引。

### <strong>pvenode acme account register</strong> `[<name>] {<contact>}` `[OPTIONS]` <a href="#cli_pvenode_acme_account_register" id="cli_pvenode_acme_account_register"></a>

在兼容的 CA 上注册新的 ACME 账户。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

**`<contact>`: `<string>`**

联系电子邮件地址。

**`--directory` `^https?://.*`**

ACME CA 目录端点的 URL。

### <strong>pvenode acme account update</strong> `[<name>]` `[OPTIONS]` <a href="#cli_pvenode_acme_account_update" id="cli_pvenode_acme_account_update"></a>

向 CA 更新现有 ACME 账户信息。注意：不指定任何新账户信息将触发刷新。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

**`--contact` `<string>`**

联系电子邮件地址。

### <strong>pvenode acme cert order</strong> `[OPTIONS]` <a href="#cli_pvenode_acme_cert_order" id="cli_pvenode_acme_cert_order"></a>

从兼容 ACME 的 CA 申请新证书。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

覆盖现有的自定义证书。

### <strong>pvenode acme cert renew</strong> `[OPTIONS]` <a href="#cli_pvenode_acme_cert_renew" id="cli_pvenode_acme_cert_renew"></a>

从 CA 续订现有证书。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

即使距离到期还有 30 天以上，也强制续订。

### <strong>pvenode acme cert revoke</strong> <a href="#cli_pvenode_acme_cert_revoke" id="cli_pvenode_acme_cert_revoke"></a>

向 CA 吊销现有证书。

### <strong>pvenode acme plugin add</strong> `<type> <id>` `[OPTIONS]` <a href="#cli_pvenode_acme_plugin_add" id="cli_pvenode_acme_plugin_add"></a>

添加 ACME 插件配置。

**`<type>`: `<dns | standalone>`**

ACME 质询类型。

**`<id>`: `<string>`**

ACME 插件 ID 名称

**`--api` `<1984hosting | acmedns | acmeproxy | active24 | ad | ali | alviy | anx | artfiles | arvan | aurora | autodns | aws | azion | azure | beget | bookmyname | bunny | cf | clouddns | cloudns | cn | conoha | constellix | cpanel | curanet | cyon | da | ddnss | desec | df | dgon | dnsexit | dnshome | dnsimple | dnsservices | doapi | domeneshop | dp | dpi | dreamhost | duckdns | durabledns | dyn | dynu | dynv6 | easydns | edgecenter | edgedns | euserv | exoscale | fornex | freedns | freemyip | gandi_livedns | gcloud | gcore | gd | geoscaling | googledomains | he | he_ddns | hetzner | hetznercloud | hexonet | hostingde | huaweicloud | infoblox | infomaniak | internetbs | inwx | ionos | ionos_cloud | ipv64 | ispconfig | jd | joker | kappernet | kas | kinghost | knot | la | leaseweb | lexicon | limacity | linode | linode_v4 | loopia | lua | maradns | me | miab | mijnhost | misaka | myapi | mydevil | mydnsjp | mythic_beasts | namecheap | namecom | namesilo | nanelo | nederhost | neodigit | netcup | netlify | nic | njalla | nm | nsd | nsone | nsupdate | nw | oci | omglol | one | online | openprovider | openprovider_rest | openstack | opnsense | ovh | pdns | pleskxml | pointhq | porkbun | rackcorp | rackspace | rage4 | rcode0 | regru | scaleway | schlundtech | selectel | selfhost | servercow | simply | spaceship | technitium | tele3 | tencent | timeweb | transip | udr | ultra | unoeuro | variomedia | veesp | vercel | vscale | vultr | websupport | west_cn | world4you | yandex360 | yc | zilore | zone | zoneedit | zonomi>`**

API 插件名称

**`--data` `File with one key-value pair per line, will be base64url encode for storage in plugin config.`**

DNS 插件数据。（base64 编码）

**`--disable` `<boolean>`**

用于禁用配置的标志。

**`--nodes` `<string>`**

集群节点名称列表。

**`--validation-delay` `<integer> (0 - 172800)` （<em>默认值 \=</em> `30`）**

请求验证前额外等待的延迟，单位为秒。用于应对 DNS 记录 TTL 较长的情况。

### <strong>pvenode acme plugin config</strong> `<id>` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_plugin_config" id="cli_pvenode_acme_plugin_config"></a>

获取 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件实例的唯一标识符。

### <strong>pvenode acme plugin list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_plugin_list" id="cli_pvenode_acme_plugin_list"></a>

ACME 插件索引。

**`--type` `<dns | standalone>`**

仅列出指定类型的 ACME 插件

### <strong>pvenode acme plugin remove</strong> `<id>` <a href="#cli_pvenode_acme_plugin_remove" id="cli_pvenode_acme_plugin_remove"></a>

删除 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件实例的唯一标识符。

### <strong>pvenode acme plugin set</strong> `<id>` `[OPTIONS]` <a href="#cli_pvenode_acme_plugin_set" id="cli_pvenode_acme_plugin_set"></a>

更新 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件 ID 名称

**`--api` `<1984hosting | acmedns | acmeproxy | active24 | ad | ali | alviy | anx | artfiles | arvan | aurora | autodns | aws | azion | azure | beget | bookmyname | bunny | cf | clouddns | cloudns | cn | conoha | constellix | cpanel | curanet | cyon | da | ddnss | desec | df | dgon | dnsexit | dnshome | dnsimple | dnsservices | doapi | domeneshop | dp | dpi | dreamhost | duckdns | durabledns | dyn | dynu | dynv6 | easydns | edgecenter | edgedns | euserv | exoscale | fornex | freedns | freemyip | gandi_livedns | gcloud | gcore | gd | geoscaling | googledomains | he | he_ddns | hetzner | hetznercloud | hexonet | hostingde | huaweicloud | infoblox | infomaniak | internetbs | inwx | ionos | ionos_cloud | ipv64 | ispconfig | jd | joker | kappernet | kas | kinghost | knot | la | leaseweb | lexicon | limacity | linode | linode_v4 | loopia | lua | maradns | me | miab | mijnhost | misaka | myapi | mydevil | mydnsjp | mythic_beasts | namecheap | namecom | namesilo | nanelo | nederhost | neodigit | netcup | netlify | nic | njalla | nm | nsd | nsone | nsupdate | nw | oci | omglol | one | online | openprovider | openprovider_rest | openstack | opnsense | ovh | pdns | pleskxml | pointhq | porkbun | rackcorp | rackspace | rage4 | rcode0 | regru | scaleway | schlundtech | selectel | selfhost | servercow | simply | spaceship | technitium | tele3 | tencent | timeweb | transip | udr | ultra | unoeuro | variomedia | veesp | vercel | vscale | vultr | websupport | west_cn | world4you | yandex360 | yc | zilore | zone | zoneedit | zonomi>`**

API 插件名称

**`--data` `File with one key-value pair per line, will be base64url encode for storage in plugin config.`**

DNS 插件数据。（base64 编码）

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

用于禁用配置的标志。

**`--nodes` `<string>`**

集群节点名称列表。

**`--validation-delay` `<integer> (0 - 172800)` （<em>默认值 \=</em> `30`）**

请求验证前额外等待的延迟，单位为秒。用于应对 DNS 记录 TTL 较长的情况。

### <strong>pvenode cert delete</strong> `[<restart>]` <a href="#cli_pvenode_cert_delete" id="cli_pvenode_cert_delete"></a>

删除自定义证书链和密钥。

**`<restart>`: `<boolean>` （<em>默认值 \=</em> `0`）**

重启 pveproxy。

### <strong>pvenode cert info</strong> `[FORMAT_OPTIONS]` <a href="#cli_pvenode_cert_info" id="cli_pvenode_cert_info"></a>

获取有关节点证书的信息。

### <strong>pvenode cert set</strong> `<certificates> [<key>]` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_cert_set" id="cli_pvenode_cert_set"></a>

上传或更新自定义证书链和密钥。

**`<certificates>`: `<string>`**

PEM 编码的证书（链）。

**`<key>`: `<string>`**

PEM 编码的私钥。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

覆盖现有自定义证书文件或 ACME 证书文件。

**`--restart` `<boolean>` （<em>默认值 \=</em> `0`）**

重启 pveproxy。

### <strong>pvenode config get</strong> `[OPTIONS]` <a href="#cli_pvenode_config_get" id="cli_pvenode_config_get"></a>

获取节点配置选项。

**`--property` `<acme | acmedomain0 | acmedomain1 | acmedomain2 | acmedomain3 | acmedomain4 | acmedomain5 | ballooning-target | description | location | startall-onboot-delay | wakeonlan>` （<em>默认值 \=</em> `all`）**

仅返回节点配置中的指定属性。

### <strong>pvenode config set</strong> `[OPTIONS]` <a href="#cli_pvenode_config_set" id="cli_pvenode_config_set"></a>

设置节点配置选项。

**`--acme` `[account=<name>] [,domains=<domain[;domain;...]>]`**

节点特定的 ACME 设置。

**`--acmedomain[n]` `[domain=]<domain> [,alias=<domain>] [,plugin=<name of the plugin configuration>]`**

ACME 域和验证插件

**`--ballooning-target` `<integer> (0 - 100)` （<em>默认值 \=</em> `80`）**

内存气球的 RAM 使用率目标（占总内存的百分比）

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

节点描述。显示在 Web 界面的节点备注面板中。以注释形式保存在配置文件内。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--location` `latitude=<number> ,longitude=<number> [,name=<name>]`**

节点的位置。覆盖数据中心配置中的默认值。

**`--startall-onboot-delay` `<integer> (0 - 300)` （<em>默认值 \=</em> `0`）**

启动所有已启用开机启动的虚拟客户机之前的初始延迟，单位为秒。

**`--wakeonlan` `[mac=]<MAC address> [,bind-interface=<bind interface>] [,broadcast-address=<IPv4 broadcast address>]`**

节点特定的网络唤醒设置。

### <strong>pvenode help</strong> `[OPTIONS]` <a href="#cli_pvenode_help" id="cli_pvenode_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvenode migrateall</strong> `<target>` `[OPTIONS]` <a href="#cli_pvenode_migrateall" id="cli_pvenode_migrateall"></a>

迁移所有虚拟机和容器。

**`<target>`: `<string>`**

目标节点。

**`--max-workers` `<integer> (1 - 64)`**

并行迁移任务的最大数量。如果未设置，则使用 max\_workers，其值来自 datacenter.cfg。两者必须至少设置一个！

**`--maxworkers` `<integer> (1 - 64)`**

并行迁移任务的最大数量。如果未设置，则使用 max\_workers，其值来自 datacenter.cfg。两者必须至少设置一个！已弃用，请改用 <em>max-workers</em>。

**`--vms` `<string>`**

仅考虑具有这些 ID 的客户机。

**`--with-local-disks` `<boolean>`**

对本地磁盘启用在线存储迁移

### <strong>pvenode startall</strong> `[OPTIONS]` <a href="#cli_pvenode_startall" id="cli_pvenode_startall"></a>

启动此节点上的所有虚拟机和容器（默认只启动设置了 onboot\=1 的客户机）。

**`--force` `<boolean>` （<em>默认值 \=</em> `off`）**

即使虚拟客户机未设置 <em>onboot</em> 或将其设置为 off，也发出启动命令。

**`--max-workers` `<integer> (1 - 64)`**

定义同时运行任务的最大数量。如果未设置，则使用 <em>max\_workers</em>，其值来自 datacenter.cfg；如果该值也未设置，则使用可用 CPU 线程数，但最多为 8。

**`--vms` `<string>`**

仅考虑此逗号分隔的 VMID 列表中的客户机。

### <strong>pvenode stopall</strong> `[OPTIONS]` <a href="#cli_pvenode_stopall" id="cli_pvenode_stopall"></a>

停止所有虚拟机和容器。

**`--force-stop` `<boolean>` （<em>默认值 \=</em> `1`）**

超时后强制停止。

**`--max-workers` `<integer> (1 - 64)`**

定义同时运行任务的最大数量。如果未设置，则使用 <em>max\_workers</em>，其值来自 datacenter.cfg；如果该值也未设置，则使用可用 CPU 线程数，但最多为 8。

**`--timeout` `<integer> (0 - 7200)` （<em>默认值 \=</em> `180`）**

每个客户机关机任务的超时时间。随后根据 `force-stop` 的设置，直接中止关机或强制停止。

**`--vms` `<string>`**

仅考虑具有这些 ID 的客户机。

### <strong>pvenode task list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_task_list" id="cli_pvenode_task_list"></a>

读取某个节点的任务列表（已完成任务）。

**`--errors` `<boolean>` （<em>默认值 \=</em> `0`）**

仅列出状态为 ERROR 的任务。

**`--limit` `<integer> (0 - N)` （<em>默认值 \=</em> `50`）**

仅列出此数量的任务。

**`--since` `<integer>`**

仅列出此 UNIX 纪元时间之后的任务。

**`--source` `<active | all | archive>` （<em>默认值 \=</em> `archive`）**

列出已归档、活动或全部任务。

**`--start` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

从此偏移量开始列出任务。

**`--statusfilter` `<string>`**

应返回的任务状态列表。

**`--typefilter` `<string>`**

仅列出此类型的任务（例如 vzstart、vzdump）。

**`--until` `<integer>`**

仅列出此 UNIX 纪元时间之前的任务。

**`--userfilter` `<string>`**

仅列出此用户的任务。

**`--vmid` `<integer> (100 - 999999999)`**

仅列出此虚拟机的任务。

### <strong>pvenode task log</strong> `<upid>` `[OPTIONS]` <a href="#cli_pvenode_task_log" id="cli_pvenode_task_log"></a>

读取任务日志。

**`<upid>`: `<string>`**

任务的唯一 ID。

**`--download` `<boolean>`**

是否应下载任务日志文件。此参数不能与其他参数同时使用

**`--start` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

读取任务日志时从此行开始

### <strong>pvenode task status</strong> `<upid>` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_task_status" id="cli_pvenode_task_status"></a>

读取任务状态。

**`<upid>`: `<string>`**

任务的唯一 ID。

### <strong>pvenode wakeonlan</strong> `<node>` <a href="#cli_pvenode_wakeonlan" id="cli_pvenode_wakeonlan"></a>

尝试通过<em>网络唤醒</em>数据包唤醒节点。

**`<node>`: `<string>`**

网络唤醒数据包的目标节点

## 22.8. <strong>pvesh</strong> \- Proxmox VE API 的 Shell 接口 <a href="#strong_pvesh_strong_shell_interface_for_the_proxmox_ve_api" id="strong_pvesh_strong_shell_interface_for_the_proxmox_ve_api"></a>

### <strong>pvesh</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesh" id="cli_pvesh"></a>

### <strong>pvesh create</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_create" id="cli_pvesh_create"></a>

对 \<api\_path\> 调用 API POST。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh delete</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_delete" id="cli_pvesh_delete"></a>

对 \<api\_path\> 调用 API DELETE。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh get</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_get" id="cli_pvesh_get"></a>

对 \<api\_path\> 调用 API GET。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh help</strong> `[OPTIONS]` <a href="#cli_pvesh_help" id="cli_pvesh_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvesh ls</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_ls" id="cli_pvesh_ls"></a>

列出 \<api\_path\> 下的子对象。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh set</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_set" id="cli_pvesh_set"></a>

对 \<api\_path\> 调用 API PUT。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh usage</strong> `<api_path>` `[OPTIONS]` <a href="#cli_pvesh_usage" id="cli_pvesh_usage"></a>

打印 \<api\_path\> 的 API 使用信息。

**`<api_path>`: `<string>`**

API 路径。

**`--command` `<create | delete | get | set>`**

API 命令。

**`--returns` `<boolean>`**

包含返回数据的模式定义。

**`--verbose` `<boolean>`**

详细输出格式。

## 22.9. <strong>qm</strong> \- QEMU/KVM 虚拟机管理器 <a href="#strong_qm_strong_qemu_kvm_virtual_machine_manager" id="strong_qm_strong_qemu_kvm_virtual_machine_manager"></a>

### <strong>qm</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_qm" id="cli_qm"></a>

### <strong>qm agent</strong> <a href="#cli_qm_agent" id="cli_qm_agent"></a>

<em>qm guest cmd</em> 的别名。

### <strong>qm cleanup</strong> `<vmid> <clean-shutdown> <guest-requested>` <a href="#cli_qm_cleanup" id="cli_qm_cleanup"></a>

清理 tap 设备、vgpu 等资源。在虚拟机关机、崩溃等情况后调用。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<clean-shutdown>`: `<boolean>`**

表示 qemu 是否正常关闭。

**`<guest-requested>`: `<boolean>`**

表示关机是由客户机请求，还是通过 qmp 请求。

### <strong>qm clone</strong> `<vmid> <newid>` `[OPTIONS]` <a href="#cli_qm_clone" id="cli_qm_clone"></a>

创建虚拟机/模板的副本。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<newid>`: `<integer> (100 - 999999999)`**

克隆的 VMID。

**`--bwlimit` `<integer> (0 - N)` （<em>默认值 \=</em> `clone limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--description` `<string>`**

新虚拟机的描述。

**`--format` `<qcow2 | raw | vmdk>`**

目标磁盘格式。仅对完整克隆有效。如果目标存储不支持该格式，则改用存储的默认格式。

**`--full` `<boolean>`**

创建所有磁盘的完整副本。克隆普通虚拟机时始终执行此操作。对于虚拟机模板，默认尝试创建链接克隆。

**`--name` `<string>`**

设置新虚拟机的名称。

**`--pool` `<string>`**

将新虚拟机添加到指定资源池。

**`--snapname` `<string>`**

快照的名称。

**`--storage` `<storage ID>`**

完整克隆的目标存储。

**`--target` `<string>`**

目标节点。仅当原始 VM 位于共享存储上时才允许。

### <strong>qm cloudinit dump</strong> `<vmid> <type>` <a href="#cli_qm_cloudinit_dump" id="cli_qm_cloudinit_dump"></a>

获取自动生成的 cloudinit 配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<type>`: `<meta | network | user>`**

配置类型。

### <strong>qm cloudinit pending</strong> `<vmid>` <a href="#cli_qm_cloudinit_pending" id="cli_qm_cloudinit_pending"></a>

获取同时包含当前值和待应用值的 cloudinit 配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm cloudinit update</strong> `<vmid>` <a href="#cli_qm_cloudinit_update" id="cli_qm_cloudinit_update"></a>

重新生成并更改 cloudinit 配置驱动器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm config</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_config" id="cli_qm_config"></a>

获取应用待定配置更改后的虚拟机配置。设置 <em>current</em> 参数可改为获取当前配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--current` `<boolean>`（<em>默认 \=</em> `0`）**

获取当前值（而非待生效值）。

**`--snapshot` `<string>`**

从指定快照获取配置值。

### <strong>qm create</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_create" id="cli_qm_create"></a>

创建或恢复虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--acpi` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 ACPI。

**`--affinity` `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`--allow-ksm` `<boolean>` （<em>默认值 \=</em> `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`--arch` `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`--archive` `<string>`**

备份归档。可以是 .tar 或 .vma 文件的文件系统路径（使用 <em>\-</em> 从 stdin 通过管道传入数据），也可以是 proxmox 存储备份卷标识符。

**`--args` `<string>`**

传递给 kvm 的任意参数。

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`--autostart` `<boolean>` （<em>默认值 \=</em> `0`）**

崩溃后自动重启（目前被忽略）。

**`--balloon` `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`--bios` `<ovmf | seabios>` （<em>默认值 \=</em> `seabios`）**

选择 BIOS 实现。

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 <em>order\=</em> 子属性，因为不带键的用法或 <em>legacy\=</em> 已弃用。

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 <em>boot: order\=foo;bar</em>。

**`--bwlimit` `<integer> (0 - N)` （<em>默认值 \=</em> `restore limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cdrom` `<volume>`**

这是选项 -ide2 的别名

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`--cipassword` `<password>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`--citype` `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`--ciupgrade` `<boolean>` （<em>默认值 \=</em> `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`--ciuser` `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`--cores` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

每个 CPU 插槽的核心数。

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`--cpulimit` `<number> (0 - 128)` （<em>默认值 \=</em> `0`）**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` （<em>默认值 \=</em> `cgroup v1: 1024, cgroup v2: 100`）**

虚拟机的 CPU 权重，在 cgroup v2 中限制为 \[1, 10000\]。

**`--description` `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是将默认 EFI 变量复制到该卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--force` `<boolean>`**

允许覆盖现有虚拟机。

{% hint style="info" %}
需要选项：`archive`
{% endhint %}

**`--freeze` `<boolean>`**

启动时冻结 CPU（使用 <em>c</em> 监视器命令开始执行）。

**`--ha-managed` `<boolean>`（<em>默认 \=</em> `0`）**

创建虚拟机后，将其添加为 HA 资源。

**`--hookscript` `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

**`--hotplug` `<string>` （<em>默认值 \=</em> `network,disk,usb`）**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：<em>network</em>、<em>disk</em>、<em>cpu</em>、<em>memory</em>、<em>usb</em> 和 <em>cloudinit</em>。使用 <em>0</em> 完全禁用热插拔。将 <em>1</em> 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`--hugepages` `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 <em>any</em>，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--import-working-storage` `<storage ID>`**

已启用 <em>images</em> 内容类型的文件存储，导入期间用作中间解压存储。默认为源存储。

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 <em>dhcp</em> 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 <em>auto</em> 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`--ivshmem` `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`--keephugepages` `<boolean>` （<em>默认值 \=</em> `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`--kvm` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 KVM 硬件虚拟化。

**`--live-restore` `<boolean>`**

立即启动虚拟机，同时在后台导入或恢复。

**`--localtime` `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--memory` `[current=]<integer>`**

内存属性。

**`--migrate_downtime` `<number> (0 - N)` （<em>默认值 \=</em> `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`--migrate_speed` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`--name` `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`--nameserver` `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`--numa` `<boolean>` （<em>默认值 \=</em> `0`）**

启用/禁用 NUMA。

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`--onboot` `<boolean>`（<em>默认 \=</em> `0`）**

指定是否在系统启动时启动虚拟机。

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` （<em>默认值 \=</em> `other`）**

指定客户机操作系统。

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>`（<em>默认 \=</em> `0`）**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`--reboot` `<boolean>` （<em>默认值 \=</em> `1`）**

允许重启。如果设为 <em>0</em>，虚拟机将在重启时退出。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` （<em>默认值 \=</em> `lsi`）**

SCSI 控制器型号

**`--searchdomain` `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--serial[n]` `(/dev/[^,]+|socket)`**

在虚拟机内创建串口设备（n 为 0 到 3）

**`--shares` `<integer> (0 - 50000)` （<em>默认值 \=</em> `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`--smp` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

CPU 数量。请改用 -sockets 选项。

**`--sockets` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

CPU 插槽数量。

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`--sshkeys` `<filepath>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--start` `<boolean>`（<em>默认 \=</em> `0`）**

成功创建后启动虚拟机。

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` （<em>默认值 \=</em> `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、<em>2006-06-17T16:01:21</em> 或 <em>2006-06-17</em>。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`**

默认存储。

**`--tablet` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 USB 数位板设备。

**`--tags` `<string>`**

虚拟机的标签。这只是元信息。

**`--tdf` `<boolean>` （<em>默认值 \=</em> `0`）**

启用/禁用时间漂移修正。

**`--template` `<boolean>`（<em>默认 \=</em> `0`）**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 <em>raw</em>。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是使用 4 MiB。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
需要选项：`archive`
{% endhint %}

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`--vcpus` `<integer> (1 - N)` （<em>默认值 \=</em> `0`）**

热插拔的 vcpu 数量。

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`--vmgenid` `<UUID>` （<em>默认值 \=</em> `1 (autogenerated)`）**

设置虚拟机世代 ID。使用 <em>1</em> 在创建或更新时自动生成，传入 <em>0</em> 可明确禁用。

**`--vmstatestorage` `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。

### <strong>qm delsnapshot</strong> `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_qm_delsnapshot" id="cli_qm_delsnapshot"></a>

删除虚拟机快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--force` `<boolean>`**

即使删除磁盘快照失败，也从配置文件中移除。

### <strong>qm destroy</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_destroy" id="cli_qm_destroy"></a>

销毁虚拟机以及所有使用的/所属的卷。移除所有虚拟机特定权限和防火墙规则

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--destroy-unreferenced-disks` `<boolean>` （<em>默认值 \=</em> `0`）**

如果设置，还会从所有已启用的存储中销毁配置中未引用但 VMID 匹配的所有磁盘。

**`--purge` `<boolean>`**

从备份任务、复制任务和 HA 等配置中移除 VMID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>qm disk import</strong> `<vmid> <source> <storage>` `[OPTIONS]` <a href="#cli_qm_disk_import" id="cli_qm_disk_import"></a>

将外部磁盘镜像作为虚拟机中的未使用磁盘导入。镜像格式必须受 qemu-img(1) 支持。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<source>`: `<string>`**

要导入的磁盘镜像路径

**`<storage>`: `<storage ID>`**

目标存储 ID

**`--format` `<qcow2 | raw | vmdk>`**

目标格式

**`--target-disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

卷将导入到的磁盘名称（例如 scsi1）。

### <strong>qm disk move</strong> `<vmid> <disk> [<storage>]` `[OPTIONS]` <a href="#cli_qm_disk_move" id="cli_qm_disk_move"></a>

将卷移动到其他存储或其他虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

要移动的磁盘。

**`<storage>`: `<storage ID>`**

目标存储。

**`--bwlimit` `<integer> (0 - N)` （<em>默认值 \=</em> `move limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (<em>默认 \=</em> `0`)**

成功复制后删除原始磁盘。默认保留原始磁盘作为未使用磁盘。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--format` `<qcow2 | raw | vmdk>`**

目标磁盘格式。仅在移动到其他存储时使用。如果目标存储不支持此格式，则改用存储的默认格式。

**`--target-digest` `<string>`**

如果目标虚拟机当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于检测并发修改。

**`--target-disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

磁盘将移动到的目标虚拟机配置键（例如 ide0 或 scsi1）。默认为源磁盘键。

**`--target-vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm disk rescan</strong> `[OPTIONS]` <a href="#cli_qm_disk_rescan" id="cli_qm_disk_rescan"></a>

重新扫描所有存储，并更新磁盘大小和未使用的磁盘映像。

**`--dryrun` `<boolean>` (<em>默认 \=</em> `0`)**

不将更改实际写入虚拟机配置。

**`--vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm disk resize</strong> `<vmid> <disk> <size>` `[OPTIONS]` <a href="#cli_qm_disk_resize" id="cli_qm_disk_resize"></a>

扩展卷大小。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

要调整大小的磁盘。

**`<size>`: `\+?\d+(\.\d+)?[KMGT]?`**

新大小。如果带有 `+` 符号，则将此值加到卷的实际大小上；否则将此值作为绝对大小。不支持缩小磁盘大小。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>qm disk unlink</strong> `<vmid> --idlist <string>` `[OPTIONS]` <a href="#cli_qm_disk_unlink" id="cli_qm_disk_unlink"></a>

解除链接/删除磁盘镜像。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--force` `<boolean>`**

强制物理删除。如果不设置此项，则只从配置文件中移除磁盘，并创建一个名为 <em>unused\[n\]</em> 的额外配置条目，其中包含卷 ID。解除 unused\[n\] 的链接始终会导致物理删除。

**`--idlist` `<string>`**

要删除的磁盘 ID 列表。

### <strong>qm enroll-efi-keys</strong> `<vmid>` <a href="#cli_qm_enroll-efi-keys" id="cli_qm_enroll-efi-keys"></a>

向具有 pre-enrolled-keys 的 EFI 磁盘注册重要的更新证书。目前这些证书为 Microsoft 的 UEFI 2023 证书。必须在虚拟机关机时调用。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm guest cmd</strong> `<vmid> <command>` <a href="#cli_qm_guest_cmd" id="cli_qm_guest_cmd"></a>

执行 QEMU 客户机代理命令。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<command>`: `<fsfreeze-freeze | fsfreeze-status | fsfreeze-thaw | fstrim | get-fsinfo | get-host-name | get-memory-block-info | get-memory-blocks | get-osinfo | get-time | get-timezone | get-users | get-vcpus | info | network-get-interfaces | ping | shutdown | suspend-disk | suspend-hybrid | suspend-ram>`**

QGA 命令。

### <strong>qm guest exec</strong> `<vmid> [<extra-args>]` `[OPTIONS]` <a href="#cli_qm_guest_exec" id="cli_qm_guest_exec"></a>

通过客户机代理执行给定命令

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--pass-stdin` `<boolean>` （<em>默认值 \=</em> `0`）**

设置后，读取 STDIN 直到 EOF，并通过 <em>input-data</em> 转发到客户机代理（通常被视为客户机代理启动进程的 STDIN）。最大允许 1 MiB。

**`--synchronous` `<boolean>` （<em>默认值 \=</em> `1`）**

如果设置为 off，则立即返回 pid，而不等待命令完成或超时。

**`--timeout` `<integer> (0 - N)` （<em>默认值 \=</em> `30`）**

同步等待命令完成的最长时间。如果达到该时间，则返回 pid。设置为 0 可禁用

### <strong>qm guest exec-status</strong> `<vmid> <pid>` <a href="#cli_qm_guest_exec-status" id="cli_qm_guest_exec-status"></a>

获取客户机代理启动的给定 pid 的状态

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<pid>`: `<integer>`**

要查询的 PID

### <strong>qm guest passwd</strong> `<vmid> <username>` `[OPTIONS]` <a href="#cli_qm_guest_passwd" id="cli_qm_guest_passwd"></a>

将给定用户的密码设置为给定密码

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<username>`: `<string>`**

要设置密码的用户。

**`--crypted` `<boolean>` （<em>默认值 \=</em> `0`）**

如果密码已通过 crypt() 处理，则设置为 1

### <strong>qm help</strong> `[OPTIONS]` <a href="#cli_qm_help" id="cli_qm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>qm import</strong> `<vmid> <source> --storage <string>` `[OPTIONS]` <a href="#cli_qm_import" id="cli_qm_import"></a>

从支持的导入源（例如 ESXi 存储）导入外部虚拟客户机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<source>`: `<string>`**

导入源的卷 ID。

**`--acpi` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 ACPI。

**`--affinity` `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`--allow-ksm` `<boolean>` （<em>默认值 \=</em> `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`--arch` `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`--args` `<string>`**

传递给 kvm 的任意参数。

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`--autostart` `<boolean>` （<em>默认值 \=</em> `0`）**

崩溃后自动重启（目前被忽略）。

**`--balloon` `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`--bios` `<ovmf | seabios>` （<em>默认值 \=</em> `seabios`）**

选择 BIOS 实现。

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 <em>order\=</em> 子属性，因为不带键的用法或 <em>legacy\=</em> 已弃用。

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 <em>boot: order\=foo;bar</em>。

**`--cdrom` `<volume>`**

这是选项 -ide2 的别名

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`--cipassword` `<string>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`--citype` `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`--ciupgrade` `<boolean>` （<em>默认值 \=</em> `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`--ciuser` `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`--cores` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

每个 CPU 插槽的核心数。

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`--cpulimit` `<number> (0 - 128)` （<em>默认值 \=</em> `0`）**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` （<em>默认值 \=</em> `cgroup v1: 1024, cgroup v2: 100`）**

虚拟机的 CPU 权重，在 cgroup v2 中限制为 \[1, 10000\]。

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`--dryrun` `<boolean>` (<em>默认 \=</em> `0`)**

显示创建命令后退出，不执行任何操作。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是将默认 EFI 变量复制到该卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--format` `<qcow2 | raw | vmdk>`**

目标格式

**`--freeze` `<boolean>`**

启动时冻结 CPU（使用 <em>c</em> 监视器命令开始执行）。

**`--hookscript` `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

**`--hotplug` `<string>` （<em>默认值 \=</em> `network,disk,usb`）**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：<em>network</em>、<em>disk</em>、<em>cpu</em>、<em>memory</em>、<em>usb</em> 和 <em>cloudinit</em>。使用 <em>0</em> 完全禁用热插拔。将 <em>1</em> 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`--hugepages` `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 <em>any</em>，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 <em>dhcp</em> 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 <em>auto</em> 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`--ivshmem` `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`--keephugepages` `<boolean>` （<em>默认值 \=</em> `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`--kvm` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 KVM 硬件虚拟化。

**`--live-import` `<boolean>` （<em>默认值 \=</em> `0`）**

立即启动虚拟机，并在后台复制数据。

**`--localtime` `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--memory` `[current=]<integer>`**

内存属性。

**`--migrate_downtime` `<number> (0 - N)` （<em>默认值 \=</em> `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`--migrate_speed` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`--name` `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`--nameserver` `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`--numa` `<boolean>` （<em>默认值 \=</em> `0`）**

启用/禁用 NUMA。

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`--onboot` `<boolean>`（<em>默认 \=</em> `0`）**

指定是否在系统启动时启动虚拟机。

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` （<em>默认值 \=</em> `other`）**

指定客户机操作系统。

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

**`--protection` `<boolean>`（<em>默认 \=</em> `0`）**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`--reboot` `<boolean>` （<em>默认值 \=</em> `1`）**

允许重启。如果设为 <em>0</em>，虚拟机将在重启时退出。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` （<em>默认值 \=</em> `lsi`）**

SCSI 控制器型号

**`--searchdomain` `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--serial[n]` `(/dev/[^,]+|socket)`**

在虚拟机内创建串口设备（n 为 0 到 3）

**`--shares` `<integer> (0 - 50000)` （<em>默认值 \=</em> `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`--smp` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

CPU 数量。请改用 -sockets 选项。

**`--sockets` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

CPU 插槽数量。

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`--sshkeys` `<string>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` （<em>默认值 \=</em> `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、<em>2006-06-17T16:01:21</em> 或 <em>2006-06-17</em>。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`**

默认存储。

**`--tablet` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 USB 数位板设备。

**`--tags` `<string>`**

虚拟机的标签。这只是元信息。

**`--tdf` `<boolean>` （<em>默认值 \=</em> `0`）**

启用/禁用时间漂移修正。

**`--template` `<boolean>`（<em>默认 \=</em> `0`）**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 <em>raw</em>。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是使用 4 MiB。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`--vcpus` `<integer> (1 - N)` （<em>默认值 \=</em> `0`）**

热插拔的 vcpu 数量。

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`--vmgenid` `<UUID>` （<em>默认值 \=</em> `1 (autogenerated)`）**

设置虚拟机世代 ID。使用 <em>1</em> 在创建或更新时自动生成，传入 <em>0</em> 可明确禁用。

**`--vmstatestorage` `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。

### <strong>qm importdisk</strong> <a href="#cli_qm_importdisk" id="cli_qm_importdisk"></a>

<em>qm disk import</em> 的别名。

### <strong>qm importovf</strong> `<vmid> <manifest> <storage>` `[OPTIONS]` <a href="#cli_qm_importovf" id="cli_qm_importovf"></a>

使用从 OVF 清单读取的参数创建新虚拟机

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<manifest>`: `<string>`**

ovf 文件的路径

**`<storage>`: `<storage ID>`**

目标存储 ID

**`--dryrun` `<boolean>`**

打印所提取 OVF 参数的解析后表示，但不创建虚拟机

**`--format` `<qcow2 | raw | vmdk>`**

目标格式

### <strong>qm list</strong> `[OPTIONS]` <a href="#cli_qm_list" id="cli_qm_list"></a>

虚拟机索引（每个节点）。

**`--full` `<boolean>`**

确定活动虚拟机的完整状态。

### <strong>qm listsnapshot</strong> `<vmid>` <a href="#cli_qm_listsnapshot" id="cli_qm_listsnapshot"></a>

列出所有快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm migrate</strong> `<vmid> <target>` `[OPTIONS]` <a href="#cli_qm_migrate" id="cli_qm_migrate"></a>

迁移虚拟机。创建新的迁移任务。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target>`: `<string>`**

目标节点。

**`--bwlimit` `<integer> (0 - N)` (<em>默认 \=</em> `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--force` `<boolean>`**

允许迁移使用本地设备的虚拟机。只有 root 可以使用此选项。

**`--migration_network` `<string>`**

用于迁移的网络（或子网）的 CIDR。

**`--migration_type` `<insecure | secure>`**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`--online` `<boolean>`**

如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。

**`--targetstorage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 <em>1</em> 会将每个源存储映射到其自身。

**`--with-conntrack-state` `<boolean>` （<em>默认值 \=</em> `0`）**

是否迁移运行中虚拟机的 conntrack 条目。

**`--with-local-disks` `<boolean>`**

对本地磁盘启用在线存储迁移

### <strong>qm monitor</strong> `<vmid>` <a href="#cli_qm_monitor" id="cli_qm_monitor"></a>

进入 QEMU 监视器界面。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm move-disk</strong> <a href="#cli_qm_move-disk" id="cli_qm_move-disk"></a>

<em>qm disk move</em> 的别名。

### <strong>qm move\_disk</strong> <a href="#cli_qm_move_disk" id="cli_qm_move_disk"></a>

<em>qm disk move</em> 的别名。

### <strong>qm mtunnel</strong> <a href="#cli_qm_mtunnel" id="cli_qm_mtunnel"></a>

由 qmigrate 使用，请勿手动使用。

### <strong>qm nbdstop</strong> `<vmid>` <a href="#cli_qm_nbdstop" id="cli_qm_nbdstop"></a>

停止内嵌 nbd 服务器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm pending</strong> `<vmid>` <a href="#cli_qm_pending" id="cli_qm_pending"></a>

获取同时包含当前值和待应用值的虚拟机配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm reboot</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_reboot" id="cli_qm_reboot"></a>

通过关闭虚拟机后重新启动来重启虚拟机。应用待定更改。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒以完成关机。

### <strong>qm remote-migrate</strong> `<vmid> [<target-vmid>] <target-endpoint> --target-bridge <string> --target-storage <string>` `[OPTIONS]` <a href="#cli_qm_remote-migrate" id="cli_qm_remote-migrate"></a>

将虚拟机迁移到远程集群。创建新的迁移任务。实验性功能！

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-endpoint>`: `apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]`**

远程目标端点

**`--bwlimit` `<integer> (0 - N)` (<em>默认 \=</em> `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (<em>默认 \=</em> `0`)**

成功迁移后删除原始虚拟机及相关数据。默认情况下，原始虚拟机保留在源集群中，处于停止状态。

**`--online` `<boolean>`**

如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。

**`--target-bridge` `<string>`**

从源网桥到目标网桥的映射。仅提供一个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 <em>1</em> 会将每个源网桥映射到其自身。

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 <em>1</em> 会将每个源存储映射到其自身。

### <strong>qm rescan</strong> <a href="#cli_qm_rescan" id="cli_qm_rescan"></a>

<em>qm disk rescan</em> 的别名。

### <strong>qm reset</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_reset" id="cli_qm_reset"></a>

重置虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>qm resize</strong> <a href="#cli_qm_resize" id="cli_qm_resize"></a>

<em>qm disk resize</em> 的别名。

### <strong>qm resume</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_resume" id="cli_qm_resume"></a>

恢复虚拟机运行。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--nocheck` `<boolean>`**

不检查虚拟机是否正在运行，内部用于迁移期间。只有 root 可以使用此选项。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>qm rollback</strong> `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_qm_rollback" id="cli_qm_rollback"></a>

将虚拟机状态回滚到指定快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--start` `<boolean>`（<em>默认 \=</em> `0`）**

成功回滚后是否启动虚拟机。（注意：如果快照包含 RAM，虚拟机将自动启动。）

### <strong>qm sendkey</strong> `<vmid> <key>` `[OPTIONS]` <a href="#cli_qm_sendkey" id="cli_qm_sendkey"></a>

向虚拟机发送按键事件。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<key>`: `<string>`**

按键（qemu 监视器编码）。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>qm set</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_set" id="cli_qm_set"></a>

设置虚拟机选项（同步 API）。对于任何涉及热插拔或存储分配的操作，应考虑改用 POST 方法。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--acpi` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 ACPI。

**`--affinity` `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`--allow-ksm` `<boolean>` （<em>默认值 \=</em> `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`--arch` `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`--args` `<string>`**

传递给 kvm 的任意参数。

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`--autostart` `<boolean>` （<em>默认值 \=</em> `0`）**

崩溃后自动重启（目前被忽略）。

**`--balloon` `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`--bios` `<ovmf | seabios>` （<em>默认值 \=</em> `seabios`）**

选择 BIOS 实现。

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 <em>order\=</em> 子属性，因为不带键的用法或 <em>legacy\=</em> 已弃用。

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 <em>boot: order\=foo;bar</em>。

**`--cdrom` `<volume>`**

这是选项 -ide2 的别名

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`--cipassword` `<password>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`--citype` `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`--ciupgrade` `<boolean>` （<em>默认值 \=</em> `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`--ciuser` `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`--cores` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

每个 CPU 插槽的核心数。

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`--cpulimit` `<number> (0 - 128)` （<em>默认值 \=</em> `0`）**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` （<em>默认值 \=</em> `cgroup v1: 1024, cgroup v2: 100`）**

虚拟机的 CPU 权重，在 cgroup v2 中限制为 \[1, 10000\]。

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是将默认 EFI 变量复制到该卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--force` `<boolean>`**

强制物理删除。如果不设置此项，则只从配置文件中移除磁盘，并创建一个名为 <em>unused\[n\]</em> 的额外配置条目，其中包含卷 ID。解除 unused\[n\] 的链接始终会导致物理删除。

{% hint style="info" %}
需要选项：`delete`
{% endhint %}

**`--freeze` `<boolean>`**

启动时冻结 CPU（使用 <em>c</em> 监视器命令开始执行）。

**`--hookscript` `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

**`--hotplug` `<string>` （<em>默认值 \=</em> `network,disk,usb`）**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：<em>network</em>、<em>disk</em>、<em>cpu</em>、<em>memory</em>、<em>usb</em> 和 <em>cloudinit</em>。使用 <em>0</em> 完全禁用热插拔。将 <em>1</em> 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`--hugepages` `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 <em>any</em>，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 <em>dhcp</em> 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 <em>auto</em> 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`--ivshmem` `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`--keephugepages` `<boolean>` （<em>默认值 \=</em> `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`--kvm` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 KVM 硬件虚拟化。

**`--localtime` `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--memory` `[current=]<integer>`**

内存属性。

**`--migrate_downtime` `<number> (0 - N)` （<em>默认值 \=</em> `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`--migrate_speed` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`--name` `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`--nameserver` `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`--numa` `<boolean>` （<em>默认值 \=</em> `0`）**

启用/禁用 NUMA。

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`--onboot` `<boolean>`（<em>默认 \=</em> `0`）**

指定是否在系统启动时启动虚拟机。

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` （<em>默认值 \=</em> `other`）**

指定客户机操作系统。

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

**`--protection` `<boolean>`（<em>默认 \=</em> `0`）**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`--reboot` `<boolean>` （<em>默认值 \=</em> `1`）**

允许重启。如果设为 <em>0</em>，虚拟机将在重启时退出。

**`--revert` `<string>`**

撤销待处理的更改。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` （<em>默认值 \=</em> `lsi`）**

SCSI 控制器型号

**`--searchdomain` `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--serial[n]` `(/dev/[^,]+|socket)`**

在虚拟机内创建串口设备（n 为 0 到 3）

**`--shares` `<integer> (0 - 50000)` （<em>默认值 \=</em> `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`--smp` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

CPU 数量。请改用 -sockets 选项。

**`--sockets` `<integer> (1 - N)` （<em>默认值 \=</em> `1`）**

CPU 插槽数量。

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`--sshkeys` `<filepath>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` （<em>默认值 \=</em> `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、<em>2006-06-17T16:01:21</em> 或 <em>2006-06-17</em>。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--tablet` `<boolean>` （<em>默认值 \=</em> `1`）**

启用/禁用 USB 数位板设备。

**`--tags` `<string>`**

虚拟机的标签。这只是元信息。

**`--tdf` `<boolean>` （<em>默认值 \=</em> `0`）**

启用/禁用时间漂移修正。

**`--template` `<boolean>`（<em>默认 \=</em> `0`）**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 <em>raw</em>。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是使用 4 MiB。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`--vcpus` `<integer> (1 - N)` （<em>默认值 \=</em> `0`）**

热插拔的 vcpu 数量。

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 <em>import-from</em> 参数从现有卷导入。

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`--vmgenid` `<UUID>` （<em>默认值 \=</em> `1 (autogenerated)`）**

设置虚拟机世代 ID。使用 <em>1</em> 在创建或更新时自动生成，传入 <em>0</em> 可明确禁用。

**`--vmstatestorage` `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。

### <strong>qm showcmd</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_showcmd" id="cli_qm_showcmd"></a>

显示用于启动虚拟机的命令行（调试信息）。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--pretty` `<boolean>` （<em>默认值 \=</em> `0`）**

将每个选项放在单独一行，以提高可读性

**`--snapshot` `<string>`**

从指定快照获取配置值。

### <strong>qm shutdown</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_shutdown" id="cli_qm_shutdown"></a>

关闭虚拟机。这类似于按下物理机器的电源按钮。此操作会向客户机操作系统发送 ACPI 事件，随后客户机应执行正常关机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--forceStop` `<boolean>` (<em>默认 \=</em> `0`)**

确保虚拟机停止。

**`--keepActive` `<boolean>` （<em>默认值 \=</em> `0`）**

不停用存储卷。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒。

### <strong>qm snapshot</strong> `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_qm_snapshot" id="cli_qm_snapshot"></a>

为虚拟机创建快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--description` `<string>`**

文本描述或注释。

**`--vmstate` `<boolean>`**

保存 vmstate

### <strong>qm start</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_start" id="cli_qm_start"></a>

启动虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--force-cpu` `<string>`**

使用给定字符串覆盖 QEMU 的 -cpu 参数。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--migratedfrom` `<string>`**

集群节点名称。

**`--migration_network` `<string>`**

用于迁移的网络（或子网）的 CIDR。

**`--migration_type` `<insecure | secure>`**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`--nets-host-mtu` `net\d+=\d+(,net\d+=\d+)*`**

用于迁移兼容性。根据迁移源端的 QEMU 对象模型列出 VirtIO 网络设备及其有效的 host\_mtu 设置。值为 0 表示对应设备应避免使用 host\_mtu 参数。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--stateuri` `<string>`**

某些命令从此位置保存/恢复状态。

**`--targetstorage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 <em>1</em> 会将每个源存储映射到其自身。

**`--timeout` `<integer> (0 - N)` （<em>默认值 \=</em> `max(30, vm memory in GiB)`）**

最多等待 timeout 秒。

**`--with-conntrack-state` `<boolean>` （<em>默认值 \=</em> `0`）**

是否迁移运行中虚拟机的 conntrack 条目。

### <strong>qm status</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_status" id="cli_qm_status"></a>

显示虚拟机状态。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--verbose` `<boolean>`**

详细输出格式

### <strong>qm stop</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_stop" id="cli_qm_stop"></a>

停止虚拟机。qemu 进程将立即退出。这相当于拔掉正在运行的计算机的电源插头，可能损坏虚拟机数据。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--keepActive` `<boolean>` （<em>默认值 \=</em> `0`）**

不停用存储卷。

**`--migratedfrom` `<string>`**

集群节点名称。

**`--overrule-shutdown` `<boolean>`（<em>默认值 \=</em> `0`）**

停止前尝试中止活动的 <em>qmshutdown</em> 任务。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒。

### <strong>qm suspend</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_suspend" id="cli_qm_suspend"></a>

挂起虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--statestorage` `<storage ID>`**

存放虚拟机状态的存储

{% hint style="info" %}
需要选项：`todisk`
{% endhint %}

**`--todisk` `<boolean>` （<em>默认值 \=</em> `0`）**

如果设置，则将虚拟机挂起到磁盘。下次启动虚拟机时将恢复运行。

### <strong>qm template</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_template" id="cli_qm_template"></a>

创建模板。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

如果只想将 1 个磁盘转换为基础镜像。

### <strong>qm terminal</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_terminal" id="cli_qm_terminal"></a>

使用串口设备打开终端（虚拟机需要配置串口设备，例如 <em>serial0: socket</em>）

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--escape` `<string>` （<em>默认值 \=</em> `^O`）**

转义字符。

**`--iface` `<serial0 | serial1 | serial2 | serial3>`**

选择串口设备。默认使用首个合适的设备。

### <strong>qm unlink</strong> <a href="#cli_qm_unlink" id="cli_qm_unlink"></a>

<em>qm disk unlink</em> 的别名。

### <strong>qm unlock</strong> `<vmid>` <a href="#cli_qm_unlock" id="cli_qm_unlock"></a>

解锁 VM。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm vncproxy</strong> `<vmid>` <a href="#cli_qm_vncproxy" id="cli_qm_vncproxy"></a>

将虚拟机 VNC 流量代理到 stdin/stdout

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>qm wait</strong> `<vmid>` `[OPTIONS]` <a href="#cli_qm_wait" id="cli_qm_wait"></a>

等待虚拟机停止。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (1 - N)`**

超时时间，单位为秒。默认无限等待。

## 22.10. <strong>qmrestore</strong> \- 恢复 QemuServer `vzdump` 备份 <a href="#strong_qmrestore_strong_restore_qemuserver_span_class_monospaced_vzdump_span_backups" id="strong_qmrestore_strong_restore_qemuserver_span_class_monospaced_vzdump_span_backups"></a>

### <strong>qmrestore</strong> `help` <a href="#cli_qmrestore_help" id="cli_qmrestore_help"></a>

### <strong>qmrestore</strong> `<archive> <vmid>` `[OPTIONS]` <a href="#cli_qmrestore" id="cli_qmrestore"></a>

恢复 QemuServer vzdump 备份。

**`<archive>`: `<string>`**

备份文件。可以传入 <em>\-</em> 以从标准输入读取。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--bwlimit` `<number> (0 - N)`**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--force` `<boolean>`**

允许覆盖现有虚拟机。

**`--ha-managed` `<boolean>`（<em>默认 \=</em> `0`）**

恢复虚拟机后，将其添加为 HA 资源。

**`--live-restore` `<boolean>`**

立即从备份启动虚拟机，并在后台恢复。仅适用于 PBS。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--start` `<boolean>`（<em>默认 \=</em> `0`）**

成功恢复后启动虚拟机。

**`--storage` `<storage ID>`**

默认存储。

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

## 22.11. <strong>pct</strong> \- Proxmox 容器工具包 <a href="#strong_pct_strong_proxmox_container_toolkit" id="strong_pct_strong_proxmox_container_toolkit"></a>

### <strong>pct</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pct" id="cli_pct"></a>

### <strong>pct clone</strong> `<vmid> <newid>` `[OPTIONS]` <a href="#cli_pct_clone" id="cli_pct_clone"></a>

创建容器克隆/副本

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<newid>`: `<integer> (100 - 999999999)`**

克隆的 VMID。

**`--bwlimit` `<number> (0 - N)`（<em>默认 \=</em> `clone limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--description` `<string>`**

新 CT 的描述。

**`--full` `<boolean>`**

创建所有磁盘的完整副本。克隆普通 CT 时始终会执行此操作。对于 CT 模板，默认会尝试创建链接克隆。

**`--hostname` `<string>`**

为新 CT 设置主机名。

**`--pool` `<string>`**

将新 CT 添加到指定池。

**`--snapname` `<string>`**

快照的名称。

**`--storage` `<storage ID>`**

完整克隆的目标存储。

**`--target` `<string>`**

目标节点。仅当原始 VM 位于共享存储上时才允许。

### <strong>pct config</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_config" id="cli_pct_config"></a>

获取容器配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--current` `<boolean>`（<em>默认 \=</em> `0`）**

获取当前值（而非待生效值）。

**`--snapshot` `<string>`**

从指定快照获取配置值。

### <strong>pct console</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_console" id="cli_pct_console"></a>

为指定容器启动控制台。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--escape` `\^?[a-z]`（<em>默认 \=</em> `^a`）**

转义序列前缀。例如，要将 \<Ctrl\+b q\> 用作转义序列，请传递 <em>^b</em>。

### <strong>pct cpusets</strong> <a href="#cli_pct_cpusets" id="cli_pct_cpusets"></a>

打印已分配的 CPU 集合列表。

### <strong>pct create</strong> `<vmid> <ostemplate>` `[OPTIONS]` <a href="#cli_pct_create" id="cli_pct_create"></a>

创建或恢复容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<ostemplate>`: `<string>`**

操作系统模板或备份文件。

**`--arch` `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>`（<em>默认 \=</em> `amd64`）**

操作系统架构类型。

**`--bwlimit` `<number> (0 - N)`（<em>默认 \=</em> `restore limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cmode` `<console | shell | tty>`（<em>默认 \=</em> `tty`）**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 <em>console</em> 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 <em>shell</em>，它只会在容器内调用一个 shell（无需登录）。

**`--console` `<boolean>`（<em>默认 \=</em> `1`）**

将控制台设备（/dev/console）连接到容器。

**`--cores` `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`--cpulimit` `<number> (0 - 8192)`（<em>默认 \=</em> `0`）**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 <em>2</em>。值 <em>0</em> 表示不限制 CPU。
{% endhint %}

**`--cpuunits` `<integer> (0 - 500000)`（<em>默认 \=</em> `cgroup v1: 1024, cgroup v2: 100`）**

容器的 CPU 权重，在 cgroup v2 中会被限制在 \[1, 10000\] 范围内。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`--description` `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`--dev[n]` `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`--entrypoint` `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)`（<em>默认 \=</em> `/sbin/init`）**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`--env` `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`--features` `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`--force` `<boolean>`**

允许覆盖现有容器。

**`--ha-managed` `<boolean>`（<em>默认 \=</em> `0`）**

创建后，将 CT 添加为 HA 资源。

**`--hookscript` `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`--hostname` `<string>`**

为容器设置主机名。

**`--ignore-unpack-errors` `<boolean>`**

提取模板时忽略错误。

**`--lock` `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`--memory` `<integer> (16 - N)`（<em>默认 \=</em> `512`）**

容器的内存量，单位为 MB。

**`--mp[n]` `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`--nameserver` `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--net[n]` `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`--onboot` `<boolean>`（<em>默认 \=</em> `0`）**

指定容器是否在系统启动时启动。

**`--ostype` `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 <em>unmanaged</em> 跳过特定于操作系统的设置。

**`--password` `<password>`**

设置容器内的 root 密码。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>`（<em>默认 \=</em> `0`）**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`--restore` `<boolean>`**

将其标记为恢复任务。

**`--rootfs` `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`--searchdomain` `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--ssh-public-keys` `<filepath>`**

设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--start` `<boolean>`（<em>默认 \=</em> `0`）**

成功完成创建后启动 CT。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`（<em>默认 \=</em> `local`）**

默认存储。

**`--swap` `<integer> (0 - N)`（<em>默认 \=</em> `512`）**

容器的 SWAP 大小，单位为 MB。

**`--tags` `<string>`**

容器的标签。这只是元信息。

**`--template` `<boolean>`（<em>默认 \=</em> `0`）**

启用/禁用模板。

**`--timezone` `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 <em>host</em> 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`--tty` `<integer> (0 - 6)`（<em>默认 \=</em> `2`）**

指定容器可用的 tty 数量

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
需要选项：`restore`
{% endhint %}

**`--unprivileged` `<boolean>`（<em>默认 \=</em> `0`）**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`--unused[n]` `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

### <strong>pct delsnapshot</strong> `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_pct_delsnapshot" id="cli_pct_delsnapshot"></a>

删除 LXC 快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--force` `<boolean>`**

即使删除磁盘快照失败，也从配置文件中移除。

### <strong>pct destroy</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_destroy" id="cli_pct_destroy"></a>

销毁容器（同时删除所有相关文件）。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--destroy-unreferenced-disks` `<boolean>`**

如果设置，还会从所有已启用的存储中销毁具有该 VMID 但未在配置中引用的所有磁盘。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

强制销毁，即使正在运行。

**`--purge` `<boolean>` (<em>默认 \=</em> `0`)**

从所有相关配置中移除容器。例如，备份任务、复制任务或 HA。相关 ACL 和防火墙条目<strong>始终</strong>会被移除。

### <strong>pct df</strong> `<vmid>` <a href="#cli_pct_df" id="cli_pct_df"></a>

获取容器当前的磁盘使用情况。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct enter</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_enter" id="cli_pct_enter"></a>

为指定的容器启动 shell。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--keep-env` `<boolean>` (<em>默认 \=</em> `1`)**

保留当前环境。在 PVE 9 中，此选项将默认禁用。如果您依赖保留的环境，请使用此选项，以确保与未来版本兼容。

### <strong>pct exec</strong> `<vmid> [<extra-args>]` `[OPTIONS]` <a href="#cli_pct_exec" id="cli_pct_exec"></a>

在指定的容器内启动命令。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--keep-env` `<boolean>` (<em>默认 \=</em> `1`)**

保留当前环境。在 PVE 9 中，此选项将默认禁用。如果您依赖保留的环境，请使用此选项，以确保与未来版本兼容。

### <strong>pct fsck</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_fsck" id="cli_pct_fsck"></a>

对容器卷运行文件系统检查（fsck）。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--device` `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs>`**

要对其运行文件系统检查的卷

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

即使文件系统看起来干净，也强制检查

### <strong>pct fstrim</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_fstrim" id="cli_pct_fstrim"></a>

对选定的容器及其挂载点运行 fstrim，绑定挂载点或只读挂载点除外。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--ignore-mountpoints` `<boolean>`**

跳过所有挂载点，仅对容器根目录执行 fstrim。

### <strong>pct help</strong> `[OPTIONS]` <a href="#cli_pct_help" id="cli_pct_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pct list</strong> <a href="#cli_pct_list" id="cli_pct_list"></a>

LXC 容器索引（按节点）。

### <strong>pct listsnapshot</strong> `<vmid>` <a href="#cli_pct_listsnapshot" id="cli_pct_listsnapshot"></a>

列出所有快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct migrate</strong> `<vmid> <target>` `[OPTIONS]` <a href="#cli_pct_migrate" id="cli_pct_migrate"></a>

将容器迁移到另一个节点。创建新的迁移任务。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target>`: `<string>`**

目标节点。

**`--bwlimit` `<number> (0 - N)` (<em>默认 \=</em> `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--online` `<boolean>`**

使用在线迁移。

**`--restart` `<boolean>`**

使用重启迁移

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 <em>1</em> 会将每个源存储映射到其自身。

**`--timeout` `<integer>` (<em>默认 \=</em> `180`)**

重启迁移时等待关机的超时时间（秒）

### <strong>pct mount</strong> `<vmid>` <a href="#cli_pct_mount" id="cli_pct_mount"></a>

将容器的文件系统挂载到宿主机。这会锁定容器，仅用于紧急维护，因为除了启动和停止之外，它将阻止对容器执行其他操作。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct move-volume</strong> `<vmid> <volume> [<storage>] [<target-vmid>] [<target-volume>]` `[OPTIONS]` <a href="#cli_pct_move-volume" id="cli_pct_move-volume"></a>

将 rootfs-/mp-volume 移动到其他存储或其他容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<volume>`: `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99>`**

将被移动的卷。

**`<storage>`: `<storage ID>`**

目标存储。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-volume>`: `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99>`**

卷将移动到的配置键。默认为源卷的配置键。

**`--bwlimit` `<number> (0 - N)`（<em>默认 \=</em> `clone limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (<em>默认 \=</em> `0`)**

成功复制后删除原始卷。默认情况下，原始卷会作为未使用的卷条目保留。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--target-digest` `<string>`**

如果目标容器的当前配置文件具有不同的 SHA1 摘要，则阻止更改。这可用于防止并发修改。

### <strong>pct move\_volume</strong> <a href="#cli_pct_move_volume" id="cli_pct_move_volume"></a>

<em>pct move-volume</em> 的别名。

### <strong>pct pending</strong> `<vmid>` <a href="#cli_pct_pending" id="cli_pct_pending"></a>

获取容器配置，包括待处理的更改。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct pull</strong> `<vmid> <path> <destination>` `[OPTIONS]` <a href="#cli_pct_pull" id="cli_pct_pull"></a>

将文件从容器复制到本地系统。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<path>`: `<string>`**

要提取的容器内文件的路径。

**`<destination>`: `<string>`**

目标位置

**`--group` `<string>`**

属组名称或 ID。

**`--perms` `<string>`**

要使用的文件权限（默认为八进制，使用十六进制时以 <em>0x</em> 为前缀）。

**`--user` `<string>`**

属主用户名或 ID。

### <strong>pct push</strong> `<vmid> <file> <destination>` `[OPTIONS]` <a href="#cli_pct_push" id="cli_pct_push"></a>

将本地文件复制到容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<file>`: `<string>`**

本地文件的路径。

**`<destination>`: `<string>`**

要写入的容器内目标位置。

**`--group` `<string>`**

属组名称或 ID。使用名称时，该名称必须存在于容器内。

**`--perms` `<string>`**

要使用的文件权限（默认为八进制，使用十六进制时以 <em>0x</em> 为前缀）。

**`--user` `<string>`**

属主用户名或 ID。使用名称时，该名称必须存在于容器内。

### <strong>pct reboot</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_reboot" id="cli_pct_reboot"></a>

通过关机并重新启动来重启容器。应用待处理的更改。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒以完成关机。

### <strong>pct remote-migrate</strong> `<vmid> [<target-vmid>] <target-endpoint> --target-bridge <string> --target-storage <string>` `[OPTIONS]` <a href="#cli_pct_remote-migrate" id="cli_pct_remote-migrate"></a>

将容器迁移到远程集群。创建新的迁移任务。实验性功能！

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-endpoint>`: `apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]`**

远程目标端点

**`--bwlimit` `<integer> (0 - N)` (<em>默认 \=</em> `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (<em>默认 \=</em> `0`)**

成功迁移后删除原始 CT 及相关数据。默认情况下，原始 CT 会以停止状态保留在源集群上。

**`--online` `<boolean>`**

使用在线迁移。

**`--restart` `<boolean>`**

使用重启迁移

**`--target-bridge` `<string>`**

从源网桥到目标网桥的映射。仅提供一个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 <em>1</em> 会将每个源网桥映射到其自身。

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 <em>1</em> 会将每个源存储映射到其自身。

**`--timeout` `<integer>` (<em>默认 \=</em> `180`)**

重启迁移时等待关机的超时时间（秒）

### <strong>pct rescan</strong> `[OPTIONS]` <a href="#cli_pct_rescan" id="cli_pct_rescan"></a>

重新扫描所有存储，并更新磁盘大小和未使用的磁盘映像。

**`--dryrun` `<boolean>` (<em>默认 \=</em> `0`)**

不实际将更改写入配置。

**`--vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct resize</strong> `<vmid> <disk> <size>` `[OPTIONS]` <a href="#cli_pct_resize" id="cli_pct_resize"></a>

调整容器挂载点的大小。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs>`**

要调整大小的磁盘。

**`<size>`: `\+?\d+(\.\d+)?[KMGT]?`**

新大小。带有 <em>\+</em> 符号时，该值会加到卷的实际大小上；不带该符号时，该值将被视为绝对大小。不支持缩小磁盘。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

### <strong>pct restore</strong> `<vmid> <ostemplate>` `[OPTIONS]` <a href="#cli_pct_restore" id="cli_pct_restore"></a>

创建或恢复容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<ostemplate>`: `<string>`**

操作系统模板或备份文件。

**`--arch` `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>`（<em>默认 \=</em> `amd64`）**

操作系统架构类型。

**`--bwlimit` `<number> (0 - N)`（<em>默认 \=</em> `restore limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cmode` `<console | shell | tty>`（<em>默认 \=</em> `tty`）**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 <em>console</em> 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 <em>shell</em>，它只会在容器内调用一个 shell（无需登录）。

**`--console` `<boolean>`（<em>默认 \=</em> `1`）**

将控制台设备（/dev/console）连接到容器。

**`--cores` `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`--cpulimit` `<number> (0 - 8192)`（<em>默认 \=</em> `0`）**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 <em>2</em>。值 <em>0</em> 表示不限制 CPU。
{% endhint %}

**`--cpuunits` `<integer> (0 - 500000)`（<em>默认 \=</em> `cgroup v1: 1024, cgroup v2: 100`）**

容器的 CPU 权重，在 cgroup v2 中会被限制在 \[1, 10000\] 范围内。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`--description` `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`--dev[n]` `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`--entrypoint` `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)`（<em>默认 \=</em> `/sbin/init`）**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`--env` `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`--features` `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`--force` `<boolean>`**

允许覆盖现有容器。

**`--ha-managed` `<boolean>`（<em>默认 \=</em> `0`）**

创建后，将 CT 添加为 HA 资源。

**`--hookscript` `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`--hostname` `<string>`**

为容器设置主机名。

**`--ignore-unpack-errors` `<boolean>`**

提取模板时忽略错误。

**`--lock` `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`--memory` `<integer> (16 - N)`（<em>默认 \=</em> `512`）**

容器的内存量，单位为 MB。

**`--mp[n]` `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`--nameserver` `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--net[n]` `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`--onboot` `<boolean>`（<em>默认 \=</em> `0`）**

指定容器是否在系统启动时启动。

**`--ostype` `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 <em>unmanaged</em> 跳过特定于操作系统的设置。

**`--password` `<password>`**

设置容器内的 root 密码。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>`（<em>默认 \=</em> `0`）**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`--rootfs` `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`--searchdomain` `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--ssh-public-keys` `<filepath>`**

设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--start` `<boolean>`（<em>默认 \=</em> `0`）**

成功完成创建后启动 CT。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`（<em>默认 \=</em> `local`）**

默认存储。

**`--swap` `<integer> (0 - N)`（<em>默认 \=</em> `512`）**

容器的 SWAP 大小，单位为 MB。

**`--tags` `<string>`**

容器的标签。这只是元信息。

**`--template` `<boolean>`（<em>默认 \=</em> `0`）**

启用/禁用模板。

**`--timezone` `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 <em>host</em> 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`--tty` `<integer> (0 - 6)`（<em>默认 \=</em> `2`）**

指定容器可用的 tty 数量

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
需要选项：`restore`
{% endhint %}

**`--unprivileged` `<boolean>`（<em>默认 \=</em> `0`）**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`--unused[n]` `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

### <strong>pct resume</strong> `<vmid>` <a href="#cli_pct_resume" id="cli_pct_resume"></a>

恢复容器运行。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct rollback</strong> `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_pct_rollback" id="cli_pct_rollback"></a>

将 LXC 状态回滚到指定快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--start` `<boolean>`（<em>默认 \=</em> `0`）**

成功回滚后是否应启动容器

### <strong>pct set</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_set" id="cli_pct_set"></a>

设置容器选项。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--arch` `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>`（<em>默认 \=</em> `amd64`）**

操作系统架构类型。

**`--cmode` `<console | shell | tty>`（<em>默认 \=</em> `tty`）**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 <em>console</em> 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 <em>shell</em>，它只会在容器内调用一个 shell（无需登录）。

**`--console` `<boolean>`（<em>默认 \=</em> `1`）**

将控制台设备（/dev/console）连接到容器。

**`--cores` `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`--cpulimit` `<number> (0 - 8192)`（<em>默认 \=</em> `0`）**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 <em>2</em>。值 <em>0</em> 表示不限制 CPU。
{% endhint %}

**`--cpuunits` `<integer> (0 - 500000)`（<em>默认 \=</em> `cgroup v1: 1024, cgroup v2: 100`）**

容器的 CPU 权重，在 cgroup v2 中会被限制在 \[1, 10000\] 范围内。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`--dev[n]` `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--entrypoint` `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)`（<em>默认 \=</em> `/sbin/init`）**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`--env` `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`--features` `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`--hookscript` `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`--hostname` `<string>`**

为容器设置主机名。

**`--lock` `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`--memory` `<integer> (16 - N)`（<em>默认 \=</em> `512`）**

容器的内存量，单位为 MB。

**`--mp[n]` `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`--nameserver` `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--net[n]` `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`--onboot` `<boolean>`（<em>默认 \=</em> `0`）**

指定容器是否在系统启动时启动。

**`--ostype` `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 <em>unmanaged</em> 跳过特定于操作系统的设置。

**`--protection` `<boolean>`（<em>默认 \=</em> `0`）**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`--revert` `<string>`**

撤销待处理的更改。

**`--rootfs` `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`--searchdomain` `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--swap` `<integer> (0 - N)`（<em>默认 \=</em> `512`）**

容器的 SWAP 大小，单位为 MB。

**`--tags` `<string>`**

容器的标签。这只是元信息。

**`--template` `<boolean>`（<em>默认 \=</em> `0`）**

启用/禁用模板。

**`--timezone` `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 <em>host</em> 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`--tty` `<integer> (0 - 6)`（<em>默认 \=</em> `2`）**

指定容器可用的 tty 数量

**`--unprivileged` `<boolean>`（<em>默认 \=</em> `0`）**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`--unused[n]` `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

### <strong>pct shutdown</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_shutdown" id="cli_pct_shutdown"></a>

关闭容器。这会触发容器正常关机，详情请参阅 lxc-stop(1)。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--forceStop` `<boolean>` (<em>默认 \=</em> `0`)**

确保容器停止。

**`--timeout` `<integer> (0 - N)` (<em>默认 \=</em> `60`)**

最多等待 timeout 秒。

### <strong>pct snapshot</strong> `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_pct_snapshot" id="cli_pct_snapshot"></a>

为容器创建快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--description` `<string>`**

文本描述或注释。

### <strong>pct start</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_start" id="cli_pct_start"></a>

启动容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

如果设置，启动时会启用非常详细的调试日志级别。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>pct status</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_status" id="cli_pct_status"></a>

显示 CT 状态。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--verbose` `<boolean>`**

详细输出格式

### <strong>pct stop</strong> `<vmid>` `[OPTIONS]` <a href="#cli_pct_stop" id="cli_pct_stop"></a>

停止容器。这将突然终止容器中运行的所有进程。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--overrule-shutdown` `<boolean>`（<em>默认值 \=</em> `0`）**

停止前尝试中止正在运行的 <em>vzshutdown</em> 任务。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

### <strong>pct suspend</strong> `<vmid>` <a href="#cli_pct_suspend" id="cli_pct_suspend"></a>

挂起容器。此功能处于实验阶段。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct template</strong> `<vmid>` <a href="#cli_pct_template" id="cli_pct_template"></a>

创建模板。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct unlock</strong> `<vmid>` <a href="#cli_pct_unlock" id="cli_pct_unlock"></a>

解锁 VM。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

### <strong>pct unmount</strong> `<vmid>` <a href="#cli_pct_unmount" id="cli_pct_unmount"></a>

卸载容器的文件系统。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## 22.12. <strong>pveam</strong> \- Proxmox VE 设备模板管理器 <a href="#strong_pveam_strong_proxmox_ve_appliance_manager" id="strong_pveam_strong_proxmox_ve_appliance_manager"></a>

### <strong>pveam</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveam" id="cli_pveam"></a>

### <strong>pveam available</strong> `[OPTIONS]` <a href="#cli_pveam_available" id="cli_pveam_available"></a>

列出可用模板。

**`--section` `<mail | system | turnkeylinux>`**

将列表限制为指定部分。

### <strong>pveam download</strong> `<storage> <template>` <a href="#cli_pveam_download" id="cli_pveam_download"></a>

下载设备模板。

**`<storage>`: `<storage ID>`**

用于保存模板的存储

**`<template>`: `<string>`**

要下载的模板

### <strong>pveam help</strong> `[OPTIONS]` <a href="#cli_pveam_help" id="cli_pveam_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pveam list</strong> `<storage>` <a href="#cli_pveam_list" id="cli_pveam_list"></a>

获取存储上的所有模板列表

**`<storage>`: `<storage ID>`**

仅列出指定存储上的模板

### <strong>pveam remove</strong> `<template_path>` <a href="#cli_pveam_remove" id="cli_pveam_remove"></a>

移除模板。

**`<template_path>`: `<string>`**

要移除的模板。

### <strong>pveam update</strong> <a href="#cli_pveam_update" id="cli_pveam_update"></a>

更新容器模板数据库。

## 22.13. <strong>pvecm</strong> \- Proxmox VE 集群管理器 <a href="#strong_pvecm_strong_proxmox_ve_cluster_manager" id="strong_pvecm_strong_proxmox_ve_cluster_manager"></a>

### <strong>pvecm</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvecm" id="cli_pvecm"></a>

### <strong>pvecm add</strong> `<hostname>` `[OPTIONS]` <a href="#cli_pvecm_add" id="cli_pvecm_add"></a>

将当前节点加入现有集群。

**`<hostname>`: `<string>`**

现有集群成员的主机名（或 IP）。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--force` `<boolean>`**

如果节点已存在，则不抛出错误。

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

单个 corosync 链路的地址和优先级信息。（最多支持 8 个链路；link0..link7）

**`--nodeid` `<integer> (1 - N)`**

此节点的节点 ID。

**`--use_ssh` `<boolean>`**

始终使用 SSH 加入，即使对端可以通过 API 完成。

**`--votes` `<integer> (0 - N)`**

此节点的票数

### <strong>pvecm addnode</strong> `<node>` `[OPTIONS]` <a href="#cli_pvecm_addnode" id="cli_pvecm_addnode"></a>

将节点添加到集群配置。此调用供内部使用。

**`<node>`: `<string>`**

集群节点名称。

**`--apiversion` `<integer>`**

新节点的 JOIN\_API\_VERSION。

**`--force` `<boolean>`**

如果节点已存在，则不抛出错误。

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

单个 corosync 链路的地址和优先级信息。（最多支持 8 个链路；link0..link7）

**`--new_node_ip` `<string>`**

要添加节点的 IP 地址。未提供链路时用作回退值。

**`--nodeid` `<integer> (1 - N)`**

此节点的节点 ID。

**`--votes` `<integer> (0 - N)`**

此节点的票数

### <strong>pvecm apiver</strong> <a href="#cli_pvecm_apiver" id="cli_pvecm_apiver"></a>

返回此节点上可用的集群加入 API 版本。

### <strong>pvecm create</strong> `<clustername>` `[OPTIONS]` <a href="#cli_pvecm_create" id="cli_pvecm_create"></a>

生成新的集群配置。如果未提供链路，则默认将本地 IP 地址用作 link0。

**`<clustername>`: `<string>`**

集群名称。

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

单个 corosync 链路的地址和优先级信息。（最多支持 8 个链路；link0..link7）

**`--nodeid` `<integer> (1 - N)`**

此节点的节点 ID。

**`--token-coefficient` `<integer> (0 - N)` （<em>默认值 \=</em> `125`）**

用于确定 Corosync 令牌超时时间的系数。详情请参阅 corosync.conf(5) 手册。

**`--votes` `<integer> (1 - N)`**

此节点的票数。

### <strong>pvecm delnode</strong> `<node>` <a href="#cli_pvecm_delnode" id="cli_pvecm_delnode"></a>

从集群配置中移除节点。

**`<node>`: `<string>`**

集群节点名称。

### <strong>pvecm expected</strong> `<expected>` <a href="#cli_pvecm_expected" id="cli_pvecm_expected"></a>

告知 corosync 新的预期票数值。

**`<expected>`: `<integer> (1 - N)`**

预期票数

### <strong>pvecm help</strong> `[OPTIONS]` <a href="#cli_pvecm_help" id="cli_pvecm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvecm keygen</strong> `<filename>` <a href="#cli_pvecm_keygen" id="cli_pvecm_keygen"></a>

为 corosync 生成新的加密密钥。

**`<filename>`: `<string>`**

输出文件名

### <strong>pvecm mtunnel</strong> `[<extra-args>]` `[OPTIONS]` <a href="#cli_pvecm_mtunnel" id="cli_pvecm_mtunnel"></a>

由虚拟机/容器迁移使用，请勿手动使用。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--get_migration_ip` `<boolean>` （<em>默认值 \=</em> `0`）**

如果配置了迁移 IP，则返回该 IP

**`--migration_network` `<string>`**

用于检测本地迁移 IP 的迁移网络

**`--run-command` `<boolean>`**

运行命令，并使用 tcp 套接字作为标准输入。首先通过此命令的标准输出打印 IP 地址和端口，各占一行。

### <strong>pvecm nodes</strong> <a href="#cli_pvecm_nodes" id="cli_pvecm_nodes"></a>

显示本地所见的集群节点。

### <strong>pvecm qdevice remove</strong> <a href="#cli_pvecm_qdevice_remove" id="cli_pvecm_qdevice_remove"></a>

移除已配置的 QDevice

### <strong>pvecm qdevice setup</strong> `<address>` `[OPTIONS]` <a href="#cli_pvecm_qdevice_setup" id="cli_pvecm_qdevice_setup"></a>

设置 QDevice 的使用

**`<address>`: `<string>`**

指定外部 corosync QDevice 的网络地址

**`--force` `<boolean>`**

遇到可能危险的操作时不抛出错误。

**`--network` `<string>`**

应使用哪个网络连接外部 qdevice

### <strong>pvecm status</strong> <a href="#cli_pvecm_status" id="cli_pvecm_status"></a>

显示本地所见的集群状态。

### <strong>pvecm updatecerts</strong> `[OPTIONS]` <a href="#cli_pvecm_updatecerts" id="cli_pvecm_updatecerts"></a>

更新节点证书（并生成所有所需文件/目录）。

**`--force` `<boolean>`**

强制生成新的 SSL 证书。

**`--silent` `<boolean>`**

忽略错误（例如集群没有仲裁时）。

**`--unmerge-known-hosts` `<boolean>` （<em>默认值 \=</em> `0`）**

取消合并旧版 SSH 已知主机记录。

## 22.14. <strong>pvesr</strong> \- Proxmox VE 存储复制 <a href="#strong_pvesr_strong_proxmox_ve_storage_replication" id="strong_pvesr_strong_proxmox_ve_storage_replication"></a>

### <strong>pvesr</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesr" id="cli_pvesr"></a>

### <strong>pvesr create-local-job</strong> `<id> <target>` `[OPTIONS]` <a href="#cli_pvesr_create-local-job" id="cli_pvesr_create-local-job"></a>

创建新的复制任务

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

**`<target>`: `<string>`**

目标节点。

**`--comment` `<string>`**

描述。

**`--disable` `<boolean>`**

用于禁用/停用条目的标志。

**`--rate` `<number> (1 - N)`**

以 mbps（兆字节每秒）为单位的浮点数速率限制。

**`--remove_job` `<full | local>`**

将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 <em>full</em>，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。

**`--schedule` `<string>` （<em>默认值 \=</em> `*/15`）**

存储复制计划。其格式是 `systemd` 日历事件的一个子集。

**`--source` `<string>`**

供内部使用，用于检测客户机是否被接管。

### <strong>pvesr delete</strong> `<id>` `[OPTIONS]` <a href="#cli_pvesr_delete" id="cli_pvesr_delete"></a>

将复制任务标记为待移除。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

将移除 jobconfig 条目，但不执行清理。

**`--keep` `<boolean>` （<em>默认值 \=</em> `0`）**

保留目标上的复制数据（不移除）。

### <strong>pvesr disable</strong> `<id>` <a href="#cli_pvesr_disable" id="cli_pvesr_disable"></a>

禁用复制任务。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

### <strong>pvesr enable</strong> `<id>` <a href="#cli_pvesr_enable" id="cli_pvesr_enable"></a>

启用复制任务。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

### <strong>pvesr finalize-local-job</strong> `<id> [<extra-args>]` `[OPTIONS]` <a href="#cli_pvesr_finalize-local-job" id="cli_pvesr_finalize-local-job"></a>

完成复制任务的收尾工作。这会移除时间戳与 \<last\_sync\> 不同的所有复制快照。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

**`<extra-args>`: `<array>`**

要考虑的卷 ID 列表。

**`--last_sync` `<integer> (0 - N)`**

上次成功同步的时间（UNIX 纪元时间）。如果未指定，则移除所有复制快照。

### <strong>pvesr help</strong> `[OPTIONS]` <a href="#cli_pvesr_help" id="cli_pvesr_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvesr list</strong> <a href="#cli_pvesr_list" id="cli_pvesr_list"></a>

列出复制任务。

### <strong>pvesr prepare-local-job</strong> `<id> [<extra-args>]` `[OPTIONS]` <a href="#cli_pvesr_prepare-local-job" id="cli_pvesr_prepare-local-job"></a>

准备启动复制任务。在复制开始之前，在目标节点上调用。此调用供内部使用，并在 stdout 上返回 JSON 对象。此方法首先检查虚拟机 \<vmid\> 是否位于本地节点上。如果是，则立即停止。随后此方法扫描所有卷 ID，查找快照，并移除时间戳与 \<last\_sync\> 不同的所有复制快照。它也会移除任何未使用的卷。返回一个哈希，对所有存在复制快照的卷提供布尔标记。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

**`<extra-args>`: `<array>`**

要考虑的卷 ID 列表。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

允许移除所有现有卷（卷列表为空）。

**`--last_sync` `<integer> (0 - N)`**

上次成功同步的时间（UNIX 纪元时间）。如果未指定，则移除所有复制快照。

**`--parent_snapname` `<string>`**

快照的名称。

**`--scan` `<string>`**

要扫描陈旧卷的存储 ID 列表。

### <strong>pvesr read</strong> `<id>` <a href="#cli_pvesr_read" id="cli_pvesr_read"></a>

读取复制任务配置。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

### <strong>pvesr run</strong> `[OPTIONS]` <a href="#cli_pvesr_run" id="cli_pvesr_run"></a>

此方法由 systemd-timer 调用，并执行所有同步任务或指定同步任务。

**`--id` `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

**`--mail` `<boolean>` （<em>默认值 \=</em> `0`）**

发生故障时发送电子邮件通知。

**`--verbose` `<boolean>`（<em>默认值 \=</em> `0`）**

向 stdout 打印更详细的日志。

### <strong>pvesr schedule-now</strong> `<id>` <a href="#cli_pvesr_schedule-now" id="cli_pvesr_schedule-now"></a>

安排复制任务尽快启动。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

### <strong>pvesr set-state</strong> `<vmid> <state>` <a href="#cli_pvesr_set-state" id="cli_pvesr_set-state"></a>

在迁移时设置任务复制状态。此调用供内部使用。它接受 JSON 对象形式的任务状态。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<state>`: `<string>`**

作为 JSON 解码后字符串的任务状态。

### <strong>pvesr status</strong> `[OPTIONS]` <a href="#cli_pvesr_status" id="cli_pvesr_status"></a>

列出此节点上所有复制任务的状态。

**`--guest` `<integer> (100 - 999999999)`**

仅列出此客户机的复制任务。

### <strong>pvesr update</strong> `<id>` `[OPTIONS]` <a href="#cli_pvesr_update" id="cli_pvesr_update"></a>

更新复制任务配置。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 <em>\<GUEST\>-\<JOBNUM\></em>。

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

用于禁用/停用条目的标志。

**`--rate` `<number> (1 - N)`**

以 mbps（兆字节每秒）为单位的浮点数速率限制。

**`--remove_job` `<full | local>`**

将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 <em>full</em>，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。

**`--schedule` `<string>` （<em>默认值 \=</em> `*/15`）**

存储复制计划。其格式是 `systemd` 日历事件的一个子集。

**`--source` `<string>`**

供内部使用，用于检测客户机是否被接管。

## 22.15. <strong>pveum</strong> \- Proxmox VE 用户管理器 <a href="#strong_pveum_strong_proxmox_ve_user_manager" id="strong_pveum_strong_proxmox_ve_user_manager"></a>

### <strong>pveum</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveum" id="cli_pveum"></a>

### <strong>pveum acl delete</strong> `<path> --roles <string>` `[OPTIONS]` <a href="#cli_pveum_acl_delete" id="cli_pveum_acl_delete"></a>

更新访问控制列表（添加或移除权限）。

**`<path>`: `<string>`**

访问控制路径

**`--groups` `<string>`**

组列表。

**`--propagate` `<boolean>` （<em>默认值 \=</em> `1`）**

允许传播（继承）权限。

**`--roles` `<string>`**

角色列表。

**`--tokens` `<string>`**

API 令牌列表。

**`--users` `<string>`**

用户列表。

### <strong>pveum acl list</strong> `[FORMAT_OPTIONS]` <a href="#cli_pveum_acl_list" id="cli_pveum_acl_list"></a>

获取访问控制列表（ACL）。

### <strong>pveum acl modify</strong> `<path> --roles <string>` `[OPTIONS]` <a href="#cli_pveum_acl_modify" id="cli_pveum_acl_modify"></a>

更新访问控制列表（添加或移除权限）。

**`<path>`: `<string>`**

访问控制路径

**`--groups` `<string>`**

组列表。

**`--propagate` `<boolean>` （<em>默认值 \=</em> `1`）**

允许传播（继承）权限。

**`--roles` `<string>`**

角色列表。

**`--tokens` `<string>`**

API 令牌列表。

**`--users` `<string>`**

用户列表。

### <strong>pveum acldel</strong> <a href="#cli_pveum_acldel" id="cli_pveum_acldel"></a>

<em>pveum acl delete</em> 的别名。

### <strong>pveum aclmod</strong> <a href="#cli_pveum_aclmod" id="cli_pveum_aclmod"></a>

<em>pveum acl modify</em> 的别名。

### <strong>pveum group add</strong> `<groupid>` `[OPTIONS]` <a href="#cli_pveum_group_add" id="cli_pveum_group_add"></a>

创建新组。

**`<groupid>`: `<string>`**

没有可用的说明

**`--comment` `<string>`**

没有可用的说明

### <strong>pveum group delete</strong> `<groupid>` <a href="#cli_pveum_group_delete" id="cli_pveum_group_delete"></a>

删除组。

**`<groupid>`: `<string>`**

没有可用的说明

### <strong>pveum group list</strong> `[FORMAT_OPTIONS]` <a href="#cli_pveum_group_list" id="cli_pveum_group_list"></a>

组索引。

### <strong>pveum group modify</strong> `<groupid>` `[OPTIONS]` <a href="#cli_pveum_group_modify" id="cli_pveum_group_modify"></a>

更新组数据。

**`<groupid>`: `<string>`**

没有可用的说明

**`--comment` `<string>`**

没有可用的说明

### <strong>pveum groupadd</strong> <a href="#cli_pveum_groupadd" id="cli_pveum_groupadd"></a>

<em>pveum group add</em> 的别名。

### <strong>pveum groupdel</strong> <a href="#cli_pveum_groupdel" id="cli_pveum_groupdel"></a>

<em>pveum group delete</em> 的别名。

### <strong>pveum groupmod</strong> <a href="#cli_pveum_groupmod" id="cli_pveum_groupmod"></a>

<em>pveum group modify</em> 的别名。

### <strong>pveum help</strong> `[OPTIONS]` <a href="#cli_pveum_help" id="cli_pveum_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pveum passwd</strong> `<userid>` `[OPTIONS]` <a href="#cli_pveum_passwd" id="cli_pveum_passwd"></a>

更改用户密码。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--confirmation-password` `<string>`**

执行更改的用户的当前密码。

### <strong>pveum pool add</strong> `<poolid>` `[OPTIONS]` <a href="#cli_pveum_pool_add" id="cli_pveum_pool_add"></a>

创建新资源池。

**`<poolid>`: `<string>`**

没有可用的说明

**`--comment` `<string>`**

没有可用的说明

### <strong>pveum pool delete</strong> `<poolid>` <a href="#cli_pveum_pool_delete" id="cli_pveum_pool_delete"></a>

删除资源池。

**`<poolid>`: `<string>`**

没有可用的说明

### <strong>pveum pool list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_pool_list" id="cli_pveum_pool_list"></a>

列出资源池或获取资源池配置。

**`--poolid` `<string>`**

没有可用的说明

**`--type` `<lxc | qemu | storage>`**

没有可用的说明

{% hint style="info" %}
需要选项：`poolid`
{% endhint %}

### <strong>pveum pool modify</strong> `<poolid>` `[OPTIONS]` <a href="#cli_pveum_pool_modify" id="cli_pveum_pool_modify"></a>

更新资源池。

**`<poolid>`: `<string>`**

没有可用的说明

**`--allow-move` `<boolean>` （<em>默认值 \=</em> `0`）**

即使客户机已在其他资源池中，也允许添加。客户机将从当前资源池移除，并添加到此资源池。

**`--comment` `<string>`**

没有可用的说明

**`--delete` `<boolean>` (<em>默认 \=</em> `0`)**

移除传入的 VMID 和/或存储 ID，而非添加。

**`--storage` `<string>`**

要添加到此资源池或从中移除的存储 ID 列表。

**`--vms` `<string>`**

要添加到此资源池或从中移除的客户机 VMID 列表。

### <strong>pveum realm add</strong> `<realm> --type <string>` `[OPTIONS]` <a href="#cli_pveum_realm_add" id="cli_pveum_realm_add"></a>

添加认证服务器。

**`<realm>`: `<string>`**

认证域 ID

**`--acr-values` `^[^\x00-\x1F\x7F <>#"]*$`**

指定请求授权服务器在认证请求中使用的认证上下文类引用值。

**`--audiences` `^[^\x00-\x1F\x7F <>#"]*$`**

除了 <em>client-id</em> 之外，还接受 OpenID 签发者可能包含的受众列表。

**`--autocreate` `<boolean>` （<em>默认值 \=</em> `0`）**

如果用户不存在，则自动创建。

**`--base_dn` `<string>`**

LDAP 基础域名

**`--bind_dn` `<string>`**

LDAP 绑定域名

**`--capath` `<string>` （<em>默认值 \=</em> `/etc/ssl/certs`）**

CA 证书存储路径

**`--case-sensitive` `<boolean>` （<em>默认值 \=</em> `1`）**

用户名区分大小写

**`--cert` `<string>`**

客户端证书路径

**`--certkey` `<string>`**

客户端证书密钥路径

**`--check-connection` `<boolean>` （<em>默认值 \=</em> `0`）**

检查与服务器的绑定连接。

**`--client-id` `<string>`**

OpenID 客户端 ID

**`--client-key` `<string>`**

OpenID 客户端密钥

**`--comment` `<string>`**

描述。

**`--default` `<boolean>`**

将此认证域用作默认认证域

**`--domain` `\S+`**

AD 域名

**`--filter` `<string>`**

用户同步的 LDAP 过滤器。

**`--group_classes` `<string>` （<em>默认值 \=</em> `groupOfNames, group, univentionGroup, ipausergroup`）**

组的对象类。

**`--group_dn` `<string>`**

组同步的 LDAP 基础域名。如果未设置，则使用 base\_dn。

**`--group_filter` `<string>`**

组同步的 LDAP 过滤器。

**`--group_name_attr` `<string>`**

表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。

**`--groups-autocreate` `<boolean>` （<em>默认值 \=</em> `0`）**

如果组不存在，则自动创建。

**`--groups-claim` `(?^:[A-Za-z0-9\.\-_]+)`**

用于获取组的 OpenID 声明。

**`--groups-overwrite` `<boolean>` （<em>默认值 \=</em> `0`）**

登录时覆盖该用户的所有组。

**`--issuer-url` `<string>`**

OpenID 签发者 URL

**`--mode` `<ldap | ldap+starttls | ldaps>` （<em>默认值 \=</em> `ldap`）**

LDAP 协议模式。

**`--password` `<string>`**

LDAP 绑定密码。将保存在 <em>/etc/pve/priv/realm/\<REALM\>.pw</em> 中。

**`--port` `<integer> (1 - 65535)`**

服务器端口。

**`--prompt` `(?:none|login|consent|select_account|\S+)`**

指定授权服务器是否提示最终用户重新认证并同意。

**`--query-userinfo` `<boolean>` （<em>默认值 \=</em> `1`）**

启用对 userinfo 端点的查询，以获取声明值。

**`--scopes` `<string>` （<em>默认值 \=</em> `email profile`）**

指定应授权并返回的作用域（用户详细信息），例如 <em>email</em> 或 <em>profile</em>。

**`--secure` `<boolean>`**

使用安全的 LDAPS 协议。已弃用：请改用 <em>mode</em>。

**`--server1` `<string>`**

服务器 IP 地址（或 DNS 名称）

**`--server2` `<string>`**

备用服务器 IP 地址（或 DNS 名称）

**`--sslversion` `<tlsv1 | tlsv1_1 | tlsv1_2 | tlsv1_3>`**

LDAPS TLS/SSL 版本。不建议使用低于 1.2 的版本！

**`--sync-defaults-options` `[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]`**

同步行为的默认选项。

**`--sync_attributes` `\w+=[^,]+(,\s*\w+=[^,]+)*`**

以逗号分隔的 key\=value 对列表，用于指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 <em>mail</em> 映射到 PVE 的 <em>email</em>，请写入 <em>email\=mail</em>。默认情况下，每个 PVE 用户字段都由同名 LDAP 属性表示。

**`--tfa` `type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]`**

使用双因素认证。

**`--type` `<ad | ldap | openid | pam | pve>`**

认证域类型。

**`--user_attr` `\S{2,}`**

LDAP 用户属性名称

**`--user_classes` `<string>` （<em>默认值 \=</em> `inetorgperson, posixaccount, person, user`）**

用户的对象类。

**`--username-claim` `<string>`**

用于生成唯一用户名的 OpenID 声明。

**`--verify` `<boolean>` （<em>默认值 \=</em> `0`）**

验证服务器的 SSL 证书

### <strong>pveum realm delete</strong> `<realm>` <a href="#cli_pveum_realm_delete" id="cli_pveum_realm_delete"></a>

删除认证服务器。

**`<realm>`: `<string>`**

认证域 ID

### <strong>pveum realm list</strong> `[FORMAT_OPTIONS]` <a href="#cli_pveum_realm_list" id="cli_pveum_realm_list"></a>

认证域索引。

### <strong>pveum realm modify</strong> `<realm>` `[OPTIONS]` <a href="#cli_pveum_realm_modify" id="cli_pveum_realm_modify"></a>

更新认证服务器设置。

**`<realm>`: `<string>`**

认证域 ID

**`--acr-values` `^[^\x00-\x1F\x7F <>#"]*$`**

指定请求授权服务器在认证请求中使用的认证上下文类引用值。

**`--audiences` `^[^\x00-\x1F\x7F <>#"]*$`**

除了 <em>client-id</em> 之外，还接受 OpenID 签发者可能包含的受众列表。

**`--autocreate` `<boolean>` （<em>默认值 \=</em> `0`）**

如果用户不存在，则自动创建。

**`--base_dn` `<string>`**

LDAP 基础域名

**`--bind_dn` `<string>`**

LDAP 绑定域名

**`--capath` `<string>` （<em>默认值 \=</em> `/etc/ssl/certs`）**

CA 证书存储路径

**`--case-sensitive` `<boolean>` （<em>默认值 \=</em> `1`）**

用户名区分大小写

**`--cert` `<string>`**

客户端证书路径

**`--certkey` `<string>`**

客户端证书密钥路径

**`--check-connection` `<boolean>` （<em>默认值 \=</em> `0`）**

检查与服务器的绑定连接。

**`--client-id` `<string>`**

OpenID 客户端 ID

**`--client-key` `<string>`**

OpenID 客户端密钥

**`--comment` `<string>`**

描述。

**`--default` `<boolean>`**

将此认证域用作默认认证域

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--domain` `\S+`**

AD 域名

**`--filter` `<string>`**

用户同步的 LDAP 过滤器。

**`--group_classes` `<string>` （<em>默认值 \=</em> `groupOfNames, group, univentionGroup, ipausergroup`）**

组的对象类。

**`--group_dn` `<string>`**

组同步的 LDAP 基础域名。如果未设置，则使用 base\_dn。

**`--group_filter` `<string>`**

组同步的 LDAP 过滤器。

**`--group_name_attr` `<string>`**

表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。

**`--groups-autocreate` `<boolean>` （<em>默认值 \=</em> `0`）**

如果组不存在，则自动创建。

**`--groups-claim` `(?^:[A-Za-z0-9\.\-_]+)`**

用于获取组的 OpenID 声明。

**`--groups-overwrite` `<boolean>` （<em>默认值 \=</em> `0`）**

登录时覆盖该用户的所有组。

**`--issuer-url` `<string>`**

OpenID 签发者 URL

**`--mode` `<ldap | ldap+starttls | ldaps>` （<em>默认值 \=</em> `ldap`）**

LDAP 协议模式。

**`--password` `<string>`**

LDAP 绑定密码。将保存在 <em>/etc/pve/priv/realm/\<REALM\>.pw</em> 中。

**`--port` `<integer> (1 - 65535)`**

服务器端口。

**`--prompt` `(?:none|login|consent|select_account|\S+)`**

指定授权服务器是否提示最终用户重新认证并同意。

**`--query-userinfo` `<boolean>` （<em>默认值 \=</em> `1`）**

启用对 userinfo 端点的查询，以获取声明值。

**`--scopes` `<string>` （<em>默认值 \=</em> `email profile`）**

指定应授权并返回的作用域（用户详细信息），例如 <em>email</em> 或 <em>profile</em>。

**`--secure` `<boolean>`**

使用安全的 LDAPS 协议。已弃用：请改用 <em>mode</em>。

**`--server1` `<string>`**

服务器 IP 地址（或 DNS 名称）

**`--server2` `<string>`**

备用服务器 IP 地址（或 DNS 名称）

**`--sslversion` `<tlsv1 | tlsv1_1 | tlsv1_2 | tlsv1_3>`**

LDAPS TLS/SSL 版本。不建议使用低于 1.2 的版本！

**`--sync-defaults-options` `[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]`**

同步行为的默认选项。

**`--sync_attributes` `\w+=[^,]+(,\s*\w+=[^,]+)*`**

以逗号分隔的 key\=value 对列表，用于指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 <em>mail</em> 映射到 PVE 的 <em>email</em>，请写入 <em>email\=mail</em>。默认情况下，每个 PVE 用户字段都由同名 LDAP 属性表示。

**`--tfa` `type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]`**

使用双因素认证。

**`--user_attr` `\S{2,}`**

LDAP 用户属性名称

**`--user_classes` `<string>` （<em>默认值 \=</em> `inetorgperson, posixaccount, person, user`）**

用户的对象类。

**`--verify` `<boolean>` （<em>默认值 \=</em> `0`）**

验证服务器的 SSL 证书

### <strong>pveum realm sync</strong> `<realm>` `[OPTIONS]` <a href="#cli_pveum_realm_sync" id="cli_pveum_realm_sync"></a>

将用户和/或组从配置的 LDAP 同步到 user.cfg。注意：同步后的组将命名为 <em>name-$realm</em>，因此请确保这些组不存在，以免覆盖。

**`<realm>`: `<string>`**

认证域 ID

**`--dry-run` `<boolean>` （<em>默认值 \=</em> `0`）**

如果设置，则不写入任何内容。

**`--enable-new` `<boolean>` （<em>默认值 \=</em> `1`）**

立即启用新同步的用户。

**`--full` `<boolean>`**

已弃用：请改用 <em>remove-vanished</em>。如果设置，则以 LDAP 目录为准，删除同步未返回的用户或组，并移除同步用户所有在本地修改的属性。如果未设置，则仅同步已同步数据中存在的信息，不删除或修改其他任何内容。

**`--purge` `<boolean>`**

已弃用：请改用 <em>remove-vanished</em>。移除在同步期间从配置中移除的用户或组的 ACL。

**`--remove-vanished` `([acl];[properties];[entry])|none` （<em>默认值 \=</em> `none`）**

以分号分隔的列表，指定当相应项目或用户在同步中消失时要移除的内容。可用值如下：<em>entry</em> 在同步未返回用户/组时将其移除。<em>properties</em> 移除现有用户/组上已设置但源中不存在的属性（包括自定义属性）。<em>acl</em> 在同步未返回用户/组时移除 ACL。也可以不使用列表，而使用 <em>none</em>（默认值）。

**`--scope` `<both | groups | users>`**

选择要同步的内容。

### <strong>pveum role add</strong> `<roleid>` `[OPTIONS]` <a href="#cli_pveum_role_add" id="cli_pveum_role_add"></a>

创建新角色。

**`<roleid>`: `<string>`**

没有可用的说明

**`--privs` `<string>`**

没有可用的说明

### <strong>pveum role delete</strong> `<roleid>` <a href="#cli_pveum_role_delete" id="cli_pveum_role_delete"></a>

删除角色。

**`<roleid>`: `<string>`**

没有可用的说明

### <strong>pveum role list</strong> `[FORMAT_OPTIONS]` <a href="#cli_pveum_role_list" id="cli_pveum_role_list"></a>

角色索引。

### <strong>pveum role modify</strong> `<roleid>` `[OPTIONS]` <a href="#cli_pveum_role_modify" id="cli_pveum_role_modify"></a>

更新现有角色。

**`<roleid>`: `<string>`**

没有可用的说明

**`--append` `<boolean>`**

没有可用的说明

{% hint style="info" %}
需要选项：`privs`
{% endhint %}

**`--privs` `<string>`**

没有可用的说明

### <strong>pveum roleadd</strong> <a href="#cli_pveum_roleadd" id="cli_pveum_roleadd"></a>

<em>pveum role add</em> 的别名。

### <strong>pveum roledel</strong> <a href="#cli_pveum_roledel" id="cli_pveum_roledel"></a>

<em>pveum role delete</em> 的别名。

### <strong>pveum rolemod</strong> <a href="#cli_pveum_rolemod" id="cli_pveum_rolemod"></a>

<em>pveum role modify</em> 的别名。

### <strong>pveum ticket</strong> `<username>` `[OPTIONS]` <a href="#cli_pveum_ticket" id="cli_pveum_ticket"></a>

创建或验证认证票据。

**`<username>`: `<string>`**

用户名

**`--new-format` `<boolean>` （<em>默认值 \=</em> `1`）**

此参数现在会被忽略，并视为 1。

**`--otp` `<string>`**

双因素认证的一次性密码。

**`--path` `<string>`**

验证票据，并检查用户是否具有 <em>privs</em> 访问权限，路径为 <em>path</em>

{% hint style="info" %}
需要选项：`privs`
{% endhint %}

**`--privs` `<string>`**

验证票据，并检查用户是否具有 <em>privs</em> 访问权限，路径为 <em>path</em>

{% hint style="info" %}
需要选项：`path`
{% endhint %}

**`--realm` `<string>`**

可以选择通过此参数传入认证域。通常将认证域直接添加到用户名中：\<username\>@\<realm\>。

**`--tfa-challenge` `<string>`**

用户要响应的已签名 TFA 质询字符串。

### <strong>pveum user add</strong> `<userid>` `[OPTIONS]` <a href="#cli_pveum_user_add" id="cli_pveum_user_add"></a>

创建新用户。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--comment` `<string>`**

没有可用的说明

**`--email` `<string>`**

没有可用的说明

**`--enable` `<boolean>` （<em>默认值 \=</em> `1`）**

启用账户（默认）。可以将其设置为 <em>0</em> 以禁用账户

**`--expire` `<integer> (0 - N)`**

账户到期日期（自纪元以来的秒数）。<em>0</em> 表示没有到期日期。

**`--firstname` `<string>`**

没有可用的说明

**`--groups` `<string>`**

没有可用的说明

**`--keys` `[0-9a-zA-Z!=]{0,4096}`**

双因素认证的密钥（yubico）。

**`--lastname` `<string>`**

没有可用的说明

**`--password` `<string>`**

初始密码。

### <strong>pveum user delete</strong> `<userid>` <a href="#cli_pveum_user_delete" id="cli_pveum_user_delete"></a>

删除用户。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

### <strong>pveum user list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_list" id="cli_pveum_user_list"></a>

用户索引。

**`--enabled` `<boolean>`**

enable 属性的可选过滤器。

**`--full` `<boolean>` （<em>默认值 \=</em> `0`）**

包含组和令牌信息。

### <strong>pveum user modify</strong> `<userid>` `[OPTIONS]` <a href="#cli_pveum_user_modify" id="cli_pveum_user_modify"></a>

更新用户配置。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--append` `<boolean>`**

没有可用的说明

{% hint style="info" %}
需要选项：`groups`
{% endhint %}

**`--comment` `<string>`**

没有可用的说明

**`--email` `<string>`**

没有可用的说明

**`--enable` `<boolean>` （<em>默认值 \=</em> `1`）**

启用账户（默认）。可以将其设置为 <em>0</em> 以禁用账户

**`--expire` `<integer> (0 - N)`**

账户到期日期（自纪元以来的秒数）。<em>0</em> 表示没有到期日期。

**`--firstname` `<string>`**

没有可用的说明

**`--groups` `<string>`**

没有可用的说明

**`--keys` `[0-9a-zA-Z!=]{0,4096}`**

双因素认证的密钥（yubico）。

**`--lastname` `<string>`**

没有可用的说明

### <strong>pveum user permissions</strong> `[<userid>]` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_permissions" id="cli_pveum_user_permissions"></a>

获取给定用户/令牌的有效权限。

**`<userid>`: `(?^:^(?^:[^\s:/]+)\@(?^:[A-Za-z][A-Za-z0-9\.\-_]+)(?:!(?^:[A-Za-z][A-Za-z0-9\.\-_]+))?$)`**

用户 ID 或完整的 API 令牌 ID

**`--path` `<string>`**

仅转储此特定路径，而不是整棵树。

### <strong>pveum user tfa delete</strong> `<userid>` `[OPTIONS]` <a href="#cli_pveum_user_tfa_delete" id="cli_pveum_user_tfa_delete"></a>

删除用户的 TFA 条目。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--id` `<string>`**

TFA ID，如果未提供，则删除所有 TFA 条目。

### <strong>pveum user tfa list</strong> `[<userid>]` <a href="#cli_pveum_user_tfa_list" id="cli_pveum_user_tfa_list"></a>

列出 TFA 条目。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

### <strong>pveum user tfa unlock</strong> `<userid>` <a href="#cli_pveum_user_tfa_unlock" id="cli_pveum_user_tfa_unlock"></a>

解锁用户的 TFA 认证。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

### <strong>pveum user token add</strong> `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_add" id="cli_pveum_user_token_add"></a>

为特定用户生成新的 API 令牌。注意：返回的 API 令牌值需要保存，因为之后无法再次获取！

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

**`--comment` `<string>`**

没有可用的说明

**`--expire` `<integer> (0 - N)` （<em>默认值 \=</em> `same as user`）**

API 令牌到期日期（自纪元以来的秒数）。<em>0</em> 表示没有到期日期。

**`--privsep` `<boolean>` （<em>默认值 \=</em> `1`）**

使用单独的 ACL 限制 API 令牌权限（默认），或赋予对应用户的全部权限。

### <strong>pveum user token delete</strong> `<userid> <tokenid>` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_delete" id="cli_pveum_user_token_delete"></a>

移除特定用户的 API 令牌。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

### <strong>pveum user token list</strong> `<userid>` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_list" id="cli_pveum_user_token_list"></a>

获取用户 API 令牌。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

### <strong>pveum user token modify</strong> `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_modify" id="cli_pveum_user_token_modify"></a>

更新特定用户的 API 令牌。注意：设置 <em>regenerate</em> 后，返回的令牌值需要保存，因为之后无法再次获取！

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

**`--comment` `<string>`**

没有可用的说明

**`--delete` `<string>`**

要删除的设置列表。

**`--expire` `<integer> (0 - N)` （<em>默认值 \=</em> `same as user`）**

API 令牌到期日期（自纪元以来的秒数）。<em>0</em> 表示没有到期日期。

**`--privsep` `<boolean>` （<em>默认值 \=</em> `1`）**

使用单独的 ACL 限制 API 令牌权限（默认），或赋予对应用户的全部权限。

**`--regenerate` `<boolean>` （<em>默认值 \=</em> `0`）**

重新生成令牌的秘密值。此操作之后，所有使用旧秘密值的用户都将失去访问权限。

### <strong>pveum user token permissions</strong> `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_permissions" id="cli_pveum_user_token_permissions"></a>

获取给定令牌的有效权限。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

**`--path` `<string>`**

仅转储此特定路径，而不是整棵树。

### <strong>pveum user token remove</strong> <a href="#cli_pveum_user_token_remove" id="cli_pveum_user_token_remove"></a>

<em>pveum user token delete</em> 的别名。

### <strong>pveum useradd</strong> <a href="#cli_pveum_useradd" id="cli_pveum_useradd"></a>

<em>pveum user add</em> 的别名。

### <strong>pveum userdel</strong> <a href="#cli_pveum_userdel" id="cli_pveum_userdel"></a>

<em>pveum user delete</em> 的别名。

### <strong>pveum usermod</strong> <a href="#cli_pveum_usermod" id="cli_pveum_usermod"></a>

<em>pveum user modify</em> 的别名。

## 22.16. <strong>vzdump</strong> \- 虚拟机和容器备份工具 <a href="#strong_vzdump_strong_backup_utility_for_vms_and_containers" id="strong_vzdump_strong_backup_utility_for_vms_and_containers"></a>

### <strong>vzdump</strong> `help` <a href="#cli_vzdump_help" id="cli_vzdump_help"></a>

### <strong>vzdump</strong> `{<vmid>}` `[OPTIONS]` <a href="#cli_vzdump" id="cli_vzdump"></a>

创建备份。

**`<vmid>`: `<string>`**

要备份的客户机系统 ID。

**`--all` `<boolean>` （<em>默认值 \=</em> `0`）**

备份此宿主机上所有已知的客户机系统。

**`--bwlimit` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

限制 I/O 带宽（KiB/s）。

**`--compress` `<0 | 1 | gzip | lzo | zstd>` （<em>默认值 \=</em> `0`）**

压缩转储文件。

**`--dumpdir` `<string>`**

将生成的文件存储到指定目录。

**`--exclude` `<string>`**

排除指定客户机系统（假定为 --all）

**`--exclude-path` `<array>`**

排除某些文件/目录（shell 通配模式）。以 <em>/</em> 开头的路径以容器根目录为锚点，其他路径相对于每个子目录匹配。

**`--fleecing` `[[enabled=]<1|0>] [,storage=<storage ID>]`**

备份 fleecing 的选项（仅限虚拟机）。

**`--ionice` `<integer> (0 - 8)` （<em>默认值 \=</em> `7`）**

使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，这仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用尽力而为优先级及指定值。

**`--job-id` `\S+`**

备份任务的 ID。如果设置，备份通知的 <em>backup-job</em> 元数据字段将设置为此值。只有 [root@pam](mailto:root@pam) 可以设置此参数。

**`--lockwait` `<integer> (0 - N)` （<em>默认值 \=</em> `180`）**

等待全局锁的最长时间（分钟）。

**`--mailnotification` `<always | failure>` （<em>默认值 \=</em> `always`）**

已弃用：请改用通知目标/匹配器。指定何时发送通知邮件

**`--mailto` `<string>`**

已弃用：请改用通知目标/匹配器。应接收电子邮件通知的电子邮件地址或用户的逗号分隔列表。

**`--mode` `<snapshot | stop | suspend>` （<em>默认值 \=</em> `snapshot`）**

备份模式。

**`--node` `<string>`**

仅在此节点上执行时运行。

**`--notes-template` `<string>`**

用于生成备份备注的模板字符串。可包含变量，这些变量会被替换为其值。目前支持 {\\{\\cluster}}、{\\{\\guestname}}、{\\{\\node}} 和 {\\{\\vmid}}，未来可能添加更多。必须为单行，换行和反斜杠分别需要转义为 <em>\\n</em> 和 <em>\\\\</em>。

{% hint style="info" %}
需要选项：`storage`
{% endhint %}

**`--notification-mode` `<auto | legacy-sendmail | notification-system>` （<em>默认值 \=</em> `auto`）**

确定要使用的通知系统。如果设为 <em>legacy-sendmail</em>，vzdump 会考虑 mailto/mailnotification 参数，并通过 <em>sendmail</em> 命令向指定地址发送电子邮件。如果设为 <em>notification-system</em>，则通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 <em>auto</em>（默认设置），在设置了 mailto 时会发送电子邮件，否则使用通知系统。

**`--pbs-change-detection-mode` `<data | legacy | metadata>`**

用于检测文件更改并切换容器备份编码格式的 PBS 模式。

**`--performance` `[max-workers=<integer>] [,pbs-entries-max=<integer>]`**

其他性能相关设置。

**`--pigz` `<integer>` （<em>默认值 \=</em> `0`）**

N\>0 时使用 pigz 代替 gzip。N\=1 使用一半核心，N\>1 使用 N 作为线程数。

**`--pool` `<string>`**

备份指定池中包含的所有已知客户机系统。

**`--protected` `<boolean>`**

如果为 true，将备份标记为受保护。

{% hint style="info" %}
需要选项：`storage`
{% endhint %}

**`--prune-backups` `[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]` （<em>默认值 \=</em> `keep-all=1`）**

使用这些保留选项，替代存储配置中的保留选项。

**`--quiet` `<boolean>` （<em>默认值 \=</em> `0`）**

静默运行。

**`--remove` `<boolean>` （<em>默认值 \=</em> `1`）**

根据 <em>prune-backups</em> 清理较旧的备份。

**`--script` `<string>`**

使用指定的钩子脚本。

**`--stdexcludes` `<boolean>` （<em>默认值 \=</em> `1`）**

排除临时文件和日志。

**`--stdout` `<boolean>`**

将 tar 写入 stdout，而不是文件。

**`--stop` `<boolean>` （<em>默认值 \=</em> `0`）**

停止此宿主机上正在运行的备份任务。

**`--stopwait` `<integer> (0 - N)` （<em>默认值 \=</em> `10`）**

等待客户机系统停止的最长时间（分钟）。

**`--storage` `<storage ID>`**

将生成的文件保存到此存储。

**`--tmpdir` `<string>`**

将临时文件保存到指定目录。

**`--zstd` `<integer>` （<em>默认值 \=</em> `1`）**

Zstd 线程数。N\=0 使用可用核心的一半；如果 N 设置为大于 0 的值，则使用 N 作为线程数。

## 22.17. <strong>ha-manager</strong> \- Proxmox VE HA 管理器 <a href="#strong_ha_manager_strong_proxmox_ve_ha_manager" id="strong_ha_manager_strong_proxmox_ve_ha_manager"></a>

### <strong>ha-manager</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_ha-manager" id="cli_ha-manager"></a>

### <strong>ha-manager add</strong> `<sid>` `[OPTIONS]` <a href="#cli_ha-manager_add" id="cli_ha-manager_add"></a>

创建新的 HA 资源。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`--auto-rebalance` `<boolean>` (<em>默认 \=</em> `1`)**

自动重新平衡期间可以迁移 HA 资源

**`--comment` `<string>`**

描述。

**`--failback` `<boolean>` (<em>默认 \=</em> `1`)**

如果优先级高于当前节点的节点上线，则根据其节点亲和性规则，自动将 HA 资源迁移到优先级最高的节点。

**`--group` `<string>`**

HA 组标识符。

**`--max_relocate` `<integer> (0 - N)` (<em>默认 \=</em> `1`)**

资源启动失败时，尝试重定位资源的最大次数。

**`--max_restart` `<integer> (0 - N)` (<em>默认 \=</em> `1`)**

资源启动失败后，在节点上重启该资源的最大尝试次数。达到该次数后，HA 管理器将尝试把资源重定位到符合条件的节点。

**`--state` `<disabled | enabled | ignored | started | stopped>` (<em>默认 \=</em> `started`)**

请求的资源状态。

**`--type` `<ct | vm>`**

资源类型。

### <strong>ha-manager config</strong> `[OPTIONS]` <a href="#cli_ha-manager_config" id="cli_ha-manager_config"></a>

列出 HA 资源。

**`--type` `<ct | vm>`**

仅列出特定类型的资源

### <strong>ha-manager crm-command arm-ha</strong> <a href="#cli_ha-manager_crm-command_arm-ha" id="cli_ha-manager_crm-command_arm-ha"></a>

请求在 HA 堆栈解除布防后重新布防。

### <strong>ha-manager crm-command disarm-ha</strong> `<resource-mode>` <a href="#cli_ha-manager_crm-command_disarm-ha" id="cli_ha-manager_crm-command_disarm-ha"></a>

请求解除 HA 堆栈的布防，并释放整个集群范围内的所有看门狗。

**`<resource-mode>`: `<freeze | ignore>`**

控制解除布防期间如何处理 HA 管理的资源。资源的当前状态不受影响。<em>freeze</em>：不应用新命令和状态更改。<em>ignore</em>：从 HA 跟踪中移除资源，并可将其当作非 HA 管理的资源进行管理。

### <strong>ha-manager crm-command migrate</strong> `<sid> <node>` <a href="#cli_ha-manager_crm-command_migrate" id="cli_ha-manager_crm-command_migrate"></a>

请求将资源在线迁移到另一个节点。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`<node>`: `<string>`**

目标节点。

### <strong>ha-manager crm-command node-maintenance disable</strong> `<node>` <a href="#cli_ha-manager_crm-command_node-maintenance_disable" id="cli_ha-manager_crm-command_node-maintenance_disable"></a>

更改 node-maintenance 请求状态。

**`<node>`: `<string>`**

集群节点名称。

### <strong>ha-manager crm-command node-maintenance enable</strong> `<node>` <a href="#cli_ha-manager_crm-command_node-maintenance_enable" id="cli_ha-manager_crm-command_node-maintenance_enable"></a>

更改 node-maintenance 请求状态。

**`<node>`: `<string>`**

集群节点名称。

### <strong>ha-manager crm-command relocate</strong> `<sid> <node>` <a href="#cli_ha-manager_crm-command_relocate" id="cli_ha-manager_crm-command_relocate"></a>

请求将资源重定位到另一个节点。这会停止旧节点上的服务，并在目标节点上重新启动该服务。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`<node>`: `<string>`**

目标节点。

### <strong>ha-manager crm-command stop</strong> `<sid> <timeout>` <a href="#cli_ha-manager_crm-command_stop" id="cli_ha-manager_crm-command_stop"></a>

请求停止服务。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`<timeout>`: `<integer> (0 - N)`**

超时时间（秒）。如果设置为 0，将执行强制停止。

### <strong>ha-manager groupadd</strong> `<group> --nodes <string>` `[OPTIONS]` <a href="#cli_ha-manager_groupadd" id="cli_ha-manager_groupadd"></a>

创建新的 HA 组。（已弃用，建议使用 HA 规则）

**`<group>`: `<string>`**

HA 组标识符。

**`--comment` `<string>`**

描述。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--nofailback` `<boolean>` (<em>默认 \=</em> `0`)**

CRM 会尝试在优先级最高的节点上运行服务。如果优先级更高的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。

**`--restricted` `<boolean>` (<em>默认 \=</em> `0`)**

绑定到受限组的资源只能在该组定义的节点上运行。

**`--type` `<group>`**

组类型。

### <strong>ha-manager groupconfig</strong> <a href="#cli_ha-manager_groupconfig" id="cli_ha-manager_groupconfig"></a>

获取 HA 组。（已弃用，建议使用 HA 规则）

### <strong>ha-manager groupremove</strong> `<group>` <a href="#cli_ha-manager_groupremove" id="cli_ha-manager_groupremove"></a>

删除 HA 组配置。（已弃用，建议使用 HA 规则）

**`<group>`: `<string>`**

HA 组标识符。

### <strong>ha-manager groupset</strong> `<group>` `[OPTIONS]` <a href="#cli_ha-manager_groupset" id="cli_ha-manager_groupset"></a>

更新 HA 组配置。（已弃用，建议使用 HA 规则）

**`<group>`: `<string>`**

HA 组标识符。

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--nofailback` `<boolean>` (<em>默认 \=</em> `0`)**

CRM 会尝试在优先级最高的节点上运行服务。如果优先级更高的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。

**`--restricted` `<boolean>` (<em>默认 \=</em> `0`)**

绑定到受限组的资源只能在该组定义的节点上运行。

### <strong>ha-manager help</strong> `[OPTIONS]` <a href="#cli_ha-manager_help" id="cli_ha-manager_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>ha-manager migrate</strong> <a href="#cli_ha-manager_migrate" id="cli_ha-manager_migrate"></a>

<em>ha-manager crm-command migrate</em> 的别名。

### <strong>ha-manager relocate</strong> <a href="#cli_ha-manager_relocate" id="cli_ha-manager_relocate"></a>

<em>ha-manager crm-command relocate</em> 的别名。

### <strong>ha-manager remove</strong> `<sid>` `[OPTIONS]` <a href="#cli_ha-manager_remove" id="cli_ha-manager_remove"></a>

删除资源配置。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`--purge` `<boolean>` (<em>默认 \=</em> `1`)**

从引用此资源的规则中移除此资源；如果此资源是规则中的唯一资源，则删除该规则

### <strong>ha-manager rules add</strong> `<type> <rule>` `[OPTIONS]` <a href="#cli_ha-manager_rules_add" id="cli_ha-manager_rules_add"></a>

创建 HA 规则。

**`<type>`: `<node-affinity | resource-affinity>`**

HA 规则类型。

**`<rule>`: `<string>`**

HA 规则标识符。

`Conditional options:`

**`[type=node-affinity]`**

**`--affinity` `<negative | positive>` (<em>默认 \=</em> `positive`)**

描述 HA 资源应放置在指定节点上（<em>positive</em>），还是应放置在指定节点以外的任何节点上（<em>negative</em>）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

**`--strict` `<boolean>` (<em>默认 \=</em> `0`)**

描述节点亲和性规则是严格的还是非严格的。

**`[type=resource-affinity]`**

**`--affinity` `<negative | positive>`**

描述 HA 资源是否应保留在同一节点上（<em>positive</em>），还是应保留在不同节点上（<em>negative</em>）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

### <strong>ha-manager rules config</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_ha-manager_rules_config" id="cli_ha-manager_rules_config"></a>

获取 HA 规则。

**`--resource` `<string>`**

将返回的列表限制为影响指定资源的规则。

**`--type` `<node-affinity | resource-affinity>`**

将返回的列表限制为指定的规则类型。

### <strong>ha-manager rules list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_ha-manager_rules_list" id="cli_ha-manager_rules_list"></a>

获取 HA 规则。

**`--resource` `<string>`**

将返回的列表限制为影响指定资源的规则。

**`--type` `<node-affinity | resource-affinity>`**

将返回的列表限制为指定的规则类型。

### <strong>ha-manager rules remove</strong> `<rule>` <a href="#cli_ha-manager_rules_remove" id="cli_ha-manager_rules_remove"></a>

删除 HA 规则。

**`<rule>`: `<string>`**

HA 规则标识符。

### <strong>ha-manager rules set</strong> `<type> <rule>` `[OPTIONS]` <a href="#cli_ha-manager_rules_set" id="cli_ha-manager_rules_set"></a>

更新 HA 规则。

**`<type>`: `<node-affinity | resource-affinity>`**

HA 规则类型。

**`<rule>`: `<string>`**

HA 规则标识符。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

`Conditional options:`

**`[type=node-affinity]`**

**`--affinity` `<negative | positive>` (<em>默认 \=</em> `positive`)**

描述 HA 资源应放置在指定节点上（<em>positive</em>），还是应放置在指定节点以外的任何节点上（<em>negative</em>）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

**`--strict` `<boolean>` (<em>默认 \=</em> `0`)**

描述节点亲和性规则是严格的还是非严格的。

**`[type=resource-affinity]`**

**`--affinity` `<negative | positive>`**

描述 HA 资源是否应保留在同一节点上（<em>positive</em>），还是应保留在不同节点上（<em>negative</em>）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

### <strong>ha-manager set</strong> `<sid>` `[OPTIONS]` <a href="#cli_ha-manager_set" id="cli_ha-manager_set"></a>

更新资源配置。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`--auto-rebalance` `<boolean>` (<em>默认 \=</em> `1`)**

自动重新平衡期间可以迁移 HA 资源

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--failback` `<boolean>` (<em>默认 \=</em> `1`)**

如果优先级高于当前节点的节点上线，则根据其节点亲和性规则，自动将 HA 资源迁移到优先级最高的节点。

**`--group` `<string>`**

HA 组标识符。

**`--max_relocate` `<integer> (0 - N)` (<em>默认 \=</em> `1`)**

资源启动失败时，尝试重定位资源的最大次数。

**`--max_restart` `<integer> (0 - N)` (<em>默认 \=</em> `1`)**

资源启动失败后，在节点上重启该资源的最大尝试次数。达到该次数后，HA 管理器将尝试把资源重定位到符合条件的节点。

**`--state` `<disabled | enabled | ignored | started | stopped>` (<em>默认 \=</em> `started`)**

请求的资源状态。

### <strong>ha-manager status</strong> `[OPTIONS]` <a href="#cli_ha-manager_status" id="cli_ha-manager_status"></a>

显示 HA 管理器状态。

**`--verbose` `<boolean>`（<em>默认值 \=</em> `0`）**

详细输出。包含完整的 CRM 和 LRM 状态（JSON）。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
