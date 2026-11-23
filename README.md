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

## GitBook 与翻译更新

`.gitbook.yaml` 指向 `docs/`；`gitbook-docs.yaml` 定义站点与稳定空间键；`docs/SUMMARY.md` 是导航来源。首次 Git Sync 方向选择 **GitHub → GitBook**。

日常勘误可修改公开译文映射并重建。更新上游快照时，可重新运行 `scripts/prepare.py` 提取变化单元，再运行 `scripts/translate.py` 使用已登录的 Kimi Code 辅助翻译，或由贡献者直接补齐映射。发布构建默认拒绝缺失或不符合校验要求的译文。

### 导航孤立页面报告

维护目录时，可离线检查哪些 Markdown 页面未列入 `SUMMARY.md`，并追踪它们能否通过正文链接到达：

```sh
.venv/bin/python scripts/report_doc_orphans.py
.venv/bin/python scripts/report_doc_orphans.py --docs docs > /tmp/pve-doc-orphans.json
.venv/bin/python scripts/report_doc_orphans.py --check
```

命令仅需 `requirements.txt`，只读取文档、向标准输出打印 JSON，无需原始快照、重建或导出工具。`counts` 区分直接列入目录（`listed`）、仅经正文链接可达（`indirect`）和完全不可达（`unreachable`）的页面；后两类分别列在 `indirect_pages`、`unreachable_pages` 中，包含相对路径、首个 H1 标题（无 H1 时使用路径）和去重后的入链页面 `referenced_by`。间接可达页面还提供从 `SUMMARY.md` 开始的最短路径 `via`；孤立页面之间的循环引用不会被误认为可达。入链仅说明引用关系，不代表来源页面可达。

默认报告不因发现遗漏而失败。加上 `--check` 后，只要任一页面未直接列入目录就退出 1，仍输出完整报告：正文可达页面也可能被按 SUMMARY 选页的导出流程遗漏。全部收录时退出 0；缺少根目录的 `SUMMARY.md`、读取或解析失败、文档目录含符号链接目录或 Markdown 符号链接时退出 2，不输出部分 JSON。不自动修复目录，也不更改发布校验。

报告以根目录 `SUMMARY.md` 中的真实链接为起点，扫描目录内全部 `.md` 页面，支持 Markdown 引用式链接、HTML 链接及 URL 编码的相对路径。注释、代码示例、图片、有效 YAML 前置元数据中的链接不计入导航；外部链接、绝对路径、目录简写、缺失目标和目录外目标不构成边。查询参数和锚点不影响页面可达性；本报告不校验锚点或推断 GitBook 自动生成的章节导航。输出按相对路径排序、无时间戳或绝对路径，可直接保存比较。

## 许可证与贡献

文档及译文采用 **GFDL-1.3-no-invariants-or-later**；本项目构建脚本/CSS/JavaScript 采用 **AGPL-3.0-or-later**；开放字体采用 **SIL OFL 1.1**。上游其他程序保留原有许可，完整来源和条款见 [NOTICE.md](NOTICE.md)、`LICENSE` 与 `LICENSES/`。

欢迎通过 Issue 或 Pull Request 提交勘误、术语改进和构建修复。
