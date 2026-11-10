# pvedaemon(8)

## 名称 <a href="#_name" id="_name"></a>

pvedaemon - PVE API Daemon

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pvedaemon"></a>



**pvedaemon** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvedaemon_help"></a>



**pvedaemon help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvedaemon_restart"></a>



**pvedaemon restart**

Restart the daemon (or start if not running).

<a id="cli_pvedaemon_start"></a>



**pvedaemon start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>`（*默认 =* `0`）**

Debug mode - stay in foreground

<a id="cli_pvedaemon_status"></a>



**pvedaemon status**

Get daemon status.

<a id="cli_pvedaemon_stop"></a>



**pvedaemon stop**

Stop the daemon.

## 描述 <a href="#_description" id="_description"></a>

This daemon exposes the whole Proxmox VE API on `127.0.0.1:85`. It runs as `root` and has permission to do all privileged operations.

{% hint style="info" %}
The daemon listens to a local address only, so you cannot access it from outside. The `pveproxy` daemon exposes the API to the outside world.
{% endhint %}

## Number of Workers <a href="#pvedaemon_max_workers" id="pvedaemon_max_workers"></a>

`pvedaemon` delegates handling of incoming requests to worker processes. By default, `pvedaemon` spawns 3 worker processes, which is sufficient for most workloads. For automation-heavy workloads that issue a huge volume of API requests and that experience slow request handling or timeouts, the number of worker processes can be increased by setting `MAX_WORKERS` in `/etc/default/pvedaemon`, for example:

```text
MAX_WORKERS=5
```

Note that a higher number of worker processes may result in higher CPU usage. The number of worker processes must be greater than 0 and smaller than 128.

The same setting exists for [pveproxy](pveproxy-8.md#pveproxy_max_workers).

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvedaemon.8.html) · 版本 9.2.13 · 非官方中文翻译。
