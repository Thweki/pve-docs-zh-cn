# `/nodes`

原始接口路径：`/nodes`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes`

集群节点索引。

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
        "description": "CPU 使用率。",
        "optional": 1,
        "renderer": "fraction_as_percentage",
        "type": "number"
      },
      "level": {
        "description": "支持级别。",
        "optional": 1,
        "type": "string"
      },
      "maxcpu": {
        "description": "可用 CPU 数量。",
        "optional": 1,
        "type": "integer"
      },
      "maxmem": {
        "description": "可用内存字节数。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "mem": {
        "description": "已用内存字节数。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "node": {
        "description": "集群节点名称。",
        "format": "pve-node",
        "type": "string"
      },
      "ssl_fingerprint": {
        "description": "节点证书的 SSL 指纹。",
        "optional": 1,
        "type": "string"
      },
      "status": {
        "description": "节点状态。",
        "enum": [
          "unknown",
          "online",
          "offline"
        ],
        "type": "string"
      },
      "uptime": {
        "description": "节点运行时间，单位为秒。",
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
