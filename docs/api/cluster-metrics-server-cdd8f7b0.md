# `/cluster/metrics/server`

原始接口路径：`/cluster/metrics/server`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/metrics/server`

列出已配置的指标服务器。

**方法标识：** `server_index`

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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "disable": {
        "description": "用于禁用插件的标志。",
        "type": "boolean"
      },
      "id": {
        "description": "条目的 ID。",
        "type": "string"
      },
      "port": {
        "description": "服务器网络端口",
        "type": "integer"
      },
      "server": {
        "description": "服务器 DNS 名称或 IP 地址",
        "type": "string"
      },
      "type": {
        "description": "插件类型。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics/server)。
