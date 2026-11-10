# `/cluster/acme/tos`

原始接口路径：`/cluster/acme/tos`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/tos`

Retrieve ACME TermsOfService URL from CA. Deprecated, please use /cluster/acme/meta.

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
  "description": "ACME TermsOfService URL.",
  "optional": 1,
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/tos)。
