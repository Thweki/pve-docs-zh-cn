# 17.4. Notification Events <a href="#notification_events" id="notification_events"></a>

<table>




<thead>
<tr>
<th>Event</th>
<th> <code>type</code> </th>
<th>Severity</th>
<th>Metadata fields (in addition to <code>type</code>)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>System updates available</p></td>
<td><p><code>package-updates</code></p></td>
<td><p><code>info</code></p></td>
<td><p><code>hostname</code></p></td>
</tr>
<tr>
<td><p>Cluster node fenced</p></td>
<td><p><code>fencing</code></p></td>
<td><p><code>error</code></p></td>
<td><p><code>hostname</code></p></td>
</tr>
<tr>
<td><p>Storage replication job failed</p></td>
<td><p><code>replication</code></p></td>
<td><p><code>error</code></p></td>
<td><p><code>hostname</code>, <code>job-id</code></p></td>
</tr>
<tr>
<td><p>Backup succeeded</p></td>
<td><p><code>vzdump</code></p></td>
<td><p><code>info</code></p></td>
<td><p><code>hostname</code>, <code>job-id</code> (only for backup jobs)</p></td>
</tr>
<tr>
<td><p>Backup failed</p></td>
<td><p><code>vzdump</code></p></td>
<td><p><code>error</code></p></td>
<td><p><code>hostname</code>, <code>job-id</code> (only for backup jobs)</p></td>
</tr>
<tr>
<td><p>Mail for root</p></td>
<td><p><code>system-mail</code></p></td>
<td><p><code>unknown</code></p></td>
<td><p><code>hostname</code></p></td>
</tr>
</tbody>
</table>

<table>


<thead>
<tr>
<th>Field name</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>type</code></p></td>
<td><p>Type of the notification</p></td>
</tr>
<tr>
<td><p><code>hostname</code></p></td>
<td><p>Hostname, without domain (e.g. <code>pve1</code>)</p></td>
</tr>
<tr>
<td><p><code>job-id</code></p></td>
<td><p>Job ID</p></td>
</tr>
</tbody>
</table>

{% hint style="info" %}
Backup job notifications only have `job-id` set if the backup job was executed automatically based on its schedule, but not if it was triggered manually by the *Run now* button in the UI.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
