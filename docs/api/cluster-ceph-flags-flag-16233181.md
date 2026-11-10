# `/cluster/ceph/flags/{flag}`

原始接口路径：`/cluster/ceph/flags/{flag}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/flags/{flag}`

获取特定 ceph 标志的状态。

**方法标识：** `get_flag`

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
| `flag` | string | 是 | — | 要获取的标志名称。；可选值：`nobackfill`, `nodeep-scrub`, `nodown`, `noin`, `noout`, `norebalance`, `norecover`, `noscrub`, `notieragent`, `noup`, `pause` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "flag": {
      "description": "要获取的标志名称。",
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

设置或清除（取消设置）特定 Ceph 标志。同步运行（不同于会派生工作任务的批量 PUT /cluster/ceph/flags 端点）。

**方法标识：** `update_flag`

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
| `flag` | string | 是 | — | 要更新的 ceph 标志；可选值：`nobackfill`, `nodeep-scrub`, `nodown`, `noin`, `noout`, `norebalance`, `norecover`, `noscrub`, `notieragent`, `noup`, `pause` |
| `value` | boolean | 是 | — | 标志的新值 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "flag": {
      "description": "要更新的 ceph 标志",
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
      "description": "标志的新值",
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
