# 17.1. 概述 <a href="#overview" id="overview"></a>

- Proxmox VE 会在存储复制失败、节点隔离、备份完成/失败等事件发生时发出[通知事件](04-notification-events.md)。这些事件根据全局通知设置进行处理。每个通知事件都包含元数据，例如时间戳、严重性级别、类型以及其他事件特定字段。
- [通知匹配器](03-notification-matchers.md)将通知事件路由到一个或多个通知目标。匹配器可以具有匹配规则，根据通知事件的元数据进行选择性路由。
- [通知目标](02-notification-targets.md)是匹配器将通知事件路由到的目的地。目标有多种类型，包括基于邮件的目标（Sendmail 和 SMTP）以及 Gotify。

可以在 GUI 的“数据中心 → 通知”下配置全局通知设置。配置保存在 `/etc/pve/notifications.cfg` 和 `/etc/pve/priv/notifications.cfg` 中，后者包含敏感配置选项，例如通知目标的密码或认证令牌，并且仅允许 `root` 读取。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
