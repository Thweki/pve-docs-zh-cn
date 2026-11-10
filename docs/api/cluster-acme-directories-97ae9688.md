# `/cluster/acme/directories`

原始接口路径：`/cluster/acme/directories`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/directories`

Get named known ACME directory endpoints.

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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "additionalProperties": 0,
    "properties": {
      "name": {
        "type": "string"
      },
      "url": {
        "description": "URL of ACME CA directory endpoint.",
        "pattern": "^https?://.*",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/directories)。
