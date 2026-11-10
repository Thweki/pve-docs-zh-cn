# `/nodes/{node}/sdn/zones/{zone}/ip-vrf`

原始接口路径：`/nodes/{node}/sdn/zones/{zone}/ip-vrf`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/zones/{zone}/ip-vrf`

Get the IP VRF of an EVPN zone.

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}",
    [
      "SDN.Audit"
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
| `zone` | string | 是 | — | Name of an EVPN zone. |

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
    "zone": {
      "description": "Name of an EVPN zone.",
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
  "description": "All entries in the VRF table of zone {zone} of the node.This does not include /32 routes for guests on this host,since they are handled via the respective vnet bridge directly.",
  "items": {
    "properties": {
      "ip": {
        "description": "The CIDR of the route table entry.",
        "format": "CIDR",
        "type": "string"
      },
      "metric": {
        "description": "This route's metric.",
        "type": "integer"
      },
      "nexthops": {
        "description": "A list of nexthops for the route table entry.",
        "items": {
          "description": "the interface name or ip address of the next hop",
          "type": "string"
        },
        "type": "array"
      },
      "protocol": {
        "description": "The protocol where this route was learned from (e.g. BGP).",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/zones/{zone}/ip-vrf)。
