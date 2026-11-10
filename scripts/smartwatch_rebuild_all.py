#!/usr/bin/env python3
"""Rebuild all Noventis smartwatch landings and thank-you pages."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import _smartwatch_ui as ui  # noqa: E402
from _smartwatch_chrome_i18n import PRESERVE_CHROME_FROM_BASE, TY_HERO_ALTS  # noqa: E402
from _smartwatch_text_patches import apply_body_patches  # noqa: E402

NOVENTIS_TEMPLATE = ROOT / "it" / "noventis" / "landing.html"
TY_TEMPLATE = ROOT / "it" / "noventis" / "thank-you.html"
LV_SRC = SCRIPTS / "_src_lv_3834.html"

BODY_START_MARKERS = (
    "<!-- ===== WHY BLOCKS",
    "<!-- ===== WHY BLOCK",
)
BODY_END_MARKER = '<footer class="site-footer">'

_CHROME_KEYS = (
    "topbar",
    "rating_line",
    "gift_strip",
    "h1_mobile",
    "h1_desktop",
    "lead",
    "hero_alt",
    "form_note_hero",
    "feat1_h",
    "feat1_p",
    "feat2_h",
    "feat2_p",
    "feat3_h",
    "feat3_p",
    "feat4_h",
    "feat4_p",
    "timer_label",
    "timer_h",
    "timer_m",
    "timer_s",
    "stock_left",
    "stock_right",
    "live_count",
    "order_h2",
    "order_p",
    "form_name_label",
    "form_tel_label",
    "form_addr_label",
    "form_submit",
    "form_note_bottom",
    "cta",
)


def _one(html: str, pat: str, group: int = 1) -> str | None:
    m = re.search(pat, html, re.DOTALL | re.IGNORECASE)
    return m.group(group).strip() if m else None


def extract_chrome_patch(html: str) -> dict:
    one = lambda pat, group=1: _one(html, pat, group)

    patch: dict[str, str] = {}
    if v := one(r'<div class="topbar">([^<]+)</div>'):
        patch["topbar"] = v
    if v := one(r'class="rating-text">([\s\S]*?)</div>'):
        patch["rating_line"] = v
    if v := one(r'class="gift-strip">([^<]+)</span>'):
        patch["gift_strip"] = v
    if v := one(r'<h1 class="h1-mobile-only">([\s\S]*?)</h1>'):
        patch["h1_mobile"] = v
    if v := one(r'<h1 class="h1-desktop-only">([\s\S]*?)</h1>'):
        patch["h1_desktop"] = v
    if v := one(r'<p class="lead">([\s\S]*?)</p>'):
        patch["lead"] = v
    if v := one(r'hero-image-mobile-only">\s*<img[^>]+alt="([^"]*)"'):
        patch["hero_alt"] = v.replace("♪", "").strip() or patch.get("hero_alt", "Noventis™")
    if v := one(r'<p class="form-note">([^<]+)</p>'):
        patch["form_note_hero"] = v
    feats = re.findall(
        r'class="feature-item"><div class="ico">[^<]+</div><h4>([^<]+)</h4><p>([^<]+)</p>',
        html,
    )
    for i, (h, p) in enumerate(feats[:4], start=1):
        patch[f"feat{i}_h"] = h
        patch[f"feat{i}_p"] = p
    if v := one(r'class="countdown-label">([^<]+)</div>'):
        patch["timer_label"] = v
    labels = re.findall(r'class="lbl">([^<]+)</div>', html)
    if len(labels) >= 3:
        patch["timer_h"], patch["timer_m"], patch["timer_s"] = labels[:3]
    if v := one(r'class="stock-label">\s*<span class="left">([^<]+)</span>'):
        patch["stock_left"] = v
    if v := one(r'<span class="right">([^<]+)</span>\s*</div>\s*<div class="stock-bar">'):
        patch["stock_right"] = v
    if v := one(r'id="liveCount">([\s\S]*?)</span>'):
        patch["live_count"] = v
    if v := one(r'<div class="order-card">\s*<h2>([^<]+)</h2>'):
        patch["order_h2"] = v
    if v := one(r'<div class="order-card">\s*<h2>[^<]+</h2>\s*<p>([\s\S]*?)</p>'):
        patch["order_p"] = v
    if v := one(r'<label for="name">([^<]+)</label>'):
        patch["form_name_label"] = v
    if v := one(r'<label for="tel">([^<]+)</label>'):
        patch["form_tel_label"] = v
    if v := one(r'<label for="street-address">([^<]+)</label>'):
        patch["form_addr_label"] = v
    if v := one(r'<button name="submit" type="submit">([^<]+)</button>'):
        patch["form_submit"] = v
    if v := one(r'class="form-note">([^<]+)</p>\s*<script src="https://offers.adricenetwork.com'):
        patch["form_note_bottom"] = v
    if v := one(r'href="#order-form" class="cta-btn">([^<]+)</a>'):
        patch["cta"] = v
    return {k: v for k, v in patch.items() if k in _CHROME_KEYS and v}


def bootstrap_chrome_from_landings() -> None:
    """Merge hero/order chrome from pre-rebuild shoproomdock exports on disk."""
    import urllib.request

    src = "https://shoproomdock.com"
    for offer_id, cfg in ui.OFFERS.items():
        if cfg["body_locale"] == "hr":
            continue
        geo = cfg["geo"]
        url = f"{src}/{geo}/smartwatch-{offer_id}/"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hss-rebuild/1.0"})
            html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
        except Exception as exc:
            print("chrome fetch skip", offer_id, exc)
            continue
        html = html.replace("Ultrawatch", "Noventis")
        patch = extract_chrome_patch(html)
        loc = cfg["body_locale"]
        base = dict(ui.LOCALE_OVERRIDES.get(loc, ui.SECTIONS_IT))
        merged = dict(base)
        merged.update({k: v for k, v in patch.items() if k in _CHROME_KEYS})
        for key in PRESERVE_CHROME_FROM_BASE:
            if key in base:
                merged[key] = base[key]
        ui.LOCALE_OVERRIDES[loc] = merged
        print("chrome", loc, len(patch))


def load_head_styles() -> str:
    html = NOVENTIS_TEMPLATE.read_text(encoding="utf-8")
    start = html.index("<head>")
    end = html.index("</head>") + len("</head>")
    return html[start:end]


def clean_body_fragment(html: str) -> str:
    html = html.replace("Ultrawatch™", "Noventis™").replace("Ultrawatch", "Noventis")
    html = re.sub(r'(<img[^>]*?)\s+♪([^"\'>]+)["\']?\s*', r'\1 alt="\2" ', html)
    html = re.sub(r'(<img[^>]*?)\s+#([^"\'>]+)\s*"', r'\1 alt="\2" ', html)
    html = re.sub(r'(<video[^>]*?)\s+♪([^">]+)["\']?\s*>', r'\1 aria-label="\2">', html)
    html = re.sub(r"\s*♪[^\"'>]+", "", html)
    html = re.sub(
        r'<img([^>]*)(?<!alt=)(?<!alt =)\s*/?>',
        lambda m: m.group(0),
        html,
    )
    html = re.sub(
        r'(<img[^>]*?)\s+♪[^">]*("|\s*/>)',
        r'\1 alt="Noventis™"\2',
        html,
    )
    html = re.sub(
        r'alt\s*=\s*"[^"]*TRANSLATOR[^"]*"',
        'alt="Noventis™"',
        html,
        flags=re.I,
    )
    html = html.replace("NAME OF TRANSLATORS", "Ar tinka kasdieniam naudojimui?")
    html = re.sub(r"III PRIEDAS\s*", "", html)
    html = re.sub(r"\bprožektorius\b", "išmanusis laikrodis", html, flags=re.I)
    html = re.sub(r"\bprožektor\b", "išmanusis laikrodis", html, flags=re.I)
    html = re.sub(r"Noventis™([A-Za-zÀ-ž])", r"Noventis™ \1", html)
    return html


def extract_body_from_landing(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    start = -1
    for mark in BODY_START_MARKERS:
        if mark in html:
            start = html.index(mark)
            break
    if start < 0:
        raise ValueError(f"body start not found in {path}")
    end = html.index(BODY_END_MARKER, start)
    return clean_body_fragment(html[start:end])


def lv_kit_from_source() -> str:
    html = LV_SRC.read_text(encoding="utf-8")
    s = html.index("<!-- ===== KIT BOX =====")
    e = html.index("<!-- ===== FAQ =====", s)
    return clean_body_fragment(html[s:e])


def replace_lv_kit(body: str) -> str:
    if "<!-- ===== KIT BOX =====" not in body:
        return body
    s = body.index("<!-- ===== KIT BOX =====")
    e = body.index("<!-- ===== FAQ =====", s)
    return body[:s] + lv_kit_from_source() + body[e:]


def fetch_shoproomdock_body(geo: str, offer_id: str) -> str:
    import urllib.request

    url = f"https://shoproomdock.com/{geo}/smartwatch-{offer_id}/"
    req = urllib.request.Request(url, headers={"User-Agent": "hss-rebuild/1.0"})
    html = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    start = -1
    for mark in BODY_START_MARKERS:
        if mark in html:
            start = html.index(mark)
            break
    if start < 0:
        raise ValueError(f"body start missing for {geo}/{offer_id}")
    end = html.index('<footer class="gsh-standalone-footer">', start)
    return clean_body_fragment(html[start:end])


def sync_body_files() -> None:
    """Always rebuild body fragments from template (hr/lt) or clean shoproomdock source."""
    ui.BODIES_DIR.mkdir(parents=True, exist_ok=True)
    template_locales = {"hr", "lt"}
    by_locale: dict[str, str] = {}
    for offer_id, cfg in ui.OFFERS.items():
        loc = cfg["body_locale"]
        if loc in by_locale:
            continue
        if loc in template_locales:
            body = ui.render_body_html(loc, cfg["was"], cfg["now"], cfg.get("lv_kit", False))
        else:
            try:
                body = fetch_shoproomdock_body(cfg["geo"], offer_id)
            except Exception as exc:
                print("body fetch fallback", loc, exc)
                body = ui.render_body_html(loc, cfg["was"], cfg["now"], cfg.get("lv_kit", False))
        if cfg.get("lv_kit"):
            body = replace_lv_kit(body)
        body = clean_body_fragment(body)
        body = apply_body_patches(body, loc)
        by_locale[loc] = body
    for loc, body in by_locale.items():
        cfg = next(c for c in ui.OFFERS.values() if c["body_locale"] == loc)
        body = re.sub(
            r'<span class="was">[^<]*</span>\s*<span class="now">[^<]*</span>',
            f'<span class="was">{cfg["was"]}</span>\n          <span class="now">{cfg["now"]}</span>',
            body,
            count=1,
        )
        out = ui.BODIES_DIR / f"{loc}.html"
        out.write_text(body, encoding="utf-8", newline="\n")
        print("body", out.name)


def patch_head(head: str, offer_id: str) -> str:
    cfg = ui.OFFERS[offer_id]
    u = ui.ui_strings(cfg["body_locale"])
    geo, slug = cfg["geo"], ui.slug_for(offer_id)
    head = re.sub(r'<html lang="[^"]*"', f'<html lang="{cfg["lang"]}"', head, count=1)
    head = re.sub(r"<title>[^<]*</title>", f"<title>{u['title']}</title>", head, count=1)
    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{u["meta_desc"]}">',
        head,
        count=1,
    )
    head = re.sub(
        r'<meta name="offer-id" content="\d+">',
        f'<meta name="offer-id" content="{offer_id}">',
        head,
        count=1,
    )
    head = re.sub(
        r'<link rel="canonical" href="[^"]+">',
        f'<link rel="canonical" href="https://homeshopspot.com/{geo}/{slug}/landing.html">',
        head,
        count=1,
    )
    site_cfg = f"""window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  OFFER_ID: '{offer_id}',
  CURRENCY: '{cfg["currency"]}',
  PRICE: {cfg["price"]},
  OFFER_NAME: 'Noventis {offer_id}',
  LP_ID: '{geo}-{slug}',
  FORM_ENDPOINT: 'https://offers.adricenetwork.com/forms/html/',
  SUBMITTING_LABEL: '{u["submitting"]}',
  COOKIE_TEXT: '{u["cookie_text"]}',
  COOKIE_ACCEPT: '{u["cookie_accept"]}',
  COOKIE_LEARN: '{u["cookie_learn"]}'
}};"""
    head = re.sub(r"window\.SITE_CONFIG = \{[\s\S]*?\};", site_cfg, head, count=1)
    if "<!-- Meta Pixel Code -->" not in head:
        head = head.replace("<head>", "<head>\n" + ui.META_PIXEL + "\n", 1)
    return head


def build_landing(offer_id: str) -> str:
    cfg = ui.OFFERS[offer_id]
    loc = cfg["body_locale"]
    body_path = ui.BODIES_DIR / f"{loc}.html"
    body_main = ui.landing_main_content(offer_id)
    body_rest = body_path.read_text(encoding="utf-8")
    footer = ui.build_footer(
        cfg["geo"], ui.footer_tr(cfg["tr"]), page_lang=cfg["lang"]
    )
    head = patch_head(load_head_styles(), offer_id)
    return (
        "<!DOCTYPE html>\n"
        + head
        + "\n<body>\n\n  <!-- Offer #"
        + offer_id
        + " -->\n"
        + body_main
        + "\n"
        + body_rest
        + "\n\n  "
        + footer
        + "\n"
        + ui.tail_scripts(loc)
    )


def build_thank_you(offer_id: str) -> str:
    cfg = ui.OFFERS[offer_id]
    u = ui.ui_strings(cfg["body_locale"])
    geo, slug = cfg["geo"], ui.slug_for(offer_id)
    net = ui._load_net()
    cpa = net.CPA[offer_id]

    html = TY_TEMPLATE.read_text(encoding="utf-8")
    html = re.sub(r'<html lang="[^"]*"', f'<html lang="{cfg["lang"]}"', html, count=1)
    html = re.sub(r"<title>[^<]*</title>", f"<title>{u['ty_title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{u["ty_desc"]}">',
        html,
        count=1,
    )
    html = re.sub(r"GEO: 'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG: 'noventis'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"PRICE: [0-9.]+", f"PRICE: {cfg['price']}", html, count=1)
    html = re.sub(r"CONVERSION_VALUE: [0-9.]+", f"CONVERSION_VALUE: {cpa}", html, count=1)
    html = re.sub(
        r"<h1 class=\"ty-headline\">[^<]*</h1>",
        f'<h1 class="ty-headline">{u["ty_h1"]}</h1>',
        html,
        count=1,
    )
    html = re.sub(
        r'<p class="ty-subhead">[\s\S]*?</p>',
        f'<p class="ty-subhead">{u["ty_sub"]}</p>',
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="ty-action__eyebrow">[^<]*</div>',
        f'<div class="ty-action__eyebrow">{u["ty_action_eyebrow"]}</div>',
        html,
        count=1,
    )
    html = re.sub(
        r'<h2 class="ty-action__title">[^<]*</h2>',
        f'<h2 class="ty-action__title">{u["ty_action_title"]}</h2>',
        html,
        count=1,
    )
    html = re.sub(
        r'<p class="ty-action__body">[\s\S]*?</p>',
        f'<p class="ty-action__body">{u["ty_action_body"]}</p>',
        html,
        count=1,
    )
    html = re.sub(
        r'<p class="ty-action__warning">[\s\S]*?</p>',
        f'<p class="ty-action__warning">{u["ty_action_warn"]}</p>',
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="ty-box__header">🕒[^<]*</div>',
        f'<div class="ty-box__header">{u["ty_hours_title"]}</div>',
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="ty-hours-line">[\s\S]*?</div>',
        f'<div class="ty-hours-line">{u["ty_hours_line"]}</div>',
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="ty-box__header">📋[^<]*</div>',
        f'<div class="ty-box__header">{u["ty_steps_title"]}</div>',
        html,
        count=1,
    )
    steps = (
        f"<li>{u['ty_step1']}</li>"
        f"<li>{u['ty_step2']}</li>"
        f"<li>{u['ty_step3']}</li>"
    )
    html = re.sub(
        r"<ol class=\"ty-steps-list\">[\s\S]*?</ol>",
        f'<ol class="ty-steps-list">{steps}</ol>',
        html,
        count=1,
    )
    badges = (
        f'<span class="ty-trust__badge">{u["ty_badge1"]}</span>'
        f'<span class="ty-trust__badge">{u["ty_badge2"]}</span>'
        f'<span class="ty-trust__badge">{u["ty_badge3"]}</span>'
    )
    html = re.sub(
        r'<div class="ty-trust">[\s\S]*?</div>',
        f'<div class="ty-trust">{badges}</div>',
        html,
        count=1,
    )
    html = re.sub(r"/it/", f"/{geo}/", html)
    html = re.sub(
        r"fbq\('track', 'Purchase', \{\s*value: [0-9.]+,\s*currency: 'EUR'\s*\}\);",
        f"fbq('track', 'Purchase', {{ value: {cpa:.2f}, currency: 'EUR' }});",
        html,
        count=1,
    )
    html = html.replace("Noventis™", "Noventis™").replace("Ultrawatch", "Noventis")
    ty_alt = TY_HERO_ALTS.get(cfg["body_locale"], "homeshopspot.com — order confirmation")
    html = re.sub(r'alt="Il team homeshopspot[^"]*"', f'alt="{ty_alt}"', html, count=1)
    footer = ui.build_footer(
        geo, ui.footer_tr(cfg["tr"]), page_lang=cfg["lang"]
    )
    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>",
        footer.strip(),
        html,
        count=1,
        flags=re.DOTALL,
    )
    return html


def apply_forms() -> None:
    spec = importlib.util.spec_from_file_location(
        "apply", SCRIPTS / "apply_smartwatch_forms.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.main()


def write_index(offer_id: str) -> str:
    cfg = ui.OFFERS[offer_id]
    geo, slug = cfg["geo"], ui.slug_for(offer_id)
    return f"""<!DOCTYPE html>
<html lang="{cfg["lang"]}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/{slug}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/{slug}/landing.html">
<link rel="canonical" href="https://homeshopspot.com/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">Noventis™</a></p>
</body>
</html>
"""


def main() -> None:
    sync_body_files()
    bootstrap_chrome_from_landings()
    for offer_id, cfg in ui.OFFERS.items():
        geo = cfg["geo"]
        slug = ui.slug_for(offer_id)
        out = ROOT / geo / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "landing.html").write_text(build_landing(offer_id), encoding="utf-8", newline="\n")
        (out / "thank-you.html").write_text(
            build_thank_you(offer_id), encoding="utf-8", newline="\n"
        )
        (out / "index.html").write_text(write_index(offer_id), encoding="utf-8", newline="\n")
        print("OK", f"{geo}/{slug}")
    ui.sync_form_snippets()
    apply_forms()
    print("done")


if __name__ == "__main__":
    main()
