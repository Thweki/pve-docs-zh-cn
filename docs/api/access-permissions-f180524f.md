# `/access/permissions`

原始接口路径：`/access/permissions`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/permissions`

获取给定用户/令牌的有效权限。

**方法标识：** `permissions`

**权限**

```json
{
  "description": "每个用户/令牌都可以导出自己的权限（或所拥有令牌的权限）。如果用户对 /access. 具有 'Sys.Audit' 权限，则可以导出其他用户或其令牌的权限",
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
| `path` | string | 否 | — | 仅导出此特定路径，而非整棵树。 |
| `userid` | string | 否 | — | 用户 ID 或完整 API 令牌 ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "path": {
      "description": "仅导出此特定路径，而非整棵树。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "userid": {
      "description": "用户 ID 或完整 API 令牌 ID",
      "optional": 1,
      "pattern": "(?^:^(?^:[^\\s:/]+)\\@(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)(?:!(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+))?$)",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "\"path\" =>（\"privilege\" => \"propagate boolean\" 的映射）的映射。",
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/permissions)。
