# `/nodes/{node}/qemu/{vmid}/migrate`

原始接口路径：`/nodes/{node}/qemu/{vmid}/migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/migrate`

Get preconditions for migration.

**方法标识：** `migrate_vm_precondition`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Migrate"
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
| `target` | string | 否 | — | Target node. |
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
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "optional": 1,
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
  "properties": {
    "allowed_nodes": {
      "description": "List of nodes allowed for migration.",
      "items": {
        "description": "An allowed node",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "dependent-ha-resources": {
      "description": "HA resources, which will be migrated to the same target node as the VM, because these are in positive affinity with the VM.",
      "items": {
        "description": "The '<ty>:<id>' resource IDs of a HA resource with a positive affinity rule to this VM.",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "has-dbus-vmstate": {
      "description": "Whether the VM host supports migrating additional VM state, such as conntrack entries.",
      "type": "boolean"
    },
    "local_disks": {
      "description": "List local disks including CD-Rom, unused and not referenced disks",
      "items": {
        "properties": {
          "cdrom": {
            "description": "True if the disk is a cdrom.",
            "type": "boolean"
          },
          "is_unused": {
            "description": "True if the disk is unused.",
            "type": "boolean"
          },
          "size": {
            "description": "The size of the disk in bytes.",
            "type": "integer"
          },
          "volid": {
            "description": "The volid of the disk.",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "local_resources": {
      "description": "List local resources (e.g. pci, usb) that block migration.",
      "items": {
        "description": "A local resource",
        "type": "string"
      },
      "type": "array"
    },
    "mapped-resource-info": {
      "description": "Object of mapped resources with additional information such if they're live migratable.",
      "type": "object"
    },
    "mapped-resources": {
      "description": "List of mapped resources e.g. pci, usb. Deprecated, use 'mapped-resource-info' instead.",
      "items": {
        "description": "A mapped resource",
        "type": "string"
      },
      "type": "array"
    },
    "not_allowed_nodes": {
      "description": "List of not allowed nodes with additional information.",
      "optional": 1,
      "properties": {
        "blocking-ha-resources": {
          "description": "HA resources, which are blocking the VM from being migrated to the node.",
          "items": {
            "description": "A blocking HA resource",
            "properties": {
              "cause": {
                "description": "The reason why the HA resource is blocking the migration.",
                "enum": [
                  "node-affinity",
                  "resource-affinity"
                ],
                "type": "string"
              },
              "sid": {
                "description": "The blocking HA resource id",
                "type": "string"
              }
            },
            "type": "object"
          },
          "optional": 1,
          "type": "array"
        },
        "unavailable_storages": {
          "description": "A list of not available storages.",
          "items": {
            "description": "A storage",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        }
      },
      "type": "object"
    },
    "running": {
      "description": "Determines if the VM is running.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/qemu/{vmid}/migrate`

Migrate virtual machine. Creates a new migration task.

**方法标识：** `migrate_vm`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Migrate"
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
| `bwlimit` | integer | 否 | "migrate limit from datacenter or storage config" | Override I/O bandwidth limit (in KiB/s). |
| `force` | boolean | 否 | — | Allow to migrate VMs which use local devices. Only root may use this option. |
| `migration_network` | string | 否 | — | CIDR of the (sub) network that is used for migration. |
| `migration_type` | string | 否 | — | Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance.；可选值：`secure`, `insecure` |
| `node` | string | 是 | — | The cluster node name. |
| `online` | boolean | 否 | — | Use online/live migration if VM is running. Ignored if VM is stopped. |
| `target` | string | 是 | — | Target node. |
| `targetstorage` | string | 否 | — | Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |
| `with-conntrack-state` | boolean | 否 | 0 | Whether to migrate conntrack entries for running VMs. |
| `with-local-disks` | boolean | 否 | — | Enable live storage migration for local disk |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "default": "migrate limit from datacenter or storage config",
      "description": "Override I/O bandwidth limit (in KiB/s).",
      "minimum": "0",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "force": {
      "description": "Allow to migrate VMs which use local devices. Only root may use this option.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "migration_network": {
      "description": "CIDR of the (sub) network that is used for migration.",
      "format": "CIDR",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "migration_type": {
      "description": "Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance.",
      "enum": [
        "secure",
        "insecure"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "online": {
      "description": "Use online/live migration if VM is running. Ignored if VM is stopped.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "targetstorage": {
      "description": "Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself.",
      "format": "storage-pair-list",
      "optional": 1,
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
    },
    "with-conntrack-state": {
      "default": 0,
      "description": "Whether to migrate conntrack entries for running VMs.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "with-local-disks": {
      "description": "Enable live storage migration for local disk",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "the task ID.",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/migrate)。
