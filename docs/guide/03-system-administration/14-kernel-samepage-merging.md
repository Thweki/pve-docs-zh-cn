# 3.14. 内核同页合并（KSM） <a href="#kernel_samepage_merging" id="kernel_samepage_merging"></a>

内核同页合并（KSM）是 Linux 内核提供的一项可选内存去重功能，在 Proxmox VE 中默认启用。KSM 通过扫描一定范围的物理内存页以查找相同内容，并识别映射到这些物理页的虚拟页来工作。如果发现相同的页，则会重新映射相应的虚拟页，使它们全部指向同一个物理页，并释放旧页。虚拟页会被标记为“写时复制”，因此对它们的任何写入都会写入新的内存区域，同时保持共享物理页不变。

## 3.14.1. KSM 的影响 <a href="#implications_of_ksm" id="implications_of_ksm"></a>

KSM 可以优化虚拟化环境中的内存使用，因为运行相似操作系统或工作负载的多个 VM 可能会共享大量相同的内存页。

然而，虽然 KSM 可以减少内存使用，但它也会带来一些安全风险，因为它可能使 VM 面临侧信道攻击。研究表明，通过利用 KSM 的某些特性，可以借助同一宿主机上的第二个 VM 推断有关正在运行的 VM 的信息。

因此，如果您使用 Proxmox VE 提供托管服务，则应考虑禁用 KSM，以便为用户提供额外的安全保障。此外，您还应查看所在国家/地区的法规，因为禁用 KSM 可能是法律要求。

## 3.14.2. 禁用 KSM <a href="#disabling_ksm" id="disabling_ksm"></a>

可以在节点上或按 VM 分别禁用 KSM。

**在节点上禁用 KSM**

要查看节点上是否已激活 KSM，可以检查以下命令的输出：

```text
# systemctl status ksmtuned
```

如果已激活，可以使用以下命令立即禁用它：

```text
# systemctl disable --now ksmtuned
```

最后，要取消合并当前所有已合并的页，请运行：

```text
# echo 2 > /sys/kernel/mm/ksm/run
```

**为特定 VM 禁用 KSM**

`allow-ksm` VM 配置选项控制是否允许对指定 VM 进行内存页合并。该选项默认为 true，可以使用以下命令禁用：

```text
# qm set <vmid> --allow-ksm 0
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
