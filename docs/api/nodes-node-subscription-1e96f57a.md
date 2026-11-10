# `/nodes/{node}/subscription`

原始接口路径：`/nodes/{node}/subscription`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/subscription`

删除此节点的订阅密钥。

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
  "type": "null"
}
```

## GET `/nodes/{node}/subscription`

读取订阅信息。

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
  "additionalProperties": 0,
  "properties": {
    "checktime": {
      "description": "上次检查的时间戳。",
      "optional": 1,
      "type": "integer"
    },
    "key": {
      "description": "订阅密钥（如果已设置且获准访问）。",
      "optional": 1,
      "type": "string"
    },
    "level": {
      "description": "订阅级别的简短代码。",
      "optional": 1,
      "type": "string"
    },
    "message": {
      "description": "更便于人类阅读的状态消息。",
      "optional": 1,
      "type": "string"
    },
    "nextduedate": {
      "description": "已设置订阅的下次到期日期。",
      "optional": 1,
      "type": "string"
    },
    "productname": {
      "description": "已设置订阅的人类可读产品名称。",
      "optional": 1,
      "type": "string"
    },
    "regdate": {
      "description": "已设置订阅的注册日期。",
      "optional": 1,
      "type": "string"
    },
    "serverid": {
      "description": "服务器 ID（如果获准访问）。",
      "optional": 1,
      "type": "string"
    },
    "signature": {
      "description": "离线密钥的签名",
      "optional": 1,
      "type": "string"
    },
    "sockets": {
      "description": "此宿主机的插槽数量。",
      "optional": 1,
      "type": "integer"
    },
    "status": {
      "description": "当前订阅状态。",
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
      "description": "网上商店的 URL。",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/subscription`

更新订阅信息。

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
| `force` | boolean | 否 | 0 | 始终连接服务器，即使本地缓存仍然有效。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "始终连接服务器，即使本地缓存仍然有效。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
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
  "type": "null"
}
```

## PUT `/nodes/{node}/subscription`

设置订阅密钥。

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
| `key` | string | 是 | — | Proxmox VE 订阅密钥 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "key": {
      "description": "Proxmox VE 订阅密钥",
      "maxLength": 32,
      "pattern": "\\s*pve([1248])([cbsp])-(arm-)?[0-9a-f]{10}\\s*",
      "type": "string"
    },
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/subscription)。
