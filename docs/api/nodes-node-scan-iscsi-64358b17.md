# `/nodes/{node}/scan/iscsi`

原始接口路径：`/nodes/{node}/scan/iscsi`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/iscsi`

Scan remote iSCSI server.

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
| `node` | string | 是 | — | The cluster node name. |
| `portal` | string | 是 | — | The iSCSI portal (IP or DNS name with optional port). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "portal": {
      "description": "The iSCSI portal (IP or DNS name with optional port).",
      "format": "pve-storage-portal-dns",
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
      "portal": {
        "description": "The iSCSI portal name.",
        "type": "string"
      },
      "target": {
        "description": "The iSCSI target name.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/iscsi)。
