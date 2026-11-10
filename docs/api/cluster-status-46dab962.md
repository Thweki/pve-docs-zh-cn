# `/cluster/status`

原始接口路径：`/cluster/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/status`

Get cluster status information.

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
        "description": "[node] IP of the resolved nodename.",
        "optional": 1,
        "type": "string"
      },
      "level": {
        "description": "[node] Proxmox VE Subscription level, indicates if eligible for enterprise support as well as access to the stable Proxmox VE Enterprise Repository.",
        "optional": 1,
        "type": "string"
      },
      "local": {
        "description": "[node] Indicates if this is the responding node.",
        "optional": 1,
        "type": "boolean"
      },
      "name": {
        "type": "string"
      },
      "nodeid": {
        "description": "[node] ID of the node from the corosync configuration.",
        "optional": 1,
        "type": "integer"
      },
      "nodes": {
        "description": "[cluster] Nodes count, including offline nodes.",
        "optional": 1,
        "type": "integer"
      },
      "online": {
        "description": "[node] Indicates if the node is online or offline.",
        "optional": 1,
        "type": "boolean"
      },
      "quorate": {
        "description": "[cluster] Indicates if there is a majority of nodes online to make decisions",
        "optional": 1,
        "type": "boolean"
      },
      "type": {
        "description": "Indicates the type, either cluster or node. The type defines the object properties e.g. quorate available for type cluster.",
        "enum": [
          "cluster",
          "node"
        ],
        "type": "string"
      },
      "version": {
        "description": "[cluster] Current version of the corosync configuration file.",
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
