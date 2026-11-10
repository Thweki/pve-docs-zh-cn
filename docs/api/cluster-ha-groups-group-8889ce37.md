# `/cluster/ha/groups/{group}`

原始接口路径：`/cluster/ha/groups/{group}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/ha/groups/{group}`

删除 HA 组配置。（已弃用，建议使用 HA 规则）

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
| `group` | string | 是 | — | HA 组标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "group": {
      "description": "HA 组标识符。",
      "format": "pve-configid",
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
  "type": "null"
}
```

## GET `/cluster/ha/groups/{group}`

读取 HA 组配置。（已弃用，改用 HA 规则）

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
| `group` | string | 是 | — | HA 组标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "group": {
      "description": "HA 组标识符。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{}
```

## PUT `/cluster/ha/groups/{group}`

更新 HA 组配置。（已弃用，建议使用 HA 规则）

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
| `comment` | string | 否 | — | 描述。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `group` | string | 是 | — | HA 组标识符。 |
| `nodes` | string | 否 | — | 集群节点成员列表，可为每个节点指定优先级。资源将在可用节点中优先级最高的节点上运行。如果最高优先级有多个节点，则资源将分布到这些节点上。优先级仅具有相对意义。数值越大，优先级越高。 |
| `nofailback` | boolean | 否 | 0 | CRM 尝试在优先级最高的节点上运行服务。如果更高优先级的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。 |
| `restricted` | boolean | 否 | 0 | 绑定到受限组的资源只能在该组定义的节点上运行。如果没有组成员节点在线，资源将进入停止状态。非受限组中的资源在所有组成员离线时可在任意集群节点上运行，但一旦有组成员上线就会迁回。使用仅含一个成员的非受限组，可实现“首选节点”行为。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    "group": {
      "description": "HA 组标识符。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "nodes": {
      "description": "集群节点名称列表，可选择指定优先级。",
      "format": "pve-ha-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<node>[:<pri>]{,<node>[:<pri>]}*",
      "verbose_description": "集群节点成员列表，可为每个节点指定优先级。资源将在可用节点中优先级最高的节点上运行。如果最高优先级有多个节点，则资源将分布到这些节点上。优先级仅具有相对意义。数值越大，优先级越高。"
    },
    "nofailback": {
      "default": 0,
      "description": "CRM 尝试在优先级最高的节点上运行服务。如果更高优先级的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "restricted": {
      "default": 0,
      "description": "绑定到受限组的资源只能在该组定义的节点上运行。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>",
      "verbose_description": "绑定到受限组的资源只能在该组定义的节点上运行。如果没有组成员节点在线，资源将进入停止状态。非受限组中的资源在所有组成员离线时可在任意集群节点上运行，但一旦有组成员上线就会迁回。使用仅含一个成员的非受限组，可实现“首选节点”行为。"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/groups/{group})。
