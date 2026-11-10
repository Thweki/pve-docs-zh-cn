# 8.8. Ceph 配置 <a href="#pve_ceph_configuration" id="pve_ceph_configuration"></a>

Ceph 守护进程和客户端从一个或多个配置源 [\[1\]](#note-02fbf917-1) 获取其配置。在 Proxmox VE 中，使用一个最小的 ceph.conf 文件来保存引导设置。大多数配置保存在由 MON 服务维护的中央配置数据库中。

要持久化更改配置值，请使用以下命令 [\[2\]](#note-02fbf917-2)：

<table>


<tbody>
<tr>
<td><p><code>ceph config dump</code></p></td>
<td><p>显示所有配置选项</p></td>
</tr>
<tr>
<td><p><code>ceph config get &lt;who&gt; &lt;name&gt;</code></p></td>
<td><p>显示某个实体的配置选项</p></td>
</tr>
<tr>
<td><p><code>ceph config set &lt;who&gt; &lt;name&gt; &lt;value&gt;</code></p></td>
<td><p>为一个或多个实体设置配置选项</p></td>
</tr>
<tr>
<td><p><code>ceph config rm &lt;who&gt; &lt;name&gt;</code></p></td>
<td><p>清除一个或多个实体的配置选项</p></td>
</tr>
</tbody>
</table>

**为所有 OSD 守护进程增大 osd\_memory\_target 的示例**

```text
ceph config set osd osd_memory_target 8G
```

{% hint style="info" %}
如果某个选项存在于本地配置文件中，MON DB 中的配置将被忽略，因为其优先级较低。
{% endhint %}

## 注释

### 注释 1 <a href="#note-02fbf917-1" id="note-02fbf917-1"></a>

Ceph 配置源 [https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#config-sources](https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#config-sources)

### 注释 2 <a href="#note-02fbf917-2" id="note-02fbf917-2"></a>

Ceph MON DB 命令 [https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#commands](https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#commands)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
