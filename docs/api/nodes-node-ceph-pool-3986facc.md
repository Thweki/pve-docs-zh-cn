# `/nodes/{node}/ceph/pool`

原始接口路径：`/nodes/{node}/ceph/pool`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/pool`

列出所有池及其设置（可通过 POST/PUT 端点设置的项目）。

**方法标识：** `lspools`

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
      "application_metadata": {
        "description": "附加到池的应用标签（应用名称到其元数据对象的映射）。",
        "optional": 1,
        "title": "关联的应用",
        "type": "object"
      },
      "autoscale_status": {
        "description": "此池的原始 pg_autoscaler 状态对象；结构随 Ceph 发行版而变化。",
        "optional": 1,
        "title": "自动扩缩状态",
        "type": "object"
      },
      "bytes_used": {
        "description": "池当前使用的字节数；未报告用量统计信息时不存在此项。",
        "optional": 1,
        "renderer": "bytes",
        "title": "已用",
        "type": "integer"
      },
      "crush_rule": {
        "description": "此池使用的 CRUSH 规则的数字 ID。",
        "title": "CRUSH 规则",
        "type": "integer"
      },
      "crush_rule_name": {
        "description": "此池使用的 CRUSH 规则的人类可读名称；规则 ID 不在当前 CRUSH 映射中时不存在此项。",
        "optional": 1,
        "title": "CRUSH 规则名称",
        "type": "string"
      },
      "min_size": {
        "description": "接受写入所需的最小副本数。",
        "title": "最小大小",
        "type": "integer"
      },
      "percent_used": {
        "description": "池容量当前使用的百分比；未报告用量统计信息时不存在此项。",
        "optional": 1,
        "title": "已用百分比",
        "type": "number"
      },
      "pg_autoscale_mode": {
        "description": "归置组自动扩缩器模式（'on'、'warn' 或 'off'）。",
        "optional": 1,
        "title": "PG 自动扩缩模式",
        "type": "string"
      },
      "pg_num": {
        "description": "当前归置组数量。",
        "title": "PG 数量",
        "type": "integer"
      },
      "pg_num_final": {
        "description": "pg_autoscaler 计算的最佳归置组数量。",
        "optional": 1,
        "title": "最佳 PG 数量",
        "type": "integer"
      },
      "pg_num_min": {
        "description": "pg_autoscaler 可选择的最小归置组数量。",
        "optional": 1,
        "title": "最小 PG 数量",
        "type": "integer"
      },
      "pool": {
        "description": "Ceph 分配的数字池 ID。",
        "title": "ID",
        "type": "integer"
      },
      "pool_name": {
        "description": "操作人员可见的池名称。",
        "title": "名称",
        "type": "string"
      },
      "size": {
        "description": "复制因子（对象副本的目标数量）。",
        "title": "大小",
        "type": "integer"
      },
      "target_size": {
        "description": "操作人员提供的目标字节大小；为 pg_autoscaler 提供提示。",
        "optional": 1,
        "title": "PG 自动扩缩目标大小",
        "type": "integer"
      },
      "target_size_ratio": {
        "description": "操作人员提供的占池总容量的目标比例；为 pg_autoscaler 提供提示。",
        "optional": 1,
        "title": "PG 自动扩缩目标比例",
        "type": "number"
      },
      "type": {
        "description": "池类型：'replicated' 表示 n 路复制，'erasure' 表示纠删码池，'unknown' 表示 PVE 尚未映射的类型。",
        "enum": [
          "replicated",
          "erasure",
          "unknown"
        ],
        "title": "类型",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{pool_name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/nodes/{node}/ceph/pool`

创建 Ceph 池

**方法标识：** `createpool`

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
| `add_storages` | boolean | 否 | 0 | 使用新池配置虚拟机和容器存储。复制池默认为 false，纠删码池默认为 true（因为 EC 池通常只有连接到存储后才有用）。 |
| `application` | string | 否 | "rbd" | 池的应用。；可选值：`rbd`, `cephfs`, `rgw` |
| `crush_rule` | string | 否 | — | 用于映射集群中对象放置位置的规则。 |
| `erasure-coding` | string | 否 | — | 为 RBD 创建纠删码池，并附带用于存储元数据的复制池。使用 EC 时，常用 ceph 选项 'size'、'min_size' 和 'crush_rule' 参数将应用于元数据池。 |
| `min_size` | integer | 否 | 2 | 每个对象的最小副本数 |
| `name` | string | 是 | — | 池名称。必须唯一。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `pg_autoscale_mode` | string | 否 | "warn" | 池的自动 PG 扩缩模式。；可选值：`on`, `off`, `warn` |
| `pg_num` | integer | 否 | 128 | 归置组数量。 |
| `pg_num_min` | integer | 否 | — | 最小归置组数量。 |
| `size` | integer | 否 | 3 | 每个对象的副本数 |
| `target_size` | string | 否 | — | PG 自动扩缩器使用的池预估目标大小。 |
| `target_size_ratio` | number | 否 | — | PG 自动扩缩器使用的池预估目标比例。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storages": {
      "default": 0,
      "description": "使用新池配置虚拟机和容器存储。复制池默认为 false，纠删码池默认为 true（因为 EC 池通常只有连接到存储后才有用）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
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
    "crush_rule": {
      "description": "用于映射集群中对象放置位置的规则。",
      "optional": 1,
      "title": "CRUSH 规则名称",
      "type": "string",
      "typetext": "<string>"
    },
    "erasure-coding": {
      "description": "为 RBD 创建纠删码池，并附带用于存储元数据的复制池。使用 EC 时，常用 ceph 选项 'size'、'min_size' 和 'crush_rule' 参数将应用于元数据池。",
      "format": {
        "device-class": {
          "description": "CRUSH 设备类别。将创建纠删码池及用于元数据的复制池。",
          "format_description": "class",
          "optional": 1,
          "type": "string"
        },
        "failure-domain": {
          "default": "host",
          "description": "CRUSH 故障域。默认为 'host'。将创建纠删码池及用于元数据的复制池。",
          "format_description": "domain",
          "optional": 1,
          "type": "string"
        },
        "k": {
          "description": "数据块数量。将创建纠删码池及用于元数据的复制池。",
          "minimum": 2,
          "type": "integer"
        },
        "m": {
          "description": "编码块数量。将创建纠删码池及用于元数据的复制池。",
          "minimum": 1,
          "type": "integer"
        },
        "profile": {
          "description": "覆盖要使用的纠删码（EC）配置文件。将创建纠删码池及用于元数据的复制池。",
          "format_description": "profile",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "k=<integer> ,m=<integer> [,device-class=<class>] [,failure-domain=<domain>] [,profile=<profile>]"
    },
    "min_size": {
      "default": 2,
      "description": "每个对象的最小副本数",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "title": "最小大小",
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
    },
    "name": {
      "description": "池名称。必须唯一。",
      "pattern": "(?^:^[^:/\\s]+$)",
      "title": "名称",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
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
      "type": "integer",
      "typetext": "<integer> (1 - 32768)"
    },
    "pg_num_min": {
      "description": "最小归置组数量。",
      "maximum": 32768,
      "optional": 1,
      "title": "最小 PG 数量",
      "type": "integer",
      "typetext": "<integer> (-N - 32768)"
    },
    "size": {
      "default": 3,
      "description": "每个对象的副本数",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "title": "大小",
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
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
      "type": "number",
      "typetext": "<number>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/pool)。
