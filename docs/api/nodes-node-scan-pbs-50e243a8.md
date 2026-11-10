# `/nodes/{node}/scan/pbs`

原始接口路径：`/nodes/{node}/scan/pbs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/pbs`

Scan remote Proxmox Backup Server.

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
| `fingerprint` | string | 否 | — | Certificate SHA 256 fingerprint. |
| `node` | string | 是 | — | The cluster node name. |
| `password` | string | 是 | — | User password or API token secret. |
| `port` | integer | 否 | 8007 | Optional port. |
| `server` | string | 是 | — | The server address (name or IP). |
| `username` | string | 是 | — | User-name or API token-ID. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {
      "description": "Certificate SHA 256 fingerprint.",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "User password or API token secret.",
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "default": 8007,
      "description": "Optional port.",
      "maximum": 65535,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65535)"
    },
    "server": {
      "description": "The server address (name or IP).",
      "format": "pve-storage-server",
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "User-name or API token-ID.",
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
        "description": "Comment from server.",
        "optional": 1,
        "type": "string"
      },
      "store": {
        "description": "The datastore name.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/pbs)。
