# `/nodes/{node}/network`

原始接口路径：`/nodes/{node}/network`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/network`

Revert network configuration changes.

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
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
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

List available networks

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
| `node` | string | 是 | — | The cluster node name. |
| `type` | string | 否 | — | Only list specific interface types.；可选值：`bridge`, `bond`, `eth`, `alias`, `vlan`, `fabric`, `OVSBridge`, `OVSBond`, `OVSPort`, `OVSIntPort`, `vnet`, `any_bridge`, `any_local_bridge`, `include_sdn` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "Only list specific interface types.",
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
        "description": "Set to true if the interface is active.",
        "optional": 1,
        "type": "boolean"
      },
      "address": {
        "description": "IP address.",
        "format": "ipv4",
        "optional": 1,
        "requires": "netmask",
        "type": "string"
      },
      "address6": {
        "description": "IP address.",
        "format": "ipv6",
        "optional": 1,
        "requires": "netmask6",
        "type": "string"
      },
      "autostart": {
        "description": "Automatically start interface on boot.",
        "optional": 1,
        "type": "boolean"
      },
      "bond-primary": {
        "description": "Specify the primary interface for active-backup bond.",
        "format": "pve-iface",
        "optional": 1,
        "type": "string"
      },
      "bond_mode": {
        "description": "Bonding mode.",
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
        "description": "Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes.",
        "enum": [
          "layer2",
          "layer2+3",
          "layer3+4"
        ],
        "optional": 1,
        "type": "string"
      },
      "bridge-access": {
        "description": "The bridge port access VLAN.",
        "optional": 1,
        "type": "integer"
      },
      "bridge-arp-nd-suppress": {
        "description": "Bridge port ARP/ND suppress flag.",
        "optional": 1,
        "type": "boolean"
      },
      "bridge-learning": {
        "description": "Bridge port learning flag.",
        "optional": 1,
        "type": "boolean"
      },
      "bridge-multicast-flood": {
        "description": "Bridge port multicast flood flag.",
        "optional": 1,
        "type": "boolean"
      },
      "bridge-unicast-flood": {
        "description": "Bridge port unicast flood flag.",
        "optional": 1,
        "type": "boolean"
      },
      "bridge_ports": {
        "description": "Specify the interfaces you want to add to your bridge.",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "bridge_vids": {
        "description": "Specify the allowed VLANs. For example: '2 4 100-200'. Only used if the bridge is VLAN aware.",
        "format": "pve-vlan-id-or-range-list",
        "optional": 1,
        "type": "string"
      },
      "bridge_vlan_aware": {
        "description": "Enable bridge vlan support.",
        "optional": 1,
        "type": "boolean"
      },
      "cidr": {
        "description": "IPv4 CIDR.",
        "format": "CIDRv4",
        "optional": 1,
        "type": "string"
      },
      "cidr6": {
        "description": "IPv6 CIDR.",
        "format": "CIDRv6",
        "optional": 1,
        "type": "string"
      },
      "comments": {
        "description": "Comments",
        "optional": 1,
        "type": "string"
      },
      "comments6": {
        "description": "Comments",
        "optional": 1,
        "type": "string"
      },
      "exists": {
        "description": "Set to true if the interface physically exists.",
        "optional": 1,
        "type": "boolean"
      },
      "families": {
        "description": "The network families.",
        "items": {
          "description": "A network family.",
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
        "description": "Default gateway address.",
        "format": "ipv4",
        "optional": 1,
        "type": "string"
      },
      "gateway6": {
        "description": "Default ipv6 gateway address.",
        "format": "ipv6",
        "optional": 1,
        "type": "string"
      },
      "iface": {
        "description": "Network interface name.",
        "format": "pve-iface",
        "maxLength": 20,
        "minLength": 2,
        "type": "string"
      },
      "link-type": {
        "description": "The link type.",
        "optional": 1,
        "type": "string"
      },
      "method": {
        "description": "The network configuration method for IPv4.",
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
        "description": "The network configuration method for IPv6.",
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
        "description": "MTU.",
        "maximum": 65520,
        "minimum": 1280,
        "optional": 1,
        "type": "integer"
      },
      "netmask": {
        "description": "Network mask.",
        "format": "ipv4mask",
        "optional": 1,
        "requires": "address",
        "type": "string"
      },
      "netmask6": {
        "description": "Network mask.",
        "maximum": 128,
        "minimum": 0,
        "optional": 1,
        "requires": "address6",
        "type": "integer"
      },
      "options": {
        "description": "A list of additional interface options for IPv4.",
        "items": {
          "description": "An interface property.",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "options6": {
        "description": "A list of additional interface options for IPv6.",
        "items": {
          "description": "An interface property.",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "ovs_bonds": {
        "description": "Specify the interfaces used by the bonding device.",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "ovs_bridge": {
        "description": "The OVS bridge associated with a OVS port. This is required when you create an OVS port.",
        "format": "pve-iface",
        "optional": 1,
        "type": "string"
      },
      "ovs_options": {
        "description": "OVS interface options.",
        "maxLength": 1024,
        "optional": 1,
        "type": "string"
      },
      "ovs_ports": {
        "description": "Specify the interfaces you want to add to your bridge.",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "ovs_tag": {
        "description": "Specify a VLan tag (used by OVSPort, OVSIntPort, OVSBond)",
        "maximum": 4094,
        "minimum": 1,
        "optional": 1,
        "type": "integer"
      },
      "priority": {
        "description": "The order of the interface.",
        "optional": 1,
        "type": "integer"
      },
      "slaves": {
        "description": "Specify the interfaces used by the bonding device.",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "type": {
        "description": "Network interface type",
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
        "description": "The uplink ID.",
        "optional": 1,
        "type": "string"
      },
      "vlan-id": {
        "description": "vlan-id for a custom named vlan interface (ifupdown2 only).",
        "maximum": 4094,
        "minimum": 1,
        "optional": 1,
        "type": "integer"
      },
      "vlan-protocol": {
        "description": "The VLAN protocol.",
        "enum": [
          "802.1ad",
          "802.1q"
        ],
        "optional": 1,
        "type": "string"
      },
      "vlan-raw-device": {
        "description": "Specify the raw interface for the vlan interface.",
        "format": "pve-iface",
        "optional": 1,
        "type": "string"
      },
      "vxlan-id": {
        "description": "The VXLAN ID.",
        "optional": 1,
        "type": "integer"
      },
      "vxlan-local-tunnelip": {
        "description": "The VXLAN local tunnel IP.",
        "optional": 1,
        "type": "string"
      },
      "vxlan-physdev": {
        "description": "The physical device for the VXLAN tunnel.",
        "optional": 1,
        "type": "string"
      },
      "vxlan-svcnodeip": {
        "description": "The VXLAN SVC node IP.",
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

Create network device configuration

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
| `address` | string | 否 | — | IP address. |
| `address6` | string | 否 | — | IP address. |
| `autostart` | boolean | 否 | — | Automatically start interface on boot. |
| `bond-primary` | string | 否 | — | Specify the primary interface for active-backup bond. |
| `bond_mode` | string | 否 | — | Bonding mode.；可选值：`balance-rr`, `active-backup`, `balance-xor`, `broadcast`, `802.3ad`, `balance-tlb`, `balance-alb`, `balance-slb`, `lacp-balance-slb`, `lacp-balance-tcp` |
| `bond_xmit_hash_policy` | string | 否 | — | Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes.；可选值：`layer2`, `layer2+3`, `layer3+4` |
| `bridge_ports` | string | 否 | — | Specify the interfaces you want to add to your bridge. |
| `bridge_vids` | string | 否 | — | Specify the allowed VLANs. For example: '2 4 100-200'. Only used if the bridge is VLAN aware. |
| `bridge_vlan_aware` | boolean | 否 | — | Enable bridge vlan support. |
| `cidr` | string | 否 | — | IPv4 CIDR. |
| `cidr6` | string | 否 | — | IPv6 CIDR. |
| `comments` | string | 否 | — | Comments |
| `comments6` | string | 否 | — | Comments |
| `gateway` | string | 否 | — | Default gateway address. |
| `gateway6` | string | 否 | — | Default ipv6 gateway address. |
| `iface` | string | 是 | — | Network interface name. |
| `mtu` | integer | 否 | — | MTU. |
| `netmask` | string | 否 | — | Network mask. |
| `netmask6` | integer | 否 | — | Network mask. |
| `node` | string | 是 | — | The cluster node name. |
| `ovs_bonds` | string | 否 | — | Specify the interfaces used by the bonding device. |
| `ovs_bridge` | string | 否 | — | The OVS bridge associated with a OVS port. This is required when you create an OVS port. |
| `ovs_options` | string | 否 | — | OVS interface options. |
| `ovs_ports` | string | 否 | — | Specify the interfaces you want to add to your bridge. |
| `ovs_tag` | integer | 否 | — | Specify a VLan tag (used by OVSPort, OVSIntPort, OVSBond) |
| `slaves` | string | 否 | — | Specify the interfaces used by the bonding device. |
| `type` | string | 是 | — | Network interface type；可选值：`bridge`, `bond`, `eth`, `alias`, `vlan`, `fabric`, `OVSBridge`, `OVSBond`, `OVSPort`, `OVSIntPort`, `vnet`, `unknown` |
| `vlan-id` | integer | 否 | — | vlan-id for a custom named vlan interface (ifupdown2 only). |
| `vlan-raw-device` | string | 否 | — | Specify the raw interface for the vlan interface. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "address": {
      "description": "IP address.",
      "format": "ipv4",
      "optional": 1,
      "requires": "netmask",
      "type": "string",
      "typetext": "<string>"
    },
    "address6": {
      "description": "IP address.",
      "format": "ipv6",
      "optional": 1,
      "requires": "netmask6",
      "type": "string",
      "typetext": "<string>"
    },
    "autostart": {
      "description": "Automatically start interface on boot.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bond-primary": {
      "description": "Specify the primary interface for active-backup bond.",
      "format": "pve-iface",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bond_mode": {
      "description": "Bonding mode.",
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
      "description": "Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes.",
      "enum": [
        "layer2",
        "layer2+3",
        "layer3+4"
      ],
      "optional": 1,
      "type": "string"
    },
    "bridge_ports": {
      "description": "Specify the interfaces you want to add to your bridge.",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge_vids": {
      "description": "Specify the allowed VLANs. For example: '2 4 100-200'. Only used if the bridge is VLAN aware.",
      "format": "pve-vlan-id-or-range-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge_vlan_aware": {
      "description": "Enable bridge vlan support.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cidr": {
      "description": "IPv4 CIDR.",
      "format": "CIDRv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "cidr6": {
      "description": "IPv6 CIDR.",
      "format": "CIDRv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comments": {
      "description": "Comments",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comments6": {
      "description": "Comments",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway": {
      "description": "Default gateway address.",
      "format": "ipv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway6": {
      "description": "Default ipv6 gateway address.",
      "format": "ipv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "iface": {
      "description": "Network interface name.",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "type": "string",
      "typetext": "<string>"
    },
    "mtu": {
      "description": "MTU.",
      "maximum": 65520,
      "minimum": 1280,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1280 - 65520)"
    },
    "netmask": {
      "description": "Network mask.",
      "format": "ipv4mask",
      "optional": 1,
      "requires": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "netmask6": {
      "description": "Network mask.",
      "maximum": 128,
      "minimum": 0,
      "optional": 1,
      "requires": "address6",
      "type": "integer",
      "typetext": "<integer> (0 - 128)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_bonds": {
      "description": "Specify the interfaces used by the bonding device.",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_bridge": {
      "description": "The OVS bridge associated with a OVS port. This is required when you create an OVS port.",
      "format": "pve-iface",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_options": {
      "description": "OVS interface options.",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_ports": {
      "description": "Specify the interfaces you want to add to your bridge.",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_tag": {
      "description": "Specify a VLan tag (used by OVSPort, OVSIntPort, OVSBond)",
      "maximum": 4094,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 4094)"
    },
    "slaves": {
      "description": "Specify the interfaces used by the bonding device.",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "Network interface type",
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
      "description": "vlan-id for a custom named vlan interface (ifupdown2 only).",
      "maximum": 4094,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 4094)"
    },
    "vlan-raw-device": {
      "description": "Specify the raw interface for the vlan interface.",
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

Reload network configuration

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
| `node` | string | 是 | — | The cluster node name. |
| `regenerate-frr` | boolean | 否 | 0 | Whether FRR config generation should get skipped or not. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "regenerate-frr": {
      "default": 0,
      "description": "Whether FRR config generation should get skipped or not.",
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
