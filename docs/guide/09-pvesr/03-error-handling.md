# 9.3. 错误处理 <a href="#error_handling" id="error_handling"></a>

如果复制作业遇到问题，它会进入错误状态。在此状态下，配置的复制间隔会暂时暂停。系统会每隔 30 分钟重试失败的复制。一旦成功，原来的计划就会重新激活。

## 9.3.1. 可能的问题 <a href="#possible_issues" id="possible_issues"></a>

以下列出了一些最常见的问题。根据您的部署情况，可能还有其他原因。

- 网络未正常工作。
- 复制目标存储上没有剩余可用空间。
- 目标节点上无法使用具有相同存储 ID 的存储。

{% hint style="info" %}
您始终可以使用复制日志来找出问题的原因。
{% endhint %}

## 9.3.2. 发生错误时迁移客户机 <a href="#migrating_a_guest_in_case_of_error" id="migrating_a_guest_in_case_of_error"></a>

发生严重错误时，虚拟客户机可能会卡在故障节点上。此时需要手动将其重新迁移到正常工作的节点。

## 9.3.3. 示例 <a href="#example_2" id="example_2"></a>

假设您有两个客户机（VM 100 和 CT 200）运行在节点 A 上，并复制到节点 B。节点 A 发生故障且无法重新上线。现在，您必须手动将客户机迁移到节点 B。

- 通过 ssh 连接到节点 B，或通过 Web UI 打开其 Shell
- 检查集群是否具有仲裁

  ```text
  # pvecm status
  ```
- 如果没有仲裁，我们强烈建议先解决此问题，使节点恢复可操作状态。仅当目前无法做到这一点时，才可使用以下命令在当前节点上强制达到仲裁：

  ```text
  # pvecm expected 1
  ```

{% hint style="warning" %}
设置 `expected votes` 后，务必避免任何影响集群的更改（例如添加/移除节点、存储、虚拟客户机）。仅使用它来让关键客户机恢复运行，或解决仲裁问题本身。
{% endhint %}

- 将两个客户机配置文件从原节点 A 移动到节点 B：

  ```text
  # mv /etc/pve/nodes/A/qemu-server/100.conf /etc/pve/nodes/B/qemu-server/100.conf
  # mv /etc/pve/nodes/A/lxc/200.conf /etc/pve/nodes/B/lxc/200.conf
  ```
- 现在可以重新启动这些客户机：

  ```text
  # qm start 100
  # pct start 200
  ```

请记得将 VMID 和节点名称替换为各自的值。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
