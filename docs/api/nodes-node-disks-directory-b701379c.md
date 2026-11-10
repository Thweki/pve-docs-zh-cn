# `/nodes/{node}/disks/directory`

原始接口路径：`/nodes/{node}/disks/directory`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/directory`

PVE 管理的目录存储。

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
      "device": {
        "description": "已挂载的设备。",
        "type": "string"
      },
      "options": {
        "description": "挂载选项。",
        "type": "string"
      },
      "path": {
        "description": "挂载路径。",
        "type": "string"
      },
      "type": {
        "description": "文件系统类型。",
        "type": "string"
      },
      "unitfile": {
        "description": "挂载单元路径。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

## POST `/nodes/{node}/disks/directory`

在未使用的磁盘上创建文件系统。将挂载在 '/mnt/pve/NAME' 下。

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
| `add_storage` | boolean | 否 | 0 | 使用目录配置存储。 |
| `device` | string | 是 | — | 要在其上创建文件系统的块设备。 |
| `filesystem` | string | 否 | "ext4" | 所需的文件系统。；可选值：`ext4`, `xfs` |
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
      "description": "使用目录配置存储。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "device": {
      "description": "要在其上创建文件系统的块设备。",
      "type": "string",
      "typetext": "<string>"
    },
    "filesystem": {
      "default": "ext4",
      "description": "所需的文件系统。",
      "enum": [
        "ext4",
        "xfs"
      ],
      "optional": 1,
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/directory)。
