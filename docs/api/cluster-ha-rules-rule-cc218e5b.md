# `/cluster/ha/rules/{rule}`

原始接口路径：`/cluster/ha/rules/{rule}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/ha/rules/{rule}`

删除 HA 规则。

**方法标识：** `delete_rule`

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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `rule` | string | 是 | — | HA rule identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "rule": {
      "description": "HA rule identifier.",
      "format": "pve-configid",
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
  "type": "null"
}
```

## GET `/cluster/ha/rules/{rule}`

Read HA rule.

**方法标识：** `read_rule`

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
| `rule` | string | 是 | — | HA rule identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "rule": {
      "description": "HA rule identifier.",
      "format": "pve-configid",
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
  "properties": {
    "rule": {
      "description": "HA rule identifier.",
      "format": "pve-configid",
      "type": "string"
    },
    "type": {
      "description": "HA rule type.",
      "enum": [
        "node-affinity",
        "resource-affinity"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/ha/rules/{rule}`

更新 HA 规则。

**方法标识：** `update_rule`

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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/rules/{rule})。
