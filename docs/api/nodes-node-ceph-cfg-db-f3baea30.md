# `/nodes/{node}/ceph/cfg/db`

原始接口路径：`/nodes/{node}/ceph/cfg/db`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/cfg/db`

Get the Ceph configuration database.

**方法标识：** `db`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Datastore.Audit"
    ],
    "any",
    1
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
    "additionalProperties": 1,
    "properties": {
      "can_update_at_runtime": {
        "description": "Set if the value can be changed at runtime without restarting the affected daemons. Emitted as the integer 1/0 to match the existing PVE wire convention.",
        "type": "boolean"
      },
      "level": {
        "description": "Config level the entry is exposed at: 'basic' for operator-visible settings, 'advanced' for tuning parameters, 'dev' for developer-only knobs.",
        "enum": [
          "basic",
          "advanced",
          "dev"
        ],
        "type": "string"
      },
      "mask": {
        "description": "Match expression restricting the entry's scope; empty when the entry has no mask. Examples: 'host:foo', 'class:ssd'.",
        "type": "string"
      },
      "name": {
        "description": "Config key name.",
        "type": "string"
      },
      "section": {
        "description": "Ceph config section the entry applies to: 'global', a daemon type ('mon', 'osd', 'mgr', 'mds', 'client'), or a specific daemon (e.g. 'osd.0', 'mon.<name>').",
        "type": "string"
      },
      "value": {
        "description": "Configured value for the key (always serialised as a string by Ceph, regardless of the option's underlying type).",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/cfg/db)。
