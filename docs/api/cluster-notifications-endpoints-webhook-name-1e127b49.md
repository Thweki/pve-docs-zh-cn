# `/cluster/notifications/endpoints/webhook/{name}`

原始接口路径：`/cluster/notifications/endpoints/webhook/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/notifications/endpoints/webhook/{name}`

Remove webhook endpoint

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

## GET `/cluster/notifications/endpoints/webhook/{name}`

Return a specific webhook endpoint

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
| `name` | string | 是 | — | Name of the endpoint. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "Name of the endpoint.",
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
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
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
}
```

## PUT `/cluster/notifications/endpoints/webhook/{name}`

Update existing webhook endpoint

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
| `delete` | array | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable` | boolean | 否 | 0 | Disable this target |
| `header` | array | 否 | — | HTTP headers to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value> |
| `method` | string | 否 | — | HTTP method；可选值：`post`, `put`, `get` |
| `name` | string | 是 | — | The name of the endpoint. |
| `secret` | array | 否 | — | Secrets to set. These have to be formatted as a property string in the format name=<name>,value=<base64 of value> |
| `url` | string | 否 | — | Server URL |

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
      "optional": 1,
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
      "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/webhook/{name})。
