"""
MkDocs hook: Convert GitHub/Typora-style Alerts to MkDocs Material admonitions.

Supports:
> [!NOTE] / > [!TIP] / > [!IMPORTANT] / > [!WARNING] / > [!CAUTION]
(with optional inline title after the marker)

Example input (engineers keep writing this):
> [!CAUTION] Don't hot-plug RS-485
> This may reset the bus.
>
> - Power off first.

Converted output:
!!! caution "Don't hot-plug RS-485"
    This may reset the bus.

    - Power off first.
"""

from __future__ import annotations

import re
from typing import List, Optional

# Map GitHub alert type -> MkDocs Material admonition type.
#
# NOTE/TIP/WARNING are built-in in Material.
# GitHub's CAUTION is closer to Material's "danger" (red) than "warning" (orange).
# IMPORTANT is kept as a custom type so we can style it as purple without
# affecting any third-party docs that may use "info"/"success".
TYPE_MAP = {
    "NOTE": ("note", None),
    "TIP": ("tip", None),
    "IMPORTANT": ("important", "Important"),
    "WARNING": ("warning", None),
    "CAUTION": ("danger", "Caution"),
}

# Start of a GitHub alert blockquote
ALERT_RE = re.compile(r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)\s*$")

# Any blockquote line (including a bare '>' line)
BQ_RE = re.compile(r"^\s*> ?(.*)$")


def _consume_blockquote(lines: List[str], start_idx: int) -> tuple[List[str], int]:
    """
    Consume consecutive blockquote lines starting at start_idx.
    Returns (content_without_chevron, next_idx_after_block).
    """
    content: List[str] = []
    i = start_idx
    while i < len(lines):
        m = BQ_RE.match(lines[i])
        if not m:
            break
        content.append(m.group(1))
        i += 1
    return content, i


def _render_admonition(adm_type: str, title: Optional[str], body_lines: List[str]) -> List[str]:
    # Trim one leading blank line in body (common pattern: '> ' right after marker)
    while body_lines and body_lines[0].strip() == "":
        body_lines = body_lines[1:]

    # Build header
    if title and title.strip():
        header = f'!!! {adm_type} "{title.strip()}"'
    else:
        header = f"!!! {adm_type}"

    rendered = [header]
    # Indent body by 4 spaces (MkDocs admonition requirement)
    for ln in body_lines:
        rendered.append("    " + ln.rstrip())
    # Ensure there's at least one indented line, otherwise MkDocs can treat it oddly
    if len(rendered) == 1:
        rendered.append("    ")
    return rendered


def on_page_markdown(markdown: str, *, page, config, files) -> str:
    lines = markdown.splitlines()
    out: List[str] = []
    i = 0

    while i < len(lines):
        m = ALERT_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        gh_type = m.group(1)
        title = m.group(2) or ""

        adm_type, default_title = TYPE_MAP.get(gh_type, ("note", None))
        if (not title.strip()) and default_title:
            title = default_title

        # Consume the full blockquote for this alert (marker line included)
        block, next_i = _consume_blockquote(lines, i)

        # block[0] is the marker line content (without '> ')
        # The rest is the body (already stripped of '> ')
        body = block[1:] if len(block) > 1 else []

        out.extend(_render_admonition(adm_type, title, body))
        i = next_i

        # Preserve a blank line after the admonition if the source had a blank line break
        if i < len(lines) and lines[i].strip() == "":
            out.append("")
            i += 1

    return "\n".join(out) + "\n"
