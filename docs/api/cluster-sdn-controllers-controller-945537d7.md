# `/cluster/sdn/controllers/{controller}`

原始接口路径：`/cluster/sdn/controllers/{controller}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/controllers/{controller}`

Delete sdn controller object configuration.

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/controllers",
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
| `controller` | string | 是 | — | The SDN controller object identifier. |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "controller": {
      "description": "The SDN controller object identifier.",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
      "type": "string"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
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

## GET `/cluster/sdn/controllers/{controller}`

Read sdn controller configuration.

**方法标识：** `read`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/controllers/{controller}",
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
| `controller` | string | 是 | — | The SDN controller object identifier. |
| `pending` | boolean | 否 | — | Display pending config. |
| `running` | boolean | 否 | — | Display running config. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "controller": {
      "description": "The SDN controller object identifier.",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
      "type": "string"
    },
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
  "properties": {
    "asn": {
      "description": "The local ASN of the controller. BGP & EVPN only.",
      "maximum": 4294967295,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "bgp-mode": {
      "default": "auto",
      "description": "Whether to use eBGP or iBGP. Auto mode chooses depending on BGP controller or falls back to iBGP.",
      "enum": [
        "auto",
        "external",
        "internal"
      ],
      "optional": 1,
      "type": "string"
    },
    "bgp-multipath-as-relax": {
      "description": "Consider different AS paths of equal length for multipath computation. BGP only.",
      "optional": 1,
      "type": "boolean"
    },
    "controller": {
      "description": "Name of the controller.",
      "type": "string"
    },
    "digest": {
      "description": "Digest of the controller section.",
      "optional": 1,
      "type": "string"
    },
    "ebgp": {
      "description": "Enable eBGP (remote-as external). BGP only.",
      "optional": 1,
      "type": "boolean"
    },
    "ebgp-multihop": {
      "description": "Set maximum amount of hops for eBGP peers. Needs ebgp set to 1. BGP only.",
      "optional": 1,
      "type": "integer"
    },
    "isis-domain": {
      "description": "Name of the IS-IS domain. IS-IS only.",
      "optional": 1,
      "type": "string"
    },
    "isis-ifaces": {
      "description": "Comma-separated list of interfaces where IS-IS should be active. IS-IS only.",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string"
    },
    "isis-net": {
      "description": "Network Entity title for this node in the IS-IS network. IS-IS only.",
      "format": "pve-sdn-isis-net",
      "optional": 1,
      "type": "string"
    },
    "loopback": {
      "description": "Name of the loopback/dummy interface that provides the Router-IP. BGP only.",
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "Node(s) where this controller is active.",
      "optional": 1,
      "type": "string"
    },
    "nodes": {
      "description": "List of cluster node names.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string"
    },
    "peer-group-name": {
      "description": "Name of the peer group for this EVPN controller",
      "optional": 1,
      "type": "string"
    },
    "peers": {
      "description": "Comma-separated list of the peers IP addresses.",
      "optional": 1,
      "type": "string"
    },
    "pending": {
      "description": "Changes that have not yet been applied to the running configuration.",
      "optional": 1,
      "properties": {
        "asn": {
          "description": "The local ASN of the controller. BGP & EVPN only.",
          "maximum": 4294967295,
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "bgp-mode": {
          "default": "auto",
          "description": "Whether to use eBGP or iBGP. Auto mode chooses depending on BGP controller or falls back to iBGP.",
          "enum": [
            "auto",
            "external",
            "internal"
          ],
          "optional": 1,
          "type": "string"
        },
        "bgp-multipath-as-relax": {
          "description": "Consider different AS paths of equal length for multipath computation. BGP only.",
          "optional": 1,
          "type": "boolean"
        },
        "ebgp": {
          "description": "Enable eBGP (remote-as external). BGP only.",
          "optional": 1,
          "type": "boolean"
        },
        "ebgp-multihop": {
          "description": "Set maximum amount of hops for eBGP peers. Needs ebgp set to 1. BGP only.",
          "optional": 1,
          "type": "integer"
        },
        "isis-domain": {
          "description": "Name of the IS-IS domain. IS-IS only.",
          "optional": 1,
          "type": "string"
        },
        "isis-ifaces": {
          "description": "Comma-separated list of interfaces where IS-IS should be active. IS-IS only.",
          "format": "pve-iface-list",
          "optional": 1,
          "type": "string"
        },
        "isis-net": {
          "description": "Network Entity title for this node in the IS-IS network. IS-IS only.",
          "format": "pve-sdn-isis-net",
          "optional": 1,
          "type": "string"
        },
        "loopback": {
          "description": "Name of the loopback/dummy interface that provides the Router-IP. BGP only.",
          "optional": 1,
          "type": "string"
        },
        "node": {
          "description": "Node(s) where this controller is active.",
          "optional": 1,
          "type": "string"
        },
        "nodes": {
          "description": "List of cluster node names.",
          "format": "pve-node-list",
          "optional": 1,
          "type": "string"
        },
        "peer-group-name": {
          "description": "Name of the peer group for this EVPN controller",
          "optional": 1,
          "type": "string"
        },
        "peers": {
          "description": "Comma-separated list of the peers IP addresses.",
          "optional": 1,
          "type": "string"
        }
      },
      "type": "object"
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
    "type": {
      "description": "Type of the controller",
      "enum": [
        "bgp",
        "evpn",
        "faucet",
        "isis"
      ],
      "type": "string"
    }
  }
}
```

## PUT `/cluster/sdn/controllers/{controller}`

Update sdn controller object configuration.

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/controllers",
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
| `asn` | integer | 否 | — | autonomous system number |
| `bgp-mode` | string | 否 | "auto" | Whether to use eBGP or iBGP. Auto mode chooses depending on BGP controller or falls back to iBGP.；可选值：`auto`, `external`, `internal` |
| `bgp-multipath-as-path-relax` | boolean | 否 | — | Consider different AS paths of equal length for multipath computation. |
| `controller` | string | 是 | — | The SDN controller object identifier. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `ebgp` | boolean | 否 | — | Enable eBGP (remote-as external). |
| `ebgp-multihop` | integer | 否 | — | Set maximum amount of hops for eBGP peers. |
| `fabric` | string | 否 | — | SDN fabric to use as underlay for this EVPN controller. |
| `isis-domain` | string | 否 | — | Name of the IS-IS domain. |
| `isis-ifaces` | string | 否 | — | Comma-separated list of interfaces where IS-IS should be active. |
| `isis-net` | string | 否 | — | Network Entity title for this node in the IS-IS network. |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `loopback` | string | 否 | — | Name of the loopback/dummy interface that provides the Router-IP. |
| `node` | string | 否 | — | The cluster node name. |
| `nodes` | string | 否 | — | List of cluster node names. |
| `peer-group-name` | string | 否 | "VTEP" | Name of the peer group for this EVPN controller |
| `peers` | string | 否 | — | peers address list. |
| `route-map-in` | string | 否 | — | Route Map that should be applied for incoming routes |
| `route-map-out` | string | 否 | — | Route Map that should be applied for outgoing routes |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "asn": {
      "description": "autonomous system number",
      "maximum": 4294967295,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 4294967295)"
    },
    "bgp-mode": {
      "default": "auto",
      "description": "Whether to use eBGP or iBGP. Auto mode chooses depending on BGP controller or falls back to iBGP.",
      "enum": [
        "auto",
        "external",
        "internal"
      ],
      "optional": 1,
      "type": "string"
    },
    "bgp-multipath-as-path-relax": {
      "description": "Consider different AS paths of equal length for multipath computation.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "controller": {
      "description": "The SDN controller object identifier.",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
      "type": "string"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ebgp": {
      "description": "Enable eBGP (remote-as external).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ebgp-multihop": {
      "description": "Set maximum amount of hops for eBGP peers.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "fabric": {
      "description": "SDN fabric to use as underlay for this EVPN controller.",
      "format": "pve-sdn-fabric-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "isis-domain": {
      "description": "Name of the IS-IS domain.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "isis-ifaces": {
      "description": "Comma-separated list of interfaces where IS-IS should be active.",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "isis-net": {
      "description": "Network Entity title for this node in the IS-IS network.",
      "format": "pve-sdn-isis-net",
      "maxLength": 50,
      "minLength": 20,
      "optional": 1,
      "pattern": "[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}",
      "type": "string"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "loopback": {
      "description": "Name of the loopback/dummy interface that provides the Router-IP.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nodes": {
      "description": "List of cluster node names.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "peer-group-name": {
      "default": "VTEP",
      "description": "Name of the peer group for this EVPN controller",
      "format": "pve-configid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "peers": {
      "description": "peers address list.",
      "format": "ip-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "route-map-in": {
      "description": "Route Map that should be applied for incoming routes",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "route-map-out": {
      "description": "Route Map that should be applied for outgoing routes",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/controllers/{controller})。
