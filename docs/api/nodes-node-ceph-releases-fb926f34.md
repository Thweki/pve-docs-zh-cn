# `/nodes/{node}/ceph/releases`

原始接口路径：`/nodes/{node}/ceph/releases`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/releases`

List all known Ceph releases, marking which ones can be installed on this node.

**方法标识：** `releases`

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
    "properties": {
      "available": {
        "description": "Whether this release can be installed on this node, that is, it has packages for the node's architecture and current Proxmox VE release.",
        "type": "boolean"
      },
      "is-default": {
        "description": "Whether this is the release recommended for new installations.",
        "type": "boolean"
      },
      "release": {
        "description": "The Ceph release code name, for example 'squid'.",
        "type": "string"
      },
      "unsupported": {
        "description": "Whether this release is not (yet) supported for production use.",
        "type": "boolean"
      },
      "version": {
        "description": "The Ceph release major version, for example '19.2'.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/releases)。
