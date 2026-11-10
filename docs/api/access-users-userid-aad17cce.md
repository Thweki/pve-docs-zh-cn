# `/access/users/{userid}`

原始接口路径：`/access/users/{userid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/users/{userid}`

删除用户。

**方法标识：** `delete_user`

**权限**

```json
{
  "check": [
    "and",
    [
      "userid-param",
      "Realm.AllocateUser"
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
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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

## GET `/access/users/{userid}`

获取用户配置。

**方法标识：** `read_user`

**权限**

```json
{
  "check": [
    "userid-group",
    [
      "User.Modify",
      "Sys.Audit"
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
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    "comment": {
      "maxLength": 2048,
      "optional": 1,
      "type": "string"
    },
    "email": {
      "format": "email-opt",
      "maxLength": 254,
      "optional": 1,
      "type": "string"
    },
    "enable": {
      "default": 1,
      "description": "启用账户（默认）。可设为 '0' 以禁用账户",
      "optional": 1,
      "type": "boolean"
    },
    "expire": {
      "description": "账户到期日期（自纪元起的秒数）。'0' 表示永不过期。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "firstname": {
      "maxLength": 1024,
      "optional": 1,
      "type": "string"
    },
    "groups": {
      "items": {
        "format": "pve-groupid",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "keys": {
      "description": "双因素身份验证密钥（yubico）。",
      "optional": 1,
      "pattern": "[0-9a-zA-Z!=]{0,4096}",
      "type": "string"
    },
    "lastname": {
      "maxLength": 1024,
      "optional": 1,
      "type": "string"
    },
    "tokens": {
      "additionalProperties": {
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
      "optional": 1,
      "type": "object"
    }
  },
  "type": "object"
}
```

## PUT `/access/users/{userid}`

更新用户配置。

**方法标识：** `update_user`

**权限**

```json
{
  "check": [
    "userid-group",
    [
      "User.Modify"
    ],
    "groups_param",
    "update"
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
| `append` | boolean | 否 | — |  |
| `comment` | string | 否 | — |  |
| `email` | string | 否 | — |  |
| `enable` | boolean | 否 | 1 | 启用账户（默认）。可设为 '0' 以禁用账户 |
| `expire` | integer | 否 | — | 账户到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `firstname` | string | 否 | — |  |
| `groups` | string | 否 | — |  |
| `keys` | string | 否 | — | 双因素身份验证密钥（yubico）。 |
| `lastname` | string | 否 | — |  |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "append": {
      "optional": 1,
      "requires": "groups",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "comment": {
      "maxLength": 2048,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "email": {
      "format": "email-opt",
      "maxLength": 254,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "default": 1,
      "description": "启用账户（默认）。可设为 '0' 以禁用账户",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "expire": {
      "description": "账户到期日期（自纪元起的秒数）。'0' 表示永不过期。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "firstname": {
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "groups": {
      "format": "pve-groupid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "keys": {
      "description": "双因素身份验证密钥（yubico）。",
      "optional": 1,
      "pattern": "[0-9a-zA-Z!=]{0,4096}",
      "type": "string"
    },
    "lastname": {
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid})。
