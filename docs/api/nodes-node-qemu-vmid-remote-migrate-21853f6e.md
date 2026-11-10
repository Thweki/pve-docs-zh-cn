# `/nodes/{node}/qemu/{vmid}/remote_migrate`

原始接口路径：`/nodes/{node}/qemu/{vmid}/remote_migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/remote_migrate`

将虚拟机迁移到远程集群。创建新的迁移任务。实验性功能！

**方法标识：** `remote_migrate_vm`

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
| `delete` | boolean | 否 | 0 | 成功迁移后删除原始虚拟机及相关数据。默认将原始虚拟机以停止状态保留在源集群中。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `online` | boolean | 否 | — | 如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。 |
| `target-bridge` | string | 是 | — | 从源网桥到目标网桥的映射。仅提供单个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 '1' 会将每个源网桥映射到其自身。 |
| `target-endpoint` | string | 是 | — | 远程目标端点 |
| `target-storage` | string | 是 | — | 从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。 |
| `target-vmid` | integer | 否 | — | 虚拟机的（唯一）ID。 |
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
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "delete": {
      "default": 0,
      "description": "成功迁移后删除原始虚拟机及相关数据。默认将原始虚拟机以停止状态保留在源集群中。",
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
    "online": {
      "description": "如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "target-bridge": {
      "description": "从源网桥到目标网桥的映射。仅提供单个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 '1' 会将每个源网桥映射到其自身。",
      "format": "bridge-pair-list",
      "type": "string",
      "typetext": "<string>"
    },
    "target-endpoint": {
      "description": "远程目标端点",
      "format": "proxmox-remote",
      "type": "string",
      "typetext": "apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]"
    },
    "target-storage": {
      "description": "从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。",
      "format": "storage-pair-list",
      "optional": 0,
      "type": "string",
      "typetext": "<string>"
    },
    "target-vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/remote_migrate)。
