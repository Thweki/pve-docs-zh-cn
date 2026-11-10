# `/nodes/{node}/ceph/fs`

原始接口路径：`/nodes/{node}/ceph/fs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/fs`

Directory index.

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
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
  "items": {
    "additionalProperties": 1,
    "properties": {
      "data_pool": {
        "description": "Name of the filesystem's first data pool. A CephFS can have more than one data pool; consumers interested in the full set should read 'data_pools' instead. Kept for backwards compatibility.",
        "type": "string"
      },
      "data_pool_ids": {
        "description": "Numeric ids of the data pools.",
        "items": {
          "description": "Data pool id.",
          "type": "integer"
        },
        "optional": 1,
        "type": "array"
      },
      "data_pools": {
        "description": "Names of all data pools assigned to the filesystem; a CephFS can have multiple data pools (e.g. replicated metadata plus EC data, or multiple device-class-specific data pools).",
        "items": {
          "description": "Data pool name.",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "metadata_pool": {
        "description": "Name of the metadata pool.",
        "type": "string"
      },
      "metadata_pool_id": {
        "description": "Numeric id of the metadata pool.",
        "optional": 1,
        "type": "integer"
      },
      "name": {
        "description": "The ceph filesystem name.",
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
