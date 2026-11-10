# `/nodes/{node}/ceph/restart-bulk`

原始接口路径：`/nodes/{node}/ceph/restart-bulk`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/ceph/restart-bulk`

Rolling restart of all Ceph OSDs on this node. Each OSD is restarted only after Ceph reports the previous one is back up and the next one is safe to stop. For non-OSD Ceph daemons, use the cluster-wide endpoint at /cluster/ceph/restart-bulk. The 'noout' flag is applied only to the OSDs targeted by this run, so unrelated OSDs on other nodes that fail during the restart window still get out-marked normally. Aborting the resulting task (for example via 'pvesh task stop') triggers a SIGTERM handler that unsets the per-OSD 'noout' if this endpoint set it. Per-daemon progress is checkpointed in Ceph's config-key store ('pve/ceph-bulk-restart/node/<node>'), so an aborted run can be resumed by re-issuing this endpoint with 'resume=1'.

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
| `dry-run` | boolean | 否 | 0 | Log the plan (which OSDs would be restarted, in what order) without actually doing anything. |
| `force` | boolean | 否 | 0 | Proceed past a HEALTH_WARN with non-benign checks like PG_DEGRADED, SLOW_OPS, or MON_DOWN. A blocking HEALTH_ERR is fatal regardless of this flag. Checks that ceph reports as muted, and checks known to be harmless for a rolling restart, never block and are named in the task log. The cluster-wide OSD map flags are only ever evaluated for an OSD restart, since they govern nothing a mon, mgr or mds restart touches. The operator is responsible for confirming the cluster is stable enough to absorb a rolling restart. |
| `node` | string | 是 | — | The cluster node name. |
| `only-outdated` | boolean | 否 | 0 | Restart only OSDs whose running version differs from the locally-installed ceph-osd binary. Useful for post-upgrade rolling restarts that should touch only daemons that need it. Refuses if the local binary version cannot be determined. Ignored on resume (the saved plan is used as-is). |
| `resume` | boolean | 否 | 0 | Resume an aborted bulk-restart from the checkpoint stored in Ceph's config-key store. The plan and noout decision from the prior run are honored; 'set-noout' is ignored. When false (default), the endpoint refuses to start if a checkpoint exists for this node, to avoid silently overwriting in-progress work. |
| `service-type` | string | 是 | — | Ceph daemon type to restart. Only OSDs can be rolling-restarted on a per-node basis.；可选值：`osd` |
| `set-noout` | boolean | 否 | 1 | Set the 'noout' flag on each OSD targeted by this run for the duration of the rolling restart, and unset it on completion. Per-OSD rather than cluster-wide so that unrelated OSDs failing on other nodes still trigger backfill normally. |
| `timeout` | integer | 否 | 600 | Per-OSD timeout (in seconds). Bounds both the wait for a restarted OSD to come back up and the wait for recovery to quiesce enough that Ceph reports the next OSD safe to stop. Default sized for busy clusters where multi-TB OSDs with many PGs can need several minutes to clear peering after a restart; bump higher for very large or heavily-loaded OSDs. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0,
      "description": "Log the plan (which OSDs would be restarted, in what order) without actually doing anything.",
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
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "only-outdated": {
      "default": 0,
      "description": "Restart only OSDs whose running version differs from the locally-installed ceph-osd binary. Useful for post-upgrade rolling restarts that should touch only daemons that need it. Refuses if the local binary version cannot be determined. Ignored on resume (the saved plan is used as-is).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "resume": {
      "default": 0,
      "description": "Resume an aborted bulk-restart from the checkpoint stored in Ceph's config-key store. The plan and noout decision from the prior run are honored; 'set-noout' is ignored. When false (default), the endpoint refuses to start if a checkpoint exists for this node, to avoid silently overwriting in-progress work.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "service-type": {
      "description": "Ceph daemon type to restart. Only OSDs can be rolling-restarted on a per-node basis.",
      "enum": [
        "osd"
      ],
      "type": "string"
    },
    "set-noout": {
      "default": 1,
      "description": "Set the 'noout' flag on each OSD targeted by this run for the duration of the rolling restart, and unset it on completion. Per-OSD rather than cluster-wide so that unrelated OSDs failing on other nodes still trigger backfill normally.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "timeout": {
      "default": 600,
      "description": "Per-OSD timeout (in seconds). Bounds both the wait for a restarted OSD to come back up and the wait for recovery to quiesce enough that Ceph reports the next OSD safe to stop. Default sized for busy clusters where multi-TB OSDs with many PGs can need several minutes to clear peering after a restart; bump higher for very large or heavily-loaded OSDs.",
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
