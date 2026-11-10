# `/nodes/{node}/ceph/restart`

原始接口路径：`/nodes/{node}/ceph/restart`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/ceph/restart`

重启 ceph 服务。

**方法标识：** `restart`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `service` | string | 否 | "ceph.target" | Ceph 服务名称。 |

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
    },
    "service": {
      "default": "ceph.target",
      "description": "Ceph 服务名称。",
      "optional": 1,
      "pattern": "(ceph|mon|mds|osd|mgr)(\\.[a-zA-Z0-9]([a-zA-Z0-9\\-]*[a-zA-Z0-9])?)?",
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/restart)。
