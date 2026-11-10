# 20\. 常见问题 <a href="#frequently_asked_questions_2" id="frequently_asked_questions_2"></a>

{% hint style="info" %}
新的常见问题会附加到本节底部。
{% endhint %}

1. <em> Proxmox VE 基于哪个发行版？ </em>

   Proxmox VE 基于 [Debian GNU/Linux](https://www.debian.org)
2. <em> Proxmox VE 项目使用什么许可证？ </em>

   Proxmox VE 代码根据 GNU Affero 通用公共许可证第 3 版授权。
3. <em> Proxmox VE 可以在 32bit 处理器上运行吗？ </em>

   Proxmox VE 仅能在 64-bit CPU 上运行。支持的架构为 x86\_64（AMD64 或 Intel 64），以及 NVIDIA Grace Hopper 和 NVIDIA Vera 平台上的 aarch64。没有支持 32-bit 宿主机的计划。

   {% hint style="info" %}
   虚拟机和容器均可以为 32-bit 或 64-bit。
   {% endhint %}
4. <em> 我的 CPU 是否支持虚拟化？ </em>

   要检查 CPU 是否兼容虚拟化，请查看以下命令输出中是否具有 `vmx` 或 `svm` 标志：

   ```text
   egrep '(vmx|svm)' /proc/cpuinfo
   ```

   {% hint style="info" %}
   此检查仅适用于 x86 宿主机。在支持的 arm64 平台上，KVM 硬件辅助虚拟化可用，并且不会报告等效的 CPU 标志。
   {% endhint %}
5. <em> 支持的 Intel CPU </em>

   [Intel 虚拟化技术（Intel VT-x）](https://en.wikipedia.org/wiki/Virtualization_Technology#Intel_virtualization_.28VT-x.29)受支持的 64-bit 处理器。（[支持 Intel VT 和 64-bit 的处理器列表](https://ark.intel.com/content/www/us/en/ark/search/featurefilter.html?productType=873&2_VTX=True&2_InstructionSet=64-bit)）
6. <em> 支持的 AMD CPU </em>

   支持 [AMD 虚拟化技术（AMD-V）](https://en.wikipedia.org/wiki/Virtualization_Technology#AMD_virtualization_.28AMD-V.29) 的 64-bit 处理器。
7. <em> 支持的 arm64 平台 </em>

   NVIDIA Grace Hopper 和 NVIDIA Vera 平台。详情请参阅[64-bit ARM（arm64）支持](../02-installation/README.md#install_arm64_support)。
8. <em> 什么是容器/虚拟环境（VE）/virtual私有服务器（VPS）？ </em>

   在容器的语境中，这些术语都指操作系统级虚拟化这一概念。操作系统级虚拟化是一种虚拟化方法：操作系统的内核允许多个隔离的实例运行，所有实例共享该内核。在提及 LXC 时，我们将这种实例称为容器。由于容器使用宿主机的内核，而不是模拟完整的操作系统，因此开销更小，但仅限于 Linux 客户机。
9. <em> 什么是 QEMU/KVM 客户机（或 VM）？ </em>

   QEMU/KVM 客户机（或 VM）是使用 QEMU 和 Linux KVM 内核模块在 Proxmox VE 下以虚拟化方式运行的客户机系统。
10. <em> 什么是 QEMU？ </em>

    QEMU 是一种通用的开源机器模拟器和虚拟化工具。QEMU 使用 Linux KVM 内核模块，直接在宿主机 CPU 上执行客户机代码，从而实现接近原生的性能。它不限于 Linux 客户机，而是允许任意操作系统运行。
11. <em> 我的 Proxmox VE 版本会获得多长时间的支持？ </em>

    Proxmox VE 版本的支持期<strong>至少与</strong>对应 Debian 版本获得 Debian 安全团队支持的期限一样长，即首次发布后约 3 年，参见 [Debian 生命周期](https://www.debian.org/security/faq#lifespan)。Proxmox VE 使用滚动发布模式，始终建议使用最新的稳定版本。

    <table id="faq-support-table">





    <thead>
    <tr>
    <th>Proxmox VE 版本</th>
    <th>Debian 版本</th>
    <th>首次发布</th>
    <th>Debian 支持终止</th>
    <th>Proxmox 支持终止</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Proxmox VE 9</p></td>
    <td><p>Debian 13（Trixie）</p></td>
    <td><p>2025-08</p></td>
    <td><p>待公布</p></td>
    <td><p>待公布</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 8</p></td>
    <td><p>Debian 12（Bookworm）</p></td>
    <td><p>2023-06</p></td>
    <td><p>2026-07</p></td>
    <td><p>2026-08</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 7</p></td>
    <td><p>Debian 11（Bullseye）</p></td>
    <td><p>2021-07</p></td>
    <td><p>2024-07</p></td>
    <td><p>2024-07</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 6</p></td>
    <td><p>Debian 10（Buster）</p></td>
    <td><p>2019-07</p></td>
    <td><p>2022-09</p></td>
    <td><p>2022-09</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 5</p></td>
    <td><p>Debian 9（Stretch）</p></td>
    <td><p>2017-07</p></td>
    <td><p>2020-07</p></td>
    <td><p>2020-07</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 4</p></td>
    <td><p>Debian 8（Jessie）</p></td>
    <td><p>2015-10</p></td>
    <td><p>2018-06</p></td>
    <td><p>2018-06</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 3</p></td>
    <td><p>Debian 7（Wheezy）</p></td>
    <td><p>2013-05</p></td>
    <td><p>2016-04</p></td>
    <td><p>2017-02</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 2</p></td>
    <td><p>Debian 6（Squeeze）</p></td>
    <td><p>2012-04</p></td>
    <td><p>2014-05</p></td>
    <td><p>2014-05</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 1</p></td>
    <td><p>Debian 5（Lenny）</p></td>
    <td><p>2008-10</p></td>
    <td><p>2012-03</p></td>
    <td><p>2013-01</p></td>
    </tr>
    </tbody>
    </table>
12. <em> 如何将 Proxmox VE 升级到下一个小版本？ </em>

    小版本升级（例如从 Proxmox VE 8.1 升级到 8.2 或 8.3）可以像普通更新一样进行。但仍应查看[发行说明](https://pve.proxmox.com/wiki/Roadmap)，了解相关的重要变更或不兼容变更。

    <a id="faq-upgrade"></a>



    对于更新本身，可以使用 Web 界面的<em>节点 → 更新</em>面板，或在 CLI 中执行：

    ```text
    apt update
    apt full-upgrade
    ```

    {% hint style="info" %}
    始终确保正确设置了[软件包仓库](../03-system-administration/README.md#sysadmin_package_repositories)，并且仅在 `apt update` 未出现任何错误时，才继续实际升级。
    {% endhint %}
13. <em> 如何将 Proxmox VE 升级到下一个主版本？ </em>

    也支持主版本升级，例如从 Proxmox VE 8.4 升级到 9.0。必须仔细规划和测试，<strong>绝不能</strong>在尚未准备好最新备份时开始升级。

    <a id="faq-upgrade-major"></a>



    虽然具体升级步骤取决于您的实际配置，但我们提供了有关如何执行升级的通用说明和建议：

    - [从 Proxmox VE 8 升级到 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
    - [从 Proxmox VE 7 升级到 8](https://pve.proxmox.com/wiki/Upgrade_from_7_to_8)
    - [从 Proxmox VE 6 升级到 7](https://pve.proxmox.com/wiki/Upgrade_from_6.x_to_7.0)
    - [从 Proxmox VE 5 升级到 6](https://pve.proxmox.com/wiki/Upgrade_from_5.x_to_6.0)
    - [从 Proxmox VE 4 升级到 5](https://pve.proxmox.com/wiki/Upgrade_from_4.x_to_5.0)
    - [从 Proxmox VE 3 升级到 4](https://pve.proxmox.com/wiki/Upgrade_from_3.x_to_4.0)
14. <em> LXC、LXD、Proxmox 容器与 Docker 的比较 </em>

    LXC 是 Linux 内核容器功能的用户空间接口。通过强大的 API 和简单的工具，Linux 用户可以轻松创建和管理系统容器。LXC 与以前的 OpenVZ 一样，面向<strong>系统虚拟化</strong>。因此，可以在容器内运行完整的操作系统，通过 ssh 登录、添加用户、运行 apache 等……

    LXD 构建于 LXC 之上，提供全新且更好的用户体验。在底层，LXD 通过 `liblxc` 及其 Go 绑定使用 LXC 来创建和管理容器。它基本上是 LXC 工具和发行版模板系统的替代方案，并增加了可通过网络控制所带来的功能。

    Proxmox 容器是指使用 Proxmox 容器工具包（`pct`）创建和管理的容器。它们同样面向<strong>系统虚拟化</strong>，并以 LXC 作为容器功能的基础。随着 OCI 镜像支持的加入（技术预览），Proxmox VE 也可以从 OCI 镜像创建容器，既包括完整系统容器，也包括应用容器（技术预览）。Proxmox 容器工具包（`pct`）与 Proxmox VE 紧密结合。这意味着它了解集群配置，并可使用与 QEMU 虚拟机（VM）相同的网络和存储资源。您甚至可以使用 Proxmox VE 防火墙、创建和恢复备份，或使用 HA 框架管理容器。一切都可以通过网络使用 Proxmox VE API 进行控制。

    Docker 旨在于隔离、自包含的环境中运行<strong>单个</strong>应用程序。这类容器通常称为“应用容器”，而非“系统容器”。您通过 Docker Engine 命令行接口从宿主机管理 Docker 实例。不建议直接在 Proxmox VE 宿主机上运行 docker。

    {% hint style="info" %}
    虽然将“应用容器”直接作为 Proxmox 容器运行可能很方便，但目前仍属于技术预览。对于需要容器编排或在线迁移的使用场景，仍建议在 Proxmox QEMU 虚拟机内运行它们。
    {% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
