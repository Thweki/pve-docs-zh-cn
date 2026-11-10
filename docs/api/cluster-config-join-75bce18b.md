# `/cluster/config/join`

原始接口路径：`/cluster/config/join`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/config/join`

Get information needed to join this cluster over the connected node.

**方法标识：** `join_info`

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
| `node` | string | 否 | "current connected node" | The node for which the joinee gets the nodeinfo. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "default": "current connected node",
      "description": "The node for which the joinee gets the nodeinfo.",
      "format": "pve-node",
      "optional": 1,
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
  "additionalProperties": 0,
  "properties": {
    "config_digest": {
      "type": "string"
    },
    "nodelist": {
      "items": {
        "additionalProperties": 1,
        "properties": {
          "name": {
            "description": "The cluster node name.",
            "format": "pve-node",
            "type": "string"
          },
          "nodeid": {
            "description": "Node id for this node.",
            "minimum": 1,
            "optional": 1,
            "type": "integer"
          },
          "pve_addr": {
            "format": "ip",
            "type": "string"
          },
          "pve_fp": {
            "description": "Certificate SHA 256 fingerprint.",
            "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
            "type": "string"
          },
          "quorum_votes": {
            "minimum": 0,
            "type": "integer"
          },
          "ring0_addr": {
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
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "preferred_node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string"
    },
    "totem": {
      "type": "object"
    }
  },
  "type": "object"
}
```

## POST `/cluster/config/join`

Joins this node into an existing cluster. If no links are given, default to IP resolved by node's hostname on single link (fallback fails for clusters with multiple links).

**方法标识：** `join`

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
| `fingerprint` | string | 是 | — | Certificate SHA 256 fingerprint. |
| `force` | boolean | 否 | — | Do not throw error if node already exists. |
| `hostname` | string | 是 | — | Hostname (or IP) of an existing cluster member. |
| `link[n]` | string | 否 | — | Address and priority information of a single corosync link. (up to 8 links supported; link0..link7) |
| `nodeid` | integer | 否 | — | Node id for this node. |
| `password` | string | 是 | — | Superuser (root) password of peer node. |
| `votes` | integer | 否 | — | Number of votes for this node |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {
      "description": "Certificate SHA 256 fingerprint.",
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "force": {
      "description": "Do not throw error if node already exists.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hostname": {
      "description": "Hostname (or IP) of an existing cluster member.",
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
    "password": {
      "description": "Superuser (root) password of peer node.",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "votes": {
      "description": "Number of votes for this node",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/join)。
