# `/nodes/{node}/ceph/fs/{name}`

原始接口路径：`/nodes/{node}/ceph/fs/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/fs/{name}`

Destroy a Ceph filesystem. Refuses if any PVE storage entry of type 'cephfs' still references the filesystem and is not disabled. Optionally also removes the storage entries and/or the underlying metadata and data pools.

**方法标识：** `destroyfs`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
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
| `name` | string | 是 | — | The Ceph filesystem name. |
| `node` | string | 是 | — | The cluster node name. |
| `remove-pools` | boolean | 否 | 0 | Remove the metadata and data pools used by this filesystem. |
| `remove-storages` | boolean | 否 | 0 | Remove pveceph-managed storages configured for this filesystem. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "The Ceph filesystem name.",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "remove-pools": {
      "default": 0,
      "description": "Remove the metadata and data pools used by this filesystem.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "remove-storages": {
      "default": 0,
      "description": "Remove pveceph-managed storages configured for this filesystem.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

## POST `/nodes/{node}/ceph/fs/{name}`

Create a Ceph filesystem

**方法标识：** `createfs`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
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
| `add-storage` | boolean | 否 | 0 | Configure the created CephFS as storage for this cluster. |
| `name` | string | 否 | "cephfs" | The ceph filesystem name. |
| `node` | string | 是 | — | The cluster node name. |
| `pg_num` | integer | 否 | 128 | Number of placement groups for the backing data pool. The metadata pool will use a quarter of this. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add-storage": {
      "default": 0,
      "description": "Configure the created CephFS as storage for this cluster.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "default": "cephfs",
      "description": "The ceph filesystem name.",
      "optional": 1,
      "pattern": "(?^:^[^:/\\s]+$)",
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pg_num": {
      "default": 128,
      "description": "Number of placement groups for the backing data pool. The metadata pool will use a quarter of this.",
      "maximum": 32768,
      "minimum": 8,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (8 - 32768)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/fs/{name})。
