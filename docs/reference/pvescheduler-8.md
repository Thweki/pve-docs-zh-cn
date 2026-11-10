# pvescheduler(8)

## 名称 <a href="#name" id="name"></a>

pvescheduler \- PVE 调度守护进程

## 概要 <a href="#synopsis" id="synopsis"></a>

### <strong>pvescheduler</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvescheduler" id="cli_pvescheduler"></a>

### <strong>pvescheduler help</strong> `[OPTIONS]` <a href="#cli_pvescheduler_help" id="cli_pvescheduler_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvescheduler restart</strong> <a href="#cli_pvescheduler_restart" id="cli_pvescheduler_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>pvescheduler start</strong> `[OPTIONS]` <a href="#cli_pvescheduler_start" id="cli_pvescheduler_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pvescheduler status</strong> <a href="#cli_pvescheduler_status" id="cli_pvescheduler_status"></a>

获取守护进程状态。

### <strong>pvescheduler stop</strong> <a href="#cli_pvescheduler_stop" id="cli_pvescheduler_stop"></a>

停止守护进程。

## 描述 <a href="#description" id="description"></a>

此守护进程负责根据计划启动任务，例如复制任务和 vzdump 任务。

对于 vzdump 任务，它从文件 `/etc/pve/jobs.cfg` 获取配置

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvescheduler.8.html) · 版本 9.2.13 · 非官方中文翻译。
