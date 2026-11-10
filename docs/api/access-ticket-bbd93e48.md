# `/access/ticket`

原始接口路径：`/access/ticket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/ticket`

Dummy. Useful for formatters which want to provide a login page.

**权限**

```json
{
  "user": "world"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "type": "null"
}
```

## POST `/access/ticket`

Create or verify authentication ticket.

**权限**

```json
{
  "description": "You need to pass valid credientials.",
  "user": "world"
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
| `new-format` | boolean | 否 | 1 | This parameter is now ignored and assumed to be 1. |
| `otp` | string | 否 | — | One-time password for Two-factor authentication. |
| `password` | string | 是 | — | The secret password. This can also be a valid ticket. |
| `path` | string | 否 | — | Verify ticket, and check if user have access 'privs' on 'path' |
| `privs` | string | 否 | — | Verify ticket, and check if user have access 'privs' on 'path' |
| `realm` | string | 否 | — | You can optionally pass the realm using this parameter. Normally the realm is simply added to the username <username>@<realm>. |
| `tfa-challenge` | string | 否 | — | The signed TFA challenge string the user wants to respond to. |
| `username` | string | 是 | — | User name |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "new-format": {
      "default": 1,
      "description": "This parameter is now ignored and assumed to be 1.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "otp": {
      "description": "One-time password for Two-factor authentication.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "The secret password. This can also be a valid ticket.",
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "Verify ticket, and check if user have access 'privs' on 'path'",
      "maxLength": 64,
      "optional": 1,
      "requires": "privs",
      "type": "string",
      "typetext": "<string>"
    },
    "privs": {
      "description": "Verify ticket, and check if user have access 'privs' on 'path'",
      "format": "pve-priv-list",
      "maxLength": 64,
      "optional": 1,
      "requires": "path",
      "type": "string",
      "typetext": "<string>"
    },
    "realm": {
      "description": "You can optionally pass the realm using this parameter. Normally the realm is simply added to the username <username>@<realm>.",
      "format": "pve-realm",
      "maxLength": 32,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tfa-challenge": {
      "description": "The signed TFA challenge string the user wants to respond to.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "User name",
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
    "CSRFPreventionToken": {
      "optional": 1,
      "type": "string"
    },
    "clustername": {
      "optional": 1,
      "type": "string"
    },
    "ticket": {
      "optional": 1,
      "type": "string"
    },
    "username": {
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/ticket)。
