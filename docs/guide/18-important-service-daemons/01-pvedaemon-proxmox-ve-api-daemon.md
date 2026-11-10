# 18.1. pvedaemon \- Proxmox VE API 守护进程 <a href="#pvedaemon_proxmox_ve_api_daemon" id="pvedaemon_proxmox_ve_api_daemon"></a>

此守护进程在 `127.0.0.1:85` 上提供完整的 Proxmox VE API。它以 `root` 身份运行，并具有执行所有特权操作的权限。

{% hint style="info" %}
此守护进程仅监听本地地址，因此无法从外部访问。`pveproxy` 守护进程将 API 对外提供。
{% endhint %}

## 18.1.1. 工作进程数量 <a href="#pvedaemon_max_workers" id="pvedaemon_max_workers"></a>

`pvedaemon` 将传入请求交给工作进程处理。默认情况下，`pvedaemon` 启动 3 个工作进程，这对大多数工作负载已经足够。对于发出大量 API 请求并遇到请求处理缓慢或超时的高度自动化工作负载，可以设置 `MAX_WORKERS` 来增加工作进程数量，此设置位于 `/etc/default/pvedaemon` 中，例如：

```text
MAX_WORKERS=5
```

请注意，增加工作进程数量可能会提高 CPU 使用率。工作进程数量必须大于 0 且小于 128。

[pveproxy](02-pveproxy-proxmox-ve-api-proxy-daemon.md#pveproxy_max_workers) 也有相同的设置。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
