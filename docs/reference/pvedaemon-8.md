# pvedaemon(8)

## 名称 <a href="#name" id="name"></a>

pvedaemon \- PVE API 守护进程

## 概要 <a href="#synopsis" id="synopsis"></a>

### <strong>pvedaemon</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvedaemon" id="cli_pvedaemon"></a>

### <strong>pvedaemon help</strong> `[OPTIONS]` <a href="#cli_pvedaemon_help" id="cli_pvedaemon_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvedaemon restart</strong> <a href="#cli_pvedaemon_restart" id="cli_pvedaemon_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>pvedaemon start</strong> `[OPTIONS]` <a href="#cli_pvedaemon_start" id="cli_pvedaemon_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pvedaemon status</strong> <a href="#cli_pvedaemon_status" id="cli_pvedaemon_status"></a>

获取守护进程状态。

### <strong>pvedaemon stop</strong> <a href="#cli_pvedaemon_stop" id="cli_pvedaemon_stop"></a>

停止守护进程。

## 描述 <a href="#description" id="description"></a>

此守护进程在 `127.0.0.1:85` 上提供完整的 Proxmox VE API。它以 `root` 身份运行，并具有执行所有特权操作的权限。

{% hint style="info" %}
此守护进程仅监听本地地址，因此无法从外部访问。`pveproxy` 守护进程将 API 对外提供。
{% endhint %}

## 工作进程数量 <a href="#pvedaemon_max_workers" id="pvedaemon_max_workers"></a>

`pvedaemon` 将传入请求交给工作进程处理。默认情况下，`pvedaemon` 启动 3 个工作进程，这对大多数工作负载已经足够。对于发出大量 API 请求并遇到请求处理缓慢或超时的高度自动化工作负载，可以设置 `MAX_WORKERS` 来增加工作进程数量，此设置位于 `/etc/default/pvedaemon` 中，例如：

```text
MAX_WORKERS=5
```

请注意，增加工作进程数量可能会提高 CPU 使用率。工作进程数量必须大于 0 且小于 128。

[pveproxy](pveproxy-8.md#pveproxy_max_workers) 也有相同的设置。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvedaemon.8.html) · 版本 9.2.13 · 非官方中文翻译。
