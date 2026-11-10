# `/nodes/{node}/lxc/{vmid}/interfaces`

原始接口路径：`/nodes/{node}/lxc/{vmid}/interfaces`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/interfaces`

Get IP addresses of the specified container interface.

**方法标识：** `ip`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
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
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

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
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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
      "hardware-address": {
        "description": "The MAC address of the interface",
        "optional": 0,
        "type": "string"
      },
      "hwaddr": {
        "description": "The MAC address of the interface",
        "optional": 0,
        "type": "string"
      },
      "inet": {
        "description": "The IPv4 address of the interface",
        "optional": 1,
        "type": "string"
      },
      "inet6": {
        "description": "The IPv6 address of the interface",
        "optional": 1,
        "type": "string"
      },
      "ip-addresses": {
        "description": "The addresses of the interface",
        "items": {
          "properties": {
            "ip-address": {
              "description": "IP-Address",
              "optional": 1,
              "type": "string"
            },
            "ip-address-type": {
              "description": "IP-Family",
              "optional": 1,
              "type": "string"
            },
            "prefix": {
              "description": "IP-Prefix",
              "optional": 1,
              "type": "integer"
            }
          },
          "type": "object"
        },
        "optional": 0,
        "type": "array"
      },
      "name": {
        "description": "The name of the interface",
        "optional": 0,
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/interfaces)。
