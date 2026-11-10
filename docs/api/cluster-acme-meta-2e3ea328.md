# `/cluster/acme/meta`

原始接口路径：`/cluster/acme/meta`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/meta`

Retrieve ACME Directory Meta Information

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Audit"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `directory` | string | 否 | "https://acme-v02.api.letsencrypt.org/directory" | URL of ACME CA directory endpoint. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory",
      "description": "URL of ACME CA directory endpoint.",
      "optional": 1,
      "pattern": "^https?://.*",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "additionalProperties": 1,
  "properties": {
    "caaIdentities": {
      "description": "Hostnames referring to the ACME servers.",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "externalAccountRequired": {
      "description": "EAB Required",
      "optional": 1,
      "type": "boolean"
    },
    "termsOfService": {
      "description": "ACME TermsOfService URL.",
      "optional": 1,
      "type": "string"
    },
    "website": {
      "description": "URL to more information about the ACME server.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/meta)。
