# `/nodes/{node}/qemu/{vmid}/status/start`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/start`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/start`

Start virtual machine.

**方法标识：** `vm_start`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.PowerMgmt"
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
| `force-cpu` | string | 否 | — | Override QEMU's -cpu argument with the given string. |
| `machine` | string | 否 | — | Specify the QEMU machine. |
| `migratedfrom` | string | 否 | — | The cluster node name. |
| `migration_network` | string | 否 | — | CIDR of the (sub) network that is used for migration. |
| `migration_type` | string | 否 | — | Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance.；可选值：`secure`, `insecure` |
| `nets-host-mtu` | string | 否 | — | Used for migration compat. List of VirtIO network devices and their effective host_mtu setting according to the QEMU object model on the source side of the migration. A value of 0 means that the host_mtu parameter is to be avoided for the corresponding device. |
| `node` | string | 是 | — | The cluster node name. |
| `skiplock` | boolean | 否 | — | Ignore locks - only root is allowed to use this option. |
| `stateuri` | string | 否 | — | Some command save/restore state from this location. |
| `targetstorage` | string | 否 | — | Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself. |
| `timeout` | integer | 否 | "max(30, vm memory in GiB)" | Wait maximal timeout seconds. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |
| `with-conntrack-state` | boolean | 否 | 0 | Whether to migrate conntrack entries for running VMs. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force-cpu": {
      "description": "Override QEMU's -cpu argument with the given string.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "machine": {
      "description": "Specify the QEMU machine.",
      "format": {
        "aw-bits": {
          "description": "Specifies the vIOMMU address space bit width.",
          "maximum": 64,
          "minimum": 32,
          "optional": 1,
          "type": "number",
          "verbose_description": "Specifies the vIOMMU address space bit width.\n\nIntel vIOMMU supports a bit width of either 39 or 48 bits and VirtIO vIOMMU supports any bit width between 32 and 64 bits."
        },
        "enable-s3": {
          "description": "Enables S3 power state. Defaults to false beginning with machine types 9.2+pve1, true before.",
          "optional": 1,
          "type": "boolean"
        },
        "enable-s4": {
          "description": "Enables S4 power state. Defaults to false beginning with machine types 9.2+pve1, true before.",
          "optional": 1,
          "type": "boolean"
        },
        "type": {
          "default_key": 1,
          "description": "Specifies the QEMU machine type.",
          "format_description": "machine type",
          "maxLength": 40,
          "optional": 1,
          "pattern": "(pc|pc(-i440fx)?-\\d+(\\.\\d+)+(\\+pve\\d+)?(\\.pxe)?|q35|pc-q35-\\d+(\\.\\d+)+(\\+pve\\d+)?(\\.pxe)?|virt(?:-\\d+(\\.\\d+)+)?(\\+pve\\d+)?)",
          "type": "string"
        },
        "viommu": {
          "description": "Enable and set guest vIOMMU variant (Intel vIOMMU needs q35 to be set as machine type).",
          "enum": [
            "intel",
            "virtio"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]"
    },
    "migratedfrom": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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
    "nets-host-mtu": {
      "description": "Used for migration compat. List of VirtIO network devices and their effective host_mtu setting according to the QEMU object model on the source side of the migration. A value of 0 means that the host_mtu parameter is to be avoided for the corresponding device.",
      "optional": 1,
      "pattern": "net\\d+=\\d+(,net\\d+=\\d+)*",
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "skiplock": {
      "description": "Ignore locks - only root is allowed to use this option.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stateuri": {
      "description": "Some command save/restore state from this location.",
      "maxLength": 128,
      "optional": 1,
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
    "timeout": {
      "default": "max(30, vm memory in GiB)",
      "description": "Wait maximal timeout seconds.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
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
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/start)。
