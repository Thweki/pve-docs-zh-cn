# `/nodes/{node}/storage/{storage}/content/{volume}`

原始接口路径：`/nodes/{node}/storage/{storage}/content/{volume}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/storage/{storage}/content/{volume}`

删除卷

**方法标识：** `delete`

**权限**

```json
{
  "description": "需要对存储具有 'Datastore.Allocate' 权限（如果对虚拟机具有 VM.Backup 权限，则对备份卷具有 'Datastore.AllocateSpace' 即可）。",
  "user": "all"
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
| `delay` | integer | 否 | — | 等待任务完成的时间。如果任务在此时间内完成，则返回 'null'。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 否 | — | 存储标识符。 |
| `volume` | string | 是 | — | 卷标识符 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delay": {
      "description": "等待任务完成的时间。如果任务在此时间内完成，则返回 'null'。",
      "maximum": 30,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 30)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "卷标识符",
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
  "optional": 1,
  "type": "string"
}
```

## GET `/nodes/{node}/storage/{storage}/content/{volume}`

获取卷属性

**方法标识：** `info`

**权限**

```json
{
  "description": "需要具有卷的读取访问权限。",
  "user": "all"
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
| `storage` | string | 否 | — | 存储标识符。 |
| `volume` | string | 是 | — | 卷标识符 |

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
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "卷标识符",
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
  "properties": {
    "format": {
      "description": "格式标识符（'raw'、'qcow2'、'subvol'、'iso'、'tgz' 等）",
      "type": "string"
    },
    "notes": {
      "description": "可选备注。",
      "optional": 1,
      "type": "string"
    },
    "path": {
      "description": "路径",
      "type": "string"
    },
    "protected": {
      "description": "保护状态。目前仅支持备份。",
      "optional": 1,
      "type": "boolean"
    },
    "size": {
      "description": "卷大小，单位为字节。",
      "renderer": "bytes",
      "type": "integer"
    },
    "used": {
      "description": "已用空间。请注意，大多数存储插件在此处不会报告有用的信息。",
      "renderer": "bytes",
      "type": "integer"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/storage/{storage}/content/{volume}`

复制卷。此代码为实验性——请勿使用。

**方法标识：** `copy`

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
| `storage` | string | 否 | — | 存储标识符。 |
| `target` | string | 是 | — | 目标卷标识符 |
| `target_node` | string | 否 | — | 目标节点。默认为本地节点。 |
| `volume` | string | 是 | — | 源卷标识符 |

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
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "target": {
      "description": "目标卷标识符",
      "type": "string",
      "typetext": "<string>"
    },
    "target_node": {
      "description": "目标节点。默认为本地节点。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "volume": {
      "description": "源卷标识符",
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
  "type": "string"
}
```

## PUT `/nodes/{node}/storage/{storage}/content/{volume}`

更新卷属性

**方法标识：** `updateattributes`

**权限**

```json
{
  "description": "需要具有卷的读取访问权限。",
  "user": "all"
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
| `notes` | string | 否 | — | 新备注。 |
| `protected` | boolean | 否 | — | 保护状态。目前仅支持备份。 |
| `storage` | string | 否 | — | 存储标识符。 |
| `volume` | string | 是 | — | 卷标识符 |

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
    "notes": {
      "description": "新备注。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "protected": {
      "description": "保护状态。目前仅支持备份。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "卷标识符",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/content/{volume})。
