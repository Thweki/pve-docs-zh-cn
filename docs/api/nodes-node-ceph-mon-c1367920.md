# `/nodes/{node}/ceph/mon`

原始接口路径：`/nodes/{node}/ceph/mon`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/mon`

Get Ceph monitor list.

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
      "addr": {
        "description": "Address as advertised by the monitor; Ceph-formatted (typically 'IP:PORT/NONCE', possibly as a messenger-v2 vector depending on Ceph version and ceph.conf shape).",
        "optional": 1,
        "type": "string"
      },
      "ceph_version": {
        "description": "Full Ceph version string of the monitor daemon.",
        "optional": 1,
        "type": "string"
      },
      "ceph_version_short": {
        "description": "Short Ceph version string of the monitor daemon (e.g. '19.2.0').",
        "optional": 1,
        "type": "string"
      },
      "direxists": {
        "description": "Set when the monitor's data directory exists on this node.",
        "optional": 1,
        "type": "boolean"
      },
      "host": {
        "description": "Host the monitor runs on.",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "Monitor id (typically the hostname).",
        "type": "string"
      },
      "quorum": {
        "description": "Set when the monitor is part of the current quorum.",
        "optional": 1,
        "type": "boolean"
      },
      "rank": {
        "description": "Rank of the monitor within the mon map.",
        "optional": 1,
        "type": "integer"
      },
      "service": {
        "description": "Set if a ceph-mon@<id> systemd unit is enabled on the hosting node; absent otherwise.",
        "optional": 1,
        "type": "boolean"
      },
      "state": {
        "description": "Run state of the monitor: 'running' (in quorum), 'stopped' (systemd unit configured but daemon not visible to the cluster), or 'unknown' (no rados access).",
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
