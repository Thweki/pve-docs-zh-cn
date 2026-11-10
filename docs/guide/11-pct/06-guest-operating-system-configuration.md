# 11.6. Guest Operating System Configuration <a href="#_guest_operating_system_configuration" id="_guest_operating_system_configuration"></a>

Proxmox VE 会尝试检测容器中的 Linux 发行版，并修改一些文件。以下是容器启动时所执行操作的简要列表：

**设置 /etc/hostname**

以设置容器名称

**修改 /etc/hosts**

以允许查询本地主机名

**网络配置**

将完整的网络配置传递给容器

**配置 DNS**

传递有关 DNS 服务器的信息

**调整 init 系统**

例如，修正生成的 getty 进程数量

**设置 root 密码**

在创建新容器时

**重写 ssh\_host\_keys**

使每个容器都有唯一的密钥

**随机化 crontab**

使 cron 不会在所有容器中同时启动

Proxmox VE 所做的更改会用注释标记括起来：

```text
# --- BEGIN PVE ---
<data>
# --- END PVE ---
```

这些标记会插入文件中的合理位置。如果这样的节已经存在，则会就地更新，不会移动。

可以通过为相应文件添加一个 `.pve-ignore.` 文件来阻止修改该文件。例如，如果存在 `/etc/.pve-ignore.hosts` 文件，则不会改动 `/etc/hosts` 文件。该文件可以是通过以下命令创建的简单空文件：

```text
# touch /etc/.pve-ignore.hosts
```

大多数修改取决于操作系统，因此会因发行版和版本而异。您可以通过手动将 `ostype` 设置为 `unmanaged` 来完全禁用这些修改。

操作系统类型检测通过测试容器内的特定文件来完成。Proxmox VE 首先检查 `/etc/os-release` 文件[\[1\]](#note-0a8e0f70-1)。如果该文件不存在，或者其中不包含清晰可辨的发行版标识符，则会检查以下发行版专用的版本文件。

**Ubuntu**

检查 /etc/lsb-release（`DISTRIB_ID=Ubuntu`）

**Debian**

检查 /etc/debian\_version

**Fedora**

检查 /etc/fedora-release

**RedHat 或 CentOS**

检查 /etc/redhat-release

**ArchLinux**

检查 /etc/arch-release

**Alpine**

检查 /etc/alpine-release

**Gentoo**

检查 /etc/gentoo-release

{% hint style="info" %}
如果配置的 `ostype` 与自动检测到的类型不同，容器将无法启动。
{% endhint %}

## 注释

### 注释 1 <a href="#note-0a8e0f70-1" id="note-0a8e0f70-1"></a>

/etc/os-release 取代了众多的各发行版专用版本文件 [https://manpages.debian.org/stable/systemd/os-release.5.en.html](https://manpages.debian.org/stable/systemd/os-release.5.en.html)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
