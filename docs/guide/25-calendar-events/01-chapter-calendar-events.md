# 25.1. Schedule Format <a href="#chapter_calendar_events" id="chapter_calendar_events"></a>

Proxmox VE has a very flexible scheduling configuration. It is based on the systemd time calendar event format.  
[see `man 7 systemd.time` for more information]  
 Calendar events may be used to refer to one or more points in time in a single expression.

Such a calendar event uses the following format:

```text
[WEEKDAY] [[YEARS-]MONTHS-DAYS] [HOURS:MINUTES[:SECONDS]]
```

This format allows you to configure a set of days on which the job should run. You can also set one or more start times. It tells the replication scheduler the moments in time when a job should start. With this information we, can create a job which runs every workday at 10 PM: `'mon,tue,wed,thu,fri 22'` which could be abbreviated to: `'mon..fri
22'`, most reasonable schedules can be written quite intuitive this way.

{% hint style="info" %}
Hours are formatted in 24-hour format.
{% endhint %}

To allow a convenient and shorter configuration, one or more repeat times per guest can be set. They indicate that replications are done on the start-time(s) itself and the start-time(s) plus all multiples of the repetition value. If you want to start replication at 8 AM and repeat it every 15 minutes until 9 AM you would use: `'8:00/15'`

Here you see that if no hour separation (`:`), is used the value gets interpreted as minute. If such a separation is used, the value on the left denotes the hour(s), and the value on the right denotes the minute(s). Further, you can use `*` to match all possible values.

To get additional ideas look at [more Examples below](02-detailed-specification.md#pvesr_schedule_format_examples).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
