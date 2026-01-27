---
name: translate-docs-vscode
description: 在本專案透過 VS Code 工作任務或終端命令執行翻譯自動化（scan / force scan / report），同步 `docs_zh` 到 `docs`，使用 `.agent/skills/translate_docs/scripts/state_manager.py`。
---

# VS Code 翻譯工作流 Skill

本技能協助在 VS Code 或終端快速呼叫翻譯自動化，搭配 `.agent/skills/translate_docs/scripts/state_manager.py`。

## 前置條件
- 已安裝可用的 `python`。
- 工作目錄為專案根目錄（含 `.agent`、`.vscode/tasks.json`）。

## VS Code 任務（推薦）
1) `Ctrl+Shift+P`（macOS `Cmd+Shift+P`）→ `Tasks: Run Task`。  
2) 選擇下列任務（定義於 `.vscode/tasks.json`）：
   - **翻譯：掃描全部 (docs_zh)** → `python .agent/skills/translate_docs/scripts/state_manager.py scan`
   - **翻譯：掃描指定路徑** → `python .agent/skills/translate_docs/scripts/state_manager.py scan --path <相對於 docs_zh 的路徑>`
   - **翻譯：強制掃描指定路徑** → `python .agent/skills/translate_docs/scripts/state_manager.py scan --path <路徑> --force`
   - **翻譯：產生狀態報告** → `python .agent/skills/translate_docs/scripts/state_manager.py report --output TRANSLATION_STATUS.md`

> 小技巧：第二、三項任務會提示輸入路徑，預設值 `docs_zh`。

## 直接用終端（替代）
- 掃描全部：`python .agent/skills/translate_docs/scripts/state_manager.py scan`
- 掃描指定路徑：`python .agent/skills/translate_docs/scripts/state_manager.py scan --path "docs_zh/<子路徑或檔案>"`
- 強制掃描：在上述命令加 `--force`
- 產生報告：`python .agent/skills/translate_docs/scripts/state_manager.py report --output TRANSLATION_STATUS.md`

## 注意
- `translation_state.json` 為自動狀態檔，請勿手動編輯。
- 翻譯結果會寫入對應的 `docs/` 路徑，結構鏡像 `docs_zh/`。
