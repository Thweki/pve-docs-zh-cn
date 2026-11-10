# `/nodes/{node}/ceph/pool/{name}`

原始接口路径：`/nodes/{node}/ceph/pool/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/pool/{name}`

Destroy pool

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
| `force` | boolean | 否 | 0 | If true, destroys pool even if in use |
| `name` | string | 是 | — | The name of the pool. It must be unique. |
| `node` | string | 是 | — | The cluster node name. |
| `remove_ecprofile` | boolean | 否 | 1 | Remove the erasure code profile. Defaults to true, if applicable. |
| `remove_storages` | boolean | 否 | 0 | Remove all pveceph-managed storages configured for this pool |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "If true, destroys pool even if in use",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "The name of the pool. It must be unique.",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "remove_ecprofile": {
      "default": 1,
      "description": "Remove the erasure code profile. Defaults to true, if applicable.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "remove_storages": {
      "default": 0,
      "description": "Remove all pveceph-managed storages configured for this pool",
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

Pool index.

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
| `name` | string | 是 | — | The name of the pool. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "The name of the pool.",
      "type": "string",
      "typetext": "<string>"
    },
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

Change POOL settings

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
| `application` | string | 否 | — | The application of the pool.；可选值：`rbd`, `cephfs`, `rgw` |
| `crush_rule` | string | 否 | — | The rule to use for mapping object placement in the cluster. |
| `min_size` | integer | 否 | — | Minimum number of replicas per object |
| `name` | string | 是 | — | The name of the pool. It must be unique. |
| `node` | string | 是 | — | The cluster node name. |
| `pg_autoscale_mode` | string | 否 | — | The automatic PG scaling mode of the pool.；可选值：`on`, `off`, `warn` |
| `pg_num` | integer | 否 | — | Number of placement groups. |
| `pg_num_min` | integer | 否 | — | Minimal number of placement groups. |
| `size` | integer | 否 | — | Number of replicas per object |
| `target_size` | string | 否 | — | The estimated target size of the pool for the PG autoscaler. |
| `target_size_ratio` | number | 否 | — | The estimated target ratio of the pool for the PG autoscaler. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "application": {
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
    "min_size": {
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/pool/{name})。
