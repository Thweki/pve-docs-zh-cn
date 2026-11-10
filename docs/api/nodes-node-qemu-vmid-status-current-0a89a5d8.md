# `/nodes/{node}/qemu/{vmid}/status/current`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/current`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/status/current`

Get virtual machine status.

**方法标识：** `vm_status`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
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
    "agent": {
      "description": "QEMU Guest Agent is enabled in config.",
      "optional": 1,
      "type": "boolean"
    },
    "clipboard": {
      "description": "Enable a specific clipboard. If not set, depending on the display type the SPICE one will be added.",
      "enum": [
        "vnc"
      ],
      "optional": 1,
      "type": "string"
    },
    "cpu": {
      "description": "Current CPU usage.",
      "optional": 1,
      "type": "number"
    },
    "cpus": {
      "description": "Maximum usable CPUs.",
      "optional": 1,
      "type": "number"
    },
    "diskread": {
      "description": "The amount of bytes the guest read from it's block devices since the guest was started. (Note: This info is not available for all storage types.)",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "diskwrite": {
      "description": "The amount of bytes the guest wrote from it's block devices since the guest was started. (Note: This info is not available for all storage types.)",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "ha": {
      "description": "HA manager service status.",
      "type": "object"
    },
    "lock": {
      "description": "The current config lock, if any.",
      "optional": 1,
      "type": "string"
    },
    "maxdisk": {
      "description": "Root disk size in bytes.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "maxmem": {
      "description": "Maximum memory in bytes.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "mem": {
      "description": "Currently used memory in bytes. Does not take into account kernel same-page merging (KSM). Uses information from ballooning when available.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "memhost": {
      "description": "Current memory usage on the host. Does not take into account kernel same-page merging (KSM).",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "name": {
      "description": "VM (host)name.",
      "optional": 1,
      "type": "string"
    },
    "netin": {
      "description": "The amount of traffic in bytes that was sent to the guest over the network since it was started.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "netout": {
      "description": "The amount of traffic in bytes that was sent from the guest over the network since it was started.",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "pid": {
      "description": "PID of the QEMU process, if the VM is running.",
      "optional": 1,
      "type": "integer"
    },
    "pressurecpufull": {
      "description": "CPU Full pressure stall average over the last 10 seconds.",
      "optional": 1,
      "type": "number"
    },
    "pressurecpusome": {
      "description": "CPU Some pressure stall average over the last 10 seconds.",
      "optional": 1,
      "type": "number"
    },
    "pressureiofull": {
      "description": "IO Full pressure stall average over the last 10 seconds.",
      "optional": 1,
      "type": "number"
    },
    "pressureiosome": {
      "description": "IO Some pressure stall average over the last 10 seconds.",
      "optional": 1,
      "type": "number"
    },
    "pressurememoryfull": {
      "description": "Memory Full pressure stall average over the last 10 seconds.",
      "optional": 1,
      "type": "number"
    },
    "pressurememorysome": {
      "description": "Memory Some pressure stall average over the last 10 seconds.",
      "optional": 1,
      "type": "number"
    },
    "qmpstatus": {
      "description": "VM run state from the 'query-status' QMP monitor command.",
      "optional": 1,
      "type": "string"
    },
    "running-machine": {
      "description": "The currently running machine type (if running).",
      "optional": 1,
      "type": "string"
    },
    "running-qemu": {
      "description": "The QEMU version the VM is currently using (if running).",
      "optional": 1,
      "type": "string"
    },
    "serial": {
      "description": "Guest has serial device configured.",
      "optional": 1,
      "type": "boolean"
    },
    "spice": {
      "description": "QEMU VGA configuration supports spice.",
      "optional": 1,
      "type": "boolean"
    },
    "status": {
      "description": "QEMU process status.",
      "enum": [
        "stopped",
        "running"
      ],
      "type": "string"
    },
    "tags": {
      "description": "The current configured tags, if any",
      "optional": 1,
      "type": "string"
    },
    "template": {
      "default": 0,
      "description": "Determines if the guest is a template.",
      "optional": 1,
      "type": "boolean"
    },
    "uptime": {
      "description": "Uptime in seconds.",
      "optional": 1,
      "renderer": "duration",
      "type": "integer"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/current)。
