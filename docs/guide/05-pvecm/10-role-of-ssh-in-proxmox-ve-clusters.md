# 5.10. Role of SSH in Proxmox VE Clusters <a href="#_role_of_ssh_in_proxmox_ve_clusters" id="_role_of_ssh_in_proxmox_ve_clusters"></a>

Proxmox VE utilizes SSH tunnels for various features.

- Proxying console/shell sessions (node and guests)

  When using the shell for node B while being connected to node A, connects to a terminal proxy on node A, which is in turn connected to the login shell on node B via a non-interactive SSH tunnel.
- VM and CT memory and local-storage migration in *secure* mode.

  During the migration, one or more SSH tunnel(s) are established between the source and target nodes, in order to exchange migration information and transfer memory and disk contents.
- Storage replication

## 5.10.1. SSH setup <a href="#_ssh_setup" id="_ssh_setup"></a>

On Proxmox VE systems, the following changes are made to the SSH configuration/setup:

- the `root` user’s SSH client config gets setup to prefer `AES` over `ChaCha20`
- the `root` user’s `authorized_keys` file gets linked to `/etc/pve/priv/authorized_keys`, merging all authorized keys within a cluster
- `sshd` is configured to allow logging in as root with a password

{% hint style="info" %}
Older systems might also have `/etc/ssh/ssh_known_hosts` set up as symlink pointing to `/etc/pve/priv/known_hosts`, containing a merged version of all node host keys. This system was replaced with explicit host key pinning in `pve-cluster <<INSERT VERSION>>`, the symlink can be deconfigured if still in place by running `pvecm updatecerts --unmerge-known-hosts`.
{% endhint %}

## 5.10.2. Pitfalls due to automatic execution of `.bashrc` and siblings <a href="#_pitfalls_due_to_automatic_execution_of_span_class_monospaced_bashrc_span_and_siblings" id="_pitfalls_due_to_automatic_execution_of_span_class_monospaced_bashrc_span_and_siblings"></a>

In case you have a custom `.bashrc`, or similar files that get executed on login by the configured shell, `ssh` will automatically run it once the session is established successfully. This can cause some unexpected behavior, as those commands may be executed with root permissions on any of the operations described above. This can cause possible problematic side-effects!

In order to avoid such complications, it’s recommended to add a check in `/root/.bashrc` to make sure the session is interactive, and only then run `.bashrc` commands.

You can add this snippet at the beginning of your `.bashrc` file:

```text
# Early exit if not running interactively to avoid side-effects!
case $- in
    *i*) ;;
      *) return;;
esac
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
