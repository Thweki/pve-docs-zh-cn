# `/nodes`

原始接口路径：`/nodes`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes`

Cluster node index.

**方法标识：** `index`

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

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
      "cpu": {
        "description": "CPU utilization.",
        "optional": 1,
        "renderer": "fraction_as_percentage",
        "type": "number"
      },
      "level": {
        "description": "Support level.",
        "optional": 1,
        "type": "string"
      },
      "maxcpu": {
        "description": "Number of available CPUs.",
        "optional": 1,
        "type": "integer"
      },
      "maxmem": {
        "description": "Number of available memory in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "mem": {
        "description": "Used memory in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "node": {
        "description": "The cluster node name.",
        "format": "pve-node",
        "type": "string"
      },
      "ssl_fingerprint": {
        "description": "The SSL fingerprint for the node certificate.",
        "optional": 1,
        "type": "string"
      },
      "status": {
        "description": "Node status.",
        "enum": [
          "unknown",
          "online",
          "offline"
        ],
        "type": "string"
      },
      "uptime": {
        "description": "Node uptime in seconds.",
        "optional": 1,
        "renderer": "duration",
        "type": "integer"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{node}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes)。
