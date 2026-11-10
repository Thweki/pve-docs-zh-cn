# `/nodes/{node}/ceph/mon`

原始接口路径：`/nodes/{node}/ceph/mon`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/mon`

获取 Ceph 监视器列表。

**方法标识：** `listmon`

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
        "description": "监视器通告的地址；采用 Ceph 格式（通常为 'IP:PORT/NONCE'，也可能是 messenger-v2 向量，取决于 Ceph 版本和 ceph.conf 的结构）。",
        "optional": 1,
        "type": "string"
      },
      "ceph_version": {
        "description": "监视器守护进程的完整 Ceph 版本字符串。",
        "optional": 1,
        "type": "string"
      },
      "ceph_version_short": {
        "description": "监视器守护进程的简短 Ceph 版本字符串（例如 '19.2.0'）。",
        "optional": 1,
        "type": "string"
      },
      "direxists": {
        "description": "此节点上存在监视器数据目录时设置。",
        "optional": 1,
        "type": "boolean"
      },
      "host": {
        "description": "运行监视器的宿主机。",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "监视器 ID（通常为主机名）。",
        "type": "string"
      },
      "quorum": {
        "description": "监视器属于当前仲裁成员时设置。",
        "optional": 1,
        "type": "boolean"
      },
      "rank": {
        "description": "监视器在 mon 映射中的 rank。",
        "optional": 1,
        "type": "integer"
      },
      "service": {
        "description": "如果运行所在节点启用了 ceph-mon@<id> systemd 单元，则设置；否则不存在此项。",
        "optional": 1,
        "type": "boolean"
      },
      "state": {
        "description": "监视器的运行状态：'running'（参与仲裁）、'stopped'（已配置 systemd 单元，但集群看不到该守护进程），或 'unknown'（无法访问 rados）。",
        "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/mon)。
