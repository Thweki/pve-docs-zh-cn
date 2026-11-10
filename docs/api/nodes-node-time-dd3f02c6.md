# `/nodes/{node}/time`

原始接口路径：`/nodes/{node}/time`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/time`

Read server time and time zone settings.

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
    "localtime": {
      "description": "Seconds since 1970-01-01 00:00:00 (local time)",
      "minimum": 1297163644,
      "renderer": "timestamp_gmt",
      "type": "integer"
    },
    "time": {
      "description": "Seconds since 1970-01-01 00:00:00 UTC.",
      "minimum": 1297163644,
      "renderer": "timestamp",
      "type": "integer"
    },
    "timezone": {
      "description": "Time zone",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/time`

Set time zone.

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
| `node` | string | 是 | — | The cluster node name. |
| `timezone` | string | 是 | — | Time zone. The file '/usr/share/zoneinfo/zone.tab' contains the list of valid names. |

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
    },
    "timezone": {
      "description": "Time zone. The file '/usr/share/zoneinfo/zone.tab' contains the list of valid names.",
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
