# `/access/openid/auth-url`

原始接口路径：`/access/openid/auth-url`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/openid/auth-url`

获取指定认证域的 OpenID 授权 URL。

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
| `realm` | string | 是 | — | 认证域 ID |
| `redirect-url` | string | 是 | — | 重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "realm": {
      "description": "认证域 ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    },
    "redirect-url": {
      "description": "重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。",
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
  "description": "重定向 URL。",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/openid/auth-url)。
