# `/nodes/{node}/disks/list`

原始接口路径：`/nodes/{node}/disks/list`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/list`

List local disks.

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
| `include-partitions` | boolean | 否 | 0 | Also include partitions. |
| `node` | string | 是 | — | The cluster node name. |
| `skipsmart` | boolean | 否 | 0 | Skip smart checks. |
| `type` | string | 否 | — | Only list specific types of disks.；可选值：`unused`, `journal_disks` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "include-partitions": {
      "default": 0,
      "description": "Also include partitions.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "skipsmart": {
      "default": 0,
      "description": "Skip smart checks.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "type": {
      "description": "Only list specific types of disks.",
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
        "description": "The device path",
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
        "description": "For partitions only. The device path of the disk the partition resides on.",
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
