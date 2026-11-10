# 10.6. VM 生成 ID <a href="#_vm_generation_id" id="_vm_generation_id"></a>

Proxmox VE 支持虚拟机的虚拟机生成 ID (*vmgenid*) [\[1\]](#note-bccd999c-1)。客户机操作系统可用它来检测任何导致时间偏移的事件，例如恢复备份或回滚快照。

创建新 VM 时，会自动生成 *vmgenid* 并将其保存在该 VM 的配置文件中。

要为现有的 VM 创建并添加 *vmgenid*，可以传入特殊值“1”，让 Proxmox VE 自动生成一个；也可以将 *UUID* [\[2\]](#note-bccd999c-2) 用作值，手动进行设置，例如：

```text
# qm set VMID -vmgenid 1
# qm set VMID -vmgenid 00000000-0000-0000-0000-000000000000
```

{% hint style="info" %}
首次向现有 VM 添加 *vmgenid* 设备，可能会产生与快照回滚、备份恢复等操作中的变更相同的影响，因为 VM 可能会将其解释为代际变更。
{% endhint %}

在极少数不需要 *vmgenid* 机制的情况下，可以在创建 VM 时将其值设为“0”，或者使用以下命令在配置中事后删除该属性：

```text
# qm set VMID -delete vmgenid
```

*vmgenid* 最主要的用例是较新的 Microsoft Windows 操作系统，它们利用该机制避免在快照回滚、备份恢复或完整 VM 克隆操作时，时间敏感型服务或复制服务（例如数据库或域控制器 [\[3\]](#note-bccd999c-3)）出现问题。

## 注释

### 注释 1 <a href="#note-bccd999c-1" id="note-bccd999c-1"></a>

官方 *vmgenid* 规范 [https://docs.microsoft.com/en-us/windows/desktop/hyperv\_v2/virtual-machine-generation-identifier](https://docs.microsoft.com/en-us/windows/desktop/hyperv_v2/virtual-machine-generation-identifier)

### 注释 2 <a href="#note-bccd999c-2" id="note-bccd999c-2"></a>

在线 GUID 生成器 [http://guid.one/](http://guid.one/)

### 注释 3 <a href="#note-bccd999c-3" id="note-bccd999c-3"></a>

[https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
