# `/nodes/{node}/ceph/osd/{osdid}/metadata`

原始接口路径：`/nodes/{node}/ceph/osd/{osdid}/metadata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/osd/{osdid}/metadata`

获取 OSD 详情

**方法标识：** `osddetails`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `osdid` | integer | 是 | — | OSD ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
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
  "properties": {
    "devices": {
      "description": "包含设备数据的数组",
      "items": {
        "properties": {
          "dev_node": {
            "description": "设备节点",
            "type": "string"
          },
          "device": {
            "description": "OSD 设备种类",
            "enum": [
              "block",
              "db",
              "wal"
            ],
            "type": "string"
          },
          "physical_device": {
            "description": "此 OSD 设备使用的底层物理设备（多个时以逗号或空格连接）。",
            "type": "string"
          },
          "size": {
            "description": "OSD 设备大小，单位为字节。",
            "type": "integer"
          },
          "support_discard": {
            "description": "底层物理设备是否支持 discard/TRIM。",
            "type": "boolean"
          },
          "type": {
            "description": "设备类型。例如 hdd 或 ssd",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "osd": {
      "description": "OSD 的常规信息",
      "properties": {
        "back_addr": {
          "description": "用于与其他 OSD 通信的地址和端口。",
          "type": "string"
        },
        "encrypted": {
          "description": "OSD 是否通过 dm-crypt 使用 LUKS 加密。",
          "type": "boolean"
        },
        "front_addr": {
          "description": "用于与客户端和监视器通信的地址和端口。",
          "type": "string"
        },
        "hb_back_addr": {
          "description": "面向其他 OSD 的心跳地址和端口。",
          "type": "string"
        },
        "hb_front_addr": {
          "description": "面向客户端和监视器的心跳地址和端口。",
          "type": "string"
        },
        "hostname": {
          "description": "包含此 OSD 的宿主机名称。",
          "type": "string"
        },
        "id": {
          "description": "OSD 的 ID。",
          "type": "integer"
        },
        "mem_usage": {
          "description": "OSD 守护进程的比例集大小（PSS）内存用量，单位为字节；进程未运行时为 0。",
          "type": "integer"
        },
        "osd_data": {
          "description": "OSD 数据目录的路径。",
          "type": "string"
        },
        "osd_objectstore": {
          "description": "使用的对象存储类型。",
          "type": "string"
        },
        "pid": {
          "description": "OSD 进程 ID；如果此 OSD 的 systemd 单元当前未运行，则不存在此项。",
          "optional": 1,
          "type": "integer"
        },
        "version": {
          "description": "OSD 服务的 Ceph 版本。",
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/osd/{osdid}/metadata)。
