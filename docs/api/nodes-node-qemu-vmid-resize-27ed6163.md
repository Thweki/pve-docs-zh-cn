# `/nodes/{node}/qemu/{vmid}/resize`

原始接口路径：`/nodes/{node}/qemu/{vmid}/resize`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/nodes/{node}/qemu/{vmid}/resize`

Extend volume size.

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
| `digest` | string | 否 | — | Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications. |
| `disk` | string | 是 | — | The disk you want to resize.；可选值：`ide0`, `ide1`, `ide2`, `ide3`, `scsi0`, `scsi1`, `scsi2`, `scsi3`, `scsi4`, `scsi5`, `scsi6`, `scsi7`, `scsi8`, `scsi9`, `scsi10`, `scsi11`, `scsi12`, `scsi13`, `scsi14`, `scsi15`, `scsi16`, `scsi17`, `scsi18`, `scsi19`, `scsi20`, `scsi21`, `scsi22`, `scsi23`, `scsi24`, `scsi25`, `scsi26`, `scsi27`, `scsi28`, `scsi29`, `scsi30`, `virtio0`, `virtio1`, `virtio2`, `virtio3`, `virtio4`, `virtio5`, `virtio6`, `virtio7`, `virtio8`, `virtio9`, `virtio10`, `virtio11`, `virtio12`, `virtio13`, `virtio14`, `virtio15`, `sata0`, `sata1`, `sata2`, `sata3`, `sata4`, `sata5`, `efidisk0`, `tpmstate0` |
| `node` | string | 是 | — | The cluster node name. |
| `size` | string | 是 | — | The new size. With the `+` sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported. |
| `skiplock` | boolean | 否 | — | Ignore locks - only root is allowed to use this option. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications.",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disk": {
      "description": "The disk you want to resize.",
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
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "size": {
      "description": "The new size. With the `+` sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported.",
      "pattern": "\\+?\\d+(\\.\\d+)?[KMGT]?",
      "type": "string"
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
  "description": "the task ID.",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/resize)。
