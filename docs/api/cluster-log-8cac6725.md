# `/cluster/log`

原始接口路径：`/cluster/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/log`

读取集群日志

**方法标识：** `log`

**权限**

```json
{
  "description": "用户需要对 '/' 具有 'Sys.Syslog' 权限，才能获取所有日志。",
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
| `max` | integer | 否 | — | 最大条目数。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max": {
      "description": "最大条目数。",
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
