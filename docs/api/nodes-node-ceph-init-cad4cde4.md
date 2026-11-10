# `/nodes/{node}/ceph/init`

原始接口路径：`/nodes/{node}/ceph/init`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/ceph/init`

Create the initial Ceph default configuration and set up symlinks. Idempotent on re-call: if a [global] section already exists in ceph.conf, the existing fsid / auth / pool defaults are preserved and most parameters are silently ignored.

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
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
| `cluster-network` | string | 否 | — | Declare a separate cluster network, OSDs will route heartbeat, object replication and recovery traffic over it |
| `disable_cephx` | boolean | 否 | 0 | Disable cephx authentication. WARNING: cephx is a security feature protecting against man-in-the-middle attacks. Only consider disabling cephx if your network is private! |
| `min_size` | integer | 否 | 2 | Minimum number of available replicas per object to allow I/O |
| `network` | string | 否 | — | Use specific network for all ceph related traffic |
| `node` | string | 是 | — | The cluster node name. |
| `pg_bits` | integer | 否 | 6 | Placement group bits, used to specify the default number of placement groups. Depreacted. This setting was deprecated in recent Ceph versions. |
| `size` | integer | 否 | 3 | Targeted number of replicas per object |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cluster-network": {
      "description": "Declare a separate cluster network, OSDs will route heartbeat, object replication and recovery traffic over it",
      "format": "CIDR",
      "maxLength": 128,
      "optional": 1,
      "requires": "network",
      "type": "string",
      "typetext": "<string>"
    },
    "disable_cephx": {
      "default": 0,
      "description": "Disable cephx authentication. WARNING: cephx is a security feature protecting against man-in-the-middle attacks. Only consider disabling cephx if your network is private!",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "min_size": {
      "default": 2,
      "description": "Minimum number of available replicas per object to allow I/O",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
    },
    "network": {
      "description": "Use specific network for all ceph related traffic",
      "format": "CIDR",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pg_bits": {
      "default": 6,
      "description": "Placement group bits, used to specify the default number of placement groups. Depreacted. This setting was deprecated in recent Ceph versions.",
      "maximum": 14,
      "minimum": 6,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (6 - 14)"
    },
    "size": {
      "default": 3,
      "description": "Targeted number of replicas per object",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/init)。
