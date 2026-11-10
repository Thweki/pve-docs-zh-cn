# `/pools`

原始接口路径：`/pools`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/pools`

删除资源池。

**方法标识：** `delete_pool`

**权限**

```json
{
  "check": [
    "perm",
    "/pool/{poolid}",
    [
      "Pool.Allocate"
    ]
  ],
  "description": "只能删除空资源池（无成员）。"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `poolid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "poolid": {
      "format": "pve-poolid",
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

## GET `/pools`

列出资源池或获取资源池配置。

**方法标识：** `index`

**权限**

```json
{
  "description": "列出您对 /pool/<pool> 具有 Pool.Audit 权限的所有资源池，或使用 {poolid} 指定的资源池",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `poolid` | string | 否 | — |  |
| `type` | string | 否 | — | ；可选值：`qemu`, `lxc`, `storage` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "poolid": {
      "format": "pve-poolid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "enum": [
        "qemu",
        "lxc",
        "storage"
      ],
      "optional": 1,
      "requires": "poolid",
      "type": "string"
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
      "comment": {
        "optional": 1,
        "type": "string"
      },
      "members": {
        "items": {
          "additionalProperties": 1,
          "properties": {
            "id": {
              "type": "string"
            },
            "node": {
              "type": "string"
            },
            "storage": {
              "optional": 1,
              "type": "string"
            },
            "type": {
              "enum": [
                "qemu",
                "lxc",
                "openvz",
                "storage"
              ],
              "type": "string"
            },
            "vmid": {
              "optional": 1,
              "type": "integer"
            }
          },
          "type": "object"
        },
        "optional": 1,
        "type": "array"
      },
      "poolid": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{poolid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/pools`

创建新资源池。

**方法标识：** `create_pool`

**权限**

```json
{
  "check": [
    "perm",
    "/pool/{poolid}",
    [
      "Pool.Allocate"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `comment` | string | 否 | — |  |
| `poolid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "poolid": {
      "format": "pve-poolid",
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

## PUT `/pools`

更新资源池。

**方法标识：** `update_pool`

**权限**

```json
{
  "check": [
    "perm",
    "/pool/{poolid}",
    [
      "Pool.Allocate"
    ]
  ],
  "description": "还需要有权修改所添加/删除的任何对象的权限。"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `allow-move` | boolean | 否 | 0 | 即使客户机已位于其他资源池，也允许添加。客户机将从当前资源池移除并加入此资源池。 |
| `comment` | string | 否 | — |  |
| `delete` | boolean | 否 | 0 | 移除传入的 VMID 和/或存储 ID，而非添加。 |
| `poolid` | string | 是 | — |  |
| `storage` | string | 否 | — | 要添加到此资源池或从中移除的存储 ID 列表。 |
| `vms` | string | 否 | — | 要添加到此资源池或从中移除的客户机 VMID 列表。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "allow-move": {
      "default": 0,
      "description": "即使客户机已位于其他资源池，也允许添加。客户机将从当前资源池移除并加入此资源池。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "comment": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "default": 0,
      "description": "移除传入的 VMID 和/或存储 ID，而非添加。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "poolid": {
      "format": "pve-poolid",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "要添加到此资源池或从中移除的存储 ID 列表。",
      "format": "pve-storage-id-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vms": {
      "description": "要添加到此资源池或从中移除的客户机 VMID 列表。",
      "format": "pve-vmid-list",
      "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/pools)。
