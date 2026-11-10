# `/cluster/acme/account`

原始接口路径：`/cluster/acme/account`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/account`

ACMEAccount index.

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

Register a new ACME account with CA.

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
| `contact` | string | 是 | — | Contact email addresses. |
| `directory` | string | 否 | "https://acme-v02.api.letsencrypt.org/directory" | URL of ACME CA directory endpoint. |
| `eab-hmac-key` | string | 否 | — | HMAC key for External Account Binding. |
| `eab-kid` | string | 否 | — | Key Identifier for External Account Binding. |
| `name` | string | 否 | "default" | ACME account config file name. |
| `tos_url` | string | 否 | — | URL of CA TermsOfService - setting this indicates agreement. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "contact": {
      "description": "Contact email addresses.",
      "format": "email-list",
      "type": "string",
      "typetext": "<string>"
    },
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory",
      "description": "URL of ACME CA directory endpoint.",
      "optional": 1,
      "pattern": "^https?://.*",
      "type": "string"
    },
    "eab-hmac-key": {
      "description": "HMAC key for External Account Binding.",
      "optional": 1,
      "requires": "eab-kid",
      "type": "string",
      "typetext": "<string>"
    },
    "eab-kid": {
      "description": "Key Identifier for External Account Binding.",
      "optional": 1,
      "requires": "eab-hmac-key",
      "type": "string",
      "typetext": "<string>"
    },
    "name": {
      "default": "default",
      "description": "ACME account config file name.",
      "format": "pve-configid",
      "format_description": "name",
      "optional": 1,
      "type": "string",
      "typetext": "<name>"
    },
    "tos_url": {
      "description": "URL of CA TermsOfService - setting this indicates agreement.",
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
