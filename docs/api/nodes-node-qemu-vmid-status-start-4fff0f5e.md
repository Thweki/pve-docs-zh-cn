# `/nodes/{node}/qemu/{vmid}/status/start`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/start`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/start`

启动虚拟机。

**方法标识：** `vm_start`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.PowerMgmt"
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
| `force-cpu` | string | 否 | — | 使用给定字符串覆盖 QEMU 的 -cpu 参数。 |
| `machine` | string | 否 | — | 指定 QEMU 机器。 |
| `migratedfrom` | string | 否 | — | 集群节点名称。 |
| `migration_network` | string | 否 | — | 用于迁移的（子）网络的 CIDR。 |
| `migration_type` | string | 否 | — | 迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。；可选值：`secure`, `insecure` |
| `nets-host-mtu` | string | 否 | — | 用于迁移兼容性。VirtIO 网络设备及其生效的 host_mtu 设置列表，依据迁移源端的 QEMU 对象模型。值为 0 表示应避免为相应设备使用 host_mtu 参数。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `skiplock` | boolean | 否 | — | 忽略锁——仅 root 可使用此选项。 |
| `stateuri` | string | 否 | — | 某些命令从此位置保存/还原状态。 |
| `targetstorage` | string | 否 | — | 从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。 |
| `timeout` | integer | 否 | "max(30, vm memory in GiB)" | 最多等待 timeout 秒。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |
| `with-conntrack-state` | boolean | 否 | 0 | 是否为运行中的虚拟机迁移 conntrack 条目。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force-cpu": {
      "description": "使用给定字符串覆盖 QEMU 的 -cpu 参数。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "machine": {
      "description": "指定 QEMU 机器。",
      "format": {
        "aw-bits": {
          "description": "指定 vIOMMU 地址空间的位宽。",
          "maximum": 64,
          "minimum": 32,
          "optional": 1,
          "type": "number",
          "verbose_description": "指定 vIOMMU 地址空间的位宽。\n\nIntel vIOMMU 支持 39 或 48 位，VirtIO vIOMMU 支持 32 到 64 位之间的任意位宽。"
        },
        "enable-s3": {
          "description": "启用 S3 电源状态。从机器类型 9.2+pve1 起默认为 false，此前为 true。",
          "optional": 1,
          "type": "boolean"
        },
        "enable-s4": {
          "description": "启用 S4 电源状态。从机器类型 9.2+pve1 起默认为 false，此前为 true。",
          "optional": 1,
          "type": "boolean"
        },
        "type": {
          "default_key": 1,
          "description": "指定 QEMU 机器类型。",
          "format_description": "machine type",
          "maxLength": 40,
          "optional": 1,
          "pattern": "(pc|pc(-i440fx)?-\\d+(\\.\\d+)+(\\+pve\\d+)?(\\.pxe)?|q35|pc-q35-\\d+(\\.\\d+)+(\\+pve\\d+)?(\\.pxe)?|virt(?:-\\d+(\\.\\d+)+)?(\\+pve\\d+)?)",
          "type": "string"
        },
        "viommu": {
          "description": "启用并设置客户机 vIOMMU 变体（Intel vIOMMU 需要将机器类型设为 q35）。",
          "enum": [
            "intel",
            "virtio"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]"
    },
    "migratedfrom": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "migration_network": {
      "description": "用于迁移的（子）网络的 CIDR。",
      "format": "CIDR",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "migration_type": {
      "description": "迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
      "enum": [
        "secure",
        "insecure"
      ],
      "optional": 1,
      "type": "string"
    },
    "nets-host-mtu": {
      "description": "用于迁移兼容性。VirtIO 网络设备及其生效的 host_mtu 设置列表，依据迁移源端的 QEMU 对象模型。值为 0 表示应避免为相应设备使用 host_mtu 参数。",
      "optional": 1,
      "pattern": "net\\d+=\\d+(,net\\d+=\\d+)*",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "skiplock": {
      "description": "忽略锁——仅 root 可使用此选项。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stateuri": {
      "description": "某些命令从此位置保存/还原状态。",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "targetstorage": {
      "description": "从源存储到目标存储的映射。仅提供单个存储 ID 会将所有源存储映射到该存储。提供特殊值 '1' 会将每个源存储映射到其自身。",
      "format": "storage-pair-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": "max(30, vm memory in GiB)",
      "description": "最多等待 timeout 秒。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "with-conntrack-state": {
      "default": 0,
      "description": "是否为运行中的虚拟机迁移 conntrack 条目。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/start)。
