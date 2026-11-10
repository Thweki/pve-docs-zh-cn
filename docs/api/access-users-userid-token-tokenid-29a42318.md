# `/access/users/{userid}/token/{tokenid}`

原始接口路径：`/access/users/{userid}/token/{tokenid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/users/{userid}/token/{tokenid}`

Remove API token for a specific user.

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
| `tokenid` | string | 是 | — | User-specific token identifier. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "tokenid": {
      "description": "User-specific token identifier.",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
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

Get specific API token information.

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
| `tokenid` | string | 是 | — | User-specific token identifier. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "tokenid": {
      "description": "User-specific token identifier.",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
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
      "description": "API token expiration date (seconds since epoch). '0' means no expiration date.",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "privsep": {
      "default": 1,
      "description": "Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/access/users/{userid}/token/{tokenid}`

Generate a new API token for a specific user. NOTE: returns API token value, which needs to be stored as it cannot be retrieved afterwards!

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
| `expire` | integer | 否 | "same as user" | API token expiration date (seconds since epoch). '0' means no expiration date. |
| `privsep` | boolean | 否 | 1 | Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user. |
| `tokenid` | string | 是 | — | User-specific token identifier. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

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
      "description": "API token expiration date (seconds since epoch). '0' means no expiration date.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "privsep": {
      "default": 1,
      "description": "Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "tokenid": {
      "description": "User-specific token identifier.",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
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
      "description": "The full token id.",
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
          "description": "API token expiration date (seconds since epoch). '0' means no expiration date.",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "privsep": {
          "default": 1,
          "description": "Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.",
          "optional": 1,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "value": {
      "description": "API token value used for authentication.",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/access/users/{userid}/token/{tokenid}`

Update API token for a specific user. NOTE: when 'regenerate' is set, the returned token value needs to be stored as it cannot be retrieved afterwards!

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
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `expire` | integer | 否 | "same as user" | API token expiration date (seconds since epoch). '0' means no expiration date. |
| `privsep` | boolean | 否 | 1 | Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user. |
| `regenerate` | boolean | 否 | 0 | Regenerate the token's secret value. All users of the previous secret will lose access after this operation. |
| `tokenid` | string | 是 | — | User-specific token identifier. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

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
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "expire": {
      "default": "same as user",
      "description": "API token expiration date (seconds since epoch). '0' means no expiration date.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "privsep": {
      "default": 1,
      "description": "Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "regenerate": {
      "default": 0,
      "description": "Regenerate the token's secret value. All users of the previous secret will lose access after this operation.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "tokenid": {
      "description": "User-specific token identifier.",
      "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
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
      "description": "API token expiration date (seconds since epoch). '0' means no expiration date.",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "full-tokenid": {
      "description": "The full token id. Only set when 'regenerate' was set.",
      "format_description": "<userid>!<tokenid>",
      "optional": 1,
      "type": "string"
    },
    "privsep": {
      "default": 1,
      "description": "Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.",
      "optional": 1,
      "type": "boolean"
    },
    "value": {
      "description": "API token value used for authentication. Only set when 'regenerate' was set.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/token/{tokenid})。
