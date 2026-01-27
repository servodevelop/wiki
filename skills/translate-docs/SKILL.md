---
name: translate-docs
description: 在此 workspace 執行翻譯工作流（scan/force/report）以同步 `docs_zh` → `docs`，對應原先 Antigravity 的 `.agent` 腳本並提供 VS Code 任務入口。
---

# 翻譯工作流（Codex 版）

> 目的：讓 Codex 在 workspace 層級也能觸發原本 Antigravity 的翻譯流程，透過 VS Code 任務或終端指令呼叫 `.agent/skills/translate_docs/scripts/state_manager.py`。

## 資源位置（保留原 .agent）
- 腳本：`.agent/skills/translate_docs/scripts/state_manager.py`
- 資料檔：`.agent/translation_state.json`（自動生成）、`.agent/glossary.csv`、`.agent/exclusion.json`
- 工作流說明：`.agent/workflows/generate_translation_report.md`
- VS Code 任務：`.vscode/tasks.json`

## 前置條件
- 已安裝可用的 `python` 指令。
- 目前工作目錄為專案根目錄（包含 `.agent` 與 `.vscode`）。

## 在 VS Code 執行（推薦）
1. `Ctrl+Shift+P`（macOS `Cmd+Shift+P`）→ `Tasks: Run Task`
2. 選擇任務：
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

## 狀態與結果
- 翻譯狀態寫入 `.agent/translation_state.json`；勿手動修改。
- 翻譯後的檔案寫入 `docs/`，路徑鏡像 `docs_zh/`。
- 報告輸出在專案根目錄的 `TRANSLATION_STATUS.md`。
- **完成翻譯後必做**：若有任何目標檔案新增或被修改，務必重新產生報告：  
  `python .agent/skills/translate_docs/scripts/state_manager.py report --output TRANSLATION_STATUS.md`
