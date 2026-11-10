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
| `type` | string | 否 | — | Only list resources of specific type；可选值：`ct`, `vm` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "Only list resources of specific type",
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
| `auto-rebalance` | boolean | 否 | 1 | HA resource may be migrated during automatic rebalancing |
| `comment` | string | 否 | — | Description. |
| `failback` | boolean | 否 | 1 | Automatically migrate HA resource to the node with the highest priority according to their node affinity rules, if a node with a higher priority than the current node comes online. |
| `group` | string | 否 | — | The HA group identifier. |
| `max_relocate` | integer | 否 | 1 | Maximal number of resource relocate tries when a resource fails to start. |
| `max_restart` | integer | 否 | 1 | Maximal number of tries to restart the resource on a node after its start failed. When reached, the HA manager will try to relocate the resource to an eligible node. |
| `sid` | string | 是 | — | HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100). |
| `state` | string | 否 | "started" | Requested resource state. The CRM reads this state and acts accordingly.<br>Please note that `enabled` is just an alias for `started`.<br><br>`started`;;<br><br>The CRM tries to start the resource. Service state is<br>set to `started` after successful start. On node failures, or when start<br>fails, it tries to recover the resource. If everything fails, service<br>state it set to `error`.<br><br>`stopped`;;<br><br>The CRM tries to keep the resource in `stopped` state, but it<br>still tries to relocate the resources on node failures.<br><br>`disabled`;;<br><br>The CRM tries to put the resource in `stopped` state, but does not try<br>to relocate the resources on node failures. The main purpose of this<br>state is error recovery, because it is the only way to move a resource out<br>of the `error` state.<br><br>`ignored`;;<br><br>The resource gets removed from the manager status and so the CRM and the LRM do<br>not touch the resource anymore. All {pve} API calls affecting this resource<br>will be executed, directly bypassing the HA stack. CRM commands will be thrown<br>away while the resource is in this state. The resource will not get relocated<br>on node failures.<br><br>；可选值：`started`, `stopped`, `enabled`, `disabled`, `ignored` |
| `type` | string | 否 | — | Resource type.；可选值：`ct`, `vm` |

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
      "verbose_description": "Requested resource state. The CRM reads this state and acts accordingly.\nPlease note that `enabled` is just an alias for `started`.\n\n`started`;;\n\nThe CRM tries to start the resource. Service state is\nset to `started` after successful start. On node failures, or when start\nfails, it tries to recover the resource. If everything fails, service\nstate it set to `error`.\n\n`stopped`;;\n\nThe CRM tries to keep the resource in `stopped` state, but it\nstill tries to relocate the resources on node failures.\n\n`disabled`;;\n\nThe CRM tries to put the resource in `stopped` state, but does not try\nto relocate the resources on node failures. The main purpose of this\nstate is error recovery, because it is the only way to move a resource out\nof the `error` state.\n\n`ignored`;;\n\nThe resource gets removed from the manager status and so the CRM and the LRM do\nnot touch the resource anymore. All {pve} API calls affecting this resource\nwill be executed, directly bypassing the HA stack. CRM commands will be thrown\naway while the resource is in this state. The resource will not get relocated\non node failures.\n\n"
    },
    "type": {
      "description": "Resource type.",
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
