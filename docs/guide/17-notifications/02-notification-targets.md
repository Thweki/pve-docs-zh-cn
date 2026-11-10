# 17.2. 通知目标 <a href="#notification_targets" id="notification_targets"></a>

Proxmox VE 提供多种类型的通知目标。

## 17.2.1. Sendmail <a href="#notification_targets_sendmail" id="notification_targets_sendmail"></a>

[![screenshot/gui-datacenter-notification-sendmail.png](../../assets/screenshot-gui-datacenter-notification-sendmail-png-17b7e706eb02.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-notification-sendmail.png)

sendmail 二进制程序是类 Unix 操作系统上常见的程序，负责发送电子邮件。它是一个命令行实用程序，允许用户和应用程序直接从命令行或脚本中发送电子邮件。

sendmail 通知目标使用 `sendmail` 二进制程序，向配置的用户或电子邮件地址列表发送邮件。如果选择用户作为收件人，将使用该用户设置中配置的电子邮件地址。对于 `root@pam` 用户，这是安装期间输入的电子邮件地址。可以在 `Datacenter → Permissions → Users` 中配置用户的电子邮件地址。如果用户没有关联的电子邮件地址，则不会发送邮件。

{% hint style="info" %}
在标准 Proxmox VE 安装中，`sendmail` 二进制程序由 Postfix 提供。可能需要配置 Postfix 才能正确投递邮件，例如设置外部邮件中继（智能主机）。如果投递失败，请查看系统日志中 Postfix 守护进程记录的消息。
{% endhint %}

Sendmail 目标插件的配置包含以下选项：

- `mailto`：接收通知的电子邮件地址。可以多次设置，以指定多个收件人。
- `mailto-user`：接收电子邮件的用户。将从 `users.cfg` 中查找用户的电子邮件地址。可以多次设置，以指定多个收件人。
- `author`：设置电子邮件的作者。默认为 `Proxmox VE`。
- `from-address`：设置电子邮件的发件地址。如果未设置此参数，插件将回退到 `email_from` 设置，该设置来自 `datacenter.cfg`。如果该设置也未设置，插件将默认使用 `root@$hostname`，其中 `$hostname` 为节点的主机名。邮件中的 `From` 标头将设置为 `$author <$from-address>`。
- `comment`：此目标的注释

配置示例（`/etc/pve/notifications.cfg`）：

```text
sendmail: example
        mailto-user root@pam
        mailto-user admin@pve
        mailto max@example.com
        from-address pve1@example.com
        comment Send to multiple users/addresses
```

## 17.2.2. SMTP <a href="#notification_targets_smtp" id="notification_targets_smtp"></a>

[![screenshot/gui-datacenter-notification-smtp.png](../../assets/screenshot-gui-datacenter-notification-smtp-png-97310312d2e2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-notification-smtp.png)

SMTP 通知目标可以直接向 SMTP 邮件中继发送电子邮件。此目标不使用系统的 MTA 投递邮件。与 sendmail 目标类似，如果选择用户作为收件人，则使用该用户配置的电子邮件地址。

{% hint style="info" %}
与 sendmail 目标不同，SMTP 目标在邮件投递失败时没有任何排队/重试机制。
{% endhint %}

SMTP 目标插件的配置包含以下选项：

- `mailto`：接收通知的电子邮件地址。可以多次设置，以指定多个收件人。
- `mailto-user`：接收电子邮件的用户。将从 `users.cfg` 中查找用户的电子邮件地址。可以多次设置，以指定多个收件人。
- `author`：设置电子邮件的作者。默认为 `Proxmox VE`。
- `from-address`：设置电子邮件的发件地址。为防止伪造，SMTP 中继可能要求此地址属于该用户。邮件中的 `From` 标头将设置为 `$author <$from-address>`。
- `username`：认证时使用的用户名。如果未设置用户名，则不进行认证。支持 PLAIN 和 LOGIN 认证方式。
- `password`：认证时使用的密码。
- `mode`：设置加密模式（`insecure`、`starttls` 或 `tls`）。默认为 `tls`。
- `server`：SMTP 中继的地址/IP。
- `port`：要连接的端口。如果未设置，使用的端口默认为 25（`insecure`）、465（`tls`）或 587（`starttls`），具体取决于 `mode` 的值。
- `comment`：此目标的注释

配置示例（`/etc/pve/notifications.cfg`）：

```text
smtp: example
        mailto-user root@pam
        mailto-user admin@pve
        mailto max@example.com
        from-address pve1@example.com
        username pve1
        server mail.example.com
        mode starttls
```

`/etc/pve/priv/notifications.cfg` 中包含密码的对应条目：

```text
smtp: example
        password somepassword
```

## 17.2.3. Gotify <a href="#notification_targets_gotify" id="notification_targets_gotify"></a>

[![screenshot/gui-datacenter-notification-gotify.png](../../assets/screenshot-gui-datacenter-notification-gotify-png-1b8ec9289482.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-notification-gotify.png)

[Gotify](http://gotify.net) 是一个开源的自托管通知服务器，可用于向各种设备和应用程序发送及接收推送通知。它提供简单的 API 和 Web 界面，便于与不同平台和服务集成。

Gotify 目标插件的配置包含以下选项：

- `server`：Gotify 服务器的基本 URL，例如 `http://<ip>:8888`
- `token`：认证令牌。可以在 Gotify Web 界面中生成令牌。
- `comment`：此目标的注释

{% hint style="info" %}
Gotify 目标插件会遵循[数据中心配置](../24-configuration-files-2/02-datacenter-configuration-file.md)中的 HTTP 代理设置
{% endhint %}

配置示例（`/etc/pve/notifications.cfg`）：

```text
gotify: example
        server http://gotify.example.com:8888
        comment Send to multiple users/addresses
```

`/etc/pve/priv/notifications.cfg` 中包含秘密令牌的对应条目：

```text
gotify: example
        token somesecrettoken
```

## 17.2.4. Webhook <a href="#notification_targets_webhook" id="notification_targets_webhook"></a>

Webhook 通知目标向可配置的 URL 发出 HTTP 请求。

可用的配置选项如下：

- `url`：执行 HTTP 请求的目标 URL。支持使用模板注入消息内容、元数据和秘密信息。
- `method`：使用的 HTTP 方法（POST/PUT/GET）
- `header`：为请求设置的 HTTP 标头数组。支持使用模板注入消息内容、元数据和秘密信息。
- `body`：要发送的 HTTP 正文。支持使用模板注入消息内容、元数据和秘密信息。
- `secret`：秘密键值对数组。这些内容将保存在只有 root 可以读取的受保护配置文件中。可以通过 `secrets` 命名空间在正文/标头/URL 模板中访问秘密信息。
- `comment`：此目标的注释。

对于支持模板的配置选项，可以使用 [Handlebars](https://handlebarsjs.com/) 语法访问以下属性：

- `{{ title }}`：渲染后的通知标题
- `{{ message }}`：渲染后的通知正文
- `{{ severity }}`：通知的严重性（`info`、`notice`、`warning`、`error`、`unknown`）
- `{{ timestamp }}`：以 UNIX 纪元时间表示的通知时间戳（秒）。
- `{{ fields.<name> }}`：通知各个元数据字段的子命名空间。例如，`fields.type` 包含通知类型；所有可用字段请参阅[通知事件](04-notification-events.md)。
- `{{ secrets.<name> }}`：秘密信息的子命名空间。例如，名为 `token` 的秘密信息可以通过 `secrets.token` 访问。

为方便使用，提供以下辅助函数：

- `{{ url-encode <value/property> }}`：对属性/字面量进行 URL 编码。
- `{{ escape <value/property> }}`：转义无法安全地表示为 JSON 字符串的控制字符。
- `{{ json <value/property> }}`：将值渲染为 JSON。这适合将整个子命名空间（例如 `fields`）作为 JSON 载荷的一部分（例如 `{{ json fields }}`）传递。

### 示例 <a href="#examples_11" id="examples_11"></a>

#### `ntfy.sh` <a href="#span_class_monospaced_ntfy_sh_span" id="span_class_monospaced_ntfy_sh_span"></a>

- 方法：`POST`
- URL：`https://ntfy.sh/{{ secrets.channel }}`
- 标头：

  - `Markdown`: `Yes`
- 正文：

````text
```
{{ message }}
```
````

- 秘密信息：

  - `channel`: `<your ntfy.sh channel>`

#### Discord <a href="#discord" id="discord"></a>

- 方法：`POST`
- URL：`https://discord.com/api/webhooks/{{ secrets.token }}`
- 标头：

  - `Content-Type`: `application/json`
- 正文：

````text
{
  "content": "``` {{ escape message }}```"
}
````

- 秘密信息：

  - `token`: `<token>`

#### Slack <a href="#slack" id="slack"></a>

- 方法：`POST`
- URL：`https://hooks.slack.com/services/{{ secrets.token }}`
- 标头：

  - `Content-Type`: `application/json`
- 正文：

````text
{
  "text": "``` {{escape message}}```",
  "type": "mrkdwn"
}
````

- 秘密信息：

  - `token`: `<token>`

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
