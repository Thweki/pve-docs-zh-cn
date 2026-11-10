# `/nodes/{node}/vncshell`

原始接口路径：`/nodes/{node}/vncshell`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/vncshell`

Creates a VNC Shell proxy.

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Console"
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
| `cmd` | string | 否 | "login" | Run specific command or default to login (requires 'root@pam')；可选值：`ceph_install`, `login`, `upgrade` |
| `cmd-opts` | string | 否 | "" | Add parameters to a command. Encoded as null terminated strings. |
| `height` | integer | 否 | — | sets the height of the console in pixels. |
| `node` | string | 是 | — | The cluster node name. |
| `websocket` | boolean | 否 | — | use websocket instead of standard vnc. |
| `width` | integer | 否 | — | sets the width of the console in pixels. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cmd": {
      "default": "login",
      "description": "Run specific command or default to login (requires 'root@pam')",
      "enum": [
        "ceph_install",
        "login",
        "upgrade"
      ],
      "optional": 1,
      "type": "string"
    },
    "cmd-opts": {
      "default": "",
      "description": "Add parameters to a command. Encoded as null terminated strings.",
      "optional": 1,
      "requires": "cmd",
      "type": "string",
      "typetext": "<string>"
    },
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
    "websocket": {
      "description": "use websocket instead of standard vnc.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/vncshell)。
