# `/nodes/{node}/disks/lvm`

原始接口路径：`/nodes/{node}/disks/lvm`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/lvm`

List LVM Volume Groups

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
  "properties": {
    "children": {
      "items": {
        "properties": {
          "children": {
            "description": "The underlying physical volumes",
            "items": {
              "properties": {
                "free": {
                  "description": "The free bytes in the physical volume",
                  "type": "integer"
                },
                "leaf": {
                  "type": "boolean"
                },
                "name": {
                  "description": "The name of the physical volume",
                  "type": "string"
                },
                "size": {
                  "description": "The size of the physical volume in bytes",
                  "type": "integer"
                }
              },
              "type": "object"
            },
            "optional": 1,
            "type": "array"
          },
          "free": {
            "description": "The free bytes in the volume group",
            "type": "integer"
          },
          "leaf": {
            "type": "boolean"
          },
          "name": {
            "description": "The name of the volume group",
            "type": "string"
          },
          "size": {
            "description": "The size of the volume group in bytes",
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

Create an LVM Volume Group

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
| `add_storage` | boolean | 否 | 0 | Configure storage using the Volume Group |
| `device` | string | 是 | — | The block device you want to create the volume group on |
| `name` | string | 是 | — | The storage identifier. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add_storage": {
      "default": 0,
      "description": "Configure storage using the Volume Group",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "device": {
      "description": "The block device you want to create the volume group on",
      "type": "string",
      "typetext": "<string>"
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
