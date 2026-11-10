# `/access/users`

原始接口路径：`/access/users`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/users`

用户索引。

**方法标识：** `index`

**权限**

```json
{
  "description": "返回列表仅限于您对 '/access/groups' 或用户所属的组具有 'User.Modify' 或 'Sys.Audit' 权限的用户。但始终包含当前（已通过身份验证的）用户。",
  "user": "all"
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
| `enabled` | boolean | 否 | — | enable 属性的可选过滤条件。 |
| `full` | boolean | 否 | 0 | 包含组和令牌信息。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "enabled": {
      "description": "enable 属性的可选过滤条件。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "full": {
      "default": 0,
      "description": "包含组和令牌信息。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
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
        "format": "pve-groupid-list",
        "optional": 1,
        "type": "string"
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
      "realm-type": {
        "description": "用户所属认证域的类型",
        "format": "pve-realm",
        "optional": 1,
        "type": "string"
      },
      "tfa-locked-until": {
        "description": "包含用户第二因素锁定截止时间的时间戳。",
        "optional": 1,
        "type": "integer"
      },
      "tokens": {
        "items": {
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
            },
            "tokenid": {
              "description": "用户特定的令牌标识符。",
              "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
              "type": "string"
            }
          },
          "type": "object"
        },
        "optional": 1,
        "type": "array"
      },
      "totp-locked": {
        "description": "如果用户当前被锁定而无法使用 TOTP 因素，则为 true。",
        "optional": 1,
        "type": "boolean"
      },
      "userid": {
        "description": "完整用户 ID，采用 `name@realm` 格式。",
        "format": "pve-userid",
        "maxLength": 64,
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{userid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/access/users`

创建新用户。

**方法标识：** `create_user`

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
      ],
      "groups_param",
      "create"
    ]
  ],
  "description": "需要对用户 <userid> 所属认证域的 '/access/realm/<realm>' 具有 'Realm.AllocateUser' 权限，并且对任何指定组的 '/access/groups/<group>' 具有 'User.Modify' 权限（如果未传入任何组，则需要对 '/access/groups' 具有 'User.Modify' 权限。"
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
| `email` | string | 否 | — |  |
| `enable` | boolean | 否 | 1 | 启用账户（默认）。可设为 '0' 以禁用账户 |
| `expire` | integer | 否 | — | 账户到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `firstname` | string | 否 | — |  |
| `groups` | string | 否 | — |  |
| `keys` | string | 否 | — | 双因素身份验证密钥（yubico）。 |
| `lastname` | string | 否 | — |  |
| `password` | string | 否 | — | 初始密码。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    "password": {
      "description": "初始密码。",
      "maxLength": 64,
      "minLength": 8,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users)。
