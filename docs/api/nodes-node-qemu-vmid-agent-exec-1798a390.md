# `/nodes/{node}/qemu/{vmid}/agent/exec`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/exec`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/agent/exec`

Executes the given command in the vm via the guest-agent and returns an object with the pid.

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
| `command` | array | 是 | — | The command as a list of program + arguments. |
| `input-data` | string | 否 | — | Data to pass as 'input-data' to the guest. Usually treated as STDIN to 'command'. |
| `node` | string | 是 | — | The cluster node name. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "command": {
      "description": "The command as a list of program + arguments.",
      "items": {
        "description": "A single part of the program + arguments.",
        "type": "string"
      },
      "type": "array",
      "typetext": "<array>"
    },
    "input-data": {
      "description": "Data to pass as 'input-data' to the guest. Usually treated as STDIN to 'command'.",
      "maxLength": 65536,
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
    "pid": {
      "description": "The PID of the process started by the guest-agent.",
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/exec)。
