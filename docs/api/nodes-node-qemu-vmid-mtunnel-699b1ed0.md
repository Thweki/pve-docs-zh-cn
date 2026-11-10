# `/nodes/{node}/qemu/{vmid}/mtunnel`

原始接口路径：`/nodes/{node}/qemu/{vmid}/mtunnel`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/mtunnel`

迁移隧道端点——仅供虚拟机迁移内部使用。

**方法标识：** `mtunnel`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/vms/{vmid}",
      [
        "VM.Allocate"
      ]
    ],
    [
      "perm",
      "/",
      [
        "Sys.Incoming"
      ]
    ]
  ],
  "description": "需要对 '/vms/{vmid}' 具有 'VM.Allocate' 权限，并对 '/' 具有 Sys.Incoming 权限。进一步的权限检查在实际迁移期间进行。"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `bridges` | string | 否 | — | 要检查可用性的网络网桥列表。迁移期间将对实际使用的网桥再次检查。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storages` | string | 否 | — | 要检查权限和可用性的存储列表。迁移期间将对所有实际使用的存储再次检查。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bridges": {
      "description": "要检查可用性的网络网桥列表。迁移期间将对实际使用的网桥再次检查。",
      "format": "pve-bridge-id-list",
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
    "storages": {
      "description": "要检查权限和可用性的存储列表。迁移期间将对所有实际使用的存储再次检查。",
      "format": "pve-storage-id-list",
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
  "additionalProperties": 0,
  "properties": {
    "socket": {
      "type": "string"
    },
    "ticket": {
      "type": "string"
    },
    "upid": {
      "type": "string"
    }
  }
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/mtunnel)。
