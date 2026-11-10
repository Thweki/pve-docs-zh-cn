# `/cluster/notifications/matcher-field-values`

原始接口路径：`/cluster/notifications/matcher-field-values`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/matcher-field-values`

Returns known notification metadata fields and their known values

**方法标识：** `get_matcher_field_values`

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
        "description": "Additional comment for this value.",
        "optional": 1,
        "type": "string"
      },
      "field": {
        "description": "Field this value belongs to.",
        "type": "string"
      },
      "value": {
        "description": "Notification metadata value known by the system.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matcher-field-values)。
