# `/nodes/{node}/dns`

原始接口路径：`/nodes/{node}/dns`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/dns`

Read DNS settings.

**方法标识：** `dns`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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
  "additionalProperties": 0,
  "properties": {
    "dns1": {
      "description": "First name server IP address.",
      "optional": 1,
      "type": "string"
    },
    "dns2": {
      "description": "Second name server IP address.",
      "optional": 1,
      "type": "string"
    },
    "dns3": {
      "description": "Third name server IP address.",
      "optional": 1,
      "type": "string"
    },
    "search": {
      "description": "Search domain for host-name lookup.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/dns`

Write DNS settings.

**方法标识：** `update_dns`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Modify"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `dns1` | string | 否 | — | First name server IP address. |
| `dns2` | string | 否 | — | Second name server IP address. |
| `dns3` | string | 否 | — | Third name server IP address. |
| `node` | string | 是 | — | The cluster node name. |
| `search` | string | 是 | — | Search domain for host-name lookup. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dns1": {
      "description": "First name server IP address.",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dns2": {
      "description": "Second name server IP address.",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dns3": {
      "description": "Third name server IP address.",
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
    "search": {
      "description": "Search domain for host-name lookup.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/dns)。
