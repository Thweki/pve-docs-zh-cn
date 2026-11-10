# `/nodes/{node}/qemu/{vmid}/mtunnelwebsocket`

原始接口路径：`/nodes/{node}/qemu/{vmid}/mtunnelwebsocket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/mtunnelwebsocket`

Migration tunnel endpoint for websocket upgrade - only for internal use by VM migration.

**方法标识：** `mtunnelwebsocket`

**权限**

```json
{
  "description": "You need to pass a ticket valid for the selected socket. Tickets can be created via the mtunnel API call, which will check permissions accordingly.",
  "user": "all"
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
| `socket` | string | 是 | — | unix socket to forward to |
| `ticket` | string | 是 | — | ticket return by initial 'mtunnel' API call, or retrieved via 'ticket' tunnel command |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

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
    "socket": {
      "description": "unix socket to forward to",
      "type": "string",
      "typetext": "<string>"
    },
    "ticket": {
      "description": "ticket return by initial 'mtunnel' API call, or retrieved via 'ticket' tunnel command",
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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
      "optional": 1,
      "type": "string"
    },
    "socket": {
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/mtunnelwebsocket)。
