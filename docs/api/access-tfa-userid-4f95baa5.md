# `/access/tfa/{userid}`

原始接口路径：`/access/tfa/{userid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/tfa/{userid}`

List TFA configurations of users.

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
        "User.Modify",
        "Sys.Audit"
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
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
  "description": "A list of the user's TFA entries.",
  "items": {
    "description": "TFA Entry.",
    "properties": {
      "created": {
        "description": "Creation time of this entry as unix epoch.",
        "type": "integer"
      },
      "description": {
        "description": "User chosen description for this entry.",
        "type": "string"
      },
      "enable": {
        "default": 1,
        "description": "Whether this TFA entry is currently enabled.",
        "optional": 1,
        "type": "boolean"
      },
      "id": {
        "description": "The id used to reference this entry.",
        "type": "string"
      },
      "type": {
        "description": "TFA Entry Type.",
        "enum": [
          "totp",
          "u2f",
          "webauthn",
          "recovery",
          "yubico"
        ],
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/access/tfa/{userid}`

Add a TFA entry for a user.

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
0
```

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `challenge` | string | 否 | — | When responding to a u2f challenge: the original challenge string |
| `description` | string | 否 | — | A description to distinguish multiple entries from one another |
| `password` | string | 否 | — | The current password of the user performing the change. |
| `totp` | string | 否 | — | A totp URI. |
| `type` | string | 是 | — | TFA Entry Type.；可选值：`totp`, `u2f`, `webauthn`, `recovery`, `yubico` |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |
| `value` | string | 否 | — | The current value for the provided totp URI, or a Webauthn/U2F challenge response |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "challenge": {
      "description": "When responding to a u2f challenge: the original challenge string",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "A description to distinguish multiple entries from one another",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "The current password of the user performing the change.",
      "maxLength": 64,
      "minLength": 5,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "totp": {
      "description": "A totp URI.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "TFA Entry Type.",
      "enum": [
        "totp",
        "u2f",
        "webauthn",
        "recovery",
        "yubico"
      ],
      "type": "string"
    },
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
      "format": "pve-userid",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "value": {
      "description": "The current value for the provided totp URI, or a Webauthn/U2F challenge response",
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
  "properties": {
    "challenge": {
      "description": "When adding u2f entries, this contains a challenge the user must respond to in order to finish the registration.",
      "optional": 1,
      "type": "string"
    },
    "id": {
      "description": "The id of a newly added TFA entry.",
      "type": "string"
    },
    "recovery": {
      "description": "When adding recovery codes, this contains the list of codes to be displayed to the user",
      "items": {
        "description": "A recovery entry.",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa/{userid})。
