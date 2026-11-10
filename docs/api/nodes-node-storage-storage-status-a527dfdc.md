# `/nodes/{node}/storage/{storage}/status`

原始接口路径：`/nodes/{node}/storage/{storage}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/status`

Read storage status.

**方法标识：** `read_status`

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
| `storage` | string | 是 | — | The storage identifier. |

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
  "properties": {
    "active": {
      "description": "Set when storage is accessible.",
      "optional": 1,
      "type": "boolean"
    },
    "avail": {
      "description": "Available storage space in bytes.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "content": {
      "description": "Allowed storage content types.",
      "format": "pve-storage-content-list",
      "type": "string"
    },
    "enabled": {
      "description": "Set when storage is enabled (not disabled).",
      "optional": 1,
      "type": "boolean"
    },
    "shared": {
      "description": "Shared flag from storage configuration.",
      "optional": 1,
      "type": "boolean"
    },
    "total": {
      "description": "Total storage space in bytes.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "type": {
      "description": "Storage type.",
      "type": "string"
    },
    "used": {
      "description": "Used storage space in bytes.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/status)。
