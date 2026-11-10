# `/nodes/{node}/ceph/mgr`

原始接口路径：`/nodes/{node}/ceph/mgr`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/mgr`

MGR directory index.

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
        "description": "Address as advertised by the manager; Ceph-formatted (typically 'IP:PORT/NONCE').",
        "optional": 1,
        "type": "string"
      },
      "ceph_version": {
        "description": "Full Ceph version string of the manager daemon.",
        "optional": 1,
        "type": "string"
      },
      "ceph_version_short": {
        "description": "Short Ceph version string of the manager daemon (e.g. '19.2.0').",
        "optional": 1,
        "type": "string"
      },
      "direxists": {
        "description": "Set when the manager's data directory exists on this node.",
        "optional": 1,
        "type": "boolean"
      },
      "host": {
        "description": "Host the manager runs on.",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "The name (ID) for the MGR.",
        "type": "string"
      },
      "service": {
        "description": "Set if a ceph-mgr@<id> systemd unit is enabled on the hosting node; absent otherwise.",
        "optional": 1,
        "type": "boolean"
      },
      "state": {
        "description": "Manager state: 'active' or 'standby' for daemons visible to the mgr cluster, 'stopped' or 'unknown' for configured daemons not currently visible.",
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
