# `/cluster/config/nodes/{node}`

原始接口路径：`/cluster/config/nodes/{node}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/config/nodes/{node}`

Removes a node from the cluster configuration.

**方法标识：** `delnode`

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
  "type": "null"
}
```

## POST `/cluster/config/nodes/{node}`

Adds a node to the cluster configuration. This call is for internal use.

**方法标识：** `addnode`

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
| `apiversion` | integer | 否 | — | The JOIN_API_VERSION of the new node. |
| `force` | boolean | 否 | — | Do not throw error if node already exists. |
| `link[n]` | string | 否 | — | Address and priority information of a single corosync link. (up to 8 links supported; link0..link7) |
| `new_node_ip` | string | 否 | — | IP Address of node to add. Used as fallback if no links are given. |
| `node` | string | 是 | — | The cluster node name. |
| `nodeid` | integer | 否 | — | Node id for this node. |
| `votes` | integer | 否 | — | Number of votes for this node |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "apiversion": {
      "description": "The JOIN_API_VERSION of the new node.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "force": {
      "description": "Do not throw error if node already exists.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "new_node_ip": {
      "description": "IP Address of node to add. Used as fallback if no links are given.",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "nodeid": {
      "description": "Node id for this node.",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
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
  "properties": {
    "corosync_authkey": {
      "type": "string"
    },
    "corosync_conf": {
      "type": "string"
    },
    "warnings": {
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/nodes/{node})。
