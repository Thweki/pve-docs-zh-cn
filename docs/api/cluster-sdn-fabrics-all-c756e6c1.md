# `/cluster/sdn/fabrics/all`

原始接口路径：`/cluster/sdn/fabrics/all`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/fabrics/all`

SDN Fabric 索引

**方法标识：** `list_all`

**权限**

```json
{
  "description": "仅列出您具有以下权限的 fabric：对\n'/sdn/fabrics/<fabric>' 的 'SDN.Audit' 或 'SDN.Allocate' 权限；仅列出您对 /nodes/<node_id> 具有 'Sys.Audit' 或 'Sys.Modify' 权限的节点",
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
  "properties": {
    "fabrics": {
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
      "type": "array"
    },
    "nodes": {
      "items": {
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
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/all)。
