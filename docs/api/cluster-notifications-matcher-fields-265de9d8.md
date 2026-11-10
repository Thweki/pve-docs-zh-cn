# `/cluster/notifications/matcher-fields`

原始接口路径：`/cluster/notifications/matcher-fields`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/matcher-fields`

返回已知的通知元数据字段

**方法标识：** `get_matcher_fields`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Audit"
      ]
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
0
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "name": {
        "description": "字段名称。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matcher-fields)。
