# `/cluster/ceph/flags`

原始接口路径：`/cluster/ceph/flags`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/flags`

获取所有 ceph 标志的状态

**方法标识：** `get_all_flags`

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
        "description": "标志描述。",
        "type": "string"
      },
      "name": {
        "description": "标志名称。",
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
        "description": "标志值。",
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

一次设置/取消设置多个 Ceph 标志。每个标志都是顶层可选布尔值：传入 true 设置标志，false 取消设置，省略则保留当前状态。以工作任务运行；返回可用于跟踪的 UPID。

**方法标识：** `set_flags`

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
| `nobackfill` | boolean | 否 | — | 暂停 PG 回填。 |
| `nodeep-scrub` | boolean | 否 | — | 禁用深度清理检查。 |
| `nodown` | boolean | 否 | — | 忽略 OSD 故障报告，因此监视器不会将 OSD 标记为 down。 |
| `noin` | boolean | 否 | — | 先前标记为 out 的 OSD 在启动时不会重新标记为 in。 |
| `noout` | boolean | 否 | — | OSD 不会在配置的时间间隔后自动标记为 out。 |
| `norebalance` | boolean | 否 | — | 暂停 PG 重新均衡。 |
| `norecover` | boolean | 否 | — | 暂停 PG 恢复。 |
| `noscrub` | boolean | 否 | — | 禁用清理检查。 |
| `notieragent` | boolean | 否 | — | 暂停缓存分层活动。 |
| `noup` | boolean | 否 | — | 不允许 OSD 启动。 |
| `pause` | boolean | 否 | — | 暂停读写。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "nobackfill": {
      "description": "暂停 PG 回填。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nodeep-scrub": {
      "description": "禁用深度清理检查。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nodown": {
      "description": "忽略 OSD 故障报告，因此监视器不会将 OSD 标记为 down。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noin": {
      "description": "先前标记为 out 的 OSD 在启动时不会重新标记为 in。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noout": {
      "description": "OSD 不会在配置的时间间隔后自动标记为 out。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "norebalance": {
      "description": "暂停 PG 重新均衡。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "norecover": {
      "description": "暂停 PG 恢复。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noscrub": {
      "description": "禁用清理检查。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "notieragent": {
      "description": "暂停缓存分层活动。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "noup": {
      "description": "不允许 OSD 启动。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "pause": {
      "description": "暂停读写。",
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
