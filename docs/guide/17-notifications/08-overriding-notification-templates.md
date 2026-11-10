# 17.8. 覆盖通知模板 <a href="#overriding_notification_templates" id="overriding_notification_templates"></a>

Proxmox VE 使用 Handlebars 模板渲染通知。Proxmox VE 提供的原始模板保存在 `/usr/share/pve-manager/templates/default/`。

可以在 `/etc/pve/notification-templates/default/` 覆盖目录中提供自定义模板文件，以覆盖通知模板。渲染指定类型的通知时，Proxmox VE 会先尝试从覆盖目录加载模板。如果模板不存在或渲染失败，则使用原始模板。

模板文件遵循 `<type>-<body|subject>.<html|txt>.hbs` 命名约定。例如，文件 `vzdump-body.html.hbs` 包含用于渲染 HTML 版备份通知的模板，而 `package-updates-subject.txt.hbs` 用于渲染可用软件包更新通知的主题行。

基于电子邮件的通知目标（例如 `sendmail` 和 `smtp`）始终发送包含 HTML 部分和纯文本部分的多部分消息。因此，在渲染邮件消息时，`<type>-body.html.hbs` 和 `<type>-body.txt.hbs` 模板都会使用。所有其他通知目标类型只使用 `<type>-body.txt.hbs` 模板。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
