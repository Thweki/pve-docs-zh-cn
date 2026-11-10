# `/cluster/ceph/metadata`

原始接口路径：`/cluster/ceph/metadata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/ceph/metadata`

获取 ceph 元数据。

**方法标识：** `metadata`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Datastore.Audit"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `scope` | string | 否 | "all" | 要返回的元数据类别：'all' 在每个守护进程的元数据中加入 PVE 端的服务状态（单元、数据目录是否存在）；'versions' 仅收集各节点的 Ceph 二进制程序版本数据。；可选值：`all`, `versions` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "scope": {
      "default": "all",
      "description": "要返回的元数据类别：'all' 在每个守护进程的元数据中加入 PVE 端的服务状态（单元、数据目录是否存在）；'versions' 仅收集各节点的 Ceph 二进制程序版本数据。",
      "enum": [
        "all",
        "versions"
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
  "description": "每种服务类型的条目，包含各实例的对象。",
  "properties": {
    "mds": {
      "additionalProperties": {
        "additionalProperties": 1,
        "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "addr": {
            "description": "绑定地址和端口。",
            "optional": 1,
            "type": "string"
          },
          "ceph_release": {
            "description": "当前使用的 Ceph 发行版代号。",
            "type": "string"
          },
          "ceph_version": {
            "description": "服务当前使用的版本信息。",
            "type": "string"
          },
          "ceph_version_short": {
            "description": "服务当前使用的简短版本（数字）信息。",
            "type": "string"
          },
          "hostname": {
            "description": "运行此服务的主机名。",
            "type": "string"
          },
          "mem_swap_kb": {
            "description": "此服务当前位于交换空间中的内存。",
            "type": "integer"
          },
          "mem_total_kb": {
            "description": "此服务的内存用量。",
            "type": "integer"
          },
          "name": {
            "description": "服务实例名称。",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
      },
      "description": "集群中配置的元数据服务器及其属性，以 '<name>@<host>' 为键。",
      "type": "object"
    },
    "mgr": {
      "additionalProperties": {
        "additionalProperties": 1,
        "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "addr": {
            "description": "绑定地址。",
            "optional": 1,
            "type": "string"
          },
          "ceph_release": {
            "description": "当前使用的 Ceph 发行版代号。",
            "type": "string"
          },
          "ceph_version": {
            "description": "服务当前使用的版本信息。",
            "type": "string"
          },
          "ceph_version_short": {
            "description": "服务当前使用的简短版本（数字）信息。",
            "type": "string"
          },
          "hostname": {
            "description": "运行此服务的主机名。",
            "type": "string"
          },
          "mem_swap_kb": {
            "description": "此服务当前位于交换空间中的内存。",
            "type": "integer"
          },
          "mem_total_kb": {
            "description": "此服务的内存用量。",
            "type": "integer"
          },
          "name": {
            "description": "服务实例名称。",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
      },
      "description": "集群中配置的管理器及其属性，以 '<name>@<host>' 为键。",
      "type": "object"
    },
    "mon": {
      "additionalProperties": {
        "additionalProperties": 1,
        "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "addrs": {
            "description": "绑定地址和端口。",
            "optional": 1,
            "type": "string"
          },
          "ceph_release": {
            "description": "当前使用的 Ceph 发行版代号。",
            "type": "string"
          },
          "ceph_version": {
            "description": "服务当前使用的版本信息。",
            "type": "string"
          },
          "ceph_version_short": {
            "description": "服务当前使用的简短版本（数字）信息。",
            "type": "string"
          },
          "hostname": {
            "description": "运行此服务的主机名。",
            "type": "string"
          },
          "mem_swap_kb": {
            "description": "此服务当前位于交换空间中的内存。",
            "type": "integer"
          },
          "mem_total_kb": {
            "description": "此服务的内存用量。",
            "type": "integer"
          },
          "name": {
            "description": "服务实例名称。",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
      },
      "description": "集群中配置的监视器及其属性，以 '<name>@<host>' 为键。",
      "type": "object"
    },
    "node": {
      "additionalProperties": {
        "additionalProperties": 1,
        "properties": {
          "buildcommit": {
            "description": "构建所用的 GIT 提交。",
            "type": "string"
          },
          "version": {
            "description": "版本信息。",
            "properties": {
              "parts": {
                "description": "主版本号、次版本号和补丁版本号。",
                "items": {
                  "description": "版本组成部分字符串。",
                  "type": "string"
                },
                "type": "array"
              },
              "str": {
                "description": "以单个字符串表示的版本。",
                "type": "string"
              }
            },
            "type": "object"
          }
        },
        "type": "object"
      },
      "description": "节点上安装的 Ceph 版本，以节点名称为键。",
      "type": "object"
    },
    "osd": {
      "description": "集群中配置的 OSD 及其属性。",
      "items": {
        "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "back_addr": {
            "description": "OSD 之间后端流量的绑定地址和端口。",
            "type": "string"
          },
          "ceph_release": {
            "description": "当前使用的 Ceph 发行版代号。",
            "type": "string"
          },
          "ceph_version": {
            "description": "服务当前使用的版本信息。",
            "type": "string"
          },
          "ceph_version_short": {
            "description": "服务当前使用的简短版本（数字）信息。",
            "type": "string"
          },
          "device_ids": {
            "description": "以逗号连接的设备标识符列表（例如 'sdb=<serial>,sdc=<serial>'）。",
            "optional": 1,
            "type": "string"
          },
          "device_paths": {
            "description": "底层设备的 /dev/disk/by-path 条目列表，以逗号连接。",
            "optional": 1,
            "type": "string"
          },
          "devices": {
            "description": "以逗号连接的底层设备名称列表（例如 'sdb,sdc'）。",
            "optional": 1,
            "type": "string"
          },
          "front_addr": {
            "description": "到 OSD 的前端流量的绑定地址和端口。",
            "type": "string"
          },
          "hostname": {
            "description": "运行此服务的主机名。",
            "type": "string"
          },
          "id": {
            "description": "OSD ID。",
            "type": "integer"
          },
          "mem_swap_kb": {
            "description": "此服务当前位于交换空间中的内存。",
            "type": "integer"
          },
          "mem_total_kb": {
            "description": "此服务的内存用量。",
            "type": "integer"
          },
          "osd_data": {
            "description": "OSD 数据目录的路径。",
            "type": "string"
          },
          "osd_objectstore": {
            "description": "OSD 对象存储类型。",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/metadata)。
