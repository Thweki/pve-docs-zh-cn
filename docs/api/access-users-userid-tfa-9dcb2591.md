# `/access/users/{userid}/tfa`

原始接口路径：`/access/users/{userid}/tfa`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/users/{userid}/tfa`

获取用户 TFA 类型（个人及认证域）。

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
| `multiple` | boolean | 否 | 0 | 将所有条目作为数组请求。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "multiple": {
      "default": 0,
      "description": "将所有条目作为数组请求。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "realm": {
      "description": "用户所属认证域设置的 TFA 类型（如有）。",
      "enum": [
        "oath",
        "yubico"
      ],
      "optional": 1,
      "type": "string"
    },
    "types": {
      "description": "用户配置的 TFA 类型数组（如有）。仅在未传入 'multiple' 时可用。",
      "items": {
        "description": "TFA 类型。",
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
      "description": "用户设置的 TFA 类型（如有）。仅在未传入 'multiple' 时设置。",
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
