# `/nodes/{node}/ceph/osd/{osdid}/scrub`

原始接口路径：`/nodes/{node}/ceph/osd/{osdid}/scrub`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/ceph/osd/{osdid}/scrub`

Instruct the OSD to scrub.

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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `deep` | boolean | 否 | 0 | If set, instructs a deep scrub instead of a normal one. |
| `node` | string | 是 | — | The cluster node name. |
| `osdid` | integer | 是 | — | OSD ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "deep": {
      "default": 0,
      "description": "If set, instructs a deep scrub instead of a normal one.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "osdid": {
      "description": "OSD ID",
      "type": "integer",
      "typetext": "<integer>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/osd/{osdid}/scrub)。
