# `/cluster/config/qdevice`

原始接口路径：`/cluster/config/qdevice`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/config/qdevice`

Get QDevice status

**方法标识：** `status`

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
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/qdevice)。
