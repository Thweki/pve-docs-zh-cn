# `/cluster/mapping/pci/{id}`

原始接口路径：`/cluster/mapping/pci/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/mapping/pci/{id}`

Remove Hardware Mapping.

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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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
  "type": "null"
}
```

## GET `/cluster/mapping/pci/{id}`

Get PCI Mapping.

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/pci/{id}",
      [
        "Mapping.Use"
      ]
    ],
    [
      "perm",
      "/mapping/pci/{id}",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "perm",
      "/mapping/pci/{id}",
      [
        "Mapping.Audit"
      ]
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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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
  "type": "object"
}
```

## PUT `/cluster/mapping/pci/{id}`

Update a hardware mapping.

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/pci/{id}",
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
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `description` | string | 否 | — | Description of the logical PCI device. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `id` | string | 是 | — | The ID of the logical PCI mapping. |
| `live-migration-capable` | boolean | 否 | 0 | Marks the device(s) as being able to be live-migrated (Experimental). This needs hardware and driver support to work. |
| `map` | array | 否 | — | A list of maps for the cluster nodes. |
| `mdev` | boolean | 否 | 0 | Marks the device(s) as being capable of providing mediated devices. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "Description of the logical PCI device.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
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
      "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/pci/{id})。
