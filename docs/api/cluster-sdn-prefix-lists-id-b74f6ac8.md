# `/cluster/sdn/prefix-lists/{id}`

原始接口路径：`/cluster/sdn/prefix-lists/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/prefix-lists/{id}`

删除前缀列表

**方法标识：** `delete_prefix_list`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/prefix-lists/{id}",
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
| `id` | string | 是 | — | SDN 前缀列表标识符 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "id": {
      "description": "SDN 前缀列表标识符",
      "format": "pve-sdn-prefix-list-id",
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
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
  "type": "null"
}
```

## GET `/cluster/sdn/prefix-lists/{id}`

获取前缀列表

**方法标识：** `get_prefix_list`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/prefix-lists/{id}",
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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | — | SDN 前缀列表标识符 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "id": {
      "description": "SDN 前缀列表标识符",
      "format": "pve-sdn-prefix-list-id",
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
  "type": "object"
}
```

## PUT `/cluster/sdn/prefix-lists/{id}`

更新前缀列表

**方法标识：** `update_prefix_list`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/prefix-lists/{id}",
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
| `delete` | array | 否 | — |  |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `entries` | array | 否 | — |  |
| `id` | string | 是 | — | SDN 前缀列表标识符 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "delete": {
      "items": {
        "enum": [
          "entries"
        ],
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "entries": {
      "items": {
        "format": {
          "action": {
            "enum": [
              "permit",
              "deny"
            ],
            "optional": 1,
            "type": "string"
          },
          "ge": {
            "maximum": 128,
            "minimum": 0,
            "optional": 1,
            "type": "integer"
          },
          "le": {
            "maximum": 128,
            "minimum": 0,
            "optional": 1,
            "type": "integer"
          },
          "prefix": {
            "format": "FullRangeCIDR",
            "optional": 1,
            "type": "string"
          },
          "seq": {
            "maximum": 4294967295,
            "minimum": 1,
            "optional": 1,
            "type": "integer"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "id": {
      "description": "SDN 前缀列表标识符",
      "format": "pve-sdn-prefix-list-id",
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/prefix-lists/{id})。
