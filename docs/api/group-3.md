# storage API

本章包含此资源组的全部接口，按路径和 HTTP 方法在同一页展开。接口路径、方法、参数、类型、约束和默认值保持原值。

## `/storage` <a href="#api-storage-3718024f" id="api-storage-3718024f"></a>

原始接口路径：`/storage`。

### GET `/storage` <a href="#api-storage-3718024f-get" id="api-storage-3718024f-get"></a>

存储索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/storage/<storage>' 具有 'Datastore.Audit' 或 'Datastore.AllocateSpace' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-storage-3718024f-get-parameters" id="api-storage-3718024f-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的存储；可选值：`btrfs`, `cephfs`, `cifs`, `dir`, `esxi`, `iscsi`, `iscsidirect`, `lvm`, `lvmthin`, `nfs`, `pbs`, `rbd`, `zfs`, `zfspool` |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"type": {"description": "仅列出特定类型的存储", "enum": ["btrfs", "cephfs", "cifs", "dir", "esxi", "iscsi", "iscsidirect", "lvm", "lvmthin", "nfs", "pbs", "rbd", "zfs", "zfspool"], "optional": 1, "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-storage-3718024f-get-returns" id="api-storage-3718024f-get-returns"></a>

```text
{"items": {"properties": {"storage": {"type": "string"}}, "type": "object"}, "links": [{"href": "{storage}", "rel": "child"}], "type": "array"}
```

### POST `/storage` <a href="#api-storage-3718024f-post" id="api-storage-3718024f-post"></a>

创建新存储。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/storage", ["Datastore.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-storage-3718024f-post-parameters" id="api-storage-3718024f-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `authsupported` | 类型：string；必填：否；默认值：—<br>Authsupported。 |
| `base` | 类型：string；必填：否；默认值：—<br>基础卷。此卷会自动激活。 |
| `blocksize` | 类型：string；必填：否；默认值：—<br>ZFS 块大小 |
| `bwlimit` | 类型：string；必填：否；默认值：—<br>为各类操作设置 I/O 带宽限制（单位为 KiB/s）。 |
| `comstar_hg` | 类型：string；必填：否；默认值：—<br>comstar 视图的主机组 |
| `comstar_tg` | 类型：string；必填：否；默认值：—<br>comstar 视图的目标组 |
| `content` | 类型：string；必填：否；默认值：—<br>允许的内容类型。<br><br>注意：值 'rootdir' 用于容器，值 'images' 用于虚拟机。<br> |
| `content-dirs` | 类型：string；必填：否；默认值：—<br>覆盖默认内容类型目录。 |
| `create-base-path` | 类型：boolean；必填：否；默认值："yes"<br>如果基础目录不存在，则创建。 |
| `create-subdirs` | 类型：boolean；必填：否；默认值："yes"<br>使用默认结构填充目录。 |
| `data-pool` | 类型：string；必填：否；默认值：—<br>数据池（仅用于纠删码） |
| `datastore` | 类型：string；必填：否；默认值：—<br>Proxmox Backup Server 数据存储名称。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用存储的标志。 |
| `domain` | 类型：string；必填：否；默认值：—<br>CIFS 域。 |
| `encryption-key` | 类型：string；必填：否；默认值：—<br>加密密钥。使用 'autogen' 自动生成不带口令的密钥。 |
| `export` | 类型：string；必填：否；默认值：—<br>NFS 导出路径。 |
| `fingerprint` | 类型：string；必填：否；默认值：—<br>证书 SHA 256 指纹。 |
| `format` | 类型：string；必填：否；默认值：—<br>默认镜像格式。；可选值：`raw`, `qcow2`, `subvol`, `vmdk` |
| `fs-name` | 类型：string；必填：否；默认值：—<br>Ceph 文件系统名称。 |
| `fuse` | 类型：boolean；必填：否；默认值：—<br>通过 FUSE 挂载 CephFS。 |
| `is_mountpoint` | 类型：string；必填：否；默认值："no"<br>将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是将目标路径填入此字段的简写方式。 |
| `iscsiprovider` | 类型：string；必填：否；默认值：—<br>iSCSI 提供程序 |
| `keyring` | 类型：string；必填：否；默认值：—<br>客户端密钥环内容（用于外部集群）。 |
| `krbd` | 类型：boolean；必填：否；默认值：0<br>始终通过 krbd 内核模块访问 RBD。 |
| `lio_tpg` | 类型：string；必填：否；默认值：—<br>Linux LIO 目标的目标门户组 |
| `master-pubkey` | 类型：string；必填：否；默认值：—<br>Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。 |
| `max-protected-backups` | 类型：integer；必填：否；默认值："Unlimited for users with Datastore.Allocate privilege, 5 for other users"<br>每个客户机的最大受保护备份数。使用 '-1' 表示无限制。 |
| `mkdir` | 类型：boolean；必填：否；默认值："yes"<br>如果目录不存在，则创建并填充默认子目录。注意：已弃用，请改用 'create-base-path' 和 'create-subdirs' 选项。 |
| `monhost` | 类型：string；必填：否；默认值：—<br>监视器的 IP 地址（用于外部集群）。 |
| `mountpoint` | 类型：string；必填：否；默认值：—<br>挂载点 |
| `namespace` | 类型：string；必填：否；默认值：—<br>命名空间。 |
| `nocow` | 类型：boolean；必填：否；默认值：0<br>为文件设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。仅当数据安全性要求不高于未使用底层 RAID 系统的单个 ext4 格式磁盘时，才使用此选项。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>存储配置适用的节点列表。 |
| `nowritecache` | 类型：boolean；必填：否；默认值：—<br>禁用目标上的写缓存 |
| `options` | 类型：string；必填：否；默认值：—<br>NFS/CIFS 挂载选项（参见 'man nfs' 或 'man mount.cifs'） |
| `password` | 类型：string；必填：否；默认值：—<br>访问共享/数据存储的密码。 |
| `path` | 类型：string；必填：否；默认值：—<br>文件系统路径。 |
| `pool` | 类型：string；必填：否；默认值：—<br>池。 |
| `port` | 类型：integer；必填：否；默认值：—<br>使用此端口代替默认端口连接存储（例如 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 'options' 选项通过挂载选项配置端口。 |
| `portal` | 类型：string；必填：否；默认值：—<br>iSCSI 门户（IP 或 DNS 名称，可带端口）。 |
| `preallocation` | 类型：string；必填：否；默认值："metadata"<br>raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 'metadata' 将产生 preallocation=off 的效果。；可选值：`off`, `metadata`, `falloc`, `full` |
| `prune-backups` | 类型：string；必填：否；默认值：—<br>优先处理时间间隔较短的保留选项，其中 --keep-last 最先处理。每个选项覆盖特定时间段。我们称此时间段内的备份被此选项覆盖。下一个选项不会处理已被覆盖的备份，只考虑更旧的备份。 |
| `saferemove` | 类型：boolean；必填：否；默认值：—<br>移除逻辑卷时将数据清零。 |
| `saferemove-stepsize` | 类型：integer；必填：否；默认值：32<br>擦除步长，单位为 MiB。上限为存储支持的最大值。；可选值：`1`, `2`, `4`, `8`, `16`, `32` |
| `saferemove_throughput` | 类型：string；必填：否；默认值：—<br>擦除吞吐量（cstream -t 参数值）。 |
| `server` | 类型：string；必填：否；默认值：—<br>服务器 IP 或 DNS 名称。 |
| `share` | 类型：string；必填：否；默认值：—<br>CIFS 共享。 |
| `shared` | 类型：boolean；必填：否；默认值：—<br>表明这是在所有节点（或 'nodes' 选项列出的所有节点）上具有相同内容的单一存储。此项不会使其他节点自动访问本地存储内容，只是将已经共享的存储标记为共享！ |
| `skip-cert-verification` | 类型：boolean；必填：否；默认值："false"<br>禁用 TLS 证书验证，仅在完全可信的网络中启用！ |
| `smbversion` | 类型：string；必填：否；默认值："default"<br>SMB 协议版本。未设置时为 'default'，协商客户端与服务器共同支持的最高 SMB2+ 版本。；可选值：`default`, `2.0`, `2.1`, `3`, `3.0`, `3.11` |
| `snapshot-as-volume-chain` | 类型：boolean；必填：否；默认值：0<br>启用通过卷后端链创建与存储供应商无关的快照的支持。 |
| `sparse` | 类型：boolean；必填：否；默认值：—<br>使用稀疏卷 |
| `storage` | 类型：string；必填：是；默认值：—<br>存储标识符。 |
| `subdir` | 类型：string；必填：否；默认值：—<br>要挂载的子目录。 |
| `tagged_only` | 类型：boolean；必填：否；默认值：—<br>仅列出带有 'pve-vm-ID' 标签的逻辑卷。 |
| `target` | 类型：string；必填：否；默认值：—<br>iSCSI 目标。 |
| `thinpool` | 类型：string；必填：否；默认值：—<br>LVM 精简池逻辑卷名称。 |
| `type` | 类型：string；必填：是；默认值：—<br>存储类型。；可选值：`btrfs`, `cephfs`, `cifs`, `dir`, `esxi`, `iscsi`, `iscsidirect`, `lvm`, `lvmthin`, `nfs`, `pbs`, `rbd`, `zfs`, `zfspool` |
| `username` | 类型：string；必填：否；默认值：—<br>RBD ID。 |
| `vgname` | 类型：string；必填：否；默认值：—<br>卷组名称。 |
| `zfs-base-path` | 类型：string；必填：否；默认值：—<br>查找创建的 ZFS 块设备的基础路径。如果未指定，则在创建时自动设置。通常为 '/dev/zvol'。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "authsupported": {"description": "Authsupported。", "optional": 1, "type": "string", "typetext": "<string>"}, "base": {"description": "基础卷。此卷会自动激活。", "format": "pve-volume-id", "optional": 1, "type": "string", "typetext": "<string>"},
    "blocksize": {"description": "ZFS 块大小", "format": "pve-storage-zfs-blocksize", "format_description": "a power of 2 with optional k or m suffix", "optional": 1, "type": "string", "typetext": "<a power of 2 with optional k or m suffix>"},
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {"description": "克隆磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}, "default": {"description": "默认带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "migration": {"description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}, "move": {"description": "移动磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "restore": {"description": "从备份还原客户机的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}
      },
      "optional": 1, "type": "string", "typetext": "[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]"
    },
    "comstar_hg": {"description": "comstar 视图的主机组", "optional": 1, "type": "string", "typetext": "<string>"}, "comstar_tg": {"description": "comstar 视图的目标组", "optional": 1, "type": "string", "typetext": "<string>"},
    "content": {"description": "允许的内容类型。\n\n注意：值 'rootdir' 用于容器，值 'images' 用于虚拟机。\n", "format": "pve-storage-content-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "content-dirs": {"description": "覆盖默认内容类型目录。", "format": "pve-dir-override-list", "optional": 1, "type": "string", "typetext": "<string>"}, "create-base-path": {"default": "yes", "description": "如果基础目录不存在，则创建。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "create-subdirs": {"default": "yes", "description": "使用默认结构填充目录。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "data-pool": {"description": "数据池（仅用于纠删码）", "optional": 1, "type": "string", "typetext": "<string>"},
    "datastore": {"description": "Proxmox Backup Server 数据存储名称。", "optional": 1, "type": "string", "typetext": "<string>"}, "disable": {"description": "用于禁用存储的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "domain": {"description": "CIFS 域。", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "encryption-key": {"description": "加密密钥。使用 'autogen' 自动生成不带口令的密钥。", "optional": 1, "type": "string", "typetext": "<string>"},
    "export": {"description": "NFS 导出路径。", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"}, "fingerprint": {"description": "证书 SHA 256 指纹。", "optional": 1, "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
    "format": {"description": "默认镜像格式。", "enum": ["raw", "qcow2", "subvol", "vmdk"], "optional": 1, "type": "string"}, "fs-name": {"description": "Ceph 文件系统名称。", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"},
    "fuse": {"description": "通过 FUSE 挂载 CephFS。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "is_mountpoint": {"default": "no", "description": "将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是将目标路径填入此字段的简写方式。", "optional": 1, "type": "string", "typetext": "<string>"},
    "iscsiprovider": {"description": "iSCSI 提供程序", "optional": 1, "type": "string", "typetext": "<string>"}, "keyring": {"description": "客户端密钥环内容（用于外部集群）。", "optional": 1, "type": "string", "typetext": "<string>"},
    "krbd": {"default": 0, "description": "始终通过 krbd 内核模块访问 RBD。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "lio_tpg": {"description": "Linux LIO 目标的目标门户组", "optional": 1, "type": "string", "typetext": "<string>"},
    "master-pubkey": {"description": "Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。", "optional": 1, "type": "string", "typetext": "<string>"},
    "max-protected-backups": {"default": "Unlimited for users with Datastore.Allocate privilege, 5 for other users", "description": "每个客户机的最大受保护备份数。使用 '-1' 表示无限制。", "minimum": -1, "optional": 1, "type": "integer", "typetext": "<integer> (-1 - N)"},
    "mkdir": {"default": "yes", "description": "如果目录不存在，则创建并填充默认子目录。注意：已弃用，请改用 'create-base-path' 和 'create-subdirs' 选项。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "monhost": {"description": "监视器的 IP 地址（用于外部集群）。", "format": "pve-storage-portal-dns-list", "optional": 1, "type": "string", "typetext": "<string>"}, "mountpoint": {"description": "挂载点", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"},
    "namespace": {"description": "命名空间。", "optional": 1, "type": "string", "typetext": "<string>"},
    "nocow": {"default": 0, "description": "为文件设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。仅当数据安全性要求不高于未使用底层 RAID 系统的单个 ext4 格式磁盘时，才使用此选项。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "nodes": {"description": "存储配置适用的节点列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"}, "nowritecache": {"description": "禁用目标上的写缓存", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "options": {"description": "NFS/CIFS 挂载选项（参见 'man nfs' 或 'man mount.cifs'）", "format": "pve-storage-options", "optional": 1, "type": "string", "typetext": "<string>"}, "password": {"description": "访问共享/数据存储的密码。", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "path": {"description": "文件系统路径。", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"}, "pool": {"description": "池。", "optional": 1, "type": "string", "typetext": "<string>"},
    "port": {"description": "使用此端口代替默认端口连接存储（例如 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 'options' 选项通过挂载选项配置端口。", "maximum": 65535, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 65535)"},
    "portal": {"description": "iSCSI 门户（IP 或 DNS 名称，可带端口）。", "format": "pve-storage-portal-dns", "optional": 1, "type": "string", "typetext": "<string>"},
    "preallocation": {"default": "metadata", "description": "raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 'metadata' 将产生 preallocation=off 的效果。", "enum": ["off", "metadata", "falloc", "full"], "optional": 1, "type": "string"},
    "prune-backups": {
      "description": "优先处理时间间隔较短的保留选项，其中 --keep-last 最先处理。每个选项覆盖特定时间段。我们称此时间段内的备份被此选项覆盖。下一个选项不会处理已被覆盖的备份，只考虑更旧的备份。", "format": "prune-backups", "optional": 1, "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "saferemove": {"description": "移除逻辑卷时将数据清零。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "saferemove-stepsize": {"default": 32, "description": "擦除步长，单位为 MiB。上限为存储支持的最大值。", "enum": ["1", "2", "4", "8", "16", "32"], "optional": 1, "type": "integer"},
    "saferemove_throughput": {"description": "擦除吞吐量（cstream -t 参数值）。", "optional": 1, "type": "string", "typetext": "<string>"}, "server": {"description": "服务器 IP 或 DNS 名称。", "format": "pve-storage-server", "optional": 1, "type": "string", "typetext": "<string>"},
    "share": {"description": "CIFS 共享。", "optional": 1, "type": "string", "typetext": "<string>"},
    "shared": {"description": "表明这是在所有节点（或 'nodes' 选项列出的所有节点）上具有相同内容的单一存储。此项不会使其他节点自动访问本地存储内容，只是将已经共享的存储标记为共享！", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "skip-cert-verification": {"default": "false", "description": "禁用 TLS 证书验证，仅在完全可信的网络中启用！", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "smbversion": {"default": "default", "description": "SMB 协议版本。未设置时为 'default'，协商客户端与服务器共同支持的最高 SMB2+ 版本。", "enum": ["default", "2.0", "2.1", "3", "3.0", "3.11"], "optional": 1, "type": "string"},
    "snapshot-as-volume-chain": {"default": 0, "description": "启用通过卷后端链创建与存储供应商无关的快照的支持。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "sparse": {"description": "使用稀疏卷", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "storage": {"description": "存储标识符。", "format": "pve-storage-id", "format_description": "storage ID", "type": "string", "typetext": "<storage ID>"}, "subdir": {"description": "要挂载的子目录。", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"},
    "tagged_only": {"description": "仅列出带有 'pve-vm-ID' 标签的逻辑卷。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "target": {"description": "iSCSI 目标。", "optional": 1, "type": "string", "typetext": "<string>"},
    "thinpool": {"description": "LVM 精简池逻辑卷名称。", "format": "pve-storage-vgname", "optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"description": "存储类型。", "enum": ["btrfs", "cephfs", "cifs", "dir", "esxi", "iscsi", "iscsidirect", "lvm", "lvmthin", "nfs", "pbs", "rbd", "zfs", "zfspool"], "type": "string"}, "username": {"description": "RBD ID。", "optional": 1, "type": "string", "typetext": "<string>"},
    "vgname": {"description": "卷组名称。", "format": "pve-storage-vgname", "optional": 1, "type": "string", "typetext": "<string>"},
    "zfs-base-path": {"description": "查找创建的 ZFS 块设备的基础路径。如果未指定，则在创建时自动设置。通常为 '/dev/zvol'。", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-storage-3718024f-post-returns" id="api-storage-3718024f-post-returns"></a>

```text
{
  "properties": {
    "config": {"additionalProperties": 1, "description": "部分配置属性，可能由服务器生成。", "optional": 1, "properties": {"encryption-key": {"description": "加密密钥，可能为自动生成。", "optional": 1, "type": "string"}}, "type": "object"}, "storage": {"description": "所创建存储的 ID。", "type": "string"},
    "type": {"description": "所创建存储的类型。", "enum": ["btrfs", "cephfs", "cifs", "dir", "esxi", "iscsi", "iscsidirect", "lvm", "lvmthin", "nfs", "pbs", "rbd", "zfs", "zfspool"], "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/storage)。

## `/storage/{storage}` <a href="#api-storage-storage-fcefaab1" id="api-storage-storage-fcefaab1"></a>

原始接口路径：`/storage/{storage}`。

### DELETE `/storage/{storage}` <a href="#api-storage-storage-fcefaab1-delete" id="api-storage-storage-fcefaab1-delete"></a>

删除存储配置。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/storage", ["Datastore.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-storage-storage-fcefaab1-delete-parameters" id="api-storage-storage-fcefaab1-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `storage` | 类型：string；必填：是；默认值：—<br>存储标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"storage": {"description": "存储标识符。", "format": "pve-storage-id", "format_description": "storage ID", "type": "string", "typetext": "<storage ID>"}}}
```

</details>

#### 返回值 <a href="#api-storage-storage-fcefaab1-delete-returns" id="api-storage-storage-fcefaab1-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/storage/{storage}` <a href="#api-storage-storage-fcefaab1-get" id="api-storage-storage-fcefaab1-get"></a>

读取存储配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/storage/{storage}", ["Datastore.Allocate"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-storage-storage-fcefaab1-get-parameters" id="api-storage-storage-fcefaab1-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `storage` | 类型：string；必填：是；默认值：—<br>存储标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"storage": {"description": "存储标识符。", "format": "pve-storage-id", "format_description": "storage ID", "type": "string", "typetext": "<storage ID>"}}}
```

</details>

#### 返回值 <a href="#api-storage-storage-fcefaab1-get-returns" id="api-storage-storage-fcefaab1-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/storage/{storage}` <a href="#api-storage-storage-fcefaab1-put" id="api-storage-storage-fcefaab1-put"></a>

更新存储配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/storage", ["Datastore.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-storage-storage-fcefaab1-put-parameters" id="api-storage-storage-fcefaab1-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `blocksize` | 类型：string；必填：否；默认值：—<br>ZFS 块大小 |
| `bwlimit` | 类型：string；必填：否；默认值：—<br>为各类操作设置 I/O 带宽限制（单位为 KiB/s）。 |
| `comstar_hg` | 类型：string；必填：否；默认值：—<br>comstar 视图的主机组 |
| `comstar_tg` | 类型：string；必填：否；默认值：—<br>comstar 视图的目标组 |
| `content` | 类型：string；必填：否；默认值：—<br>允许的内容类型。<br><br>注意：值 'rootdir' 用于容器，值 'images' 用于虚拟机。<br> |
| `content-dirs` | 类型：string；必填：否；默认值：—<br>覆盖默认内容类型目录。 |
| `create-base-path` | 类型：boolean；必填：否；默认值："yes"<br>如果基础目录不存在，则创建。 |
| `create-subdirs` | 类型：boolean；必填：否；默认值："yes"<br>使用默认结构填充目录。 |
| `data-pool` | 类型：string；必填：否；默认值：—<br>数据池（仅用于纠删码） |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用存储的标志。 |
| `domain` | 类型：string；必填：否；默认值：—<br>CIFS 域。 |
| `encryption-key` | 类型：string；必填：否；默认值：—<br>加密密钥。使用 'autogen' 自动生成不带口令的密钥。 |
| `fingerprint` | 类型：string；必填：否；默认值：—<br>证书 SHA 256 指纹。 |
| `format` | 类型：string；必填：否；默认值：—<br>默认镜像格式。；可选值：`raw`, `qcow2`, `subvol`, `vmdk` |
| `fs-name` | 类型：string；必填：否；默认值：—<br>Ceph 文件系统名称。 |
| `fuse` | 类型：boolean；必填：否；默认值：—<br>通过 FUSE 挂载 CephFS。 |
| `is_mountpoint` | 类型：string；必填：否；默认值："no"<br>将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是将目标路径填入此字段的简写方式。 |
| `keyring` | 类型：string；必填：否；默认值：—<br>客户端密钥环内容（用于外部集群）。 |
| `krbd` | 类型：boolean；必填：否；默认值：0<br>始终通过 krbd 内核模块访问 RBD。 |
| `lio_tpg` | 类型：string；必填：否；默认值：—<br>Linux LIO 目标的目标门户组 |
| `master-pubkey` | 类型：string；必填：否；默认值：—<br>Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。 |
| `max-protected-backups` | 类型：integer；必填：否；默认值："Unlimited for users with Datastore.Allocate privilege, 5 for other users"<br>每个客户机的最大受保护备份数。使用 '-1' 表示无限制。 |
| `mkdir` | 类型：boolean；必填：否；默认值："yes"<br>如果目录不存在，则创建并填充默认子目录。注意：已弃用，请改用 'create-base-path' 和 'create-subdirs' 选项。 |
| `monhost` | 类型：string；必填：否；默认值：—<br>监视器的 IP 地址（用于外部集群）。 |
| `mountpoint` | 类型：string；必填：否；默认值：—<br>挂载点 |
| `namespace` | 类型：string；必填：否；默认值：—<br>命名空间。 |
| `nocow` | 类型：boolean；必填：否；默认值：0<br>为文件设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。仅当数据安全性要求不高于未使用底层 RAID 系统的单个 ext4 格式磁盘时，才使用此选项。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>存储配置适用的节点列表。 |
| `nowritecache` | 类型：boolean；必填：否；默认值：—<br>禁用目标上的写缓存 |
| `options` | 类型：string；必填：否；默认值：—<br>NFS/CIFS 挂载选项（参见 'man nfs' 或 'man mount.cifs'） |
| `password` | 类型：string；必填：否；默认值：—<br>访问共享/数据存储的密码。 |
| `pool` | 类型：string；必填：否；默认值：—<br>池。 |
| `port` | 类型：integer；必填：否；默认值：—<br>使用此端口代替默认端口连接存储（例如 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 'options' 选项通过挂载选项配置端口。 |
| `preallocation` | 类型：string；必填：否；默认值："metadata"<br>raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 'metadata' 将产生 preallocation=off 的效果。；可选值：`off`, `metadata`, `falloc`, `full` |
| `prune-backups` | 类型：string；必填：否；默认值：—<br>优先处理时间间隔较短的保留选项，其中 --keep-last 最先处理。每个选项覆盖特定时间段。我们称此时间段内的备份被此选项覆盖。下一个选项不会处理已被覆盖的备份，只考虑更旧的备份。 |
| `saferemove` | 类型：boolean；必填：否；默认值：—<br>移除逻辑卷时将数据清零。 |
| `saferemove-stepsize` | 类型：integer；必填：否；默认值：32<br>擦除步长，单位为 MiB。上限为存储支持的最大值。；可选值：`1`, `2`, `4`, `8`, `16`, `32` |
| `saferemove_throughput` | 类型：string；必填：否；默认值：—<br>擦除吞吐量（cstream -t 参数值）。 |
| `server` | 类型：string；必填：否；默认值：—<br>服务器 IP 或 DNS 名称。 |
| `shared` | 类型：boolean；必填：否；默认值：—<br>表明这是在所有节点（或 'nodes' 选项列出的所有节点）上具有相同内容的单一存储。此项不会使其他节点自动访问本地存储内容，只是将已经共享的存储标记为共享！ |
| `skip-cert-verification` | 类型：boolean；必填：否；默认值："false"<br>禁用 TLS 证书验证，仅在完全可信的网络中启用！ |
| `smbversion` | 类型：string；必填：否；默认值："default"<br>SMB 协议版本。未设置时为 'default'，协商客户端与服务器共同支持的最高 SMB2+ 版本。；可选值：`default`, `2.0`, `2.1`, `3`, `3.0`, `3.11` |
| `snapshot-as-volume-chain` | 类型：boolean；必填：否；默认值：0<br>启用通过卷后端链创建与存储供应商无关的快照的支持。 |
| `sparse` | 类型：boolean；必填：否；默认值：—<br>使用稀疏卷 |
| `storage` | 类型：string；必填：是；默认值：—<br>存储标识符。 |
| `subdir` | 类型：string；必填：否；默认值：—<br>要挂载的子目录。 |
| `tagged_only` | 类型：boolean；必填：否；默认值：—<br>仅列出带有 'pve-vm-ID' 标签的逻辑卷。 |
| `username` | 类型：string；必填：否；默认值：—<br>RBD ID。 |
| `zfs-base-path` | 类型：string；必填：否；默认值：—<br>查找创建的 ZFS 块设备的基础路径。如果未指定，则在创建时自动设置。通常为 '/dev/zvol'。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "blocksize": {"description": "ZFS 块大小", "format": "pve-storage-zfs-blocksize", "format_description": "a power of 2 with optional k or m suffix", "optional": 1, "type": "string", "typetext": "<a power of 2 with optional k or m suffix>"},
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {"description": "克隆磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}, "default": {"description": "默认带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "migration": {"description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}, "move": {"description": "移动磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "restore": {"description": "从备份还原客户机的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}
      },
      "optional": 1, "type": "string", "typetext": "[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]"
    },
    "comstar_hg": {"description": "comstar 视图的主机组", "optional": 1, "type": "string", "typetext": "<string>"}, "comstar_tg": {"description": "comstar 视图的目标组", "optional": 1, "type": "string", "typetext": "<string>"},
    "content": {"description": "允许的内容类型。\n\n注意：值 'rootdir' 用于容器，值 'images' 用于虚拟机。\n", "format": "pve-storage-content-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "content-dirs": {"description": "覆盖默认内容类型目录。", "format": "pve-dir-override-list", "optional": 1, "type": "string", "typetext": "<string>"}, "create-base-path": {"default": "yes", "description": "如果基础目录不存在，则创建。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "create-subdirs": {"default": "yes", "description": "使用默认结构填充目录。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "data-pool": {"description": "数据池（仅用于纠删码）", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string", "typetext": "<string>"}, "disable": {"description": "用于禁用存储的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "domain": {"description": "CIFS 域。", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "encryption-key": {"description": "加密密钥。使用 'autogen' 自动生成不带口令的密钥。", "optional": 1, "type": "string", "typetext": "<string>"},
    "fingerprint": {"description": "证书 SHA 256 指纹。", "optional": 1, "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"}, "format": {"description": "默认镜像格式。", "enum": ["raw", "qcow2", "subvol", "vmdk"], "optional": 1, "type": "string"},
    "fs-name": {"description": "Ceph 文件系统名称。", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"}, "fuse": {"description": "通过 FUSE 挂载 CephFS。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "is_mountpoint": {"default": "no", "description": "将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是将目标路径填入此字段的简写方式。", "optional": 1, "type": "string", "typetext": "<string>"},
    "keyring": {"description": "客户端密钥环内容（用于外部集群）。", "optional": 1, "type": "string", "typetext": "<string>"}, "krbd": {"default": 0, "description": "始终通过 krbd 内核模块访问 RBD。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "lio_tpg": {"description": "Linux LIO 目标的目标门户组", "optional": 1, "type": "string", "typetext": "<string>"}, "master-pubkey": {"description": "Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。", "optional": 1, "type": "string", "typetext": "<string>"},
    "max-protected-backups": {"default": "Unlimited for users with Datastore.Allocate privilege, 5 for other users", "description": "每个客户机的最大受保护备份数。使用 '-1' 表示无限制。", "minimum": -1, "optional": 1, "type": "integer", "typetext": "<integer> (-1 - N)"},
    "mkdir": {"default": "yes", "description": "如果目录不存在，则创建并填充默认子目录。注意：已弃用，请改用 'create-base-path' 和 'create-subdirs' 选项。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "monhost": {"description": "监视器的 IP 地址（用于外部集群）。", "format": "pve-storage-portal-dns-list", "optional": 1, "type": "string", "typetext": "<string>"}, "mountpoint": {"description": "挂载点", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"},
    "namespace": {"description": "命名空间。", "optional": 1, "type": "string", "typetext": "<string>"},
    "nocow": {"default": 0, "description": "为文件设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。仅当数据安全性要求不高于未使用底层 RAID 系统的单个 ext4 格式磁盘时，才使用此选项。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "nodes": {"description": "存储配置适用的节点列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"}, "nowritecache": {"description": "禁用目标上的写缓存", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "options": {"description": "NFS/CIFS 挂载选项（参见 'man nfs' 或 'man mount.cifs'）", "format": "pve-storage-options", "optional": 1, "type": "string", "typetext": "<string>"}, "password": {"description": "访问共享/数据存储的密码。", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "pool": {"description": "池。", "optional": 1, "type": "string", "typetext": "<string>"},
    "port": {"description": "使用此端口代替默认端口连接存储（例如 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 'options' 选项通过挂载选项配置端口。", "maximum": 65535, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 65535)"},
    "preallocation": {"default": "metadata", "description": "raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 'metadata' 将产生 preallocation=off 的效果。", "enum": ["off", "metadata", "falloc", "full"], "optional": 1, "type": "string"},
    "prune-backups": {
      "description": "优先处理时间间隔较短的保留选项，其中 --keep-last 最先处理。每个选项覆盖特定时间段。我们称此时间段内的备份被此选项覆盖。下一个选项不会处理已被覆盖的备份，只考虑更旧的备份。", "format": "prune-backups", "optional": 1, "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "saferemove": {"description": "移除逻辑卷时将数据清零。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "saferemove-stepsize": {"default": 32, "description": "擦除步长，单位为 MiB。上限为存储支持的最大值。", "enum": ["1", "2", "4", "8", "16", "32"], "optional": 1, "type": "integer"},
    "saferemove_throughput": {"description": "擦除吞吐量（cstream -t 参数值）。", "optional": 1, "type": "string", "typetext": "<string>"}, "server": {"description": "服务器 IP 或 DNS 名称。", "format": "pve-storage-server", "optional": 1, "type": "string", "typetext": "<string>"},
    "shared": {"description": "表明这是在所有节点（或 'nodes' 选项列出的所有节点）上具有相同内容的单一存储。此项不会使其他节点自动访问本地存储内容，只是将已经共享的存储标记为共享！", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "skip-cert-verification": {"default": "false", "description": "禁用 TLS 证书验证，仅在完全可信的网络中启用！", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "smbversion": {"default": "default", "description": "SMB 协议版本。未设置时为 'default'，协商客户端与服务器共同支持的最高 SMB2+ 版本。", "enum": ["default", "2.0", "2.1", "3", "3.0", "3.11"], "optional": 1, "type": "string"},
    "snapshot-as-volume-chain": {"default": 0, "description": "启用通过卷后端链创建与存储供应商无关的快照的支持。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "sparse": {"description": "使用稀疏卷", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "storage": {"description": "存储标识符。", "format": "pve-storage-id", "format_description": "storage ID", "type": "string", "typetext": "<storage ID>"}, "subdir": {"description": "要挂载的子目录。", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"},
    "tagged_only": {"description": "仅列出带有 'pve-vm-ID' 标签的逻辑卷。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "username": {"description": "RBD ID。", "optional": 1, "type": "string", "typetext": "<string>"},
    "zfs-base-path": {"description": "查找创建的 ZFS 块设备的基础路径。如果未指定，则在创建时自动设置。通常为 '/dev/zvol'。", "format": "pve-storage-path", "optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-storage-storage-fcefaab1-put-returns" id="api-storage-storage-fcefaab1-put-returns"></a>

```text
{
  "properties": {
    "config": {"additionalProperties": 1, "description": "部分配置属性，可能由服务器生成。", "optional": 1, "properties": {"encryption-key": {"description": "加密密钥，可能为自动生成。", "optional": 1, "type": "string"}}, "type": "object"}, "storage": {"description": "所创建存储的 ID。", "type": "string"},
    "type": {"description": "所创建存储的类型。", "enum": ["btrfs", "cephfs", "cifs", "dir", "esxi", "iscsi", "iscsidirect", "lvm", "lvmthin", "nfs", "pbs", "rbd", "zfs", "zfspool"], "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/storage/{storage})。
