# `/nodes/{node}/ceph/pool/{name}/status`

原始接口路径：`/nodes/{node}/ceph/pool/{name}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/pool/{name}/status`

显示池的当前状态。

**方法标识：** `getpool`

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
| `name` | string | 是 | — | 池名称。必须唯一。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `verbose` | boolean | 否 | 0 | 如果启用，将显示附加数据（例如统计信息）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "池名称。必须唯一。",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "verbose": {
      "default": 0,
      "description": "如果启用，将显示附加数据（例如统计信息）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "application": {
      "default": "rbd",
      "description": "池的应用。",
      "enum": [
        "rbd",
        "cephfs",
        "rgw"
      ],
      "optional": 1,
      "title": "应用",
      "type": "string"
    },
    "application_list": {
      "description": "当前关联到此池的应用名称。",
      "items": {
        "description": "应用名称（例如 'rbd'、'cephfs'、'rgw'）。",
        "type": "string"
      },
      "optional": 1,
      "title": "应用",
      "type": "array"
    },
    "autoscale_status": {
      "description": "此池的原始 pg_autoscaler 状态对象；结构随 Ceph 发行版而变化。",
      "optional": 1,
      "title": "自动扩缩状态",
      "type": "object"
    },
    "crush_rule": {
      "description": "用于映射集群中对象放置位置的规则。",
      "optional": 1,
      "title": "CRUSH 规则名称",
      "type": "string"
    },
    "fast_read": {
      "description": "此池对纠删码读取使用 fast-read 时设置。",
      "title": "快速读取",
      "type": "boolean"
    },
    "hashpspool": {
      "description": "此池将池 ID 哈希到其 CRUSH 归置种子时设置。",
      "title": "hashpspool",
      "type": "boolean"
    },
    "id": {
      "description": "Ceph 分配的数字池 ID。",
      "title": "ID",
      "type": "integer"
    },
    "min_size": {
      "default": 2,
      "description": "每个对象的最小副本数",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "title": "最小大小",
      "type": "integer"
    },
    "name": {
      "description": "池名称。必须唯一。",
      "pattern": "(?^:^[^:/\\s]+$)",
      "title": "名称",
      "type": "string"
    },
    "nodeep-scrub": {
      "description": "此池禁用深度清理检查时设置。",
      "title": "nodeep-scrub",
      "type": "boolean"
    },
    "nodelete": {
      "description": "阻止删除池时设置。",
      "title": "nodelete",
      "type": "boolean"
    },
    "nopgchange": {
      "description": "阻止更改归置组数量时设置。",
      "title": "nopgchange",
      "type": "boolean"
    },
    "noscrub": {
      "description": "此池禁用清理检查时设置。",
      "title": "noscrub",
      "type": "boolean"
    },
    "nosizechange": {
      "description": "阻止更改复制副本数时设置。",
      "title": "nosizechange",
      "type": "boolean"
    },
    "pg_autoscale_mode": {
      "default": "warn",
      "description": "池的自动 PG 扩缩模式。",
      "enum": [
        "on",
        "off",
        "warn"
      ],
      "optional": 1,
      "title": "PG 自动扩缩模式",
      "type": "string"
    },
    "pg_num": {
      "default": 128,
      "description": "归置组数量。",
      "maximum": 32768,
      "minimum": 1,
      "optional": 1,
      "title": "PG 数量",
      "type": "integer"
    },
    "pg_num_min": {
      "description": "最小归置组数量。",
      "maximum": 32768,
      "optional": 1,
      "title": "最小 PG 数量",
      "type": "integer"
    },
    "pgp_num": {
      "description": "用于归置的归置组数量。",
      "title": "PGP 数量",
      "type": "integer"
    },
    "size": {
      "default": 3,
      "description": "每个对象的副本数",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "title": "大小",
      "type": "integer"
    },
    "statistics": {
      "description": "可选的池用量和 IO 统计信息（仅在请求 verbose=1 时存在）。",
      "optional": 1,
      "title": "统计信息",
      "type": "object"
    },
    "target_size": {
      "description": "PG 自动扩缩器使用的池预估目标大小。",
      "optional": 1,
      "pattern": "^(\\d+(\\.\\d+)?)([KMGT])?$",
      "title": "PG 自动扩缩目标大小",
      "type": "string"
    },
    "target_size_ratio": {
      "description": "PG 自动扩缩器使用的池预估目标比例。",
      "optional": 1,
      "title": "PG 自动扩缩目标比例",
      "type": "number"
    },
    "use_gmt_hitset": {
      "description": "hitset 使用 GMT 时间戳时设置（适用于缓存层池）。",
      "title": "use_gmt_hitset",
      "type": "boolean"
    },
    "write_fadvise_dontneed": {
      "description": "此池在写入时设置 FADV_DONTNEED 提示时设置。",
      "title": "write_fadvise_dontneed",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/pool/{name}/status)。
