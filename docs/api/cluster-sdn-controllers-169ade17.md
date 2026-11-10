# `/cluster/sdn/controllers`

原始接口路径：`/cluster/sdn/controllers`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/controllers`

SDN 控制器索引。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/sdn/controllers/<controller>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目",
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
| `type` | string | 否 | — | 仅列出特定类型的 SDN 控制器；可选值：`bgp`, `evpn`, `faucet`, `isis` |

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
    "type": {
      "description": "仅列出特定类型的 SDN 控制器",
      "enum": [
        "bgp",
        "evpn",
        "faucet",
        "isis"
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
      "asn": {
        "description": "控制器的本地 ASN。仅适用于 BGP 和 EVPN。",
        "maximum": 4294967295,
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "bgp-mode": {
        "default": "auto",
        "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。",
        "enum": [
          "auto",
          "external",
          "internal"
        ],
        "optional": 1,
        "type": "string"
      },
      "bgp-multipath-as-relax": {
        "description": "在多路径计算中考虑长度相等的不同 AS 路径。仅适用于 BGP。",
        "optional": 1,
        "type": "boolean"
      },
      "controller": {
        "description": "控制器名称。",
        "type": "string"
      },
      "digest": {
        "description": "控制器配置节的摘要。",
        "optional": 1,
        "type": "string"
      },
      "ebgp": {
        "description": "启用 eBGP（remote-as external）。仅适用于 BGP。",
        "optional": 1,
        "type": "boolean"
      },
      "ebgp-multihop": {
        "description": "设置 eBGP 对等端的最大跳数。需要将 ebgp 设为 1。仅适用于 BGP。",
        "optional": 1,
        "type": "integer"
      },
      "isis-domain": {
        "description": "IS-IS 域的名称。仅适用于 IS-IS。",
        "optional": 1,
        "type": "string"
      },
      "isis-ifaces": {
        "description": "应启用 IS-IS 的接口列表，以逗号分隔。仅适用于 IS-IS。",
        "format": "pve-iface-list",
        "optional": 1,
        "type": "string"
      },
      "isis-net": {
        "description": "此节点在 IS-IS 网络中的网络实体名称。仅适用于 IS-IS。",
        "format": "pve-sdn-isis-net",
        "optional": 1,
        "type": "string"
      },
      "loopback": {
        "description": "提供 Router-IP 的 loopback/dummy 接口名称。仅适用于 BGP。",
        "optional": 1,
        "type": "string"
      },
      "node": {
        "description": "启用此控制器的节点。",
        "optional": 1,
        "type": "string"
      },
      "nodes": {
        "description": "集群节点名称列表。",
        "format": "pve-node-list",
        "optional": 1,
        "type": "string"
      },
      "peer-group-name": {
        "description": "此 EVPN 控制器的对等组名称",
        "optional": 1,
        "type": "string"
      },
      "peers": {
        "description": "对等端 IP 地址列表，以逗号分隔。",
        "optional": 1,
        "type": "string"
      },
      "pending": {
        "description": "尚未应用到运行配置的更改。",
        "optional": 1,
        "properties": {
          "asn": {
            "description": "控制器的本地 ASN。仅适用于 BGP 和 EVPN。",
            "maximum": 4294967295,
            "minimum": 0,
            "optional": 1,
            "type": "integer"
          },
          "bgp-mode": {
            "default": "auto",
            "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。",
            "enum": [
              "auto",
              "external",
              "internal"
            ],
            "optional": 1,
            "type": "string"
          },
          "bgp-multipath-as-relax": {
            "description": "在多路径计算中考虑长度相等的不同 AS 路径。仅适用于 BGP。",
            "optional": 1,
            "type": "boolean"
          },
          "ebgp": {
            "description": "启用 eBGP（remote-as external）。仅适用于 BGP。",
            "optional": 1,
            "type": "boolean"
          },
          "ebgp-multihop": {
            "description": "设置 eBGP 对等端的最大跳数。需要将 ebgp 设为 1。仅适用于 BGP。",
            "optional": 1,
            "type": "integer"
          },
          "isis-domain": {
            "description": "IS-IS 域的名称。仅适用于 IS-IS。",
            "optional": 1,
            "type": "string"
          },
          "isis-ifaces": {
            "description": "应启用 IS-IS 的接口列表，以逗号分隔。仅适用于 IS-IS。",
            "format": "pve-iface-list",
            "optional": 1,
            "type": "string"
          },
          "isis-net": {
            "description": "此节点在 IS-IS 网络中的网络实体名称。仅适用于 IS-IS。",
            "format": "pve-sdn-isis-net",
            "optional": 1,
            "type": "string"
          },
          "loopback": {
            "description": "提供 Router-IP 的 loopback/dummy 接口名称。仅适用于 BGP。",
            "optional": 1,
            "type": "string"
          },
          "node": {
            "description": "启用此控制器的节点。",
            "optional": 1,
            "type": "string"
          },
          "nodes": {
            "description": "集群节点名称列表。",
            "format": "pve-node-list",
            "optional": 1,
            "type": "string"
          },
          "peer-group-name": {
            "description": "此 EVPN 控制器的对等组名称",
            "optional": 1,
            "type": "string"
          },
          "peers": {
            "description": "对等端 IP 地址列表，以逗号分隔。",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
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
      "type": {
        "description": "控制器类型",
        "enum": [
          "bgp",
          "evpn",
          "faucet",
          "isis"
        ],
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{controller}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/sdn/controllers`

创建新的 SDN 控制器对象。

**方法标识：** `create`

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
| `asn` | integer | 否 | — | 自治系统编号 |
| `bgp-mode` | string | 否 | "auto" | 使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。；可选值：`auto`, `external`, `internal` |
| `bgp-multipath-as-path-relax` | boolean | 否 | — | 在多路径计算中考虑长度相等的不同 AS 路径。 |
| `controller` | string | 是 | — | SDN 控制器对象标识符。 |
| `ebgp` | boolean | 否 | — | 启用 eBGP（remote-as external）。 |
| `ebgp-multihop` | integer | 否 | — | 设置 eBGP 对等端的最大跳数。 |
| `fabric` | string | 否 | — | 此 EVPN 控制器用作底层网络的 SDN fabric。 |
| `isis-domain` | string | 否 | — | IS-IS 域的名称。 |
| `isis-ifaces` | string | 否 | — | 应启用 IS-IS 的接口列表，以逗号分隔。 |
| `isis-net` | string | 否 | — | 此节点在 IS-IS 网络中的网络实体名称。 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `loopback` | string | 否 | — | 提供 Router-IP 的 loopback/dummy 接口名称。 |
| `node` | string | 否 | — | 集群节点名称。 |
| `nodes` | string | 否 | — | 集群节点名称列表。 |
| `peer-group-name` | string | 否 | "VTEP" | 此 EVPN 控制器的对等组名称 |
| `peers` | string | 否 | — | 对等端地址列表。 |
| `route-map-in` | string | 否 | — | 应对传入路由应用的 Route Map |
| `route-map-out` | string | 否 | — | 应对传出路由应用的 Route Map |
| `type` | string | 是 | — | 插件类型。；可选值：`bgp`, `evpn`, `faucet`, `isis` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "asn": {
      "description": "自治系统编号",
      "maximum": 4294967295,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 4294967295)"
    },
    "bgp-mode": {
      "default": "auto",
      "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。",
      "enum": [
        "auto",
        "external",
        "internal"
      ],
      "optional": 1,
      "type": "string"
    },
    "bgp-multipath-as-path-relax": {
      "description": "在多路径计算中考虑长度相等的不同 AS 路径。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "controller": {
      "description": "SDN 控制器对象标识符。",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]",
      "type": "string"
    },
    "ebgp": {
      "description": "启用 eBGP（remote-as external）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ebgp-multihop": {
      "description": "设置 eBGP 对等端的最大跳数。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "fabric": {
      "description": "此 EVPN 控制器用作底层网络的 SDN fabric。",
      "format": "pve-sdn-fabric-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "isis-domain": {
      "description": "IS-IS 域的名称。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "isis-ifaces": {
      "description": "应启用 IS-IS 的接口列表，以逗号分隔。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "isis-net": {
      "description": "此节点在 IS-IS 网络中的网络实体名称。",
      "format": "pve-sdn-isis-net",
      "maxLength": 50,
      "minLength": 20,
      "optional": 1,
      "pattern": "[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}",
      "type": "string"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "loopback": {
      "description": "提供 Router-IP 的 loopback/dummy 接口名称。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nodes": {
      "description": "集群节点名称列表。",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "peer-group-name": {
      "default": "VTEP",
      "description": "此 EVPN 控制器的对等组名称",
      "format": "pve-configid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "peers": {
      "description": "对等端地址列表。",
      "format": "ip-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "route-map-in": {
      "description": "应对传入路由应用的 Route Map",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "route-map-out": {
      "description": "应对传出路由应用的 Route Map",
      "format": "pve-sdn-route-map-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "插件类型。",
      "enum": [
        "bgp",
        "evpn",
        "faucet",
        "isis"
      ],
      "format": "pve-configid",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/controllers)。
