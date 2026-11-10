# `/nodes/{node}/ceph/mds/{name}`

原始接口路径：`/nodes/{node}/ceph/mds/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/mds/{name}`

销毁 Ceph 元数据服务器

**方法标识：** `destroymds`

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
| `name` | string | 是 | — | MDS 的名称（ID） |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "MDS 的名称（ID）",
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

## POST `/nodes/{node}/ceph/mds/{name}`

创建 Ceph 元数据服务器（MDS）

**方法标识：** `createmds`

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
| `hotstandby` | boolean | 否 | 0 | 确定 ceph-mds 守护进程是否轮询并重放活动 MDS 的日志。可在 MDS 故障时更快切换，但需要更多空闲资源。已弃用：此设置已在 Ceph 14.1.1 中移除。 |
| `name` | string | 否 | "nodename" | MDS 的 ID，省略时与节点名称相同 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "hotstandby": {
      "default": 0,
      "description": "确定 ceph-mds 守护进程是否轮询并重放活动 MDS 的日志。可在 MDS 故障时更快切换，但需要更多空闲资源。已弃用：此设置已在 Ceph 14.1.1 中移除。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "default": "nodename",
      "description": "MDS 的 ID，省略时与节点名称相同",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/mds/{name})。
