# `/nodes/{node}/lxc/{vmid}/migrate`

原始接口路径：`/nodes/{node}/lxc/{vmid}/migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/migrate`

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
    "allowed-nodes": {
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
        "description": "与此容器具有正向亲和性规则的 HA 资源的 '<ty>:<id>' 资源 ID。",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "not-allowed-nodes": {
      "description": "不允许迁移到的节点列表及附加信息。",
      "optional": 1,
      "properties": {
        "blocking-ha-resources": {
          "description": "阻止容器迁移到该节点的 HA 资源。",
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
        }
      },
      "type": "object"
    },
    "running": {
      "description": "确定容器是否正在运行。",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/lxc/{vmid}/migrate`

将容器迁移到另一个节点。创建新的迁移任务。

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
| `bwlimit` | number | 否 | "migrate limit from datacenter or storage config" | 覆盖 I/O 带宽限制（KiB/s）。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `online` | boolean | 否 | — | 使用在线迁移。 |
| `restart` | boolean | 否 | — | 使用重启迁移 |
| `target` | string | 是 | — | 目标节点。 |
| `target-storage` | string | 否 | — | 从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。 |
| `timeout` | integer | 否 | 180 | 重启迁移的关闭超时时间，单位为秒 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

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
      "type": "number",
      "typetext": "<number> (0 - N)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "online": {
      "description": "使用在线迁移。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "restart": {
      "description": "使用重启迁移",
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
    "target-storage": {
      "description": "从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。",
      "format": "storage-pair-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": 180,
      "description": "重启迁移的关闭超时时间，单位为秒",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
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
  "description": "任务 ID。",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/migrate)。
