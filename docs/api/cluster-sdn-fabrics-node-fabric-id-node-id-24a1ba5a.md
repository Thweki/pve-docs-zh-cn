# `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`

原始接口路径：`/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`

Add a node

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
| `fabric_id` | string | 是 | — | Identifier for SDN fabrics |
| `node_id` | string | 是 | — | Identifier for nodes in an SDN fabric |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "fabric_id": {
      "description": "Identifier for SDN fabrics",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node_id": {
      "description": "Identifier for nodes in an SDN fabric",
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

Get a node

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
| `fabric_id` | string | 是 | — | Identifier for SDN fabrics |
| `node_id` | string | 是 | — | Identifier for nodes in an SDN fabric |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "fabric_id": {
      "description": "Identifier for SDN fabrics",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node_id": {
      "description": "Identifier for nodes in an SDN fabric",
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
      "description": "A list of IPs that are routable via this node in the WireGuard fabric.",
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
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "endpoint": {
      "description": "The endpoint used for connecting to this node.",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol"
    },
    "fabric_id": {
      "description": "Identifier for SDN fabrics",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric network interface",
          "instance-types": [
            "openfabric"
          ],
          "items": {
            "format": {
              "hello_multiplier": {
                "description": "The hello_multiplier property of the interface",
                "maximum": 100,
                "minimum": 2,
                "optional": 1,
                "type": "integer"
              },
              "ip": {
                "description": "IPv4 address for this node",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "ip6": {
                "description": "IPv6 address for this node",
                "format": "CIDRv6",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "Name of the network interface",
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
          "description": "OSPF network interface",
          "instance-types": [
            "ospf"
          ],
          "items": {
            "format": {
              "ip": {
                "description": "IPv4 address for this node",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "Name of the network interface",
                "format": "pve-iface",
                "type": "string"
              },
              "network_type": {
                "description": "Network Type of the OSPF interface",
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
          "description": "List of WireGuard network interfaces for this node.",
          "instance-types": [
            "wireguard"
          ],
          "items": {
            "description": "WireGuard network interface",
            "format": "pve-sdn-fabric-wireguard-interface",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "BGP network interface",
          "instance-types": [
            "bgp"
          ],
          "items": {
            "format": {
              "name": {
                "description": "Name of the network interface",
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
      "description": "IPv4 address for this node",
      "format": "ipv4",
      "optional": 1,
      "type": "string"
    },
    "ip6": {
      "description": "IPv6 address for this node",
      "format": "ipv6",
      "optional": 1,
      "type": "string"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string"
    },
    "node_id": {
      "description": "Identifier for nodes in an SDN fabric",
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
            "description": "Override for the endpoint settings in the node section.",
            "optional": 1,
            "type": "string"
          },
          "iface": {
            "description": "The interface of this node that uses this peer definition.",
            "type": "string"
          },
          "node": {
            "description": "The name of the referenced node section (the external node or the internal peer node).",
            "type": "string"
          },
          "node_iface": {
            "description": "The interface of the other node, if it is internal",
            "optional": 1,
            "type": "string"
          },
          "skip_route_generation": {
            "default": 0,
            "description": "Whether routes for the allowed IPs should be created in the kernel routing table.",
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
      "description": "Type of configuration entry in an SDN Fabric section config",
      "enum": [
        "openfabric",
        "ospf",
        "wireguard",
        "bgp"
      ],
      "type": "string"
    },
    "public_key": {
      "description": "The public key for the external node.",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol"
    },
    "role": {
      "description": "The role of this node in the WireGuard fabric.",
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

Update a node

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
| `allowed_ips` | array | 否 | — | A list of IPs that are routable via this node in the WireGuard fabric. |
| `delete` | array | 是 | — |  |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `endpoint` | string | 否 | — | The endpoint used for connecting to this node. |
| `fabric_id` | string | 是 | — | Identifier for SDN fabrics |
| `interfaces` | array | 是 | — |  |
| `ip` | string | 否 | — | IPv4 address for this node |
| `ip6` | string | 否 | — | IPv6 address for this node |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `node_id` | string | 是 | — | Identifier for nodes in an SDN fabric |
| `peers` | array | 否 | — |  |
| `protocol` | string | 是 | — | Type of configuration entry in an SDN Fabric section config；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `public_key` | string | 否 | — | The public key for the external node. |
| `role` | string | 否 | — | The role of this node in the WireGuard fabric.；可选值：`internal`, `external` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "allowed_ips": {
      "description": "A list of IPs that are routable via this node in the WireGuard fabric.",
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
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "endpoint": {
      "description": "The endpoint used for connecting to this node.",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
      "typetext": "<string>"
    },
    "fabric_id": {
      "description": "Identifier for SDN fabrics",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric network interface",
          "instance-types": [
            "openfabric"
          ],
          "items": {
            "format": {
              "hello_multiplier": {
                "description": "The hello_multiplier property of the interface",
                "maximum": 100,
                "minimum": 2,
                "optional": 1,
                "type": "integer"
              },
              "ip": {
                "description": "IPv4 address for this node",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "ip6": {
                "description": "IPv6 address for this node",
                "format": "CIDRv6",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "Name of the network interface",
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
          "description": "OSPF network interface",
          "instance-types": [
            "ospf"
          ],
          "items": {
            "format": {
              "ip": {
                "description": "IPv4 address for this node",
                "format": "CIDRv4",
                "optional": 1,
                "type": "string"
              },
              "name": {
                "description": "Name of the network interface",
                "format": "pve-iface",
                "type": "string"
              },
              "network_type": {
                "description": "Network Type of the OSPF interface",
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
          "description": "List of WireGuard network interfaces for this node.",
          "instance-types": [
            "wireguard"
          ],
          "items": {
            "description": "WireGuard network interface",
            "format": "pve-sdn-fabric-wireguard-interface",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        {
          "description": "BGP network interface",
          "instance-types": [
            "bgp"
          ],
          "items": {
            "format": {
              "name": {
                "description": "Name of the network interface",
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
      "description": "IPv4 address for this node",
      "format": "ipv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ip6": {
      "description": "IPv6 address for this node",
      "format": "ipv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node_id": {
      "description": "Identifier for nodes in an SDN fabric",
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
            "description": "Override for the endpoint settings in the node section.",
            "optional": 1,
            "type": "string"
          },
          "iface": {
            "description": "The interface of this node that uses this peer definition.",
            "type": "string"
          },
          "node": {
            "description": "The name of the referenced node section (the external node or the internal peer node).",
            "type": "string"
          },
          "node_iface": {
            "description": "The interface of the other node, if it is internal",
            "optional": 1,
            "type": "string"
          },
          "skip_route_generation": {
            "default": 0,
            "description": "Whether routes for the allowed IPs should be created in the kernel routing table.",
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
      "description": "Type of configuration entry in an SDN Fabric section config",
      "enum": [
        "openfabric",
        "ospf",
        "wireguard",
        "bgp"
      ],
      "type": "string"
    },
    "public_key": {
      "description": "The public key for the external node.",
      "instance-types": [
        "wireguard"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
      "typetext": "<string>"
    },
    "role": {
      "description": "The role of this node in the WireGuard fabric.",
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
