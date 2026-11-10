# `/nodes/{node}/disks/zfs`

原始接口路径：`/nodes/{node}/disks/zfs`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/zfs`

List Zpools.

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

Create a ZFS pool.

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
  "description": "Requires additionally 'Datastore.Allocate' on /storage when setting 'add_storage'"
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
| `add_storage` | boolean | 否 | 0 | Configure storage using the zpool. |
| `ashift` | integer | 否 | 12 | Pool sector size exponent. |
| `compression` | string | 否 | "on" | The compression algorithm to use.；可选值：`on`, `off`, `gzip`, `lz4`, `lzjb`, `zle`, `zstd` |
| `devices` | string | 是 | — | The block devices you want to create the zpool on. |
| `draid-config` | string | 否 | — |  |
| `name` | string | 是 | — | The storage identifier. |
| `node` | string | 是 | — | The cluster node name. |
| `raidlevel` | string | 是 | — | The RAID level to use.；可选值：`single`, `mirror`, `raid10`, `raidz`, `raidz2`, `raidz3`, `draid`, `draid2`, `draid3` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storage": {
      "default": 0,
      "description": "Configure storage using the zpool.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ashift": {
      "default": 12,
      "description": "Pool sector size exponent.",
      "maximum": 16,
      "minimum": 9,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (9 - 16)"
    },
    "compression": {
      "default": "on",
      "description": "The compression algorithm to use.",
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
      "description": "The block devices you want to create the zpool on.",
      "format": "string-list",
      "type": "string",
      "typetext": "<string>"
    },
    "draid-config": {
      "format": {
        "data": {
          "description": "The number of data devices per redundancy group. (dRAID)",
          "minimum": 1,
          "type": "integer"
        },
        "spares": {
          "description": "Number of dRAID spares.",
          "minimum": 0,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "data=<integer> ,spares=<integer>"
    },
    "name": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "raidlevel": {
      "description": "The RAID level to use.",
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
