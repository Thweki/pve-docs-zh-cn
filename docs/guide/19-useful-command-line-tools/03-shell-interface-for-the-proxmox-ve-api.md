# 19.3. Shell interface for the Proxmox VE API <a href="#_shell_interface_for_the_proxmox_ve_api" id="_shell_interface_for_the_proxmox_ve_api"></a>

The Proxmox VE management tool (`pvesh`) allows to directly invoke API function, without using the REST/HTTPS server.

{% hint style="info" %}
Only *root* is allowed to do that.
{% endhint %}

## 19.3.1. EXAMPLES <a href="#_examples_13" id="_examples_13"></a>

Get the list of nodes in my cluster

```text
# pvesh get /nodes
```

Get a list of available options for the datacenter

```text
# pvesh usage cluster/options -v
```

Set the HTMl5 NoVNC console as the default console for the datacenter

```text
# pvesh set cluster/options -console html5
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
