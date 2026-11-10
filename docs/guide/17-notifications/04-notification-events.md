# 17.4. 通知事件 <a href="#notification_events" id="notification_events"></a>

<table>




<thead>
<tr>
<th>事件</th>
<th> <code>type</code> </th>
<th>严重性</th>
<th>元数据字段（除 <code>type</code> 之外）</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>有可用的系统更新</p></td>
<td><p><code>package-updates</code></p></td>
<td><p><code>info</code></p></td>
<td><p><code>hostname</code></p></td>
</tr>
<tr>
<td><p>集群节点被隔离</p></td>
<td><p><code>fencing</code></p></td>
<td><p><code>error</code></p></td>
<td><p><code>hostname</code></p></td>
</tr>
<tr>
<td><p>存储复制任务失败</p></td>
<td><p><code>replication</code></p></td>
<td><p><code>error</code></p></td>
<td><p><code>hostname</code>, <code>job-id</code></p></td>
</tr>
<tr>
<td><p>备份成功</p></td>
<td><p><code>vzdump</code></p></td>
<td><p><code>info</code></p></td>
<td><p><code>hostname</code>、<code>job-id</code>（仅适用于备份任务）</p></td>
</tr>
<tr>
<td><p>备份失败</p></td>
<td><p><code>vzdump</code></p></td>
<td><p><code>error</code></p></td>
<td><p><code>hostname</code>、<code>job-id</code>（仅适用于备份任务）</p></td>
</tr>
<tr>
<td><p>发给 root 的邮件</p></td>
<td><p><code>system-mail</code></p></td>
<td><p><code>unknown</code></p></td>
<td><p><code>hostname</code></p></td>
</tr>
</tbody>
</table>

<table>


<thead>
<tr>
<th>字段名</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>type</code></p></td>
<td><p>通知类型</p></td>
</tr>
<tr>
<td><p><code>hostname</code></p></td>
<td><p>不含域名的主机名（例如 <code>pve1</code>）</p></td>
</tr>
<tr>
<td><p><code>job-id</code></p></td>
<td><p>任务 ID</p></td>
</tr>
</tbody>
</table>

{% hint style="info" %}
备份任务通知仅在备份任务按计划自动执行时才会设置 `job-id`；如果通过界面中的*立即运行*按钮手动触发，则不会设置。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
