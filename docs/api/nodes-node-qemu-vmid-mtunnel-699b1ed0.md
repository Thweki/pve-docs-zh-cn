# `/nodes/{node}/qemu/{vmid}/mtunnel`

原始接口路径：`/nodes/{node}/qemu/{vmid}/mtunnel`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/mtunnel`

Migration tunnel endpoint - only for internal use by VM migration.

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
  "description": "You need 'VM.Allocate' permissions on '/vms/{vmid}' and Sys.Incoming on '/'. Further permission checks happen during the actual migration."
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
| `bridges` | string | 否 | — | List of network bridges to check availability. Will be checked again for actually used bridges during migration. |
| `node` | string | 是 | — | The cluster node name. |
| `storages` | string | 否 | — | List of storages to check permission and availability. Will be checked again for all actually used storages during migration. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bridges": {
      "description": "List of network bridges to check availability. Will be checked again for actually used bridges during migration.",
      "format": "pve-bridge-id-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storages": {
      "description": "List of storages to check permission and availability. Will be checked again for all actually used storages during migration.",
      "format": "pve-storage-id-list",
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
