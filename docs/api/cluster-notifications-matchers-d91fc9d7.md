# `/cluster/notifications/matchers`

原始接口路径：`/cluster/notifications/matchers`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/matchers`

Returns a list of all matchers

**方法标识：** `get_matchers`

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
    ],
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Use"
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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "comment": {
        "description": "Comment",
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
      "origin": {
        "description": "Show if this entry was created by a user or was built-in",
        "enum": [
          "user-created",
          "builtin",
          "modified-builtin"
        ],
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
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/notifications/matchers`

Create a new matcher

**方法标识：** `create_matcher`

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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matchers)。
