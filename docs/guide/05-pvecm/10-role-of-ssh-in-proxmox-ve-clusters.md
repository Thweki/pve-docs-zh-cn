# 5.10. Role of SSH in Proxmox VE Clusters <a href="#_role_of_ssh_in_proxmox_ve_clusters" id="_role_of_ssh_in_proxmox_ve_clusters"></a>

Proxmox VE 将 SSH 隧道用于多种功能。

- 代理控制台/shell 会话（节点和客户机）

  在连接到节点 A 的情况下使用节点 B 的 shell 时，会连接到节点 A 上的终端代理，该代理再通过非交互式 SSH 隧道连接到节点 B 上的登录 shell。
- 在 *secure* 模式下迁移虚拟机和 CT 的内存及本地存储。

  迁移期间，会在源节点和目标节点之间建立一条或多条 SSH 隧道，用于交换迁移信息以及传输内存和磁盘内容。
- 存储复制

## 5.10.1. SSH setup <a href="#_ssh_setup" id="_ssh_setup"></a>

在 Proxmox VE 系统上，会对 SSH 配置/设置进行以下更改：

- the `root` user’s SSH client config gets setup to prefer `AES` over `ChaCha20`
- `root` 用户的 `authorized_keys` 文件会链接到 `/etc/pve/priv/authorized_keys`，从而合并集群内的所有授权密钥
- `sshd` is configured to allow logging in as root with a password

{% hint style="info" %}
较早的系统还可能将 `/etc/ssh/ssh_known_hosts` 设置为指向 `/etc/pve/priv/known_hosts` 的符号链接，其中包含所有节点主机密钥的合并版本。此机制已在 `pve-cluster <<INSERT VERSION>>` 中被显式主机密钥固定取代；如果该符号链接仍然存在，可以通过运行 `pvecm updatecerts --unmerge-known-hosts` 将其解除配置。
{% endhint %}

## 5.10.2. Pitfalls due to automatic execution of `.bashrc` and siblings <a href="#_pitfalls_due_to_automatic_execution_of_span_class_monospaced_bashrc_span_and_siblings" id="_pitfalls_due_to_automatic_execution_of_span_class_monospaced_bashrc_span_and_siblings"></a>

如果您有自定义的 `.bashrc`，或由所配置 shell 在登录时执行的其他类似文件，那么一旦会话成功建立，`ssh` 就会自动运行该文件。这可能会导致一些意外行为，因为在上述任何操作中，这些命令都可能以 root 权限执行。这可能产生有问题的副作用！

为避免此类问题，建议在 `/root/.bashrc` 中添加检查，以确保会话是交互式的，并且只有在此情况下才运行 `.bashrc` 命令。

您可以将以下代码片段添加到 `.bashrc` 文件的开头：

```text
# Early exit if not running interactively to avoid side-effects!
case $- in
    *i*) ;;
      *) return;;
esac
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
