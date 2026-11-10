# `/cluster/ceph/flags/{flag}`

原始接口路径：`/cluster/ceph/flags/{flag}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/flags/{flag}`

Get the status of a specific ceph flag.

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

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `flag` | string | 是 | — | The name of the flag name to get.；可选值：`nobackfill`, `nodeep-scrub`, `nodown`, `noin`, `noout`, `norebalance`, `norecover`, `noscrub`, `notieragent`, `noup`, `pause` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "flag": {
      "description": "The name of the flag name to get.",
      "enum": [
        "nobackfill",
        "nodeep-scrub",
        "nodown",
        "noin",
        "noout",
        "norebalance",
        "norecover",
        "noscrub",
        "notieragent",
        "noup",
        "pause"
      ],
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "boolean"
}
```

## PUT `/cluster/ceph/flags/{flag}`

Set or clear (unset) a specific Ceph flag. Runs synchronously (unlike the bulk PUT /cluster/ceph/flags endpoint, which forks a worker task).

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
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
| `flag` | string | 是 | — | The ceph flag to update；可选值：`nobackfill`, `nodeep-scrub`, `nodown`, `noin`, `noout`, `norebalance`, `norecover`, `noscrub`, `notieragent`, `noup`, `pause` |
| `value` | boolean | 是 | — | The new value of the flag |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "flag": {
      "description": "The ceph flag to update",
      "enum": [
        "nobackfill",
        "nodeep-scrub",
        "nodown",
        "noin",
        "noout",
        "norebalance",
        "norecover",
        "noscrub",
        "notieragent",
        "noup",
        "pause"
      ],
      "type": "string"
    },
    "value": {
      "description": "The new value of the flag",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/flags/{flag})。
