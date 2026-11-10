# `/cluster/config/apiversion`

原始接口路径：`/cluster/config/apiversion`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/config/apiversion`

返回此节点上可用的集群加入 API 版本。

**方法标识：** `join_api_version`

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
  "description": "集群加入 API 版本，目前为 1",
  "minimum": 0,
  "type": "integer"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/apiversion)。
