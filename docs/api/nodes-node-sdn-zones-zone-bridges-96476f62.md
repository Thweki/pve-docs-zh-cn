# `/nodes/{node}/sdn/zones/{zone}/bridges`

原始接口路径：`/nodes/{node}/sdn/zones/{zone}/bridges`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/sdn/zones/{zone}/bridges`

Get a list of all bridges (vnets) that are part of a zone, as well as the ports that are members of that bridge.

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
| `zone` | string | 是 | — | zone name or "localnetwork" |

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
      "description": "zone name or \"localnetwork\"",
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
    "description": "List of bridges contained in the SDN zone.",
    "properties": {
      "name": {
        "description": "Name of the bridge.",
        "type": "string"
      },
      "ports": {
        "description": "All ports that are members of the bridge",
        "items": {
          "description": "Information about bridge ports.",
          "properties": {
            "index": {
              "description": "The index of the guests network device that this interface belongs to.",
              "optional": 1,
              "type": "string"
            },
            "name": {
              "description": "The name of the bridge port.",
              "type": "string"
            },
            "primary_vlan": {
              "description": "The primary VLAN configured for the port of this bridge (= PVID). Only for VLAN-aware bridges.",
              "optional": 1,
              "type": "number"
            },
            "vlans": {
              "description": "A list of VLANs and VLAN ranges that are allowed for this bridge port in addition to the primary VLAN. Only for VLAN-aware bridges.",
              "items": {
                "description": "A single VLAN (123) or a VLAN range (234-435).",
                "type": "string"
              },
              "optional": 1,
              "type": "array"
            },
            "vmid": {
              "description": "The ID of the guest that this interface belongs to.",
              "optional": 1,
              "type": "number"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "vlan_filtering": {
        "description": "Whether VLAN filtering is enabled for this bridge (= VLAN-aware).",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/sdn/zones/{zone}/bridges)。
