# 11\. Proxmox Container Toolkit <a href="#chapter_pct" id="chapter_pct"></a>

容器是完全虚拟机（VM）的轻量级替代方案。它们使用所运行宿主机系统的内核，而不是模拟完整的操作系统（OS）。这意味着容器可以直接访问宿主机系统上的资源。

容器的运行时开销很低，通常可以忽略不计。但是，有一些缺点需要考虑：

- Proxmox 容器中只能运行 Linux 发行版。无法在容器内运行其他操作系统，例如 FreeBSD 或 Microsoft Windows。
- 出于安全原因，需要限制对宿主机资源的访问。因此，容器在各自独立的命名空间中运行。此外，容器内不允许使用某些系统调用（用户空间对 Linux 内核的请求）。

Proxmox VE 使用 [Linux Containers (LXC)](https://linuxcontainers.org/lxc/introduction/) 作为其底层容器技术。“Proxmox Container Toolkit”（`pct`）通过提供抽象复杂任务的接口，简化了 LXC 的使用和管理。

容器与 Proxmox VE 紧密集成。这意味着它们可以感知集群配置，并且可以使用与虚拟机相同的网络和存储资源。您还可以使用 Proxmox VE 防火墙，或通过 HA 框架管理容器。

我们的主要目标传统上一直是提供一种既能获得使用 VM 的好处、又没有额外开销的环境。这意味着 Proxmox 容器主要被归类为“系统容器”。

随着对 OCI（**O**pen **C**ontainer **I**nitiative）镜像支持的引入，Proxmox VE 现在还将“应用容器”作为技术预览集成进来。从 OCI 镜像创建容器时，该镜像会自动转换为 Proxmox VE 使用的 LXC 技术栈。

这种方法使用户既能受益于广泛的预打包应用生态系统，又能保留 Proxmox VE 强大的管理功能。

尽管直接运行轻量级“应用容器”相比完整 VM 具有显著优势，但对于要求最大隔离性和在线迁移能力的用例，将容器嵌套在 Proxmox QEMU VM 内仍是推荐做法。

## 本章内容

- [11.1. Technology Overview](01-technology-overview.md)
- [11.2. Supported Distributions](02-pct-supported-distributions.md)
- [11.3. Container Images](03-pct-container-images.md)
- [11.4. Container Settings](04-pct-settings.md)
- [11.5. Security Considerations](05-security-considerations.md)
- [11.6. Guest Operating System Configuration](06-guest-operating-system-configuration.md)
- [11.7. Container Storage](07-pct-container-storage.md)
- [11.8. Backup and Restore](08-backup-and-restore.md)
- [11.9. Managing Containers with pct](09-managing-containers-with-span-class-monospaced-pct-span.md)
- [11.10. Migration](10-pct-migration.md)
- [11.11. Configuration](11-pct-configuration.md)
- [11.12. Locks](12-locks-2.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
