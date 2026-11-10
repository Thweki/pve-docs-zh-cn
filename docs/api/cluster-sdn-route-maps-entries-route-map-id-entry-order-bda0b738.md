# `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`

原始接口路径：`/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`

删除路由映射条目

**方法标识：** `delete_route_map_entry`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/route-maps/{route-map-id}",
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
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `order` | integer | 是 | — | 此路由映射条目的索引 |
| `route-map-id` | string | 是 | — | SDN 路由映射标识符 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "order": {
      "description": "此路由映射条目的索引",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer",
      "typetext": "<integer> (0 - 65535)"
    },
    "route-map-id": {
      "description": "SDN 路由映射标识符",
      "format": "pve-sdn-route-map-id",
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

## GET `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`

获取路由映射条目

**方法标识：** `get_route_map_entry`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/route-maps/{route-map-id}",
    [
      "SDN.Audit",
      "SDN.Allocate"
    ],
    "any",
    1
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
| `order` | integer | 是 | — | 此路由映射条目的索引 |
| `route-map-id` | string | 是 | — | SDN 路由映射标识符 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "order": {
      "description": "此路由映射条目的索引",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer",
      "typetext": "<integer> (0 - 65535)"
    },
    "route-map-id": {
      "description": "SDN 路由映射标识符",
      "format": "pve-sdn-route-map-id",
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
  "properties": {
    "action": {
      "description": "路由映射条目的匹配策略。",
      "enum": [
        "permit",
        "deny"
      ],
      "optional": 0,
      "type": "string"
    },
    "call": {
      "description": "SDN 路由映射标识符",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "exit-action": {
      "format": {
        "key": {
          "enum": [
            "on-match-goto",
            "on-match-next",
            "continue"
          ],
          "type": "string"
        },
        "value": {
          "description": "此路由映射条目的索引",
          "maximum": 65535,
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "match": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "route-type",
              "vni",
              "ip-address-prefix-list",
              "ip6-address-prefix-list",
              "ip-next-hop-prefix-list",
              "ip6-next-hop-prefix-list",
              "ip-next-hop-address",
              "ip6-next-hop-address",
              "metric",
              "local-preference",
              "peer",
              "tag"
            ],
            "type": "string"
          },
          "value": {
            "description": "字段 <key> 应匹配的值。",
            "format_description": "<key-dependent>",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "order": {
      "description": "此路由映射条目的索引",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer"
    },
    "route-map-id": {
      "description": "SDN 路由映射标识符",
      "format": "pve-sdn-route-map-id",
      "type": "string"
    },
    "set": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "ip-next-hop-peer-address",
              "ip-next-hop",
              "ip-next-hop-unchanged",
              "ip6-next-hop-peer-address",
              "ip6-next-hop-prefer-global",
              "ip6-next-hop",
              "local-preference",
              "tag",
              "weight",
              "metric",
              "src"
            ],
            "type": "string"
          },
          "value": {
            "description": "字段 <key> 应设置的值。",
            "format_description": "<key-dependent>",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`

更新路由映射条目

**方法标识：** `update_route_map_entry`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/route-maps/{route-map-id}",
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
| `action` | string | 否 | — | 路由映射条目的匹配策略。；可选值：`permit`, `deny` |
| `call` | string | 否 | — | SDN 路由映射标识符 |
| `delete` | array | 否 | — |  |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `exit-action` | string | 否 | — |  |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `match` | array | 否 | — |  |
| `order` | integer | 是 | — | 此路由映射条目的索引 |
| `route-map-id` | string | 是 | — | SDN 路由映射标识符 |
| `set` | array | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "action": {
      "description": "路由映射条目的匹配策略。",
      "enum": [
        "permit",
        "deny"
      ],
      "optional": 1,
      "type": "string"
    },
    "call": {
      "description": "SDN 路由映射标识符",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "items": {
        "enum": [
          "set",
          "match",
          "call",
          "exit-action"
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
    "exit-action": {
      "format": {
        "key": {
          "enum": [
            "on-match-goto",
            "on-match-next",
            "continue"
          ],
          "type": "string"
        },
        "value": {
          "description": "此路由映射条目的索引",
          "maximum": 65535,
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "key=<on-match-goto|on-match-next|continue> [,value=<integer>]"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "match": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "route-type",
              "vni",
              "ip-address-prefix-list",
              "ip6-address-prefix-list",
              "ip-next-hop-prefix-list",
              "ip6-next-hop-prefix-list",
              "ip-next-hop-address",
              "ip6-next-hop-address",
              "metric",
              "local-preference",
              "peer",
              "tag"
            ],
            "type": "string"
          },
          "value": {
            "description": "字段 <key> 应匹配的值。",
            "format_description": "<key-dependent>",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "order": {
      "description": "此路由映射条目的索引",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer",
      "typetext": "<integer> (0 - 65535)"
    },
    "route-map-id": {
      "description": "SDN 路由映射标识符",
      "format": "pve-sdn-route-map-id",
      "type": "string",
      "typetext": "<string>"
    },
    "set": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "ip-next-hop-peer-address",
              "ip-next-hop",
              "ip-next-hop-unchanged",
              "ip6-next-hop-peer-address",
              "ip6-next-hop-prefer-global",
              "ip6-next-hop",
              "local-preference",
              "tag",
              "weight",
              "metric",
              "src"
            ],
            "type": "string"
          },
          "value": {
            "description": "字段 <key> 应设置的值。",
            "format_description": "<key-dependent>",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order})。
