# `/nodes/{node}/qemu/{vmid}/mtunnelwebsocket`

原始接口路径：`/nodes/{node}/qemu/{vmid}/mtunnelwebsocket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/mtunnelwebsocket`

用于 websocket 升级的迁移隧道端点——仅供虚拟机迁移内部使用。

**方法标识：** `mtunnelwebsocket`

**权限**

```json
{
  "description": "需要传入对所选套接字有效的票据。可通过 mtunnel API 调用创建票据，该调用会相应检查权限。",
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
| `node` | string | 是 | — | 集群节点名称。 |
| `socket` | string | 是 | — | 要转发到的 UNIX 套接字 |
| `ticket` | string | 是 | — | 初始 'mtunnel' API 调用返回的票据，或通过 'ticket' 隧道命令获取的票据 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "socket": {
      "description": "要转发到的 UNIX 套接字",
      "type": "string",
      "typetext": "<string>"
    },
    "ticket": {
      "description": "初始 'mtunnel' API 调用返回的票据，或通过 'ticket' 隧道命令获取的票据",
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
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
