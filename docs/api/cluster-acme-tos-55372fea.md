# `/cluster/acme/tos`

原始接口路径：`/cluster/acme/tos`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/tos`

从 CA 获取 ACME 服务条款 URL。已弃用，请使用 /cluster/acme/meta.

**方法标识：** `get_tos`

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
| `directory` | string | 否 | "https://acme-v02.api.letsencrypt.org/directory" | ACME CA 目录端点的 URL。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory",
      "description": "ACME CA 目录端点的 URL。",
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
  "description": "ACME 服务条款 URL。",
  "optional": 1,
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/tos)。
