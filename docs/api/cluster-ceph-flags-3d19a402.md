# `/cluster/ceph/flags`

原始接口路径：`/cluster/ceph/flags`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/flags`

get the status of all ceph flags

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "additionalProperties": 1,
    "properties": {
      "description": {
        "description": "Flag description.",
        "type": "string"
      },
      "name": {
        "description": "Flag name.",
        "enum": [
          "nobackfill",
          "nodeep-scrub",
          "nodown",
          "noin",
          "noout",
          "norebalance",
          "norecover",
          "noscrub",
          "notieragent",
          "noup",
          "pause"
        ],
        "type": "string"
      },
      "value": {
        "description": "Flag value.",
        "type": "boolean"
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

## PUT `/cluster/ceph/flags`

Set/Unset multiple Ceph flags at once. Each flag is a top-level optional boolean: passing true sets the flag, false unsets it, omitting it leaves the current state untouched. Runs as a worker task; returns a UPID to follow.

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `nobackfill` | boolean | 否 | — | Backfilling of PGs is suspended. |
| `nodeep-scrub` | boolean | 否 | — | Deep Scrubbing is disabled. |
| `nodown` | boolean | 否 | — | OSD failure reports are being ignored, such that the monitors will not mark OSDs down. |
| `noin` | boolean | 否 | — | OSDs that were previously marked out will not be marked back in when they start. |
| `noout` | boolean | 否 | — | OSDs will not automatically be marked out after the configured interval. |
| `norebalance` | boolean | 否 | — | Rebalancing of PGs is suspended. |
| `norecover` | boolean | 否 | — | Recovery of PGs is suspended. |
| `noscrub` | boolean | 否 | — | Scrubbing is disabled. |
| `notieragent` | boolean | 否 | — | Cache tiering activity is suspended. |
| `noup` | boolean | 否 | — | OSDs are not allowed to start. |
| `pause` | boolean | 否 | — | Pauses read and writes. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "nobackfill": {
      "description": "Backfilling of PGs is suspended.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nodeep-scrub": {
      "description": "Deep Scrubbing is disabled.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nodown": {
      "description": "OSD failure reports are being ignored, such that the monitors will not mark OSDs down.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noin": {
      "description": "OSDs that were previously marked out will not be marked back in when they start.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noout": {
      "description": "OSDs will not automatically be marked out after the configured interval.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "norebalance": {
      "description": "Rebalancing of PGs is suspended.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "norecover": {
      "description": "Recovery of PGs is suspended.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noscrub": {
      "description": "Scrubbing is disabled.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "notieragent": {
      "description": "Cache tiering activity is suspended.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noup": {
      "description": "OSDs are not allowed to start.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "pause": {
      "description": "Pauses read and writes.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/flags)。
