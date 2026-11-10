# `/cluster/config/join`

原始接口路径：`/cluster/config/join`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/config/join`

通过已连接的节点获取加入此集群所需的信息。

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
| `node` | string | 否 | "current connected node" | 加入者要获取其 nodeinfo 的节点。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "default": "current connected node",
      "description": "加入者要获取其 nodeinfo 的节点。",
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
            "description": "集群节点名称。",
            "format": "pve-node",
            "type": "string"
          },
          "nodeid": {
            "description": "此节点的节点 ID。",
            "minimum": 1,
            "optional": 1,
            "type": "integer"
          },
          "pve_addr": {
            "format": "ip",
            "type": "string"
          },
          "pve_fp": {
            "description": "证书 SHA 256 指纹。",
            "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
            "type": "string"
          },
          "quorum_votes": {
            "minimum": 0,
            "type": "integer"
          },
          "ring0_addr": {
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
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "preferred_node": {
      "description": "集群节点名称。",
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

将此节点加入现有集群。如果未提供链路，则默认在单条链路上使用由节点主机名解析得到的 IP（对于具有多条链路的集群，回退会失败）。

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
| `fingerprint` | string | 是 | — | 证书 SHA 256 指纹。 |
| `force` | boolean | 否 | — | 如果节点已存在，则不抛出错误。 |
| `hostname` | string | 是 | — | 现有集群成员的主机名（或 IP）。 |
| `link[n]` | string | 否 | — | 单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7） |
| `nodeid` | integer | 否 | — | 此节点的节点 ID。 |
| `password` | string | 是 | — | 对端节点的超级用户（root）密码。 |
| `votes` | integer | 否 | — | 此节点的票数 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {
      "description": "证书 SHA 256 指纹。",
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "force": {
      "description": "如果节点已存在，则不抛出错误。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hostname": {
      "description": "现有集群成员的主机名（或 IP）。",
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
    "password": {
      "description": "对端节点的超级用户（root）密码。",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "votes": {
      "description": "此节点的票数",
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
