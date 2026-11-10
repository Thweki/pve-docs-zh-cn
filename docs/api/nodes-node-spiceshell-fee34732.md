# `/nodes/{node}/spiceshell`

原始接口路径：`/nodes/{node}/spiceshell`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/spiceshell`

Creates a SPICE shell.

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
| `cmd` | string | 否 | "login" | Run specific command or default to login (requires 'root@pam')；可选值：`ceph_install`, `login`, `upgrade` |
| `cmd-opts` | string | 否 | "" | Add parameters to a command. Encoded as null terminated strings. |
| `node` | string | 是 | — | The cluster node name. |
| `proxy` | string | 否 | — | SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI). |

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
    },
    "proxy": {
      "description": "SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI).",
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
  "description": "Returned values can be directly passed to the 'remote-viewer' application.",
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
