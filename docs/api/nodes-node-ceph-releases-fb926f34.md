# `/nodes/{node}/ceph/releases`

原始接口路径：`/nodes/{node}/ceph/releases`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/releases`

列出所有已知的 Ceph 发行版，并标记哪些可安装到此节点。

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
    "properties": {
      "available": {
        "description": "此发行版是否可安装到此节点，即是否提供适用于节点架构和当前 Proxmox VE 发行版的软件包。",
        "type": "boolean"
      },
      "is-default": {
        "description": "此发行版是否为新安装推荐的版本。",
        "type": "boolean"
      },
      "release": {
        "description": "Ceph 发行版代号，例如 'squid'。",
        "type": "string"
      },
      "unsupported": {
        "description": "此发行版是否尚不支持用于生产环境。",
        "type": "boolean"
      },
      "version": {
        "description": "Ceph 发行版主版本，例如 '19.2'。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/releases)。
