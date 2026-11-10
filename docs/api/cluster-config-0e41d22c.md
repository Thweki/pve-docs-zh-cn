# `/cluster/config`

原始接口路径：`/cluster/config`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/config`

Directory index.

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

Generate new cluster configuration. If no links given, default to local IP address as link0.

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
| `clustername` | string | 是 | — | The name of the cluster. |
| `link[n]` | string | 否 | — | Address and priority information of a single corosync link. (up to 8 links supported; link0..link7) |
| `nodeid` | integer | 否 | — | Node id for this node. |
| `token-coefficient` | integer | 否 | 125 | Coefficient used to determine Corosync's token timeout. See the corosync.conf(5) manual for more details. |
| `votes` | integer | 否 | — | Number of votes for this node. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "clustername": {
      "description": "The name of the cluster.",
      "format": "pve-node",
      "maxLength": 15,
      "type": "string",
      "typetext": "<string>"
    },
    "link[n]": {
      "description": "Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)",
      "format": {
        "address": {
          "default_key": 1,
          "description": "Hostname (or IP) of this corosync link address.",
          "format": "address",
          "format_description": "IP",
          "type": "string"
        },
        "priority": {
          "default": 0,
          "description": "The priority for the link when knet is used in 'passive' mode (default). Lower value means higher priority. Only valid for cluster create, ignored on node add.",
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
      "description": "Node id for this node.",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "token-coefficient": {
      "default": 125,
      "description": "Coefficient used to determine Corosync's token timeout. See the corosync.conf(5) manual for more details.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "votes": {
      "description": "Number of votes for this node.",
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
