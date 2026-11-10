# `/nodes/{node}/qemu/{vmid}/vncproxy`

原始接口路径：`/nodes/{node}/qemu/{vmid}/vncproxy`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/vncproxy`

创建 TCP VNC 代理连接。

**方法标识：** `vncproxy`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Console"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `generate-password` | boolean | 否 | 0 | 已弃用，请勿使用。需要时会生成密码。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |
| `websocket` | boolean | 否 | — | 准备 websocket 升级（仅使用串行终端时需要，否则始终可升级）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "generate-password": {
      "default": 0,
      "description": "已弃用，请勿使用。需要时会生成密码。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
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
    },
    "websocket": {
      "description": "准备 websocket 升级（仅使用串行终端时需要，否则始终可升级）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "additionalProperties": 0,
  "properties": {
    "cert": {
      "type": "string"
    },
    "password": {
      "description": "VNC 协议中用于身份验证的密码。由可打印 ASCII 字符（'!' .. '~'）组成。",
      "optional": 1,
      "type": "string"
    },
    "port": {
      "type": "integer"
    },
    "ticket": {
      "type": "string"
    },
    "upid": {
      "type": "string"
    },
    "user": {
      "type": "string"
    }
  }
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/vncproxy)。
