# `/nodes/{node}/ceph/mds`

原始接口路径：`/nodes/{node}/ceph/mds`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/mds`

MDS 目录索引。

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
        "description": "MDS 通告的地址；采用 Ceph 格式（通常为 'IP:PORT/NONCE'）。",
        "optional": 1,
        "type": "string"
      },
      "ceph_version": {
        "description": "MDS 守护进程的完整 Ceph 版本字符串。",
        "optional": 1,
        "type": "string"
      },
      "ceph_version_short": {
        "description": "MDS 守护进程的简短 Ceph 版本字符串（例如 '19.2.0'）。",
        "optional": 1,
        "type": "string"
      },
      "direxists": {
        "description": "此节点上存在 MDS 数据目录时设置。",
        "optional": 1,
        "type": "boolean"
      },
      "fs_name": {
        "description": "此 MDS 绑定的 CephFS 名称；对于当前未负责任何 rank 的备用 MDS，不存在或为 null。",
        "optional": 1,
        "type": "string"
      },
      "host": {
        "description": "运行 MDS 的宿主机。",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "MDS 的名称（ID）。",
        "type": "string"
      },
      "rank": {
        "description": "MDS 在文件系统中的 rank；对于当前未绑定到 rank 的备用 MDS，为 -1。",
        "optional": 1,
        "type": "integer"
      },
      "service": {
        "description": "如果运行所在节点启用了 ceph-mds@<id> systemd 单元，则设置；否则不存在此项。",
        "optional": 1,
        "type": "boolean"
      },
      "standby_replay": {
        "description": "如果为 true，则备用 MDS 正在轮询活动 MDS 以加快恢复（热备）。",
        "optional": 1,
        "type": "boolean"
      },
      "state": {
        "description": "MDS 状态：对于集群已知的守护进程，为 Ceph 报告的运行状态（例如 'up:active'、'up:standby'、'up:standby-replay'）；对于已配置但集群不可见的守护进程，为 'stopped' 或 'unknown'。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/mds)。
