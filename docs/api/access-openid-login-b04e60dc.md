# `/access/openid/login`

原始接口路径：`/access/openid/login`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/openid/login`

Verify OpenID authorization code and create a ticket.

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

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `code` | string | 是 | — | OpenId authorization code. |
| `redirect-url` | string | 是 | — | Redirection Url. The client should set this to the used server url (location.origin). |
| `state` | string | 是 | — | OpenId state. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "code": {
      "description": "OpenId authorization code.",
      "maxLength": 4096,
      "type": "string",
      "typetext": "<string>"
    },
    "redirect-url": {
      "description": "Redirection Url. The client should set this to the used server url (location.origin).",
      "maxLength": 255,
      "type": "string",
      "typetext": "<string>"
    },
    "state": {
      "description": "OpenId state.",
      "maxLength": 1024,
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
      "type": "string"
    },
    "cap": {
      "type": "object"
    },
    "clustername": {
      "optional": 1,
      "type": "string"
    },
    "ticket": {
      "type": "string"
    },
    "username": {
      "type": "string"
    }
  }
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/openid/login)。
