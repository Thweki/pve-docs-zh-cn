# `/cluster/sdn/vnets`

原始接口路径：`/cluster/sdn/vnets`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets`

SDN vnets index.

**权限**

```json
{
  "description": "Only list entries where you have 'SDN.Audit' or 'SDN.Allocate' permissions on '/sdn/zones/<zone>/<vnet>'",
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
      "alias": {
        "description": "Alias name of the VNet.",
        "maxLength": 256,
        "optional": 1,
        "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})",
        "type": "string"
      },
      "digest": {
        "description": "Digest of the VNet section.",
        "optional": 1,
        "type": "string"
      },
      "isolate-ports": {
        "description": "If true, sets the isolated property for all interfaces on the bridge of this VNet.",
        "optional": 1,
        "type": "boolean"
      },
      "pending": {
        "description": "Changes that have not yet been applied to the running configuration.",
        "optional": 1,
        "properties": {
          "alias": {
            "description": "Alias name of the VNet.",
            "maxLength": 256,
            "optional": 1,
            "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})",
            "type": "string"
          },
          "isolate-ports": {
            "description": "If true, sets the isolated property for all interfaces on the bridge of this VNet.",
            "optional": 1,
            "type": "boolean"
          },
          "tag": {
            "description": "VLAN Tag (for VLAN or QinQ zones) or VXLAN VNI (for VXLAN or EVPN zones).",
            "maximum": 16777215,
            "minimum": 1,
            "optional": 1,
            "type": "integer"
          },
          "vlanaware": {
            "description": "Allow VLANs to pass through this VNet.",
            "optional": 1,
            "type": "boolean"
          },
          "zone": {
            "description": "Name of the zone this VNet belongs to.",
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
      "tag": {
        "description": "VLAN Tag (for VLAN or QinQ zones) or VXLAN VNI (for VXLAN or EVPN zones).",
        "maximum": 16777215,
        "minimum": 1,
        "optional": 1,
        "type": "integer"
      },
      "type": {
        "description": "Type of the VNet.",
        "enum": [
          "vnet"
        ],
        "optional": 0,
        "type": "string"
      },
      "vlanaware": {
        "description": "Allow VLANs to pass through this VNet.",
        "optional": 1,
        "type": "boolean"
      },
      "vnet": {
        "description": "Name of the VNet.",
        "optional": 0,
        "type": "string"
      },
      "zone": {
        "description": "Name of the zone this VNet belongs to.",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{vnet}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/sdn/vnets`

Create a new sdn vnet object.

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
| `alias` | string | 否 | — | Alias name of the VNet. |
| `isolate-ports` | boolean | 否 | — | If true, sets the isolated property for all interfaces on the bridge of this VNet. |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `tag` | integer | 否 | — | VLAN Tag (for VLAN or QinQ zones) or VXLAN VNI (for VXLAN or EVPN zones). |
| `type` | string | 否 | — | Type of the VNet.；可选值：`vnet` |
| `vlanaware` | boolean | 否 | — | Allow VLANs to pass through this vnet. |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |
| `zone` | string | 是 | — | Name of the zone this VNet belongs to. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "alias": {
      "description": "Alias name of the VNet.",
      "maxLength": 256,
      "optional": 1,
      "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})",
      "type": "string"
    },
    "isolate-ports": {
      "description": "If true, sets the isolated property for all interfaces on the bridge of this VNet.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tag": {
      "description": "VLAN Tag (for VLAN or QinQ zones) or VXLAN VNI (for VXLAN or EVPN zones).",
      "maximum": 16777215,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 16777215)"
    },
    "type": {
      "description": "Type of the VNet.",
      "enum": [
        "vnet"
      ],
      "optional": 1,
      "type": "string"
    },
    "vlanaware": {
      "description": "Allow VLANs to pass through this vnet.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vnet": {
      "description": "The SDN vnet object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "Name of the zone this VNet belongs to.",
      "optional": 0,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets)。
