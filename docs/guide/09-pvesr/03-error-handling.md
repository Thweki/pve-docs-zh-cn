# 9.3. Error Handling <a href="#_error_handling" id="_error_handling"></a>

If a replication job encounters problems, it is placed in an error state. In this state, the configured replication intervals get suspended temporarily. The failed replication is repeatedly tried again in a 30 minute interval. Once this succeeds, the original schedule gets activated again.

## 9.3.1. Possible issues <a href="#_possible_issues" id="_possible_issues"></a>

Some of the most common issues are in the following list. Depending on your setup there may be another cause.

- Network is not working.
- No free space left on the replication target storage.
- Storage with the same storage ID is not available on the target node.

{% hint style="info" %}
You can always use the replication log to find out what is causing the problem.
{% endhint %}

## 9.3.2. Migrating a guest in case of Error <a href="#_migrating_a_guest_in_case_of_error" id="_migrating_a_guest_in_case_of_error"></a>

In the case of a grave error, a virtual guest may get stuck on a failed node. You then need to move it manually to a working node again.

## 9.3.3. Example <a href="#_example_2" id="_example_2"></a>

Let’s assume that you have two guests (VM 100 and CT 200) running on node A and replicate to node B. Node A failed and can not get back online. Now you have to migrate the guest to Node B manually.

- connect to node B over ssh or open its shell via the web UI
- check if that the cluster is quorate

  ```text
  # pvecm status
  ```
- If you have no quorum, we strongly advise to fix this first and make the node operable again. Only if this is not possible at the moment, you may use the following command to enforce quorum on the current node:

  ```text
  # pvecm expected 1
  ```

{% hint style="warning" %}
Avoid changes which affect the cluster if `expected votes` are set (for example adding/removing nodes, storages, virtual guests) at all costs. Only use it to get vital guests up and running again or to resolve the quorum issue itself.
{% endhint %}

- move both guest configuration files form the origin node A to node B:

  ```text
  # mv /etc/pve/nodes/A/qemu-server/100.conf /etc/pve/nodes/B/qemu-server/100.conf
  # mv /etc/pve/nodes/A/lxc/200.conf /etc/pve/nodes/B/lxc/200.conf
  ```
- Now you can start the guests again:

  ```text
  # qm start 100
  # pct start 200
  ```

Remember to replace the VMIDs and node names with your respective values.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
