# 8.8. Ceph Configuration <a href="#pve_ceph_configuration" id="pve_ceph_configuration"></a>

Ceph daemon and clients pull their configuration from one or more sources   
[Ceph config sources [https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#config-sources](https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#config-sources)]  
. In Proxmox VE, a minimal ceph.conf file is used to hold bootstrap settings. Most of the configuration is held in the central configuration database maintained by the MON services.

To persistently change configuration values use the following commands   
[Ceph MON DB commands [https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#commands](https://docs.ceph.com/en/latest/rados/configuration/ceph-conf/#commands)]  
:

<table>


<tbody>
<tr>
<td><p><code>ceph config dump</code></p></td>
<td><p>Show all configuration option(s)</p></td>
</tr>
<tr>
<td><p><code>ceph config get &lt;who&gt; &lt;name&gt;</code></p></td>
<td><p>Show configuration option(s) for an entity</p></td>
</tr>
<tr>
<td><p><code>ceph config set &lt;who&gt; &lt;name&gt; &lt;value&gt;</code></p></td>
<td><p>Set a configuration option for one or more entities</p></td>
</tr>
<tr>
<td><p><code>ceph config rm &lt;who&gt; &lt;name&gt;</code></p></td>
<td><p>Clear a configuration option for one or more entities</p></td>
</tr>
</tbody>
</table>

**Example for increasing the osd_memory_target for all OSD daemons**

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph config set osd osd_memory_target 8G
```

{% hint style="info" %}
If an option exists in a local configuration file, the configuration in the MON DB will be ignored because it has a lower precedence.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
