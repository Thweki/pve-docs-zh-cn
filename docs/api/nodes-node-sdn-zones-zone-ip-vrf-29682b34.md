# `/nodes/{node}/sdn/zones/{zone}/ip-vrf`

原始接口路径：`/nodes/{node}/sdn/zones/{zone}/ip-vrf`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/zones/{zone}/ip-vrf`

获取 EVPN 区域的 IP VRF。

**方法标识：** `ip-vrf`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `zone` | string | 是 | — | EVPN 区域名称。 |

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
    "zone": {
      "description": "EVPN 区域名称。",
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
  "description": "节点上区域 {zone} 的 VRF 表中的所有条目。不包括此宿主机上客户机的 /32 路由，因为这些路由通过相应的 vnet 网桥直接处理。",
  "items": {
    "properties": {
      "ip": {
        "description": "路由表条目的 CIDR。",
        "format": "CIDR",
        "type": "string"
      },
      "metric": {
        "description": "此路由的度量值。",
        "type": "integer"
      },
      "nexthops": {
        "description": "路由表条目的下一跳列表。",
        "items": {
          "description": "下一跳的接口名称或 IP 地址",
          "type": "string"
        },
        "type": "array"
      },
      "protocol": {
        "description": "学习到此路由所用的协议（例如 BGP）。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/zones/{zone}/ip-vrf)。
