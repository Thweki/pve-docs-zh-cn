# `/nodes/{node}/ceph/osd/{osdid}/lv-info`

原始接口路径：`/nodes/{node}/ceph/osd/{osdid}/lv-info`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/osd/{osdid}/lv-info`

Get OSD volume details

**方法标识：** `osdvolume`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
    ],
    "any",
    1
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
| `node` | string | 是 | — | The cluster node name. |
| `osdid` | integer | 是 | — | OSD ID |
| `type` | string | 否 | "block" | OSD device type；可选值：`block`, `db`, `wal` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    },
    "type": {
      "default": "block",
      "description": "OSD device type",
      "enum": [
        "block",
        "db",
        "wal"
      ],
      "optional": 1,
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "creation_time": {
      "description": "Creation time as reported by `lvs`.",
      "type": "string"
    },
    "lv_name": {
      "description": "Name of the logical volume (LV).",
      "type": "string"
    },
    "lv_path": {
      "description": "Path to the logical volume (LV).",
      "type": "string"
    },
    "lv_size": {
      "description": "Size of the logical volume (LV).",
      "type": "integer"
    },
    "lv_uuid": {
      "description": "UUID of the logical volume (LV).",
      "type": "string"
    },
    "vg_name": {
      "description": "Name of the volume group (VG).",
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/osd/{osdid}/lv-info)。
