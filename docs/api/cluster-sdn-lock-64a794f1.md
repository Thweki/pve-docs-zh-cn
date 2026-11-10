# `/cluster/sdn/lock`

原始接口路径：`/cluster/sdn/lock`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/lock`

释放 SDN 配置的全局锁

**方法标识：** `release_lock`

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
| `force` | boolean | 否 | 0 | 如果为 true，则允许在未提供令牌的情况下释放锁 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "如果为 true，则允许在未提供令牌的情况下释放锁",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
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

获取 SDN 配置的全局锁

**方法标识：** `lock`

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
| `allow-pending` | boolean | 否 | 0 | 如果为 true，则即使有待应用的更改，也允许获取锁 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "allow-pending": {
      "default": 0,
      "description": "如果为 true，则即使有待应用的更改，也允许获取锁",
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
