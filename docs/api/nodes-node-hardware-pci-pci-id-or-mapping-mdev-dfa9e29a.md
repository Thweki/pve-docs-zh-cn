# `/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev`

原始接口路径：`/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev`

List mediated device types for given PCI device.

**方法标识：** `mdevscan`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Sys.Modify"
    ],
    "any",
    1
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
| `pci-id-or-mapping` | string | 是 | — | The PCI ID or mapping to list the mdev types for. |

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
    "pci-id-or-mapping": {
      "description": "The PCI ID or mapping to list the mdev types for.",
      "pattern": "(?:(?:[0-9a-fA-F]{4}:)?[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\\.[0-9a-fA-F])|([a-zA-Z][a-zA-Z0-9_-]+)",
      "type": "string"
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
      "available": {
        "description": "The number of still available instances of this type.",
        "type": "integer"
      },
      "description": {
        "description": "Additional description of the type.",
        "type": "string"
      },
      "name": {
        "description": "A human readable name for the type.",
        "optional": 1,
        "type": "string"
      },
      "type": {
        "description": "The name of the mdev type.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev)。
