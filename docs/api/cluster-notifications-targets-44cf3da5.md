# `/cluster/notifications/targets`

原始接口路径：`/cluster/notifications/targets`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/targets`

返回所有可用作通知目标的实体列表。

**方法标识：** `get_all_targets`

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
    ],
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Use"
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
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "comment": {
        "description": "注释",
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "default": 0,
        "description": "显示此目标是否已禁用",
        "optional": 1,
        "type": "boolean"
      },
      "name": {
        "description": "目标名称。",
        "format": "pve-configid",
        "type": "string"
      },
      "origin": {
        "description": "显示此条目是用户创建还是内置",
        "enum": [
          "user-created",
          "builtin",
          "modified-builtin"
        ],
        "type": "string"
      },
      "type": {
        "description": "目标类型。",
        "enum": [
          "sendmail",
          "gotify",
          "smtp",
          "webhook"
        ],
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/targets)。
