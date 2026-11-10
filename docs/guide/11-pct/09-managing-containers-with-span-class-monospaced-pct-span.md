# 11.9. Managing Containers with `pct` <a href="#_managing_containers_with_span_class_monospaced_pct_span" id="_managing_containers_with_span_class_monospaced_pct_span"></a>

“Proxmox Container Toolkit”（`pct`）是用于管理 Proxmox VE 容器的命令行工具。它可用于创建或销毁容器，以及控制容器的运行（启动、停止、重启、迁移等）。它还可用于设置容器配置文件中的参数，例如网络配置或内存限制。

## 11.9.1. CLI Usage Examples <a href="#_cli_usage_examples_2" id="_cli_usage_examples_2"></a>

基于 Debian 模板创建容器（前提是你已通过 Web 界面下载该模板）

```text
# pct create 100 /var/lib/vz/template/cache/debian-10.0-standard_10.0-1_amd64.tar.gz
```

启动容器 100

```text
# pct start 100
```

通过 getty 启动登录会话

```text
# pct console 100
```

进入 LXC 命名空间并以 root 用户身份运行 shell

```text
# pct enter 100
```

显示配置

```text
# pct config 100
```

在容器运行时添加名为 `eth0` 的网络接口，将其桥接到宿主机网桥 `vmbr0`，并设置地址和网关

```text
# pct set 100 -net0 name=eth0,bridge=vmbr0,ip=192.168.15.147/24,gw=192.168.15.1
```

将容器的内存减少到 512MB

```text
# pct set 100 -memory 512
```

销毁容器时，始终会将其从访问控制列表中移除，并始终会移除该容器的防火墙配置。如果还想将容器从复制任务、备份任务和 HA 资源配置中移除，则必须启用 *--purge*。

{% hint style="info" %}
启用 purge 还会从所有引用该 HA 资源的亲和性规则中移除该资源，并移除仅剩这一个资源的规则。
{% endhint %}

```text
# pct destroy 100 --purge
```

将挂载点卷移动到其他存储。

```text
# pct move-volume 100 mp0 other-storage
```

将卷重新分配给另一个 CT。这会从源 CT 中移除卷 `mp0`，并将其作为 `mp1` 附加到目标 CT。在后台，该卷会被重命名，使名称与新所有者匹配。

```text
#  pct move-volume 100 mp0 --target-vmid 200 --target-volume mp1
```

## 11.9.2. Obtaining Debugging Logs <a href="#_obtaining_debugging_logs" id="_obtaining_debugging_logs"></a>

如果 `pct start` 无法启动特定容器，可以通过传递 `--debug` 标志来收集调试输出（将 `CTID` 替换为容器的 CTID），这可能会有所帮助：

```text
# pct start CTID --debug
```

或者，你可以使用以下 `lxc-start` 命令，它会将调试日志保存到 `-o` 输出选项指定的文件中：

```text
# lxc-start -n CTID -F -l DEBUG -o /tmp/lxc-CTID.log
```

此命令会尝试以前台模式启动容器。要停止容器，请在另一个终端中运行 `pct shutdown CTID` 或 `pct stop CTID`。

收集到的调试日志将写入 `/tmp/lxc-CTID.log`。

{% hint style="info" %}
如果自上次使用 `pct start` 尝试启动以来，你更改了容器配置，则需要至少运行一次 `pct start`，以同时更新 `lxc-start` 使用的配置。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
