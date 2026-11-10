# `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`

原始接口路径：`/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`

Delete Route Map Entry

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
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `order` | integer | 是 | — | The index of this route map entry |
| `route-map-id` | string | 是 | — | The SDN route map identifier |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "order": {
      "description": "The index of this route map entry",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer",
      "typetext": "<integer> (0 - 65535)"
    },
    "route-map-id": {
      "description": "The SDN route map identifier",
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

Get Route Map Entry

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
| `order` | integer | 是 | — | The index of this route map entry |
| `route-map-id` | string | 是 | — | The SDN route map identifier |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "order": {
      "description": "The index of this route map entry",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer",
      "typetext": "<integer> (0 - 65535)"
    },
    "route-map-id": {
      "description": "The SDN route map identifier",
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
      "description": "Matching policy of a route map entry.",
      "enum": [
        "permit",
        "deny"
      ],
      "optional": 0,
      "type": "string"
    },
    "call": {
      "description": "The SDN route map identifier",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
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
          "description": "The index of this route map entry",
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
            "description": "Value that the field <key> should be matched on.",
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
      "description": "The index of this route map entry",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer"
    },
    "route-map-id": {
      "description": "The SDN route map identifier",
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
            "description": "Value that the field <key> should be set to.",
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

Update Route Map Entry

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
| `action` | string | 否 | — | Matching policy of a route map entry.；可选值：`permit`, `deny` |
| `call` | string | 否 | — | The SDN route map identifier |
| `delete` | array | 否 | — |  |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `exit-action` | string | 否 | — |  |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `match` | array | 否 | — |  |
| `order` | integer | 是 | — | The index of this route map entry |
| `route-map-id` | string | 是 | — | The SDN route map identifier |
| `set` | array | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "action": {
      "description": "Matching policy of a route map entry.",
      "enum": [
        "permit",
        "deny"
      ],
      "optional": 1,
      "type": "string"
    },
    "call": {
      "description": "The SDN route map identifier",
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
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
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
          "description": "The index of this route map entry",
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
      "description": "the token for unlocking the global SDN configuration",
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
            "description": "Value that the field <key> should be matched on.",
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
      "description": "The index of this route map entry",
      "maximum": 65535,
      "minimum": 0,
      "type": "integer",
      "typetext": "<integer> (0 - 65535)"
    },
    "route-map-id": {
      "description": "The SDN route map identifier",
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
            "description": "Value that the field <key> should be set to.",
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
