# `/cluster/ha/resources/{sid}`

原始接口路径：`/cluster/ha/resources/{sid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/ha/resources/{sid}`

删除资源配置。

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
| `purge` | boolean | 否 | 1 | Remove this resource from rules that reference it, deleting the rule if this resource is the only resource in the rule |
| `sid` | string | 是 | — | HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "purge": {
      "default": 1,
      "description": "Remove this resource from rules that reference it, deleting the rule if this resource is the only resource in the rule",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "sid": {
      "description": "HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100).",
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

Read resource configuration.

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
| `sid` | string | 是 | — | HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "sid": {
      "description": "HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100).",
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
      "description": "HA resource may be migrated during automatic rebalancing.",
      "optional": 1,
      "type": "boolean"
    },
    "comment": {
      "description": "Description.",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Can be used to prevent concurrent modifications.",
      "type": "string"
    },
    "failback": {
      "default": 1,
      "description": "The HA resource is automatically migrated to the node with the highest priority according to their node affinity rule, if a node with a higher priority than the current node comes online.",
      "optional": 1,
      "type": "boolean"
    },
    "group": {
      "description": "The HA group identifier.",
      "format": "pve-configid",
      "optional": 1,
      "type": "string"
    },
    "max_relocate": {
      "description": "Maximal number of service relocate tries when a service fails to start.",
      "optional": 1,
      "type": "integer"
    },
    "max_restart": {
      "description": "Maximal number of tries to restart the service on a node after its start failed.",
      "optional": 1,
      "type": "integer"
    },
    "sid": {
      "description": "HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100).",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    },
    "state": {
      "description": "Requested resource state.",
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
      "description": "The type of the resources.",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/ha/resources/{sid}`

更新资源配置。

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
| `auto-rebalance` | boolean | 否 | 1 | HA resource may be migrated during automatic rebalancing |
| `comment` | string | 否 | — | Description. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `failback` | boolean | 否 | 1 | Automatically migrate HA resource to the node with the highest priority according to their node affinity rules, if a node with a higher priority than the current node comes online. |
| `group` | string | 否 | — | The HA group identifier. |
| `max_relocate` | integer | 否 | 1 | Maximal number of resource relocate tries when a resource fails to start. |
| `max_restart` | integer | 否 | 1 | Maximal number of tries to restart the resource on a node after its start failed. When reached, the HA manager will try to relocate the resource to an eligible node. |
| `sid` | string | 是 | — | HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100). |
| `state` | string | 否 | "started" | Requested resource state.；可选值：`started`, `stopped`, `enabled`, `disabled`, `ignored` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "auto-rebalance": {
      "default": 1,
      "description": "HA resource may be migrated during automatic rebalancing",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "comment": {
      "description": "Description.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "failback": {
      "default": 1,
      "description": "Automatically migrate HA resource to the node with the highest priority according to their node affinity rules, if a node with a higher priority than the current node comes online.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "group": {
      "description": "The HA group identifier.",
      "format": "pve-configid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "max_relocate": {
      "default": 1,
      "description": "Maximal number of resource relocate tries when a resource fails to start.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "max_restart": {
      "default": 1,
      "description": "Maximal number of tries to restart the resource on a node after its start failed. When reached, the HA manager will try to relocate the resource to an eligible node.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "sid": {
      "description": "HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100).",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    },
    "state": {
      "default": "started",
      "description": "Requested resource state.",
      "enum": [
        "started",
        "stopped",
        "enabled",
        "disabled",
        "ignored"
      ],
      "optional": 1,
      "type": "string",
      "verbose_description": "Requested resource state. The CRM reads this state and acts accordingly.\nPlease note that `enabled` is just an alias for `started`.\n\n`started`;;\n\nThe CRM tries to start the resource. Service state is\nset to `started` after successful start. On node failures, or when start\nfails, it tries to recover the resource.  If everything fails, service\nstate it set to `error`.\n\n`stopped`;;\n\nThe CRM tries to keep the resource in `stopped` state, but it\nstill tries to relocate the resources on node failures.\n\n`disabled`;;\n\nThe CRM tries to put the resource in `stopped` state, but does not try\nto relocate the resources on node failures. The main purpose of this\nstate is error recovery, because it is the only way to move a resource out\nof the `error` state.\n\n`ignored`;;\n\nThe resource gets removed from the manager status and so the CRM and the LRM do\nnot touch the resource anymore. All {pve} API calls affecting this resource\nwill be executed, directly bypassing the HA stack. CRM commands will be thrown\naway while the resource is in this state. The resource will not get relocated\non node failures.\n\n"
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
