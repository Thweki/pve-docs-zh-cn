# `/nodes/{node}/storage`

原始接口路径：`/nodes/{node}/storage`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage`

获取所有数据存储的状态。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/storage/<storage>' 具有 'Datastore.Audit' 或 'Datastore.AllocateSpace' 权限的条目",
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
| `content` | string | 否 | — | 仅列出支持此内容类型的存储。 |
| `enabled` | boolean | 否 | 0 | 仅列出已启用的存储（在配置中未禁用）。 |
| `format` | boolean | 否 | 0 | 包含格式信息 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 否 | — | 仅列出  指定存储的状态 |
| `target` | string | 否 | — | 如果 target 与 'node' 不同，则仅列出内容可同时在此 'node' 和指定 'target' 节点上访问的共享存储。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "content": {
      "description": "仅列出支持此内容类型的存储。",
      "format": "pve-storage-content-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enabled": {
      "default": 0,
      "description": "仅列出已启用的存储（在配置中未禁用）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "format": {
      "default": 0,
      "description": "包含格式信息",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "仅列出  指定存储的状态",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "target": {
      "description": "如果 target 与 'node' 不同，则仅列出内容可同时在此 'node' 和指定 'target' 节点上访问的共享存储。",
      "format": "pve-node",
      "optional": 1,
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
      "formats": {
        "description": "列出支持的格式和默认格式。请改用 'formats'。仅在设置了 'format' 参数时包含。",
        "optional": 1,
        "properties": {
          "default": {
            "description": "存储的默认格式。",
            "enum": [
              "qcow2",
              "raw",
              "subvol",
              "vmdk"
            ],
            "type": "string"
          },
          "supported": {
            "description": "支持的格式列表",
            "items": {
              "enum": [
                "qcow2",
                "raw",
                "subvol",
                "vmdk"
              ],
              "type": "string"
            },
            "type": "array"
          }
        },
        "type": "object"
      },
      "select_existing": {
        "description": "必须选择已有卷，而非创建新卷。仅在设置了 'format' 参数时包含。",
        "optional": 1,
        "type": "boolean"
      },
      "shared": {
        "description": "存储配置中的 shared 标志。",
        "optional": 1,
        "type": "boolean"
      },
      "storage": {
        "description": "存储标识符。",
        "format": "pve-storage-id",
        "format_description": "storage ID",
        "type": "string"
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
      },
      "used_fraction": {
        "description": "已用比例（used/total）。",
        "optional": 1,
        "renderer": "fraction_as_percentage",
        "type": "number"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{storage}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage)。
