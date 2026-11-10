# `/cluster/jobs/realm-sync`

原始接口路径：`/cluster/jobs/realm-sync`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/jobs/realm-sync`

列出已配置的 realm-sync 作业。

**方法标识：** `syncjob_index`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
    ]
  ]
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
      "comment": {
        "description": "作业注释。",
        "optional": 1,
        "type": "string"
      },
      "enabled": {
        "description": "作业是否启用。",
        "type": "boolean"
      },
      "id": {
        "description": "条目的 ID。",
        "type": "string"
      },
      "last-run": {
        "description": "作业上次执行时间，以自 UNIX 纪元起的秒数表示",
        "optional": 1,
        "type": "integer"
      },
      "next-run": {
        "description": "作业下次计划执行时间，以自 UNIX 纪元起的秒数表示。",
        "optional": 1,
        "type": "integer"
      },
      "realm": {
        "description": "认证域 ID",
        "format": "pve-realm",
        "maxLength": 32,
        "type": "string"
      },
      "remove-vanished": {
        "default": "none",
        "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
        "optional": "1",
        "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
        "type": "string",
        "typetext": "([acl];[properties];[entry])|none"
      },
      "schedule": {
        "description": "已配置的同步计划。",
        "type": "string"
      },
      "scope": {
        "description": "选择要同步的内容。",
        "enum": [
          "users",
          "groups",
          "both"
        ],
        "optional": "1",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/realm-sync)。
