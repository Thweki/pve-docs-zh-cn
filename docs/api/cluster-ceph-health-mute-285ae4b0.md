# `/cluster/ceph/health-mute`

原始接口路径：`/cluster/ceph/health-mute`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/health-mute`

Get the currently muted Ceph health checks.

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
        "description": "The muted health check.",
        "type": "string"
      },
      "sticky": {
        "description": "Whether the mute survives the check getting worse.",
        "type": "boolean"
      },
      "summary": {
        "description": "What the check reports.",
        "optional": 1,
        "type": "string"
      },
      "ttl": {
        "description": "When the mute expires. Absent if it does not.",
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
