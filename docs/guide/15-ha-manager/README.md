# 15\. High Availability <a href="#chapter_ha_manager" id="chapter_ha_manager"></a>

我们的现代社会高度依赖计算机通过网络提供的信息。移动设备加剧了这种依赖，因为人们可以随时随地访问网络。如果您提供此类服务，那么确保它们在绝大多数时间内可用就非常重要。

我们可以从数学上将可用性定义为 (A)（在给定时间间隔内服务能够被使用的总时间）与 (B)（该时间间隔的长度）之比。通常以给定年份内正常运行时间的百分比表示。

<table>
<caption>Table 17. Availability - Downtime per Year</caption>


<thead>
<tr>
<th>可用性 %</th>
<th>每年停机时间</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>99</p></td>
<td><p>3.65 days</p></td>
</tr>
<tr>
<td><p>99.9</p></td>
<td><p>8.76 hours</p></td>
</tr>
<tr>
<td><p>99.99</p></td>
<td><p>52.56 minutes</p></td>
</tr>
<tr>
<td><p>99.999</p></td>
<td><p>5.26 minutes</p></td>
</tr>
<tr>
<td><p>99.9999</p></td>
<td><p>31.5 seconds</p></td>
</tr>
<tr>
<td><p>99.99999</p></td>
<td><p>3.15 seconds</p></td>
</tr>
</tbody>
</table>

提高可用性有多种方法。最优雅的解决方案是重写您的软件，以便您可以同时在多台宿主机上运行它。软件本身需要具备检测错误和执行故障转移的方法。如果您只想提供只读网页，那么这相对简单。然而，这通常很复杂，有时甚至不可能，因为您无法自行修改软件。以下解决方案无需修改软件即可工作：

- 使用可靠的“服务器”组件

  {% hint style="info" %}
  具有相同功能的计算机组件，其可靠性指标可能因组件质量而异。大多数供应商将可靠性更高的组件作为“服务器”组件出售——通常价格也更高。
  {% endhint %}
- 消除单点故障（冗余组件）

  - 使用不间断电源（UPS）
  - 在服务器中使用冗余电源
  - 使用 ECC-RAM
  - 使用冗余网络硬件
  - 为本地存储使用 RAID
  - 为 VM 数据使用分布式冗余存储
- 减少停机时间

  - 可快速联系到的管理员（24/7）
  - 备件的可用性（Proxmox VE 集群中的其他节点）
  - 自动错误检测（由`ha-manager`提供）
  - 自动故障转移（由`ha-manager`提供）

像 Proxmox VE 这样的虚拟化环境消除了对“硬件”的依赖，因此更容易实现高可用性。它们还支持配置和使用冗余存储及网络设备，因此，如果一台宿主机发生故障，您只需在集群中的另一台宿主机上启动这些服务即可。

更棒的是，Proxmox VE 提供了一个名为`ha-manager`的软件栈，它可以自动为您完成这些操作。它能够自动检测错误并执行自动故障转移。

Proxmox VE `ha-manager`的工作方式就像一位“自动化”管理员。首先，您要配置它应管理哪些资源（VM、容器……）。然后，`ha-manager`会监视其是否正常运行，并在发生错误时将服务故障转移到另一个节点。`ha-manager`还可以处理可能启动、停止、重新定位和迁移服务的普通用户请求。

但高可用性是有代价的。高质量组件价格更高，而使其冗余至少会使成本翻倍。额外的备件会进一步增加成本。因此，您应仔细计算收益，并与这些额外成本进行比较。

{% hint style="success" %}
将可用性从 99% 提高到 99.9% 相对简单。但将可用性从 99.9999% 提高到 99.99999% 则非常困难且成本高昂。`ha-manager`的典型错误检测和故障转移时间约为 2 minutes，因此您最多只能获得 99.999% 的可用性。
{% endhint %}

## 本章内容

- [15.1. Requirements](01-requirements-2.md)
- [15.2. Resources](02-ha-manager-resources.md)
- [15.3. Management Tasks](03-management-tasks.md)
- [15.4. How It Works](04-how-it-works-2.md)
- [15.5. HA Simulator](05-ha-simulator.md)
- [15.6. Configuration](06-configuration-15.md)
- [15.7. Fencing](07-ha-manager-fencing.md)
- [15.8. Start Failure Policy](08-ha-manager-start-failure-policy.md)
- [15.9. Error Recovery](09-ha-manager-error-recovery.md)
- [15.10. Package Updates](10-ha-manager-package-updates.md)
- [15.11. Node Maintenance](11-ha-manager-node-maintenance.md)
- [15.12. Disarming HA for Cluster Maintenance](12-ha-manager-disarm.md)
- [15.13. Cluster Resource Scheduling](13-ha-manager-crs.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
