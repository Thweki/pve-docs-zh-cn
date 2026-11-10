# 15.1. 要求 <a href="#requirements_2" id="requirements_2"></a>

在开始使用 HA 之前，您必须满足以下要求：

- 至少三个集群节点（以获得可靠的仲裁）
- VM 和容器的共享存储
- 硬件冗余（所有环节）
- 使用可靠的“服务器”组件

可选地，可以使用硬件看门狗——如果不可用，我们将回退到 Linux 内核软件看门狗（`softdog`）。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
