# `/cluster/mapping/pci`

原始接口路径：`/cluster/mapping/pci`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/mapping/pci`

List PCI Hardware Mapping

**方法标识：** `index`

**权限**

```json
{
  "description": "Only lists entries where you have 'Mapping.Modify', 'Mapping.Use' or 'Mapping.Audit' permissions on '/mapping/pci/<id>'.",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `check-node` | string | 否 | — | If given, checks the configurations on the given node for correctness, and adds relevant diagnostics for the devices to the response. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "If given, checks the configurations on the given node for correctness, and adds relevant diagnostics for the devices to the response.",
      "format": "pve-node",
      "optional": 1,
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
    "properties": {
      "checks": {
        "description": "A list of checks, only present if 'check_node' is set.",
        "items": {
          "properties": {
            "message": {
              "description": "The message of the error",
              "type": "string"
            },
            "severity": {
              "description": "The severity of the error",
              "enum": [
                "warning",
                "error"
              ],
              "type": "string"
            }
          },
          "type": "object"
        },
        "optional": 1,
        "type": "array"
      },
      "description": {
        "description": "A description of the logical mapping.",
        "type": "string"
      },
      "id": {
        "description": "The logical ID of the mapping.",
        "type": "string"
      },
      "map": {
        "description": "The entries of the mapping.",
        "items": {
          "description": "A mapping for a node.",
          "type": "string"
        },
        "type": "array"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/mapping/pci`

Create a new hardware mapping.

**方法标识：** `create`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/pci",
    [
      "Mapping.Modify"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `description` | string | 否 | — | Description of the logical PCI device. |
| `id` | string | 是 | — | The ID of the logical PCI mapping. |
| `live-migration-capable` | boolean | 否 | 0 | Marks the device(s) as being able to be live-migrated (Experimental). This needs hardware and driver support to work. |
| `map` | array | 是 | — | A list of maps for the cluster nodes. |
| `mdev` | boolean | 否 | 0 | Marks the device(s) as being capable of providing mediated devices. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "Description of the logical PCI device.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "id": {
      "description": "The ID of the logical PCI mapping.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "live-migration-capable": {
      "default": 0,
      "description": "Marks the device(s) as being able to be live-migrated (Experimental). This needs hardware and driver support to work.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "map": {
      "description": "A list of maps for the cluster nodes.",
      "items": {
        "format": {
          "description": {
            "description": "Description of the node specific device.",
            "maxLength": 4096,
            "optional": 1,
            "type": "string"
          },
          "id": {
            "description": "The vendor and device ID that is expected. Used for detecting hardware changes",
            "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          },
          "iommugroup": {
            "description": "The IOMMU group in which the device is to be expected in. Used for detecting hardware changes.",
            "optional": 1,
            "type": "integer"
          },
          "node": {
            "description": "The cluster node name.",
            "format": "pve-node",
            "type": "string"
          },
          "path": {
            "description": "The path to the device. If the function is omitted, the whole device is mapped. In that case use the attributes of the first device. You can give multiple paths as a semicolon separated list, the first available will then be chosen on guest start.",
            "pattern": "(?:[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?;)*[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?",
            "type": "string"
          },
          "subsystem-id": {
            "description": "The subsystem vendor and device ID that is expected. Used for detecting hardware changes.",
            "optional": 1,
            "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 0,
      "type": "array",
      "typetext": "<array>"
    },
    "mdev": {
      "default": 0,
      "description": "Marks the device(s) as being capable of providing mediated devices.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/pci)。
