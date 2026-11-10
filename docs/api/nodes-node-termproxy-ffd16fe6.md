# `/nodes/{node}/termproxy`

原始接口路径：`/nodes/{node}/termproxy`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/termproxy`

创建 VNC Shell 代理。

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
| `cmd` | string | 否 | "login" | 运行特定命令，默认为 login（需要 'root@pam'）；可选值：`ceph_install`, `login`, `upgrade` |
| `cmd-opts` | string | 否 | "" | 向命令添加参数。编码为以空字符结尾的字符串。 |
| `node` | string | 是 | — | 集群节点名称。 |

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
    "node": {
      "description": "集群节点名称。",
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
      "description": "termproxy 绑定的端口。",
      "type": "integer"
    },
    "ticket": {
      "description": "用于验证 websocket 连接的 VNC 票据。",
      "type": "string"
    },
    "upid": {
      "description": "termproxy 工作任务的 UPID。",
      "type": "string"
    },
    "user": {
      "description": "在 `ticket` 中生成 VNC 票据的用户/令牌。",
      "type": "string"
    }
  }
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/termproxy)。
