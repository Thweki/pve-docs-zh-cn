# `/nodes/{node}/ceph/cfg/db`

原始接口路径：`/nodes/{node}/ceph/cfg/db`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/cfg/db`

获取 Ceph 配置数据库。

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
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
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
        "description": "如果可在运行时更改该值而不重启受影响的守护进程，则设置此项。以整数 1/0 输出，以符合现有 PVE 传输约定。",
        "type": "boolean"
      },
      "level": {
        "description": "条目公开的配置级别：'basic' 为操作人员可见的设置，'advanced' 为调优参数，'dev' 为仅供开发人员使用的选项。",
        "enum": [
          "basic",
          "advanced",
          "dev"
        ],
        "type": "string"
      },
      "mask": {
        "description": "限制条目作用域的匹配表达式；条目没有掩码时为空。例如：'host:foo'、'class:ssd'。",
        "type": "string"
      },
      "name": {
        "description": "配置键名。",
        "type": "string"
      },
      "section": {
        "description": "条目适用的 Ceph 配置节：'global'、守护进程类型（'mon'、'osd'、'mgr'、'mds'、'client'），或特定守护进程（例如 'osd.0'、'mon.<name>'）。",
        "type": "string"
      },
      "value": {
        "description": "键的配置值（无论选项的底层类型为何，Ceph 始终将其序列化为字符串）。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/cfg/db)。
