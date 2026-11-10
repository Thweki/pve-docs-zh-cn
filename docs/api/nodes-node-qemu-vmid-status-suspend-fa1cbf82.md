# `/nodes/{node}/qemu/{vmid}/status/suspend`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/suspend`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/suspend`

挂起虚拟机。

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
  "description": "需要对 /vms/{vmid} 具有 'VM.PowerMgmt' 权限；如果设置了 'todisk'，还需要对 /vms/{vmid} 具有 'VM.Config.Disk' 权限，以及对存放 vmstate 的存储具有 'Datastore.AllocateSpace' 权限。"
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
| `skiplock` | boolean | 否 | — | 忽略锁——仅 root 可使用此选项。 |
| `statestorage` | string | 否 | — | 存放虚拟机状态的存储 |
| `todisk` | boolean | 否 | 0 | 如果设置，则将虚拟机挂起到磁盘。下次启动虚拟机时将恢复。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

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
    "skiplock": {
      "description": "忽略锁——仅 root 可使用此选项。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "statestorage": {
      "description": "存放虚拟机状态的存储",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "requires": "todisk",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "todisk": {
      "default": 0,
      "description": "如果设置，则将虚拟机挂起到磁盘。下次启动虚拟机时将恢复。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
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
