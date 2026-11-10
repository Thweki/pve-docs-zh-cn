# `/nodes/{node}/journal`

原始接口路径：`/nodes/{node}/journal`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/journal`

读取 Journal 日志

**方法标识：** `journal`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Syslog"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `endcursor` | string | 否 | — | 在给定 Cursor 之前结束。与 'until' 冲突 |
| `identifiers` | boolean | 否 | 0 | 同时返回一条记录，列出存在的不同 syslog 标识符，用于过滤器补全。仅与 'structured' 一同使用时生效。 |
| `kernel` | boolean | 否 | 0 | 仅输出内核消息。 |
| `lastentries` | integer | 否 | — | 限制为最后 X 行。与范围设置冲突。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `priority` | string | 否 | — | 仅输出此 syslog 优先级的消息：可以是 0（emerg）到 7（debug）之间的单个级别，选择该级别及所有更严重的级别，或 'LOW..HIGH' 范围。留空表示不按优先级过滤。 |
| `service` | string | 否 | — | 仅输出 syslog 标识符匹配此通配模式的消息，例如 'pve*' 或 'postfix/*'。 |
| `since` | integer | 否 | — | 显示从此 UNIX 时间戳开始的所有日志。与 'startcursor' 冲突。 |
| `startcursor` | string | 否 | — | 在给定 Cursor 之后开始。与 'since' 冲突 |
| `structured` | boolean | 否 | 0 | 每个条目返回一个具有独立字段（timestamp、identifier、message、priority 等）的 JSON 对象，而非预先渲染的文本行。 |
| `unit` | string | 否 | — | 仅输出此 systemd 单元的消息（隐含 .service 后缀）。 |
| `units` | boolean | 否 | 0 | 同时返回一条记录，列出存在的不同 systemd 单元，用于过滤器补全。仅与 'structured' 一同使用时生效。 |
| `until` | integer | 否 | — | 显示截至此 UNIX 时间戳的所有日志。与 'endcursor' 冲突。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "endcursor": {
      "description": "在给定 Cursor 之前结束。与 'until' 冲突",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "identifiers": {
      "default": 0,
      "description": "同时返回一条记录，列出存在的不同 syslog 标识符，用于过滤器补全。仅与 'structured' 一同使用时生效。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "kernel": {
      "default": 0,
      "description": "仅输出内核消息。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lastentries": {
      "description": "限制为最后 X 行。与范围设置冲突。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "priority": {
      "description": "仅输出此 syslog 优先级的消息：可以是 0（emerg）到 7（debug）之间的单个级别，选择该级别及所有更严重的级别，或 'LOW..HIGH' 范围。留空表示不按优先级过滤。",
      "optional": 1,
      "pattern": "^([0-7](\\.\\.[0-7])?)?$",
      "type": "string"
    },
    "service": {
      "description": "仅输出 syslog 标识符匹配此通配模式的消息，例如 'pve*' 或 'postfix/*'。",
      "maxLength": 128,
      "optional": 1,
      "pattern": "^[A-Za-z0-9_.@:*?!\\[\\]\\/-]+$",
      "type": "string"
    },
    "since": {
      "description": "显示从此 UNIX 时间戳开始的所有日志。与 'startcursor' 冲突。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "startcursor": {
      "description": "在给定 Cursor 之后开始。与 'since' 冲突",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "structured": {
      "default": 0,
      "description": "每个条目返回一个具有独立字段（timestamp、identifier、message、priority 等）的 JSON 对象，而非预先渲染的文本行。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "unit": {
      "description": "仅输出此 systemd 单元的消息（隐含 .service 后缀）。",
      "maxLength": 256,
      "optional": 1,
      "pattern": "^[A-Za-z0-9_.@:-]+$",
      "type": "string"
    },
    "units": {
      "default": 0,
      "description": "同时返回一条记录，列出存在的不同 systemd 单元，用于过滤器补全。仅与 'structured' 一同使用时生效。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "until": {
      "description": "显示截至此 UNIX 时间戳的所有日志。与 'endcursor' 冲突。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "type": "string"
  },
  "type": "array"
}
```

<details>
<summary>其他接口元数据</summary>

```json
{
  "download_allowed": 1
}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/journal)。
