# `/nodes/{node}/ceph/fs`

原始接口路径：`/nodes/{node}/ceph/fs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/fs`

目录索引。

**方法标识：** `index`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Datastore.Audit"
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
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "additionalProperties": 1,
    "properties": {
      "data_pool": {
        "description": "文件系统第一个数据池的名称。CephFS 可拥有多个数据池；需要完整集合的使用方应读取 'data_pools'。为向后兼容而保留。",
        "type": "string"
      },
      "data_pool_ids": {
        "description": "数据池的数字 ID。",
        "items": {
          "description": "数据池 ID。",
          "type": "integer"
        },
        "optional": 1,
        "type": "array"
      },
      "data_pools": {
        "description": "分配给文件系统的所有数据池的名称；CephFS 可有多个数据池（例如复制型元数据加 EC 数据，或多个特定设备类别的数据池）。",
        "items": {
          "description": "数据池名称。",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "metadata_pool": {
        "description": "元数据池名称。",
        "type": "string"
      },
      "metadata_pool_id": {
        "description": "元数据池的数字 ID。",
        "optional": 1,
        "type": "integer"
      },
      "name": {
        "description": "Ceph 文件系统名称。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/fs)。
