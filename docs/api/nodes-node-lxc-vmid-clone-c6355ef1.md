# `/nodes/{node}/lxc/{vmid}/clone`

原始接口路径：`/nodes/{node}/lxc/{vmid}/clone`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/lxc/{vmid}/clone`

创建容器克隆/副本

**方法标识：** `clone_vm`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/vms/{vmid}",
      [
        "VM.Clone"
      ]
    ],
    [
      "or",
      [
        "perm",
        "/vms/{newid}",
        [
          "VM.Allocate"
        ]
      ],
      [
        "perm",
        "/pool/{pool}",
        [
          "VM.Allocate"
        ],
        "require_param",
        "pool"
      ]
    ]
  ],
  "description": "需要对 /vms/{vmid} 具有 'VM.Clone' 权限，以及对 /vms/{newid}（或虚拟机资源池 /pool/{pool}）具有 'VM.Allocate' 权限。还需要对所有使用的存储具有 'Datastore.AllocateSpace' 权限，以及对所有网桥具有 'SDN.Use' 权限。"
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
| `bwlimit` | number | 否 | "clone limit from datacenter or storage config" | 覆盖 I/O 带宽限制（KiB/s）。 |
| `description` | string | 否 | — | 新容器的描述。 |
| `full` | boolean | 否 | — | 创建所有磁盘的完整副本。克隆普通容器时始终执行完整复制。对于容器模板，默认尝试创建链接克隆。 |
| `hostname` | string | 否 | — | 为新容器设置主机名。 |
| `newid` | integer | 是 | — | 克隆的 VMID。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `pool` | string | 否 | — | 将新容器添加到指定资源池。 |
| `snapname` | string | 否 | — | 快照名称。 |
| `storage` | string | 否 | — | 完整克隆的目标存储。 |
| `target` | string | 否 | — | 目标节点。仅当原始虚拟机位于共享存储上时允许。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "default": "clone limit from datacenter or storage config",
      "description": "覆盖 I/O 带宽限制（KiB/s）。",
      "minimum": "0",
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - N)"
    },
    "description": {
      "description": "新容器的描述。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "full": {
      "description": "创建所有磁盘的完整副本。克隆普通容器时始终执行完整复制。对于容器模板，默认尝试创建链接克隆。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hostname": {
      "description": "为新容器设置主机名。",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "newid": {
      "description": "克隆的 VMID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pool": {
      "description": "将新容器添加到指定资源池。",
      "format": "pve-poolid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "snapname": {
      "description": "快照名称。",
      "format": "pve-configid",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "完整克隆的目标存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "target": {
      "description": "目标节点。仅当原始虚拟机位于共享存储上时允许。",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/clone)。
