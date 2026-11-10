# `/nodes/{node}/qemu/{vmid}/template`

原始接口路径：`/nodes/{node}/qemu/{vmid}/template`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/template`

创建模板。

**方法标识：** `template`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Allocate"
    ]
  ],
  "description": "You need 'VM.Allocate' permissions on /vms/{vmid}"
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
| `disk` | string | 否 | — | If you want to convert only 1 disk to base image.；可选值：`ide0`, `ide1`, `ide2`, `ide3`, `scsi0`, `scsi1`, `scsi2`, `scsi3`, `scsi4`, `scsi5`, `scsi6`, `scsi7`, `scsi8`, `scsi9`, `scsi10`, `scsi11`, `scsi12`, `scsi13`, `scsi14`, `scsi15`, `scsi16`, `scsi17`, `scsi18`, `scsi19`, `scsi20`, `scsi21`, `scsi22`, `scsi23`, `scsi24`, `scsi25`, `scsi26`, `scsi27`, `scsi28`, `scsi29`, `scsi30`, `virtio0`, `virtio1`, `virtio2`, `virtio3`, `virtio4`, `virtio5`, `virtio6`, `virtio7`, `virtio8`, `virtio9`, `virtio10`, `virtio11`, `virtio12`, `virtio13`, `virtio14`, `virtio15`, `sata0`, `sata1`, `sata2`, `sata3`, `sata4`, `sata5`, `efidisk0`, `tpmstate0` |
| `node` | string | 是 | — | The cluster node name. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "disk": {
      "description": "If you want to convert only 1 disk to base image.",
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
      "optional": 1,
      "type": "string"
    },
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
  "description": "the task ID.",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/template)。
