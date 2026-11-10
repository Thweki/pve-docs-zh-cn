# `/cluster/ha/status/current`

原始接口路径：`/cluster/ha/status/current`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ha/status/current`

Get HA manager status.

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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "armed-state": {
        "description": "For type 'fencing'. Whether HA is armed, on standby, disarming or disarmed.",
        "enum": [
          "armed",
          "standby",
          "disarming",
          "disarmed"
        ],
        "optional": 1,
        "type": "string"
      },
      "auto-rebalance": {
        "default": 1,
        "description": "HA resource may be migrated during automatic rebalancing.",
        "optional": 1,
        "type": "boolean"
      },
      "crm_state": {
        "description": "For type 'service'. Service state as seen by the CRM.",
        "optional": 1,
        "type": "string"
      },
      "failback": {
        "default": 1,
        "description": "The HA resource is automatically migrated to the node with the highest priority according to their node affinity rule, if a node with a higher priority than the current node comes online.",
        "optional": 1,
        "type": "boolean"
      },
      "id": {
        "description": "Status entry ID (quorum, master, lrm:<node>, service:<sid>).",
        "type": "string"
      },
      "max_relocate": {
        "description": "For type 'service'.",
        "optional": 1,
        "type": "integer"
      },
      "max_restart": {
        "description": "For type 'service'.",
        "optional": 1,
        "type": "integer"
      },
      "node": {
        "description": "Node associated to status entry.",
        "type": "string"
      },
      "quorate": {
        "description": "For type 'quorum'. Whether the cluster is quorate or not.",
        "optional": 1,
        "type": "boolean"
      },
      "request_state": {
        "description": "For type 'service'. Requested service state.",
        "optional": 1,
        "type": "string"
      },
      "resource_mode": {
        "description": "For type 'fencing'. How resources are handled while disarmed.",
        "enum": [
          "freeze",
          "ignore"
        ],
        "optional": 1,
        "type": "string"
      },
      "sid": {
        "description": "For type 'service'. Service ID.",
        "optional": 1,
        "type": "string"
      },
      "state": {
        "description": "For type 'service'. Verbose service state.",
        "optional": 1,
        "type": "string"
      },
      "status": {
        "description": "Status of the entry (value depends on type).",
        "type": "string"
      },
      "timestamp": {
        "description": "For type 'lrm','master'. Timestamp of the status information.",
        "optional": 1,
        "type": "integer"
      },
      "type": {
        "description": "Type of status entry.",
        "enum": [
          "quorum",
          "master",
          "lrm",
          "service",
          "fencing"
        ]
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/current)。
