# `/cluster/firewall/refs`

原始接口路径：`/cluster/firewall/refs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/refs`

Lists possible IPSet/Alias reference which are allowed in source/dest properties.

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `type` | string | 否 | — | Only list references of specified type.；可选值：`alias`, `ipset` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "Only list references of specified type.",
      "enum": [
        "alias",
        "ipset"
      ],
      "optional": 1,
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
      "comment": {
        "description": "Optional comment or description.",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "The name of the alias or ipset.",
        "type": "string"
      },
      "ref": {
        "description": "The reference string used in firewall rules.",
        "type": "string"
      },
      "scope": {
        "description": "The scope of the reference (e.g., SDN).",
        "type": "string"
      },
      "type": {
        "description": "The type of reference (alias or ipset).",
        "enum": [
          "alias",
          "ipset"
        ],
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/refs)。
