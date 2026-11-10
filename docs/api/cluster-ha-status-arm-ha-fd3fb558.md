# `/cluster/ha/status/arm-ha`

原始接口路径：`/cluster/ha/status/arm-ha`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ha/status/arm-ha`

请求在 HA 堆栈解除布防后重新布防。

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Console"
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/arm-ha)。
