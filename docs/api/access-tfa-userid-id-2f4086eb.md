# `/access/tfa/{userid}/{id}`

原始接口路径：`/access/tfa/{userid}/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/tfa/{userid}/{id}`

按 ID 删除 TFA 条目。

**方法标识：** `delete_tfa`

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
| `id` | string | 是 | — | TFA 条目 ID。 |
| `password` | string | 否 | — | 执行更改的用户的当前密码。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "TFA 条目 ID。",
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

## GET `/access/tfa/{userid}/{id}`

获取请求的 TFA 条目（如存在）。

**方法标识：** `get_tfa_entry`

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
| `id` | string | 是 | — | TFA 条目 ID。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "TFA 条目 ID。",
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
}
```

## PUT `/access/tfa/{userid}/{id}`

为用户添加 TFA 条目。

**方法标识：** `update_tfa_entry`

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
| `description` | string | 否 | — | 用于区分多个条目的描述 |
| `enable` | boolean | 否 | — | 是否应启用此条目用于登录。 |
| `id` | string | 是 | — | TFA 条目 ID。 |
| `password` | string | 否 | — | 执行更改的用户的当前密码。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "用于区分多个条目的描述",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "description": "是否应启用此条目用于登录。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "TFA 条目 ID。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa/{userid}/{id})。
