# `/access/permissions`

原始接口路径：`/access/permissions`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/permissions`

Retrieve effective permissions of given user/token.

**权限**

```json
{
  "description": "Each user/token is allowed to dump their own permissions (or that of owned tokens). A user can dump the permissions of another user or their tokens if they have 'Sys.Audit' permission on /access.",
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
| `path` | string | 否 | — | Only dump this specific path, not the whole tree. |
| `userid` | string | 否 | — | User ID or full API token ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "path": {
      "description": "Only dump this specific path, not the whole tree.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "userid": {
      "description": "User ID or full API token ID",
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
  "description": "Map of \"path\" => (Map of \"privilege\" => \"propagate boolean\").",
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/permissions)。
