# `/cluster/ha/resources/{sid}`

原始接口路径：`/cluster/ha/resources/{sid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/ha/resources/{sid}`

删除资源配置。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Console"
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
| `purge` | boolean | 否 | 1 | 从引用此资源的规则中移除此资源；如果此资源是规则中的唯一资源，则删除该规则 |
| `sid` | string | 是 | — | HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "purge": {
      "default": 1,
      "description": "从引用此资源的规则中移除此资源；如果此资源是规则中的唯一资源，则删除该规则",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## GET `/cluster/ha/resources/{sid}`

读取资源配置。

**方法标识：** `read`

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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `sid` | string | 是 | — | HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "auto-rebalance": {
      "default": 1,
      "description": "HA 资源可以在自动重新均衡期间迁移。",
      "optional": 1,
      "type": "boolean"
    },
    "comment": {
      "description": "描述。",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "可用于防止并发修改。",
      "type": "string"
    },
    "failback": {
      "default": 1,
      "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性规则，将 HA 资源自动迁移到优先级最高的节点。",
      "optional": 1,
      "type": "boolean"
    },
    "group": {
      "description": "HA 组标识符。",
      "format": "pve-configid",
      "optional": 1,
      "type": "string"
    },
    "max_relocate": {
      "description": "服务启动失败时尝试重新安置服务的最大次数。",
      "optional": 1,
      "type": "integer"
    },
    "max_restart": {
      "description": "服务启动失败后在节点上尝试重新启动服务的最大次数。",
      "optional": 1,
      "type": "integer"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    },
    "state": {
      "description": "请求的资源状态。",
      "enum": [
        "started",
        "stopped",
        "enabled",
        "disabled",
        "ignored"
      ],
      "optional": 1,
      "type": "string"
    },
    "type": {
      "description": "资源类型。",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/ha/resources/{sid}`

更新资源配置。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Console"
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
| `auto-rebalance` | boolean | 否 | 1 | HA 资源可以在自动重新均衡期间迁移 |
| `comment` | string | 否 | — | 描述。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `failback` | boolean | 否 | 1 | 如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。 |
| `group` | string | 否 | — | HA 组标识符。 |
| `max_relocate` | integer | 否 | 1 | 资源启动失败时尝试重新安置资源的最大次数。 |
| `max_restart` | integer | 否 | 1 | 资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。 |
| `sid` | string | 是 | — | HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |
| `state` | string | 否 | "started" | 请求的资源状态。CRM 读取此状态并据此采取操作。<br>请注意，`enabled` 只是 `started` 的别名。<br><br>`started`;;<br><br>CRM 尝试启动资源。服务状态<br>在成功启动后设为 `started`。发生节点故障或启动<br>失败时，它会尝试恢复资源。  如果所有尝试均失败，服务<br>状态将设为 `error`。<br><br>`stopped`;;<br><br>CRM 尝试使资源保持 `stopped` 状态，但<br>在节点故障时仍会尝试重新安置资源。<br><br>`disabled`;;<br><br>CRM 尝试将资源置于 `stopped` 状态，但不会尝试<br>在节点故障时重新安置资源。此<br>状态主要用于错误恢复，因为这是使资源脱离<br>`error` 状态的唯一方式。<br><br>`ignored`;;<br><br>资源会从管理器状态中移除，因此 CRM 和 LRM 将<br>不再操作此资源。所有影响此资源的 {pve} API 调用<br>都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢<br>弃。发生节点故障时，此资源不会被重新安置<br>。<br><br>；可选值：`started`, `stopped`, `enabled`, `disabled`, `ignored` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "auto-rebalance": {
      "default": 1,
      "description": "HA 资源可以在自动重新均衡期间迁移",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "comment": {
      "description": "描述。",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "failback": {
      "default": 1,
      "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "group": {
      "description": "HA 组标识符。",
      "format": "pve-configid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "max_relocate": {
      "default": 1,
      "description": "资源启动失败时尝试重新安置资源的最大次数。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "max_restart": {
      "default": 1,
      "description": "资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    },
    "state": {
      "default": "started",
      "description": "请求的资源状态。",
      "enum": [
        "started",
        "stopped",
        "enabled",
        "disabled",
        "ignored"
      ],
      "optional": 1,
      "type": "string",
      "verbose_description": "请求的资源状态。CRM 读取此状态并据此采取操作。\n请注意，`enabled` 只是 `started` 的别名。\n\n`started`;;\n\nCRM 尝试启动资源。服务状态\n在成功启动后设为 `started`。发生节点故障或启动\n失败时，它会尝试恢复资源。  如果所有尝试均失败，服务\n状态将设为 `error`。\n\n`stopped`;;\n\nCRM 尝试使资源保持 `stopped` 状态，但\n在节点故障时仍会尝试重新安置资源。\n\n`disabled`;;\n\nCRM 尝试将资源置于 `stopped` 状态，但不会尝试\n在节点故障时重新安置资源。此\n状态主要用于错误恢复，因为这是使资源脱离\n`error` 状态的唯一方式。\n\n`ignored`;;\n\n资源会从管理器状态中移除，因此 CRM 和 LRM 将\n不再操作此资源。所有影响此资源的 {pve} API 调用\n都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢\n弃。发生节点故障时，此资源不会被重新安置\n。\n\n"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources/{sid})。
