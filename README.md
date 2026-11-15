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

## 离线标题索引

无需重建全书，即可按 `docs/SUMMARY.md` 的顺序列出各页和章节标题，或查询 API、命令及中文章节标题：

```sh
.venv/bin/python scripts/report_doc_index.py > /tmp/pve-doc-index.json
.venv/bin/python scripts/report_doc_index.py --query 'GET /nodes'
.venv/bin/python scripts/report_doc_index.py --docs docs --query '备份'
```

命令只读取文档，将 JSON 输出到标准输出；仅需 `requirements.txt`，不需要 Pandoc、PDF 工具或原始快照。索引包含导航标题、相对文档路径、目录深度（顶层为 0）、标题级别及离线 HTML 链接。`href` 相对于导出的 `builds/html/` 目录，使用与导出器一致的锚点；对应 HTML 必须由同一份文档构建。输出不含时间戳或绝对路径，便于保存和比较。

`--query` 按标题文字进行不区分大小写的子串匹配，不搜索正文；页数和标题数仅统计匹配结果。无匹配时输出空索引并正常退出。索引仅覆盖导航中列出的页面，重复页面只收录一次；它不是完整性校验工具。导航文件缺失、页面不存在或路径越界时，命令报错并以非零状态退出，不输出部分 JSON。

## 离线交叉引用诊断

检查书内链接是否指向缺失页面、未收录页面、越界路径、不存在的锚点或多个同名目标，无需原始快照或重建全书：

```sh
.venv/bin/python scripts/report_doc_crossrefs.py > /tmp/pve-crossrefs.json
.venv/bin/python scripts/report_doc_crossrefs.py --docs docs --check
```

这是常规功能，无需实验开关；仅需 `requirements.txt`。命令只读取 `docs/SUMMARY.md` 收录的页面，按目录和页面内链接顺序向标准输出写入 JSON，不修改文档或现有报告。默认即使发现问题也退出 0；`--check` 在有问题时退出 1，仍输出完整 JSON。导航无效、文件不可读或解析失败时退出 2，不输出部分报告。

诊断使用离线 HTML/EPUB 导出器的锚点规则，支持自动标题别名、显式 ID、命名书签、中文及 URL 编码。多个目标共用一个别名时报告 `ambiguous_fragment`，即使导出器会选择第一个目标；同一标题重复声明同一个别名不算歧义。每条问题包含源页面、原始链接、链接文字、目标路径、片段和原因；`link_index` 为移除空标题书签后页面内所有 `a[href]` 的序号（从 1 开始，非源码行号）。歧义候选提供标题（非标题书签为 `null`）及相对于 `builds/html/` 的链接，便于定位同一份文档导出的具体目标。

报告含页数、检查链接数、无歧义解析数和按原因分类的问题数，不含运行时间或绝对解析路径；越界目标的 `target` 为 `null`。它只检查页面正文中的本地 Markdown 页面链接和页内跳转，不检查外部网址、资源、代码示例、导航条目中的片段或未收录页面的正文；空标题书签自链接随导出器移除。它不枚举孤立页面、不修改链接，也不替代 GitBook 或完整发布校验。

## GitBook 与翻译更新

`.gitbook.yaml` 指向 `docs/`；`gitbook-docs.yaml` 定义站点与稳定空间键；`docs/SUMMARY.md` 是导航来源。首次 Git Sync 方向选择 **GitHub → GitBook**。

日常勘误可修改公开译文映射并重建。更新上游快照时，可重新运行 `scripts/prepare.py` 提取变化单元，再运行 `scripts/translate.py` 使用已登录的 Kimi Code 辅助翻译，或由贡献者直接补齐映射。发布构建默认拒绝缺失或不符合校验要求的译文。

## 许可证与贡献

文档及译文采用 **GFDL-1.3-no-invariants-or-later**；本项目构建脚本/CSS/JavaScript 采用 **AGPL-3.0-or-later**；开放字体采用 **SIL OFL 1.1**。上游其他程序保留原有许可，完整来源和条款见 [NOTICE.md](NOTICE.md)、`LICENSE` 与 `LICENSES/`。

欢迎通过 Issue 或 Pull Request 提交勘误、术语改进和构建修复。
