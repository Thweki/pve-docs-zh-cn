# 25.2. Detailed Specification <a href="#_detailed_specification" id="_detailed_specification"></a>

**weekdays**

Days are specified with an abbreviated English version: `sun, mon,
tue, wed, thu, fri and sat`. You may use multiple days as a comma-separated list. A range of days can also be set by specifying the start and end day separated by “..”, for example `mon..fri`. These formats can be mixed. If omitted `'*'` is assumed.

**time-format**

A time format consists of hours and minutes interval lists. Hours and minutes are separated by `':'`. Both hour and minute can be list and ranges of values, using the same format as days. First are hours, then minutes. Hours can be omitted if not needed. In this case `'*'` is assumed for the value of hours. The valid range for values is `0-23` for hours and `0-59` for minutes.

{% hint style="info" %}
You can use `systemd-analyze calendar` to see whether a given calendar event specification is valid and when it would be triggered next. By passing the `--iterations=<N>` flag you can also let it output the next `<N>` times the calendar event would trigger (you need to replace `<N>` with a valid integer).
{% endhint %}

## 25.2.1. Examples: <a href="#pvesr_schedule_format_examples" id="pvesr_schedule_format_examples"></a>

There are some special values that have a specific meaning:

<table>
<caption>Table 19. Special Values</caption>


<thead>
<tr>
<th>Value</th>
<th>Syntax</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>minutely</code></p></td>
<td><p><code>*-*-* *:*:00</code></p></td>
</tr>
<tr>
<td><p><code>hourly</code></p></td>
<td><p><code>*-*-* *:00:00</code></p></td>
</tr>
<tr>
<td><p><code>daily</code></p></td>
<td><p><code>*-*-* 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>weekly</code></p></td>
<td><p><code>mon *-*-* 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>monthly</code></p></td>
<td><p><code>*-*-01 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>yearly</code> or <code>annually</code></p></td>
<td><p><code>*-01-01 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>quarterly</code></p></td>
<td><p><code>*-01,04,07,10-01 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>semiannually</code> or <code>semi-annually</code></p></td>
<td><p><code>*-01,07-01 00:00:00</code></p></td>
</tr>
</tbody>
</table>

<table>
<caption>Table 20. Schedule Examples</caption>



<thead>
<tr>
<th>Schedule String</th>
<th>Alternative</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>mon,tue,wed,thu,fri</p></td>
<td><p>mon..fri</p></td>
<td><p>Every working day at 0:00</p></td>
</tr>
<tr>
<td><p>sat,sun</p></td>
<td><p>sat..sun</p></td>
<td><p>Only on weekends at 0:00</p></td>
</tr>
<tr>
<td><p>mon,wed,fri</p></td>
<td><p>— </p></td>
<td><p>Only on Monday, Wednesday and Friday at 0:00</p></td>
</tr>
<tr>
<td><p>12:05</p></td>
<td><p>12:05</p></td>
<td><p>Every day at 12:05 PM</p></td>
</tr>
<tr>
<td><p>*/5</p></td>
<td><p>0/5</p></td>
<td><p>Every five minutes</p></td>
</tr>
<tr>
<td><p>mon..wed 30/10</p></td>
<td><p>mon,tue,wed 30/10</p></td>
<td><p>Monday, Tuesday, Wednesday 30, 40 and 50 minutes after every full hour</p></td>
</tr>
<tr>
<td><p>mon..fri 8..17,22:0/15</p></td>
<td><p>— </p></td>
<td><p>Every working day every 15 minutes between 8 AM and 6 PM and between 10 PM and 11 PM</p></td>
</tr>
<tr>
<td><p>fri 12..13:5/20</p></td>
<td><p>fri 12,13:5/20</p></td>
<td><p>Friday at 12:05, 12:25, 12:45, 13:05, 13:25 and 13:45</p></td>
</tr>
<tr>
<td><p>12,14,16,18,20,22:5</p></td>
<td><p>12/2:5</p></td>
<td><p>Every day starting at 12:05 until 22:05, every 2 hours</p></td>
</tr>
<tr>
<td><p>*</p></td>
<td><p>*/1</p></td>
<td><p>Every minute (minimum interval)</p></td>
</tr>
<tr>
<td><p>*-05</p></td>
<td><p>— </p></td>
<td><p>On the 5th day of every Month</p></td>
</tr>
<tr>
<td><p>Sat *-1..7 15:00</p></td>
<td><p>— </p></td>
<td><p>First Saturday each Month at 15:00</p></td>
</tr>
<tr>
<td><p>2015-10-21</p></td>
<td><p>— </p></td>
<td><p>21st October 2015 at 00:00</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
