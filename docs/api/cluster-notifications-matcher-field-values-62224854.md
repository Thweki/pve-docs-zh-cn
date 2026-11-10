# `/cluster/notifications/matcher-field-values`

原始接口路径：`/cluster/notifications/matcher-field-values`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/matcher-field-values`

返回已知的通知元数据字段及其已知值

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
        "description": "此值的额外注释。",
        "optional": 1,
        "type": "string"
      },
      "field": {
        "description": "此值所属的字段。",
        "type": "string"
      },
      "value": {
        "description": "系统已知的通知元数据值。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matcher-field-values)。
