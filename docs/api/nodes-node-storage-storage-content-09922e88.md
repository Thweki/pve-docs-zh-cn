# `/nodes/{node}/storage/{storage}/content`

原始接口路径：`/nodes/{node}/storage/{storage}/content`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/content`

列出存储内容。

**方法标识：** `index`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.Audit",
      "Datastore.AllocateSpace"
    ],
    "any",
    1
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
| `content` | string | 否 | — | 仅列出此类型的内容。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `vmid` | integer | 否 | — | 仅列出此虚拟机的镜像 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "content": {
      "description": "仅列出此类型的内容。",
      "format": "pve-storage-content",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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
      "type": "string",
      "typetext": "<storage ID>"
    },
    "vmid": {
      "description": "仅列出此虚拟机的镜像",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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
      "approximate-size": {
        "description": "近似卷大小，单位为字节。对于因技术限制而无法确定精确大小的存储，以此项代替 'size'。通常为实际大小的上限，但确切含义取决于存储插件。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "ctime": {
        "description": "创建时间（自 UNIX 纪元起的秒数）。",
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "encrypted": {
        "description": "如果整个备份已加密，此值为指纹，或使用 '1'  表示已加密。仅对 Proxmox Backup Server 存储类型有用。",
        "optional": 1,
        "type": "string"
      },
      "format": {
        "description": "格式标识符（'raw'、'qcow2'、'subvol'、'iso'、'tgz' 等）",
        "type": "string"
      },
      "notes": {
        "description": "可选备注。如果包含多行，此处仅返回第一行。",
        "optional": 1,
        "type": "string"
      },
      "parent": {
        "description": "父卷的卷标识符（用于链接克隆）。",
        "optional": 1,
        "type": "string"
      },
      "protected": {
        "description": "保护状态。目前仅支持备份。",
        "optional": 1,
        "type": "boolean"
      },
      "size": {
        "description": "卷大小，单位为字节。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "used": {
        "description": "已用空间。请注意，大多数存储插件在此处不会报告有用的信息。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "verification": {
        "description": "上次备份验证结果，仅对 PBS 存储有用。",
        "optional": 1,
        "properties": {
          "state": {
            "description": "上次备份验证状态。",
            "type": "string"
          },
          "upid": {
            "description": "上次备份验证的 UPID。",
            "type": "string"
          }
        },
        "type": "object"
      },
      "vmid": {
        "description": "关联的所有者 VMID。",
        "optional": 1,
        "type": "integer"
      },
      "volid": {
        "description": "卷标识符。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{volid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/nodes/{node}/storage/{storage}/content`

分配磁盘镜像。

**方法标识：** `create`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.AllocateSpace"
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
| `filename` | string | 是 | — | 要创建的文件名称。 |
| `format` | string | 否 | — | 镜像格式。；可选值：`raw`, `qcow2`, `subvol`, `vmdk` |
| `node` | string | 是 | — | 集群节点名称。 |
| `size` | string | 是 | — | 大小，单位为千字节（1024 字节）。可选后缀 'M'（兆字节，1024K）和 'G'（吉字节，1024M） |
| `storage` | string | 是 | — | 存储标识符。 |
| `vmid` | integer | 是 | — | 指定所有者虚拟机 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "filename": {
      "description": "要创建的文件名称。",
      "type": "string",
      "typetext": "<string>"
    },
    "format": {
      "description": "镜像格式。",
      "enum": [
        "raw",
        "qcow2",
        "subvol",
        "vmdk"
      ],
      "optional": 1,
      "requires": "size",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "size": {
      "description": "大小，单位为千字节（1024 字节）。可选后缀 'M'（兆字节，1024K）和 'G'（吉字节，1024M）",
      "pattern": "\\d+[MG]?",
      "type": "string"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "vmid": {
      "description": "指定所有者虚拟机",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "卷标识符",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/content)。
