# `/cluster/ceph/restart-bulk`

原始接口路径：`/cluster/ceph/restart-bulk`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ceph/restart-bulk`

在整个集群中滚动重启给定类型的所有 Ceph 守护进程。对于 MON/MGR/MDS，只有在 Ceph 报告上一个守护进程已恢复运行且下一个可以安全停止后，才会重启该守护进程。对于 OSD，集群路径会依次编排各节点上的 /nodes/{node}/ceph/restart-bulk 节点级端点，沿用该端点的每个 OSD 的 'noout' 处理和恢复执行支持。此端点不直接提供 'noout' 标志，因为它仅适用于 OSD（对于 OSD，由各节点子任务处理）。

**方法标识：** `restart_bulk`

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
| `dry-run` | boolean | 否 | 0 | 记录计划（将重启哪些守护进程及其顺序），但不执行实际操作。 |
| `force` | boolean | 否 | 0 | 对于带有非良性检查的 HEALTH_WARN，例如 PG_DEGRADED、SLOW_OPS 或 MON_DOWN，继续执行。无论此标志如何，阻塞性 HEALTH_ERR 都是致命错误。ceph 报告为已静默的检查以及已知对滚动重启无害的检查永远不会阻塞操作，并会在任务日志中列明。集群范围的 OSD 映射标志仅在重启 OSD 时才会评估，因为重启 mon、mgr 或 mds 不会涉及其控制的内容。操作人员有责任确认集群足够稳定，能够承受滚动重启。 |
| `only-outdated` | boolean | 否 | 0 | 仅适用于 OSD：只重启运行版本与其宿主机本地安装的 ceph-osd 二进制程序版本不同的 OSD。此选项会传递到每个节点级子任务，以使用各宿主机安装的版本（可正确处理某个宿主机采用较新构建版本的部分升级情形）。 |
| `service-type` | string | 是 | — | 要在整个集群中重启的 Ceph 守护进程类型。；可选值：`mon`, `mgr`, `mds`, `osd` |
| `timeout` | integer | 否 | 600 | 每个守护进程等待上线阶段的超时时间（秒）。注意：对于远程节点上的守护进程，同一超时时间也会约束远程重启任务，因此每个守护进程的总时间预算可达此值的 2 倍。默认值考虑了繁忙集群中缓慢的 MDS 日志重放或 MON paxos 稳定过程；如果集群在守护进程重启后通常需要更长时间才能稳定，请增大此值。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0,
      "description": "记录计划（将重启哪些守护进程及其顺序），但不执行实际操作。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "force": {
      "default": 0,
      "description": "对于带有非良性检查的 HEALTH_WARN，例如 PG_DEGRADED、SLOW_OPS 或 MON_DOWN，继续执行。无论此标志如何，阻塞性 HEALTH_ERR 都是致命错误。ceph 报告为已静默的检查以及已知对滚动重启无害的检查永远不会阻塞操作，并会在任务日志中列明。集群范围的 OSD 映射标志仅在重启 OSD 时才会评估，因为重启 mon、mgr 或 mds 不会涉及其控制的内容。操作人员有责任确认集群足够稳定，能够承受滚动重启。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "only-outdated": {
      "default": 0,
      "description": "仅适用于 OSD：只重启运行版本与其宿主机本地安装的 ceph-osd 二进制程序版本不同的 OSD。此选项会传递到每个节点级子任务，以使用各宿主机安装的版本（可正确处理某个宿主机采用较新构建版本的部分升级情形）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "service-type": {
      "description": "要在整个集群中重启的 Ceph 守护进程类型。",
      "enum": [
        "mon",
        "mgr",
        "mds",
        "osd"
      ],
      "type": "string"
    },
    "timeout": {
      "default": 600,
      "description": "每个守护进程等待上线阶段的超时时间（秒）。注意：对于远程节点上的守护进程，同一超时时间也会约束远程重启任务，因此每个守护进程的总时间预算可达此值的 2 倍。默认值考虑了繁忙集群中缓慢的 MDS 日志重放或 MON paxos 稳定过程；如果集群在守护进程重启后通常需要更长时间才能稳定，请增大此值。",
      "maximum": 1800,
      "minimum": 30,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (30 - 1800)"
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

<details>
<summary>其他接口元数据</summary>

```json
{
  "expose_credentials": 1
}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/restart-bulk)。
