# `/cluster/firewall/macros`

原始接口路径：`/cluster/firewall/macros`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/macros`

列出可用宏

**方法标识：** `get_macros`

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
      "descr": {
        "description": "更详细的描述（如有）。",
        "type": "string"
      },
      "macro": {
        "description": "宏名称。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/macros)。
