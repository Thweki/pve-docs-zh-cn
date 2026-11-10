# `/nodes/{node}/storage/{storage}/content/{volume}`

原始接口路径：`/nodes/{node}/storage/{storage}/content/{volume}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/storage/{storage}/content/{volume}`

Delete volume

**权限**

```json
{
  "description": "You need 'Datastore.Allocate' privilege on the storage (or 'Datastore.AllocateSpace' for backup volumes if you have VM.Backup privilege on the VM).",
  "user": "all"
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
| `delay` | integer | 否 | — | Time to wait for the task to finish. We return 'null' if the task finish within that time. |
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 否 | — | The storage identifier. |
| `volume` | string | 是 | — | Volume identifier |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delay": {
      "description": "Time to wait for the task to finish. We return 'null' if the task finish within that time.",
      "maximum": 30,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 30)"
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
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "Volume identifier",
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
  "optional": 1,
  "type": "string"
}
```

## GET `/nodes/{node}/storage/{storage}/content/{volume}`

Get volume attributes

**权限**

```json
{
  "description": "You need read access for the volume.",
  "user": "all"
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
| `storage` | string | 否 | — | The storage identifier. |
| `volume` | string | 是 | — | Volume identifier |

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
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "Volume identifier",
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
    "format": {
      "description": "Format identifier ('raw', 'qcow2', 'subvol', 'iso', 'tgz' ...)",
      "type": "string"
    },
    "notes": {
      "description": "Optional notes.",
      "optional": 1,
      "type": "string"
    },
    "path": {
      "description": "The Path",
      "type": "string"
    },
    "protected": {
      "description": "Protection status. Currently only supported for backups.",
      "optional": 1,
      "type": "boolean"
    },
    "size": {
      "description": "Volume size in bytes.",
      "renderer": "bytes",
      "type": "integer"
    },
    "used": {
      "description": "Used space. Please note that most storage plugins do not report anything useful here.",
      "renderer": "bytes",
      "type": "integer"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/storage/{storage}/content/{volume}`

Copy a volume. This is experimental code - do not use.

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
| `storage` | string | 否 | — | The storage identifier. |
| `target` | string | 是 | — | Target volume identifier |
| `target_node` | string | 否 | — | Target node. Default is local node. |
| `volume` | string | 是 | — | Source volume identifier |

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
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "target": {
      "description": "Target volume identifier",
      "type": "string",
      "typetext": "<string>"
    },
    "target_node": {
      "description": "Target node. Default is local node.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "volume": {
      "description": "Source volume identifier",
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

## PUT `/nodes/{node}/storage/{storage}/content/{volume}`

Update volume attributes

**权限**

```json
{
  "description": "You need read access for the volume.",
  "user": "all"
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
| `notes` | string | 否 | — | The new notes. |
| `protected` | boolean | 否 | — | Protection status. Currently only supported for backups. |
| `storage` | string | 否 | — | The storage identifier. |
| `volume` | string | 是 | — | Volume identifier |

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
    },
    "notes": {
      "description": "The new notes.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "protected": {
      "description": "Protection status. Currently only supported for backups.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "volume": {
      "description": "Volume identifier",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/content/{volume})。
