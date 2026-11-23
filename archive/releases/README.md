# Proxmox VE 中文文档下载

这里保留 **Proxmox VE 9.2.13 非官方简体中文文档**原独立下载仓库的维护工具和发布说明。[完整 Git 历史](https://github.com/Thweki/pve-docs-zh-cn/raw/refs/heads/main/archive/releases/pve-docs-zh-cn-releases.bundle)包含原仓库的 10 个分支和原始标签，可通过 `git clone pve-docs-zh-cn-releases.bundle` 恢复。

## 下载版本

请从 [Releases](https://github.com/Thweki/pve-docs-zh-cn/releases) 下载已发布的文件。当前发行标签为 **`v9.2.13-zh.2`**，对应上游文档版本 **9.2.13**。

| 文件格式 | 内容与用途 |
| --- | --- |
| EPUB | 完整电子书，适合电子书阅读器和移动设备。 |
| PDF | 完整分页版本，适合检索、打印及归档。 |
| 离线 HTML ZIP | 解压后在浏览器中离线阅读完整文档。 |
| Source ZIP | 完整可编辑源码、原始输入快照、有效译文映射、构建脚本及开放字体。 |
| SHA256 校验文件 | 校验每份下载文件的完整性。 |

在线阅读：[GitBook 完整中文文档](https://thweki.gitbook.io/pve-docs-zh-cn/)。

### 发行附件预检（维护者）

附件预检和 SHA-256 校验统一使用 [主仓库发布校验工具](https://github.com/Thweki/pve-docs-zh-cn/blob/main/scripts/README.release-tools.md)。

### 本地发行归档清单

需要长期保存一份发行下载目录时，可生成包含所有本地文件的清单，并在复制或恢复归档后核对目录是否完整。先将要归档的附件、`SHA256SUMS` 及可选签名等放入专用目录，再运行（Python 3.9 或更新版本，无需安装依赖或启用开关）：

```sh
python3 scripts/release_manifest.py create /path/to/release --tag v9.2.13-zh.2
# 将整个目录（包括新生成的 RELEASE-MANIFEST.json）一起归档或复制
python3 scripts/release_manifest.py verify /path/to/restored-release --tag v9.2.13-zh.2
```

`create` 在目录根部新建 `RELEASE-MANIFEST.json`，记录 `schema_version: 1`、`release_tag` 和按相对路径排序的 `files` 列表；每个文件条目包含 `path`、字节数 `bytes` 和小写 `sha256`。路径使用 `/` 分隔，覆盖子目录、隐藏文件、空文件及额外附件，仅排除根部清单自身。不记录时间戳或绝对路径，相同标签和文件内容生成相同清单；大文件分块读取。已有清单不会被覆盖；确需重新建立基准时，请先将旧清单移出归档目录。

`verify` 要求标签（包括中文修订号）一致，并检查完整文件集合、大小及哈希。缺少文件、多出文件、内容改变或清单格式错误均返回状态码 `1` 并说明原因；成功返回 `0`，命令参数错误返回 `2`。符号链接及其他特殊文件会被拒绝；空目录、权限和文件时间不属于清单内容。创建和核对期间请勿修改目录。

这是本地归档基准，不判断是否下载齐了发行必需附件，不解析或替代发行提供的 `SHA256SUMS`，也不证明来源真实性；请先完成下载校验，再保存清单。命令完全离线，不下载、解压或上传任何文件。运行专项测试：`python3 -B -m unittest discover -s tests -p 'test_release_manifest.py' -v`。

## 内容范围

- 完整管理手册及附录，按原始 **29 个章节**组织；每章及其全部子节在同一页完整呈现。
- **29 份**命令、服务和配置参考手册，每篇同页。
- 完整 **680 个 API 操作**及请求参数、返回结构、权限说明，按资源组同页组织。
- 保留原始图片、技术图、命令、配置、代码示例、表格、提示框、脚注与交叉引用。

这是由 AI 辅助完成的非官方译文，未经 Proxmox 官方审核。截图保持原图，图中英文界面文字不重绘。遇到译文歧义，请对照 [Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/)。

## 来源与许可证

原始文档 Copyright (C) 2015–2026 Proxmox Server Solutions GmbH。文档及中文译文依据 **GNU Free Documentation License 1.3 或更新版本**分发，无不变章节、无封面文字、无封底文字，完整条款见 [LICENSE](LICENSE)。

API JavaScript 程序及构建程序的 AGPL、原始 AsciiDoc 脚本的 GPL、开放字体的 SIL OFL 许可分别保留；详情及对应源地址见 [NOTICE.md](NOTICE.md)、[LICENSES](LICENSES) 和 [字体许可及来源](export-assets/fonts)。本仓库保留声明和许可文件，字体程序、完整文档及可重建输入随正式下载归档提供。

技术问题及翻译更正请提交到 [源码仓库 Issues](https://github.com/Thweki/pve-docs-zh-cn/issues)。

## 元数据校验

使用 Python 3.9 或更新版本，无需安装依赖：

```sh
python3 scripts/validate_metadata.py
python3 -m unittest discover -s tests -v
```

校验字体来源清单的字段、固定提交与 SHA256 格式，两份本地 OFL 文件的字节数和哈希，README/NOTICE 的发行及上游版本，以及两份文档中行内 Markdown 链接的本地文件或目录目标（不检查锚点）。在归档目录运行这些离线检查即可，无需下载字体或安装依赖。

四份字体二进制文件仅随发行归档提供，本校验不要求它们存在，也不核对其实际哈希。不检查远程链接、发行资产、源码归档内容或译文数量。根目录 GFDL 文本的完整性校验留待独立许可证修复后添加；本校验不修改或固定该文本。

## 本地发行目录树

下载附件或解压离线 HTML、源码归档后，可只读查看目录层级、每个普通文件的字节数及总大小。使用 Python 3.9 或更新版本，无需依赖或启用实验选项：

```sh
python3 scripts/release_tree.py /path/to/downloads
# 可选：按块读取文件，同时显示每个普通文件的 SHA256
python3 scripts/release_tree.py /path/to/extracted-html --sha256
```

输出示例（文件大小仅作演示）：

```text
'/path/to/downloads'/
|-- 'Proxmox-VE-9.2.13-zh-CN.pdf' [1024 bytes]
`-- 'html'/
    `-- 'index.html' [512 bytes]

2 files, 1 directories, 0 symlinks, 0 special entries; 1536 bytes
```

所有条目（含隐藏文件）按名称排序，文件名中的控制字符会转义。汇总不含根目录；大小为普通文件的逻辑字节数之和，不是磁盘占用量，硬链接的每个路径分别计数。默认只读取元数据，`--sha256` 才读取文件内容；不联网、不解压、不创建清单、不修改目录内容。

符号链接和特殊文件只标注、不跟随或读取，根路径必须为实际目录。读取失败会标记 `ERROR`、继续列出其他条目，并将汇总标为 `incomplete`；退出码为 0 表示完成，1 表示失败或结果不完整，2 表示参数错误。请在下载或解压完成、目录不再变化时运行；结果不是原子快照。显示的哈希仅供查看，不会与 `SHA256SUMS` 比较，也不检查发行附件是否齐全。测试已包含在 `python3 -B -m unittest discover -s tests -v` 中。

## 生成发行说明

将本次实际改动写入一个 UTF-8 Markdown 文件（例如 `changes.md`），再运行：

```sh
python3 scripts/generate_release_notes.py changes.md
```

此只读工具离线输出可供审阅的中文发行说明，包含改动摘要、README 的“下载版本”和“内容范围”章节，以及对应发行标签的来源与许可证链接。它复用元数据校验器检查 README/NOTICE 的版本一致性；摘要为空、所需章节缺失或版本冲突时返回非零状态，不输出部分说明。默认读取脚本所在仓库，也可用 `--root PATH` 指定其他检出目录。

确认输出后可用 `> release-notes.md` 保存，再手动用于 GitHub Release；输入摘要和输出文件须使用不同路径。工具不推断历史改动、不检查附件或远程链接，也不创建标签或发布发行。发布前请确认标签指向包含相应声明文件的提交，并审阅摘要及下载说明。仅需 Python 3.9 或更新版本，测试已纳入上述 unittest 命令。
