# `/access/users`

原始接口路径：`/access/users`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/users`

User index.

**方法标识：** `index`

**权限**

```json
{
  "description": "The returned list is restricted to users where you have 'User.Modify' or 'Sys.Audit' permissions on '/access/groups' or on a group the user belongs too. But it always includes the current (authenticated) user.",
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
| `enabled` | boolean | 否 | — | Optional filter for enable property. |
| `full` | boolean | 否 | 0 | Include group and token information. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "enabled": {
      "description": "Optional filter for enable property.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "full": {
      "default": 0,
      "description": "Include group and token information.",
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
        "description": "Enable the account (default). You can set this to '0' to disable the account",
        "optional": 1,
        "type": "boolean"
      },
      "expire": {
        "description": "Account expiration date (seconds since epoch). '0' means no expiration date.",
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
        "description": "Keys for two factor auth (yubico).",
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
        "description": "The type of the users realm",
        "format": "pve-realm",
        "optional": 1,
        "type": "string"
      },
      "tfa-locked-until": {
        "description": "Contains a timestamp until when a user is locked out of 2nd factors.",
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
            },
            "tokenid": {
              "description": "User-specific token identifier.",
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
        "description": "True if the user is currently locked out of TOTP factors.",
        "optional": 1,
        "type": "boolean"
      },
      "userid": {
        "description": "Full User ID, in the `name@realm` format.",
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

Create new user.

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
  "description": "You need 'Realm.AllocateUser' on '/access/realm/<realm>' on the realm of user <userid>, and 'User.Modify' permissions to '/access/groups/<group>' for any group specified (or 'User.Modify' on '/access/groups' if you pass no groups."
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
| `enable` | boolean | 否 | 1 | Enable the account (default). You can set this to '0' to disable the account |
| `expire` | integer | 否 | — | Account expiration date (seconds since epoch). '0' means no expiration date. |
| `firstname` | string | 否 | — |  |
| `groups` | string | 否 | — |  |
| `keys` | string | 否 | — | Keys for two factor auth (yubico). |
| `lastname` | string | 否 | — |  |
| `password` | string | 否 | — | Initial password. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

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
      "description": "Enable the account (default). You can set this to '0' to disable the account",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "expire": {
      "description": "Account expiration date (seconds since epoch). '0' means no expiration date.",
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
      "description": "Keys for two factor auth (yubico).",
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
      "description": "Initial password.",
      "maxLength": 64,
      "minLength": 8,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users)。
