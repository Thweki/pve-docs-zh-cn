# `/cluster/sdn/lock`

原始接口路径：`/cluster/sdn/lock`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/lock`

Release global lock for SDN configuration

**权限**

```json
{
  "check": [
    "perm",
    "/sdn",
    [
      "SDN.Allocate"
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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `force` | boolean | 否 | 0 | if true, allow releasing lock without providing the token |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "if true, allow releasing lock without providing the token",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## POST `/cluster/sdn/lock`

Acquire global lock for SDN configuration

**权限**

```json
{
  "check": [
    "perm",
    "/sdn",
    [
      "SDN.Allocate"
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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `allow-pending` | boolean | 否 | 0 | if true, allow acquiring lock even though there are pending changes |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "allow-pending": {
      "default": 0,
      "description": "if true, allow acquiring lock even though there are pending changes",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/lock)。
