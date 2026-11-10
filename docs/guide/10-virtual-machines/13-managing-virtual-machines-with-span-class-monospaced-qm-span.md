# 10.13. 使用 `qm` 管理虚拟机 <a href="#managing_virtual_machines_with_span_class_monospaced_qm_span" id="managing_virtual_machines_with_span_class_monospaced_qm_span"></a>

qm 是 Proxmox VE 上用于管理 QEMU/KVM 虚拟机的工具。您可以创建和销毁虚拟机，并控制其运行（启动/停止/挂起/恢复）。此外，还可以使用 qm 在关联的配置文件中设置参数，也可以创建和删除虚拟磁盘。

## 10.13.1. CLI 使用示例 <a href="#cli_usage_examples" id="cli_usage_examples"></a>

使用上传到 *local* 存储的 iso 文件，在 *local-lvm* 存储上创建一个带有 4 GB IDE 磁盘的 VM

```text
# qm create 300 -ide0 local-lvm:4 -net0 e1000 -cdrom local:iso/proxmox-mailgateway_2.1.iso
```

启动新的 VM

```text
# qm start 300
```

发送关机请求，然后等待，直到 VM 停止。

```text
# qm shutdown 300 && qm wait 300
```

与上述相同，但只等待 40 秒。

```text
# qm shutdown 300 && qm wait 300 -timeout 40
```

如果 VM 未关机，则强制停止它，并覆盖任何正在运行的关机任务。由于停止 VM 可能导致数据丢失，请谨慎使用。

```text
# qm stop 300 -overrule-shutdown 1
```

销毁 VM 始终会将其从访问控制列表中移除，并始终会移除该 VM 的防火墙配置。如果还希望将 VM 从复制作业、备份作业和 HA 资源配置中移除，则必须激活 *--purge*。

{% hint style="info" %}
启用 purge 还会从所有引用该 HA 资源的亲和性规则中移除该资源，并移除仅剩这一个资源的规则。
{% endhint %}

```text
# qm destroy 300 --purge
```

将磁盘映像移动到另一存储。

```text
# qm move-disk 300 scsi0 other-storage
```

将磁盘映像重新分配给另一个 VM。这会从源 VM 中移除磁盘 `scsi1`，并将其作为 `scsi3` 附加到目标 VM。在后台，磁盘映像会被重命名，以使名称与新所有者匹配。

```text
# qm move-disk 300 scsi1 --target-vmid 400 --target-disk scsi3
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
