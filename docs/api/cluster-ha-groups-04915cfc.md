# `/cluster/ha/groups`

原始接口路径：`/cluster/ha/groups`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ha/groups`

获取 HA 组。（已弃用，建议使用 HA 规则）

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
      "group": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{group}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/ha/groups`

创建新的 HA 组。（已弃用，建议使用 HA 规则）

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
| `comment` | string | 否 | — | Description. |
| `group` | string | 是 | — | The HA group identifier. |
| `nodes` | string | 是 | — | List of cluster node names with optional priority. |
| `nofailback` | boolean | 否 | 0 | The CRM tries to run services on the node with the highest priority. If a node with higher priority comes online, the CRM migrates the service to that node. Enabling nofailback prevents that behavior. |
| `restricted` | boolean | 否 | 0 | Resources bound to restricted groups may only run on nodes defined by the group. |
| `type` | string | 否 | — | Group type.；可选值：`group` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "Description.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group": {
      "description": "The HA group identifier.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "nodes": {
      "description": "List of cluster node names with optional priority.",
      "format": "pve-ha-node-list",
      "optional": 0,
      "type": "string",
      "typetext": "<node>[:<pri>]{,<node>[:<pri>]}*",
      "verbose_description": "List of cluster node members, where a priority can be given to each node. A resource will run on the available nodes with the highest priority. If there are more nodes in the highest priority class, the resources will get distributed to those nodes. The priorities have a relative meaning only. The higher the number, the higher the priority."
    },
    "nofailback": {
      "default": 0,
      "description": "The CRM tries to run services on the node with the highest priority. If a node with higher priority comes online, the CRM migrates the service to that node. Enabling nofailback prevents that behavior.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "restricted": {
      "default": 0,
      "description": "Resources bound to restricted groups may only run on nodes defined by the group.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>",
      "verbose_description": "Resources bound to restricted groups may only run on nodes defined by the group. The resource will be placed in the stopped state if no group node member is online. Resources on unrestricted groups may run on any cluster node if all group members are offline, but they will migrate back as soon as a group member comes online. One can implement a 'preferred node' behavior using an unrestricted group with only one member."
    },
    "type": {
      "description": "Group type.",
      "enum": [
        "group"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/groups)。
