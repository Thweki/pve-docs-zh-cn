# `/nodes/{node}/sdn/zones/{zone}/content`

原始接口路径：`/nodes/{node}/sdn/zones/{zone}/content`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/zones/{zone}/content`

List zone content.

**方法标识：** `index`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}",
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
| `node` | string | 是 | — | The cluster node name. |
| `zone` | string | 是 | — | The SDN zone object identifier. |

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
    "zone": {
      "description": "The SDN zone object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
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
        "description": "Status.",
        "optional": 1,
        "type": "string"
      },
      "statusmsg": {
        "description": "Status details",
        "optional": 1,
        "type": "string"
      },
      "vnet": {
        "description": "Vnet identifier.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{vnet}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/zones/{zone}/content)。
