# `/nodes/{node}/subscription`

原始接口路径：`/nodes/{node}/subscription`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/subscription`

Delete subscription key of this node.

**方法标识：** `delete`

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

## GET `/nodes/{node}/subscription`

Read subscription info.

**方法标识：** `get`

**权限**

```json
{
  "user": "all"
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
    "checktime": {
      "description": "Timestamp of the last check done.",
      "optional": 1,
      "type": "integer"
    },
    "key": {
      "description": "The subscription key, if set and permitted to access.",
      "optional": 1,
      "type": "string"
    },
    "level": {
      "description": "A short code for the subscription level.",
      "optional": 1,
      "type": "string"
    },
    "message": {
      "description": "A more human readable status message.",
      "optional": 1,
      "type": "string"
    },
    "nextduedate": {
      "description": "Next due date of the set subscription.",
      "optional": 1,
      "type": "string"
    },
    "productname": {
      "description": "Human readable productname of the set subscription.",
      "optional": 1,
      "type": "string"
    },
    "regdate": {
      "description": "Register date of the set subscription.",
      "optional": 1,
      "type": "string"
    },
    "serverid": {
      "description": "The server ID, if permitted to access.",
      "optional": 1,
      "type": "string"
    },
    "signature": {
      "description": "Signature for offline keys",
      "optional": 1,
      "type": "string"
    },
    "sockets": {
      "description": "The number of sockets for this host.",
      "optional": 1,
      "type": "integer"
    },
    "status": {
      "description": "The current subscription status.",
      "enum": [
        "new",
        "notfound",
        "active",
        "invalid",
        "expired",
        "suspended"
      ],
      "type": "string"
    },
    "url": {
      "description": "URL to the web shop.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/subscription`

Update subscription info.

**方法标识：** `update`

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
| `force` | boolean | 否 | 0 | Always connect to server, even if local cache is still valid. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "Always connect to server, even if local cache is still valid.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
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

## PUT `/nodes/{node}/subscription`

Set subscription key.

**方法标识：** `set`

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
| `key` | string | 是 | — | Proxmox VE subscription key |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "key": {
      "description": "Proxmox VE subscription key",
      "maxLength": 32,
      "pattern": "\\s*pve([1248])([cbsp])-(arm-)?[0-9a-f]{10}\\s*",
      "type": "string"
    },
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/subscription)。
