# `/nodes/{node}/sdn/vnets/{vnet}/mac-vrf`

原始接口路径：`/nodes/{node}/sdn/vnets/{vnet}/mac-vrf`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/vnets/{vnet}/mac-vrf`

Get the MAC VRF for a VNet in an EVPN zone.

**方法标识：** `mac-vrf`

**权限**

```json
{
  "description": "Require 'SDN.Audit' permissions on '/sdn/zones/<zone>/<vnet>'",
  "user": "all"
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
| `vnet` | string | 是 | — | The SDN vnet object identifier. |

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
    "vnet": {
      "description": "The SDN vnet object identifier.",
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
  "description": "All routes from the MAC VRF that this node self-originates or has learned via BGP.",
  "items": {
    "properties": {
      "ip": {
        "description": "The IP address of the MAC VRF entry.",
        "format": "ip",
        "type": "string"
      },
      "mac": {
        "description": "The MAC address of the MAC VRF entry.",
        "format": "mac-addr",
        "type": "string"
      },
      "nexthop": {
        "description": "The IP address of the nexthop.",
        "format": "ip",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/vnets/{vnet}/mac-vrf)。
