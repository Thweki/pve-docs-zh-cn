# `/cluster/tasks`

原始接口路径：`/cluster/tasks`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/tasks`

List recent tasks (cluster wide).

**方法标识：** `tasks`

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
      "upid": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/tasks)。
