# `/nodes/{node}/storage/{storage}/prunebackups`

原始接口路径：`/nodes/{node}/storage/{storage}/prunebackups`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/storage/{storage}/prunebackups`

清理备份。仅考虑采用标准命名方案的备份。

**方法标识：** `delete`

**权限**

```json
{
  "description": "需要对存储具有 'Datastore.Allocate' 权限（若指定了虚拟机 ID，则需 'Datastore.AllocateSpace' 权限以及该虚拟机的 'VM.Backup' 权限）。",
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
| `node` | string | 是 | — | 集群节点名称。 |
| `prune-backups` | string | 否 | — | 使用这些保留选项，而非存储配置中的选项。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `type` | string | 否 | — | 'qemu' 或 'lxc'。仅考虑此类型客户机的备份。；可选值：`qemu`, `lxc` |
| `vmid` | integer | 否 | — | 仅清理此虚拟机的备份。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "prune-backups": {
      "description": "使用这些保留选项，而非存储配置中的选项。",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "type": {
      "description": "'qemu' 或 'lxc'。仅考虑此类型客户机的备份。",
      "enum": [
        "qemu",
        "lxc"
      ],
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "仅清理此虚拟机的备份。",
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

获取备份清理信息。注意：这只是预览，如果期间移除/添加了备份，则后续清理调用的实际操作可能与预览不同。

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
| `node` | string | 是 | — | 集群节点名称。 |
| `prune-backups` | string | 否 | — | 使用这些保留选项，而非存储配置中的选项。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `type` | string | 否 | — | 'qemu' 或 'lxc'。仅考虑此类型客户机的备份。；可选值：`qemu`, `lxc` |
| `vmid` | integer | 否 | — | 仅考虑此客户机的备份。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "prune-backups": {
      "description": "使用这些保留选项，而非存储配置中的选项。",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "type": {
      "description": "'qemu' 或 'lxc'。仅考虑此类型客户机的备份。",
      "enum": [
        "qemu",
        "lxc"
      ],
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "仅考虑此客户机的备份。",
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
        "description": "备份创建时间（自 UNIX 纪元起的秒数）。",
        "type": "integer"
      },
      "mark": {
        "description": "备份将被保留还是移除。受保护或不采用标准命名方案的备份不会被移除。",
        "enum": [
          "keep",
          "remove",
          "protected",
          "renamed"
        ],
        "type": "string"
      },
      "type": {
        "description": "'qemu'、'lxc'、'openvz' 或 'unknown' 之一。",
        "type": "string"
      },
      "vmid": {
        "description": "备份所属的虚拟机。",
        "optional": 1,
        "type": "integer"
      },
      "volid": {
        "description": "备份卷 ID。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/prunebackups)。
