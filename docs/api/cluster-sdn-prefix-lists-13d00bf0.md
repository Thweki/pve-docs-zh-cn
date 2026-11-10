# `/cluster/sdn/prefix-lists`

原始接口路径：`/cluster/sdn/prefix-lists`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/prefix-lists`

列出前缀列表

**方法标识：** `list_prefix_lists`

**权限**

```json
{
  "description": "仅返回您具有 'SDN.Audit' 或 'SDN.Allocate' 权限的前缀列表条目。",
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
| `pending` | boolean | 否 | — | 显示待应用的配置。 |
| `running` | boolean | 否 | — | 显示运行中的配置。 |
| `verbose` | boolean | 否 | — | 如果为 0，则仅返回 id；否则返回所有属性。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "pending": {
      "description": "显示待应用的配置。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "running": {
      "description": "显示运行中的配置。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "verbose": {
      "description": "如果为 0，则仅返回 id；否则返回所有属性。",
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
  "items": {
    "properties": {},
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

## POST `/cluster/sdn/prefix-lists`

创建前缀列表

**方法标识：** `create_prefix_list_entry`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/prefix-lists",
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
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `entries` | array | 否 | — |  |
| `id` | string | 是 | — | SDN 前缀列表标识符 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
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
            "optional": 0,
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
            "optional": 0,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/prefix-lists)。
