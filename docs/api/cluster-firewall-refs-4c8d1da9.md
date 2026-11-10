# `/cluster/firewall/refs`

原始接口路径：`/cluster/firewall/refs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/refs`

列出源地址/目标地址属性中允许使用的 IPSet/别名引用。

**方法标识：** `refs`

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
| `type` | string | 否 | — | 仅列出指定类型的引用。；可选值：`alias`, `ipset` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "仅列出指定类型的引用。",
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
        "description": "可选注释或描述。",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "别名或 ipset 的名称。",
        "type": "string"
      },
      "ref": {
        "description": "防火墙规则中使用的引用字符串。",
        "type": "string"
      },
      "scope": {
        "description": "引用的作用域（例如 SDN）。",
        "type": "string"
      },
      "type": {
        "description": "引用类型（alias 或 ipset）。",
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
