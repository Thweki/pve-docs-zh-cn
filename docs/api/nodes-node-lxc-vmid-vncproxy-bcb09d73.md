# `/nodes/{node}/lxc/{vmid}/vncproxy`

原始接口路径：`/nodes/{node}/lxc/{vmid}/vncproxy`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/lxc/{vmid}/vncproxy`

Creates a TCP VNC proxy connections.

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
| `height` | integer | 否 | — | sets the height of the console in pixels. |
| `node` | string | 是 | — | The cluster node name. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |
| `websocket` | boolean | 否 | — | use websocket instead of standard VNC. |
| `width` | integer | 否 | — | sets the width of the console in pixels. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "height": {
      "description": "sets the height of the console in pixels.",
      "maximum": 2160,
      "minimum": 16,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (16 - 2160)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
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
    },
    "websocket": {
      "description": "use websocket instead of standard VNC.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "width": {
      "description": "sets the width of the console in pixels.",
      "maximum": 4096,
      "minimum": 16,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (16 - 4096)"
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
      "description": "Password used for authentication within the VNC protocol. Consists of printable ASCII characters ('!' .. '~').",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/vncproxy)。
