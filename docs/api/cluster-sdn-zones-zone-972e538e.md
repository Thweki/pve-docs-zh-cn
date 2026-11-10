# `/cluster/sdn/zones/{zone}`

原始接口路径：`/cluster/sdn/zones/{zone}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/zones/{zone}`

删除 SDN 区域对象配置。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}",
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
| `zone` | string | 是 | — | SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "zone": {
      "description": "SDN 区域对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
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

## GET `/cluster/sdn/zones/{zone}`

读取 SDN 区域配置。

**方法标识：** `read`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}",
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `pending` | boolean | 否 | — | 显示待应用的配置。 |
| `running` | boolean | 否 | — | 显示运行中的配置。 |
| `zone` | string | 是 | — | SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
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
    "zone": {
      "description": "SDN 区域对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "advertise-subnets": {
      "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。仅适用于 EVPN 区域。",
      "optional": 1,
      "type": "boolean"
    },
    "bridge": {
      "description": "要管理其 VLAN 的网桥。仅适用于 VLAN 和 QinQ 区域。",
      "optional": 1,
      "type": "string"
    },
    "bridge-disable-mac-learning": {
      "description": "禁用自动 MAC 学习。仅适用于 VLAN 区域。",
      "optional": 1,
      "type": "boolean"
    },
    "controller": {
      "description": "此区域的控制器 ID。仅适用于 EVPN 区域。",
      "optional": 1,
      "type": "string"
    },
    "dhcp": {
      "description": "此区域的 DHCP 服务器后端名称。",
      "enum": [
        "dnsmasq"
      ],
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "控制器配置节的摘要。",
      "optional": 1,
      "type": "string"
    },
    "disable-arp-nd-suppression": {
      "description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。仅适用于 EVPN 区域。",
      "optional": 1,
      "type": "boolean"
    },
    "dns": {
      "description": "此区域的 DNS 服务器 ID。",
      "optional": 1,
      "type": "string"
    },
    "dnszone": {
      "description": "此区域的域名。",
      "optional": 1,
      "type": "string"
    },
    "exitnodes": {
      "description": "应充当此区域出口节点的 PVE 节点列表。仅适用于 EVPN 区域。",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string"
    },
    "exitnodes-local-routing": {
      "description": "在出口节点上创建路由，使其能够连接 EVPN 客户机。仅适用于 EVPN 区域。",
      "optional": 1,
      "type": "boolean"
    },
    "exitnodes-primary": {
      "description": "强制流量首先经过此出口节点。仅适用于 EVPN 区域。",
      "format": "pve-node",
      "optional": 1,
      "type": "string"
    },
    "ipam": {
      "description": "此区域的 IPAM ID。",
      "optional": 1,
      "type": "string"
    },
    "mac": {
      "description": "此区域任播路由器的 MAC 地址。",
      "optional": 1,
      "type": "string"
    },
    "mtu": {
      "description": "区域的 MTU，将用于创建的 VNet 网桥。",
      "optional": 1,
      "type": "integer"
    },
    "nodes": {
      "description": "应创建此区域的节点。",
      "optional": 1,
      "type": "string"
    },
    "peers": {
      "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。仅适用于 VXLAN 区域。",
      "format": "ip-list",
      "optional": 1,
      "type": "string"
    },
    "pending": {
      "description": "尚未应用到运行配置的更改。",
      "optional": 1,
      "properties": {
        "advertise-subnets": {
          "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。仅适用于 EVPN 区域。",
          "optional": 1,
          "type": "boolean"
        },
        "bridge": {
          "description": "要管理其 VLAN 的网桥。仅适用于 VLAN 和 QinQ 区域。",
          "optional": 1,
          "type": "string"
        },
        "bridge-disable-mac-learning": {
          "description": "禁用自动 MAC 学习。仅适用于 VLAN 区域。",
          "optional": 1,
          "type": "boolean"
        },
        "controller": {
          "description": "此区域的控制器 ID。仅适用于 EVPN 区域。",
          "optional": 1,
          "type": "string"
        },
        "dhcp": {
          "description": "此区域的 DHCP 服务器后端名称。",
          "enum": [
            "dnsmasq"
          ],
          "optional": 1,
          "type": "string"
        },
        "disable-arp-nd-suppression": {
          "description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。仅适用于 EVPN 区域。",
          "optional": 1,
          "type": "boolean"
        },
        "dns": {
          "description": "此区域的 DNS 服务器 ID。",
          "optional": 1,
          "type": "string"
        },
        "dnszone": {
          "description": "此区域的域名。",
          "optional": 1,
          "type": "string"
        },
        "exitnodes": {
          "description": "应充当此区域出口节点的 PVE 节点列表。仅适用于 EVPN 区域。",
          "format": "pve-node-list",
          "optional": 1,
          "type": "string"
        },
        "exitnodes-local-routing": {
          "description": "在出口节点上创建路由，使其能够连接 EVPN 客户机。仅适用于 EVPN 区域。",
          "optional": 1,
          "type": "boolean"
        },
        "exitnodes-primary": {
          "description": "强制流量首先经过此出口节点。仅适用于 EVPN 区域。",
          "format": "pve-node",
          "optional": 1,
          "type": "string"
        },
        "ipam": {
          "description": "此区域的 IPAM ID。",
          "optional": 1,
          "type": "string"
        },
        "mac": {
          "description": "此区域任播路由器的 MAC 地址。",
          "optional": 1,
          "type": "string"
        },
        "mtu": {
          "description": "区域的 MTU，将用于创建的 VNet 网桥。",
          "optional": 1,
          "type": "integer"
        },
        "nodes": {
          "description": "应创建此区域的节点。",
          "optional": 1,
          "type": "string"
        },
        "peers": {
          "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。仅适用于 VXLAN 区域。",
          "format": "ip-list",
          "optional": 1,
          "type": "string"
        },
        "reversedns": {
          "description": "此区域的反向 DNS 服务器 ID。",
          "optional": 1,
          "type": "string"
        },
        "rt-import": {
          "description": "应通过 BGP 导入此区域 VRF 的 Route-Target。仅适用于 EVPN 区域。",
          "format": "pve-sdn-bgp-rt-list",
          "optional": 1,
          "type": "string"
        },
        "secondary-controllers": {
          "description": "附加控制器。",
          "items": {
            "description": "控制器 ID。",
            "maxLength": 64,
            "minLength": 2,
            "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        "tag": {
          "description": "Service-VLAN 标签（外层 VLAN）。仅适用于 QinQ 区域",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "vlan-protocol": {
          "default": "802.1q",
          "description": "创建 QinQ 区域所用的 VLAN 协议。仅适用于 QinQ 区域。",
          "enum": [
            "802.1q",
            "802.1ad"
          ],
          "optional": 1,
          "type": "string"
        },
        "vrf-vxlan": {
          "description": "区域 VRF 的 VNI。仅适用于 EVPN 区域。",
          "maximum": 16777215,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "vxlan-port": {
          "default": 4789,
          "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。仅适用于 VXLAN 区域。",
          "maximum": 65536,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "reversedns": {
      "description": "此区域的反向 DNS 服务器 ID。",
      "optional": 1,
      "type": "string"
    },
    "rt-import": {
      "description": "应通过 BGP 导入此区域 VRF 的 Route-Target。仅适用于 EVPN 区域。",
      "format": "pve-sdn-bgp-rt-list",
      "optional": 1,
      "type": "string"
    },
    "secondary-controllers": {
      "description": "附加控制器。",
      "items": {
        "description": "控制器 ID。",
        "maxLength": 64,
        "minLength": 2,
        "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "state": {
      "description": "SDN 配置对象的状态。",
      "enum": [
        "new",
        "changed",
        "deleted"
      ],
      "optional": 1,
      "type": "string"
    },
    "tag": {
      "description": "Service-VLAN 标签（外层 VLAN）。仅适用于 QinQ 区域",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "type": {
      "description": "区域类型。",
      "enum": [
        "evpn",
        "faucet",
        "qinq",
        "simple",
        "vlan",
        "vxlan"
      ],
      "type": "string"
    },
    "vlan-protocol": {
      "default": "802.1q",
      "description": "创建 QinQ 区域所用的 VLAN 协议。仅适用于 QinQ 区域。",
      "enum": [
        "802.1q",
        "802.1ad"
      ],
      "optional": 1,
      "type": "string"
    },
    "vrf-vxlan": {
      "description": "区域 VRF 的 VNI。仅适用于 EVPN 区域。",
      "maximum": 16777215,
      "minimum": 1,
      "optional": 1,
      "type": "integer"
    },
    "vxlan-port": {
      "default": 4789,
      "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。仅适用于 VXLAN 区域。",
      "maximum": 65536,
      "minimum": 1,
      "optional": 1,
      "type": "integer"
    },
    "zone": {
      "description": "区域名称。",
      "type": "string"
    }
  }
}
```

## PUT `/cluster/sdn/zones/{zone}`

更新 SDN 区域对象配置。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}",
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
| `advertise-subnets` | boolean | 否 | — | 通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。 |
| `bridge` | string | 否 | — | 要管理其 VLAN 的网桥。 |
| `bridge-disable-mac-learning` | boolean | 否 | — | 禁用自动 MAC 学习。 |
| `controller` | string | 否 | — | 此区域的控制器。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `dhcp` | string | 否 | — | 此区域的 DHCP 后端类型；可选值：`dnsmasq` |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable-arp-nd-suppression` | boolean | 否 | — | 抑制 IPv4 ARP 和 IPv6 邻居发现消息。 |
| `dns` | string | 否 | — | DNS API 服务器 |
| `dnszone` | string | 否 | — | DNS 域区域  例如：mydomain.com |
| `dp-id` | integer | 否 | — | Faucet 数据平面 ID |
| `exitnodes` | string | 否 | — | 集群节点名称列表。 |
| `exitnodes-local-routing` | boolean | 否 | — | 允许出口节点连接 EVPN 客户机。 |
| `exitnodes-primary` | string | 否 | — | 强制流量首先经过此出口节点。 |
| `fabric` | string | 否 | — | 此 VXLAN 区域用作底层网络的 SDN fabric。 |
| `ipam` | string | 否 | — | 使用指定的 ipam |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `mac` | string | 否 | — | 任播逻辑路由器 MAC 地址。 |
| `mtu` | integer | 否 | — | 区域的 MTU，将用于创建的 VNet 网桥。 |
| `nodes` | string | 否 | — | 集群节点名称列表。 |
| `peers` | string | 否 | — | 属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。 |
| `reversedns` | string | 否 | — | 反向 DNS API 服务器 |
| `rt-import` | string | 否 | — | 应导入此区域 VRF 的 Route Target 列表。 |
| `secondary-controllers` | array | 否 | — | 附加控制器。 |
| `tag` | integer | 否 | — | Service-VLAN 标签（外层 VLAN） |
| `vlan-protocol` | string | 否 | "802.1q" | 创建 QinQ 区域应使用的 VLAN 协议。；可选值：`802.1q`, `802.1ad` |
| `vrf-vxlan` | integer | 否 | — | 区域 VRF 的 VNI。 |
| `vxlan-port` | integer | 否 | 4789 | VXLAN 隧道应使用的 UDP 端口（默认 4789）。 |
| `zone` | string | 是 | — | SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "advertise-subnets": {
      "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bridge": {
      "description": "要管理其 VLAN 的网桥。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge-disable-mac-learning": {
      "description": "禁用自动 MAC 学习。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "controller": {
      "description": "此区域的控制器。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dhcp": {
      "description": "此区域的 DHCP 后端类型",
      "enum": [
        "dnsmasq"
      ],
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable-arp-nd-suppression": {
      "description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "dns": {
      "description": "DNS API 服务器",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dnszone": {
      "description": "DNS 域区域  例如：mydomain.com",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dp-id": {
      "description": "Faucet 数据平面 ID",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "exitnodes": {
      "description": "集群节点名称列表。",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "exitnodes-local-routing": {
      "description": "允许出口节点连接 EVPN 客户机。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "exitnodes-primary": {
      "description": "强制流量首先经过此出口节点。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fabric": {
      "description": "此 VXLAN 区域用作底层网络的 SDN fabric。",
      "format": "pve-sdn-fabric-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ipam": {
      "description": "使用指定的 ipam",
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
    "mac": {
      "description": "任播逻辑路由器 MAC 地址。",
      "format": "mac-addr",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mtu": {
      "description": "区域的 MTU，将用于创建的 VNet 网桥。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "nodes": {
      "description": "集群节点名称列表。",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "peers": {
      "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。",
      "format": "ip-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "reversedns": {
      "description": "反向 DNS API 服务器",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "rt-import": {
      "description": "应导入此区域 VRF 的 Route Target 列表。",
      "format": "pve-sdn-bgp-rt-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "secondary-controllers": {
      "description": "附加控制器。",
      "items": {
        "description": "控制器 ID。",
        "maxLength": 64,
        "minLength": 2,
        "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "tag": {
      "description": "Service-VLAN 标签（外层 VLAN）",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vlan-protocol": {
      "default": "802.1q",
      "description": "创建 QinQ 区域应使用的 VLAN 协议。",
      "enum": [
        "802.1q",
        "802.1ad"
      ],
      "optional": 1,
      "type": "string"
    },
    "vrf-vxlan": {
      "description": "区域 VRF 的 VNI。",
      "maximum": 16777215,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 16777215)"
    },
    "vxlan-port": {
      "default": 4789,
      "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。",
      "maximum": 65536,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "zone": {
      "description": "SDN 区域对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/zones/{zone})。
