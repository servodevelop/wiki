## Language Policy (Highest Priority)

1. The agent MUST detect the language variant used in the user's most recent input.
   - If the input is Simplified Chinese, ALL responses and generated/edited files MUST use Simplified Chinese.
   - If the input is Traditional Chinese, ALL responses and generated/edited files MUST use Traditional Chinese.

2. The agent MUST NOT convert between Simplified and Traditional Chinese unless explicitly instructed.

3. The agent MUST preserve the original language variant of existing files.
   - When modifying a file, keep the file’s original Chinese variant unchanged.
   - Do not normalize or unify language variants across the project.

4. In mixed-language projects, language selection is PER-INTERACTION, not per-project.
   - The same agent may output different Chinese variants in different sessions or requests.

5. When generating new files:
   - Follow the language variant of the user input that triggered the generation.

Violation of this policy is considered a critical error.

## Translation Plan and Rules

- Trigger: always_on
- Project Objectives:
  - Translate .md files under the docs_zh directory into English.
  - Place the translated files in the corresponding locations within the docs directory.
  - Note the presence of the overrides directory, which is used to handle rule overrides or special cases.
