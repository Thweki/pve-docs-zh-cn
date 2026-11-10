# `/nodes/{node}/ceph/osd/{osdid}`

原始接口路径：`/nodes/{node}/ceph/osd/{osdid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/osd/{osdid}`

销毁 OSD

**方法标识：** `destroyosd`

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
| `cleanup` | boolean | 否 | 0 | 如果设置，还将通过 'ceph-volume lvm zap --destroy' 销毁底层逻辑卷，使用 pvremove 移除卷组的物理卷，并擦除 filestore OSD 遗留的所有 journal/block.db/block.wal 分区。未设置此标志时，保留逻辑卷和分区以供检查。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `osdid` | integer | 是 | — | OSD ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cleanup": {
      "default": 0,
      "description": "如果设置，还将通过 'ceph-volume lvm zap --destroy' 销毁底层逻辑卷，使用 pvremove 移除卷组的物理卷，并擦除 filestore OSD 遗留的所有 journal/block.db/block.wal 分区。未设置此标志时，保留逻辑卷和分区以供检查。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "osdid": {
      "description": "OSD ID",
      "type": "integer",
      "typetext": "<integer>"
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

## GET `/nodes/{node}/ceph/osd/{osdid}`

OSD 索引。

**方法标识：** `osdindex`

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |
| `osdid` | integer | 是 | — | OSD ID |

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
    "osdid": {
      "description": "OSD ID",
      "type": "integer",
      "typetext": "<integer>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "properties": {},
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/osd/{osdid})。
