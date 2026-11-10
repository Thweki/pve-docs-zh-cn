# `/nodes/{node}/storage/{storage}/import-metadata`

原始接口路径：`/nodes/{node}/storage/{storage}/import-metadata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/import-metadata`

Get the base parameters for creating a guest which imports data from a foreign importable guest, like an ESXi VM

**权限**

```json
{
  "description": "You need read access for the volume.",
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
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 是 | — | The storage identifier. |
| `volume` | string | 是 | — | Volume identifier for the guest archive/entry. |

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
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "Volume identifier for the guest archive/entry.",
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
  "description": "Information about how to import a guest.",
  "properties": {
    "create-args": {
      "additionalProperties": 1,
      "description": "Parameters which can be used in a call to create a VM or container.",
      "type": "object"
    },
    "disks": {
      "additionalProperties": 1,
      "description": "Recognised disk volumes as `$bus$id` => `$storeid:$path` map.",
      "optional": 1,
      "type": "object"
    },
    "net": {
      "additionalProperties": 1,
      "description": "Recognised network interfaces as `net$id` => { ...params } object.",
      "optional": 1,
      "type": "object"
    },
    "source": {
      "description": "The type of the import-source of this guest volume.",
      "enum": [
        "esxi"
      ],
      "type": "string"
    },
    "type": {
      "description": "The type of guest this is going to produce.",
      "enum": [
        "vm"
      ],
      "type": "string"
    },
    "warnings": {
      "description": "List of known issues that can affect the import of a guest. Note that lack of warning does not imply that there cannot be any problems.",
      "items": {
        "additionalProperties": 1,
        "properties": {
          "key": {
            "description": "Related subject (config) key of warning.",
            "optional": 1,
            "type": "string"
          },
          "type": {
            "description": "What this warning is about.",
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
            "description": "Related subject (config) value of warning.",
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
