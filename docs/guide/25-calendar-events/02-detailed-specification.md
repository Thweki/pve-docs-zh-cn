# 25.2. 详细规范 <a href="#detailed_specification" id="detailed_specification"></a>

**weekdays**

星期使用英文缩写指定：`sun, mon,
tue, wed, thu, fri and sat`。可以使用逗号分隔的列表指定多天。还可以使用“..”分隔起始和结束星期来指定范围，例如 `mon..fri`。这些格式可以混用。如果省略，则假定为 `'*'`。

**time-format**

时间格式由小时和分钟的间隔列表组成。小时和分钟由 `':'` 分隔。小时和分钟都可以是值列表和范围，格式与星期相同。先写小时，再写分钟。不需要时可省略小时，此时小时值假定为 `'*'`。有效值范围为：小时 `0-23`，分钟 `0-59`。

{% hint style="info" %}
可以使用 `systemd-analyze calendar` 检查给定日历事件规范是否有效，以及下次何时触发。通过传入 `--iterations=<N>` 标志，还可以使其输出日历事件接下来的 `<N>` 次触发时间（需要将 `<N>` 替换为有效整数）。
{% endhint %}

## 25.2.1. 示例： <a href="#pvesr_schedule_format_examples" id="pvesr_schedule_format_examples"></a>

以下一些特殊值具有特定含义：

<table>
<caption>表 19. 特殊值</caption>


<thead>
<tr>
<th>值</th>
<th>语法</th>
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
<td><p><code>yearly</code> 或 <code>annually</code></p></td>
<td><p><code>*-01-01 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>quarterly</code></p></td>
<td><p><code>*-01,04,07,10-01 00:00:00</code></p></td>
</tr>
<tr>
<td><p><code>semiannually</code> 或 <code>semi-annually</code></p></td>
<td><p><code>*-01,07-01 00:00:00</code></p></td>
</tr>
</tbody>
</table>

<table>
<caption>表 20. 计划示例</caption>



<thead>
<tr>
<th>计划字符串</th>
<th>替代写法</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>mon,tue,wed,thu,fri</p></td>
<td><p>mon..fri</p></td>
<td><p>每个工作日的 0:00</p></td>
</tr>
<tr>
<td><p>sat,sun</p></td>
<td><p>sat..sun</p></td>
<td><p>仅在周末的 0:00</p></td>
</tr>
<tr>
<td><p>mon,wed,fri</p></td>
<td><p>— </p></td>
<td><p>仅在星期一、星期三和星期五的 0:00</p></td>
</tr>
<tr>
<td><p>12:05</p></td>
<td><p>12:05</p></td>
<td><p>每天 12:05 PM</p></td>
</tr>
<tr>
<td><p>*/5</p></td>
<td><p>0/5</p></td>
<td><p>每五分钟</p></td>
</tr>
<tr>
<td><p>mon..wed 30/10</p></td>
<td><p>mon,tue,wed 30/10</p></td>
<td><p>星期一、星期二、星期三的每个整点后 30、40 和 50 分钟</p></td>
</tr>
<tr>
<td><p>mon..fri 8..17,22:0/15</p></td>
<td><p>— </p></td>
<td><p>每个工作日的 8 AM 到 6 PM 以及 10 PM 到 11 PM 之间，每 15 分钟</p></td>
</tr>
<tr>
<td><p>fri 12..13:5/20</p></td>
<td><p>fri 12,13:5/20</p></td>
<td><p>星期五的 12:05、12:25、12:45、13:05、13:25 和 13:45</p></td>
</tr>
<tr>
<td><p>12,14,16,18,20,22:5</p></td>
<td><p>12/2:5</p></td>
<td><p>每天从 12:05 到 22:05，每 2 小时</p></td>
</tr>
<tr>
<td><p>*</p></td>
<td><p>*/1</p></td>
<td><p>每分钟（最小间隔）</p></td>
</tr>
<tr>
<td><p>*-05</p></td>
<td><p>— </p></td>
<td><p>每月第 5 天</p></td>
</tr>
<tr>
<td><p>Sat *-1..7 15:00</p></td>
<td><p>— </p></td>
<td><p>每月第一个星期六的 15:00</p></td>
</tr>
<tr>
<td><p>2015-10-21</p></td>
<td><p>— </p></td>
<td><p>2015 年 10 月 21 日 00:00</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
