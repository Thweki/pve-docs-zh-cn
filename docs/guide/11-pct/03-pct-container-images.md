# 11.3. Container Images <a href="#pct_container_images" id="pct_container_images"></a>

容器镜像有时也称为“模板”或“应用设备”，是包含运行容器所需一切的 `tar` 归档文件。Proxmox VE 可以使用两种主要类型的镜像：用于创建完整虚拟环境的 **System Container Templates**，以及基于 OCI 标准、用于运行特定应用的 **Application Container Images**。

## 11.3.1. System Container Templates <a href="#_system_container_templates" id="_system_container_templates"></a>

Proxmox VE itself provides a variety of basic templates for the [most common Linux distributions](02-pct-supported-distributions.md). They can be downloaded using the GUI or the `pveam` (short for Proxmox VE Appliance Manager) command-line utility. Additionally, [TurnKey Linux](https://www.turnkeylinux.org/) container templates are also available to download.

可用模板列表通过 *pve-daily-update* 定时器每天更新。您也可以通过执行以下命令手动触发更新：

```text
# pveam update
```

要查看可用镜像列表，请运行：

```text
# pveam available
```

您可以通过指定感兴趣的 `section` 来缩小这个大列表的范围，例如基础 `system` 镜像：

**列出可用的系统镜像**

```text
# pveam available --section system
system          alpine-3.12-default_20200823_amd64.tar.xz
system          alpine-3.13-default_20210419_amd64.tar.xz
system          alpine-3.14-default_20210623_amd64.tar.xz
system          archlinux-base_20210420-1_amd64.tar.gz
system          centos-7-default_20190926_amd64.tar.xz
system          centos-8-default_20201210_amd64.tar.xz
system          debian-9.0-standard_9.7-1_amd64.tar.gz
system          debian-10-standard_10.7-1_amd64.tar.gz
system          devuan-3.0-standard_3.0_amd64.tar.gz
system          fedora-33-default_20201115_amd64.tar.xz
system          fedora-34-default_20210427_amd64.tar.xz
system          gentoo-current-default_20200310_amd64.tar.xz
system          opensuse-15.2-default_20200824_amd64.tar.xz
system          ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz
system          ubuntu-18.04-standard_18.04.1-1_amd64.tar.gz
system          ubuntu-20.04-standard_20.04-1_amd64.tar.gz
system          ubuntu-20.10-standard_20.10-1_amd64.tar.gz
system          ubuntu-21.04-standard_21.04-1_amd64.tar.gz
```

在使用此类模板之前，您需要将其下载到您的某个存储中。如果不确定下载到哪个存储，可以直接使用名为 `local` 的存储。对于集群部署，最好使用共享存储，以便所有节点都能访问这些镜像。

```text
# pveam download local debian-10.0-standard_10.0-1_amd64.tar.gz
```

现在，您已准备好使用该镜像创建容器，并可以使用以下命令列出存储 `local` 上所有已下载的镜像：

```text
# pveam list local
local:vztmpl/debian-10.0-standard_10.0-1_amd64.tar.gz  219.95MB
```

{% hint style="success" %}
您还可以使用 Proxmox VE Web 图形用户界面（GUI）下载、列出和删除容器模板。
{% endhint %}

`pct` 使用它们创建新容器，例如：

```text
# pct create 999 local:vztmpl/debian-10.0-standard_10.0-1_amd64.tar.gz
```

上述命令会显示完整的 Proxmox VE 卷标识符。其中包含存储名称，大多数其他 Proxmox VE 命令都可以使用这些标识符。例如，您可以稍后使用以下命令删除该镜像：

```text
# pveam remove local:vztmpl/debian-10.0-standard_10.0-1_amd64.tar.gz
```

## 11.3.2. Open Container Initiative (OCI) Images <a href="#_open_container_initiative_oci_images" id="_open_container_initiative_oci_images"></a>

Proxmox VE 还可以使用 OCI 镜像创建容器，包括系统容器和应用容器。请注意，目前在 Proxmox VE 中运行应用容器仍被视为技术预览。

从 OCI 镜像创建的容器仍使用现有的 LXC 框架。

## 11.3.3. Obtaining OCI Images <a href="#_obtaining_oci_images" id="_obtaining_oci_images"></a>

在 Web 界面中，可以手动上传 OCI 镜像，也可以通过存储的容器模板视图中的 **Pull from OCI registry** 按钮从镜像仓库拉取镜像。

模板位于存储中后，您可以使用 `pct create` 创建容器，或使用 Web 界面中的向导。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
