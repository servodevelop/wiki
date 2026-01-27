---
name: generate-translation-report
description: 產生翻譯狀態報告，對應 Antigravity 工作流 /generate_translation_report（觸發詞），使用 `.agent/skills/translate_docs/scripts/state_manager.py report` 於本專案根目錄執行。
---

# 翻譯狀態報告 Skill

用來在專案層級生成 `TRANSLATION_STATUS.md`，列出 `docs_zh` 與 `docs` 的同步狀態。

## 觸發詞
- `/generate_translation_report`
- 「產生翻譯狀態報告」、「生成翻譯報告」、「翻譯報告」

## 前置條件
- `python` 可直接執行。
- 目前工作目錄為專案根目錄（含 `.agent` 與 `docs_zh`）。

## 快速指令
```powershell
python .agent/skills/translate_docs/scripts/state_manager.py report --output TRANSLATION_STATUS.md
```

## 操作步驟
1) 在 VS Code 內開啟整個 workspace。  
2) 打開終端或使用 `Tasks: Run Task`（可自訂任務指向上述指令）。  
3) 執行命令後，報告會產生在根目錄的 `TRANSLATION_STATUS.md`。  
4) 若需檢視結果，可直接在 VS Code 開啟該檔案。

## 輸出說明
- 報告包含每個檔案的狀態（新增、來源已改、目標已改、遺失目標、已翻譯、已忽略）。  
- 狀態來源：`.agent/translation_state.json` 與實際檔案雜湊比對。
