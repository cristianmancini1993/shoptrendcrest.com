#!/usr/bin/env python3
"""Ensure all thankyoupage hidden fields use full https:// URLs."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(
    r'(name="thankyoupage"\s+type="hidden"\s+value=")(?!https://)([^"]+)(")',
    re.IGNORECASE,
)


def fix_text(text: str) -> tuple[str, int]:
    def repl(match: re.Match[str]) -> str:
        value = match.group(2)
        if value.startswith("https://"):
            return match.group(0)
        if value.startswith("gadgetshifthub.com/"):
            value = "https://" + value
        elif value.startswith("/"):
            value = "https://gadgetshifthub.com" + value
        else:
            value = "https://gadgetshifthub.com/" + value.lstrip("/")
        return match.group(1) + value + match.group(3)

    new_text, count = PATTERN.subn(repl, text)
    return new_text, count


def main() -> None:
    total_files = 0
    total_replacements = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".py", ".js"}:
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new_text, count = fix_text(text)
        if count:
            path.write_text(new_text, encoding="utf-8")
            total_files += 1
            total_replacements += count
            print(f"fixed {count:2d}  {path.relative_to(ROOT)}")
    print(f"\nDone: {total_replacements} replacements in {total_files} files")


if __name__ == "__main__":
    main()
