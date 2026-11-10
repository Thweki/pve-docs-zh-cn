# `/nodes/{node}/disks/lvmthin`

原始接口路径：`/nodes/{node}/disks/lvmthin`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/lvmthin`

List LVM thinpools

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
| `node` | string | 是 | — | The cluster node name. |

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
      "lv": {
        "description": "The name of the thinpool.",
        "type": "string"
      },
      "lv_size": {
        "description": "The size of the thinpool in bytes.",
        "type": "integer"
      },
      "metadata_size": {
        "description": "The size of the metadata lv in bytes.",
        "type": "integer"
      },
      "metadata_used": {
        "description": "The used bytes of the metadata lv.",
        "type": "integer"
      },
      "used": {
        "description": "The used bytes of the thinpool.",
        "type": "integer"
      },
      "vg": {
        "description": "The associated volume group.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

## POST `/nodes/{node}/disks/lvmthin`

Create an LVM thinpool

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
  "description": "Requires additionally 'Datastore.Allocate' on /storage when setting 'add_storage'"
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
| `add_storage` | boolean | 否 | 0 | Configure storage using the thinpool. |
| `device` | string | 是 | — | The block device you want to create the thinpool on. |
| `name` | string | 是 | — | The storage identifier. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storage": {
      "default": 0,
      "description": "Configure storage using the thinpool.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "device": {
      "description": "The block device you want to create the thinpool on.",
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/lvmthin)。
