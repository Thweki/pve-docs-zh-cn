# `/nodes/{node}/lxc/{vmid}/firewall/refs`

原始接口路径：`/nodes/{node}/lxc/{vmid}/firewall/refs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/firewall/refs`

列出源地址/目标地址属性中允许使用的 IPSet/别名引用。

**方法标识：** `refs`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |
| `type` | string | 否 | — | 仅列出指定类型的引用。；可选值：`alias`, `ipset` |
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
    "type": {
      "description": "仅列出指定类型的引用。",
      "enum": [
        "alias",
        "ipset"
      ],
      "optional": 1,
      "type": "string"
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
      "comment": {
        "optional": 1,
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "ref": {
        "type": "string"
      },
      "scope": {
        "type": "string"
      },
      "type": {
        "enum": [
          "alias",
          "ipset"
        ],
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/firewall/refs)。
