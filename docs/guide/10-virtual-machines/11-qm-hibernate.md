# 10.11. 休眠 <a href="#qm_hibernate" id="qm_hibernate"></a>

可以使用 GUI 选项 `Hibernate` 或通过以下命令将虚拟机休眠到磁盘：

```text
# qm suspend ID --todisk
```

这意味着当前内存内容将保存到磁盘，并且虚拟机会停止。下次启动时，将加载内存内容，虚拟机可以从中断处继续运行。

<a id="qm_vmstatestorage"></a>



**状态存储选择**

如果未指定内存的目标存储，将自动选择以下第一项：

1. 虚拟机配置中的存储 `vmstatestorage`。
2. 任意虚拟机磁盘的第一个共享存储。
3. 任意虚拟机磁盘的第一个非共享存储。
4. 作为回退的存储 `local`。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
