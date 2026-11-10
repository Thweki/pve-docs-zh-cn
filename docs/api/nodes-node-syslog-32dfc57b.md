# `/nodes/{node}/syslog`

原始接口路径：`/nodes/{node}/syslog`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/syslog`

读取系统日志

**方法标识：** `syslog`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Syslog"
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
| `limit` | integer | 否 | — |  |
| `node` | string | 是 | — | 集群节点名称。 |
| `service` | string | 否 | — | 服务 ID |
| `since` | string | 否 | — | 显示从此日期时间字符串开始的所有日志。 |
| `start` | integer | 否 | — |  |
| `until` | string | 否 | — | 显示截至此日期时间字符串的所有日志。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "limit": {
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "service": {
      "description": "服务 ID",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "since": {
      "description": "显示从此日期时间字符串开始的所有日志。",
      "optional": 1,
      "pattern": "^\\d{4}-\\d{2}-\\d{2}( \\d{2}:\\d{2}(:\\d{2})?)?$",
      "type": "string"
    },
    "start": {
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "until": {
      "description": "显示截至此日期时间字符串的所有日志。",
      "optional": 1,
      "pattern": "^\\d{4}-\\d{2}-\\d{2}( \\d{2}:\\d{2}(:\\d{2})?)?$",
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
      "n": {
        "description": "行号",
        "type": "integer"
      },
      "t": {
        "description": "行文本",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/syslog)。
