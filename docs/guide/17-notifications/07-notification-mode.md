# 17.7. 通知模式 <a href="#notification_mode" id="notification_mode"></a>

备份任务允许在两种模式之间选择，用于发送备份相关通知。这由 `notification-mode` 选项控制，该选项位于[备份任务配置](../16-vzdump/10-vzdump-configuration.md)中。

- 根据全局通知设置发送通知（`notification-system`）。
- 通过系统的 `sendmail` 命令，将通知邮件发送到备份任务中配置的电子邮件地址（`legacy-sendmail`）。此模式还允许选择始终发送邮件，或仅在备份失败时发送。全局通知设置中的所有目标或匹配器均会被忽略。此模式等同于 Proxmox VE 8.1 之前版本的通知行为。此模式可能在 Proxmox VE 的后续版本中移除。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
