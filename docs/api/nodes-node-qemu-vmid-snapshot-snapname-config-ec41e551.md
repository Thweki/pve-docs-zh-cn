# `/nodes/{node}/qemu/{vmid}/snapshot/{snapname}/config`

原始接口路径：`/nodes/{node}/qemu/{vmid}/snapshot/{snapname}/config`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/snapshot/{snapname}/config`

获取快照配置

**方法标识：** `get_snapshot_config`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Snapshot",
      "VM.Snapshot.Rollback",
      "VM.Audit"
    ],
    "any",
    1
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
| `snapname` | string | 是 | — | 快照名称。 |
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
    "snapname": {
      "description": "快照名称。",
      "format": "pve-configid",
      "maxLength": 40,
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
  "type": "object"
}
```

## PUT `/nodes/{node}/qemu/{vmid}/snapshot/{snapname}/config`

更新快照元数据。

**方法标识：** `update_snapshot_config`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Snapshot"
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
| `description` | string | 否 | — | 文本描述或注释。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `snapname` | string | 是 | — | 快照名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "文本描述或注释。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "snapname": {
      "description": "快照名称。",
      "format": "pve-configid",
      "maxLength": 40,
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/snapshot/{snapname}/config)。
