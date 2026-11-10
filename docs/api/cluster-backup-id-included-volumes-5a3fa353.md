# `/cluster/backup/{id}/included_volumes`

原始接口路径：`/cluster/backup/{id}/included_volumes`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/backup/{id}/included_volumes`

Returns included guests and the backup status of their disks. Optimized to be used in ExtJS tree views.

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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | — | The job ID. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "The job ID.",
      "maxLength": 50,
      "pattern": "\\S+",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "Root node of the tree object. Children represent guests, grandchildren represent volumes of that guest.",
  "properties": {
    "children": {
      "items": {
        "properties": {
          "children": {
            "description": "The volumes of the guest with the information if they will be included in backups.",
            "items": {
              "properties": {
                "id": {
                  "description": "Configuration key of the volume.",
                  "type": "string"
                },
                "included": {
                  "description": "Whether the volume is included in the backup or not.",
                  "type": "boolean"
                },
                "name": {
                  "description": "Name of the volume.",
                  "type": "string"
                },
                "reason": {
                  "description": "The reason why the volume is included (or excluded).",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "optional": 1,
            "type": "array"
          },
          "id": {
            "description": "VMID of the guest.",
            "type": "integer"
          },
          "name": {
            "description": "Name of the guest",
            "optional": 1,
            "type": "string"
          },
          "type": {
            "description": "Type of the guest, VM, CT or unknown for removed but not purged guests.",
            "enum": [
              "qemu",
              "lxc",
              "unknown"
            ],
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup/{id}/included_volumes)。
