# `/nodes/{node}/storage/{storage}/prunebackups`

原始接口路径：`/nodes/{node}/storage/{storage}/prunebackups`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/storage/{storage}/prunebackups`

Prune backups. Only those using the standard naming scheme are considered.

**方法标识：** `delete`

**权限**

```json
{
  "description": "You need the 'Datastore.Allocate' privilege on the storage (or if a VM ID is specified, 'Datastore.AllocateSpace' and 'VM.Backup' for the VM).",
  "user": "all"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `prune-backups` | string | 否 | — | Use these retention options instead of those from the storage configuration. |
| `storage` | string | 是 | — | The storage identifier. |
| `type` | string | 否 | — | Either 'qemu' or 'lxc'. Only consider backups for guests of this type.；可选值：`qemu`, `lxc` |
| `vmid` | integer | 否 | — | Only prune backups for this VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "prune-backups": {
      "description": "Use these retention options instead of those from the storage configuration.",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "type": {
      "description": "Either 'qemu' or 'lxc'. Only consider backups for guests of this type.",
      "enum": [
        "qemu",
        "lxc"
      ],
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "Only prune backups for this VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

## GET `/nodes/{node}/storage/{storage}/prunebackups`

Get prune information for backups. NOTE: this is only a preview and might not be what a subsequent prune call does if backups are removed/added in the meantime.

**方法标识：** `dryrun`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.Audit",
      "Datastore.AllocateSpace"
    ],
    "any",
    1
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `prune-backups` | string | 否 | — | Use these retention options instead of those from the storage configuration. |
| `storage` | string | 是 | — | The storage identifier. |
| `type` | string | 否 | — | Either 'qemu' or 'lxc'. Only consider backups for guests of this type.；可选值：`qemu`, `lxc` |
| `vmid` | integer | 否 | — | Only consider backups for this guest. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "prune-backups": {
      "description": "Use these retention options instead of those from the storage configuration.",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "type": {
      "description": "Either 'qemu' or 'lxc'. Only consider backups for guests of this type.",
      "enum": [
        "qemu",
        "lxc"
      ],
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "Only consider backups for this guest.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "properties": {
      "ctime": {
        "description": "Creation time of the backup (seconds since the UNIX epoch).",
        "type": "integer"
      },
      "mark": {
        "description": "Whether the backup would be kept or removed. Backups that are protected or don't use the standard naming scheme are not removed.",
        "enum": [
          "keep",
          "remove",
          "protected",
          "renamed"
        ],
        "type": "string"
      },
      "type": {
        "description": "One of 'qemu', 'lxc', 'openvz' or 'unknown'.",
        "type": "string"
      },
      "vmid": {
        "description": "The VM the backup belongs to.",
        "optional": 1,
        "type": "integer"
      },
      "volid": {
        "description": "Backup volume ID.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/prunebackups)。
