# Proxmox VE 中文文档

Proxmox VE **9.2.13** 官方文档的非官方简体中文译本。原文日期为 2026 年 9 月 24 日，源快照获取于 2026 年 11 月 10 日。

- **管理手册 29 章**：每章与全部子节同页，章内跳转。
- **命令、服务与配置参考 29 篇**：每篇完整同页。
- **680 个 API 操作**：按 6 个资源组整组同页，保留参数、约束、权限和返回结构。
- 原始图片、代码、表格、提示框、注释与引用关系均有完整性校验。

[GitBook 在线阅读](https://thweki.gitbook.io/pve-docs-zh-cn/) · [公开版本下载](https://github.com/Thweki/pve-docs-zh-cn-releases/releases)提供 EPUB、完整 PDF、单页离线 HTML 与可重建源码。HTML、EPUB 中每章的子节也连续显示。译文由 AI 辅助完成，未经 Proxmox 官方审核；截图及命令示例保持原值。

## 从公开源码离线重建

需要 Python 3.12 或更新版本。原始输入、固定译文映射、开放字体和构建脚本均随源码提供。

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
mkdir -p work
.venv/bin/python scripts/package_source.py --restore-snapshot
.venv/bin/python scripts/render.py
.venv/bin/python scripts/verify.py
```

`translations/units.json` 保存原文和受保护标记，`translations/zh-CN.json` 保存 11,508 条有效译文。构建直接使用这些映射。`source/upstream-snapshot.tar.gz` 保存原始 HTML/API 与可重新生成的定位缓存，附逐文件校验清单。已验证断网、无工作缓存条件下可逐字节重建 `docs/`。

## 导出 EPUB、PDF 和 HTML

macOS 系统依赖：

```sh
brew install pandoc pango poppler
.venv/bin/pip install -r requirements-export.txt
touch work/CHAPTER_LAYOUT_READY
.venv/bin/python scripts/export_web_epub.py
.venv/bin/python scripts/package_html.py
.venv/bin/python scripts/export_pdf.py --qa
.venv/bin/python scripts/package_source.py
```

其他系统安装相应的 Pandoc、Pango、Poppler，参见 [Pandoc](https://pandoc.org/installing.html) 和 [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) 官方安装说明。

- `builds/html/index.html`：带目录、搜索和代码复制的单页离线全书，资源全部本地化。
- `builds/Proxmox-VE-9.2.13-zh-CN.epub`：EPUB 3，每章内子节保持在同一文档项。
- `output/pdf/Proxmox-VE-9.2.13-zh-CN.pdf`：完整 PDF，含书签、目录与页码。
- `builds/Proxmox-VE-9.2.13-zh-CN-source.zip`：含原始快照与译文映射的源码归档。

`reports/` 与导出报告记录文字、代码、图片、字体、链接、分页及复建检查。PDF 的超高表格采用保留完整字段内容的可分页排版。

## GitBook 与翻译更新

`.gitbook.yaml` 指向 `docs/`；`gitbook-docs.yaml` 定义站点与稳定空间键；`docs/SUMMARY.md` 是导航来源。首次 Git Sync 方向选择 **GitHub → GitBook**。

日常勘误可修改公开译文映射并重建。更新上游快照时，可重新运行 `scripts/prepare.py` 提取变化单元，再运行 `scripts/translate.py` 使用已登录的 Kimi Code 辅助翻译，或由贡献者直接补齐映射。发布构建默认拒绝缺失或不符合校验要求的译文。

## 许可证与贡献

文档及译文采用 **GFDL-1.3-no-invariants-or-later**；本项目构建脚本/CSS/JavaScript 采用 **AGPL-3.0-or-later**；开放字体采用 **SIL OFL 1.1**。上游其他程序保留原有许可，完整来源和条款见 [NOTICE.md](NOTICE.md)、`LICENSE` 与 `LICENSES/`。

欢迎通过 Issue 或 Pull Request 提交勘误、术语改进和构建修复。
