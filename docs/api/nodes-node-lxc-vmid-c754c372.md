# `/nodes/{node}/lxc/{vmid}`

原始接口路径：`/nodes/{node}/lxc/{vmid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/lxc/{vmid}`

销毁容器（同时删除所有相关文件）。

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
| `destroy-unreferenced-disks` | boolean | 否 | — | 如果设置，还将销毁所有已启用存储中具有该 VMID 且未在配置中引用的磁盘。 |
| `force` | boolean | 否 | 0 | 强制销毁，即使正在运行。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `purge` | boolean | 否 | 0 | 从所有相关配置中移除容器，例如备份作业、复制作业或 HA。相关 ACL 和防火墙条目始终会被移除。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "destroy-unreferenced-disks": {
      "description": "如果设置，还将销毁所有已启用存储中具有该 VMID 且未在配置中引用的磁盘。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "force": {
      "default": 0,
      "description": "强制销毁，即使正在运行。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "purge": {
      "default": 0,
      "description": "从所有相关配置中移除容器，例如备份作业、复制作业或 HA。相关 ACL 和防火墙条目始终会被移除。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
  "type": "string"
}
```

## GET `/nodes/{node}/lxc/{vmid}`

目录索引

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
| `node` | string | 是 | — | 集群节点名称。 |
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid})。
