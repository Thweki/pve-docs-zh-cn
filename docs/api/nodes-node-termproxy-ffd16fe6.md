# `/nodes/{node}/termproxy`

原始接口路径：`/nodes/{node}/termproxy`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/termproxy`

Creates a VNC Shell proxy.

**方法标识：** `termproxy`

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
| `node` | string | 是 | — | The cluster node name. |

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
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
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
  "additionalProperties": 0,
  "properties": {
    "port": {
      "description": "port used to bind termproxy to.",
      "type": "integer"
    },
    "ticket": {
      "description": "VNC ticket used to verify websocket connection.",
      "type": "string"
    },
    "upid": {
      "description": "UPID for termproxy worker task.",
      "type": "string"
    },
    "user": {
      "description": "user/token that generated the VNC ticket in `ticket`.",
      "type": "string"
    }
  }
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/termproxy)。
