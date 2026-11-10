# `/nodes/{node}/lxc/{vmid}/migrate`

原始接口路径：`/nodes/{node}/lxc/{vmid}/migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/migrate`

Get preconditions for migration.

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
| `node` | string | 是 | — | The cluster node name. |
| `target` | string | 否 | — | Target node. |
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
    "target": {
      "description": "Target node.",
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
  "properties": {
    "allowed-nodes": {
      "description": "List of nodes allowed for migration.",
      "items": {
        "description": "An allowed node",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "dependent-ha-resources": {
      "description": "HA resources, which will be migrated to the same target node as the VM, because these are in positive affinity with the VM.",
      "items": {
        "description": "The '<ty>:<id>' resource IDs of a HA resource with a positive affinity rule to this CT.",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "not-allowed-nodes": {
      "description": "List of not allowed nodes with additional information.",
      "optional": 1,
      "properties": {
        "blocking-ha-resources": {
          "description": "HA resources, which are blocking the container from being migrated to the node.",
          "items": {
            "description": "A blocking HA resource",
            "properties": {
              "cause": {
                "description": "The reason why the HA resource is blocking the migration.",
                "enum": [
                  "node-affinity",
                  "resource-affinity"
                ],
                "type": "string"
              },
              "sid": {
                "description": "The blocking HA resource id",
                "type": "string"
              }
            },
            "type": "object"
          },
          "optional": 1,
          "type": "array"
        }
      },
      "type": "object"
    },
    "running": {
      "description": "Determines if the container is running.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/lxc/{vmid}/migrate`

将容器迁移到另一个节点。创建新的迁移任务。

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
| `bwlimit` | number | 否 | "migrate limit from datacenter or storage config" | Override I/O bandwidth limit (in KiB/s). |
| `node` | string | 是 | — | The cluster node name. |
| `online` | boolean | 否 | — | Use online/live migration. |
| `restart` | boolean | 否 | — | Use restart migration |
| `target` | string | 是 | — | Target node. |
| `target-storage` | string | 否 | — | Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself. |
| `timeout` | integer | 否 | 180 | Timeout in seconds for shutdown for restart migration |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "default": "migrate limit from datacenter or storage config",
      "description": "Override I/O bandwidth limit (in KiB/s).",
      "minimum": "0",
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - N)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "online": {
      "description": "Use online/live migration.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "restart": {
      "description": "Use restart migration",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "target-storage": {
      "description": "Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself.",
      "format": "storage-pair-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": 180,
      "description": "Timeout in seconds for shutdown for restart migration",
      "optional": 1,
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
  "description": "the task ID.",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/migrate)。
