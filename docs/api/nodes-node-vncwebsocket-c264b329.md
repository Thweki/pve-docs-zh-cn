# `/nodes/{node}/vncwebsocket`

原始接口路径：`/nodes/{node}/vncwebsocket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/vncwebsocket`

Opens a websocket for VNC traffic.

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Console"
    ]
  ],
  "description": "You also need to pass a valid ticket (vncticket)."
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `port` | integer | 是 | — | Port number returned by previous 'vncshell' call. |
| `vncticket` | string | 是 | — | Ticket from previous call to 'vncshell'. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "Port number returned by previous 'vncshell' call.",
      "maximum": 5999,
      "minimum": 5900,
      "type": "integer",
      "typetext": "<integer> (5900 - 5999)"
    },
    "vncticket": {
      "description": "Ticket from previous call to 'vncshell'.",
      "maxLength": 512,
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
    "port": {
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/vncwebsocket)。
