---
name: translate_docs
description: Translates Markdown documentation from Simplified Chinese to English, maintaining structure and formatting. Supports incremental updates via hash synchronization.
---

# Translate Docs Skill

This skill helps you translate documentation from `docs_zh` (Simplified Chinese) to `docs` (English). It supports both single-file translation and bulk synchronization based on content hash.

## Workflow

### 1. Check for Pending Translations
Run the state manager script to see which files need translation. You can scan all files, a specific directory, or a single file.

```powershell
# Scan all
python .agent/skills/translate_docs/scripts/state_manager.py scan

# Scan specific path (file or folder)
python .agent/skills/translate_docs/scripts/state_manager.py scan --path "docs_zh/subdir"

# Force re-scan (ignore hash state)
python .agent/skills/translate_docs/scripts/state_manager.py scan --path "docs_zh/file.md" --force
```

### 2. Translate a File
For each file in the list (or a specific file requested by the user), follow these steps:

1.  **Read Source**: Read the content of the `source` file.
2.  **Translate**: Translate the content from Simplified Chinese to English.
    *   **Rules**:
        *   Maintain all Markdown formatting (headers, lists, bold, italic, links, images).
        *   Keep HTML tags exactly as is.
        *   Translate comments in code blocks if they explain the logic; keep code logic unchanged.
        *   **Do NOT** translate technical terms that are standard (e.g., protocol names, specific variable names).
        *   **Mirror Structure**: The target file path should mirror the source file path (e.g., `docs_zh/a/b.md` -> `docs/a/b.md`).
        *   **Images/Links**: Since the structure is mirrored, relative links (e.g., `../assets/img.png`) usually remain valid. Only adjust if you detect a level change.
3.  **Write Target**: Write the translated content to the `target` file path. Ensure the directory exists.
4.  **Update State**: After successful write, update the hash state to mark it as done.
    ```powershell
    python .agent/skills/translate_docs/scripts/state_manager.py update --file "relative/path/to/file.md" --hash "md5_hash_of_source"
    ```

## Example Usage

**User**: "Translate all updated files."

**Agent**:
1. Run `state_manager.py scan`.
2. Receive list: `[{"source": "...", "target": "...", "relative": "uart/index.md", "current_hash": "abc..."}]`.
3. Read `docs_zh/uart/index.md`.
4. Translate content.
5. Write to `docs/uart/index.md`.
6. Run `state_manager.py update --file "uart/index.md" --hash "abc..."`.
