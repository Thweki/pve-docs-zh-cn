# `/cluster/ceph/restart-bulk`

原始接口路径：`/cluster/ceph/restart-bulk`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ceph/restart-bulk`

Cluster-wide rolling restart of all Ceph daemons of the given type. For MON/MGR/MDS each daemon is restarted only after Ceph reports the previous one is back up and the next one is safe to stop. For OSDs the cluster path orchestrates the per-node endpoint at /nodes/{node}/ceph/restart-bulk on each node in turn, inheriting that endpoint's per-OSD 'noout' handling and resume support. The 'noout' flag itself is not exposed by this endpoint as it is OSD-specific (and for OSDs handled by the per-node sub-tasks).

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
| `dry-run` | boolean | 否 | 0 | Log the plan (which daemons would be restarted, in what order) without actually doing anything. |
| `force` | boolean | 否 | 0 | Proceed past a HEALTH_WARN with non-benign checks like PG_DEGRADED, SLOW_OPS, or MON_DOWN. A blocking HEALTH_ERR is fatal regardless of this flag. Checks that ceph reports as muted, and checks known to be harmless for a rolling restart, never block and are named in the task log. The cluster-wide OSD map flags are only ever evaluated for an OSD restart, since they govern nothing a mon, mgr or mds restart touches. The operator is responsible for confirming the cluster is stable enough to absorb a rolling restart. |
| `only-outdated` | boolean | 否 | 0 | OSDs only: restart only OSDs whose running version differs from the locally-installed ceph-osd binary on their host. Forwarded to each per-node sub-task so the per-host installed version is used (a partial upgrade where one host is on a newer build is handled correctly). |
| `service-type` | string | 是 | — | Ceph daemon type to restart cluster-wide.；可选值：`mon`, `mgr`, `mds`, `osd` |
| `timeout` | integer | 否 | 600 | Per-daemon timeout (in seconds) for the up-wait phase. Note: for daemons on remote nodes the same timeout also bounds the remote restart task, so the per-daemon budget can be up to 2x this value. Default sized for slow MDS journal replay or MON paxos settle on busy clusters; bump higher if the cluster routinely takes longer to stabilize after a daemon restart. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0,
      "description": "Log the plan (which daemons would be restarted, in what order) without actually doing anything.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "force": {
      "default": 0,
      "description": "Proceed past a HEALTH_WARN with non-benign checks like PG_DEGRADED, SLOW_OPS, or MON_DOWN. A blocking HEALTH_ERR is fatal regardless of this flag. Checks that ceph reports as muted, and checks known to be harmless for a rolling restart, never block and are named in the task log. The cluster-wide OSD map flags are only ever evaluated for an OSD restart, since they govern nothing a mon, mgr or mds restart touches. The operator is responsible for confirming the cluster is stable enough to absorb a rolling restart.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "only-outdated": {
      "default": 0,
      "description": "OSDs only: restart only OSDs whose running version differs from the locally-installed ceph-osd binary on their host. Forwarded to each per-node sub-task so the per-host installed version is used (a partial upgrade where one host is on a newer build is handled correctly).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "service-type": {
      "description": "Ceph daemon type to restart cluster-wide.",
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
      "description": "Per-daemon timeout (in seconds) for the up-wait phase. Note: for daemons on remote nodes the same timeout also bounds the remote restart task, so the per-daemon budget can be up to 2x this value. Default sized for slow MDS journal replay or MON paxos settle on busy clusters; bump higher if the cluster routinely takes longer to stabilize after a daemon restart.",
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
