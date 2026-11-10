# `/nodes/{node}/ceph/osd`

原始接口路径：`/nodes/{node}/ceph/osd`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/osd`

获取 Ceph OSD 列表/树。

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
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
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
      "description": "当前已设置的 OSD 标志列表，以逗号连接；集群未设置任何标志时不存在此项。",
      "optional": 1,
      "type": "string"
    },
    "root": {
      "additionalProperties": 1,
      "description": "顶层 CRUSH 桶；递归结构，'children' 列表包含嵌套桶和 OSD 叶节点。各节点属性（状态、权重、in、用量、延迟等）随节点类型变化，此处不作静态类型定义。",
      "type": "object"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/ceph/osd`

创建 OSD

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
| `crush-device-class` | string | 否 | — | 在 CRUSH 中设置 OSD 的设备类别。 |
| `db_dev` | string | 否 | — | block.db 的块设备名称。 |
| `db_dev_size` | number | 否 | — | 如果请求 block.db 但未给出大小，将依次从 ceph 数据库（osd 或 global 配置节）或配置（osd 或 global 配置节）中的 bluestore_block_db_size 自动选择。如果不可用，则大小设为 OSD 设备大小的 10%。如果可用空间不足则失败。 |
| `dev` | string | 是 | — | 块设备名称。 |
| `encrypted` | boolean | 否 | 0 | 启用 OSD 加密。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `osds-per-device` | integer | 否 | — | 每个物理设备的 OSD 服务数。仅对高速 NVMe 设备有用，以更充分地利用性能。与 'db_dev' 和 'wal_dev' 互斥。 |
| `wal_dev` | string | 否 | — | block.wal 的块设备名称。 |
| `wal_dev_size` | number | 否 | — | 如果请求 block.wal 但未给出大小，将依次从 ceph 数据库（osd 或 global 配置节）或配置（osd 或 global 配置节）中的 bluestore_block_wal_size 自动选择。如果不可用，则大小设为 OSD 设备大小的 1%。如果可用空间不足则失败。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "crush-device-class": {
      "description": "在 CRUSH 中设置 OSD 的设备类别。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "db_dev": {
      "description": "block.db 的块设备名称。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "db_dev_size": {
      "description": "block.db 的大小，单位为 GiB。",
      "minimum": 1,
      "optional": 1,
      "requires": "db_dev",
      "type": "number",
      "typetext": "<number> (1 - N)",
      "verbose_description": "如果请求 block.db 但未给出大小，将依次从 ceph 数据库（osd 或 global 配置节）或配置（osd 或 global 配置节）中的 bluestore_block_db_size 自动选择。如果不可用，则大小设为 OSD 设备大小的 10%。如果可用空间不足则失败。"
    },
    "dev": {
      "description": "块设备名称。",
      "type": "string",
      "typetext": "<string>"
    },
    "encrypted": {
      "default": 0,
      "description": "启用 OSD 加密。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "osds-per-device": {
      "description": "每个物理设备的 OSD 服务数。仅对高速 NVMe 设备有用，以更充分地利用性能。与 'db_dev' 和 'wal_dev' 互斥。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "wal_dev": {
      "description": "block.wal 的块设备名称。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "wal_dev_size": {
      "description": "block.wal 的大小，单位为 GiB。",
      "minimum": 0.5,
      "optional": 1,
      "requires": "wal_dev",
      "type": "number",
      "typetext": "<number> (0.5 - N)",
      "verbose_description": "如果请求 block.wal 但未给出大小，将依次从 ceph 数据库（osd 或 global 配置节）或配置（osd 或 global 配置节）中的 bluestore_block_wal_size 自动选择。如果不可用，则大小设为 OSD 设备大小的 1%。如果可用空间不足则失败。"
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
