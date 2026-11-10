# 14.3. API 令牌 <a href="#pveum_tokens" id="pveum_tokens"></a>

API 令牌允许其他系统、软件或 API 客户端以无状态方式访问 REST API 的大部分功能。例外是提供虚拟机或系统控制台访问的端点。这些端点需要用户权限，不能通过 API 令牌访问。

可以为单个用户生成令牌，并赋予单独的权限和到期日期，以限制访问范围和持续时间。如果 API 令牌泄露，可以撤销令牌，而无需禁用用户本身。

API 令牌有两种基本类型：

- 分离权限：需要通过 ACL 向令牌显式授予访问权限。其有效权限通过用户权限与令牌权限取交集计算。**这是默认设置**，适用于新创建的令牌。
- 完整权限：令牌权限与关联用户的权限完全相同。只有集成确实需要用户的完整权限时，才禁用权限分离。

创建令牌时设置 `expire` 时间戳（Unix 纪元秒数），以免废弃的自动化任务悄无声息地继续运行。一旦超过期限，身份验证代码就会拒绝请求。

{% hint style="danger" %}
令牌值仅在生成令牌时显示/返回一次。之后无法再次通过 API 获取！
{% endhint %}

要使用 API 令牌，请在发出 API 请求时将 HTTP 标头 *Authorization* 设为显示的值，形式为 `PVEAPIToken=USER@REALM!TOKENID=UUID`，或参阅 API 客户端文档。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
