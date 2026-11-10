# `/pools`

原始接口路径：`/pools`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/pools`

Delete pool.

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
  "description": "You can only delete empty pools (no members)."
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

List pools or get pool configuration.

**方法标识：** `index`

**权限**

```json
{
  "description": "List all pools where you have Pool.Audit permissions on /pool/<pool>, or the pool specific with {poolid}",
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

Create new pool.

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

Update pool.

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
  "description": "You also need the right to modify permissions on any object you add/delete."
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
| `allow-move` | boolean | 否 | 0 | Allow adding a guest even if already in another pool. The guest will be removed from its current pool and added to this one. |
| `comment` | string | 否 | — |  |
| `delete` | boolean | 否 | 0 | Remove the passed VMIDs and/or storage IDs instead of adding them. |
| `poolid` | string | 是 | — |  |
| `storage` | string | 否 | — | List of storage IDs to add or remove from this pool. |
| `vms` | string | 否 | — | List of guest VMIDs to add or remove from this pool. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "allow-move": {
      "default": 0,
      "description": "Allow adding a guest even if already in another pool. The guest will be removed from its current pool and added to this one.",
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
      "description": "Remove the passed VMIDs and/or storage IDs instead of adding them.",
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
      "description": "List of storage IDs to add or remove from this pool.",
      "format": "pve-storage-id-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vms": {
      "description": "List of guest VMIDs to add or remove from this pool.",
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
