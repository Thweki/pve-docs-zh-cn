# `/nodes/{node}/disks/list`

原始接口路径：`/nodes/{node}/disks/list`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/list`

列出本地磁盘。

**方法标识：** `list`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/",
      [
        "Sys.Audit"
      ]
    ],
    [
      "perm",
      "/nodes/{node}",
      [
        "Sys.Audit"
      ]
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
| `include-partitions` | boolean | 否 | 0 | 同时包含分区。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `skipsmart` | boolean | 否 | 0 | 跳过 SMART 检查。 |
| `type` | string | 否 | — | 仅列出指定类型的磁盘。；可选值：`unused`, `journal_disks` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "include-partitions": {
      "default": 0,
      "description": "同时包含分区。",
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
    "skipsmart": {
      "default": 0,
      "description": "跳过 SMART 检查。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "type": {
      "description": "仅列出指定类型的磁盘。",
      "enum": [
        "unused",
        "journal_disks"
      ],
      "optional": 1,
      "type": "string"
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
      "devpath": {
        "description": "设备路径",
        "type": "string"
      },
      "gpt": {
        "type": "boolean"
      },
      "health": {
        "optional": 1,
        "type": "string"
      },
      "model": {
        "optional": 1,
        "type": "string"
      },
      "mounted": {
        "type": "boolean"
      },
      "osdid": {
        "type": "integer"
      },
      "osdid-list": {
        "items": {
          "type": "integer"
        },
        "type": "array"
      },
      "parent": {
        "description": "仅适用于分区。分区所在磁盘的设备路径。",
        "optional": 1,
        "type": "string"
      },
      "serial": {
        "optional": 1,
        "type": "string"
      },
      "size": {
        "type": "integer"
      },
      "used": {
        "optional": 1,
        "type": "string"
      },
      "vendor": {
        "optional": 1,
        "type": "string"
      },
      "wwn": {
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/list)。
