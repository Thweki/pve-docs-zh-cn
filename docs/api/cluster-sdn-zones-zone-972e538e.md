# `/cluster/sdn/zones/{zone}`

原始接口路径：`/cluster/sdn/zones/{zone}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/zones/{zone}`

Delete sdn zone object configuration.

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
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `zone` | string | 是 | — | The SDN zone object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "zone": {
      "description": "The SDN zone object identifier.",
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

Read sdn zone configuration.

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
| `pending` | boolean | 否 | — | Display pending config. |
| `running` | boolean | 否 | — | Display running config. |
| `zone` | string | 是 | — | The SDN zone object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
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
    },
    "zone": {
      "description": "The SDN zone object identifier.",
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
      "description": "Advertise IP prefixes (Type-5 routes) instead of MAC/IP pairs (Type-2 routes). EVPN zone only.",
      "optional": 1,
      "type": "boolean"
    },
    "bridge": {
      "description": "the bridge for which VLANs should be managed. VLAN & QinQ zone only.",
      "optional": 1,
      "type": "string"
    },
    "bridge-disable-mac-learning": {
      "description": "Disable auto mac learning. VLAN zone only.",
      "optional": 1,
      "type": "boolean"
    },
    "controller": {
      "description": "ID of the controller for this zone. EVPN zone only.",
      "optional": 1,
      "type": "string"
    },
    "dhcp": {
      "description": "Name of DHCP server backend for this zone.",
      "enum": [
        "dnsmasq"
      ],
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Digest of the controller section.",
      "optional": 1,
      "type": "string"
    },
    "disable-arp-nd-suppression": {
      "description": "Suppress IPv4 ARP && IPv6 Neighbour Discovery messages. EVPN zone only.",
      "optional": 1,
      "type": "boolean"
    },
    "dns": {
      "description": "ID of the DNS server for this zone.",
      "optional": 1,
      "type": "string"
    },
    "dnszone": {
      "description": "Domain name for this zone.",
      "optional": 1,
      "type": "string"
    },
    "exitnodes": {
      "description": "List of PVE Nodes that should act as exit node for this zone. EVPN zone only.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string"
    },
    "exitnodes-local-routing": {
      "description": "Create routes on the exit nodes, so they can connect to EVPN guests. EVPN zone only.",
      "optional": 1,
      "type": "boolean"
    },
    "exitnodes-primary": {
      "description": "Force traffic through this exitnode first. EVPN zone only.",
      "format": "pve-node",
      "optional": 1,
      "type": "string"
    },
    "ipam": {
      "description": "ID of the IPAM for this zone.",
      "optional": 1,
      "type": "string"
    },
    "mac": {
      "description": "MAC address of the anycast router for this zone.",
      "optional": 1,
      "type": "string"
    },
    "mtu": {
      "description": "MTU of the zone, will be used for the created VNet bridges.",
      "optional": 1,
      "type": "integer"
    },
    "nodes": {
      "description": "Nodes where this zone should be created.",
      "optional": 1,
      "type": "string"
    },
    "peers": {
      "description": "Comma-separated list of peers, that are part of the VXLAN zone. Usually the IPs of the nodes. VXLAN zone only.",
      "format": "ip-list",
      "optional": 1,
      "type": "string"
    },
    "pending": {
      "description": "Changes that have not yet been applied to the running configuration.",
      "optional": 1,
      "properties": {
        "advertise-subnets": {
          "description": "Advertise IP prefixes (Type-5 routes) instead of MAC/IP pairs (Type-2 routes). EVPN zone only.",
          "optional": 1,
          "type": "boolean"
        },
        "bridge": {
          "description": "the bridge for which VLANs should be managed. VLAN & QinQ zone only.",
          "optional": 1,
          "type": "string"
        },
        "bridge-disable-mac-learning": {
          "description": "Disable auto mac learning. VLAN zone only.",
          "optional": 1,
          "type": "boolean"
        },
        "controller": {
          "description": "ID of the controller for this zone. EVPN zone only.",
          "optional": 1,
          "type": "string"
        },
        "dhcp": {
          "description": "Name of DHCP server backend for this zone.",
          "enum": [
            "dnsmasq"
          ],
          "optional": 1,
          "type": "string"
        },
        "disable-arp-nd-suppression": {
          "description": "Suppress IPv4 ARP && IPv6 Neighbour Discovery messages. EVPN zone only.",
          "optional": 1,
          "type": "boolean"
        },
        "dns": {
          "description": "ID of the DNS server for this zone.",
          "optional": 1,
          "type": "string"
        },
        "dnszone": {
          "description": "Domain name for this zone.",
          "optional": 1,
          "type": "string"
        },
        "exitnodes": {
          "description": "List of PVE Nodes that should act as exit node for this zone. EVPN zone only.",
          "format": "pve-node-list",
          "optional": 1,
          "type": "string"
        },
        "exitnodes-local-routing": {
          "description": "Create routes on the exit nodes, so they can connect to EVPN guests. EVPN zone only.",
          "optional": 1,
          "type": "boolean"
        },
        "exitnodes-primary": {
          "description": "Force traffic through this exitnode first. EVPN zone only.",
          "format": "pve-node",
          "optional": 1,
          "type": "string"
        },
        "ipam": {
          "description": "ID of the IPAM for this zone.",
          "optional": 1,
          "type": "string"
        },
        "mac": {
          "description": "MAC address of the anycast router for this zone.",
          "optional": 1,
          "type": "string"
        },
        "mtu": {
          "description": "MTU of the zone, will be used for the created VNet bridges.",
          "optional": 1,
          "type": "integer"
        },
        "nodes": {
          "description": "Nodes where this zone should be created.",
          "optional": 1,
          "type": "string"
        },
        "peers": {
          "description": "Comma-separated list of peers, that are part of the VXLAN zone. Usually the IPs of the nodes. VXLAN zone only.",
          "format": "ip-list",
          "optional": 1,
          "type": "string"
        },
        "reversedns": {
          "description": "ID of the reverse DNS server for this zone.",
          "optional": 1,
          "type": "string"
        },
        "rt-import": {
          "description": "Route-Targets that should be imported into the VRF of this zone via BGP. EVPN zone only.",
          "format": "pve-sdn-bgp-rt-list",
          "optional": 1,
          "type": "string"
        },
        "secondary-controllers": {
          "description": "Additional controllers.",
          "items": {
            "description": "Controller ID.",
            "maxLength": 64,
            "minLength": 2,
            "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        },
        "tag": {
          "description": "Service-VLAN Tag (outer VLAN). QinQ zone only",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "vlan-protocol": {
          "default": "802.1q",
          "description": "VLAN protocol for the creation of the QinQ zone. QinQ zone only.",
          "enum": [
            "802.1q",
            "802.1ad"
          ],
          "optional": 1,
          "type": "string"
        },
        "vrf-vxlan": {
          "description": "VNI for the zone VRF. EVPN zone only.",
          "maximum": 16777215,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "vxlan-port": {
          "default": 4789,
          "description": "UDP port that should be used for the VXLAN tunnel (default 4789). VXLAN zone only.",
          "maximum": 65536,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "reversedns": {
      "description": "ID of the reverse DNS server for this zone.",
      "optional": 1,
      "type": "string"
    },
    "rt-import": {
      "description": "Route-Targets that should be imported into the VRF of this zone via BGP. EVPN zone only.",
      "format": "pve-sdn-bgp-rt-list",
      "optional": 1,
      "type": "string"
    },
    "secondary-controllers": {
      "description": "Additional controllers.",
      "items": {
        "description": "Controller ID.",
        "maxLength": 64,
        "minLength": 2,
        "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "state": {
      "description": "State of the SDN configuration object.",
      "enum": [
        "new",
        "changed",
        "deleted"
      ],
      "optional": 1,
      "type": "string"
    },
    "tag": {
      "description": "Service-VLAN Tag (outer VLAN). QinQ zone only",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "type": {
      "description": "Type of the zone.",
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
      "description": "VLAN protocol for the creation of the QinQ zone. QinQ zone only.",
      "enum": [
        "802.1q",
        "802.1ad"
      ],
      "optional": 1,
      "type": "string"
    },
    "vrf-vxlan": {
      "description": "VNI for the zone VRF. EVPN zone only.",
      "maximum": 16777215,
      "minimum": 1,
      "optional": 1,
      "type": "integer"
    },
    "vxlan-port": {
      "default": 4789,
      "description": "UDP port that should be used for the VXLAN tunnel (default 4789). VXLAN zone only.",
      "maximum": 65536,
      "minimum": 1,
      "optional": 1,
      "type": "integer"
    },
    "zone": {
      "description": "Name of the zone.",
      "type": "string"
    }
  }
}
```

## PUT `/cluster/sdn/zones/{zone}`

Update sdn zone object configuration.

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
| `advertise-subnets` | boolean | 否 | — | Advertise IP prefixes (Type-5 routes) instead of MAC/IP pairs (Type-2 routes). |
| `bridge` | string | 否 | — | The bridge for which VLANs should be managed. |
| `bridge-disable-mac-learning` | boolean | 否 | — | Disable auto mac learning. |
| `controller` | string | 否 | — | Controller for this zone. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `dhcp` | string | 否 | — | Type of the DHCP backend for this zone；可选值：`dnsmasq` |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable-arp-nd-suppression` | boolean | 否 | — | Suppress IPv4 ARP && IPv6 Neighbour Discovery messages. |
| `dns` | string | 否 | — | dns api server |
| `dnszone` | string | 否 | — | dns domain zone ex: mydomain.com |
| `dp-id` | integer | 否 | — | Faucet dataplane id |
| `exitnodes` | string | 否 | — | List of cluster node names. |
| `exitnodes-local-routing` | boolean | 否 | — | Allow exitnodes to connect to EVPN guests. |
| `exitnodes-primary` | string | 否 | — | Force traffic through this exitnode first. |
| `fabric` | string | 否 | — | SDN fabric to use as underlay for this VXLAN zone. |
| `ipam` | string | 否 | — | use a specific ipam |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `mac` | string | 否 | — | Anycast logical router mac address. |
| `mtu` | integer | 否 | — | MTU of the zone, will be used for the created VNet bridges. |
| `nodes` | string | 否 | — | List of cluster node names. |
| `peers` | string | 否 | — | Comma-separated list of peers, that are part of the VXLAN zone. Usually the IPs of the nodes. |
| `reversedns` | string | 否 | — | reverse dns api server |
| `rt-import` | string | 否 | — | List of Route Targets that should be imported into the VRF of the zone. |
| `secondary-controllers` | array | 否 | — | Additional controllers. |
| `tag` | integer | 否 | — | Service-VLAN Tag (outer VLAN) |
| `vlan-protocol` | string | 否 | "802.1q" | Which VLAN protocol should be used for the creation of the QinQ zone.；可选值：`802.1q`, `802.1ad` |
| `vrf-vxlan` | integer | 否 | — | VNI for the zone VRF. |
| `vxlan-port` | integer | 否 | 4789 | UDP port that should be used for the VXLAN tunnel (default 4789). |
| `zone` | string | 是 | — | The SDN zone object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "advertise-subnets": {
      "description": "Advertise IP prefixes (Type-5 routes) instead of MAC/IP pairs (Type-2 routes).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bridge": {
      "description": "The bridge for which VLANs should be managed.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge-disable-mac-learning": {
      "description": "Disable auto mac learning.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "controller": {
      "description": "Controller for this zone.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dhcp": {
      "description": "Type of the DHCP backend for this zone",
      "enum": [
        "dnsmasq"
      ],
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable-arp-nd-suppression": {
      "description": "Suppress IPv4 ARP && IPv6 Neighbour Discovery messages.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "dns": {
      "description": "dns api server",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dnszone": {
      "description": "dns domain zone ex: mydomain.com",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dp-id": {
      "description": "Faucet dataplane id",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "exitnodes": {
      "description": "List of cluster node names.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "exitnodes-local-routing": {
      "description": "Allow exitnodes to connect to EVPN guests.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "exitnodes-primary": {
      "description": "Force traffic through this exitnode first.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fabric": {
      "description": "SDN fabric to use as underlay for this VXLAN zone.",
      "format": "pve-sdn-fabric-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ipam": {
      "description": "use a specific ipam",
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
    "mac": {
      "description": "Anycast logical router mac address.",
      "format": "mac-addr",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mtu": {
      "description": "MTU of the zone, will be used for the created VNet bridges.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "nodes": {
      "description": "List of cluster node names.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "peers": {
      "description": "Comma-separated list of peers, that are part of the VXLAN zone. Usually the IPs of the nodes.",
      "format": "ip-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "reversedns": {
      "description": "reverse dns api server",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "rt-import": {
      "description": "List of Route Targets that should be imported into the VRF of the zone.",
      "format": "pve-sdn-bgp-rt-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "secondary-controllers": {
      "description": "Additional controllers.",
      "items": {
        "description": "Controller ID.",
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
      "description": "Service-VLAN Tag (outer VLAN)",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vlan-protocol": {
      "default": "802.1q",
      "description": "Which VLAN protocol should be used for the creation of the QinQ zone.",
      "enum": [
        "802.1q",
        "802.1ad"
      ],
      "optional": 1,
      "type": "string"
    },
    "vrf-vxlan": {
      "description": "VNI for the zone VRF.",
      "maximum": 16777215,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 16777215)"
    },
    "vxlan-port": {
      "default": 4789,
      "description": "UDP port that should be used for the VXLAN tunnel (default 4789).",
      "maximum": 65536,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "zone": {
      "description": "The SDN zone object identifier.",
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
