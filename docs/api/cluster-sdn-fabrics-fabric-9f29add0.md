# `/cluster/sdn/fabrics/fabric`

原始接口路径：`/cluster/sdn/fabrics/fabric`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/fabrics/fabric`

SDN Fabrics Index

**方法标识：** `index`

**权限**

```json
{
  "description": "Only list entries where you have 'SDN.Audit' or 'SDN.Allocate' permissions on '/sdn/fabrics/<fabric>'",
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
| `pending` | boolean | 否 | — | Display pending config. |
| `running` | boolean | 否 | — | Display running config. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "pending": {
      "description": "Display pending config.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "running": {
      "description": "Display running config.",
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
        "description": "OSPF area. Either a IPv4 address or a 32-bit number. Gets validated in rust.",
        "instance-types": [
          "ospf"
        ],
        "optional": 1,
        "type": "string",
        "type-property": "protocol"
      },
      "csnp_interval": {
        "description": "The csnp_interval property for Openfabric",
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
        "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
        "maxLength": 64,
        "optional": 1,
        "type": "string"
      },
      "hello_interval": {
        "description": "The hello_interval property for Openfabric",
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
        "description": "Identifier for SDN fabrics",
        "format": "pve-sdn-fabric-id",
        "maxLength": 8,
        "minLength": 2,
        "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
        "type": "string"
      },
      "ip6_prefix": {
        "description": "The IP prefix for Node IPs",
        "format": "CIDR",
        "optional": 1,
        "type": "string"
      },
      "ip_prefix": {
        "description": "The IP prefix for Node IPs",
        "format": "CIDR",
        "optional": 1,
        "type": "string"
      },
      "lock-token": {
        "description": "the token for unlocking the global SDN configuration",
        "optional": 1,
        "type": "string"
      },
      "persistent_keepalive": {
        "description": "A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from another node, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds. If unset or set to 0, it is turned off",
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
        "description": "Type of configuration entry in an SDN Fabric section config",
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
                  "description": "Route map to filter or transform redistributed routes from this source.",
                  "format": "pve-sdn-route-map-id",
                  "optional": 1,
                  "type": "string"
                },
                "source": {
                  "description": "The protocol from which to redistribute routes from.",
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
                  "description": "Route map to filter or transform redistributed routes from this source.",
                  "format": "pve-sdn-route-map-id",
                  "optional": 1,
                  "type": "string"
                },
                "source": {
                  "description": "The protocol from which to redistribute routes from.",
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
        "description": "A prefix list that should be used for filtering routes that are to be installed into the kernel routing table",
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

Add a fabric

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
| `area` | string | 否 | — | OSPF area. Either a IPv4 address or a 32-bit number. Gets validated in rust. |
| `csnp_interval` | number | 否 | — | The csnp_interval property for Openfabric |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `hello_interval` | number | 否 | — | The hello_interval property for Openfabric |
| `id` | string | 是 | — | Identifier for SDN fabrics |
| `ip6_prefix` | string | 否 | — | The IP prefix for Node IPs |
| `ip_prefix` | string | 否 | — | The IP prefix for Node IPs |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `persistent_keepalive` | number | 否 | — | A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from another node, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds. If unset or set to 0, it is turned off |
| `protocol` | string | 是 | — | Type of configuration entry in an SDN Fabric section config；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `redistribute` | array | 是 | — |  |
| `route_filter` | string | 否 | — | A prefix list that should be used for filtering routes that are to be installed into the kernel routing table |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "area": {
      "description": "OSPF area. Either a IPv4 address or a 32-bit number. Gets validated in rust.",
      "instance-types": [
        "ospf"
      ],
      "optional": 1,
      "type": "string",
      "type-property": "protocol",
      "typetext": "<string>"
    },
    "csnp_interval": {
      "description": "The csnp_interval property for Openfabric",
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
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "hello_interval": {
      "description": "The hello_interval property for Openfabric",
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
      "description": "Identifier for SDN fabrics",
      "format": "pve-sdn-fabric-id",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "ip6_prefix": {
      "description": "The IP prefix for Node IPs",
      "format": "CIDR",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ip_prefix": {
      "description": "The IP prefix for Node IPs",
      "format": "CIDR",
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
    "persistent_keepalive": {
      "description": "A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from another node, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds. If unset or set to 0, it is turned off",
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
      "description": "Type of configuration entry in an SDN Fabric section config",
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
                "description": "Route map to filter or transform redistributed routes from this source.",
                "format": "pve-sdn-route-map-id",
                "optional": 1,
                "type": "string"
              },
              "source": {
                "description": "The protocol from which to redistribute routes from.",
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
                "description": "Route map to filter or transform redistributed routes from this source.",
                "format": "pve-sdn-route-map-id",
                "optional": 1,
                "type": "string"
              },
              "source": {
                "description": "The protocol from which to redistribute routes from.",
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
      "description": "A prefix list that should be used for filtering routes that are to be installed into the kernel routing table",
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
