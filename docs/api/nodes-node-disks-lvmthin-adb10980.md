# `/nodes/{node}/disks/lvmthin`

原始接口路径：`/nodes/{node}/disks/lvmthin`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/lvmthin`

列出 LVM 精简池

**方法标识：** `index`

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
  "items": {
    "properties": {
      "lv": {
        "description": "精简池名称。",
        "type": "string"
      },
      "lv_size": {
        "description": "精简池大小，单位为字节。",
        "type": "integer"
      },
      "metadata_size": {
        "description": "元数据逻辑卷大小，单位为字节。",
        "type": "integer"
      },
      "metadata_used": {
        "description": "元数据逻辑卷已用字节数。",
        "type": "integer"
      },
      "used": {
        "description": "精简池已用字节数。",
        "type": "integer"
      },
      "vg": {
        "description": "关联的卷组。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

## POST `/nodes/{node}/disks/lvmthin`

创建 LVM 精简池

**方法标识：** `create`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
  ],
  "description": "还需要对 /storage 具有 'Datastore.Allocate' 权限（设置 'add_storage' 时）"
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
| `add_storage` | boolean | 否 | 0 | 使用精简池配置存储。 |
| `device` | string | 是 | — | 要在其上创建精简池的块设备。 |
| `name` | string | 是 | — | 存储标识符。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storage": {
      "default": 0,
      "description": "使用精简池配置存储。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "device": {
      "description": "要在其上创建精简池的块设备。",
      "type": "string",
      "typetext": "<string>"
    },
    "name": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/lvmthin)。
