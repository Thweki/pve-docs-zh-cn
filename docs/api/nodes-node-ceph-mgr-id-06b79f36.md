# `/nodes/{node}/ceph/mgr/{id}`

原始接口路径：`/nodes/{node}/ceph/mgr/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/mgr/{id}`

销毁 Ceph 管理器。

**方法标识：** `destroymgr`

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
| `id` | string | 是 | — | 管理器的 ID |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "管理器的 ID",
      "pattern": "[a-zA-Z0-9]([a-zA-Z0-9\\-]*[a-zA-Z0-9])?",
      "type": "string"
    },
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
  "type": "string"
}
```

## POST `/nodes/{node}/ceph/mgr/{id}`

创建 Ceph 管理器

**方法标识：** `createmgr`

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
| `id` | string | 否 | "nodename" | 管理器的 ID，省略时与节点名称相同。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "default": "nodename",
      "description": "管理器的 ID，省略时与节点名称相同。",
      "maxLength": 200,
      "optional": 1,
      "pattern": "[a-zA-Z0-9]([a-zA-Z0-9\\-]*[a-zA-Z0-9])?",
      "type": "string"
    },
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/mgr/{id})。
