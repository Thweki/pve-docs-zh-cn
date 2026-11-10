# `/nodes/{node}/lxc/{vmid}/clone`

原始接口路径：`/nodes/{node}/lxc/{vmid}/clone`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/lxc/{vmid}/clone`

创建容器克隆/副本

**方法标识：** `clone_vm`

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
  "description": "You need 'VM.Clone' permissions on /vms/{vmid}, and 'VM.Allocate' permissions on /vms/{newid} (or on the VM pool /pool/{pool}). You also need 'Datastore.AllocateSpace' on any used storage, and 'SDN.Use' on any bridge."
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
| `bwlimit` | number | 否 | "clone limit from datacenter or storage config" | Override I/O bandwidth limit (in KiB/s). |
| `description` | string | 否 | — | Description for the new CT. |
| `full` | boolean | 否 | — | Create a full copy of all disks. This is always done when you clone a normal CT. For CT templates, we try to create a linked clone by default. |
| `hostname` | string | 否 | — | Set a hostname for the new CT. |
| `newid` | integer | 是 | — | VMID for the clone. |
| `node` | string | 是 | — | The cluster node name. |
| `pool` | string | 否 | — | Add the new CT to the specified pool. |
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
      "type": "number",
      "typetext": "<number> (0 - N)"
    },
    "description": {
      "description": "Description for the new CT.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "full": {
      "description": "Create a full copy of all disks. This is always done when you clone a normal CT. For CT templates, we try to create a linked clone by default.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hostname": {
      "description": "Set a hostname for the new CT.",
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
      "description": "Add the new CT to the specified pool.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/clone)。
