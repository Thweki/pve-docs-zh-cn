# `/nodes/{node}/storage/{storage}/identity`

原始接口路径：`/nodes/{node}/storage/{storage}/identity`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/identity`

返回此存储实例的标识信息。

**方法标识：** `identity`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.Audit",
      "Datastore.AllocateSpace"
    ],
    "any",
    1
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
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "id": {
      "description": "此存储实例的唯一标识符。确切格式和含义取决于存储插件类型。",
      "type": "string"
    },
    "type": {
      "description": "存储类型。",
      "enum": [
        "btrfs",
        "cephfs",
        "cifs",
        "dir",
        "esxi",
        "iscsi",
        "iscsidirect",
        "lvm",
        "lvmthin",
        "nfs",
        "pbs",
        "rbd",
        "zfs",
        "zfspool"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/identity)。
