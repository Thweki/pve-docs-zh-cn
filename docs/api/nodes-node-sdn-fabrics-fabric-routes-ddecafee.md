# `/nodes/{node}/sdn/fabrics/{fabric}/routes`

原始接口路径：`/nodes/{node}/sdn/fabrics/{fabric}/routes`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/fabrics/{fabric}/routes`

Get all routes for a fabric.

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
| `fabric` | string | 是 | — | Identifier for SDN fabrics |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fabric": {
      "description": "Identifier for SDN fabrics",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
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
        "description": "The CIDR block for this routing table entry.",
        "type": "string"
      },
      "via": {
        "description": "A list of nexthops for that route.",
        "items": {
          "description": "The IP address of the nexthop.",
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
