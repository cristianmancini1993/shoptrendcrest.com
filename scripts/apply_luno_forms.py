#!/usr/bin/env python3
"""Replace LUNO order forms with network snippets."""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "snip", Path(__file__).with_name("_luno_form_snippets.py")
)
snip = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(snip)

FORM_RE = re.compile(
    r'<form class="tm-order-form[^"]*"[\s\S]*?</form>',
    re.MULTILINE,
)
NOTE_RE = re.compile(r'<p class="form-note">[\s\S]*?</p>')


def main() -> None:
    for offer_id, rel in snip.LANDINGS.items():
        path = ROOT / rel
        html = path.read_text(encoding="utf-8")
        note = NOTE_RE.search(html)
        new_form = snip.FORMS[offer_id]
        if note:
            new_form = new_form.replace(
                "</form>",
                f'\n          {note.group(0).strip()}\n</form>',
                1,
            )
        html2, n = FORM_RE.subn(new_form, html, count=1)
        if n != 1:
            raise SystemExit(f"form not replaced once in {rel} (n={n})")
        path.write_text(html2, encoding="utf-8", newline="\n")
        print("OK", rel)


if __name__ == "__main__":
    main()
