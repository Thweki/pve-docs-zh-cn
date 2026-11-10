# `/nodes/{node}/storage/{storage}/import-metadata`

原始接口路径：`/nodes/{node}/storage/{storage}/import-metadata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/import-metadata`

获取创建客户机的基本参数，该客户机从外部可导入客户机（例如 ESXi 虚拟机）导入数据

**方法标识：** `get_import_metadata`

**权限**

```json
{
  "description": "需要具有卷的读取访问权限。",
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
| `storage` | string | 是 | — | 存储标识符。 |
| `volume` | string | 是 | — | 客户机归档/条目的卷标识符。 |

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
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "客户机归档/条目的卷标识符。",
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
  "additionalProperties": 0,
  "description": "有关如何导入客户机的信息。",
  "properties": {
    "create-args": {
      "additionalProperties": 1,
      "description": "可用于创建虚拟机或容器调用的参数。",
      "type": "object"
    },
    "disks": {
      "additionalProperties": 1,
      "description": "识别的磁盘卷，形式为 `$bus$id` => `$storeid:$path` 映射。",
      "optional": 1,
      "type": "object"
    },
    "net": {
      "additionalProperties": 1,
      "description": "识别的网络接口，形式为 `net$id` => { ...params } 对象。",
      "optional": 1,
      "type": "object"
    },
    "source": {
      "description": "此客户机卷的导入源类型。",
      "enum": [
        "esxi"
      ],
      "type": "string"
    },
    "type": {
      "description": "将生成的客户机类型。",
      "enum": [
        "vm"
      ],
      "type": "string"
    },
    "warnings": {
      "description": "可能影响客户机导入的已知问题列表。注意，没有警告并不表示不会出现问题。",
      "items": {
        "additionalProperties": 1,
        "properties": {
          "key": {
            "description": "警告相关主题的（配置）键。",
            "optional": 1,
            "type": "string"
          },
          "type": {
            "description": "此警告的内容。",
            "enum": [
              "cdrom-image-ignored",
              "efi-state-lost",
              "guest-is-running",
              "nvme-unsupported",
              "ova-needs-extracting",
              "ovmf-with-lsi-unsupported",
              "serial-port-socket-only"
            ],
            "type": "string"
          },
          "value": {
            "description": "警告相关主题的（配置）值。",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
      },
      "optional": 1,
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/import-metadata)。
