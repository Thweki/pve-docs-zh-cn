# `/nodes/{node}/qemu/{vmid}/monitor`

原始接口路径：`/nodes/{node}/qemu/{vmid}/monitor`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/monitor`

Execute QEMU monitor commands.

**方法标识：** `monitor`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "Sys.Audit",
      "Sys.Modify"
    ],
    "any",
    1
  ],
  "description": "The following commands do not require any additional privilege: ?, help, info\n\nThe following commands require 'Sys.Modify': announce_self, backup_cancel, balloon, block_job_cancel, block_job_complete, block_job_pause, block_job_resume, block_job_set_speed, block_resize, block_set_io_throttle, boot_set, c, calc_dirty_rate, cancel_vcpu_dirty_limit, chardev-send-break, closefd, commit, cont, cpu, delvm, eject, exit_preconfig, expire_password, getfd, gpa2hpa, gpa2hva, gva2gpa, i, loadvm, log, migrate_cancel, migrate_continue, migrate_pause, migrate_set_capability, migrate_set_parameter, migrate_start_postcopy, mouse_button, mouse_move, mouse_set, one-insn-per-tb, p, print, q, qemu-io, qom-get, qom-list, quit, replay_break, replay_delete_break, replay_seek, ringbuf_read, ringbuf_write, s, savevm, sendkey, set_link, set_password, set_vcpu_dirty_limit, snapshot_blkdev_internal, snapshot_delete_blkdev_internal, stop, stopcapture, sum, sync-profile, system_powerdown, system_reset, system_wakeup, trace-event, x, x_colo_lost_heartbeat, xp\n\nThe following commands are root-only: backup, block_stream, change, chardev-add, chardev-change, chardev-remove, client_migrate_info, device_add, device_del, drive_add, drive_backup, drive_del, drive_mirror, dump-guest-memory, dumpdtb, gdbserver, hostfwd_add, hostfwd_remove, logfile, mce, memsave, migrate, migrate_incoming, migrate_recover, nbd_server_add, nbd_server_remove, nbd_server_start, nbd_server_stop, netdev_add, netdev_del, nmi, o, object_add, object_del, pcie_aer_inject_error, pmemsave, qom-set, savevm-end, savevm-start, screendump, snapshot_blkdev, watchdog_action, wavcapture, xen-event-inject, xen-event-list\n\nThe following commands are deprecated: stopcapture, wavcapture\n"
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
| `command` | string | 是 | — | The monitor command. |
| `node` | string | 是 | — | The cluster node name. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "command": {
      "description": "The monitor command.",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/monitor)。
