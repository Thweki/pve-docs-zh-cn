# `/nodes/{node}/network`

原始接口路径：`/nodes/{node}/network`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/network`

撤销网络配置更改。

**方法标识：** `revert_network_changes`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Modify"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
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

## GET `/nodes/{node}/network`

列出可用网络

**方法标识：** `index`

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |
| `type` | string | 否 | — | 仅列出指定接口类型。；可选值：`bridge`, `bond`, `eth`, `alias`, `vlan`, `fabric`, `OVSBridge`, `OVSBond`, `OVSPort`, `OVSIntPort`, `vnet`, `any_bridge`, `any_local_bridge`, `include_sdn` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "仅列出指定接口类型。",
      "enum": [
        "bridge",
        "bond",
        "eth",
        "alias",
        "vlan",
        "fabric",
        "OVSBridge",
        "OVSBond",
        "OVSPort",
        "OVSIntPort",
        "vnet",
        "any_bridge",
        "any_local_bridge",
        "include_sdn"
      ],
      "optional": 1,
      "type": "string"
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
      "active": {
        "description": "如果接口处于活动状态，则设为 true。",
        "optional": 1,
        "type": "boolean"
      },
      "address": {
        "description": "IP 地址。",
        "format": "ipv4",
        "optional": 1,
        "requires": "netmask",
        "type": "string"
      },
      "address6": {
        "description": "IP 地址。",
        "format": "ipv6",
        "optional": 1,
        "requires": "netmask6",
        "type": "string"
      },
      "autostart": {
        "description": "启动时自动启用接口。",
        "optional": 1,
        "type": "boolean"
      },
      "bond-primary": {
        "description": "为 active-backup 绑定指定主接口。",
        "format": "pve-iface",
        "optional": 1,
        "type": "string"
      },
      "bond_mode": {
        "description": "绑定模式。",
        "enum": [
          "balance-rr",
          "active-backup",
          "balance-xor",
          "broadcast",
          "802.3ad",
          "balance-tlb",
          "balance-alb",
          "balance-slb",
          "lacp-balance-slb",
          "lacp-balance-tcp"
        ],
        "optional": 1,
        "type": "string"
      },
      "bond_xmit_hash_policy": {
        "description": "选择 balance-xor 和 802.3ad 模式中用于选择从接口的发送哈希策略。",
        "enum": [
          "layer2",
          "layer2+3",
          "layer3+4"
        ],
        "optional": 1,
        "type": "string"
      },
      "bridge-access": {
        "description": "网桥端口的接入 VLAN。",
        "optional": 1,
        "type": "integer"
      },
      "bridge-arp-nd-suppress": {
        "description": "网桥端口 ARP/ND 抑制标志。",
        "optional": 1,
        "type": "boolean"
      },
      "bridge-learning": {
        "description": "网桥端口学习标志。",
        "optional": 1,
        "type": "boolean"
      },
      "bridge-multicast-flood": {
        "description": "网桥端口组播泛洪标志。",
        "optional": 1,
        "type": "boolean"
      },
      "bridge-unicast-flood": {
        "description": "网桥端口单播泛洪标志。",
        "optional": 1,
        "type": "boolean"
      },
      "bridge_ports": {
        "description": "指定要加入网桥的接口。",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "bridge_vids": {
        "description": "指定允许的 VLAN。例如：'2 4 100-200'。仅在网桥支持 VLAN 感知时使用。",
        "format": "pve-vlan-id-or-range-list",
        "optional": 1,
        "type": "string"
      },
      "bridge_vlan_aware": {
        "description": "启用网桥 VLAN 支持。",
        "optional": 1,
        "type": "boolean"
      },
      "cidr": {
        "description": "IPv4 CIDR。",
        "format": "CIDRv4",
        "optional": 1,
        "type": "string"
      },
      "cidr6": {
        "description": "IPv6 CIDR。",
        "format": "CIDRv6",
        "optional": 1,
        "type": "string"
      },
      "comments": {
        "description": "注释",
        "optional": 1,
        "type": "string"
      },
      "comments6": {
        "description": "注释",
        "optional": 1,
        "type": "string"
      },
      "exists": {
        "description": "如果接口物理存在，则设为 true。",
        "optional": 1,
        "type": "boolean"
      },
      "families": {
        "description": "网络地址族。",
        "items": {
          "description": "网络地址族。",
          "enum": [
            "inet",
            "inet6"
          ],
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "gateway": {
        "description": "默认网关地址。",
        "format": "ipv4",
        "optional": 1,
        "type": "string"
      },
      "gateway6": {
        "description": "默认 IPv6 网关地址。",
        "format": "ipv6",
        "optional": 1,
        "type": "string"
      },
      "iface": {
        "description": "网络接口名称。",
        "format": "pve-iface",
        "maxLength": 20,
        "minLength": 2,
        "type": "string"
      },
      "link-type": {
        "description": "链路类型。",
        "optional": 1,
        "type": "string"
      },
      "method": {
        "description": "IPv4 网络配置方法。",
        "enum": [
          "loopback",
          "dhcp",
          "manual",
          "static",
          "auto"
        ],
        "optional": 1,
        "type": "string"
      },
      "method6": {
        "description": "IPv6 网络配置方法。",
        "enum": [
          "loopback",
          "dhcp",
          "manual",
          "static",
          "auto"
        ],
        "optional": 1,
        "type": "string"
      },
      "mtu": {
        "description": "MTU。",
        "maximum": 65520,
        "minimum": 1280,
        "optional": 1,
        "type": "integer"
      },
      "netmask": {
        "description": "网络掩码。",
        "format": "ipv4mask",
        "optional": 1,
        "requires": "address",
        "type": "string"
      },
      "netmask6": {
        "description": "网络掩码。",
        "maximum": 128,
        "minimum": 0,
        "optional": 1,
        "requires": "address6",
        "type": "integer"
      },
      "options": {
        "description": "IPv4 附加接口选项列表。",
        "items": {
          "description": "接口属性。",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "options6": {
        "description": "IPv6 附加接口选项列表。",
        "items": {
          "description": "接口属性。",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "ovs_bonds": {
        "description": "指定绑定设备使用的接口。",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "ovs_bridge": {
        "description": "与 OVS 端口关联的 OVS 网桥。创建 OVS 端口时需要此项。",
        "format": "pve-iface",
        "optional": 1,
        "type": "string"
      },
      "ovs_options": {
        "description": "OVS 接口选项。",
        "maxLength": 1024,
        "optional": 1,
        "type": "string"
      },
      "ovs_ports": {
        "description": "指定要加入网桥的接口。",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "ovs_tag": {
        "description": "指定 VLAN 标签（用于 OVSPort、OVSIntPort、OVSBond）",
        "maximum": 4094,
        "minimum": 1,
        "optional": 1,
        "type": "integer"
      },
      "priority": {
        "description": "接口顺序。",
        "optional": 1,
        "type": "integer"
      },
      "slaves": {
        "description": "指定绑定设备使用的接口。",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "type": {
        "description": "网络接口类型",
        "enum": [
          "bridge",
          "bond",
          "eth",
          "alias",
          "vlan",
          "fabric",
          "OVSBridge",
          "OVSBond",
          "OVSPort",
          "OVSIntPort",
          "vnet",
          "unknown"
        ],
        "type": "string"
      },
      "uplink-id": {
        "description": "上行链路 ID。",
        "optional": 1,
        "type": "string"
      },
      "vlan-id": {
        "description": "自定义名称的 VLAN 接口的 vlan-id（仅限 ifupdown2）。",
        "maximum": 4094,
        "minimum": 1,
        "optional": 1,
        "type": "integer"
      },
      "vlan-protocol": {
        "description": "VLAN 协议。",
        "enum": [
          "802.1ad",
          "802.1q"
        ],
        "optional": 1,
        "type": "string"
      },
      "vlan-raw-device": {
        "description": "指定 VLAN 接口的原始接口。",
        "format": "pve-iface",
        "optional": 1,
        "type": "string"
      },
      "vxlan-id": {
        "description": "VXLAN ID。",
        "optional": 1,
        "type": "integer"
      },
      "vxlan-local-tunnelip": {
        "description": "VXLAN 本地隧道 IP。",
        "optional": 1,
        "type": "string"
      },
      "vxlan-physdev": {
        "description": "VXLAN 隧道的物理设备。",
        "optional": 1,
        "type": "string"
      },
      "vxlan-svcnodeip": {
        "description": "VXLAN SVC 节点 IP。",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{iface}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/nodes/{node}/network`

创建网络设备配置

**方法标识：** `create_network`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Modify"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `address` | string | 否 | — | IP 地址。 |
| `address6` | string | 否 | — | IP 地址。 |
| `autostart` | boolean | 否 | — | 启动时自动启用接口。 |
| `bond-primary` | string | 否 | — | 为 active-backup 绑定指定主接口。 |
| `bond_mode` | string | 否 | — | 绑定模式。；可选值：`balance-rr`, `active-backup`, `balance-xor`, `broadcast`, `802.3ad`, `balance-tlb`, `balance-alb`, `balance-slb`, `lacp-balance-slb`, `lacp-balance-tcp` |
| `bond_xmit_hash_policy` | string | 否 | — | 选择 balance-xor 和 802.3ad 模式中用于选择从接口的发送哈希策略。；可选值：`layer2`, `layer2+3`, `layer3+4` |
| `bridge_ports` | string | 否 | — | 指定要加入网桥的接口。 |
| `bridge_vids` | string | 否 | — | 指定允许的 VLAN。例如：'2 4 100-200'。仅在网桥支持 VLAN 感知时使用。 |
| `bridge_vlan_aware` | boolean | 否 | — | 启用网桥 VLAN 支持。 |
| `cidr` | string | 否 | — | IPv4 CIDR。 |
| `cidr6` | string | 否 | — | IPv6 CIDR。 |
| `comments` | string | 否 | — | 注释 |
| `comments6` | string | 否 | — | 注释 |
| `gateway` | string | 否 | — | 默认网关地址。 |
| `gateway6` | string | 否 | — | 默认 IPv6 网关地址。 |
| `iface` | string | 是 | — | 网络接口名称。 |
| `mtu` | integer | 否 | — | MTU。 |
| `netmask` | string | 否 | — | 网络掩码。 |
| `netmask6` | integer | 否 | — | 网络掩码。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `ovs_bonds` | string | 否 | — | 指定绑定设备使用的接口。 |
| `ovs_bridge` | string | 否 | — | 与 OVS 端口关联的 OVS 网桥。创建 OVS 端口时需要此项。 |
| `ovs_options` | string | 否 | — | OVS 接口选项。 |
| `ovs_ports` | string | 否 | — | 指定要加入网桥的接口。 |
| `ovs_tag` | integer | 否 | — | 指定 VLAN 标签（用于 OVSPort、OVSIntPort、OVSBond） |
| `slaves` | string | 否 | — | 指定绑定设备使用的接口。 |
| `type` | string | 是 | — | 网络接口类型；可选值：`bridge`, `bond`, `eth`, `alias`, `vlan`, `fabric`, `OVSBridge`, `OVSBond`, `OVSPort`, `OVSIntPort`, `vnet`, `unknown` |
| `vlan-id` | integer | 否 | — | 自定义名称的 VLAN 接口的 vlan-id（仅限 ifupdown2）。 |
| `vlan-raw-device` | string | 否 | — | 指定 VLAN 接口的原始接口。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "address": {
      "description": "IP 地址。",
      "format": "ipv4",
      "optional": 1,
      "requires": "netmask",
      "type": "string",
      "typetext": "<string>"
    },
    "address6": {
      "description": "IP 地址。",
      "format": "ipv6",
      "optional": 1,
      "requires": "netmask6",
      "type": "string",
      "typetext": "<string>"
    },
    "autostart": {
      "description": "启动时自动启用接口。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bond-primary": {
      "description": "为 active-backup 绑定指定主接口。",
      "format": "pve-iface",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bond_mode": {
      "description": "绑定模式。",
      "enum": [
        "balance-rr",
        "active-backup",
        "balance-xor",
        "broadcast",
        "802.3ad",
        "balance-tlb",
        "balance-alb",
        "balance-slb",
        "lacp-balance-slb",
        "lacp-balance-tcp"
      ],
      "optional": 1,
      "type": "string"
    },
    "bond_xmit_hash_policy": {
      "description": "选择 balance-xor 和 802.3ad 模式中用于选择从接口的发送哈希策略。",
      "enum": [
        "layer2",
        "layer2+3",
        "layer3+4"
      ],
      "optional": 1,
      "type": "string"
    },
    "bridge_ports": {
      "description": "指定要加入网桥的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge_vids": {
      "description": "指定允许的 VLAN。例如：'2 4 100-200'。仅在网桥支持 VLAN 感知时使用。",
      "format": "pve-vlan-id-or-range-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge_vlan_aware": {
      "description": "启用网桥 VLAN 支持。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cidr": {
      "description": "IPv4 CIDR。",
      "format": "CIDRv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "cidr6": {
      "description": "IPv6 CIDR。",
      "format": "CIDRv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comments": {
      "description": "注释",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comments6": {
      "description": "注释",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway": {
      "description": "默认网关地址。",
      "format": "ipv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway6": {
      "description": "默认 IPv6 网关地址。",
      "format": "ipv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "type": "string",
      "typetext": "<string>"
    },
    "mtu": {
      "description": "MTU。",
      "maximum": 65520,
      "minimum": 1280,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1280 - 65520)"
    },
    "netmask": {
      "description": "网络掩码。",
      "format": "ipv4mask",
      "optional": 1,
      "requires": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "netmask6": {
      "description": "网络掩码。",
      "maximum": 128,
      "minimum": 0,
      "optional": 1,
      "requires": "address6",
      "type": "integer",
      "typetext": "<integer> (0 - 128)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_bonds": {
      "description": "指定绑定设备使用的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_bridge": {
      "description": "与 OVS 端口关联的 OVS 网桥。创建 OVS 端口时需要此项。",
      "format": "pve-iface",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_options": {
      "description": "OVS 接口选项。",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_ports": {
      "description": "指定要加入网桥的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_tag": {
      "description": "指定 VLAN 标签（用于 OVSPort、OVSIntPort、OVSBond）",
      "maximum": 4094,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 4094)"
    },
    "slaves": {
      "description": "指定绑定设备使用的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "网络接口类型",
      "enum": [
        "bridge",
        "bond",
        "eth",
        "alias",
        "vlan",
        "fabric",
        "OVSBridge",
        "OVSBond",
        "OVSPort",
        "OVSIntPort",
        "vnet",
        "unknown"
      ],
      "type": "string"
    },
    "vlan-id": {
      "description": "自定义名称的 VLAN 接口的 vlan-id（仅限 ifupdown2）。",
      "maximum": 4094,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 4094)"
    },
    "vlan-raw-device": {
      "description": "指定 VLAN 接口的原始接口。",
      "format": "pve-iface",
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

## PUT `/nodes/{node}/network`

重新加载网络配置

**方法标识：** `reload_network_config`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Modify"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |
| `regenerate-frr` | boolean | 否 | 0 | 是否应跳过 FRR 配置生成。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "regenerate-frr": {
      "default": 0,
      "description": "是否应跳过 FRR 配置生成。",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/network)。
