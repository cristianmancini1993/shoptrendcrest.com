#!/usr/bin/env python3
"""Browser QA: Granvia geo order forms — placeholders after Adrice js-v2 + screenshots."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent

from _granvia_form_examples import FIELD_ORDER, GRANVIA_FORM_EXAMPLES  # noqa: E402

OFFERS = json.loads((ROOT / "content/granvia/offers.json").read_text(encoding="utf-8"))
OFFER_ROWS = [(str(o["id"]), o["geo"], o["lang"]) for o in OFFERS]

VIEWPORTS = {
    "desktop": (1440, 900),
    "mobile": (390, 844),
}

ADRICE_SETTLE_MS = 9000


def expected_for_lang(lang: str) -> dict[str, str]:
    return {
        "name": GRANVIA_FORM_EXAMPLES[lang]["ph_name"],
        "tel": GRANVIA_FORM_EXAMPLES[lang]["ph_tel"],
        "street-address": GRANVIA_FORM_EXAMPLES[lang]["ph_addr"],
    }


def audit_form(page, base: str, offer: str, geo: str, lang: str, shot_dir: Path) -> list[str]:
    url = f"{base}/{geo}/granvia-{offer}/#order-form"
    errs: list[str] = []
    page.goto(url, wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(ADRICE_SETTLE_MS)

    want = expected_for_lang(lang)
    got = page.evaluate(
        """() => {
      const f = document.querySelector('.tm-order-form');
      if (!f) return { err: 'no form' };
      const fields = ['name', 'tel', 'street-address'];
      const out = {};
      fields.forEach((n) => {
        const el = f.querySelector('input[name="' + n + '"]');
        const lab = el ? f.querySelector('label[for="' + el.id + '"]') : null;
        out[n] = {
          placeholder: el ? el.placeholder : '',
          value: el ? el.value : '',
          label: lab ? lab.textContent.trim() : '',
          dataPh: el ? el.getAttribute('data-cendora-placeholder') || '' : '',
        };
      });
      const labels = Array.from(f.querySelectorAll('label'))
        .map((l) => l.getAttribute('for'))
        .filter(Boolean);
      return { fields: out, labelOrder: labels };
    }"""
    )
    if got.get("err"):
        return [got["err"]]

    label_order = got.get("labelOrder") or []
    if label_order != list(FIELD_ORDER):
        errs.append(f"label order {label_order}")

    for field in FIELD_ORDER:
        info = got["fields"][field]
        if info["value"]:
            errs.append(f"{field} has value (must be empty): {info['value']!r}")
        if info["placeholder"] != want[field]:
            errs.append(
                f"{field} placeholder {info['placeholder']!r} != {want[field]!r}"
            )
        if info["dataPh"] and info["dataPh"] != want[field]:
            errs.append(f"{field} data-cendora-placeholder mismatch")
        if info["placeholder"] == info["label"].rstrip("*"):
            errs.append(f"{field} placeholder equals label text (Adrice leak)")

    cfg = page.evaluate(
        "() => (window.SITE_CONFIG && window.SITE_CONFIG.FORM_PLACEHOLDERS) || null"
    )
    if not cfg:
        errs.append("SITE_CONFIG.FORM_PLACEHOLDERS missing")
    else:
        for field in FIELD_ORDER:
            if cfg.get(field) != want[field]:
                errs.append(f"SITE_CONFIG {field} {cfg.get(field)!r} != {want[field]!r}")

    form = page.locator("#order-form")
    for vp_name, size in VIEWPORTS.items():
        page.set_viewport_size({"width": size[0], "height": size[1]})
        page.wait_for_timeout(300)
        form.scroll_into_view_if_needed()
        page.wait_for_timeout(200)
        shot = shot_dir / f"granvia-{offer}-{geo}-{vp_name}.png"
        form.screenshot(path=str(shot))

    return errs


def main() -> int:
    base = (sys.argv[1] if len(sys.argv) > 1 else "https://shoptrendcrest.com").rstrip("/")
    shot_dir = SCRIPTS / "_tmp" / "granvia-form-screenshots"
    shot_dir.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright

    results: dict[str, list[str]] = {}
    failed = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for offer, geo, lang in OFFER_ROWS:
            context = browser.new_context(locale="en-US")
            page = context.new_page()
            key = f"{offer}-{geo}"
            try:
                errs = audit_form(page, base, offer, geo, lang, shot_dir)
            except Exception as exc:
                errs = [f"exception: {exc}"]
            results[key] = errs
            if errs:
                failed += 1
                print(f"FAIL {key}: " + "; ".join(errs))
            else:
                print(f"OK   {key} — screenshots in {shot_dir.name}")
            context.close()
        browser.close()

    report = SCRIPTS.parent / "verify-granvia-forms-browser.json"
    report.write_text(
        json.dumps({"base": base, "results": results}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nScreenshots: {shot_dir}")
    print(f"Report: {report.name}")
    print(f"Failed: {failed}/{len(OFFER_ROWS)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
