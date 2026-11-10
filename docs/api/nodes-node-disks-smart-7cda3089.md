# `/nodes/{node}/disks/smart`

原始接口路径：`/nodes/{node}/disks/smart`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/smart`

Get SMART Health of a disk.

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
| `disk` | string | 是 | — | Block device name |
| `healthonly` | boolean | 否 | — | If true returns only the health status |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "disk": {
      "description": "Block device name",
      "pattern": "^/dev/[a-zA-Z0-9\\/]+$",
      "type": "string"
    },
    "healthonly": {
      "description": "If true returns only the health status",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "attributes": {
      "optional": 1,
      "type": "array"
    },
    "health": {
      "type": "string"
    },
    "text": {
      "optional": 1,
      "type": "string"
    },
    "type": {
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/smart)。
