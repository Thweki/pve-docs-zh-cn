# `/nodes/{node}/spiceshell`

原始接口路径：`/nodes/{node}/spiceshell`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/spiceshell`

创建 SPICE shell。

**方法标识：** `spiceshell`

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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `cmd` | string | 否 | "login" | 运行特定命令，默认为 login（需要 'root@pam'）；可选值：`ceph_install`, `login`, `upgrade` |
| `cmd-opts` | string | 否 | "" | 向命令添加参数。编码为以空字符结尾的字符串。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `proxy` | string | 否 | — | SPICE 代理服务器。客户端可用此项指定代理服务器。集群中所有节点均运行 'spiceproxy'，因此由客户端选择使用哪个。默认返回虚拟机当前运行所在的节点。一种合理设置是使用连接 API 时所用的同一节点（在 JS GUI 中即 window.location.hostname）。 |

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
    },
    "proxy": {
      "description": "SPICE 代理服务器。客户端可用此项指定代理服务器。集群中所有节点均运行 'spiceproxy'，因此由客户端选择使用哪个。默认返回虚拟机当前运行所在的节点。一种合理设置是使用连接 API 时所用的同一节点（在 JS GUI 中即 window.location.hostname）。",
      "format": "address",
      "optional": 1,
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
  "additionalProperties": 1,
  "description": "返回值可直接传递给 'remote-viewer' 应用程序。",
  "properties": {
    "host": {
      "type": "string"
    },
    "password": {
      "type": "string"
    },
    "proxy": {
      "type": "string"
    },
    "tls-port": {
      "type": "integer"
    },
    "type": {
      "type": "string"
    }
  }
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/spiceshell)。
