# `/access/openid/auth-url`

原始接口路径：`/access/openid/auth-url`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/openid/auth-url`

Get the OpenId Authorization Url for the specified realm.

**方法标识：** `auth_url`

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
| `realm` | string | 是 | — | Authentication domain ID |
| `redirect-url` | string | 是 | — | Redirection Url. The client should set this to the used server url (location.origin). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "realm": {
      "description": "Authentication domain ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    },
    "redirect-url": {
      "description": "Redirection Url. The client should set this to the used server url (location.origin).",
      "maxLength": 255,
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
  "description": "Redirection URL.",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/openid/auth-url)。
