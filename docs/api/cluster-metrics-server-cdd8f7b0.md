# `/cluster/metrics/server`

原始接口路径：`/cluster/metrics/server`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/metrics/server`

List configured metric servers.

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
        "description": "Flag to disable the plugin.",
        "type": "boolean"
      },
      "id": {
        "description": "The ID of the entry.",
        "type": "string"
      },
      "port": {
        "description": "Server network port",
        "type": "integer"
      },
      "server": {
        "description": "Server dns name or IP address",
        "type": "string"
      },
      "type": {
        "description": "Plugin type.",
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
