# `/access/ticket`

原始接口路径：`/access/ticket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/ticket`

占位项。适用于希望提供登录页面的格式化程序。

**方法标识：** `get_ticket`

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

创建或验证认证票据。

**方法标识：** `create_ticket`

**权限**

```json
{
  "description": "需要传入有效凭据。",
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
| `new-format` | boolean | 否 | 1 | 此参数现在被忽略，并假定为 1。 |
| `otp` | string | 否 | — | 双因素身份验证的一次性密码。 |
| `password` | string | 是 | — | 秘密密码。也可以是有效票据。 |
| `path` | string | 否 | — | 验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `privs` | string | 否 | — | 验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `realm` | string | 否 | — | 可以选择使用此参数传入认证域。通常只需将认证域添加到用户名后，形式为 &lt;username&gt;@&lt;realm&gt;。 |
| `tfa-challenge` | string | 否 | — | 用户要响应的已签名 TFA 质询字符串。 |
| `username` | string | 是 | — | 用户名 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "new-format": {
      "default": 1,
      "description": "此参数现在被忽略，并假定为 1。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "otp": {
      "description": "双因素身份验证的一次性密码。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "秘密密码。也可以是有效票据。",
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限",
      "maxLength": 64,
      "optional": 1,
      "requires": "privs",
      "type": "string",
      "typetext": "<string>"
    },
    "privs": {
      "description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限",
      "format": "pve-priv-list",
      "maxLength": 64,
      "optional": 1,
      "requires": "path",
      "type": "string",
      "typetext": "<string>"
    },
    "realm": {
      "description": "可以选择使用此参数传入认证域。通常只需将认证域添加到用户名后，形式为 <username>@<realm>。",
      "format": "pve-realm",
      "maxLength": 32,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tfa-challenge": {
      "description": "用户要响应的已签名 TFA 质询字符串。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "用户名",
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
