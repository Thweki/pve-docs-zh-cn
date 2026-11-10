# `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`

原始接口路径：`/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`

添加节点

**方法标识：** `delete_node`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/sdn/fabrics/{fabric_id}",
      [
        "SDN.Allocate"
      ]
    ],
    [
      "perm",
      "/nodes/{node_id}",
      [
        "Sys.Modify"
      ]
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
| `fabric_id` | string | 是 | — | SDN fabric 的标识符 |
| `node_id` | string | 是 | — | SDN fabric 中节点的标识符 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "fabric_id": {
      "description": "SDN fabric 的标识符",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node_id": {
      "description": "SDN fabric 中节点的标识符",
      "format": "pve-node",
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

## GET `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`

获取节点

**方法标识：** `get_node`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/sdn/fabrics/{fabric_id}",
      [
        "SDN.Audit",
        "SDN.Allocate"
      ],
      "any",
      1
    ],
    [
      "perm",
      "/nodes/{node_id}",
      [
        "Sys.Audit",
        "Sys.Modify"
      ],
      "any",
      1
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
| `fabric_id` | string | 是 | — | SDN fabric 的标识符 |
| `node_id` | string | 是 | — | SDN fabric 中节点的标识符 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "fabric_id": {
      "description": "SDN fabric 的标识符",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node_id": {
      "description": "SDN fabric 中节点的标识符",
      "format": "pve-node",
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
    "allowed_ips": {
      "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。",
      "instance-types": [
        "wireguard"
      ],
      "items": {
        "format": "FullRangeCIDR",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "type-property": "protocol"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "endpoint": {
      "description": "用于连接此节点的端点。",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol"
    },
    "fabric_id": {
      "description": "SDN fabric 的标识符",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric 网络接口",
          "instance-types": [
            "openfabric"
          ],
          "items": {
            "format": {
              "hello_multiplier": {
                "description": "接口的 hello_multiplier 属性",
                "maximum": 100,
                "minimum": 2,
                "optional": 1,
                "type": "integer"
              },
              "ip": {
                "description": "此节点的 IPv4 地址",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "ip6": {
                "description": "此节点的 IPv6 地址",
                "format": "CIDRv6",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "网络接口名称",
                "format": "pve-iface",
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "OSPF 网络接口",
          "instance-types": [
            "ospf"
          ],
          "items": {
            "format": {
              "ip": {
                "description": "此节点的 IPv4 地址",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "网络接口名称",
                "format": "pve-iface",
                "type": "string"
              },
              "network_type": {
                "description": "OSPF 接口的网络类型",
                "enum": [
                  "broadcast",
                  "non-broadcast",
                  "point-to-multipoint",
                  "point-to-point"
                ],
                "optional": 1,
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "此节点的 WireGuard 网络接口列表。",
          "instance-types": [
            "wireguard"
          ],
          "items": {
            "description": "WireGuard 网络接口",
            "format": "pve-sdn-fabric-wireguard-interface",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "BGP 网络接口",
          "instance-types": [
            "bgp"
          ],
          "items": {
            "format": {
              "name": {
                "description": "网络接口名称",
                "format": "pve-iface",
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1
        }
      ],
      "type": "array",
      "type-property": "protocol"
    },
    "ip": {
      "description": "此节点的 IPv4 地址",
      "format": "ipv4",
      "optional": 1,
      "type": "string"
    },
    "ip6": {
      "description": "此节点的 IPv6 地址",
      "format": "ipv6",
      "optional": 1,
      "type": "string"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string"
    },
    "node_id": {
      "description": "SDN fabric 中节点的标识符",
      "format": "pve-node",
      "type": "string"
    },
    "peers": {
      "instance-types": [
        "wireguard"
      ],
      "items": {
        "format": {
          "endpoint": {
            "description": "覆盖节点配置节中的端点设置。",
            "optional": 1,
            "type": "string"
          },
          "iface": {
            "description": "此节点使用此对等端定义的接口。",
            "type": "string"
          },
          "node": {
            "description": "所引用节点配置节的名称（外部节点或内部对等节点）。",
            "type": "string"
          },
          "node_iface": {
            "description": "另一个节点的接口（如果它是内部节点）",
            "optional": 1,
            "type": "string"
          },
          "skip_route_generation": {
            "default": 0,
            "description": "是否应在内核路由表中为允许的 IP 创建路由。",
            "optional": 1,
            "type": "boolean"
          },
          "type": {
            "enum": [
              "internal",
              "external"
            ],
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array",
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
    "public_key": {
      "description": "外部节点的公钥。",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol"
    },
    "role": {
      "description": "此节点在 WireGuard fabric 中的角色。",
      "enum": [
        "internal",
        "external"
      ],
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol"
    }
  }
}
```

## PUT `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`

更新节点

**方法标识：** `update_node`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/sdn/fabrics/{fabric_id}",
      [
        "SDN.Allocate"
      ]
    ],
    [
      "perm",
      "/nodes/{node_id}",
      [
        "Sys.Modify"
      ]
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
| `allowed_ips` | array | 否 | — | WireGuard fabric 中可经由此节点路由的 IP 列表。 |
| `delete` | array | 是 | — |  |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `endpoint` | string | 否 | — | 用于连接此节点的端点。 |
| `fabric_id` | string | 是 | — | SDN fabric 的标识符 |
| `interfaces` | array | 是 | — |  |
| `ip` | string | 否 | — | 此节点的 IPv4 地址 |
| `ip6` | string | 否 | — | 此节点的 IPv6 地址 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `node_id` | string | 是 | — | SDN fabric 中节点的标识符 |
| `peers` | array | 否 | — |  |
| `protocol` | string | 是 | — | SDN Fabric 配置节中配置条目的类型；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `public_key` | string | 否 | — | 外部节点的公钥。 |
| `role` | string | 否 | — | 此节点在 WireGuard fabric 中的角色。；可选值：`internal`, `external` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "allowed_ips": {
      "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。",
      "instance-types": [
        "wireguard"
      ],
      "items": {
        "format": "FullRangeCIDR",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "type-property": "protocol",
      "typetext": "<array>"
    },
    "delete": {
      "oneOf": [
        {
          "instance-types": [
            "bgp"
          ],
          "items": {
            "enum": [
              "interfaces",
              "ip",
              "ip6"
            ],
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "instance-types": [
            "openfabric",
            "ospf"
          ],
          "items": {
            "enum": [
              "interfaces",
              "ip",
              "ip6"
            ],
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "instance-types": [
            "wireguard"
          ],
          "items": {
            "enum": [
              "allowed_ips",
              "endpoint",
              "interfaces",
              "ip",
              "ip6",
              "peers"
            ],
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
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "endpoint": {
      "description": "用于连接此节点的端点。",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
      "typetext": "<string>"
    },
    "fabric_id": {
      "description": "SDN fabric 的标识符",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric 网络接口",
          "instance-types": [
            "openfabric"
          ],
          "items": {
            "format": {
              "hello_multiplier": {
                "description": "接口的 hello_multiplier 属性",
                "maximum": 100,
                "minimum": 2,
                "optional": 1,
                "type": "integer"
              },
              "ip": {
                "description": "此节点的 IPv4 地址",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "ip6": {
                "description": "此节点的 IPv6 地址",
                "format": "CIDRv6",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "网络接口名称",
                "format": "pve-iface",
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "OSPF 网络接口",
          "instance-types": [
            "ospf"
          ],
          "items": {
            "format": {
              "ip": {
                "description": "此节点的 IPv4 地址",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "网络接口名称",
                "format": "pve-iface",
                "type": "string"
              },
              "network_type": {
                "description": "OSPF 接口的网络类型",
                "enum": [
                  "broadcast",
                  "non-broadcast",
                  "point-to-multipoint",
                  "point-to-point"
                ],
                "optional": 1,
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "此节点的 WireGuard 网络接口列表。",
          "instance-types": [
            "wireguard"
          ],
          "items": {
            "description": "WireGuard 网络接口",
            "format": "pve-sdn-fabric-wireguard-interface",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "BGP 网络接口",
          "instance-types": [
            "bgp"
          ],
          "items": {
            "format": {
              "name": {
                "description": "网络接口名称",
                "format": "pve-iface",
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1
        }
      ],
      "type": "array",
      "type-property": "protocol",
      "typetext": "<array>"
    },
    "ip": {
      "description": "此节点的 IPv4 地址",
      "format": "ipv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ip6": {
      "description": "此节点的 IPv6 地址",
      "format": "ipv6",
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
    "node_id": {
      "description": "SDN fabric 中节点的标识符",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "peers": {
      "instance-types": [
        "wireguard"
      ],
      "items": {
        "format": {
          "endpoint": {
            "description": "覆盖节点配置节中的端点设置。",
            "optional": 1,
            "type": "string"
          },
          "iface": {
            "description": "此节点使用此对等端定义的接口。",
            "type": "string"
          },
          "node": {
            "description": "所引用节点配置节的名称（外部节点或内部对等节点）。",
            "type": "string"
          },
          "node_iface": {
            "description": "另一个节点的接口（如果它是内部节点）",
            "optional": 1,
            "type": "string"
          },
          "skip_route_generation": {
            "default": 0,
            "description": "是否应在内核路由表中为允许的 IP 创建路由。",
            "optional": 1,
            "type": "boolean"
          },
          "type": {
            "enum": [
              "internal",
              "external"
            ],
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "type-property": "protocol",
      "typetext": "<array>"
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
    "public_key": {
      "description": "外部节点的公钥。",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
      "typetext": "<string>"
    },
    "role": {
      "description": "此节点在 WireGuard fabric 中的角色。",
      "enum": [
        "internal",
        "external"
      ],
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/node/{fabric_id}/{node_id})。
