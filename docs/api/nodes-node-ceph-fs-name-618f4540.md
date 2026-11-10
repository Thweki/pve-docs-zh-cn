# `/nodes/{node}/ceph/fs/{name}`

原始接口路径：`/nodes/{node}/ceph/fs/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/fs/{name}`

销毁 Ceph 文件系统。如果仍有未禁用的 'cephfs' 类型 PVE 存储条目引用此文件系统，则拒绝操作。也可选择移除存储条目和/或底层元数据池与数据池。

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
| `name` | string | 是 | — | Ceph 文件系统名称。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `remove-pools` | boolean | 否 | 0 | 移除此文件系统使用的元数据池和数据池。 |
| `remove-storages` | boolean | 否 | 0 | 移除为此文件系统配置的、由 pveceph 管理的存储。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "Ceph 文件系统名称。",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "remove-pools": {
      "default": 0,
      "description": "移除此文件系统使用的元数据池和数据池。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "remove-storages": {
      "default": 0,
      "description": "移除为此文件系统配置的、由 pveceph 管理的存储。",
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

创建 Ceph 文件系统

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
| `add-storage` | boolean | 否 | 0 | 将创建的 CephFS 配置为此集群的存储。 |
| `name` | string | 否 | "cephfs" | Ceph 文件系统名称。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `pg_num` | integer | 否 | 128 | 底层数据池的归置组数量。元数据池将使用此数量的四分之一。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "add-storage": {
      "default": 0,
      "description": "将创建的 CephFS 配置为此集群的存储。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "default": "cephfs",
      "description": "Ceph 文件系统名称。",
      "optional": 1,
      "pattern": "(?^:^[^:/\\s]+$)",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pg_num": {
      "default": 128,
      "description": "底层数据池的归置组数量。元数据池将使用此数量的四分之一。",
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
