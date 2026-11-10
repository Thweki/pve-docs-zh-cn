# `/cluster/log`

原始接口路径：`/cluster/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/log`

Read cluster log

**方法标识：** `log`

**权限**

```json
{
  "description": "The user needs 'Sys.Syslog' on '/' in order to get all logs.",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `max` | integer | 否 | — | Maximum number of entries. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max": {
      "description": "Maximum number of entries.",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "properties": {},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/log)。
