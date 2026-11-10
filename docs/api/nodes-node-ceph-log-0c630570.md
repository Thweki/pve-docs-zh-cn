# `/nodes/{node}/ceph/log`

原始接口路径：`/nodes/{node}/ceph/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/log`

读取 ceph 日志

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
| `limit` | integer | 否 | — | 返回日志行的最大数量。省略时默认为 dump_logfile 的限制（通常为 50）。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `start` | integer | 否 | — | 返回的首个日志行的偏移量（从 0 开始）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "limit": {
      "description": "返回日志行的最大数量。省略时默认为 dump_logfile 的限制（通常为 50）。",
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
    "start": {
      "description": "返回的首个日志行的偏移量（从 0 开始）。",
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
        "description": "日志文件行号（从 1 开始）。",
        "type": "integer"
      },
      "t": {
        "description": "日志行文本。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/log)。
