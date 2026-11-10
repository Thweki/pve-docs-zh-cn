# `/nodes/{node}/firewall/log`

原始接口路径：`/nodes/{node}/firewall/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/firewall/log`

读取防火墙日志

**方法标识：** `log`

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
| `since` | integer | 否 | — | 显示从此 UNIX 时间戳开始的日志。 |
| `start` | integer | 否 | — |  |
| `until` | integer | 否 | — | 显示截至此 UNIX 时间戳的日志。 |

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
    "since": {
      "description": "显示从此 UNIX 时间戳开始的日志。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "start": {
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "until": {
      "description": "显示截至此 UNIX 时间戳的日志。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/firewall/log)。
