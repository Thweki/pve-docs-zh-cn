# `/nodes/{node}/journal`

原始接口路径：`/nodes/{node}/journal`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/journal`

Read Journal

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
| `endcursor` | string | 否 | — | End before the given Cursor. Conflicts with 'until' |
| `identifiers` | boolean | 否 | 0 | Also return a record listing the distinct syslog identifiers present, for filter completion. Only honored together with 'structured'. |
| `kernel` | boolean | 否 | 0 | Only print kernel messages. |
| `lastentries` | integer | 否 | — | Limit to the last X lines. Conflicts with a range. |
| `node` | string | 是 | — | The cluster node name. |
| `priority` | string | 否 | — | Only print messages of this syslog priority: a single level from 0 (emerg) to 7 (debug), selecting that level and everything more severe, or a 'LOW..HIGH' range. Empty means no priority filter. |
| `service` | string | 否 | — | Only print messages whose syslog identifier matches this glob, for example 'pve*' or 'postfix/*'. |
| `since` | integer | 否 | — | Display all log since this UNIX epoch. Conflicts with 'startcursor'. |
| `startcursor` | string | 否 | — | Start after the given Cursor. Conflicts with 'since' |
| `structured` | boolean | 否 | 0 | Return one JSON object per entry with separate fields (timestamp, identifier, message, priority, ...) instead of pre-rendered text lines. |
| `unit` | string | 否 | — | Only print messages of this systemd unit (the .service suffix is implied). |
| `units` | boolean | 否 | 0 | Also return a record listing the distinct systemd units present, for filter completion. Only honored together with 'structured'. |
| `until` | integer | 否 | — | Display all log until this UNIX epoch. Conflicts with 'endcursor'. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "endcursor": {
      "description": "End before the given Cursor. Conflicts with 'until'",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "identifiers": {
      "default": 0,
      "description": "Also return a record listing the distinct syslog identifiers present, for filter completion. Only honored together with 'structured'.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "kernel": {
      "default": 0,
      "description": "Only print kernel messages.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lastentries": {
      "description": "Limit to the last X lines. Conflicts with a range.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "priority": {
      "description": "Only print messages of this syslog priority: a single level from 0 (emerg) to 7 (debug), selecting that level and everything more severe, or a 'LOW..HIGH' range. Empty means no priority filter.",
      "optional": 1,
      "pattern": "^([0-7](\\.\\.[0-7])?)?$",
      "type": "string"
    },
    "service": {
      "description": "Only print messages whose syslog identifier matches this glob, for example 'pve*' or 'postfix/*'.",
      "maxLength": 128,
      "optional": 1,
      "pattern": "^[A-Za-z0-9_.@:*?!\\[\\]\\/-]+$",
      "type": "string"
    },
    "since": {
      "description": "Display all log since this UNIX epoch. Conflicts with 'startcursor'.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "startcursor": {
      "description": "Start after the given Cursor. Conflicts with 'since'",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "structured": {
      "default": 0,
      "description": "Return one JSON object per entry with separate fields (timestamp, identifier, message, priority, ...) instead of pre-rendered text lines.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "unit": {
      "description": "Only print messages of this systemd unit (the .service suffix is implied).",
      "maxLength": 256,
      "optional": 1,
      "pattern": "^[A-Za-z0-9_.@:-]+$",
      "type": "string"
    },
    "units": {
      "default": 0,
      "description": "Also return a record listing the distinct systemd units present, for filter completion. Only honored together with 'structured'.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "until": {
      "description": "Display all log until this UNIX epoch. Conflicts with 'endcursor'.",
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
