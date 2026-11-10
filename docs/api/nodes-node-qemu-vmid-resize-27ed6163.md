# `/nodes/{node}/qemu/{vmid}/resize`

原始接口路径：`/nodes/{node}/qemu/{vmid}/resize`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/nodes/{node}/qemu/{vmid}/resize`

扩展卷大小。

**方法标识：** `resize_vm`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Disk"
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
| `digest` | string | 否 | — | 如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。 |
| `disk` | string | 是 | — | 要调整大小的磁盘。；可选值：`ide0`, `ide1`, `ide2`, `ide3`, `scsi0`, `scsi1`, `scsi2`, `scsi3`, `scsi4`, `scsi5`, `scsi6`, `scsi7`, `scsi8`, `scsi9`, `scsi10`, `scsi11`, `scsi12`, `scsi13`, `scsi14`, `scsi15`, `scsi16`, `scsi17`, `scsi18`, `scsi19`, `scsi20`, `scsi21`, `scsi22`, `scsi23`, `scsi24`, `scsi25`, `scsi26`, `scsi27`, `scsi28`, `scsi29`, `scsi30`, `virtio0`, `virtio1`, `virtio2`, `virtio3`, `virtio4`, `virtio5`, `virtio6`, `virtio7`, `virtio8`, `virtio9`, `virtio10`, `virtio11`, `virtio12`, `virtio13`, `virtio14`, `virtio15`, `sata0`, `sata1`, `sata2`, `sata3`, `sata4`, `sata5`, `efidisk0`, `tpmstate0` |
| `node` | string | 是 | — | 集群节点名称。 |
| `size` | string | 是 | — | 新大小。带 `+` 符号时，将此值加到卷的实际大小上；不带时，将此值视为绝对大小。不支持缩小磁盘。 |
| `skiplock` | boolean | 否 | — | 忽略锁——仅 root 可使用此选项。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disk": {
      "description": "要调整大小的磁盘。",
      "enum": [
        "ide0",
        "ide1",
        "ide2",
        "ide3",
        "scsi0",
        "scsi1",
        "scsi2",
        "scsi3",
        "scsi4",
        "scsi5",
        "scsi6",
        "scsi7",
        "scsi8",
        "scsi9",
        "scsi10",
        "scsi11",
        "scsi12",
        "scsi13",
        "scsi14",
        "scsi15",
        "scsi16",
        "scsi17",
        "scsi18",
        "scsi19",
        "scsi20",
        "scsi21",
        "scsi22",
        "scsi23",
        "scsi24",
        "scsi25",
        "scsi26",
        "scsi27",
        "scsi28",
        "scsi29",
        "scsi30",
        "virtio0",
        "virtio1",
        "virtio2",
        "virtio3",
        "virtio4",
        "virtio5",
        "virtio6",
        "virtio7",
        "virtio8",
        "virtio9",
        "virtio10",
        "virtio11",
        "virtio12",
        "virtio13",
        "virtio14",
        "virtio15",
        "sata0",
        "sata1",
        "sata2",
        "sata3",
        "sata4",
        "sata5",
        "efidisk0",
        "tpmstate0"
      ],
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "size": {
      "description": "新大小。带 `+` 符号时，将此值加到卷的实际大小上；不带时，将此值视为绝对大小。不支持缩小磁盘。",
      "pattern": "\\+?\\d+(\\.\\d+)?[KMGT]?",
      "type": "string"
    },
    "skiplock": {
      "description": "忽略锁——仅 root 可使用此选项。",
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
  "description": "任务 ID。",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/resize)。
