# `/cluster/nextid`

原始接口路径：`/cluster/nextid`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/nextid`

获取下一个空闲 VMID。传入 VMID 可确认其是否空闲（以检查时为准）。

**方法标识：** `nextid`

**权限**

```json
{
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
| `vmid` | integer | 否 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "下一个空闲 VMID。",
  "type": "integer"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/nextid)。
