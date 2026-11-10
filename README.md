# Proxmox VE 中文文档

基于 <https://pve.proxmox.com/pve-docs/> 的非官方简体中文译本，目标版本为 **9.2.13**。GitBook 内容位于 `docs/`，保留原始图片、代码、表格、提示框和章节引用关系。

## 内容范围

- 完整管理手册及附录。
- 官方入口列出的 29 份命令、服务和配置参考手册。
- API 浏览器中的 680 个接口操作及参数、返回结构和权限信息。
- 术语、来源、版本快照、资源校验记录与原始许可证。

翻译由 AI 辅助完成，未经 Proxmox 官方审核。截图保持原图，图中英文界面文字不重绘。GitBook 使用其原生页面样式。

## 构建与更新

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
# 初次使用，保存官方索引、完整管理手册和 API JS 到 source/ 对应目录。
mkdir -p source/html source/api source/prepared source/raw-assets work docs/assets reports
curl -fsSL https://pve.proxmox.com/pve-docs/ -o source/html/index.html
curl -fsSL https://pve.proxmox.com/pve-docs/pve-admin-guide.html -o source/html/pve-admin-guide.html
curl -fsSL https://pve.proxmox.com/pve-docs/api-viewer/apidoc.js -o source/api/apidoc.js
.venv/bin/python scripts/prepare.py
.venv/bin/python scripts/translate.py --workers 3
.venv/bin/python scripts/render.py
.venv/bin/python scripts/verify.py
```

翻译步骤调用本机已登录的 Kimi Code CLI，不读取、保存或输出登录凭据。每个有效译文单元会立即缓存于忽略跟踪的 `work/translations.jsonl`。恢复时只处理缺失或校验失败的单元。

本次译本在 Kimi 达到窗口用量上限后，经发布者授权由 Codex 子代理接力完成。辅助翻译批次可通过 `scripts/merge_agent_outputs.py` 合并；只有通过相同完整性校验的译文才会进入缓存。

`render.py` 默认拒绝生成含有未译内容的发布版本。`--allow-partial` 仅用于排版预览。发布前应检查 `reports/` 的完整性报告与 GitBook 的实际渲染。

## GitBook

`.gitbook.yaml` 指向 `docs/`，`gitbook-docs.yaml` 定义站点、中文空间与稳定空间键。`docs/SUMMARY.md` 是唯一导航来源。首次同步方向应选择 **GitHub → GitBook**。

原始页面与翻译工作缓存不提交到代码仓库；`source/manifest.json`、`source/assets-manifest.json` 和 `reports/` 保留内容来源与校验记录。

## 许可证

原始文档 Copyright (C) 2015 - 2026 Proxmox Server Solutions GmbH，依据 GNU Free Documentation License 1.3 或更新版本分发，无不变章节、封面文字或封底文字。中文翻译按同一文档许可证分发。完整英文条款见 `LICENSE` 与书内许可证页面。
