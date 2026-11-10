# `/nodes/{node}/ceph/mon/{monid}`

原始接口路径：`/nodes/{node}/ceph/mon/{monid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/ceph/mon/{monid}`

销毁 Ceph 监视器。拒绝移除集群的最后一个监视器。不会销毁同一节点上的任何管理器；如需销毁，请使用 /nodes/{node}/ceph/mgr/{id}。

**方法标识：** `destroymon`

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
| `monid` | string | 是 | — | 监视器 ID |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "monid": {
      "description": "监视器 ID",
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

## POST `/nodes/{node}/ceph/mon/{monid}`

创建 Ceph 监视器。对于首个监视器，还会自动创建管理器。

**方法标识：** `createmon`

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
| `mon-address` | string | 否 | — | 覆盖自动检测到的监视器 IP 地址。必须位于 Ceph 的公共网络中。 |
| `monid` | string | 否 | "nodename" | 监视器的 ID，省略时与节点名称相同。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "mon-address": {
      "description": "覆盖自动检测到的监视器 IP 地址。必须位于 Ceph 的公共网络中。",
      "format": "ip-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "monid": {
      "default": "nodename",
      "description": "监视器的 ID，省略时与节点名称相同。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/mon/{monid})。
