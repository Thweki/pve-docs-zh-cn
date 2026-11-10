# `/nodes/{node}/services/{service}/reload`

原始接口路径：`/nodes/{node}/services/{service}/reload`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/services/{service}/reload`

Reload service. Falls back to restart if service cannot be reloaded.

**方法标识：** `service_reload`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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
| `node` | string | 是 | — | The cluster node name. |
| `service` | string | 是 | — | Service ID；可选值：`chrony`, `corosync`, `cron`, `ksmtuned`, `lxcfs`, `postfix`, `proxmox-firewall`, `pve-cluster`, `pve-firewall`, `pve-ha-crm`, `pve-ha-lrm`, `pve-lxc-syscalld`, `pvedaemon`, `pvefw-logger`, `pveproxy`, `pvescheduler`, `pvestatd`, `qmeventd`, `spiceproxy`, `sshd`, `syslog`, `systemd-journald`, `systemd-timesyncd` |

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
    "service": {
      "description": "Service ID",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/services/{service}/reload)。
