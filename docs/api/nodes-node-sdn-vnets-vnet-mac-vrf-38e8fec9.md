# `/nodes/{node}/sdn/vnets/{vnet}/mac-vrf`

原始接口路径：`/nodes/{node}/sdn/vnets/{vnet}/mac-vrf`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/vnets/{vnet}/mac-vrf`

获取 EVPN 区域中某 VNet 的 MAC VRF。

**方法标识：** `mac-vrf`

**权限**

```json
{
  "description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 权限",
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
| `node` | string | 是 | — | 集群节点名称。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

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
    "vnet": {
      "description": "SDN vnet 对象标识符。",
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
  "description": "此节点自行发起或通过 BGP 学习到的 MAC VRF 中的所有路由。",
  "items": {
    "properties": {
      "ip": {
        "description": "MAC VRF 条目的 IP 地址。",
        "format": "ip",
        "type": "string"
      },
      "mac": {
        "description": "MAC VRF 条目的 MAC 地址。",
        "format": "mac-addr",
        "type": "string"
      },
      "nexthop": {
        "description": "下一跳的 IP 地址。",
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
