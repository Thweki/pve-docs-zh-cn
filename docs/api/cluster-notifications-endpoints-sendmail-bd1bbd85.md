# `/cluster/notifications/endpoints/sendmail`

原始接口路径：`/cluster/notifications/endpoints/sendmail`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/endpoints/sendmail`

返回所有 sendmail 端点的列表

**方法标识：** `get_sendmail_endpoints`

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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "author": {
        "description": "邮件作者",
        "optional": 1,
        "type": "string"
      },
      "comment": {
        "description": "注释",
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "default": 0,
        "description": "禁用此目标",
        "optional": 1,
        "type": "boolean"
      },
      "from-address": {
        "description": "邮件的 `From` 地址",
        "optional": 1,
        "type": "string"
      },
      "mailto": {
        "description": "电子邮件收件人列表",
        "items": {
          "format": "email-or-username",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "mailto-user": {
        "description": "用户列表",
        "items": {
          "format": "pve-userid",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "name": {
        "description": "端点名称。",
        "format": "pve-configid",
        "type": "string"
      },
      "origin": {
        "description": "显示此条目是用户创建还是内置",
        "enum": [
          "user-created",
          "builtin",
          "modified-builtin"
        ],
        "type": "string"
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

## POST `/cluster/notifications/endpoints/sendmail`

创建新的 sendmail 端点

**方法标识：** `create_sendmail_endpoint`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "or",
      [
        "perm",
        "/",
        [
          "Sys.Audit",
          "Sys.Modify"
        ]
      ],
      [
        "perm",
        "/",
        [
          "Sys.AccessNetwork"
        ]
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
| `author` | string | 否 | — | 邮件作者 |
| `comment` | string | 否 | — | 注释 |
| `disable` | boolean | 否 | 0 | 禁用此目标 |
| `from-address` | string | 否 | — | 邮件的 `From` 地址 |
| `mailto` | array | 否 | — | 电子邮件收件人列表 |
| `mailto-user` | array | 否 | — | 用户列表 |
| `name` | string | 是 | — | 端点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "author": {
      "description": "邮件作者",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "description": "注释",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "default": 0,
      "description": "禁用此目标",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "from-address": {
      "description": "邮件的 `From` 地址",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mailto": {
      "description": "电子邮件收件人列表",
      "items": {
        "format": "email-or-username",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "mailto-user": {
      "description": "用户列表",
      "items": {
        "format": "pve-userid",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "name": {
      "description": "端点名称。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/sendmail)。
