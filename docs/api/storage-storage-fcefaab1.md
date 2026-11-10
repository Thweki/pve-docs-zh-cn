# `/storage/{storage}`

原始接口路径：`/storage/{storage}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/storage/{storage}`

删除存储配置。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/storage",
    [
      "Datastore.Allocate"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `storage` | string | 是 | — | 存储标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## GET `/storage/{storage}`

读取存储配置。

**方法标识：** `read`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.Allocate"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `storage` | string | 是 | — | 存储标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "object"
}
```

## PUT `/storage/{storage}`

更新存储配置。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/storage",
    [
      "Datastore.Allocate"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `blocksize` | string | 否 | — | ZFS 块大小 |
| `bwlimit` | string | 否 | — | 为各类操作设置 I/O 带宽限制（单位为 KiB/s）。 |
| `comstar_hg` | string | 否 | — | comstar 视图的主机组 |
| `comstar_tg` | string | 否 | — | comstar 视图的目标组 |
| `content` | string | 否 | — | 允许的内容类型。<br><br>注意：值 'rootdir' 用于容器，值 'images' 用于虚拟机。<br> |
| `content-dirs` | string | 否 | — | 覆盖默认内容类型目录。 |
| `create-base-path` | boolean | 否 | "yes" | 如果基础目录不存在，则创建。 |
| `create-subdirs` | boolean | 否 | "yes" | 使用默认结构填充目录。 |
| `data-pool` | string | 否 | — | 数据池（仅用于纠删码） |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | boolean | 否 | — | 用于禁用存储的标志。 |
| `domain` | string | 否 | — | CIFS 域。 |
| `encryption-key` | string | 否 | — | 加密密钥。使用 'autogen' 自动生成不带口令的密钥。 |
| `fingerprint` | string | 否 | — | 证书 SHA 256 指纹。 |
| `format` | string | 否 | — | 默认镜像格式。；可选值：`raw`, `qcow2`, `subvol`, `vmdk` |
| `fs-name` | string | 否 | — | Ceph 文件系统名称。 |
| `fuse` | boolean | 否 | — | 通过 FUSE 挂载 CephFS。 |
| `is_mountpoint` | string | 否 | "no" | 将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是将目标路径填入此字段的简写方式。 |
| `keyring` | string | 否 | — | 客户端密钥环内容（用于外部集群）。 |
| `krbd` | boolean | 否 | 0 | 始终通过 krbd 内核模块访问 RBD。 |
| `lio_tpg` | string | 否 | — | Linux LIO 目标的目标门户组 |
| `master-pubkey` | string | 否 | — | Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。 |
| `max-protected-backups` | integer | 否 | "Unlimited for users with Datastore.Allocate privilege, 5 for other users" | 每个客户机的最大受保护备份数。使用 '-1' 表示无限制。 |
| `mkdir` | boolean | 否 | "yes" | 如果目录不存在，则创建并填充默认子目录。注意：已弃用，请改用 'create-base-path' 和 'create-subdirs' 选项。 |
| `monhost` | string | 否 | — | 监视器的 IP 地址（用于外部集群）。 |
| `mountpoint` | string | 否 | — | 挂载点 |
| `namespace` | string | 否 | — | 命名空间。 |
| `nocow` | boolean | 否 | 0 | 为文件设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。仅当数据安全性要求不高于未使用底层 RAID 系统的单个 ext4 格式磁盘时，才使用此选项。 |
| `nodes` | string | 否 | — | 存储配置适用的节点列表。 |
| `nowritecache` | boolean | 否 | — | 禁用目标上的写缓存 |
| `options` | string | 否 | — | NFS/CIFS 挂载选项（参见 'man nfs' 或 'man mount.cifs'） |
| `password` | string | 否 | — | 访问共享/数据存储的密码。 |
| `pool` | string | 否 | — | 池。 |
| `port` | integer | 否 | — | 使用此端口代替默认端口连接存储（例如 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 'options' 选项通过挂载选项配置端口。 |
| `preallocation` | string | 否 | "metadata" | raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 'metadata' 将产生 preallocation=off 的效果。；可选值：`off`, `metadata`, `falloc`, `full` |
| `prune-backups` | string | 否 | — | 优先处理时间间隔较短的保留选项，其中 --keep-last 最先处理。每个选项覆盖特定时间段。我们称此时间段内的备份被此选项覆盖。下一个选项不会处理已被覆盖的备份，只考虑更旧的备份。 |
| `saferemove` | boolean | 否 | — | 移除逻辑卷时将数据清零。 |
| `saferemove-stepsize` | integer | 否 | 32 | 擦除步长，单位为 MiB。上限为存储支持的最大值。；可选值：`1`, `2`, `4`, `8`, `16`, `32` |
| `saferemove_throughput` | string | 否 | — | 擦除吞吐量（cstream -t 参数值）。 |
| `server` | string | 否 | — | 服务器 IP 或 DNS 名称。 |
| `shared` | boolean | 否 | — | 表明这是在所有节点（或 'nodes' 选项列出的所有节点）上具有相同内容的单一存储。此项不会使其他节点自动访问本地存储内容，只是将已经共享的存储标记为共享！ |
| `skip-cert-verification` | boolean | 否 | "false" | 禁用 TLS 证书验证，仅在完全可信的网络中启用！ |
| `smbversion` | string | 否 | "default" | SMB 协议版本。未设置时为 'default'，协商客户端与服务器共同支持的最高 SMB2+ 版本。；可选值：`default`, `2.0`, `2.1`, `3`, `3.0`, `3.11` |
| `snapshot-as-volume-chain` | boolean | 否 | 0 | 启用通过卷后端链创建与存储供应商无关的快照的支持。 |
| `sparse` | boolean | 否 | — | 使用稀疏卷 |
| `storage` | string | 是 | — | 存储标识符。 |
| `subdir` | string | 否 | — | 要挂载的子目录。 |
| `tagged_only` | boolean | 否 | — | 仅列出带有 'pve-vm-ID' 标签的逻辑卷。 |
| `username` | string | 否 | — | RBD ID。 |
| `zfs-base-path` | string | 否 | — | 查找创建的 ZFS 块设备的基础路径。如果未指定，则在创建时自动设置。通常为 '/dev/zvol'。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "blocksize": {
      "description": "ZFS 块大小",
      "format": "pve-storage-zfs-blocksize",
      "format_description": "a power of 2 with optional k or m suffix",
      "optional": 1,
      "type": "string",
      "typetext": "<a power of 2 with optional k or m suffix>"
    },
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {
          "description": "克隆磁盘的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "default": {
          "description": "默认带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "migration": {
          "description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "move": {
          "description": "移动磁盘的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "restore": {
          "description": "从备份还原客户机的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]"
    },
    "comstar_hg": {
      "description": "comstar 视图的主机组",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comstar_tg": {
      "description": "comstar 视图的目标组",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "content": {
      "description": "允许的内容类型。\n\n注意：值 'rootdir' 用于容器，值 'images' 用于虚拟机。\n",
      "format": "pve-storage-content-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "content-dirs": {
      "description": "覆盖默认内容类型目录。",
      "format": "pve-dir-override-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "create-base-path": {
      "default": "yes",
      "description": "如果基础目录不存在，则创建。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "create-subdirs": {
      "default": "yes",
      "description": "使用默认结构填充目录。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "data-pool": {
      "description": "数据池（仅用于纠删码）",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "用于禁用存储的标志。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "domain": {
      "description": "CIFS 域。",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "encryption-key": {
      "description": "加密密钥。使用 'autogen' 自动生成不带口令的密钥。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fingerprint": {
      "description": "证书 SHA 256 指纹。",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "format": {
      "description": "默认镜像格式。",
      "enum": [
        "raw",
        "qcow2",
        "subvol",
        "vmdk"
      ],
      "optional": 1,
      "type": "string"
    },
    "fs-name": {
      "description": "Ceph 文件系统名称。",
      "format": "pve-configid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fuse": {
      "description": "通过 FUSE 挂载 CephFS。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "is_mountpoint": {
      "default": "no",
      "description": "将给定路径视为外部管理的挂载点，如果未挂载，则认为存储离线。使用布尔值（yes/no）是将目标路径填入此字段的简写方式。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "keyring": {
      "description": "客户端密钥环内容（用于外部集群）。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "krbd": {
      "default": 0,
      "description": "始终通过 krbd 内核模块访问 RBD。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lio_tpg": {
      "description": "Linux LIO 目标的目标门户组",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "master-pubkey": {
      "description": "Base64 编码、PEM 格式的 RSA 公钥。用于加密 encryption-key 的副本，该副本将添加到每个加密备份中。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "max-protected-backups": {
      "default": "Unlimited for users with Datastore.Allocate privilege, 5 for other users",
      "description": "每个客户机的最大受保护备份数。使用 '-1' 表示无限制。",
      "minimum": -1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (-1 - N)"
    },
    "mkdir": {
      "default": "yes",
      "description": "如果目录不存在，则创建并填充默认子目录。注意：已弃用，请改用 'create-base-path' 和 'create-subdirs' 选项。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "monhost": {
      "description": "监视器的 IP 地址（用于外部集群）。",
      "format": "pve-storage-portal-dns-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mountpoint": {
      "description": "挂载点",
      "format": "pve-storage-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "namespace": {
      "description": "命名空间。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nocow": {
      "default": 0,
      "description": "为文件设置 NOCOW 标志。禁用数据校验和，使数据错误无法恢复，同时允许直接 I/O。仅当数据安全性要求不高于未使用底层 RAID 系统的单个 ext4 格式磁盘时，才使用此选项。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nodes": {
      "description": "存储配置适用的节点列表。",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nowritecache": {
      "description": "禁用目标上的写缓存",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "options": {
      "description": "NFS/CIFS 挂载选项（参见 'man nfs' 或 'man mount.cifs'）",
      "format": "pve-storage-options",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "访问共享/数据存储的密码。",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "pool": {
      "description": "池。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "使用此端口代替默认端口连接存储（例如 PBS 或 ESXi）。对于 NFS 和 CIFS，请使用 'options' 选项通过挂载选项配置端口。",
      "maximum": 65535,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65535)"
    },
    "preallocation": {
      "default": "metadata",
      "description": "raw 和 qcow2 镜像的预分配模式。对 raw 镜像使用 'metadata' 将产生 preallocation=off 的效果。",
      "enum": [
        "off",
        "metadata",
        "falloc",
        "full"
      ],
      "optional": 1,
      "type": "string"
    },
    "prune-backups": {
      "description": "优先处理时间间隔较短的保留选项，其中 --keep-last 最先处理。每个选项覆盖特定时间段。我们称此时间段内的备份被此选项覆盖。下一个选项不会处理已被覆盖的备份，只考虑更旧的备份。",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "saferemove": {
      "description": "移除逻辑卷时将数据清零。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "saferemove-stepsize": {
      "default": 32,
      "description": "擦除步长，单位为 MiB。上限为存储支持的最大值。",
      "enum": [
        "1",
        "2",
        "4",
        "8",
        "16",
        "32"
      ],
      "optional": 1,
      "type": "integer"
    },
    "saferemove_throughput": {
      "description": "擦除吞吐量（cstream -t 参数值）。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "server": {
      "description": "服务器 IP 或 DNS 名称。",
      "format": "pve-storage-server",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "shared": {
      "description": "表明这是在所有节点（或 'nodes' 选项列出的所有节点）上具有相同内容的单一存储。此项不会使其他节点自动访问本地存储内容，只是将已经共享的存储标记为共享！",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "skip-cert-verification": {
      "default": "false",
      "description": "禁用 TLS 证书验证，仅在完全可信的网络中启用！",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "smbversion": {
      "default": "default",
      "description": "SMB 协议版本。未设置时为 'default'，协商客户端与服务器共同支持的最高 SMB2+ 版本。",
      "enum": [
        "default",
        "2.0",
        "2.1",
        "3",
        "3.0",
        "3.11"
      ],
      "optional": 1,
      "type": "string"
    },
    "snapshot-as-volume-chain": {
      "default": 0,
      "description": "启用通过卷后端链创建与存储供应商无关的快照的支持。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "sparse": {
      "description": "使用稀疏卷",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "subdir": {
      "description": "要挂载的子目录。",
      "format": "pve-storage-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tagged_only": {
      "description": "仅列出带有 'pve-vm-ID' 标签的逻辑卷。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "username": {
      "description": "RBD ID。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "zfs-base-path": {
      "description": "查找创建的 ZFS 块设备的基础路径。如果未指定，则在创建时自动设置。通常为 '/dev/zvol'。",
      "format": "pve-storage-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "properties": {
    "config": {
      "additionalProperties": 1,
      "description": "部分配置属性，可能由服务器生成。",
      "optional": 1,
      "properties": {
        "encryption-key": {
          "description": "加密密钥，可能为自动生成。",
          "optional": 1,
          "type": "string"
        }
      },
      "type": "object"
    },
    "storage": {
      "description": "所创建存储的 ID。",
      "type": "string"
    },
    "type": {
      "description": "所创建存储的类型。",
      "enum": [
        "btrfs",
        "cephfs",
        "cifs",
        "dir",
        "esxi",
        "iscsi",
        "iscsidirect",
        "lvm",
        "lvmthin",
        "nfs",
        "pbs",
        "rbd",
        "zfs",
        "zfspool"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/storage/{storage})。
