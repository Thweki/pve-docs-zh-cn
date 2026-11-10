# `/cluster/ha/resources`

原始接口路径：`/cluster/ha/resources`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ha/resources`

列出 HA 资源。

**方法标识：** `index`

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
| `type` | string | 否 | — | 仅列出特定类型的资源；可选值：`ct`, `vm` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "仅列出特定类型的资源",
      "enum": [
        "ct",
        "vm"
      ],
      "optional": 1,
      "type": "string"
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
      "sid": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{sid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/ha/resources`

创建新的 HA 资源。

**方法标识：** `create`

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
| `failback` | boolean | 否 | 1 | 如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。 |
| `group` | string | 否 | — | HA 组标识符。 |
| `max_relocate` | integer | 否 | 1 | 资源启动失败时尝试重新安置资源的最大次数。 |
| `max_restart` | integer | 否 | 1 | 资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。 |
| `sid` | string | 是 | — | HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |
| `state` | string | 否 | "started" | 请求的资源状态。CRM 读取此状态并据此采取操作。<br>请注意，`enabled` 只是 `started` 的别名。<br><br>`started`;;<br><br>CRM 尝试启动资源。服务状态<br>在成功启动后设为 `started`。发生节点故障或启动<br>失败时，它会尝试恢复资源。  如果所有尝试均失败，服务<br>状态将设为 `error`。<br><br>`stopped`;;<br><br>CRM 尝试使资源保持 `stopped` 状态，但<br>在节点故障时仍会尝试重新安置资源。<br><br>`disabled`;;<br><br>CRM 尝试将资源置于 `stopped` 状态，但不会尝试<br>在节点故障时重新安置资源。此<br>状态主要用于错误恢复，因为这是使资源脱离<br>`error` 状态的唯一方式。<br><br>`ignored`;;<br><br>资源会从管理器状态中移除，因此 CRM 和 LRM 将<br>不再操作此资源。所有影响此资源的 {pve} API 调用<br>都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢<br>弃。发生节点故障时，此资源不会被重新安置<br>。<br><br>；可选值：`started`, `stopped`, `enabled`, `disabled`, `ignored` |
| `type` | string | 否 | — | 资源类型。；可选值：`ct`, `vm` |

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
    },
    "type": {
      "description": "资源类型。",
      "enum": [
        "ct",
        "vm"
      ],
      "optional": 1,
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources)。
