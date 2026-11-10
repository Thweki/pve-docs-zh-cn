# 2.4. Unattended Installation <a href="#installation_unattended" id="installation_unattended"></a>

自动化安装方法允许以无人值守方式安装 Proxmox VE。这使您能够在裸机上完全自动化设置过程。安装完成且宿主机启动后，可以使用 Ansible 等自动化工具进一步配置安装。

必须在应答文件中提供安装程序所需的选项。此文件允许使用过滤规则来确定应使用哪些磁盘和网卡。

要使用自动化安装，首先选择获取应答文件的来源，然后根据该选择准备安装 ISO。

ISO 准备好后，其初始引导菜单将显示一个名为 *Automated Installation* 的新引导条目，该条目会在 10 秒超时后自动选中。

[访问 Wiki](https://pve.proxmox.com/wiki/Automated_Installation)，了解有关无人值守安装的更多详情和信息。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
