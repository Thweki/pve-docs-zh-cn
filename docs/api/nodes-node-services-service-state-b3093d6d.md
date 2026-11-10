# `/nodes/{node}/services/{service}/state`

原始接口路径：`/nodes/{node}/services/{service}/state`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/services/{service}/state`

读取服务属性

**方法标识：** `service_state`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |
| `service` | string | 是 | — | 服务 ID；可选值：`chrony`, `corosync`, `cron`, `ksmtuned`, `lxcfs`, `postfix`, `proxmox-firewall`, `pve-cluster`, `pve-firewall`, `pve-ha-crm`, `pve-ha-lrm`, `pve-lxc-syscalld`, `pvedaemon`, `pvefw-logger`, `pveproxy`, `pvescheduler`, `pvestatd`, `qmeventd`, `spiceproxy`, `sshd`, `syslog`, `systemd-journald`, `systemd-timesyncd` |

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
    "service": {
      "description": "服务 ID",
      "enum": [
        "chrony",
        "corosync",
        "cron",
        "ksmtuned",
        "lxcfs",
        "postfix",
        "proxmox-firewall",
        "pve-cluster",
        "pve-firewall",
        "pve-ha-crm",
        "pve-ha-lrm",
        "pve-lxc-syscalld",
        "pvedaemon",
        "pvefw-logger",
        "pveproxy",
        "pvescheduler",
        "pvestatd",
        "qmeventd",
        "spiceproxy",
        "sshd",
        "syslog",
        "systemd-journald",
        "systemd-timesyncd"
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
  "properties": {
    "active-state": {
      "description": "服务进程的当前状态（systemd ActiveState）。",
      "enum": [
        "active",
        "inactive",
        "failed",
        "activating",
        "deactivating",
        "maintenance",
        "reloading",
        "refreshing",
        "unknown"
      ],
      "type": "string"
    },
    "desc": {
      "description": "服务描述。",
      "type": "string"
    },
    "name": {
      "description": "服务的简短标识符（例如 \"pveproxy\"）。",
      "type": "string"
    },
    "service": {
      "description": "Systemd 单元名称（例如 pveproxy）。",
      "type": "string"
    },
    "state": {
      "description": "服务执行状态（systemd SubState）。",
      "enum": [
        "dead",
        "condition",
        "start-pre",
        "start",
        "start-post",
        "running",
        "exited",
        "reload",
        "reload-signal",
        "reload-notify",
        "mounting",
        "stop",
        "stop-watchdog",
        "stop-sigterm",
        "stop-sigkill",
        "stop-post",
        "final-watchdog",
        "final-sigterm",
        "final-sigkill",
        "failed",
        "dead-before-auto-restart",
        "failed-before-auto-restart",
        "dead-resources-pinned",
        "auto-restart",
        "auto-restart-queued",
        "cleaning",
        "unknown"
      ],
      "type": "string"
    },
    "unit-state": {
      "description": "服务是否已启用（systemd UnitFileState）。",
      "enum": [
        "enabled",
        "enabled-runtime",
        "linked",
        "linked-runtime",
        "alias",
        "masked",
        "masked-runtime",
        "static",
        "disabled",
        "indirect",
        "generated",
        "transient",
        "bad",
        "not-found",
        "unknown"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/services/{service}/state)。
