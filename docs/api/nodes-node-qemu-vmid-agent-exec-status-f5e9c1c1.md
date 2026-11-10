# `/nodes/{node}/qemu/{vmid}/agent/exec-status`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/exec-status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/agent/exec-status`

Gets the status of the given pid started by the guest-agent

**方法标识：** `exec-status`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.GuestAgent.Unrestricted"
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
| `pid` | integer | 是 | — | The PID to query |
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
    "pid": {
      "description": "The PID to query",
      "type": "integer",
      "typetext": "<integer>"
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
    "err-data": {
      "description": "stderr of the process",
      "optional": 1,
      "type": "string"
    },
    "err-truncated": {
      "description": "true if stderr was not fully captured",
      "optional": 1,
      "type": "boolean"
    },
    "exitcode": {
      "description": "process exit code if it was normally terminated.",
      "optional": 1,
      "type": "integer"
    },
    "exited": {
      "description": "Tells if the given command has exited yet.",
      "type": "boolean"
    },
    "out-data": {
      "description": "stdout of the process",
      "optional": 1,
      "type": "string"
    },
    "out-truncated": {
      "description": "true if stdout was not fully captured",
      "optional": 1,
      "type": "boolean"
    },
    "signal": {
      "description": "signal number or exception code if the process was abnormally terminated.",
      "optional": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/exec-status)。
