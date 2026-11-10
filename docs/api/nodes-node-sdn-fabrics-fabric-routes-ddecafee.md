# `/nodes/{node}/sdn/fabrics/{fabric}/routes`

原始接口路径：`/nodes/{node}/sdn/fabrics/{fabric}/routes`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/fabrics/{fabric}/routes`

获取 fabric 的所有路由。

**方法标识：** `routes`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/fabrics/{fabric}",
    [
      "SDN.Audit"
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
| `fabric` | string | 是 | — | SDN fabric 的标识符 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fabric": {
      "description": "SDN fabric 的标识符",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
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
  "items": {
    "properties": {
      "route": {
        "description": "此路由表条目的 CIDR 块。",
        "type": "string"
      },
      "via": {
        "description": "此路由的下一跳列表。",
        "items": {
          "description": "下一跳的 IP 地址。",
          "type": "string"
        },
        "type": "array"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/fabrics/{fabric}/routes)。
