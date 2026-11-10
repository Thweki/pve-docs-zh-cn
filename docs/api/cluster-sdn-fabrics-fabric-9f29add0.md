# `/cluster/sdn/fabrics/fabric`

原始接口路径：`/cluster/sdn/fabrics/fabric`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/fabrics/fabric`

SDN Fabric 索引

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/sdn/fabrics/<fabric>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目",
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
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "properties": {
      "area": {
        "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。",
        "instance-types": [
          "ospf"
        ],
        "optional": 1,
        "type": "string",
        "type-property": "protocol"
      },
      "csnp_interval": {
        "description": "Openfabric 的 csnp_interval 属性",
        "instance-types": [
          "openfabric"
        ],
        "maximum": 600,
        "minimum": 1,
        "optional": 1,
        "type": "number",
        "type-property": "protocol"
      },
      "digest": {
        "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
        "maxLength": 64,
        "optional": 1,
        "type": "string"
      },
      "hello_interval": {
        "description": "Openfabric 的 hello_interval 属性",
        "instance-types": [
          "openfabric"
        ],
        "maximum": 600,
        "minimum": 1,
        "optional": 1,
        "type": "number",
        "type-property": "protocol"
      },
      "id": {
        "description": "SDN fabric 的标识符",
        "format": "pve-sdn-fabric-id",
        "maxLength": 8,
        "minLength": 2,
        "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
        "type": "string"
      },
      "ip6_prefix": {
        "description": "节点 IP 的 IP 前缀",
        "format": "CIDR",
        "optional": 1,
        "type": "string"
      },
      "ip_prefix": {
        "description": "节点 IP 的 IP 前缀",
        "format": "CIDR",
        "optional": 1,
        "type": "string"
      },
      "lock-token": {
        "description": "用于解锁全局 SDN 配置的令牌",
        "optional": 1,
        "type": "string"
      },
      "persistent_keepalive": {
        "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
        "instance-types": [
          "wireguard"
        ],
        "maximum": 65535,
        "minimum": 0,
        "optional": 1,
        "type": "number",
        "type-property": "protocol"
      },
      "protocol": {
        "description": "SDN Fabric 配置节中配置条目的类型",
        "enum": [
          "openfabric",
          "ospf",
          "wireguard",
          "bgp"
        ],
        "type": "string"
      },
      "redistribute": {
        "oneOf": [
          {
            "instance-types": [
              "ospf"
            ],
            "items": {
              "format": {
                "route-map": {
                  "description": "用于过滤或转换从此来源重分发的路由的路由映射。",
                  "format": "pve-sdn-route-map-id",
                  "optional": 1,
                  "type": "string"
                },
                "source": {
                  "description": "要从中重分发路由的协议。",
                  "enum": [
                    "bgp",
                    "connected",
                    "kernel",
                    "static"
                  ],
                  "type": "string"
                }
              },
              "type": "string"
            },
            "optional": 1,
            "type": "array"
          },
          {
            "instance-types": [
              "bgp"
            ],
            "items": {
              "format": {
                "route-map": {
                  "description": "用于过滤或转换从此来源重分发的路由的路由映射。",
                  "format": "pve-sdn-route-map-id",
                  "optional": 1,
                  "type": "string"
                },
                "source": {
                  "description": "要从中重分发路由的协议。",
                  "enum": [
                    "connected",
                    "kernel",
                    "ospf",
                    "static"
                  ],
                  "type": "string"
                }
              },
              "type": "string"
            },
            "optional": 1,
            "type": "array"
          }
        ],
        "type": "array",
        "type-property": "protocol"
      },
      "route_filter": {
        "description": "用于过滤将安装到内核路由表中的路由的前缀列表",
        "format": "pve-sdn-prefix-list-id",
        "instance-types": [
          "ospf",
          "openfabric"
        ],
        "optional": 1,
        "type": "string",
        "type-property": "protocol"
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

## POST `/cluster/sdn/fabrics/fabric`

添加 fabric

**方法标识：** `add_fabric`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/fabrics",
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
| `area` | string | 否 | — | OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。 |
| `csnp_interval` | number | 否 | — | Openfabric 的 csnp_interval 属性 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `hello_interval` | number | 否 | — | Openfabric 的 hello_interval 属性 |
| `id` | string | 是 | — | SDN fabric 的标识符 |
| `ip6_prefix` | string | 否 | — | 节点 IP 的 IP 前缀 |
| `ip_prefix` | string | 否 | — | 节点 IP 的 IP 前缀 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `persistent_keepalive` | number | 否 | — | 发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用 |
| `protocol` | string | 是 | — | SDN Fabric 配置节中配置条目的类型；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `redistribute` | array | 是 | — |  |
| `route_filter` | string | 否 | — | 用于过滤将安装到内核路由表中的路由的前缀列表 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "area": {
      "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。",
      "instance-types": [
        "ospf"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
      "typetext": "<string>"
    },
    "csnp_interval": {
      "description": "Openfabric 的 csnp_interval 属性",
      "instance-types": [
        "openfabric"
      ],
      "maximum": 600,
      "minimum": 1,
      "optional": 1,
      "type": "number",
      "type-property": "protocol",
      "typetext": "<number> (1 - 600)"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "hello_interval": {
      "description": "Openfabric 的 hello_interval 属性",
      "instance-types": [
        "openfabric"
      ],
      "maximum": 600,
      "minimum": 1,
      "optional": 1,
      "type": "number",
      "type-property": "protocol",
      "typetext": "<number> (1 - 600)"
    },
    "id": {
      "description": "SDN fabric 的标识符",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "ip6_prefix": {
      "description": "节点 IP 的 IP 前缀",
      "format": "CIDR",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ip_prefix": {
      "description": "节点 IP 的 IP 前缀",
      "format": "CIDR",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "persistent_keepalive": {
      "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
      "instance-types": [
        "wireguard"
      ],
      "maximum": 65535,
      "minimum": 0,
      "optional": 1,
      "type": "number",
      "type-property": "protocol",
      "typetext": "<number> (0 - 65535)"
    },
    "protocol": {
      "description": "SDN Fabric 配置节中配置条目的类型",
      "enum": [
        "openfabric",
        "ospf",
        "wireguard",
        "bgp"
      ],
      "type": "string"
    },
    "redistribute": {
      "oneOf": [
        {
          "instance-types": [
            "ospf"
          ],
          "items": {
            "format": {
              "route-map": {
                "description": "用于过滤或转换从此来源重分发的路由的路由映射。",
                "format": "pve-sdn-route-map-id",
                "optional": 1,
                "type": "string"
              },
              "source": {
                "description": "要从中重分发路由的协议。",
                "enum": [
                  "bgp",
                  "connected",
                  "kernel",
                  "static"
                ],
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "instance-types": [
            "bgp"
          ],
          "items": {
            "format": {
              "route-map": {
                "description": "用于过滤或转换从此来源重分发的路由的路由映射。",
                "format": "pve-sdn-route-map-id",
                "optional": 1,
                "type": "string"
              },
              "source": {
                "description": "要从中重分发路由的协议。",
                "enum": [
                  "connected",
                  "kernel",
                  "ospf",
                  "static"
                ],
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        }
      ],
      "type": "array",
      "type-property": "protocol",
      "typetext": "<array>"
    },
    "route_filter": {
      "description": "用于过滤将安装到内核路由表中的路由的前缀列表",
      "format": "pve-sdn-prefix-list-id",
      "instance-types": [
        "ospf",
        "openfabric"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/fabric)。
