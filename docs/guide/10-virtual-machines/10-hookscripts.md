# 10.10. 钩子脚本 <a href="#hookscripts" id="hookscripts"></a>

可以通过配置属性 `hookscript` 为虚拟机添加钩子脚本。

```text
# qm set 100 --hookscript local:snippets/hookscript.pl
```

它将在客户机生命周期的各个阶段被调用。有关示例和文档，请参阅 `/usr/share/pve-docs/examples/guest-example-hookscript.pl` 下的示例脚本。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
