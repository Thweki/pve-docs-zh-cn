# `/nodes/{node}/status`

原始接口路径：`/nodes/{node}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/status`

读取节点状态

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
| `node` | string | 是 | — | 集群节点名称。 |

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
      "description": "有关启动模式的元信息。",
      "properties": {
        "mode": {
          "description": "系统通过哪种固件启动。",
          "enum": [
            "efi",
            "legacy-bios"
          ],
          "type": "string"
        },
        "secureboot": {
          "description": "系统以安全模式启动，仅适用于 \"efi\" 模式。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "cpu": {
      "description": "当前 CPU 使用率。",
      "type": "number"
    },
    "cpuinfo": {
      "properties": {
        "cores": {
          "description": "CPU 的物理核心数量。",
          "type": "integer"
        },
        "cpus": {
          "description": "CPU 的逻辑线程数量。",
          "type": "integer"
        },
        "model": {
          "description": "CPU 型号",
          "type": "string"
        },
        "sockets": {
          "description": "CPU 的逻辑线程数量。",
          "type": "integer"
        }
      },
      "type": "object"
    },
    "current-kernel": {
      "description": "有关此节点当前启动的内核的元信息。",
      "properties": {
        "machine": {
          "description": "硬件（架构）类型",
          "type": "string"
        },
        "release": {
          "description": "操作系统内核发行版本（例如 \"6.8.0\"）",
          "type": "string"
        },
        "sysname": {
          "description": "操作系统内核名称（例如 \"Linux\"）",
          "type": "string"
        },
        "version": {
          "description": "包含构建信息的操作系统内核版本",
          "type": "string"
        }
      },
      "type": "object"
    },
    "loadavg": {
      "description": "分别为 1、5 和 15 分钟平均负载的数组。",
      "items": {
        "description": "负载值。",
        "type": "string"
      },
      "type": "array"
    },
    "memory": {
      "properties": {
        "available": {
          "description": "可用内存字节数。",
          "type": "integer"
        },
        "free": {
          "description": "空闲内存字节数。",
          "type": "integer"
        },
        "total": {
          "description": "总内存字节数。",
          "type": "integer"
        },
        "used": {
          "description": "已用内存字节数。",
          "type": "integer"
        }
      },
      "type": "object"
    },
    "pveversion": {
      "description": "PVE 版本字符串。",
      "type": "string"
    },
    "rootfs": {
      "properties": {
        "avail": {
          "description": "根文件系统中的可用字节数。",
          "type": "integer"
        },
        "free": {
          "description": "根文件系统上的空闲字节数。",
          "type": "integer"
        },
        "total": {
          "description": "根文件系统总大小，单位为字节。",
          "type": "integer"
        },
        "used": {
          "description": "根文件系统中的已用字节数。",
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

重启或关闭节点。

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
| `command` | string | 是 | — | 指定命令。；可选值：`reboot`, `shutdown` |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "command": {
      "description": "指定命令。",
      "enum": [
        "reboot",
        "shutdown"
      ],
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
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
