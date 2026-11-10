# `/cluster/acme/account`

原始接口路径：`/cluster/acme/account`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/account`

ACMEAccount 索引。

**方法标识：** `account_index`

**权限**

```json
{
  "user": "all"
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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {},
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/acme/account`

向 CA 注册新的 ACME 账户。

**方法标识：** `register_account`

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
| `contact` | string | 是 | — | 联系电子邮件地址。 |
| `directory` | string | 否 | "https://acme-v02.api.letsencrypt.org/directory" | ACME CA 目录端点的 URL。 |
| `eab-hmac-key` | string | 否 | — | 外部账户绑定的 HMAC 密钥。 |
| `eab-kid` | string | 否 | — | 外部账户绑定的密钥标识符。 |
| `name` | string | 否 | "default" | ACME 账户配置文件名。 |
| `tos_url` | string | 否 | — | CA 服务条款的 URL——设置此项表示同意条款。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "contact": {
      "description": "联系电子邮件地址。",
      "format": "email-list",
      "type": "string",
      "typetext": "<string>"
    },
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory",
      "description": "ACME CA 目录端点的 URL。",
      "optional": 1,
      "pattern": "^https?://.*",
      "type": "string"
    },
    "eab-hmac-key": {
      "description": "外部账户绑定的 HMAC 密钥。",
      "optional": 1,
      "requires": "eab-kid",
      "type": "string",
      "typetext": "<string>"
    },
    "eab-kid": {
      "description": "外部账户绑定的密钥标识符。",
      "optional": 1,
      "requires": "eab-hmac-key",
      "type": "string",
      "typetext": "<string>"
    },
    "name": {
      "default": "default",
      "description": "ACME 账户配置文件名。",
      "format": "pve-configid",
      "format_description": "name",
      "optional": 1,
      "type": "string",
      "typetext": "<name>"
    },
    "tos_url": {
      "description": "CA 服务条款的 URL——设置此项表示同意条款。",
      "optional": 1,
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/account)。
