# `/cluster/backup-info`

原始接口路径：`/cluster/backup-info`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/backup-info`

备份信息相关端点的索引

**方法标识：** `index`

**允许 API 令牌**

```json
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "description": "目录索引。",
  "items": {
    "properties": {
      "subdir": {
        "description": "API 子目录端点",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{subdir}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup-info)。
