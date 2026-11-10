# qmeventd(8)

## 名称 <a href="#name" id="name"></a>

qmeventd \- PVE QEMU Eventd 守护进程

## 概要 <a href="#synopsis" id="synopsis"></a>

**qmeventd** `[-f]` `[-v]` `PATH`

**`-v`**

启用详细消息

**`-f`**

不要将服务器守护进程化

**`PATH`**

监听的路径

此服务通常使用 systemd 工具集启动和管理。服务名为 *qmeventd*。

```text
systemctl start qmeventd
```

```text
systemctl stop qmeventd
```

```text
systemctl status qmeventd
```

## 描述 <a href="#description" id="description"></a>

`qmeventd` 是一个守护进程，在 PATH 上监听来自 qemu qmp 套接字的传入连接，并等待 SHUTDOWN 事件。随后当客户端断开连接时，它会执行 `/usr/sbin/qm cleanup`。这使清理残留的 tap 设备、vgpu 等变得容易。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/qmeventd.8.html) · 版本 9.2.13 · 非官方中文翻译。
