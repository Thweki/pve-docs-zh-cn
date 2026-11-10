# `/cluster/notifications/endpoints/webhook`

原始接口路径：`/cluster/notifications/endpoints/webhook`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/endpoints/webhook`

返回所有 webhook 端点的列表

**方法标识：** `get_webhook_endpoints`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/notifications",
    [
      "Mapping.Audit"
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
      "body": {
        "description": "HTTP 正文，采用 base64 编码",
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
      "header": {
        "description": "要设置的 HTTP 标头。必须采用属性字符串格式：name=<name>,value=<base64 of value>",
        "items": {
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "method": {
        "description": "HTTP 方法",
        "enum": [
          "post",
          "put",
          "get"
        ],
        "type": "string"
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
      },
      "secret": {
        "description": "要设置的秘密信息。必须采用属性字符串格式：name=<name>,value=<base64 of value>",
        "items": {
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "url": {
        "description": "服务器 URL",
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

## POST `/cluster/notifications/endpoints/webhook`

创建新的 webhook 端点

**方法标识：** `create_webhook_endpoint`

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
| `body` | string | 否 | — | HTTP 正文，采用 base64 编码 |
| `comment` | string | 否 | — | 注释 |
| `disable` | boolean | 否 | 0 | 禁用此目标 |
| `header` | array | 否 | — | 要设置的 HTTP 标头。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `method` | string | 是 | — | HTTP 方法；可选值：`post`, `put`, `get` |
| `name` | string | 是 | — | 端点名称。 |
| `secret` | array | 否 | — | 要设置的秘密信息。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `url` | string | 是 | — | 服务器 URL |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "body": {
      "description": "HTTP 正文，采用 base64 编码",
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
    "header": {
      "description": "要设置的 HTTP 标头。必须采用属性字符串格式：name=<name>,value=<base64 of value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "method": {
      "description": "HTTP 方法",
      "enum": [
        "post",
        "put",
        "get"
      ],
      "type": "string"
    },
    "name": {
      "description": "端点名称。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "secret": {
      "description": "要设置的秘密信息。必须采用属性字符串格式：name=<name>,value=<base64 of value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "url": {
      "description": "服务器 URL",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/webhook)。
