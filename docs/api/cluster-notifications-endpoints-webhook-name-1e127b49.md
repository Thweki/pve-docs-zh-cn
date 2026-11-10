# `/cluster/notifications/endpoints/webhook/{name}`

原始接口路径：`/cluster/notifications/endpoints/webhook/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/notifications/endpoints/webhook/{name}`

移除 webhook 端点

**方法标识：** `delete_webhook_endpoint`

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

返回指定的 webhook 端点

**方法标识：** `get_webhook_endpoint`

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
| `name` | string | 是 | — | 端点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
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
}
```

## PUT `/cluster/notifications/endpoints/webhook/{name}`

更新现有 webhook 端点

**方法标识：** `update_webhook_endpoint`

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
| `delete` | array | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | boolean | 否 | 0 | 禁用此目标 |
| `header` | array | 否 | — | 要设置的 HTTP 标头。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `method` | string | 否 | — | HTTP 方法；可选值：`post`, `put`, `get` |
| `name` | string | 是 | — | 端点名称。 |
| `secret` | array | 否 | — | 要设置的秘密信息。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `url` | string | 否 | — | 服务器 URL |

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
      "optional": 1,
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
