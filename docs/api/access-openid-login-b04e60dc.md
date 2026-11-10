# `/access/openid/login`

原始接口路径：`/access/openid/login`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/openid/login`

验证 OpenID 授权码并创建票据。

**方法标识：** `login`

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
| `code` | string | 是 | — | OpenID 授权码。 |
| `redirect-url` | string | 是 | — | 重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。 |
| `state` | string | 是 | — | OpenID 状态。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "code": {
      "description": "OpenID 授权码。",
      "maxLength": 4096,
      "type": "string",
      "typetext": "<string>"
    },
    "redirect-url": {
      "description": "重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。",
      "maxLength": 255,
      "type": "string",
      "typetext": "<string>"
    },
    "state": {
      "description": "OpenID 状态。",
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
