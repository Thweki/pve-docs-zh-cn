# `/access/users/{userid}/tfa`

原始接口路径：`/access/users/{userid}/tfa`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/users/{userid}/tfa`

Get user TFA types (Personal and Realm).

**方法标识：** `read_user_tfa_type`

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
| `multiple` | boolean | 否 | 0 | Request all entries as an array. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "multiple": {
      "default": 0,
      "description": "Request all entries as an array.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "realm": {
      "description": "The type of TFA the users realm has set, if any.",
      "enum": [
        "oath",
        "yubico"
      ],
      "optional": 1,
      "type": "string"
    },
    "types": {
      "description": "Array of the user configured TFA types, if any. Only available if 'multiple' was not passed.",
      "items": {
        "description": "A TFA type.",
        "enum": [
          "totp",
          "u2f",
          "yubico",
          "webauthn",
          "recovedry"
        ],
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "user": {
      "description": "The type of TFA the user has set, if any. Only set if 'multiple' was not passed.",
      "enum": [
        "oath",
        "u2f"
      ],
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/tfa)。
