# `/cluster/backup/{id}/included_volumes`

原始接口路径：`/cluster/backup/{id}/included_volumes`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/backup/{id}/included_volumes`

返回包含的客户机及其磁盘的备份状态。已针对 ExtJS 树视图进行优化。

**方法标识：** `get_volume_backup_included`

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
| `id` | string | 是 | — | 作业 ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "作业 ID。",
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
  "description": "树对象的根节点。子节点表示客户机，孙节点表示该客户机的卷。",
  "properties": {
    "children": {
      "items": {
        "properties": {
          "children": {
            "description": "客户机的卷及其是否包含在备份中的信息。",
            "items": {
              "properties": {
                "id": {
                  "description": "卷的配置键。",
                  "type": "string"
                },
                "included": {
                  "description": "卷是否包含在备份中。",
                  "type": "boolean"
                },
                "name": {
                  "description": "卷名称。",
                  "type": "string"
                },
                "reason": {
                  "description": "包含（或排除）该卷的原因。",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "optional": 1,
            "type": "array"
          },
          "id": {
            "description": "客户机的 VMID。",
            "type": "integer"
          },
          "name": {
            "description": "客户机名称",
            "optional": 1,
            "type": "string"
          },
          "type": {
            "description": "客户机类型：VM、CT，或对于已移除但未清除的客户机为 unknown。",
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
