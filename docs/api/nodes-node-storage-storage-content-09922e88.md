# `/nodes/{node}/storage/{storage}/content`

原始接口路径：`/nodes/{node}/storage/{storage}/content`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/content`

List storage content.

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
| `content` | string | 否 | — | Only list content of this type. |
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 是 | — | The storage identifier. |
| `vmid` | integer | 否 | — | Only list images for this VM |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "content": {
      "description": "Only list content of this type.",
      "format": "pve-storage-content",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "vmid": {
      "description": "Only list images for this VM",
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
        "description": "Approximate volume size in bytes. Present instead of 'size' for storages where determining the exact size has technical limitations. Will typically be an upper bound on the actual size, but the exact semantics depend on the storage plugin.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "ctime": {
        "description": "Creation time (seconds since the UNIX Epoch).",
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "encrypted": {
        "description": "If whole backup is encrypted, value is the fingerprint or '1'  if encrypted. Only useful for the Proxmox Backup Server storage type.",
        "optional": 1,
        "type": "string"
      },
      "format": {
        "description": "Format identifier ('raw', 'qcow2', 'subvol', 'iso', 'tgz' ...)",
        "type": "string"
      },
      "notes": {
        "description": "Optional notes. If they contain multiple lines, only the first one is returned here.",
        "optional": 1,
        "type": "string"
      },
      "parent": {
        "description": "Volume identifier of parent (for linked cloned).",
        "optional": 1,
        "type": "string"
      },
      "protected": {
        "description": "Protection status. Currently only supported for backups.",
        "optional": 1,
        "type": "boolean"
      },
      "size": {
        "description": "Volume size in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "used": {
        "description": "Used space. Please note that most storage plugins do not report anything useful here.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "verification": {
        "description": "Last backup verification result, only useful for PBS storages.",
        "optional": 1,
        "properties": {
          "state": {
            "description": "Last backup verification state.",
            "type": "string"
          },
          "upid": {
            "description": "Last backup verification UPID.",
            "type": "string"
          }
        },
        "type": "object"
      },
      "vmid": {
        "description": "Associated Owner VMID.",
        "optional": 1,
        "type": "integer"
      },
      "volid": {
        "description": "Volume identifier.",
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

Allocate disk images.

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
| `filename` | string | 是 | — | The name of the file to create. |
| `format` | string | 否 | — | Format of the image.；可选值：`raw`, `qcow2`, `subvol`, `vmdk` |
| `node` | string | 是 | — | The cluster node name. |
| `size` | string | 是 | — | Size in kilobyte (1024 bytes). Optional suffixes 'M' (megabyte, 1024K) and 'G' (gigabyte, 1024M) |
| `storage` | string | 是 | — | The storage identifier. |
| `vmid` | integer | 是 | — | Specify owner VM |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "filename": {
      "description": "The name of the file to create.",
      "type": "string",
      "typetext": "<string>"
    },
    "format": {
      "description": "Format of the image.",
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
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "size": {
      "description": "Size in kilobyte (1024 bytes). Optional suffixes 'M' (megabyte, 1024K) and 'G' (gigabyte, 1024M)",
      "pattern": "\\d+[MG]?",
      "type": "string"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "vmid": {
      "description": "Specify owner VM",
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
  "description": "Volume identifier",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/content)。
