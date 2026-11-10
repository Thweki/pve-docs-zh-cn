# `/cluster/acme/challenge-schema`

原始接口路径：`/cluster/acme/challenge-schema`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/challenge-schema`

Get schema of ACME challenge types.

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
      "id": {
        "type": "string"
      },
      "name": {
        "description": "Human readable name, falls back to id",
        "type": "string"
      },
      "schema": {
        "type": "object"
      },
      "type": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/challenge-schema)。
