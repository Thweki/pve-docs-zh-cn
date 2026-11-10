# `/nodes/{node}/qemu/{vmid}/status/current`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/current`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/status/current`

获取虚拟机状态。

**方法标识：** `vm_status`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
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
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

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
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
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
  "properties": {
    "agent": {
      "description": "配置中已启用 QEMU Guest Agent。",
      "optional": 1,
      "type": "boolean"
    },
    "clipboard": {
      "description": "启用特定剪贴板。未设置时，将根据显示类型添加 SPICE 剪贴板。",
      "enum": [
        "vnc"
      ],
      "optional": 1,
      "type": "string"
    },
    "cpu": {
      "description": "当前 CPU 使用率。",
      "optional": 1,
      "type": "number"
    },
    "cpus": {
      "description": "最大可用 CPU 数量。",
      "optional": 1,
      "type": "number"
    },
    "diskread": {
      "description": "自客户机启动以来从其块设备读取的字节数。（注意：并非所有存储类型都提供此信息。）",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "diskwrite": {
      "description": "自客户机启动以来写入其块设备的字节数。（注意：并非所有存储类型都提供此信息。）",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "ha": {
      "description": "HA 管理器服务状态。",
      "type": "object"
    },
    "lock": {
      "description": "当前的配置锁（如有）。",
      "optional": 1,
      "type": "string"
    },
    "maxdisk": {
      "description": "根磁盘大小，单位为字节。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "maxmem": {
      "description": "最大内存，单位为字节。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "mem": {
      "description": "当前已用内存，单位为字节。不考虑内核同页合并（KSM）。如果 ballooning 信息可用，则使用该信息。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "memhost": {
      "description": "宿主机上的当前内存用量。不考虑内核同页合并（KSM）。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "name": {
      "description": "虚拟机的（主机）名称。",
      "optional": 1,
      "type": "string"
    },
    "netin": {
      "description": "自客户机启动以来通过网络向其发送的流量字节数。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "netout": {
      "description": "自客户机启动以来通过网络从其发送的流量字节数。",
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    },
    "pid": {
      "description": "QEMU 进程的 PID（如果虚拟机正在运行）。",
      "optional": 1,
      "type": "integer"
    },
    "pressurecpufull": {
      "description": "过去 10 秒的 CPU Full 压力停滞平均值。",
      "optional": 1,
      "type": "number"
    },
    "pressurecpusome": {
      "description": "过去 10 秒的 CPU Some 压力停滞平均值。",
      "optional": 1,
      "type": "number"
    },
    "pressureiofull": {
      "description": "过去 10 秒的 IO Full 压力停滞平均值。",
      "optional": 1,
      "type": "number"
    },
    "pressureiosome": {
      "description": "过去 10 秒的 IO Some 压力停滞平均值。",
      "optional": 1,
      "type": "number"
    },
    "pressurememoryfull": {
      "description": "过去 10 秒的内存 Full 压力停滞平均值。",
      "optional": 1,
      "type": "number"
    },
    "pressurememorysome": {
      "description": "过去 10 秒的内存 Some 压力停滞平均值。",
      "optional": 1,
      "type": "number"
    },
    "qmpstatus": {
      "description": "'query-status' QMP 监视器命令报告的虚拟机运行状态。",
      "optional": 1,
      "type": "string"
    },
    "running-machine": {
      "description": "当前运行的机器类型（如果正在运行）。",
      "optional": 1,
      "type": "string"
    },
    "running-qemu": {
      "description": "虚拟机当前使用的 QEMU 版本（如果正在运行）。",
      "optional": 1,
      "type": "string"
    },
    "serial": {
      "description": "客户机配置了串行设备。",
      "optional": 1,
      "type": "boolean"
    },
    "spice": {
      "description": "QEMU VGA 配置支持 spice。",
      "optional": 1,
      "type": "boolean"
    },
    "status": {
      "description": "QEMU 进程状态。",
      "enum": [
        "stopped",
        "running"
      ],
      "type": "string"
    },
    "tags": {
      "description": "当前配置的标签（如有）",
      "optional": 1,
      "type": "string"
    },
    "template": {
      "default": 0,
      "description": "确定客户机是否为模板。",
      "optional": 1,
      "type": "boolean"
    },
    "uptime": {
      "description": "运行时间，单位为秒。",
      "optional": 1,
      "renderer": "duration",
      "type": "integer"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/current)。
