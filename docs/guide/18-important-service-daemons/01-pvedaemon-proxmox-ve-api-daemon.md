# 18.1. pvedaemon - Proxmox VE API Daemon <a href="#_pvedaemon_proxmox_ve_api_daemon" id="_pvedaemon_proxmox_ve_api_daemon"></a>

This daemon exposes the whole Proxmox VE API on `127.0.0.1:85`. It runs as `root` and has permission to do all privileged operations.

{% hint style="info" %}
The daemon listens to a local address only, so you cannot access it from outside. The `pveproxy` daemon exposes the API to the outside world.
{% endhint %}

## 18.1.1. Number of Workers <a href="#pvedaemon_max_workers" id="pvedaemon_max_workers"></a>

`pvedaemon` delegates handling of incoming requests to worker processes. By default, `pvedaemon` spawns 3 worker processes, which is sufficient for most workloads. For automation-heavy workloads that issue a huge volume of API requests and that experience slow request handling or timeouts, the number of worker processes can be increased by setting `MAX_WORKERS` in `/etc/default/pvedaemon`, for example:

```text
MAX_WORKERS=5
```

Note that a higher number of worker processes may result in higher CPU usage. The number of worker processes must be greater than 0 and smaller than 128.

The same setting exists for [pveproxy](02-pveproxy-proxmox-ve-api-proxy-daemon.md#pveproxy_max_workers).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
