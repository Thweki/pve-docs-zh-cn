# `/cluster/sdn/vnets`

原始接口路径：`/cluster/sdn/vnets`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets`

SDN vnet 索引。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目",
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
        "description": "VNet 的别名。",
        "maxLength": 256,
        "optional": 1,
        "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})",
        "type": "string"
      },
      "digest": {
        "description": "VNet 配置节的摘要。",
        "optional": 1,
        "type": "string"
      },
      "isolate-ports": {
        "description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。",
        "optional": 1,
        "type": "boolean"
      },
      "pending": {
        "description": "尚未应用到运行配置的更改。",
        "optional": 1,
        "properties": {
          "alias": {
            "description": "VNet 的别名。",
            "maxLength": 256,
            "optional": 1,
            "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})",
            "type": "string"
          },
          "isolate-ports": {
            "description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。",
            "optional": 1,
            "type": "boolean"
          },
          "tag": {
            "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。",
            "maximum": 16777215,
            "minimum": 1,
            "optional": 1,
            "type": "integer"
          },
          "vlanaware": {
            "description": "允许 VLAN 穿过此 VNet。",
            "optional": 1,
            "type": "boolean"
          },
          "zone": {
            "description": "此 VNet 所属区域的名称。",
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
      "tag": {
        "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。",
        "maximum": 16777215,
        "minimum": 1,
        "optional": 1,
        "type": "integer"
      },
      "type": {
        "description": "VNet 的类型。",
        "enum": [
          "vnet"
        ],
        "optional": 0,
        "type": "string"
      },
      "vlanaware": {
        "description": "允许 VLAN 穿过此 VNet。",
        "optional": 1,
        "type": "boolean"
      },
      "vnet": {
        "description": "VNet 的名称。",
        "optional": 0,
        "type": "string"
      },
      "zone": {
        "description": "此 VNet 所属区域的名称。",
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

创建新的 SDN vnet 对象。

**方法标识：** `create`

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
| `alias` | string | 否 | — | VNet 的别名。 |
| `isolate-ports` | boolean | 否 | — | 如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `tag` | integer | 否 | — | VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。 |
| `type` | string | 否 | — | VNet 的类型。；可选值：`vnet` |
| `vlanaware` | boolean | 否 | — | 允许 VLAN 穿过此 vnet。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |
| `zone` | string | 是 | — | 此 VNet 所属区域的名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "alias": {
      "description": "VNet 的别名。",
      "maxLength": 256,
      "optional": 1,
      "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})",
      "type": "string"
    },
    "isolate-ports": {
      "description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tag": {
      "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。",
      "maximum": 16777215,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 16777215)"
    },
    "type": {
      "description": "VNet 的类型。",
      "enum": [
        "vnet"
      ],
      "optional": 1,
      "type": "string"
    },
    "vlanaware": {
      "description": "允许 VLAN 穿过此 vnet。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "此 VNet 所属区域的名称。",
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
