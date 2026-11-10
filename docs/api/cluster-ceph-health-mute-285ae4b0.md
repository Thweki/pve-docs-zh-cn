# `/cluster/ceph/health-mute`

原始接口路径：`/cluster/ceph/health-mute`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/health-mute`

获取当前已静默的 Ceph 健康检查。

**方法标识：** `health_mute_index`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Datastore.Audit"
    ],
    "any",
    1
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
  "items": {
    "properties": {
      "code": {
        "description": "已静默的健康检查。",
        "type": "string"
      },
      "sticky": {
        "description": "检查情况恶化后是否仍保持静默。",
        "type": "boolean"
      },
      "summary": {
        "description": "检查报告的内容。",
        "optional": 1,
        "type": "string"
      },
      "ttl": {
        "description": "静默到期时间。若不会到期则不存在此项。",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/health-mute)。
