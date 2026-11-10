# `/nodes/{node}/services/{service}`

原始接口路径：`/nodes/{node}/services/{service}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/services/{service}`

Directory index

**方法标识：** `srvcmdidx`

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
  "items": {
    "properties": {
      "subdir": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{subdir}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/services/{service})。
