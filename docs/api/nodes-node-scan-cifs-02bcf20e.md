# `/nodes/{node}/scan/cifs`

原始接口路径：`/nodes/{node}/scan/cifs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/cifs`

Scan remote CIFS server.

**方法标识：** `cifsscan`

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
| `domain` | string | 否 | — | SMB domain (Workgroup). |
| `node` | string | 是 | — | The cluster node name. |
| `password` | string | 否 | — | User password. |
| `server` | string | 是 | — | The server address (name or IP). |
| `username` | string | 否 | — | User name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "domain": {
      "description": "SMB domain (Workgroup).",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "User password.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "server": {
      "description": "The server address (name or IP).",
      "format": "pve-storage-server",
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "User name.",
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
  "items": {
    "properties": {
      "description": {
        "description": "Descriptive text from server.",
        "type": "string"
      },
      "share": {
        "description": "The cifs share name.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/cifs)。
