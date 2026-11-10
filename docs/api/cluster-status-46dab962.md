# `/cluster/status`

原始接口路径：`/cluster/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/status`

获取集群状态信息。

**方法标识：** `get_status`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "id": {
        "type": "string"
      },
      "ip": {
        "description": "[node] 解析节点名称得到的 IP 地址。",
        "optional": 1,
        "type": "string"
      },
      "level": {
        "description": "[node] Proxmox VE 订阅级别，表明是否有资格获得企业支持及访问稳定的 Proxmox VE Enterprise Repository。",
        "optional": 1,
        "type": "string"
      },
      "local": {
        "description": "[node] 表明是否为作出响应的节点。",
        "optional": 1,
        "type": "boolean"
      },
      "name": {
        "type": "string"
      },
      "nodeid": {
        "description": "[node] corosync 配置中的节点 ID。",
        "optional": 1,
        "type": "integer"
      },
      "nodes": {
        "description": "[cluster] 节点数量，包括离线节点。",
        "optional": 1,
        "type": "integer"
      },
      "online": {
        "description": "[node] 表明节点在线还是离线。",
        "optional": 1,
        "type": "boolean"
      },
      "quorate": {
        "description": "[cluster] 表明是否有多数节点在线以进行决策",
        "optional": 1,
        "type": "boolean"
      },
      "type": {
        "description": "表明类型，为 cluster 或 node。类型定义对象属性，例如 quorate 适用于 cluster 类型。",
        "enum": [
          "cluster",
          "node"
        ],
        "type": "string"
      },
      "version": {
        "description": "[cluster] corosync 配置文件的当前版本。",
        "optional": 1,
        "type": "integer"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/status)。
