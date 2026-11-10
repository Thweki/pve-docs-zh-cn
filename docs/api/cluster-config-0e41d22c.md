# `/cluster/config`

原始接口路径：`/cluster/config`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/config`

目录索引。

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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {},
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/config`

生成新的集群配置。如果未提供链路，则默认将本地 IP 地址用作 link0。

**方法标识：** `create`

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
| `clustername` | string | 是 | — | 集群名称。 |
| `link[n]` | string | 否 | — | 单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7） |
| `nodeid` | integer | 否 | — | 此节点的节点 ID。 |
| `token-coefficient` | integer | 否 | 125 | 用于确定 Corosync 令牌超时时间的系数。详情请参阅 corosync.conf(5) 手册。 |
| `votes` | integer | 否 | — | 此节点的票数。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "clustername": {
      "description": "集群名称。",
      "format": "pve-node",
      "maxLength": 15,
      "type": "string",
      "typetext": "<string>"
    },
    "link[n]": {
      "description": "单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7）",
      "format": {
        "address": {
          "default_key": 1,
          "description": "此 corosync 链路地址的主机名（或 IP）。",
          "format": "address",
          "format_description": "IP",
          "type": "string"
        },
        "priority": {
          "default": 0,
          "description": "knet 在 'passive' 模式（默认）下使用时的链路优先级。值越小，优先级越高。仅对创建集群有效，添加节点时忽略。",
          "maximum": 255,
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[address=]<IP> [,priority=<integer>]"
    },
    "nodeid": {
      "description": "此节点的节点 ID。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "token-coefficient": {
      "default": 125,
      "description": "用于确定 Corosync 令牌超时时间的系数。详情请参阅 corosync.conf(5) 手册。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "votes": {
      "description": "此节点的票数。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config)。
