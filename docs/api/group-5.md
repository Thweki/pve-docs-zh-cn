# pools API

本章包含此资源组的全部接口，按路径和 HTTP 方法在同一页展开。接口路径、方法、参数、类型、约束和默认值保持原值。

## `/pools` <a href="#api-pools-4eb15ae6" id="api-pools-4eb15ae6"></a>

原始接口路径：`/pools`。

### DELETE `/pools` <a href="#api-pools-4eb15ae6-delete" id="api-pools-4eb15ae6-delete"></a>

删除资源池。

**方法标识：** `delete_pool`

**权限**

```text
{"check": ["perm", "/pool/{poolid}", ["Pool.Allocate"]], "description": "只能删除空资源池（无成员）。"}
```

**允许 API 令牌**

```text
1
```

**受保护接口**

```text
1
```

#### 请求参数 <a href="#api-pools-4eb15ae6-delete-parameters" id="api-pools-4eb15ae6-delete-parameters"></a>

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `poolid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"poolid": {"format": "pve-poolid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-pools-4eb15ae6-delete-returns" id="api-pools-4eb15ae6-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/pools` <a href="#api-pools-4eb15ae6-get" id="api-pools-4eb15ae6-get"></a>

列出资源池或获取资源池配置。

**方法标识：** `index`

**权限**

```text
{"description": "列出您对 /pool/<pool> 具有 Pool.Audit 权限的所有资源池，或使用 {poolid} 指定的资源池", "user": "all"}
```

**允许 API 令牌**

```text
1
```

#### 请求参数 <a href="#api-pools-4eb15ae6-get-parameters" id="api-pools-4eb15ae6-get-parameters"></a>

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `poolid` | string | 否 | — |  |
| `type` | string | 否 | — | ；可选值：`qemu`, `lxc`, `storage` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "poolid": {"format": "pve-poolid", "optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"enum": ["qemu", "lxc", "storage"], "optional": 1, "requires": "poolid", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-pools-4eb15ae6-get-returns" id="api-pools-4eb15ae6-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"optional": 1, "type": "string"},
      "members": {
        "items": {
          "additionalProperties": 1,
          "properties": {
            "id": {"type": "string"}, "node": {"type": "string"}, "storage": {"optional": 1, "type": "string"},
            "type": {"enum": ["qemu", "lxc", "openvz", "storage"], "type": "string"}, "vmid": {"optional": 1, "type": "integer"}
          },
          "type": "object"
        },
        "optional": 1, "type": "array"
      },
      "poolid": {"type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{poolid}", "rel": "child"}], "type": "array"
}
```

### POST `/pools` <a href="#api-pools-4eb15ae6-post" id="api-pools-4eb15ae6-post"></a>

创建新资源池。

**方法标识：** `create_pool`

**权限**

```text
{"check": ["perm", "/pool/{poolid}", ["Pool.Allocate"]]}
```

**允许 API 令牌**

```text
1
```

**受保护接口**

```text
1
```

#### 请求参数 <a href="#api-pools-4eb15ae6-post-parameters" id="api-pools-4eb15ae6-post-parameters"></a>

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `comment` | string | 否 | — |  |
| `poolid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"optional": 1, "type": "string", "typetext": "<string>"}, "poolid": {"format": "pve-poolid", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-pools-4eb15ae6-post-returns" id="api-pools-4eb15ae6-post-returns"></a>

```text
{"type": "null"}
```

### PUT `/pools` <a href="#api-pools-4eb15ae6-put" id="api-pools-4eb15ae6-put"></a>

更新资源池。

**方法标识：** `update_pool`

**权限**

```text
{"check": ["perm", "/pool/{poolid}", ["Pool.Allocate"]], "description": "还需要有权修改所添加/删除的任何对象的权限。"}
```

**允许 API 令牌**

```text
1
```

**受保护接口**

```text
1
```

#### 请求参数 <a href="#api-pools-4eb15ae6-put-parameters" id="api-pools-4eb15ae6-put-parameters"></a>

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

```text
{
  "additionalProperties": 0,
  "properties": {
    "allow-move": {
      "default": 0, "description": "即使客户机已位于其他资源池，也允许添加。客户机将从当前资源池移除并加入此资源池。", "optional": 1, "type": "boolean",
      "typetext": "<boolean>"
    },
    "comment": {"optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"default": 0, "description": "移除传入的 VMID 和/或存储 ID，而非添加。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "poolid": {"format": "pve-poolid", "type": "string", "typetext": "<string>"},
    "storage": {
      "description": "要添加到此资源池或从中移除的存储 ID 列表。", "format": "pve-storage-id-list", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "vms": {"description": "要添加到此资源池或从中移除的客户机 VMID 列表。", "format": "pve-vmid-list", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-pools-4eb15ae6-put-returns" id="api-pools-4eb15ae6-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/pools)。

## `/pools/{poolid}` <a href="#api-pools-poolid-654b0ce2" id="api-pools-poolid-654b0ce2"></a>

原始接口路径：`/pools/{poolid}`。

### DELETE `/pools/{poolid}` <a href="#api-pools-poolid-654b0ce2-delete" id="api-pools-poolid-654b0ce2-delete"></a>

删除资源池（已弃用，不支持嵌套资源池，请使用 'DELETE /pools/?poolid={poolid}'）。

**方法标识：** `delete_pool_deprecated`

**权限**

```text
{"check": ["perm", "/pool/{poolid}", ["Pool.Allocate"]], "description": "只能删除空资源池（无成员）。"}
```

**允许 API 令牌**

```text
1
```

**受保护接口**

```text
1
```

#### 请求参数 <a href="#api-pools-poolid-654b0ce2-delete-parameters" id="api-pools-poolid-654b0ce2-delete-parameters"></a>

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `poolid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"poolid": {"format": "pve-poolid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-pools-poolid-654b0ce2-delete-returns" id="api-pools-poolid-654b0ce2-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/pools/{poolid}` <a href="#api-pools-poolid-654b0ce2-get" id="api-pools-poolid-654b0ce2-get"></a>

获取资源池配置（已弃用，不支持嵌套资源池，请使用 'GET /pools/?poolid={poolid}'）。

**方法标识：** `read_pool`

**权限**

```text
{"check": ["perm", "/pool/{poolid}", ["Pool.Audit"]]}
```

**允许 API 令牌**

```text
1
```

#### 请求参数 <a href="#api-pools-poolid-654b0ce2-get-parameters" id="api-pools-poolid-654b0ce2-get-parameters"></a>

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `poolid` | string | 是 | — |  |
| `type` | string | 否 | — | ；可选值：`qemu`, `lxc`, `storage` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "poolid": {"format": "pve-poolid", "type": "string", "typetext": "<string>"}, "type": {"enum": ["qemu", "lxc", "storage"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-pools-poolid-654b0ce2-get-returns" id="api-pools-poolid-654b0ce2-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"optional": 1, "type": "string"},
    "members": {
      "items": {
        "additionalProperties": 1,
        "properties": {
          "id": {"type": "string"}, "node": {"type": "string"}, "storage": {"optional": 1, "type": "string"},
          "type": {"enum": ["qemu", "lxc", "openvz", "storage"], "type": "string"}, "vmid": {"optional": 1, "type": "integer"}
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

### PUT `/pools/{poolid}` <a href="#api-pools-poolid-654b0ce2-put" id="api-pools-poolid-654b0ce2-put"></a>

更新资源池数据（已弃用，不支持嵌套资源池——请改用 'PUT /pools/?poolid={poolid}'）。

**方法标识：** `update_pool_deprecated`

**权限**

```text
{"check": ["perm", "/pool/{poolid}", ["Pool.Allocate"]], "description": "还需要有权修改所添加/删除的任何对象的权限。"}
```

**允许 API 令牌**

```text
1
```

**受保护接口**

```text
1
```

#### 请求参数 <a href="#api-pools-poolid-654b0ce2-put-parameters" id="api-pools-poolid-654b0ce2-put-parameters"></a>

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

```text
{
  "additionalProperties": 0,
  "properties": {
    "allow-move": {
      "default": 0, "description": "即使客户机已位于其他资源池，也允许添加。客户机将从当前资源池移除并加入此资源池。", "optional": 1, "type": "boolean",
      "typetext": "<boolean>"
    },
    "comment": {"optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"default": 0, "description": "移除传入的 VMID 和/或存储 ID，而非添加。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "poolid": {"format": "pve-poolid", "type": "string", "typetext": "<string>"},
    "storage": {
      "description": "要添加到此资源池或从中移除的存储 ID 列表。", "format": "pve-storage-id-list", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "vms": {"description": "要添加到此资源池或从中移除的客户机 VMID 列表。", "format": "pve-vmid-list", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-pools-poolid-654b0ce2-put-returns" id="api-pools-poolid-654b0ce2-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/pools/{poolid})。
