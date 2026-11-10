# `/cluster/resources`

原始接口路径：`/cluster/resources`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/resources`

资源索引（整个集群）。

**方法标识：** `resources`

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
| `type` | string | 否 | — | 资源类型。；可选值：`vm`, `storage`, `node`, `sdn` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "资源类型。",
      "enum": [
        "vm",
        "storage",
        "node",
        "sdn"
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
  "items": {
    "properties": {
      "cgroup-mode": {
        "description": "节点运行所用的 cgroup 模式（用于 'node' 类型）。",
        "optional": 1,
        "type": "integer"
      },
      "content": {
        "description": "允许的存储内容类型（用于 'storage' 类型）。",
        "format": "pve-storage-content-list",
        "optional": 1,
        "type": "string"
      },
      "cpu": {
        "description": "CPU 使用率（用于 'node'、'qemu' 和 'lxc' 类型）。",
        "minimum": 0,
        "optional": 1,
        "renderer": "fraction_as_percentage",
        "type": "number"
      },
      "disk": {
        "description": "已用磁盘空间，单位为字节（用于 'storage' 类型）；虚拟机已用根镜像空间（用于 'qemu' 和 'lxc' 类型）。",
        "minimum": 0,
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "diskread": {
        "description": "自客户机启动以来从其块设备读取的字节数。并非所有存储类型都提供此信息。（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "diskwrite": {
        "description": "自客户机启动以来写入其块设备的字节数。并非所有存储类型都提供此信息。（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "hastate": {
        "description": "HA 服务状态（用于 HA 管理的虚拟机）。",
        "optional": 1,
        "type": "string"
      },
      "host-arch": {
        "default": "x86_64",
        "description": "节点的 CPU 架构。（用于 'node' 类型）。",
        "enum": [
          "x86_64",
          "aarch64"
        ],
        "optional": 1,
        "type": "string"
      },
      "id": {
        "description": "资源 ID。",
        "type": "string"
      },
      "level": {
        "description": "支持级别（用于 'node' 类型）。",
        "optional": 1,
        "type": "string"
      },
      "lock": {
        "description": "客户机当前的配置锁（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "type": "string"
      },
      "maxcpu": {
        "description": "可用 CPU 数量（用于 'node'、'qemu' 和 'lxc' 类型）。",
        "minimum": 0,
        "optional": 1,
        "type": "number"
      },
      "maxdisk": {
        "description": "存储大小，单位为字节（用于 'storage' 类型）；虚拟机根镜像大小（用于 'qemu' 和 'lxc' 类型）。",
        "minimum": 0,
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "maxmem": {
        "description": "可用内存字节数（用于 'node'、'qemu' 和 'lxc' 类型）。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "mem": {
        "description": "已用内存字节数（用于 'node'、'qemu' 和 'lxc' 类型）。",
        "minimum": 0,
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "memhost": {
        "description": "从宿主机角度看到的已用内存字节数（用于 'qemu' 类型）。",
        "minimum": 0,
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "name": {
        "description": "资源名称。",
        "optional": 1,
        "type": "string"
      },
      "netin": {
        "description": "自客户机启动以来通过网络向其发送的流量字节数。（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "netout": {
        "description": "自客户机启动以来通过网络从其发送的流量字节数。（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "network": {
        "description": "网络实体名称（用于 'network' 类型）。",
        "optional": 1,
        "type": "string"
      },
      "network-type": {
        "description": "网络资源类型（用于 'network' 类型）。",
        "enum": [
          "fabric",
          "zone"
        ],
        "optional": 1,
        "type": "string"
      },
      "node": {
        "description": "集群节点名称（用于 'node'、'storage'、'qemu' 和 'lxc' 类型）。",
        "format": "pve-node",
        "optional": 1,
        "type": "string"
      },
      "plugintype": {
        "description": "更具体的类型（如有）。",
        "optional": 1,
        "type": "string"
      },
      "pool": {
        "description": "资源池名称（用于 'pool'、'qemu' 和 'lxc' 类型）。",
        "optional": 1,
        "type": "string"
      },
      "protocol": {
        "description": "fabric 协议（用于 'network' 类型、'fabric' 网络类型）。",
        "optional": 1,
        "type": "string"
      },
      "sdn": {
        "description": "SDN 实体名称（用于 'sdn' 类型）",
        "optional": 1,
        "type": "string"
      },
      "shared": {
        "description": "确定存储是否共享",
        "optional": 1,
        "type": "boolean"
      },
      "status": {
        "description": "取决于资源类型的状态。",
        "optional": 1,
        "type": "string"
      },
      "storage": {
        "description": "存储标识符（用于 'storage' 类型）。",
        "format": "pve-storage-id",
        "format_description": "storage ID",
        "optional": 1,
        "type": "string"
      },
      "tags": {
        "description": "客户机的标签（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "type": "string"
      },
      "template": {
        "default": 0,
        "description": "确定客户机是否为模板。（用于 'qemu' 和 'lxc' 类型）",
        "optional": 1,
        "type": "boolean"
      },
      "type": {
        "description": "资源类型。",
        "enum": [
          "node",
          "storage",
          "pool",
          "qemu",
          "lxc",
          "openvz",
          "sdn",
          "network"
        ],
        "type": "string"
      },
      "uptime": {
        "description": "节点或虚拟客户机的运行时间，单位为秒（用于 'node'、'qemu' 和 'lxc' 类型）。",
        "optional": 1,
        "renderer": "duration",
        "type": "integer"
      },
      "vmid": {
        "description": "数值形式的 vmid（用于 'qemu' 和 'lxc' 类型）。",
        "format": "pve-vmid",
        "maximum": 999999999,
        "minimum": 100,
        "optional": 1,
        "type": "integer"
      },
      "zone-type": {
        "description": "SDN 区域类型（用于 'sdn' 类型）。",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/resources)。
