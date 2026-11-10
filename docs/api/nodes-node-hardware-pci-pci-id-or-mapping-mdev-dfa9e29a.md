# `/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev`

原始接口路径：`/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev`

列出给定 PCI 设备的中介设备类型。

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
| `node` | string | 是 | — | 集群节点名称。 |
| `pci-id-or-mapping` | string | 是 | — | 要列出其 mdev 类型的 PCI ID 或映射。 |

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
    "pci-id-or-mapping": {
      "description": "要列出其 mdev 类型的 PCI ID 或映射。",
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
        "description": "此类型仍可用的实例数量。",
        "type": "integer"
      },
      "description": {
        "description": "类型的附加描述。",
        "type": "string"
      },
      "name": {
        "description": "类型的人类可读名称。",
        "optional": 1,
        "type": "string"
      },
      "type": {
        "description": "mdev 类型名称。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/hardware/pci/{pci-id-or-mapping}/mdev)。
