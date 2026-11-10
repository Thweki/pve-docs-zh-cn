# `/cluster/sdn`

原始接口路径：`/cluster/sdn`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn`

Directory index.

**权限**

```json
{
  "check": [
    "perm",
    "/sdn",
    [
      "SDN.Audit"
    ]
  ]
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
    "properties": {
      "id": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## PUT `/cluster/sdn`

Apply sdn controller changes && reload.

**权限**

```json
{
  "check": [
    "perm",
    "/sdn",
    [
      "SDN.Allocate"
    ]
  ]
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
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `release-lock` | boolean | 否 | 1 | When lock-token has been provided and configuration successfully committed, release the lock automatically afterwards |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "release-lock": {
      "default": 1,
      "description": "When lock-token has been provided and configuration successfully committed, release the lock automatically afterwards",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn)。
