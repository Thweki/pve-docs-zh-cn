# `/nodes/{node}/disks/zfs`

原始接口路径：`/nodes/{node}/disks/zfs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/zfs`

列出 Zpool。

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
      "alloc": {
        "description": "",
        "type": "integer"
      },
      "dedup": {
        "description": "",
        "type": "number"
      },
      "frag": {
        "description": "",
        "type": "integer"
      },
      "free": {
        "description": "",
        "type": "integer"
      },
      "health": {
        "description": "",
        "type": "string"
      },
      "name": {
        "description": "",
        "type": "string"
      },
      "size": {
        "description": "",
        "type": "integer"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/nodes/{node}/disks/zfs`

创建 ZFS 池。

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
| `add_storage` | boolean | 否 | 0 | 使用 zpool 配置存储。 |
| `ashift` | integer | 否 | 12 | 池扇区大小指数。 |
| `compression` | string | 否 | "on" | 要使用的压缩算法。；可选值：`on`, `off`, `gzip`, `lz4`, `lzjb`, `zle`, `zstd` |
| `devices` | string | 是 | — | 要在其上创建 zpool 的块设备。 |
| `draid-config` | string | 否 | — |  |
| `name` | string | 是 | — | 存储标识符。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `raidlevel` | string | 是 | — | 要使用的 RAID 级别。；可选值：`single`, `mirror`, `raid10`, `raidz`, `raidz2`, `raidz3`, `draid`, `draid2`, `draid3` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storage": {
      "default": 0,
      "description": "使用 zpool 配置存储。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ashift": {
      "default": 12,
      "description": "池扇区大小指数。",
      "maximum": 16,
      "minimum": 9,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (9 - 16)"
    },
    "compression": {
      "default": "on",
      "description": "要使用的压缩算法。",
      "enum": [
        "on",
        "off",
        "gzip",
        "lz4",
        "lzjb",
        "zle",
        "zstd"
      ],
      "optional": 1,
      "type": "string"
    },
    "devices": {
      "description": "要在其上创建 zpool 的块设备。",
      "format": "string-list",
      "type": "string",
      "typetext": "<string>"
    },
    "draid-config": {
      "format": {
        "data": {
          "description": "每个冗余组的数据设备数量。（dRAID）",
          "minimum": 1,
          "type": "integer"
        },
        "spares": {
          "description": "dRAID 备用设备数量。",
          "minimum": 0,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "data=<integer> ,spares=<integer>"
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
    },
    "raidlevel": {
      "description": "要使用的 RAID 级别。",
      "enum": [
        "single",
        "mirror",
        "raid10",
        "raidz",
        "raidz2",
        "raidz3",
        "draid",
        "draid2",
        "draid3"
      ],
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/zfs)。
