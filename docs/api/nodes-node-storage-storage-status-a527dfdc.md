# `/nodes/{node}/storage/{storage}/status`

原始接口路径：`/nodes/{node}/storage/{storage}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/status`

读取存储状态。

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
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |

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
  "properties": {
    "active": {
      "description": "存储可访问时设置。",
      "optional": 1,
      "type": "boolean"
    },
    "avail": {
      "description": "可用存储空间，单位为字节。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "content": {
      "description": "允许的存储内容类型。",
      "format": "pve-storage-content-list",
      "type": "string"
    },
    "enabled": {
      "description": "存储已启用（未禁用）时设置。",
      "optional": 1,
      "type": "boolean"
    },
    "shared": {
      "description": "存储配置中的 shared 标志。",
      "optional": 1,
      "type": "boolean"
    },
    "total": {
      "description": "总存储空间，单位为字节。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "type": {
      "description": "存储类型。",
      "type": "string"
    },
    "used": {
      "description": "已用存储空间，单位为字节。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/status)。
