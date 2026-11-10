# `/cluster/backup-info/not-backed-up`

原始接口路径：`/cluster/backup-info/not-backed-up`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/backup-info/not-backed-up`

显示未被任何备份作业覆盖的所有客户机。

**方法标识：** `get_guests_not_in_backup`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "description": "包含客户机对象。",
  "items": {
    "properties": {
      "name": {
        "description": "客户机名称",
        "optional": 1,
        "type": "string"
      },
      "type": {
        "description": "客户机类型。",
        "enum": [
          "qemu",
          "lxc"
        ],
        "type": "string"
      },
      "vmid": {
        "description": "客户机的 VMID。",
        "type": "integer"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup-info/not-backed-up)。
