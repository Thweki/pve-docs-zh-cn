# `/nodes/{node}/hardware/pci/{pci-id-or-mapping}`

原始接口路径：`/nodes/{node}/hardware/pci/{pci-id-or-mapping}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/hardware/pci/{pci-id-or-mapping}`

Index of available pci methods

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `pci-id-or-mapping` | string | 是 | — |  |

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
    "pci-id-or-mapping": {
      "pattern": "(?:(?:[0-9a-fA-F]{4}:)?[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\\.[0-9a-fA-F])|([a-zA-Z][a-zA-Z0-9_-]+)",
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
      "method": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{method}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/hardware/pci/{pci-id-or-mapping})。
