# `/cluster/mapping/dir/{id}`

原始接口路径：`/cluster/mapping/dir/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/mapping/dir/{id}`

移除目录映射。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/dir",
    [
      "Mapping.Modify"
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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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

## GET `/cluster/mapping/dir/{id}`

获取目录映射。

**方法标识：** `get`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/dir/{id}",
      [
        "Mapping.Use"
      ]
    ],
    [
      "perm",
      "/mapping/dir/{id}",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "perm",
      "/mapping/dir/{id}",
      [
        "Mapping.Audit"
      ]
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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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
  "type": "object"
}
```

## PUT `/cluster/mapping/dir/{id}`

更新目录映射。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/dir/{id}",
    [
      "Mapping.Modify"
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
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `description` | string | 否 | — | 目录映射的描述 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `id` | string | 是 | — | 目录映射的 ID |
| `map` | array | 否 | — | 集群节点的映射列表。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "目录映射的描述",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "id": {
      "description": "目录映射的 ID",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "node": {
            "description": "集群节点名称。",
            "format": "pve-node",
            "type": "string"
          },
          "path": {
            "description": "应与客户机共享的目录的绝对路径。",
            "format": "pve-storage-path-in-property-string",
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/dir/{id})。
