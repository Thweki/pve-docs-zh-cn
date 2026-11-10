# 17.7. Notification Mode <a href="#notification_mode" id="notification_mode"></a>

Backup jobs allow to choose between two modes for sending backup related notifications. This is controlled by the `notification-mode` option in the [backup job configuration](../16-vzdump/10-vzdump-configuration.md#vzdump_configuration).

- Send notifications based on the global notification settings (`notification-system`).
- Send notification emails via the system’s `sendmail` command to the email address configured in the backup job (`legacy-sendmail`). This mode also allows to select whether the email should be sent always or only on failure of the backup. Any targets or matchers from the global notification settings are ignored. This mode is equivalent to the notification behavior for Proxmox VE versions before 8.1. This mode might be removed in a later release of Proxmox VE.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
