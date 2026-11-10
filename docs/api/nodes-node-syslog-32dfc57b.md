# `/nodes/{node}/syslog`

原始接口路径：`/nodes/{node}/syslog`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/syslog`

Read system log

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
| `node` | string | 是 | — | The cluster node name. |
| `service` | string | 否 | — | Service ID |
| `since` | string | 否 | — | Display all log since this date-time string. |
| `start` | integer | 否 | — |  |
| `until` | string | 否 | — | Display all log until this date-time string. |

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
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "service": {
      "description": "Service ID",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "since": {
      "description": "Display all log since this date-time string.",
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
      "description": "Display all log until this date-time string.",
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
        "description": "Line number",
        "type": "integer"
      },
      "t": {
        "description": "Line text",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/syslog)。
