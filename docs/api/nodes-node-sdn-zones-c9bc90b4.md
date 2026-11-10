# `/nodes/{node}/sdn/zones`

原始接口路径：`/nodes/{node}/sdn/zones`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/zones`

获取所有区域的状态。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您具有 'SDN.Audit' 权限的条目",
  "user": "all"
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
      "status": {
        "description": "区域状态",
        "enum": [
          "available",
          "pending",
          "error"
        ],
        "type": "string"
      },
      "zone": {
        "description": "SDN 区域对象标识符。",
        "maxLength": 8,
        "minLength": 2,
        "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{zone}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/zones)。
