# `/cluster/ha/status/current`

原始接口路径：`/cluster/ha/status/current`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ha/status/current`

获取 HA 管理器状态。

**方法标识：** `status`

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
        "description": "用于 'fencing' 类型。HA 是已启用、待机、正在解除还是已解除。",
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
        "description": "HA 资源可以在自动重新均衡期间迁移。",
        "optional": 1,
        "type": "boolean"
      },
      "crm_state": {
        "description": "用于 'service' 类型。CRM 所见的服务状态。",
        "optional": 1,
        "type": "string"
      },
      "failback": {
        "default": 1,
        "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性规则，将 HA 资源自动迁移到优先级最高的节点。",
        "optional": 1,
        "type": "boolean"
      },
      "id": {
        "description": "状态条目 ID（quorum、master、lrm:<node>、service:<sid>）。",
        "type": "string"
      },
      "max_relocate": {
        "description": "用于 'service' 类型。",
        "optional": 1,
        "type": "integer"
      },
      "max_restart": {
        "description": "用于 'service' 类型。",
        "optional": 1,
        "type": "integer"
      },
      "node": {
        "description": "与状态条目关联的节点。",
        "type": "string"
      },
      "quorate": {
        "description": "用于 'quorum' 类型。集群是否达到仲裁。",
        "optional": 1,
        "type": "boolean"
      },
      "request_state": {
        "description": "用于 'service' 类型。请求的服务状态。",
        "optional": 1,
        "type": "string"
      },
      "resource_mode": {
        "description": "用于 'fencing' 类型。解除后如何处理资源。",
        "enum": [
          "freeze",
          "ignore"
        ],
        "optional": 1,
        "type": "string"
      },
      "sid": {
        "description": "用于 'service' 类型。服务 ID。",
        "optional": 1,
        "type": "string"
      },
      "state": {
        "description": "用于 'service' 类型。详细服务状态。",
        "optional": 1,
        "type": "string"
      },
      "status": {
        "description": "条目状态（值取决于类型）。",
        "type": "string"
      },
      "timestamp": {
        "description": "用于 'lrm'、'master' 类型。状态信息的时间戳。",
        "optional": 1,
        "type": "integer"
      },
      "type": {
        "description": "状态条目类型。",
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
