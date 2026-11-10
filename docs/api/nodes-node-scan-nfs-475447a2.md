# `/nodes/{node}/scan/nfs`

原始接口路径：`/nodes/{node}/scan/nfs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/nfs`

扫描远程 NFS 服务器。

**方法标识：** `nfsscan`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `server` | string | 是 | — | 服务器地址（名称或 IP）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "server": {
      "description": "服务器地址（名称或 IP）。",
      "format": "pve-storage-server",
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
      "options": {
        "description": "NFS 导出选项。",
        "type": "string"
      },
      "path": {
        "description": "导出的路径。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/nfs)。
