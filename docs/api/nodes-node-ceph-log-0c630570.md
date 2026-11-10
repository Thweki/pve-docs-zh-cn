# `/nodes/{node}/ceph/log`

原始接口路径：`/nodes/{node}/ceph/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/log`

Read ceph log

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
| `limit` | integer | 否 | — | Maximum number of log lines to return. Defaults to the dump_logfile limit (typically 50) when omitted. |
| `node` | string | 是 | — | The cluster node name. |
| `start` | integer | 否 | — | Offset of the first log line to return (0-based). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "limit": {
      "description": "Maximum number of log lines to return. Defaults to the dump_logfile limit (typically 50) when omitted.",
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
    "start": {
      "description": "Offset of the first log line to return (0-based).",
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
        "description": "Log-file line number (1-based).",
        "type": "integer"
      },
      "t": {
        "description": "Log line text.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/log)。
