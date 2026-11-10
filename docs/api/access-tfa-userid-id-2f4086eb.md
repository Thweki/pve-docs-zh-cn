# `/access/tfa/{userid}/{id}`

原始接口路径：`/access/tfa/{userid}/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/tfa/{userid}/{id}`

Delete a TFA entry by ID.

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
| `id` | string | 是 | — | A TFA entry id. |
| `password` | string | 否 | — | The current password of the user performing the change. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "A TFA entry id.",
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

## GET `/access/tfa/{userid}/{id}`

Fetch a requested TFA entry if present.

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
| `id` | string | 是 | — | A TFA entry id. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "A TFA entry id.",
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
}
```

## PUT `/access/tfa/{userid}/{id}`

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
| `description` | string | 否 | — | A description to distinguish multiple entries from one another |
| `enable` | boolean | 否 | — | Whether the entry should be enabled for login. |
| `id` | string | 是 | — | A TFA entry id. |
| `password` | string | 否 | — | The current password of the user performing the change. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "A description to distinguish multiple entries from one another",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "description": "Whether the entry should be enabled for login.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "A TFA entry id.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa/{userid}/{id})。
