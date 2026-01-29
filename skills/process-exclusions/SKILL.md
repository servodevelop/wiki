---
name: process-exclusions
description: 處理 TRANSLATION_STATUS.md 中勾選為排除的條目（觸發詞 /process_exclusions），把對應路徑寫入 `.agent/exclusion.json`，並自動重新產生翻譯狀態報告；對應 Antigravity 工作流 `process_exclusions`。
---

# 處理排除清單（Codex / VS Code 版）

當你在 `TRANSLATION_STATUS.md` 的「排除」欄位把某些行改成 `[x]` 後，用這個技能把這些檔案加入排除清單（`.agent/exclusion.json`），並刷新報告。

## 觸發詞（記名）
- `/process_exclusions`
- 「處理排除清單」「把勾選的加入排除」「更新 exclusion」

## VS Code（推薦）
1) 打開命令面板：`Tasks: Run Task`  
2) 執行任務：**翻譯：處理排除清單**（定義於 `.vscode/tasks.json`）  

## 終端命令（等效）
```powershell
python .agent/skills/translate_docs/scripts/state_manager.py process_exclusions --output TRANSLATION_STATUS.md
```

## 結果
- 新增的排除項會寫入 `.agent/exclusion.json` 的 `excludes`。
- 腳本會自動重新產生 `TRANSLATION_STATUS.md` 以反映最新排除結果。
