# `/nodes/{node}/qemu/{vmid}/migrate`

原始接口路径：`/nodes/{node}/qemu/{vmid}/migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/migrate`

获取迁移前提条件。

**方法标识：** `migrate_vm_precondition`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Migrate"
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
| `node` | string | 是 | — | 集群节点名称。 |
| `target` | string | 否 | — | 目标节点。 |
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
    "target": {
      "description": "目标节点。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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
  "properties": {
    "allowed_nodes": {
      "description": "允许迁移到的节点列表。",
      "items": {
        "description": "允许的节点",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "dependent-ha-resources": {
      "description": "由于与虚拟机具有正向亲和性，而将迁移到同一目标节点的 HA 资源。",
      "items": {
        "description": "与此虚拟机具有正向亲和性规则的 HA 资源的 '<ty>:<id>' 资源 ID。",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "has-dbus-vmstate": {
      "description": "虚拟机宿主机是否支持迁移附加虚拟机状态，例如 conntrack 条目。",
      "type": "boolean"
    },
    "local_disks": {
      "description": "列出本地磁盘，包括 CD-ROM、未使用及未被引用的磁盘",
      "items": {
        "properties": {
          "cdrom": {
            "description": "如果磁盘为 cdrom，则为 true。",
            "type": "boolean"
          },
          "is_unused": {
            "description": "如果磁盘未使用，则为 true。",
            "type": "boolean"
          },
          "size": {
            "description": "磁盘大小，单位为字节。",
            "type": "integer"
          },
          "volid": {
            "description": "磁盘的 volid。",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "local_resources": {
      "description": "列出阻止迁移的本地资源（例如 PCI、USB）。",
      "items": {
        "description": "本地资源",
        "type": "string"
      },
      "type": "array"
    },
    "mapped-resource-info": {
      "description": "映射资源对象，包含其是否支持在线迁移等附加信息。",
      "type": "object"
    },
    "mapped-resources": {
      "description": "映射资源列表，例如 PCI、USB。已弃用，请改用 'mapped-resource-info'。",
      "items": {
        "description": "映射资源",
        "type": "string"
      },
      "type": "array"
    },
    "not_allowed_nodes": {
      "description": "不允许迁移到的节点列表及附加信息。",
      "optional": 1,
      "properties": {
        "blocking-ha-resources": {
          "description": "阻止虚拟机迁移到该节点的 HA 资源。",
          "items": {
            "description": "阻塞迁移的 HA 资源",
            "properties": {
              "cause": {
                "description": "此 HA 资源阻塞迁移的原因。",
                "enum": [
                  "node-affinity",
                  "resource-affinity"
                ],
                "type": "string"
              },
              "sid": {
                "description": "阻塞迁移的 HA 资源 ID",
                "type": "string"
              }
            },
            "type": "object"
          },
          "optional": 1,
          "type": "array"
        },
        "unavailable_storages": {
          "description": "不可用存储列表。",
          "items": {
            "description": "存储",
            "type": "string"
          },
          "optional": 1,
          "type": "array"
        }
      },
      "type": "object"
    },
    "running": {
      "description": "确定虚拟机是否正在运行。",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/qemu/{vmid}/migrate`

迁移虚拟机。创建新的迁移任务。

**方法标识：** `migrate_vm`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Migrate"
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
| `bwlimit` | integer | 否 | "migrate limit from datacenter or storage config" | 覆盖 I/O 带宽限制（KiB/s）。 |
| `force` | boolean | 否 | — | 允许迁移使用本地设备的虚拟机。仅 root 可使用此选项。 |
| `migration_network` | string | 否 | — | 用于迁移的（子）网络的 CIDR。 |
| `migration_type` | string | 否 | — | 迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。；可选值：`secure`, `insecure` |
| `node` | string | 是 | — | 集群节点名称。 |
| `online` | boolean | 否 | — | 如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。 |
| `target` | string | 是 | — | 目标节点。 |
| `targetstorage` | string | 否 | — | 从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |
| `with-conntrack-state` | boolean | 否 | 0 | 是否为运行中的虚拟机迁移 conntrack 条目。 |
| `with-local-disks` | boolean | 否 | — | 为本地磁盘启用在线存储迁移 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "default": "migrate limit from datacenter or storage config",
      "description": "覆盖 I/O 带宽限制（KiB/s）。",
      "minimum": "0",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "force": {
      "description": "允许迁移使用本地设备的虚拟机。仅 root 可使用此选项。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "migration_network": {
      "description": "用于迁移的（子）网络的 CIDR。",
      "format": "CIDR",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "migration_type": {
      "description": "迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
      "enum": [
        "secure",
        "insecure"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "online": {
      "description": "如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "target": {
      "description": "目标节点。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "targetstorage": {
      "description": "从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。",
      "format": "storage-pair-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "with-conntrack-state": {
      "default": 0,
      "description": "是否为运行中的虚拟机迁移 conntrack 条目。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "with-local-disks": {
      "description": "为本地磁盘启用在线存储迁移",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "任务 ID。",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/migrate)。
