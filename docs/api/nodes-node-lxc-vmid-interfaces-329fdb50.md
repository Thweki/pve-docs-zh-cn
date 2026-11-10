# `/nodes/{node}/lxc/{vmid}/interfaces`

原始接口路径：`/nodes/{node}/lxc/{vmid}/interfaces`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/interfaces`

获取指定容器接口的 IP 地址。

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
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

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
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
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
        "description": "接口的 MAC 地址",
        "optional": 0,
        "type": "string"
      },
      "hwaddr": {
        "description": "接口的 MAC 地址",
        "optional": 0,
        "type": "string"
      },
      "inet": {
        "description": "接口的 IPv4 地址",
        "optional": 1,
        "type": "string"
      },
      "inet6": {
        "description": "接口的 IPv6 地址",
        "optional": 1,
        "type": "string"
      },
      "ip-addresses": {
        "description": "接口的地址",
        "items": {
          "properties": {
            "ip-address": {
              "description": "IP 地址",
              "optional": 1,
              "type": "string"
            },
            "ip-address-type": {
              "description": "IP 地址族",
              "optional": 1,
              "type": "string"
            },
            "prefix": {
              "description": "IP 前缀",
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
        "description": "接口名称",
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
