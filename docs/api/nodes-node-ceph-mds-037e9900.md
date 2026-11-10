# `/nodes/{node}/ceph/mds`

原始接口路径：`/nodes/{node}/ceph/mds`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/mds`

MDS directory index.

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
        "description": "Address as advertised by the MDS; Ceph-formatted (typically 'IP:PORT/NONCE').",
        "optional": 1,
        "type": "string"
      },
      "ceph_version": {
        "description": "Full Ceph version string of the MDS daemon.",
        "optional": 1,
        "type": "string"
      },
      "ceph_version_short": {
        "description": "Short Ceph version string of the MDS daemon (e.g. '19.2.0').",
        "optional": 1,
        "type": "string"
      },
      "direxists": {
        "description": "Set when the MDS's data directory exists on this node.",
        "optional": 1,
        "type": "boolean"
      },
      "fs_name": {
        "description": "Name of the CephFS this MDS is bound to; absent or null for standby MDSes not currently serving a rank.",
        "optional": 1,
        "type": "string"
      },
      "host": {
        "description": "Host the MDS runs on.",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "The name (ID) for the MDS.",
        "type": "string"
      },
      "rank": {
        "description": "MDS rank within the file system; -1 for standby MDSes not currently bound to a rank.",
        "optional": 1,
        "type": "integer"
      },
      "service": {
        "description": "Set if a ceph-mds@<id> systemd unit is enabled on the hosting node; absent otherwise.",
        "optional": 1,
        "type": "boolean"
      },
      "standby_replay": {
        "description": "If true, the standby MDS is polling the active MDS for faster recovery (hot standby).",
        "optional": 1,
        "type": "boolean"
      },
      "state": {
        "description": "MDS state: Ceph-reported run state (e.g. 'up:active', 'up:standby', 'up:standby-replay') for daemons known to the cluster; 'stopped' or 'unknown' for configured daemons not visible to the cluster.",
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
