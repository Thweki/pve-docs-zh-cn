# `/nodes/{node}/status`

原始接口路径：`/nodes/{node}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/status`

Read node status

**方法标识：** `status`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Audit"
    ]
  ]
}
```

**允许 API 令牌**

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
    }
  }
}
```

</details>

### 返回值

```json
{
  "additionalProperties": 1,
  "properties": {
    "boot-info": {
      "description": "Meta-information about the boot mode.",
      "properties": {
        "mode": {
          "description": "Through which firmware the system got booted.",
          "enum": [
            "efi",
            "legacy-bios"
          ],
          "type": "string"
        },
        "secureboot": {
          "description": "System is booted in secure mode, only applicable for the \"efi\" mode.",
          "optional": 1,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "cpu": {
      "description": "The current cpu usage.",
      "type": "number"
    },
    "cpuinfo": {
      "properties": {
        "cores": {
          "description": "The number of physical cores of the CPU.",
          "type": "integer"
        },
        "cpus": {
          "description": "The number of logical threads of the CPU.",
          "type": "integer"
        },
        "model": {
          "description": "The CPU model",
          "type": "string"
        },
        "sockets": {
          "description": "The number of logical threads of the CPU.",
          "type": "integer"
        }
      },
      "type": "object"
    },
    "current-kernel": {
      "description": "Meta-information about the currently booted kernel of this node.",
      "properties": {
        "machine": {
          "description": "Hardware (architecture) type",
          "type": "string"
        },
        "release": {
          "description": "OS kernel release (e.g., \"6.8.0\")",
          "type": "string"
        },
        "sysname": {
          "description": "OS kernel name (e.g., \"Linux\")",
          "type": "string"
        },
        "version": {
          "description": "OS kernel version with build info",
          "type": "string"
        }
      },
      "type": "object"
    },
    "loadavg": {
      "description": "An array of load avg for 1, 5 and 15 minutes respectively.",
      "items": {
        "description": "The value of the load.",
        "type": "string"
      },
      "type": "array"
    },
    "memory": {
      "properties": {
        "available": {
          "description": "The available memory in bytes.",
          "type": "integer"
        },
        "free": {
          "description": "The free memory in bytes.",
          "type": "integer"
        },
        "total": {
          "description": "The total memory in bytes.",
          "type": "integer"
        },
        "used": {
          "description": "The used memory in bytes.",
          "type": "integer"
        }
      },
      "type": "object"
    },
    "pveversion": {
      "description": "The PVE version string.",
      "type": "string"
    },
    "rootfs": {
      "properties": {
        "avail": {
          "description": "The available bytes in the root filesystem.",
          "type": "integer"
        },
        "free": {
          "description": "The free bytes on the root filesystem.",
          "type": "integer"
        },
        "total": {
          "description": "The total size of the root filesystem in bytes.",
          "type": "integer"
        },
        "used": {
          "description": "The used bytes in the root filesystem.",
          "type": "integer"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/status`

Reboot or shutdown a node.

**方法标识：** `node_cmd`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.PowerMgmt"
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
| `command` | string | 是 | — | Specify the command.；可选值：`reboot`, `shutdown` |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "command": {
      "description": "Specify the command.",
      "enum": [
        "reboot",
        "shutdown"
      ],
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/status)。
