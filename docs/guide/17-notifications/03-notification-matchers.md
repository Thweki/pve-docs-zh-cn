# 17.3. 通知匹配器 <a href="#notification_matchers" id="notification_matchers"></a>

[![screenshot/gui-datacenter-notification-matcher.png](../../assets/screenshot-gui-datacenter-notification-matcher-png-ce9976b1ea69.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-notification-matcher.png)

通知匹配器根据其匹配规则将通知路由到通知目标。这些规则可以匹配通知的某些属性，例如时间戳（`match-calendar`）、通知的严重性（`match-severity`）或元数据字段（`match-field`）。如果通知被某个匹配器匹配，为该匹配器配置的所有目标都会收到通知。

可以创建任意数量的匹配器，每个匹配器都有自己的匹配规则和通知目标。即使同一目标用于多个匹配器，每个通知也最多向该目标发送一次。

没有任何匹配规则的匹配器始终为真；配置的目标始终会收到通知。

```text
matcher: always-matches
        target admin
        comment This matcher always matches
```

## 17.3.1. 匹配器选项 <a href="#matcher_options" id="matcher_options"></a>

- `target`：确定匹配器匹配时应通知哪个目标。可以多次使用，以通知多个目标。
- `invert-match`：反转整个匹配器的结果
- `mode`：确定如何求值各个匹配规则，以计算整个匹配器的结果。如果设置为 `all`，则所有匹配规则都必须匹配。如果设置为 `any`，则至少一个规则必须匹配。默认为 `all`。
- `match-calendar`：将通知的时间戳与时间计划匹配。
- `match-field`：匹配通知的元数据字段。
- `match-severity`：匹配通知的严重性。
- `comment`：此匹配器的注释。

## 17.3.2. 日历匹配规则 <a href="#notification_matchers_calendar" id="notification_matchers_calendar"></a>

日历匹配器将通知发送的时间与可配置的时间计划进行匹配。

- `match-calendar 8-12`
- `match-calendar 8:00-15:30`
- `match-calendar mon..fri 9:00-17:00`
- `match-calendar sun,tue..wed,fri 9-17`

## 17.3.3. 字段匹配规则 <a href="#notification_matchers_field" id="notification_matchers_field"></a>

通知具有一些可供匹配的元数据字段。使用 `exact` 作为匹配模式时，可以使用 `,` 作为分隔符。只要元数据字段具有指定值中的**任意一个**，匹配规则就会匹配。

- `match-field exact:type=vzdump` 仅匹配与备份有关的通知。
- `match-field exact:type=replication,fencing` 匹配 `replication` 和 `fencing` 通知。
- `match-field regex:hostname=^.+\.example\.com$` 匹配节点的主机名。

如果要匹配的元数据字段不存在，通知将不会被匹配。例如，`match-field regex:hostname=.*` 指令只会匹配具有任意 `hostname` 元数据字段的通知，如果该字段不存在，则不会匹配。

## 17.3.4. 严重性匹配规则 <a href="#notification_matchers_severity" id="notification_matchers_severity"></a>

通知具有关联的严重性，可用于匹配。

- `match-severity error`：仅匹配错误
- `match-severity warning,error`：匹配警告和错误

使用以下严重性：`info`、`notice`、`warning`、`error`、`unknown`。

## 17.3.5. 示例 <a href="#examples_12" id="examples_12"></a>

```text
matcher: workday
        match-calendar mon..fri 9-17
        target admin
        comment Notify admins during working hours

matcher: night-and-weekend
        match-calendar mon..fri 9-17
        invert-match true
        target on-call-admins
        comment Separate target for non-working hours
```

```text
matcher: backup-failures
        match-field exact:type=vzdump
        match-severity error
        target backup-admins
        comment Send notifications about backup failures to one group of admins

matcher: cluster-failures
        match-field exact:type=replication,fencing
        target cluster-admins
        comment Send cluster-related notifications to other group of admins
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
