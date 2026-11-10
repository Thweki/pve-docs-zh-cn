# `/nodes/{node}/sdn/zones/{zone}/bridges`

原始接口路径：`/nodes/{node}/sdn/zones/{zone}/bridges`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/zones/{zone}/bridges`

获取属于某区域的所有网桥（vnet）以及各网桥成员端口的列表。

**方法标识：** `bridges`

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
| `zone` | string | 是 | — | 区域名称或 "localnetwork" |

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
      "description": "区域名称或 \"localnetwork\"",
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
  "items": {
    "description": "SDN 区域中包含的网桥列表。",
    "properties": {
      "name": {
        "description": "网桥名称。",
        "type": "string"
      },
      "ports": {
        "description": "属于网桥成员的所有端口",
        "items": {
          "description": "有关网桥端口的信息。",
          "properties": {
            "index": {
              "description": "此接口所属的客户机网络设备的索引。",
              "optional": 1,
              "type": "string"
            },
            "name": {
              "description": "网桥端口名称。",
              "type": "string"
            },
            "primary_vlan": {
              "description": "为此网桥端口配置的主 VLAN（= PVID）。仅适用于支持 VLAN 感知的网桥。",
              "optional": 1,
              "type": "number"
            },
            "vlans": {
              "description": "除了主 VLAN 之外，此网桥端口允许的 VLAN 和 VLAN 范围列表。仅适用于支持 VLAN 感知的网桥。",
              "items": {
                "description": "单个 VLAN（123）或 VLAN 范围（234-435）。",
                "type": "string"
              },
              "optional": 1,
              "type": "array"
            },
            "vmid": {
              "description": "此接口所属的客户机 ID。",
              "optional": 1,
              "type": "number"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "vlan_filtering": {
        "description": "此网桥是否启用了 VLAN 过滤（= VLAN 感知）。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/zones/{zone}/bridges)。
