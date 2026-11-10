# `/nodes/{node}/disks/lvm`

原始接口路径：`/nodes/{node}/disks/lvm`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/lvm`

列出 LVM 卷组

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
  "properties": {
    "children": {
      "items": {
        "properties": {
          "children": {
            "description": "底层物理卷",
            "items": {
              "properties": {
                "free": {
                  "description": "物理卷中的空闲字节数",
                  "type": "integer"
                },
                "leaf": {
                  "type": "boolean"
                },
                "name": {
                  "description": "物理卷名称",
                  "type": "string"
                },
                "size": {
                  "description": "物理卷大小，单位为字节",
                  "type": "integer"
                }
              },
              "type": "object"
            },
            "optional": 1,
            "type": "array"
          },
          "free": {
            "description": "卷组中的空闲字节数",
            "type": "integer"
          },
          "leaf": {
            "type": "boolean"
          },
          "name": {
            "description": "卷组名称",
            "type": "string"
          },
          "size": {
            "description": "卷组大小，单位为字节",
            "type": "integer"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "leaf": {
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/disks/lvm`

创建 LVM 卷组

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
| `add_storage` | boolean | 否 | 0 | 使用卷组配置存储 |
| `device` | string | 是 | — | 要在其上创建卷组的块设备 |
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
      "description": "使用卷组配置存储",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "device": {
      "description": "要在其上创建卷组的块设备",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/lvm)。
