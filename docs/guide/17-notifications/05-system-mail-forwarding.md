# 17.5. 系统邮件转发 <a href="#system_mail_forwarding" id="system_mail_forwarding"></a>

某些本地系统守护进程（例如 `smartd`）会生成通知邮件，最初发送给本地 `root` 用户。这些邮件会转换为类型为 `system-mail`、严重性为 `unknown` 的通知事件，并根据全局通知设置进行处理。

将电子邮件转发到 sendmail 目标时，邮件内容和标头会原样转发。对于所有其他目标，系统会尝试从电子邮件内容中提取主题行和主要正文。如果电子邮件只包含 HTML 内容，则会在此过程中转换为纯文本格式。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
