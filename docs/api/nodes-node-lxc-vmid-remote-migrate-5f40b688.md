# `/nodes/{node}/lxc/{vmid}/remote_migrate`

原始接口路径：`/nodes/{node}/lxc/{vmid}/remote_migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/lxc/{vmid}/remote_migrate`

Migrate the container to another cluster. Creates a new migration task. EXPERIMENTAL feature!

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
| `delete` | boolean | 否 | 0 | Delete the original CT and related data after successful migration. By default the original CT is kept on the source cluster in a stopped state. |
| `node` | string | 是 | — | The cluster node name. |
| `online` | boolean | 否 | — | Use online/live migration. |
| `restart` | boolean | 否 | — | Use restart migration |
| `target-bridge` | string | 是 | — | Mapping from source to target bridges. Providing only a single bridge ID maps all source bridges to that bridge. Providing the special value '1' will map each source bridge to itself. |
| `target-endpoint` | string | 是 | — | Remote target endpoint |
| `target-storage` | string | 是 | — | Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself. |
| `target-vmid` | integer | 否 | — | The (unique) ID of the VM. |
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
    "delete": {
      "default": 0,
      "description": "Delete the original CT and related data after successful migration. By default the original CT is kept on the source cluster in a stopped state.",
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
    "target-bridge": {
      "description": "Mapping from source to target bridges. Providing only a single bridge ID maps all source bridges to that bridge. Providing the special value '1' will map each source bridge to itself.",
      "format": "bridge-pair-list",
      "type": "string",
      "typetext": "<string>"
    },
    "target-endpoint": {
      "description": "Remote target endpoint",
      "format": "proxmox-remote",
      "type": "string",
      "typetext": "apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]"
    },
    "target-storage": {
      "description": "Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself.",
      "format": "storage-pair-list",
      "optional": 0,
      "type": "string",
      "typetext": "<string>"
    },
    "target-vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/remote_migrate)。
