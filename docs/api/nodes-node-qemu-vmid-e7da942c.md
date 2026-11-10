# `/nodes/{node}/qemu/{vmid}`

原始接口路径：`/nodes/{node}/qemu/{vmid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/qemu/{vmid}`

Destroy the VM and  all used/owned volumes. Removes any VM specific permissions and firewall rules

**方法标识：** `destroy_vm`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Allocate"
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
| `destroy-unreferenced-disks` | boolean | 否 | 0 | If set, destroy additionally all disks not referenced in the config but with a matching VMID from all enabled storages. |
| `node` | string | 是 | — | The cluster node name. |
| `purge` | boolean | 否 | — | Remove VMID from configurations, like backup &amp; replication jobs and HA. |
| `skiplock` | boolean | 否 | — | Ignore locks - only root is allowed to use this option. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "destroy-unreferenced-disks": {
      "default": 0,
      "description": "If set, destroy additionally all disks not referenced in the config but with a matching VMID from all enabled storages.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "purge": {
      "description": "Remove VMID from configurations, like backup & replication jobs and HA.",
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

## GET `/nodes/{node}/qemu/{vmid}`

Directory index

**方法标识：** `vmdiridx`

**权限**

```json
{
  "user": "all"
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
  "items": {
    "properties": {
      "subdir": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{subdir}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid})。
