# `/cluster/notifications/endpoints/webhook`

原始接口路径：`/cluster/notifications/endpoints/webhook`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/endpoints/webhook`

Returns a list of all webhook endpoints

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
        "description": "HTTP body, base64 encoded",
        "optional": 1,
        "type": "string"
      },
      "comment": {
        "description": "Comment",
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "default": 0,
        "description": "Disable this target",
        "optional": 1,
        "type": "boolean"
      },
      "header": {
        "description": "HTTP headers to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value>",
        "items": {
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "method": {
        "description": "HTTP method",
        "enum": [
          "post",
          "put",
          "get"
        ],
        "type": "string"
      },
      "name": {
        "description": "The name of the endpoint.",
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
      "secret": {
        "description": "Secrets to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value>",
        "items": {
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "url": {
        "description": "Server URL",
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

Create a new webhook endpoint

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
| `body` | string | 否 | — | HTTP body, base64 encoded |
| `comment` | string | 否 | — | Comment |
| `disable` | boolean | 否 | 0 | Disable this target |
| `header` | array | 否 | — | HTTP headers to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value> |
| `method` | string | 是 | — | HTTP method；可选值：`post`, `put`, `get` |
| `name` | string | 是 | — | The name of the endpoint. |
| `secret` | array | 否 | — | Secrets to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value> |
| `url` | string | 是 | — | Server URL |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "body": {
      "description": "HTTP body, base64 encoded",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "description": "Comment",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "default": 0,
      "description": "Disable this target",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "header": {
      "description": "HTTP headers to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "method": {
      "description": "HTTP method",
      "enum": [
        "post",
        "put",
        "get"
      ],
      "type": "string"
    },
    "name": {
      "description": "The name of the endpoint.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "secret": {
      "description": "Secrets to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value>",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "url": {
      "description": "Server URL",
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
