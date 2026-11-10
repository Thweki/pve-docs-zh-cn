# `/nodes/{node}/ceph/pool`

原始接口路径：`/nodes/{node}/ceph/pool`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/pool`

List all pools and their settings (which are settable by the POST/PUT endpoints).

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
      "application_metadata": {
        "description": "Application tags attached to the pool (mapping of application name to its metadata object).",
        "optional": 1,
        "title": "Associated Applications",
        "type": "object"
      },
      "autoscale_status": {
        "description": "Raw pg_autoscaler status object for this pool; shape varies between Ceph releases.",
        "optional": 1,
        "title": "Autoscale Status",
        "type": "object"
      },
      "bytes_used": {
        "description": "Bytes currently used in the pool; absent if no usage statistics are reported.",
        "optional": 1,
        "renderer": "bytes",
        "title": "Used",
        "type": "integer"
      },
      "crush_rule": {
        "description": "Numeric id of the CRUSH rule used by this pool.",
        "title": "Crush Rule",
        "type": "integer"
      },
      "crush_rule_name": {
        "description": "Human-readable name of the CRUSH rule used by this pool; absent if the rule id is not in the current CRUSH map.",
        "optional": 1,
        "title": "Crush Rule Name",
        "type": "string"
      },
      "min_size": {
        "description": "Minimum number of replicas required to accept writes.",
        "title": "Min Size",
        "type": "integer"
      },
      "percent_used": {
        "description": "Percentage of pool capacity currently used; absent if no usage statistics are reported.",
        "optional": 1,
        "title": "%-Used",
        "type": "number"
      },
      "pg_autoscale_mode": {
        "description": "Placement-group autoscaler mode ('on', 'warn' or 'off').",
        "optional": 1,
        "title": "PG Autoscale Mode",
        "type": "string"
      },
      "pg_num": {
        "description": "Current placement-group count.",
        "title": "PG Num",
        "type": "integer"
      },
      "pg_num_final": {
        "description": "Optimal placement-group count computed by pg_autoscaler.",
        "optional": 1,
        "title": "Optimal PG Num",
        "type": "integer"
      },
      "pg_num_min": {
        "description": "Minimum placement-group count the pg_autoscaler may choose.",
        "optional": 1,
        "title": "min. PG Num",
        "type": "integer"
      },
      "pool": {
        "description": "Numeric pool id assigned by Ceph.",
        "title": "ID",
        "type": "integer"
      },
      "pool_name": {
        "description": "Operator-visible name of the pool.",
        "title": "Name",
        "type": "string"
      },
      "size": {
        "description": "Replication factor (target number of object replicas).",
        "title": "Size",
        "type": "integer"
      },
      "target_size": {
        "description": "Operator-supplied target size in bytes; hints the pg_autoscaler.",
        "optional": 1,
        "title": "PG Autoscale Target Size",
        "type": "integer"
      },
      "target_size_ratio": {
        "description": "Operator-supplied target ratio of total pool capacity; hints the pg_autoscaler.",
        "optional": 1,
        "title": "PG Autoscale Target Ratio",
        "type": "number"
      },
      "type": {
        "description": "Pool type: 'replicated' for n-way replication, 'erasure' for an erasure-coded pool, 'unknown' for types PVE does not yet map.",
        "enum": [
          "replicated",
          "erasure",
          "unknown"
        ],
        "title": "Type",
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

Create Ceph pool

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
| `add_storages` | boolean | 否 | 0 | Configure VM and CT storage using the new pool. Defaults to false for replicated pools and to true for erasure-coded pools (since EC pools are typically only useful when wired up to storage). |
| `application` | string | 否 | "rbd" | The application of the pool.；可选值：`rbd`, `cephfs`, `rgw` |
| `crush_rule` | string | 否 | — | The rule to use for mapping object placement in the cluster. |
| `erasure-coding` | string | 否 | — | Create an erasure coded pool for RBD with an accompaning replicated pool for metadata storage. With EC, the common ceph options 'size', 'min_size' and 'crush_rule' parameters will be applied to the metadata pool. |
| `min_size` | integer | 否 | 2 | Minimum number of replicas per object |
| `name` | string | 是 | — | The name of the pool. It must be unique. |
| `node` | string | 是 | — | The cluster node name. |
| `pg_autoscale_mode` | string | 否 | "warn" | The automatic PG scaling mode of the pool.；可选值：`on`, `off`, `warn` |
| `pg_num` | integer | 否 | 128 | Number of placement groups. |
| `pg_num_min` | integer | 否 | — | Minimal number of placement groups. |
| `size` | integer | 否 | 3 | Number of replicas per object |
| `target_size` | string | 否 | — | The estimated target size of the pool for the PG autoscaler. |
| `target_size_ratio` | number | 否 | — | The estimated target ratio of the pool for the PG autoscaler. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storages": {
      "default": 0,
      "description": "Configure VM and CT storage using the new pool. Defaults to false for replicated pools and to true for erasure-coded pools (since EC pools are typically only useful when wired up to storage).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "application": {
      "default": "rbd",
      "description": "The application of the pool.",
      "enum": [
        "rbd",
        "cephfs",
        "rgw"
      ],
      "optional": 1,
      "title": "Application",
      "type": "string"
    },
    "crush_rule": {
      "description": "The rule to use for mapping object placement in the cluster.",
      "optional": 1,
      "title": "Crush Rule Name",
      "type": "string",
      "typetext": "<string>"
    },
    "erasure-coding": {
      "description": "Create an erasure coded pool for RBD with an accompaning replicated pool for metadata storage. With EC, the common ceph options 'size', 'min_size' and 'crush_rule' parameters will be applied to the metadata pool.",
      "format": {
        "device-class": {
          "description": "CRUSH device class. Will create an erasure coded pool plus a replicated pool for metadata.",
          "format_description": "class",
          "optional": 1,
          "type": "string"
        },
        "failure-domain": {
          "default": "host",
          "description": "CRUSH failure domain. Default is 'host'. Will create an erasure coded pool plus a replicated pool for metadata.",
          "format_description": "domain",
          "optional": 1,
          "type": "string"
        },
        "k": {
          "description": "Number of data chunks. Will create an erasure coded pool plus a replicated pool for metadata.",
          "minimum": 2,
          "type": "integer"
        },
        "m": {
          "description": "Number of coding chunks. Will create an erasure coded pool plus a replicated pool for metadata.",
          "minimum": 1,
          "type": "integer"
        },
        "profile": {
          "description": "Override the erasure code (EC) profile to use. Will create an erasure coded pool plus a replicated pool for metadata.",
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
      "description": "Minimum number of replicas per object",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "title": "Min Size",
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
    },
    "name": {
      "description": "The name of the pool. It must be unique.",
      "pattern": "(?^:^[^:/\\s]+$)",
      "title": "Name",
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pg_autoscale_mode": {
      "default": "warn",
      "description": "The automatic PG scaling mode of the pool.",
      "enum": [
        "on",
        "off",
        "warn"
      ],
      "optional": 1,
      "title": "PG Autoscale Mode",
      "type": "string"
    },
    "pg_num": {
      "default": 128,
      "description": "Number of placement groups.",
      "maximum": 32768,
      "minimum": 1,
      "optional": 1,
      "title": "PG Num",
      "type": "integer",
      "typetext": "<integer> (1 - 32768)"
    },
    "pg_num_min": {
      "description": "Minimal number of placement groups.",
      "maximum": 32768,
      "optional": 1,
      "title": "min. PG Num",
      "type": "integer",
      "typetext": "<integer> (-N - 32768)"
    },
    "size": {
      "default": 3,
      "description": "Number of replicas per object",
      "maximum": 7,
      "minimum": 1,
      "optional": 1,
      "title": "Size",
      "type": "integer",
      "typetext": "<integer> (1 - 7)"
    },
    "target_size": {
      "description": "The estimated target size of the pool for the PG autoscaler.",
      "optional": 1,
      "pattern": "^(\\d+(\\.\\d+)?)([KMGT])?$",
      "title": "PG Autoscale Target Size",
      "type": "string"
    },
    "target_size_ratio": {
      "description": "The estimated target ratio of the pool for the PG autoscaler.",
      "optional": 1,
      "title": "PG Autoscale Target Ratio",
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
