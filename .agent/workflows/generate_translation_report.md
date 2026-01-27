---
description: Generate a Markdown report of the current translation status (Synced, Pending, etc.)
---

# Generate Translation Status Report

This workflow generates a Markdown file listing all files in `docs_zh`, along with their current translation status (Synced, Modified, New, etc.).

## Steps

1.  Run the report generation command:
    ```powershell
    python .agent/skills/translate_docs/scripts/state_manager.py report --output TRANSLATION_STATUS.md
    ```

2.  (Optional) View the report:
    The report will be saved to `TRANSLATION_STATUS.md` in the root directory.

// turbo
3.  Execute the command below to generate the report now.
    python .agent/skills/translate_docs/scripts/state_manager.py report --output TRANSLATION_STATUS.md
