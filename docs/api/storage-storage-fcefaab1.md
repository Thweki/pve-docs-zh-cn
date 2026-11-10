# `/storage/{storage}`

原始接口路径：`/storage/{storage}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/storage/{storage}`

Delete storage configuration.

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
| `storage` | string | 是 | — | The storage identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "storage": {
      "description": "The storage identifier.",
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

Read storage configuration.

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
| `storage` | string | 是 | — | The storage identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "storage": {
      "description": "The storage identifier.",
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

Update storage configuration.

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
| `blocksize` | string | 否 | — | ZFS block size |
| `bwlimit` | string | 否 | — | Set I/O bandwidth limit for various operations (in KiB/s). |
| `comstar_hg` | string | 否 | — | host group for comstar views |
| `comstar_tg` | string | 否 | — | target group for comstar views |
| `content` | string | 否 | — | Allowed content types.<br><br>NOTE: the value 'rootdir' is used for Containers, and value 'images' for VMs.<br> |
| `content-dirs` | string | 否 | — | Overrides for default content type directories. |
| `create-base-path` | boolean | 否 | "yes" | Create the base directory if it doesn't exist. |
| `create-subdirs` | boolean | 否 | "yes" | Populate the directory with the default structure. |
| `data-pool` | string | 否 | — | Data Pool (for erasure coding only) |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable` | boolean | 否 | — | Flag to disable the storage. |
| `domain` | string | 否 | — | CIFS domain. |
| `encryption-key` | string | 否 | — | Encryption key. Use 'autogen' to generate one automatically without passphrase. |
| `fingerprint` | string | 否 | — | Certificate SHA 256 fingerprint. |
| `format` | string | 否 | — | Default image format.；可选值：`raw`, `qcow2`, `subvol`, `vmdk` |
| `fs-name` | string | 否 | — | The Ceph filesystem name. |
| `fuse` | boolean | 否 | — | Mount CephFS through FUSE. |
| `is_mountpoint` | string | 否 | "no" | Assume the given path is an externally managed mountpoint and consider the storage offline if it is not mounted. Using a boolean (yes/no) value serves as a shortcut to using the target path in this field. |
| `keyring` | string | 否 | — | Client keyring contents (for external clusters). |
| `krbd` | boolean | 否 | 0 | Always access rbd through krbd kernel module. |
| `lio_tpg` | string | 否 | — | target portal group for Linux LIO targets |
| `master-pubkey` | string | 否 | — | Base64-encoded, PEM-formatted public RSA key. Used to encrypt a copy of the encryption-key which will be added to each encrypted backup. |
| `max-protected-backups` | integer | 否 | "Unlimited for users with Datastore.Allocate privilege, 5 for other users" | Maximal number of protected backups per guest. Use '-1' for unlimited. |
| `mkdir` | boolean | 否 | "yes" | Create the directory if it doesn't exist and populate it with default sub-dirs. NOTE: Deprecated, use the 'create-base-path' and 'create-subdirs' options instead. |
| `monhost` | string | 否 | — | IP addresses of monitors (for external clusters). |
| `mountpoint` | string | 否 | — | mount point |
| `namespace` | string | 否 | — | Namespace. |
| `nocow` | boolean | 否 | 0 | Set the NOCOW flag on files. Disables data checksumming and causes data errors to be unrecoverable from while allowing direct I/O. Only use this if data does not need to be any more safe than on a single ext4 formatted disk with no underlying raid system. |
| `nodes` | string | 否 | — | List of nodes for which the storage configuration applies. |
| `nowritecache` | boolean | 否 | — | disable write caching on the target |
| `options` | string | 否 | — | NFS/CIFS mount options (see 'man nfs' or 'man mount.cifs') |
| `password` | string | 否 | — | Password for accessing the share/datastore. |
| `pool` | string | 否 | — | Pool. |
| `port` | integer | 否 | — | Use this port to connect to the storage instead of the default one (for example, with PBS or ESXi). For NFS and CIFS, use the 'options' option to configure the port via the mount options. |
| `preallocation` | string | 否 | "metadata" | Preallocation mode for raw and qcow2 images. Using 'metadata' on raw images results in preallocation=off.；可选值：`off`, `metadata`, `falloc`, `full` |
| `prune-backups` | string | 否 | — | The retention options with shorter intervals are processed first with --keep-last being the very first one. Each option covers a specific period of time. We say that backups within this period are covered by this option. The next option does not take care of already covered backups and only considers older backups. |
| `saferemove` | boolean | 否 | — | Zero-out data when removing LVs. |
| `saferemove-stepsize` | integer | 否 | 32 | Wipe step size in MiB. It will be capped to the maximum supported by the storage.；可选值：`1`, `2`, `4`, `8`, `16`, `32` |
| `saferemove_throughput` | string | 否 | — | Wipe throughput (cstream -t parameter value). |
| `server` | string | 否 | — | Server IP or DNS name. |
| `shared` | boolean | 否 | — | Indicate that this is a single storage with the same contents on all nodes (or all listed in the 'nodes' option). It will not make the contents of a local storage automatically accessible to other nodes, it just marks an already shared storage as such! |
| `skip-cert-verification` | boolean | 否 | "false" | Disable TLS certificate verification, only enable on fully trusted networks! |
| `smbversion` | string | 否 | "default" | SMB protocol version. 'default' if not set, negotiates the highest SMB2+ version supported by both the client and server.；可选值：`default`, `2.0`, `2.1`, `3`, `3.0`, `3.11` |
| `snapshot-as-volume-chain` | boolean | 否 | 0 | Enable support for creating storage-vendor agnostic snapshot through volume backing-chains. |
| `sparse` | boolean | 否 | — | use sparse volumes |
| `storage` | string | 是 | — | The storage identifier. |
| `subdir` | string | 否 | — | Subdir to mount. |
| `tagged_only` | boolean | 否 | — | Only list logical volumes tagged with 'pve-vm-ID'. |
| `username` | string | 否 | — | RBD Id. |
| `zfs-base-path` | string | 否 | — | Base path where to look for the created ZFS block devices. Set automatically during creation if not specified. Usually '/dev/zvol'. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "blocksize": {
      "description": "ZFS block size",
      "format": "pve-storage-zfs-blocksize",
      "format_description": "a power of 2 with optional k or m suffix",
      "optional": 1,
      "type": "string",
      "typetext": "<a power of 2 with optional k or m suffix>"
    },
    "bwlimit": {
      "description": "Set I/O bandwidth limit for various operations (in KiB/s).",
      "format": {
        "clone": {
          "description": "bandwidth limit in KiB/s for cloning disks",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "default": {
          "description": "default bandwidth limit in KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "migration": {
          "description": "bandwidth limit in KiB/s for migrating guests (including moving local disks)",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "move": {
          "description": "bandwidth limit in KiB/s for moving disks",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "restore": {
          "description": "bandwidth limit in KiB/s for restoring guests from backups",
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
      "description": "host group for comstar views",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comstar_tg": {
      "description": "target group for comstar views",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "content": {
      "description": "Allowed content types.\n\nNOTE: the value 'rootdir' is used for Containers, and value 'images' for VMs.\n",
      "format": "pve-storage-content-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "content-dirs": {
      "description": "Overrides for default content type directories.",
      "format": "pve-dir-override-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "create-base-path": {
      "default": "yes",
      "description": "Create the base directory if it doesn't exist.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "create-subdirs": {
      "default": "yes",
      "description": "Populate the directory with the default structure.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "data-pool": {
      "description": "Data Pool (for erasure coding only)",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "Flag to disable the storage.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "domain": {
      "description": "CIFS domain.",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "encryption-key": {
      "description": "Encryption key. Use 'autogen' to generate one automatically without passphrase.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fingerprint": {
      "description": "Certificate SHA 256 fingerprint.",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "format": {
      "description": "Default image format.",
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
      "description": "The Ceph filesystem name.",
      "format": "pve-configid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fuse": {
      "description": "Mount CephFS through FUSE.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "is_mountpoint": {
      "default": "no",
      "description": "Assume the given path is an externally managed mountpoint and consider the storage offline if it is not mounted. Using a boolean (yes/no) value serves as a shortcut to using the target path in this field.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "keyring": {
      "description": "Client keyring contents (for external clusters).",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "krbd": {
      "default": 0,
      "description": "Always access rbd through krbd kernel module.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lio_tpg": {
      "description": "target portal group for Linux LIO targets",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "master-pubkey": {
      "description": "Base64-encoded, PEM-formatted public RSA key. Used to encrypt a copy of the encryption-key which will be added to each encrypted backup.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "max-protected-backups": {
      "default": "Unlimited for users with Datastore.Allocate privilege, 5 for other users",
      "description": "Maximal number of protected backups per guest. Use '-1' for unlimited.",
      "minimum": -1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (-1 - N)"
    },
    "mkdir": {
      "default": "yes",
      "description": "Create the directory if it doesn't exist and populate it with default sub-dirs. NOTE: Deprecated, use the 'create-base-path' and 'create-subdirs' options instead.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "monhost": {
      "description": "IP addresses of monitors (for external clusters).",
      "format": "pve-storage-portal-dns-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mountpoint": {
      "description": "mount point",
      "format": "pve-storage-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "namespace": {
      "description": "Namespace.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nocow": {
      "default": 0,
      "description": "Set the NOCOW flag on files. Disables data checksumming and causes data errors to be unrecoverable from while allowing direct I/O. Only use this if data does not need to be any more safe than on a single ext4 formatted disk with no underlying raid system.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nodes": {
      "description": "List of nodes for which the storage configuration applies.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nowritecache": {
      "description": "disable write caching on the target",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "options": {
      "description": "NFS/CIFS mount options (see 'man nfs' or 'man mount.cifs')",
      "format": "pve-storage-options",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "Password for accessing the share/datastore.",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "pool": {
      "description": "Pool.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "Use this port to connect to the storage instead of the default one (for example, with PBS or ESXi). For NFS and CIFS, use the 'options' option to configure the port via the mount options.",
      "maximum": 65535,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65535)"
    },
    "preallocation": {
      "default": "metadata",
      "description": "Preallocation mode for raw and qcow2 images. Using 'metadata' on raw images results in preallocation=off.",
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
      "description": "The retention options with shorter intervals are processed first with --keep-last being the very first one. Each option covers a specific period of time. We say that backups within this period are covered by this option. The next option does not take care of already covered backups and only considers older backups.",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "saferemove": {
      "description": "Zero-out data when removing LVs.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "saferemove-stepsize": {
      "default": 32,
      "description": "Wipe step size in MiB. It will be capped to the maximum supported by the storage.",
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
      "description": "Wipe throughput (cstream -t parameter value).",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "server": {
      "description": "Server IP or DNS name.",
      "format": "pve-storage-server",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "shared": {
      "description": "Indicate that this is a single storage with the same contents on all nodes (or all listed in the 'nodes' option). It will not make the contents of a local storage automatically accessible to other nodes, it just marks an already shared storage as such!",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "skip-cert-verification": {
      "default": "false",
      "description": "Disable TLS certificate verification, only enable on fully trusted networks!",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "smbversion": {
      "default": "default",
      "description": "SMB protocol version. 'default' if not set, negotiates the highest SMB2+ version supported by both the client and server.",
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
      "description": "Enable support for creating storage-vendor agnostic snapshot through volume backing-chains.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "sparse": {
      "description": "use sparse volumes",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "subdir": {
      "description": "Subdir to mount.",
      "format": "pve-storage-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tagged_only": {
      "description": "Only list logical volumes tagged with 'pve-vm-ID'.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "username": {
      "description": "RBD Id.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "zfs-base-path": {
      "description": "Base path where to look for the created ZFS block devices. Set automatically during creation if not specified. Usually '/dev/zvol'.",
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
      "description": "Partial, possibly server generated, configuration properties.",
      "optional": 1,
      "properties": {
        "encryption-key": {
          "description": "The, possibly auto-generated, encryption-key.",
          "optional": 1,
          "type": "string"
        }
      },
      "type": "object"
    },
    "storage": {
      "description": "The ID of the created storage.",
      "type": "string"
    },
    "type": {
      "description": "The type of the created storage.",
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
