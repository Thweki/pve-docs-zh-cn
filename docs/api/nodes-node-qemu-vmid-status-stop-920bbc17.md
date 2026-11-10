# `/nodes/{node}/qemu/{vmid}/status/stop`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/stop`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/stop`

Stop virtual machine. The qemu process will exit immediately. This is akin to pulling the power plug of a running computer and may damage the VM data.

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
| `keepActive` | boolean | 否 | 0 | Do not deactivate storage volumes. |
| `migratedfrom` | string | 否 | — | The cluster node name. |
| `node` | string | 是 | — | The cluster node name. |
| `overrule-shutdown` | boolean | 否 | 0 | Try to abort active 'qmshutdown' tasks before stopping. |
| `skiplock` | boolean | 否 | — | Ignore locks - only root is allowed to use this option. |
| `timeout` | integer | 否 | — | Wait maximal timeout seconds. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "keepActive": {
      "default": 0,
      "description": "Do not deactivate storage volumes.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "migratedfrom": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "overrule-shutdown": {
      "default": 0,
      "description": "Try to abort active 'qmshutdown' tasks before stopping.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "skiplock": {
      "description": "Ignore locks - only root is allowed to use this option.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "timeout": {
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/stop)。
