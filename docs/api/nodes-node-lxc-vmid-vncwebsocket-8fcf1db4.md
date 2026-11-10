# `/nodes/{node}/lxc/{vmid}/vncwebsocket`

原始接口路径：`/nodes/{node}/lxc/{vmid}/vncwebsocket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/vncwebsocket`

为 VNC 流量打开 websocket。

**方法标识：** `vncwebsocket`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Console"
    ]
  ],
  "description": "还需要传入有效票据（vncticket）。"
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
| `port` | integer | 是 | — | 上次 vncproxy 调用返回的端口号。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |
| `vncticket` | string | 是 | — | 上次 vncproxy 调用的票据。 |

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
    "port": {
      "description": "上次 vncproxy 调用返回的端口号。",
      "maximum": 5999,
      "minimum": 5900,
      "type": "integer",
      "typetext": "<integer> (5900 - 5999)"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "vncticket": {
      "description": "上次 vncproxy 调用的票据。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/vncwebsocket)。
