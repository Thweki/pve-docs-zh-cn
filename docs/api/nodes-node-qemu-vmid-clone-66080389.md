# `/nodes/{node}/qemu/{vmid}/clone`

原始接口路径：`/nodes/{node}/qemu/{vmid}/clone`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/clone`

Create a copy of virtual machine/template.

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/vms/{vmid}",
      [
        "VM.Clone"
      ]
    ],
    [
      "or",
      [
        "perm",
        "/vms/{newid}",
        [
          "VM.Allocate"
        ]
      ],
      [
        "perm",
        "/pool/{pool}",
        [
          "VM.Allocate"
        ],
        "require_param",
        "pool"
      ]
    ]
  ],
  "description": "You need 'VM.Clone' permissions on /vms/{vmid}, and 'VM.Allocate' permissions on /vms/{newid} (or on the VM pool /pool/{pool}). You also need 'Datastore.AllocateSpace' on any used storage and 'SDN.Use' on any used bridge/vnet"
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
| `bwlimit` | integer | 否 | "clone limit from datacenter or storage config" | Override I/O bandwidth limit (in KiB/s). |
| `description` | string | 否 | — | Description for the new VM. |
| `format` | string | 否 | — | Target disk format. Only valid for full clone. If the target storage does not support the format, the storage's default format is used instead.；可选值：`raw`, `qcow2`, `vmdk` |
| `full` | boolean | 否 | — | Create a full copy of all disks. This is always done when you clone a normal VM. For VM templates, we try to create a linked clone by default. |
| `name` | string | 否 | — | Set a name for the new VM. |
| `newid` | integer | 是 | — | VMID for the clone. |
| `node` | string | 是 | — | The cluster node name. |
| `pool` | string | 否 | — | Add the new VM to the specified pool. |
| `snapname` | string | 否 | — | The name of the snapshot. |
| `storage` | string | 否 | — | Target storage for full clone. |
| `target` | string | 否 | — | Target node. Only allowed if the original VM is on shared storage. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "default": "clone limit from datacenter or storage config",
      "description": "Override I/O bandwidth limit (in KiB/s).",
      "minimum": "0",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "description": {
      "description": "Description for the new VM.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "format": {
      "description": "Target disk format. Only valid for full clone. If the target storage does not support the format, the storage's default format is used instead.",
      "enum": [
        "raw",
        "qcow2",
        "vmdk"
      ],
      "optional": 1,
      "type": "string"
    },
    "full": {
      "description": "Create a full copy of all disks. This is always done when you clone a normal VM. For VM templates, we try to create a linked clone by default.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "Set a name for the new VM.",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "newid": {
      "description": "VMID for the clone.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pool": {
      "description": "Add the new VM to the specified pool.",
      "format": "pve-poolid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "snapname": {
      "description": "The name of the snapshot.",
      "format": "pve-configid",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "Target storage for full clone.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "target": {
      "description": "Target node. Only allowed if the original VM is on shared storage.",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/clone)。
