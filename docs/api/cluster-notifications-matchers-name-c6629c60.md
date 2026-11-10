# `/cluster/notifications/matchers/{name}`

原始接口路径：`/cluster/notifications/matchers/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/notifications/matchers/{name}`

移除匹配器

**方法标识：** `delete_matcher`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/notifications",
    [
      "Mapping.Modify"
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
| `name` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
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

## GET `/cluster/notifications/matchers/{name}`

返回指定的匹配器

**方法标识：** `get_matcher`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Audit"
      ]
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
| `name` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
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
    "comment": {
      "description": "注释",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "disable": {
      "default": 0,
      "description": "禁用此匹配器",
      "optional": 1,
      "type": "boolean"
    },
    "invert-match": {
      "description": "反转整个匹配器的匹配结果",
      "optional": 1,
      "type": "boolean"
    },
    "match-calendar": {
      "description": "匹配通知时间戳",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "match-field": {
      "description": "要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex|exact):<field>=<value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "match-severity": {
      "description": "要匹配的通知严重性",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "mode": {
      "default": "all",
      "description": "指定多个属性时，在 'all' 和 'any' 之间选择",
      "enum": [
        "all",
        "any"
      ],
      "optional": 1,
      "type": "string"
    },
    "name": {
      "description": "匹配器名称。",
      "format": "pve-configid",
      "type": "string"
    },
    "target": {
      "description": "匹配时要通知的目标",
      "items": {
        "format": "pve-configid",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/notifications/matchers/{name}`

更新现有匹配器

**方法标识：** `update_matcher`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/notifications",
    [
      "Mapping.Modify"
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
| `comment` | string | 否 | — | 注释 |
| `delete` | array | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | boolean | 否 | 0 | 禁用此匹配器 |
| `invert-match` | boolean | 否 | — | 反转整个匹配器的匹配结果 |
| `match-calendar` | array | 否 | — | 匹配通知时间戳 |
| `match-field` | array | 否 | — | 要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex\|exact):&lt;field&gt;=&lt;value&gt; |
| `match-severity` | array | 否 | — | 要匹配的通知严重性 |
| `mode` | string | 否 | "all" | 指定多个属性时，在 'all' 和 'any' 之间选择；可选值：`all`, `any` |
| `name` | string | 是 | — | 匹配器名称。 |
| `target` | array | 否 | — | 匹配时要通知的目标 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "注释",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "items": {
        "format": "pve-configid",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "default": 0,
      "description": "禁用此匹配器",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "invert-match": {
      "description": "反转整个匹配器的匹配结果",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "match-calendar": {
      "description": "匹配通知时间戳",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "match-field": {
      "description": "要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex|exact):<field>=<value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "match-severity": {
      "description": "要匹配的通知严重性",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "mode": {
      "default": "all",
      "description": "指定多个属性时，在 'all' 和 'any' 之间选择",
      "enum": [
        "all",
        "any"
      ],
      "optional": 1,
      "type": "string"
    },
    "name": {
      "description": "匹配器名称。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "target": {
      "description": "匹配时要通知的目标",
      "items": {
        "format": "pve-configid",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matchers/{name})。
