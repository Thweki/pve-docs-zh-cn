# `/nodes/{node}/scan/pbs`

原始接口路径：`/nodes/{node}/scan/pbs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/pbs`

扫描远程 Proxmox Backup Server。

**方法标识：** `pbsscan`

**权限**

```json
{
  "check": [
    "perm",
    "/storage",
    [
      "Datastore.Allocate"
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
| `fingerprint` | string | 否 | — | 证书 SHA 256 指纹。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `password` | string | 是 | — | 用户密码或 API 令牌密钥。 |
| `port` | integer | 否 | 8007 | 可选端口。 |
| `server` | string | 是 | — | 服务器地址（名称或 IP）。 |
| `username` | string | 是 | — | 用户名或 API 令牌 ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {
      "description": "证书 SHA 256 指纹。",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "用户密码或 API 令牌密钥。",
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "default": 8007,
      "description": "可选端口。",
      "maximum": 65535,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65535)"
    },
    "server": {
      "description": "服务器地址（名称或 IP）。",
      "format": "pve-storage-server",
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "用户名或 API 令牌 ID。",
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
  "items": {
    "properties": {
      "comment": {
        "description": "服务器提供的注释。",
        "optional": 1,
        "type": "string"
      },
      "store": {
        "description": "数据存储名称。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/pbs)。
