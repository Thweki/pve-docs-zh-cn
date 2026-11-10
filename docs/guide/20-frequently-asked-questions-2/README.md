# 20\. Frequently Asked Questions <a href="#_frequently_asked_questions_2" id="_frequently_asked_questions_2"></a>

{% hint style="info" %}
New FAQs are appended to the bottom of this section.
{% endhint %}

1. *What distribution is Proxmox VE based on?*

   Proxmox VE is based on [Debian GNU/Linux](https://www.debian.org)
2. *What license does the Proxmox VE project use?*

   Proxmox VE code is licensed under the GNU Affero General Public License, version 3\.
3. *Will Proxmox VE run on a 32bit processor?*

   Proxmox VE works only on 64-bit CPUs. The supported architectures are x86\_64 (AMD64 or Intel 64\) and aarch64 on the NVIDIA Grace Hopper and NVIDIA Vera platforms. There is no plan to support 32-bit hosts.

   {% hint style="info" %}
   VMs and Containers can be both 32-bit and 64-bit.
   {% endhint %}
4. *Does my CPU support virtualization?*

   To check if your CPU is virtualization compatible, check for the `vmx` or `svm` tag in this command output:

   ```text
   egrep '(vmx|svm)' /proc/cpuinfo
   ```

   {% hint style="info" %}
   This check applies to x86 hosts only. On the supported arm64 platforms, KVM hardware-assisted virtualization is available and reports no equivalent CPU flag.
   {% endhint %}
5. *Supported Intel CPUs*

   64-bit processors with [Intel Virtualization Technology (Intel VT-x)](https://en.wikipedia.org/wiki/Virtualization_Technology#Intel_virtualization_.28VT-x.29) support. ([List of processors with Intel VT and 64-bit](https://ark.intel.com/content/www/us/en/ark/search/featurefilter.html?productType=873&2_VTX=True&2_InstructionSet=64-bit))
6. *Supported AMD CPUs*

   64-bit processors with [AMD Virtualization Technology (AMD-V)](https://en.wikipedia.org/wiki/Virtualization_Technology#AMD_virtualization_.28AMD-V.29) support.
7. *Supported arm64 platforms*

   The NVIDIA Grace Hopper and NVIDIA Vera platforms. See [64-bit ARM (arm64) Support](../02-installation/01-system-requirements.md#install_arm64_support) for details.
8. *What is a container/virtual environment (VE)/virtual private server (VPS)?*

   In the context of containers, these terms all refer to the concept of operating-system-level virtualization. Operating-system-level virtualization is a method of virtualization, in which the kernel of an operating system allows for multiple isolated instances, that all share the kernel. When referring to LXC, we call such instances containers. Because containers use the host’s kernel rather than emulating a full operating system, they require less overhead, but are limited to Linux guests.
9. *What is a QEMU/KVM guest (or VM)?*

   A QEMU/KVM guest (or VM) is a guest system running virtualized under Proxmox VE using QEMU and the Linux KVM kernel module.
10. *What is QEMU?*

    QEMU is a generic and open source machine emulator and virtualizer. QEMU uses the Linux KVM kernel module to achieve near native performance by executing the guest code directly on the host CPU. It is not limited to Linux guests but allows arbitrary operating systems to run.
11. *How long will my Proxmox VE version be supported?*

    Proxmox VE versions are supported **at least as long** as the corresponding Debian version is supported by the Debian Security Team, i.e. approximately 3 years after its initial release, see [Debian lifespan](https://www.debian.org/security/faq#lifespan). Proxmox VE uses a rolling release model and using the latest stable version is always recommended.

    <table id="faq-support-table">





    <thead>
    <tr>
    <th>Proxmox VE Version</th>
    <th>Debian Version</th>
    <th>First Release</th>
    <th>Debian EOL</th>
    <th>Proxmox EOL</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Proxmox VE 9</p></td>
    <td><p>Debian 13 (Trixie)</p></td>
    <td><p>2025-08</p></td>
    <td><p>tba</p></td>
    <td><p>tba</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 8</p></td>
    <td><p>Debian 12 (Bookworm)</p></td>
    <td><p>2023-06</p></td>
    <td><p>2026-07</p></td>
    <td><p>2026-08</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 7</p></td>
    <td><p>Debian 11 (Bullseye)</p></td>
    <td><p>2021-07</p></td>
    <td><p>2024-07</p></td>
    <td><p>2024-07</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 6</p></td>
    <td><p>Debian 10 (Buster)</p></td>
    <td><p>2019-07</p></td>
    <td><p>2022-09</p></td>
    <td><p>2022-09</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 5</p></td>
    <td><p>Debian 9 (Stretch)</p></td>
    <td><p>2017-07</p></td>
    <td><p>2020-07</p></td>
    <td><p>2020-07</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 4</p></td>
    <td><p>Debian 8 (Jessie)</p></td>
    <td><p>2015-10</p></td>
    <td><p>2018-06</p></td>
    <td><p>2018-06</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 3</p></td>
    <td><p>Debian 7 (Wheezy)</p></td>
    <td><p>2013-05</p></td>
    <td><p>2016-04</p></td>
    <td><p>2017-02</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 2</p></td>
    <td><p>Debian 6 (Squeeze)</p></td>
    <td><p>2012-04</p></td>
    <td><p>2014-05</p></td>
    <td><p>2014-05</p></td>
    </tr>
    <tr>
    <td><p>Proxmox VE 1</p></td>
    <td><p>Debian 5 (Lenny)</p></td>
    <td><p>2008-10</p></td>
    <td><p>2012-03</p></td>
    <td><p>2013-01</p></td>
    </tr>
    </tbody>
    </table>
12. *How can I upgrade Proxmox VE to the next point release?*

    Minor version upgrades, for example upgrading from Proxmox VE in version 8.1 to 8.2 or 8.3, can be done just like any normal update. But you should still check the [release notes](https://pve.proxmox.com/wiki/Roadmap) for any relevant notable, or breaking change.

    <a id="faq-upgrade"></a>



    For the update itself use either the Web UI *Node → Updates* panel or through the CLI with:

    ```text
    apt update
    apt full-upgrade
    ```

    {% hint style="info" %}
    Always ensure you correctly setup the [package repositories](../03-system-administration/01-sysadmin-package-repositories.md#sysadmin_package_repositories) and only continue with the actual upgrade if `apt update` did not hit any error.
    {% endhint %}
13. *How can I upgrade Proxmox VE to the next major release?*

    Major version upgrades, for example going from Proxmox VE 8.4 to 9.0, are also supported. They must be carefully planned and tested and should **never** be started without having a current backup ready.

    <a id="faq-upgrade-major"></a>



    Although the specific upgrade steps depend on your respective setup, we provide general instructions and advice on how an upgrade should be performed:

    - [Upgrade from Proxmox VE 8 to 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
    - [Upgrade from Proxmox VE 7 to 8](https://pve.proxmox.com/wiki/Upgrade_from_7_to_8)
    - [Upgrade from Proxmox VE 6 to 7](https://pve.proxmox.com/wiki/Upgrade_from_6.x_to_7.0)
    - [Upgrade from Proxmox VE 5 to 6](https://pve.proxmox.com/wiki/Upgrade_from_5.x_to_6.0)
    - [Upgrade from Proxmox VE 4 to 5](https://pve.proxmox.com/wiki/Upgrade_from_4.x_to_5.0)
    - [Upgrade from Proxmox VE 3 to 4](https://pve.proxmox.com/wiki/Upgrade_from_3.x_to_4.0)
14. *LXC vs LXD vs Proxmox Containers vs Docker*

    LXC is a userspace interface for the Linux kernel containment features. Through a powerful API and simple tools, it lets Linux users easily create and manage system containers. LXC, as well as the former OpenVZ, aims at **system virtualization**. Thus, it allows you to run a complete OS inside a container, where you log in using ssh, add users, run apache, etc…

    LXD is built on top of LXC to provide a new, better user experience. Under the hood, LXD uses LXC through `liblxc` and its Go binding to create and manage the containers. It’s basically an alternative to LXC’s tools and distribution template system with the added features that come from being controllable over the network.

    Proxmox Containers are how we refer to containers that are created and managed using the Proxmox Container Toolkit (`pct`). They also target **system virtualization** and use LXC as the basis of the container offering. With the addition of OCI image support (technology preview), Proxmox VE can also create containers from OCI images, including full system containers but also application containers (tech preview). The Proxmox Container Toolkit (`pct`) is tightly coupled with Proxmox VE. This means that it is aware of cluster setups, and it can use the same network and storage resources as QEMU virtual machines (VMs). You can even use the Proxmox VE firewall, create and restore backups, or manage containers using the HA framework. Everything can be controlled over the network using the Proxmox VE API.

    Docker aims at running a **single** application in an isolated, self-contained environment. These are generally referred to as “Application Containers”, rather than “System Containers”. You manage a Docker instance from the host, using the Docker Engine command-line interface. It is not recommended to run docker directly on your Proxmox VE host.

    {% hint style="info" %}
    While it can be convenient to run “Application Containers” directly as Proxmox Containers, doing so is currently a tech preview. For use cases requiring container orchestration or live migration, it is still recommended to run them inside a Proxmox QEMU virtual machine.
    {% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
