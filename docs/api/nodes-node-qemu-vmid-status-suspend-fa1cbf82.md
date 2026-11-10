# `/nodes/{node}/qemu/{vmid}/status/suspend`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/suspend`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/suspend`

Suspend virtual machine.

**方法标识：** `vm_suspend`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.PowerMgmt"
    ]
  ],
  "description": "You need 'VM.PowerMgmt' on /vms/{vmid}, and if you have set 'todisk', you need also 'VM.Config.Disk' on /vms/{vmid} and 'Datastore.AllocateSpace' on the storage for the vmstate."
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
| `skiplock` | boolean | 否 | — | Ignore locks - only root is allowed to use this option. |
| `statestorage` | string | 否 | — | The storage for the VM state |
| `todisk` | boolean | 否 | 0 | If set, suspends the VM to disk. Will be resumed on next VM start. |
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
    "skiplock": {
      "description": "Ignore locks - only root is allowed to use this option.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "statestorage": {
      "description": "The storage for the VM state",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "requires": "todisk",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "todisk": {
      "default": 0,
      "description": "If set, suspends the VM to disk. Will be resumed on next VM start.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/suspend)。
