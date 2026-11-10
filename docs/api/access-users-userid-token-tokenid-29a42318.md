# `/access/users/{userid}/token/{tokenid}`

原始接口路径：`/access/users/{userid}/token/{tokenid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/users/{userid}/token/{tokenid}`

移除特定用户的 API 令牌。

**方法标识：** `remove_token`

**权限**

```json
{
  "check": [
    "or",
    [
      "userid-param",
      "self"
    ],
    [
      "userid-group",
      [
        "User.Modify"
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
| `tokenid` | string | 是 | — | 用户特定的令牌标识符。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "tokenid": {
      "description": "用户特定的令牌标识符。",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "完整用户 ID，采用 `name@realm` 格式。",
      "format": "pve-userid",
      "maxLength": 64,
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

## GET `/access/users/{userid}/token/{tokenid}`

获取特定 API 令牌信息。

**方法标识：** `read_token`

**权限**

```json
{
  "check": [
    "or",
    [
      "userid-param",
      "self"
    ],
    [
      "userid-group",
      [
        "User.Modify"
      ]
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
| `tokenid` | string | 是 | — | 用户特定的令牌标识符。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "tokenid": {
      "description": "用户特定的令牌标识符。",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "完整用户 ID，采用 `name@realm` 格式。",
      "format": "pve-userid",
      "maxLength": 64,
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
      "optional": 1,
      "type": "string"
    },
    "expire": {
      "default": "same as user",
      "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "privsep": {
      "default": 1,
      "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/access/users/{userid}/token/{tokenid}`

为特定用户生成新的 API 令牌。注意：返回 API 令牌值，必须保存，因为之后无法再次获取！

**方法标识：** `generate_token`

**权限**

```json
{
  "check": [
    "or",
    [
      "userid-param",
      "self"
    ],
    [
      "userid-group",
      [
        "User.Modify"
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
| `comment` | string | 否 | — |  |
| `expire` | integer | 否 | "same as user" | API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `privsep` | boolean | 否 | 1 | 使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。 |
| `tokenid` | string | 是 | — | 用户特定的令牌标识符。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "expire": {
      "default": "same as user",
      "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "privsep": {
      "default": 1,
      "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "tokenid": {
      "description": "用户特定的令牌标识符。",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "完整用户 ID，采用 `name@realm` 格式。",
      "format": "pve-userid",
      "maxLength": 64,
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
  "additionalProperties": 0,
  "properties": {
    "full-tokenid": {
      "description": "完整令牌 ID。",
      "format_description": "<userid>!<tokenid>",
      "type": "string"
    },
    "info": {
      "properties": {
        "comment": {
          "optional": 1,
          "type": "string"
        },
        "expire": {
          "default": "same as user",
          "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "privsep": {
          "default": 1,
          "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "value": {
      "description": "用于身份验证的 API 令牌值。",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/access/users/{userid}/token/{tokenid}`

更新特定用户的 API 令牌。注意：设置 'regenerate' 时，必须保存返回的令牌值，因为之后无法再次获取！

**方法标识：** `update_token_info`

**权限**

```json
{
  "check": [
    "or",
    [
      "userid-param",
      "self"
    ],
    [
      "userid-group",
      [
        "User.Modify"
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
| `comment` | string | 否 | — |  |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `expire` | integer | 否 | "same as user" | API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `privsep` | boolean | 否 | 1 | 使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。 |
| `regenerate` | boolean | 否 | 0 | 重新生成令牌的密钥值。此操作后，所有使用旧密钥的使用方都将失去访问权限。 |
| `tokenid` | string | 是 | — | 用户特定的令牌标识符。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "expire": {
      "default": "same as user",
      "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "privsep": {
      "default": 1,
      "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "regenerate": {
      "default": 0,
      "description": "重新生成令牌的密钥值。此操作后，所有使用旧密钥的使用方都将失去访问权限。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "tokenid": {
      "description": "用户特定的令牌标识符。",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "完整用户 ID，采用 `name@realm` 格式。",
      "format": "pve-userid",
      "maxLength": 64,
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
      "optional": 1,
      "type": "string"
    },
    "expire": {
      "default": "same as user",
      "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "full-tokenid": {
      "description": "完整令牌 ID。仅在设置了 'regenerate' 时设置。",
      "format_description": "<userid>!<tokenid>",
      "optional": 1,
      "type": "string"
    },
    "privsep": {
      "default": 1,
      "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。",
      "optional": 1,
      "type": "boolean"
    },
    "value": {
      "description": "用于身份验证的 API 令牌值。仅在设置了 'regenerate' 时设置。",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/token/{tokenid})。
