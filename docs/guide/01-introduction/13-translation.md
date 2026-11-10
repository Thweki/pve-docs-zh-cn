# 1.13. 翻译 Proxmox VE <a href="#translation" id="translation"></a>

Proxmox VE 用户界面默认使用英语。不过，得益于社区的贡献，也提供了其他语言的翻译。我们欢迎任何支持，包括添加新语言、翻译最新功能以及改进不完整或不一致的翻译。

我们使用 [gettext](https://www.gnu.org/software/gettext/) 管理翻译文件。[Poedit](https://poedit.net/) 等工具提供了用于编辑翻译文件的良好用户界面，但您可以使用任何自己熟悉的编辑器。翻译无需编程知识。

## 1.13.1. 使用 git 翻译 <a href="#i18n_with_git" id="i18n_with_git"></a>

语言文件以 [git 仓库](https://git.proxmox.com/?p=proxmox-i18n.git) 的形式提供。如果您熟悉 git，请按照我们的 [开发者文档](https://pve.proxmox.com/wiki/Developer_Documentation) 参与贡献。

您可以通过执行以下操作创建新翻译（将 \<LANG\> 替换为语言 ID）：

```text
# git clone git://git.proxmox.com/git/proxmox-i18n.git
# cd proxmox-i18n
# make init-<LANG>.po
```

或者，您可以使用所选的编辑器编辑现有翻译：

```text
# poedit <LANG>.po
```

## 1.13.2. 不使用 git 进行翻译 <a href="#i18n_without_git" id="i18n_without_git"></a>

即使您不熟悉 git，也可以帮助翻译 Proxmox VE。首先，您可以在[此处](https://git.proxmox.com/?p=proxmox-i18n.git;a=tree)下载语言文件。找到要改进的语言，然后右键单击该语言文件的“raw”链接，并选择*“将链接另存为…”*。对文件进行修改，然后将最终译文连同已签署的[贡献者许可协议](https://pve.proxmox.com/wiki/Developer_Documentation#Software_License_and_Copyright)直接发送至 office(at)proxmox.com。

## 1.13.3. 测试翻译 <a href="#_testing_the_translation" id="_testing_the_translation"></a>

要在 Proxmox VE 中使用该翻译，必须先将 `.po` 文件转换为 `.js` 文件。您可以通过调用以下脚本完成此操作，该脚本位于同一仓库中：

```text
# ./po2js.pl -t pve xx.po >pve-lang-xx.js
```

然后，可以将生成的文件 `pve-lang-xx.js` 复制到 Proxmox 服务器上的目录 `/usr/share/pve-i18n` 中进行测试。

或者，您可以在仓库根目录下运行以下命令来构建 deb 软件包：

```text
# make deb
```

{% hint style="warning" %}
要使这两种方法中的任意一种正常工作，您需要在系统上安装以下 perl 软件包。对于 Debian/Ubuntu：
{% endhint %}

```text
# apt-get install perl liblocale-po-perl libjson-perl
```

## 1.13.4. 发送翻译 <a href="#_sending_the_translation" id="_sending_the_translation"></a>

您可以将完成的翻译（`.po` 文件）连同已签署的贡献者许可协议发送至 Proxmox 团队，地址为 office(at)proxmox.com。或者，如果您有一定的开发经验，可以将其作为补丁发送至 Proxmox VE 开发邮件列表。请参阅[开发者文档](https://pve.proxmox.com/wiki/Developer_Documentation)。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
