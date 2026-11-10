# `/nodes/{node}/ceph/pool/{name}`

原始接口路径：`/nodes/{node}/ceph/pool/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/pool/{name}`

销毁池

**方法标识：** `destroypool`

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
| `force` | boolean | 否 | 0 | 如果为 true，则即使池正在使用也销毁 |
| `name` | string | 是 | — | 池名称。必须唯一。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `remove_ecprofile` | boolean | 否 | 1 | 移除纠删码配置文件。如果适用，默认为 true。 |
| `remove_storages` | boolean | 否 | 0 | 移除为此池配置的所有由 pveceph 管理的存储 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "如果为 true，则即使池正在使用也销毁",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
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
    "remove_ecprofile": {
      "default": 1,
      "description": "移除纠删码配置文件。如果适用，默认为 true。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "remove_storages": {
      "default": 0,
      "description": "移除为此池配置的所有由 pveceph 管理的存储",
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
  "type": "string"
}
```

## GET `/nodes/{node}/ceph/pool/{name}`

池索引。

**方法标识：** `poolindex`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | string | 是 | — | 池名称。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "池名称。",
      "type": "string",
      "typetext": "<string>"
    },
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
    "properties": {},
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

## PUT `/nodes/{node}/ceph/pool/{name}`

更改 POOL 设置

**方法标识：** `setpool`

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
| `application` | string | 否 | — | 池的应用。；可选值：`rbd`, `cephfs`, `rgw` |
| `crush_rule` | string | 否 | — | 用于映射集群中对象放置位置的规则。 |
| `min_size` | integer | 否 | — | 每个对象的最小副本数 |
| `name` | string | 是 | — | 池名称。必须唯一。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `pg_autoscale_mode` | string | 否 | — | 池的自动 PG 扩缩模式。；可选值：`on`, `off`, `warn` |
| `pg_num` | integer | 否 | — | 归置组数量。 |
| `pg_num_min` | integer | 否 | — | 最小归置组数量。 |
| `size` | integer | 否 | — | 每个对象的副本数 |
| `target_size` | string | 否 | — | PG 自动扩缩器使用的池预估目标大小。 |
| `target_size_ratio` | number | 否 | — | PG 自动扩缩器使用的池预估目标比例。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "application": {
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
    "min_size": {
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/pool/{name})。
