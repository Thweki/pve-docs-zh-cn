# `/nodes/{node}/disks/lvm/{name}`

原始接口路径：`/nodes/{node}/disks/lvm/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/disks/lvm/{name}`

Remove an LVM Volume Group.

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
  ],
  "description": "Requires additionally 'Datastore.Allocate' on /storage when setting 'cleanup-config'"
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
| `cleanup-config` | boolean | 否 | 0 | Marks associated storage(s) as not available on this node anymore or removes them from the configuration (if configured for this node only). |
| `cleanup-disks` | boolean | 否 | 0 | Also wipe disks so they can be repurposed afterwards. |
| `name` | string | 是 | — | The storage identifier. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cleanup-config": {
      "default": 0,
      "description": "Marks associated storage(s) as not available on this node anymore or removes them from the configuration (if configured for this node only).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cleanup-disks": {
      "default": 0,
      "description": "Also wipe disks so they can be repurposed afterwards.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/lvm/{name})。
