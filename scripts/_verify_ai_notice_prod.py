#!/usr/bin/env python3
"""Fetch home + all locale landing.html from production domains; report AI notice presence."""
from __future__ import annotations

import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = {
    "bg",
    "cz",
    "de",
    "ee",
    "en",
    "es",
    "fr",
    "gr",
    "hr",
    "hu",
    "it",
    "lt",
    "lv",
    "pl",
    "pt",
    "ro",
    "si",
    "sk",
}

DOMAINS = [
    "gadgetshifthub.com",
    "hubaurashop.com",
    "shopterva.com",
    "shoptrendcrest.com",
    "devicegridbay.com",
    "shoproomdock.com",
    "hometrendlivora.com",
]

NOTICE_CLASS = "site-footer__ai-image-notice"
EN_SNIP = "Some images on this page have been generated or modified"


def paths() -> list[str]:
    out = [""]
    for geo in sorted(LOCALES):
        for p in (ROOT / geo).rglob("landing.html"):
            rel = p.relative_to(ROOT).as_posix()
            out.append("/" + rel)
    return out


def fetch(url: str, ctx: ssl.SSLContext) -> tuple[int | None, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (AI-check)"})
    try:
        with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except Exception as e:  # noqa: BLE001 — report raw error
        return None, str(e)


def main() -> None:
    ctx = ssl.create_default_context()
    landing_paths = paths()

    for domain in DOMAINS:
        home_url = f"https://{domain}/"
        st, body = fetch(home_url, ctx)
        home_ok = (
            st == 200
            and NOTICE_CLASS in body
            and body.count(NOTICE_CLASS) == 1
            and EN_SNIP in body
        )

        bad: list[tuple[str, str]] = []
        checked = 0
        for path in landing_paths:
            if not path:
                continue
            url = f"https://{domain}{path}"
            st_l, b = fetch(url, ctx)
            checked += 1
            if st_l != 200:
                bad.append((url, f"HTTP {st_l!r}: {b[:80]}"))
                continue
            c = b.count(NOTICE_CLASS)
            if c != 1:
                bad.append((url, f"notice_count={c}"))

        print(f"=== {domain} ===")
        home_label = "OK" if home_ok else "FAIL"
        print(f"Home /: {home_label}")
        if not home_ok:
            c = body.count(NOTICE_CLASS) if body and st == 200 else "n/a"
            print(f"  home: status={st!r} notice_count={c} has_en_snip={EN_SNIP in (body or '')}")
        print(f"Landings checked: {checked}; failures: {len(bad)}")
        for u, msg in bad[:25]:
            print(f"  {msg} — {u}")
        if len(bad) > 25:
            print(f"  ... and {len(bad) - 25} more")
        print()


if __name__ == "__main__":
    main()
