# `/access/tfa/{userid}`

原始接口路径：`/access/tfa/{userid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/tfa/{userid}`

列出用户的 TFA 配置。

**方法标识：** `list_user_tfa`

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
  "description": "用户的 TFA 条目列表。",
  "items": {
    "description": "TFA 条目。",
    "properties": {
      "created": {
        "description": "此条目的创建时间，以 UNIX 纪元时间表示。",
        "type": "integer"
      },
      "description": {
        "description": "用户为此条目选择的描述。",
        "type": "string"
      },
      "enable": {
        "default": 1,
        "description": "此 TFA 条目当前是否已启用。",
        "optional": 1,
        "type": "boolean"
      },
      "id": {
        "description": "用于引用此条目的 ID。",
        "type": "string"
      },
      "type": {
        "description": "TFA 条目类型。",
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

为用户添加 TFA 条目。

**方法标识：** `add_tfa_entry`

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
| `challenge` | string | 否 | — | 响应 U2F 质询时：原始质询字符串 |
| `description` | string | 否 | — | 用于区分多个条目的描述 |
| `password` | string | 否 | — | 执行更改的用户的当前密码。 |
| `totp` | string | 否 | — | TOTP URI。 |
| `type` | string | 是 | — | TFA 条目类型。；可选值：`totp`, `u2f`, `webauthn`, `recovery`, `yubico` |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |
| `value` | string | 否 | — | 提供的 TOTP URI 的当前值，或 Webauthn/U2F 质询响应 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "challenge": {
      "description": "响应 U2F 质询时：原始质询字符串",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "用于区分多个条目的描述",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "执行更改的用户的当前密码。",
      "maxLength": 64,
      "minLength": 5,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "totp": {
      "description": "TOTP URI。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "TFA 条目类型。",
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
      "description": "完整用户 ID，采用 `name@realm` 格式。",
      "format": "pve-userid",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "value": {
      "description": "提供的 TOTP URI 的当前值，或 Webauthn/U2F 质询响应",
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
      "description": "添加 U2F 条目时，此项包含用户必须响应以完成注册的质询。",
      "optional": 1,
      "type": "string"
    },
    "id": {
      "description": "新添加的 TFA 条目的 ID。",
      "type": "string"
    },
    "recovery": {
      "description": "添加恢复码时，此项包含要向用户显示的恢复码列表",
      "items": {
        "description": "恢复条目。",
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
