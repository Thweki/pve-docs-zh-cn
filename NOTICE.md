# 来源、版权与许可证声明

本项目是 Proxmox VE **9.2.13** 文档的非官方简体中文译本，发布版本为 **9.2.13-zh.1**。翻译、章节组织及 EPUB、PDF、离线 HTML 导出由本项目制作，未经 Proxmox 官方审核。产品名称、商标及上游作者署名归各权利人所有。

## 文档与原始图片

原始文档、图片和文档内代码示例来自 [Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/)，原始文档 Copyright (C) 2015–2026 Proxmox Server Solutions GmbH。各参考手册中的其他原始版权声明继续有效，原图、程序示例及其作者署名予以保留。

依据上游的 [pve-docs 版权声明](https://github.com/proxmox/pve-docs/blob/master/debian/copyright)，文档适用 **GNU Free Documentation License 1.3 或更新版本**，无不变章节、无封面文字、无封底文字。中文译文及文档排版修改按同一文档许可证提供。完整英文许可见根目录 `LICENSE` 及书内许可证附录。文档的可编辑 Markdown、原始输入、译文映射和构建脚本随公开源码提供。

上游文档源代码：[官方 Git](https://git.proxmox.com/?p=pve-docs.git)、[Proxmox 官方只读镜像](https://github.com/proxmox/pve-docs)。来源版本、输入及图片的校验记录见 `source/manifest.json`、`source/assets-manifest.json` 和源归档内的清单。

## API JavaScript 程序

`source/upstream-snapshot.tar.gz` 中的 `source/api/apidoc.js` 是从 [官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/apidoc.js) 保存的未压缩 JavaScript 输入，其原始程序内容未被中文译文替换。`source/api/schema.json` 及带有翻译定位标记的 `source/prepared/` 是可重新生成的处理缓存，不是额外的在线服务数据。

API 程序 Copyright (C) 2015–2026 Proxmox Server Solutions GmbH；其中 Proxmox Widget Toolkit 的原始版权范围和其他上游声明亦继续适用。依据 [pve-docs 的程序许可](https://github.com/proxmox/pve-docs/blob/master/debian/copyright) 与 [Proxmox Widget Toolkit 版权声明](https://github.com/proxmox/proxmox-widget-toolkit/blob/master/debian/copyright)，这些程序适用 **GNU Affero General Public License 第 3 版或更新版本（AGPL-3.0-or-later）**。完整英文条款从 [GNU 官方地址](https://www.gnu.org/licenses/agpl-3.0.txt) 下载，随包保存在 `LICENSES/AGPL-3.0.txt`。上游程序不附带任何担保，包括适销性及特定用途适用性的默示担保。

对应源代码和构建方法：

- [pve-docs 官方仓库](https://git.proxmox.com/?p=pve-docs.git)；[官方镜像](https://github.com/proxmox/pve-docs)。`Makefile` 的 `API_VIEWER_FILES` 与 `api-viewer/apidoc.js` 构建规则说明了聚合过程。
- [PVEAPI.js](https://github.com/proxmox/pve-docs/blob/master/api-viewer/PVEAPI.js) 和 [API 数据提取器](https://github.com/proxmox/pve-docs/blob/master/scripts/extractapi.pl)。
- [Proxmox Widget Toolkit 官方仓库](https://git.proxmox.com/?p=proxmox-widget-toolkit.git)；[APIViewer.js 官方镜像](https://github.com/proxmox/proxmox-widget-toolkit/blob/master/src/api-viewer/APIViewer.js)。
- API 模式由 Proxmox VE 各组件的 API 实现提取；这些组件的完整对应源代码可从 [Proxmox 官方源代码仓库](https://git.proxmox.com/) 获取，包括 pve-manager、qemu-server、pve-container、pve-cluster、pve-storage、pve-access-control、pve-firewall、pve-ha-manager 和 pve-network。

原始 HTML 还包含 AsciiDoc 目录/脚注脚本，保留了 Mihai Bazon、Troy D. Hanson、Stuart Rackham 的原始作者及 GNU GPL 许可注释；这些注释不因文档转换而被删除。与原始页面生成器版本一致的对应源代码见 [AsciiDoc.py 10.2.1 的 asciidoc.js](https://github.com/asciidoc-py/asciidoc-py/blob/10.2.1/asciidoc/resources/javascripts/asciidoc.js)，完整生成器源见 [AsciiDoc.py 10.2.1](https://github.com/asciidoc-py/asciidoc-py/tree/10.2.1)。原脚本注释只标明 GNU GPL，未在该注释内指定版本；本包同时附上从 GNU 官方下载的 [GPL 第 2 版完整英文原文](LICENSES/GPL-2.0.txt)及 [GPL 第 3 版完整英文原文](LICENSES/GPL-3.0.txt)，分别来自 [GNU GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)和 [GNU GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.txt)。本项目没有将这些单独的软件程序改为 GFDL 许可。

## 开放字体

离线阅读和 PDF/EPUB 导出使用未修改的 Noto Sans CJK SC Regular、Noto Sans CJK SC Bold、Noto Sans Mono CJK SC Regular，以及用于符号显示的 Noto Emoji 可变字体（`NotoEmoji-wght.ttf`）。这些字体适用 **SIL Open Font License 1.1**，不是 GFDL 或 AGPL。

前三份 CJK 字体的完整许可见 `export-assets/fonts/OFL.txt`，上游为 [Noto CJK](https://github.com/notofonts/noto-cjk)，本次来源提交为 `f8d157532fbfaeda587e826d4cd5b21a49186f7c`。Noto Emoji 的完整许可和原始版权声明（Copyright 2013 Google LLC）见 `export-assets/fonts/OFL-NotoEmoji.txt`，来源为 [Google Fonts 的 Noto Emoji](https://github.com/google/fonts/tree/5bb28733cec313b63fbd415b574b5ae35c8aa8b8/ofl/notoemoji)，固定提交为 `5bb28733cec313b63fbd415b574b5ae35c8aa8b8`。

全部字体和许可文件的下载地址、固定上游提交及逐文件 SHA256 见 `export-assets/fonts/FONT-SOURCES.json`。字体内嵌的版权与命名信息保持不变。源码打包会动态核对该清单中的每个文件。

## 本项目构建程序与可重建输入

本项目新增的 `scripts/` Python 构建程序以及 `export-assets/` 中由本项目制作的 CSS/JavaScript，Copyright (C) 2026 本项目贡献者，按 **AGPL-3.0-or-later** 提供；字体、上游程序和文档仍分别适用其原有许可证。修改和再分发时请保留来源、版权、许可声明及对应源代码。

源码 ZIP 包含 `translations/units.json` 和 `translations/zh-CN.json` 的完整有效译文映射，以及公共源快照 `source/upstream-snapshot.tar.gz`。快照仅含 `source/html/`、`source/api/`、`source/prepared/`、`source/raw-assets/` 和其 SHA256 清单。它不包含浏览器登录、OAuth 回调、Kimi/Codex 会话或用量日志，也不包含本机虚拟环境。

解压源码 ZIP 后，可先运行 `python3 scripts/package_source.py --restore-snapshot` 恢复公共输入。安装 `requirements.txt` 及相应导出依赖后，可使用随包脚本和固定译文重新生成中文版，无需再次调用翻译服务。构建命令与各格式依赖见 `README.md` 及导出脚本说明。
