# `/nodes/{node}/vncshell`

原始接口路径：`/nodes/{node}/vncshell`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/vncshell`

创建 VNC Shell 代理。

**方法标识：** `vncshell`

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
| `cmd` | string | 否 | "login" | 运行特定命令，默认为 login（需要 'root@pam'）；可选值：`ceph_install`, `login`, `upgrade` |
| `cmd-opts` | string | 否 | "" | 向命令添加参数。编码为以空字符结尾的字符串。 |
| `height` | integer | 否 | — | 设置控制台高度，单位为像素。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `websocket` | boolean | 否 | — | 使用 websocket 代替标准 VNC。 |
| `width` | integer | 否 | — | 设置控制台宽度，单位为像素。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cmd": {
      "default": "login",
      "description": "运行特定命令，默认为 login（需要 'root@pam'）",
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
      "description": "向命令添加参数。编码为以空字符结尾的字符串。",
      "optional": 1,
      "requires": "cmd",
      "type": "string",
      "typetext": "<string>"
    },
    "height": {
      "description": "设置控制台高度，单位为像素。",
      "maximum": 2160,
      "minimum": 16,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (16 - 2160)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "websocket": {
      "description": "使用 websocket 代替标准 VNC。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "width": {
      "description": "设置控制台宽度，单位为像素。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/vncshell)。
