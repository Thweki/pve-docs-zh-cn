# `/nodes/{node}/services`

原始接口路径：`/nodes/{node}/services`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/services`

Service list.

**方法标识：** `index`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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
      "active-state": {
        "description": "Current state of the service process (systemd ActiveState).",
        "enum": [
          "active",
          "inactive",
          "failed",
          "activating",
          "deactivating",
          "maintenance",
          "reloading",
          "refreshing",
          "unknown"
        ],
        "type": "string"
      },
      "desc": {
        "description": "Description of the service.",
        "type": "string"
      },
      "name": {
        "description": "Short identifier for the service (e.g., \"pveproxy\").",
        "type": "string"
      },
      "service": {
        "description": "Systemd unit name (e.g., pveproxy).",
        "type": "string"
      },
      "state": {
        "description": "Execution status of the service (systemd SubState).",
        "enum": [
          "dead",
          "condition",
          "start-pre",
          "start",
          "start-post",
          "running",
          "exited",
          "reload",
          "reload-signal",
          "reload-notify",
          "mounting",
          "stop",
          "stop-watchdog",
          "stop-sigterm",
          "stop-sigkill",
          "stop-post",
          "final-watchdog",
          "final-sigterm",
          "final-sigkill",
          "failed",
          "dead-before-auto-restart",
          "failed-before-auto-restart",
          "dead-resources-pinned",
          "auto-restart",
          "auto-restart-queued",
          "cleaning",
          "unknown"
        ],
        "type": "string"
      },
      "unit-state": {
        "description": "Whether the service is enabled (systemd UnitFileState).",
        "enum": [
          "enabled",
          "enabled-runtime",
          "linked",
          "linked-runtime",
          "alias",
          "masked",
          "masked-runtime",
          "static",
          "disabled",
          "indirect",
          "generated",
          "transient",
          "bad",
          "not-found",
          "unknown"
        ],
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{service}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/services)。
