# 5.7. 仲裁 <a href="#quorum" id="quorum"></a>

Proxmox VE 使用基于仲裁的技术，在所有集群节点之间提供一致的状态。

仲裁是分布式事务为获准在分布式系统中执行操作而必须获得的最低票数。

*仲裁（分布式计算）*  
——摘自维基百科

如果发生网络分区，状态更改要求大多数节点在线。如果集群失去仲裁，将切换到只读模式。

{% hint style="info" %}
默认情况下，Proxmox VE 为每个节点分配一票。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
