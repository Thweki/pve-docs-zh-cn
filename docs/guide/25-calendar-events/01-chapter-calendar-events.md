# 25.1. 计划格式 <a href="#chapter_calendar_events" id="chapter_calendar_events"></a>

Proxmox VE 具有非常灵活的调度配置。它基于 systemd 时间日历事件格式。[\[1\]](#note-a1ddaff8-1) 日历事件可以用单个表达式引用一个或多个时间点。

此类日历事件采用以下格式：

```text
[WEEKDAY] [[YEARS-]MONTHS-DAYS] [HOURS:MINUTES[:SECONDS]]
```

此格式允许配置任务应在哪些天运行。也可以设置一个或多个开始时间。它会告知复制调度器任务应启动的时间点。根据这些信息，可以创建一个每个工作日晚上 10 点运行的任务：`'mon,tue,wed,thu,fri 22'`，可简写为：`'mon..fri
22'`；大多数合理的计划都能以这种方式直观地编写。

{% hint style="info" %}
小时采用 24 小时制。
{% endhint %}

为使配置更方便、简短，可以为每个客户机设置一个或多个重复时间。它们表示在开始时间本身，以及开始时间加上重复值的所有倍数时执行复制。如果希望从上午 8 点开始复制，并每 15 分钟重复一次直到上午 9 点，可以使用：`'8:00/15'`

这里可以看到，如果未使用小时分隔符（`:`），则该值解释为分钟。如果使用此分隔符，则左侧值表示小时，右侧值表示分钟。此外，还可以使用 `*` 匹配所有可能值。

更多思路请查看[下方的更多示例](02-detailed-specification.md#pvesr_schedule_format_examples)。

## 注释

### 注释 1 <a href="#note-a1ddaff8-1" id="note-a1ddaff8-1"></a>

更多信息请参见 `man 7 systemd.time`

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
