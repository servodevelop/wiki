# Translation Project Guide (翻譯專案指南)

本文件說明將 `docs_zh` (簡體中文) 同步翻譯至 `docs` (英文) 的自動化工作流與工具使用方式。

## 1. 專案架構 (Architecture)

*   **來源目錄 (Source)**: `docs_zh/` (作為唯一的結構依據 Source of Truth)
*   **目標目錄 (Target)**: `docs/`
*   **同步策略**: 目錄結構直接鏡像 (Mirroring)。英文版不再進行 Snake/Kebab case 轉換，完全對應中文版路徑。
*   **變更偵測**: 採用 MD5 Hash 值比對，而非時間戳記。

## 2. 自動化工具 (Automation)

本專案使用專屬的 Agent Skill `translate_docs` 搭配 Python 腳本進行管理。

*   **Skill 定義**: `.agent/skills/translate_docs/SKILL.md`
*   **狀態管理腳本**: `.agent/skills/translate_docs/scripts/state_manager.py`
*   **狀態記錄檔**: `.agent/translation_state.json` (自動生成，請勿手動修改)

## 3. 與 Agent 互動 (Interaction)

您可以使用自然語言直接指揮 Agent 執行翻譯任務。Agent 會透過 Skills 自動判斷需執行的指令。

### 常見指令範例

| 需求 | 指令範例 (自然語言) | 備註 |
| :--- | :--- | :--- |
| **同步所有變更** | "幫我掃描並翻譯所有更新的檔案。" | Agent 會自動掃描全站，找出 `New` 或 `Modified` 的檔案進行翻譯。 |
| **翻譯特定目錄** | "翻譯 `docs_zh/rs485-servo` 這個目錄。" | Agent 會鎖定該目錄範圍進行掃描與翻譯。 |
| **翻譯特定檔案** | "重新翻譯 `index.md`。" | 若檔案未變更，Agent 會詢問是否強制執行。 |
| **強制重譯** | "把 `index.md` 強制重翻一次。" | Agent 會忽略 Hash 狀態，強制覆寫目標檔案。 |

## 4. 手動/進階操作 (Manual CLI)

若需除錯或手動檢查狀態，可直接在終端機執行 Python 腳本：

```powershell
# 1. 掃描全站狀態 (列出需翻譯檔案)
python .agent/skills/translate_docs/scripts/state_manager.py scan

# 2. 掃描特定目錄
python .agent/skills/translate_docs/scripts/state_manager.py scan --path "docs_zh/uart-servo"

# 3. 強制列出特定檔案 (即使已同步)
python .agent/skills/translate_docs/scripts/state_manager.py scan --path "docs_zh/index.md" --force
```

## 5. 注意事項

*   **翻譯品質**: Agent 會保留 Markdown 語法、HTML 標籤與程式碼區塊邏輯，僅翻譯可讀文字。
*   **連結修正**: 由於結構直接鏡像，大部分相對連結 (`../assets/...`) 應能直接沿用。若有圖片無法顯示，請檢查 `docs_zh` 中的原始連結是否正確。
