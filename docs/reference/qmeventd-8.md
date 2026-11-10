# qmeventd(8)

## 名称 <a href="#_name" id="_name"></a>

qmeventd - PVE QEMU Eventd Daemon

## 概要 <a href="#_synopsis" id="_synopsis"></a>

**qmeventd** `[-f]` `[-v]` `PATH`

**`-v`**

Turn on verbose messages

**`-f`**

Do not daemonize server

**`PATH`**

The path to listen on

This service is usually started and managed using systemd toolset. The service is called *qmeventd*.

```text
systemctl start qmeventd
```

```text
systemctl stop qmeventd
```

```text
systemctl status qmeventd
```

## 描述 <a href="#_description" id="_description"></a>

`qmeventd` is a daemon that listens on PATH for incoming connections from a qemu qmp socket, and waits for SHUTDOWN events. When a client then disconnects, it executes `/usr/sbin/qm cleanup`. This makes it easy to clean up leftover tap devices, vgpus, etc.

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/qmeventd.8.html) · 版本 9.2.13 · 非官方中文翻译。
