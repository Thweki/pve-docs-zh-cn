# `/nodes/{node}/ceph/mgr`

原始接口路径：`/nodes/{node}/ceph/mgr`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/mgr`

MGR 目录索引。

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
    "properties": {
      "addr": {
        "description": "管理器通告的地址；采用 Ceph 格式（通常为 'IP:PORT/NONCE'）。",
        "optional": 1,
        "type": "string"
      },
      "ceph_version": {
        "description": "管理器守护进程的完整 Ceph 版本字符串。",
        "optional": 1,
        "type": "string"
      },
      "ceph_version_short": {
        "description": "管理器守护进程的简短 Ceph 版本字符串（例如 '19.2.0'）。",
        "optional": 1,
        "type": "string"
      },
      "direxists": {
        "description": "此节点上存在管理器数据目录时设置。",
        "optional": 1,
        "type": "boolean"
      },
      "host": {
        "description": "运行管理器的宿主机。",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "MGR 的名称（ID）。",
        "type": "string"
      },
      "service": {
        "description": "如果运行所在节点启用了 ceph-mgr@<id> systemd 单元，则设置；否则不存在此项。",
        "optional": 1,
        "type": "boolean"
      },
      "state": {
        "description": "管理器状态：对于 mgr 集群可见的守护进程，为 'active' 或 'standby'；对于已配置但当前不可见的守护进程，为 'stopped' 或 'unknown'。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/mgr)。
