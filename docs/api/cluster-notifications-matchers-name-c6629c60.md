# `/cluster/notifications/matchers/{name}`

原始接口路径：`/cluster/notifications/matchers/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/notifications/matchers/{name}`

Remove matcher

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

Return a specific matcher

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
      "description": "Comment",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "disable": {
      "default": 0,
      "description": "Disable this matcher",
      "optional": 1,
      "type": "boolean"
    },
    "invert-match": {
      "description": "Invert match of the whole matcher",
      "optional": 1,
      "type": "boolean"
    },
    "match-calendar": {
      "description": "Match notification timestamp",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "match-field": {
      "description": "Metadata fields to match (regex or exact match). Must be in the form (regex|exact):<field>=<value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "match-severity": {
      "description": "Notification severities to match",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "mode": {
      "default": "all",
      "description": "Choose between 'all' and 'any' for when multiple properties are specified",
      "enum": [
        "all",
        "any"
      ],
      "optional": 1,
      "type": "string"
    },
    "name": {
      "description": "Name of the matcher.",
      "format": "pve-configid",
      "type": "string"
    },
    "target": {
      "description": "Targets to notify on match",
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

Update existing matcher

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
| `comment` | string | 否 | — | Comment |
| `delete` | array | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable` | boolean | 否 | 0 | Disable this matcher |
| `invert-match` | boolean | 否 | — | Invert match of the whole matcher |
| `match-calendar` | array | 否 | — | Match notification timestamp |
| `match-field` | array | 否 | — | Metadata fields to match (regex or exact match). Must be in the form (regex\|exact):&lt;field&gt;=&lt;value&gt; |
| `match-severity` | array | 否 | — | Notification severities to match |
| `mode` | string | 否 | "all" | Choose between 'all' and 'any' for when multiple properties are specified；可选值：`all`, `any` |
| `name` | string | 是 | — | Name of the matcher. |
| `target` | array | 否 | — | Targets to notify on match |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "Comment",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "items": {
        "format": "pve-configid",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "default": 0,
      "description": "Disable this matcher",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "invert-match": {
      "description": "Invert match of the whole matcher",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "match-calendar": {
      "description": "Match notification timestamp",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "match-field": {
      "description": "Metadata fields to match (regex or exact match). Must be in the form (regex|exact):<field>=<value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "match-severity": {
      "description": "Notification severities to match",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "mode": {
      "default": "all",
      "description": "Choose between 'all' and 'any' for when multiple properties are specified",
      "enum": [
        "all",
        "any"
      ],
      "optional": 1,
      "type": "string"
    },
    "name": {
      "description": "Name of the matcher.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "target": {
      "description": "Targets to notify on match",
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
