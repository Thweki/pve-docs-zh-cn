# `/nodes/{node}/ceph/osd`

原始接口路径：`/nodes/{node}/ceph/osd`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/osd`

Get Ceph osd list/tree.

**方法标识：** `index`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Datastore.Audit"
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
  "additionalProperties": 1,
  "properties": {
    "flags": {
      "description": "Comma-joined list of currently-set OSD flags; absent when no flags are set on the cluster.",
      "optional": 1,
      "type": "string"
    },
    "root": {
      "additionalProperties": 1,
      "description": "Top-level CRUSH bucket; recursive structure with 'children' lists holding nested buckets and OSD leaves. Per-node properties (status, weight, in, usage, latencies, etc.) vary by node type and are not statically typed here.",
      "type": "object"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/ceph/osd`

Create OSD

**方法标识：** `createosd`

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
| `crush-device-class` | string | 否 | — | Set the device class of the OSD in crush. |
| `db_dev` | string | 否 | — | Block device name for block.db. |
| `db_dev_size` | number | 否 | — | Size in GiB for block.db. |
| `dev` | string | 是 | — | Block device name. |
| `encrypted` | boolean | 否 | 0 | Enables encryption of the OSD. |
| `node` | string | 是 | — | The cluster node name. |
| `osds-per-device` | integer | 否 | — | OSD services per physical device. Only useful for fast NVMe devices to utilize their performance better. Mutually exclusive with 'db_dev' and 'wal_dev'. |
| `wal_dev` | string | 否 | — | Block device name for block.wal. |
| `wal_dev_size` | number | 否 | — | Size in GiB for block.wal. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "crush-device-class": {
      "description": "Set the device class of the OSD in crush.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "db_dev": {
      "description": "Block device name for block.db.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "db_dev_size": {
      "description": "Size in GiB for block.db.",
      "minimum": 1,
      "optional": 1,
      "requires": "db_dev",
      "type": "number",
      "typetext": "<number> (1 - N)",
      "verbose_description": "If a block.db is requested but the size is not given, will be automatically selected by: bluestore_block_db_size from the ceph database (osd or global section) or config (osd or global section) in that order. If this is not available, it will be sized 10% of the size of the OSD device. Fails if the available size is not enough."
    },
    "dev": {
      "description": "Block device name.",
      "type": "string",
      "typetext": "<string>"
    },
    "encrypted": {
      "default": 0,
      "description": "Enables encryption of the OSD.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "osds-per-device": {
      "description": "OSD services per physical device. Only useful for fast NVMe devices to utilize their performance better. Mutually exclusive with 'db_dev' and 'wal_dev'.",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "wal_dev": {
      "description": "Block device name for block.wal.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "wal_dev_size": {
      "description": "Size in GiB for block.wal.",
      "minimum": 0.5,
      "optional": 1,
      "requires": "wal_dev",
      "type": "number",
      "typetext": "<number> (0.5 - N)",
      "verbose_description": "If a block.wal is requested but the size is not given, will be automatically selected by: bluestore_block_wal_size from the ceph database (osd or global section) or config (osd or global section) in that order. If this is not available, it will be sized 1% of the size of the OSD device. Fails if the available size is not enough."
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/osd)。
