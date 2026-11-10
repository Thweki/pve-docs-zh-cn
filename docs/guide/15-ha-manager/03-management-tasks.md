# 15.3. 管理任务 <a href="#management_tasks" id="management_tasks"></a>

本节简要介绍常见的管理任务。第一步是为资源启用 HA。这通过将资源添加到 HA 资源配置中来完成。您可以使用 GUI 执行此操作，也可以直接使用命令行工具，例如：

```text
# ha-manager add vm:100
```

HA 软件栈现在会尝试启动资源并使其保持运行。请注意，您可以配置资源的“请求”状态。例如，您可能希望 HA 软件栈停止资源：

```text
# ha-manager set vm:100 --state stopped
```

并在稍后再次启动它：

```text
# ha-manager set vm:100 --state started
```

您还可以使用常规的 VM 和容器管理命令。它们会自动将命令转发给 HA 软件栈，因此

```text
# qm start 100
```

只是将请求的状态设置为`started`。`qm
stop`也是如此，它会将请求的状态设置为`stopped`。

{% hint style="info" %}
HA 软件栈以完全异步的方式工作，并且需要与其他集群成员通信。因此，您需要等待几秒钟才能看到此类操作的结果。
{% endhint %}

要查看当前 HA 资源配置，请使用：

```text
# ha-manager config
vm:100
        state stopped
```

您还可以使用以下命令查看 HA 管理器和资源的实际状态：

```text
# ha-manager status
quorum OK
master node1 (active, Wed Nov 23 11:07:23 2016)
lrm elsa (active, Wed Nov 23 11:07:19 2016)
service vm:100 (node1, started)
```

您还可以发起将资源迁移到其他节点的操作：

```text
# ha-manager migrate vm:100 node2
```

这使用在线迁移，并尝试让 VM 保持运行。在线迁移需要通过网络传输所有已使用的内存，因此有时先停止 VM，然后在新节点上重新启动它会更快。这可以使用`relocate`命令完成：

```text
# ha-manager relocate vm:100 node2
```

最后，您可以使用以下命令将资源从 HA 配置中移除：

```text
# ha-manager remove vm:100
```

默认情况下，这还会从引用该资源的任何规则中移除该资源，并删除仅引用此资源的规则。您可以使用*--purge 0*覆盖此行为。

{% hint style="info" %}
这不会启动或停止资源。
{% endhint %}

但所有与 HA 相关的任务都可以在 GUI 中完成，因此完全不需要使用命令行。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
