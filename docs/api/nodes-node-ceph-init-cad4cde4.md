# `/nodes/{node}/ceph/init`

原始接口路径：`/nodes/{node}/ceph/init`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/ceph/init`

创建初始 Ceph 默认配置并设置符号链接。重复调用具有幂等性：如果 ceph.conf 中已有 [global] 配置节，则保留现有 fsid / auth / pool 默认值，并静默忽略大多数参数。

**方法标识：** `init`

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
| `cluster-network` | string | 否 | — | 声明单独的集群网络，OSD 将通过该网络传输心跳、对象复制和恢复流量 |
| `disable_cephx` | boolean | 否 | 0 | 禁用 cephx 身份验证。<br><br>警告：cephx 是防范中间人攻击的安全功能。仅在网络为私有网络时才考虑禁用 cephx！ |
| `min_size` | integer | 否 | 2 | 允许 I/O 所需的每个对象的最小可用副本数 |
| `network` | string | 否 | — | 为所有 ceph 相关流量使用指定网络 |
| `node` | string | 是 | — | 集群节点名称。 |
| `pg_bits` | integer | 否 | 6 | 归置组位数，用于指定默认归置组数量。<br><br>已弃用。此设置已在近期 Ceph 版本中弃用。 |
| `size` | integer | 否 | 3 | 每个对象的目标副本数 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cluster-network": {
      "description": "声明单独的集群网络，OSD 将通过该网络传输心跳、对象复制和恢复流量",
      "format": "CIDR",
      "maxLength": 128,
      "optional": 1,
      "requires": "network",
      "type": "string",
      "typetext": "<string>"
    },
    "disable_cephx": {
      "default": 0,
      "description": "禁用 cephx 身份验证。\n\n警告：cephx 是防范中间人攻击的安全功能。仅在网络为私有网络时才考虑禁用 cephx！",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "min_size": {
      "default": 2,
      "description": "允许 I/O 所需的每个对象的最小可用副本数",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
    },
    "network": {
      "description": "为所有 ceph 相关流量使用指定网络",
      "format": "CIDR",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pg_bits": {
      "default": 6,
      "description": "归置组位数，用于指定默认归置组数量。\n\n已弃用。此设置已在近期 Ceph 版本中弃用。",
      "maximum": 14,
      "minimum": 6,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (6 - 14)"
    },
    "size": {
      "default": 3,
      "description": "每个对象的目标副本数",
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
