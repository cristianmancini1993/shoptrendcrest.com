#!/usr/bin/env python3
"""Browser QA for live WARMIO landings (layout, JS UI, form HTML5 validation)."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location("gen", SCRIPTS / "gen_warmio_geos.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

BASE = "https://shoptrendcrest.com"
VIEWPORTS = [(375, 812), (768, 1024), (1440, 900)]


def audit_landing(page, offer: str, geo: str) -> list[str]:
    url = f"{BASE}/{geo}/warmio-{offer}/"
    errs: list[str] = []
    page.goto(url, wait_until="networkidle", timeout=60000)

    cfg = page.evaluate("() => window.SITE_CONFIG || {}")
    if cfg.get("GEO") != geo:
        errs.append(f"SITE_CONFIG.GEO={cfg.get('GEO')}")
    sub = cfg.get("SUBMITTING_LABEL") or ""
    if not sub or sub == "Sending...":
        errs.append(f"SUBMITTING_LABEL missing: {sub!r}")
    if geo != "it" and (sub.startswith("Invio") or sub == "Invio ordine in corso..."):
        errs.append(f"SUBMITTING_LABEL Italian leak: {sub!r}")
    cookie = cfg.get("COOKIE_TEXT") or ""
    if not cookie or cookie.startswith("We use cookies"):
        errs.append("COOKIE_TEXT not localized")
    page.wait_for_timeout(300)
    banner = page.locator("#df-cookie-ok")
    if banner.count():
        if cookie and cookie[:20] not in page.content():
            errs.append("cookie banner missing localized COOKIE_TEXT")
    else:
        errs.append("cookie accept button not shown")

    for w, h in VIEWPORTS:
        page.set_viewport_size({"width": w, "height": h})
        page.wait_for_timeout(200)
        overflow = page.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 2"
        )
        if overflow:
            errs.append(f"horizontal overflow @{w}px")

    page.set_viewport_size({"width": 375, "height": 812})

    # Countdown ticks (seconds should change within ~2s)
    s0 = page.locator("#cd-s").inner_text(timeout=5000)
    page.wait_for_timeout(2200)
    s1 = page.locator("#cd-s").inner_text()
    if s0 == s1:
        errs.append("countdown seconds did not tick")

    # Live counter localized template
    live = page.locator("#liveCount")
    if not live.count():
        errs.append("missing #liveCount")
    else:
        html = live.inner_html()
        if "persone" in html and geo != "it":
            errs.append("liveCount Italian leak")

    # FAQ
    faq = page.locator(".faq-item").first
    if not faq.count():
        errs.append("no FAQ")
    else:
        faq.locator(".faq-q").click()
        page.wait_for_timeout(200)
        if "open" not in (faq.get_attribute("class") or ""):
            errs.append("FAQ did not open")

    # CTA → form
    cta = page.locator('a.cta-inline[href="#order-form"], a.cta-btn[href="#order-form"]').first
    if cta.count():
        cta.click()
        page.wait_for_timeout(400)
        in_view = page.evaluate(
            """() => {
              const el = document.getElementById('order-form');
              if (!el) return false;
              const r = el.getBoundingClientRect();
              return r.top < window.innerHeight && r.bottom > 0;
            }"""
        )
        if not in_view:
            errs.append("CTA scroll to #order-form failed")

    # Images
    for i, sel in enumerate(["img.t-photo", "img.avatar"]):
        imgs = page.locator(sel)
        n = imgs.count()
        if n < 1 and sel == "img.t-photo":
            errs.append("no testimonial photos")
            break
        for j in range(min(n, 3)):
            ok = imgs.nth(j).evaluate(
                "el => el.complete && el.naturalWidth > 0"
            )
            if not ok:
                errs.append(f"broken image {sel} #{j}")

    # Form fields order + required
    ids = page.evaluate(
        """() => Array.from(document.querySelectorAll('.tm-order-form label'))
          .map(l => l.getAttribute('for')).filter(Boolean)"""
    )
    if ids != ["name", "tel", "street-address"]:
        errs.append(f"form field order {ids}")

    for fid in ("name", "tel", "street-address"):
        if not page.locator(f"#{fid}[required]").count():
            errs.append(f"missing required #{fid}")

    # HTML5 validation: empty submit stays on page
    page.locator('.tm-order-form button[type="submit"]').click()
    page.wait_for_timeout(500)
    if page.url != url and "/thank-you/" in page.url:
        errs.append("empty submit redirected (unexpected)")
    if page.url != url and "/thank-you/" not in page.url:
        errs.append("empty submit changed URL unexpectedly")

    return errs


def audit_typ(page, offer: str, geo: str) -> list[str]:
    url = f"{BASE}/{geo}/warmio-{offer}/thank-you/"
    errs: list[str] = []
    page.goto(url, wait_until="networkidle", timeout=60000)
    for w, h in VIEWPORTS:
        page.set_viewport_size({"width": w, "height": h})
        page.wait_for_timeout(150)
        overflow = page.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 2"
        )
        if overflow:
            errs.append(f"TYP horizontal overflow @{w}px")
    if "WARMIO" not in page.content():
        errs.append("no WARMIO on TYP")
    return errs


def main() -> int:
    from playwright.sync_api import sync_playwright

    results: dict[str, list[str]] = {}
    failed = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for offer, cfg in sorted(mod.GEOS.items(), key=lambda x: x[1]["geo"]):
            geo = cfg["geo"]
            for kind, fn in (("LP", audit_landing), ("TYP", audit_typ)):
                context = browser.new_context(locale="en-US")
                page = context.new_page()
                key = f"{offer}-{geo}-{kind}"
                try:
                    errs = fn(page, offer, geo)
                except Exception as e:
                    errs = [f"exception: {e}"]
                results[key] = errs
                if errs:
                    failed += 1
                    print(f"FAIL {key}: " + "; ".join(errs))
                else:
                    print(f"OK   {key}")
                context.close()

        browser.close()

    out = SCRIPTS.parent / "verify-warmio-browser.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nFailed: {failed}/26 — details in {out.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
