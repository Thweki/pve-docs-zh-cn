# 14.1. 用户 <a href="#pveum_users" id="pveum_users"></a>

Proxmox VE 将用户属性存储在 `/etc/pve/user.cfg` 中。密码不存储在此处；用户会关联到下文所述的 [认证域](05-pveum-authentication-realms.md)。因此，内部通常使用用户名和认证域来标识用户，形式为 `<userid>@<realm>`。

此文件中的每个用户条目包含以下信息：

- 名字
- 姓氏
- 电子邮件地址
- 所属组
- 可选的到期日期
- 关于此用户的注释或备注
- 此用户是启用还是禁用
- 可选的双因素身份验证密钥

{% hint style="danger" %}
禁用或删除用户，或设置的到期日期已过时，此用户将无法登录新会话或启动新任务。此用户已启动的所有任务（例如终端会话）都 **不会** 因任何此类事件而自动终止。
{% endhint %}

## 14.1.1. 系统管理员 <a href="#system_administrator" id="system_administrator"></a>

系统的 root 用户始终可以通过 Linux PAM 认证域登录，并且是不受限制的管理员。此用户不能删除，但仍可更改其属性。系统邮件会发送到分配给此用户的电子邮件地址。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
