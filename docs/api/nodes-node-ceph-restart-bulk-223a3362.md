# `/nodes/{node}/ceph/restart-bulk`

原始接口路径：`/nodes/{node}/ceph/restart-bulk`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/ceph/restart-bulk`

滚动重启此节点上的所有 Ceph OSD。只有 Ceph 报告上一个 OSD 已恢复运行且下一个可安全停止后，才重启相应 OSD。对于非 OSD 的 Ceph 守护进程，请使用集群级端点 /cluster/ceph/restart-bulk.。'noout' 标志仅应用于本次运行针对的 OSD，因此其他节点上不相关的 OSD 即使在重启期间发生故障，仍会正常标记为 out。中止生成的任务（例如通过 'pvesh task stop'）会触发 SIGTERM 处理程序，如果此端点设置了各 OSD 的 'noout'，则将其取消。各守护进程的进度检查点保存在 Ceph 的 config-key 存储（'pve/ceph-bulk-restart/node/&lt;node&gt;'）中，因此可使用 'resume=1' 重新调用此端点来恢复中止的运行。

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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `dry-run` | boolean | 否 | 0 | 记录计划（将重启哪些 OSD 及其顺序），但不执行实际操作。 |
| `force` | boolean | 否 | 0 | 对于带有非良性检查的 HEALTH_WARN，例如 PG_DEGRADED、SLOW_OPS 或 MON_DOWN，继续执行。无论此标志如何，阻塞性 HEALTH_ERR 都是致命错误。ceph 报告为已静默的检查以及已知对滚动重启无害的检查永远不会阻塞操作，并会在任务日志中列明。集群范围的 OSD 映射标志仅在重启 OSD 时才会评估，因为重启 mon、mgr 或 mds 不会涉及其控制的内容。操作人员有责任确认集群足够稳定，能够承受滚动重启。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `only-outdated` | boolean | 否 | 0 | 只重启运行版本与本地安装的 ceph-osd 二进制程序不同的 OSD。适用于升级后仅针对需要重启的守护进程执行滚动重启。如果无法确定本地二进制版本，则拒绝操作。恢复执行时忽略此选项（原样使用保存的计划）。 |
| `resume` | boolean | 否 | 0 | 从 Ceph config-key 存储中的检查点恢复已中止的批量重启。沿用上次运行的计划和 noout 决定；忽略 'set-noout'。为 false（默认值）时，如果此节点存在检查点，端点将拒绝启动，避免静默覆盖正在进行的工作。 |
| `service-type` | string | 是 | — | 要重启的 Ceph 守护进程类型。只有 OSD 可按节点滚动重启。；可选值：`osd` |
| `set-noout` | boolean | 否 | 1 | 在滚动重启期间，为本次运行针对的每个 OSD 设置 'noout' 标志，并在完成时取消设置。采用每个 OSD 而非集群范围的设置，使其他节点上不相关 OSD 的故障仍能正常触发回填。 |
| `timeout` | integer | 否 | 600 | 每个 OSD 的超时时间（秒）。同时限制等待重启的 OSD 恢复上线的时间，以及等待恢复活动足够平静、使 Ceph 报告下一个 OSD 可安全停止的时间。默认值适用于繁忙集群，其中包含大量 PG 的多 TB OSD 在重启后可能需要数分钟才能完成对等互联；对于非常大或负载很高的 OSD，请增大此值。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0,
      "description": "记录计划（将重启哪些 OSD 及其顺序），但不执行实际操作。",
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
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "only-outdated": {
      "default": 0,
      "description": "只重启运行版本与本地安装的 ceph-osd 二进制程序不同的 OSD。适用于升级后仅针对需要重启的守护进程执行滚动重启。如果无法确定本地二进制版本，则拒绝操作。恢复执行时忽略此选项（原样使用保存的计划）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "resume": {
      "default": 0,
      "description": "从 Ceph config-key 存储中的检查点恢复已中止的批量重启。沿用上次运行的计划和 noout 决定；忽略 'set-noout'。为 false（默认值）时，如果此节点存在检查点，端点将拒绝启动，避免静默覆盖正在进行的工作。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "service-type": {
      "description": "要重启的 Ceph 守护进程类型。只有 OSD 可按节点滚动重启。",
      "enum": [
        "osd"
      ],
      "type": "string"
    },
    "set-noout": {
      "default": 1,
      "description": "在滚动重启期间，为本次运行针对的每个 OSD 设置 'noout' 标志，并在完成时取消设置。采用每个 OSD 而非集群范围的设置，使其他节点上不相关 OSD 的故障仍能正常触发回填。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "timeout": {
      "default": 600,
      "description": "每个 OSD 的超时时间（秒）。同时限制等待重启的 OSD 恢复上线的时间，以及等待恢复活动足够平静、使 Ceph 报告下一个 OSD 可安全停止的时间。默认值适用于繁忙集群，其中包含大量 PG 的多 TB OSD 在重启后可能需要数分钟才能完成对等互联；对于非常大或负载很高的 OSD，请增大此值。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/restart-bulk)。
