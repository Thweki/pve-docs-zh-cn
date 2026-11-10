# `/nodes/{node}/scan/cifs`

原始接口路径：`/nodes/{node}/scan/cifs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/cifs`

扫描远程 CIFS 服务器。

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
| `domain` | string | 否 | — | SMB 域（工作组）。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `password` | string | 否 | — | 用户密码。 |
| `server` | string | 是 | — | 服务器地址（名称或 IP）。 |
| `username` | string | 否 | — | 用户名。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "domain": {
      "description": "SMB 域（工作组）。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "用户密码。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "server": {
      "description": "服务器地址（名称或 IP）。",
      "format": "pve-storage-server",
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "用户名。",
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
        "description": "服务器提供的描述文本。",
        "type": "string"
      },
      "share": {
        "description": "CIFS 共享名称。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/cifs)。
