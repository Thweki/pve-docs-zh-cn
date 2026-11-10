# `/cluster/ha/rules`

原始接口路径：`/cluster/ha/rules`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ha/rules`

获取 HA 规则。

**方法标识：** `index`

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
| `resource` | string | 否 | — | Limit the returned list to rules affecting the specified resource. |
| `type` | string | 否 | — | Limit the returned list to the specified rule type.；可选值：`node-affinity`, `resource-affinity` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "resource": {
      "description": "Limit the returned list to rules affecting the specified resource.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "Limit the returned list to the specified rule type.",
      "enum": [
        "node-affinity",
        "resource-affinity"
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
    "links": [
      {
        "href": "{rule}",
        "rel": "child"
      }
    ],
    "properties": {
      "rule": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

## POST `/cluster/ha/rules`

创建 HA 规则。

**方法标识：** `create_rule`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Console"
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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/rules)。
