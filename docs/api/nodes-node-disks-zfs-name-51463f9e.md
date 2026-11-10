# `/nodes/{node}/disks/zfs/{name}`

原始接口路径：`/nodes/{node}/disks/zfs/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/disks/zfs/{name}`

Destroy a ZFS pool.

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
  ],
  "description": "Requires additionally 'Datastore.Allocate' on /storage when setting 'cleanup-config'"
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
| `cleanup-config` | boolean | 否 | 0 | Marks associated storage(s) as not available on this node anymore or removes them from the configuration (if configured for this node only). |
| `cleanup-disks` | boolean | 否 | 0 | Also wipe disks so they can be repurposed afterwards. |
| `name` | string | 是 | — | The storage identifier. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cleanup-config": {
      "default": 0,
      "description": "Marks associated storage(s) as not available on this node anymore or removes them from the configuration (if configured for this node only).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cleanup-disks": {
      "default": 0,
      "description": "Also wipe disks so they can be repurposed afterwards.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
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

## GET `/nodes/{node}/disks/zfs/{name}`

Get details about a zpool.

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | string | 是 | — | The storage identifier. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "action": {
      "description": "Information about the recommended action to fix the state.",
      "optional": 1,
      "type": "string"
    },
    "children": {
      "description": "The pool configuration information, including the vdevs for each section (e.g. spares, cache), may be nested.",
      "items": {
        "properties": {
          "cksum": {
            "optional": 1,
            "type": "number"
          },
          "msg": {
            "description": "An optional message about the vdev.",
            "type": "string"
          },
          "name": {
            "description": "The name of the vdev or section.",
            "type": "string"
          },
          "read": {
            "optional": 1,
            "type": "number"
          },
          "state": {
            "description": "The state of the vdev.",
            "optional": 1,
            "type": "string"
          },
          "write": {
            "optional": 1,
            "type": "number"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "errors": {
      "description": "Information about the errors on the zpool.",
      "type": "string"
    },
    "name": {
      "description": "The name of the zpool.",
      "type": "string"
    },
    "scan": {
      "description": "Information about the last/current scrub.",
      "optional": 1,
      "type": "string"
    },
    "state": {
      "description": "The state of the zpool.",
      "type": "string"
    },
    "status": {
      "description": "Information about the state of the zpool.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/zfs/{name})。
