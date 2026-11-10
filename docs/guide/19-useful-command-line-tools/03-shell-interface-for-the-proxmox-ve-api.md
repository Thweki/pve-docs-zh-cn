# 19.3. Proxmox VE API 的 Shell 接口 <a href="#shell_interface_for_the_proxmox_ve_api" id="shell_interface_for_the_proxmox_ve_api"></a>

Proxmox VE 管理工具（`pvesh`）允许直接调用 API 函数，无需使用 REST/HTTPS 服务器。

{% hint style="info" %}
只有 *root* 可以这样做。
{% endhint %}

## 19.3.1. 示例 <a href="#examples_13" id="examples_13"></a>

获取我的集群中的节点列表

```text
# pvesh get /nodes
```

获取数据中心的可用选项列表

```text
# pvesh usage cluster/options -v
```

将 HTMl5 NoVNC 控制台设置为数据中心的默认控制台

```text
# pvesh set cluster/options -console html5
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
