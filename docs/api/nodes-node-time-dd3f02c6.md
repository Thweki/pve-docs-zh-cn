# `/nodes/{node}/time`

原始接口路径：`/nodes/{node}/time`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/time`

读取服务器时间和时区设置。

**方法标识：** `time`

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
    "localtime": {
      "description": "自 1970-01-01 00:00:00（本地时间）起的秒数",
      "minimum": 1297163644,
      "renderer": "timestamp_gmt",
      "type": "integer"
    },
    "time": {
      "description": "自 1970-01-01 00:00:00 UTC 起的秒数。",
      "minimum": 1297163644,
      "renderer": "timestamp",
      "type": "integer"
    },
    "timezone": {
      "description": "时区",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/time`

设置时区。

**方法标识：** `set_timezone`

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
| `timezone` | string | 是 | — | 时区。文件 '/usr/share/zoneinfo/zone.tab' 包含有效名称列表。 |

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
    },
    "timezone": {
      "description": "时区。文件 '/usr/share/zoneinfo/zone.tab' 包含有效名称列表。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/time)。
