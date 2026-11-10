#!/usr/bin/env python3
"""Apply forms, kit lines, and translation fixes to LUNO geo pages."""

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "patches", Path(__file__).with_name("_luno_content_patches.py")
)
patches = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(patches)

OFFER_CFG = {
    "1912": {"lang": "de", "price": 92.0, "currency": "EUR"},
    "1915": {"lang": "hu", "price": 29999.0, "currency": "HUF"},
    "2480": {"lang": "pt", "price": 79.0, "currency": "EUR"},
    "3163": {"lang": "es", "price": 79.0, "currency": "EUR"},
    "3167": {"lang": "pl", "price": 339.0, "currency": "PLN"},
    "3169": {"lang": "cs", "price": 1899.0, "currency": "CZK"},
    "3910": {"lang": "lv", "price": 85.0, "currency": "EUR"},
    "4321": {"lang": "sk", "price": 74.0, "currency": "EUR"},
}

KIT_TEXT_FIX = (
    ("1× Vyztužené ramínka", "1× Vyztužená ramínka"),
    ("1× Vyztužené vešiaky", "1× Vystužené vešiaky"),
)


def append_kit_items(html: str, extra: str) -> str:
    if extra.strip() in html:
        return html
    return re.sub(
        r"(<section class=\"kit-section wrap\">[\s\S]*?<ul>[\s\S]*?)(        </ul>)",
        lambda m: m.group(1) + extra + "\n" + m.group(2),
        html,
        count=1,
    )


def apply_replacements(html: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in sorted(pairs, key=lambda p: -len(p[0])):
        html = html.replace(old, new)
    return html


def patch_landing(rel: str, lang: str, timing) -> None:
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    pairs = list(patches.LANDING_REPLACEMENTS.get(rel, []))
    pairs.extend(patches.LANG_WIDE_REPLACEMENTS.get(lang, []))
    pairs.extend(KIT_TEXT_FIX)
    html = apply_replacements(html, pairs)
    html = append_kit_items(html, patches.KIT_APPEND[lang])
    html = timing.patch_footer_blurb(html, lang)
    path.write_text(html, encoding="utf-8", newline="\n")


def patch_thank_you(geo_slug: str, lang: str, price_s: str, timing) -> None:
    path = ROOT / geo_slug / "thank-you.html"
    html = path.read_text(encoding="utf-8")
    html = timing.patch_footer_blurb(html, lang)
    html = timing.patch_ty_step3(html, lang, price_s)
    path.write_text(html, encoding="utf-8", newline="\n")


def patch_it_source() -> None:
    path = ROOT / "it" / "luno" / "landing.html"
    html = path.read_text(encoding="utf-8")
    html = append_kit_items(html, patches.IT_KIT_APPEND)
    # Form order: name → tel → address (IT placeholders)
    form = """<form class="cod-form tm-order-form order-form">
          <label for="name">Nome e cognome*</label>
          <input id="name" class="cod-form__input" type="text" name="name" autocomplete="name" placeholder="Mario Rossi" required><br>
          <label for="tel">Numero di telefono*</label>
          <input id="tel" class="cod-form__input" type="tel" name="tel" autocomplete="tel" placeholder="+39 312 345 6789" required><br>
          <label for="street-address">Indirizzo di consegna*</label>
          <input id="street-address" class="cod-form__input" type="text" name="street-address" autocomplete="street-address" placeholder="Via Roma 45, Interno 12, 00100 Roma" required><br>

          <input name="subid" type="hidden" value="">
          <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/it/luno/thank-you.html">
          <div style="margin-top:10px;text-align:center">
            <button name="submit" type="submit">INVIA LA RICHIESTA</button>
          </div>
          <p class="form-note">🔒 Nessun anticipo · Nessuna carta · Paghi al corriere</p>
        </form>"""
    html = re.sub(
        r'<form class="cod-form tm-order-form order-form">[\s\S]*?</form>',
        form,
        html,
        count=1,
    )
    path.write_text(html, encoding="utf-8", newline="\n")


def main() -> None:
    apply = Path(__file__).with_name("apply_luno_forms.py")
    subprocess.run([sys.executable, str(apply)], check=True)

    snip_spec = importlib.util.spec_from_file_location(
        "snip", Path(__file__).with_name("_luno_form_snippets.py")
    )
    snip = importlib.util.module_from_spec(snip_spec)
    assert snip_spec.loader is not None
    snip_spec.loader.exec_module(snip)

    gen_spec = importlib.util.spec_from_file_location(
        "gen", Path(__file__).with_name("gen_luno_geos.py")
    )
    gen = importlib.util.module_from_spec(gen_spec)
    assert gen_spec.loader is not None
    gen_spec.loader.exec_module(gen)

    timing_spec = importlib.util.spec_from_file_location(
        "timing", Path(__file__).with_name("_luno_timing.py")
    )
    timing = importlib.util.module_from_spec(timing_spec)
    assert timing_spec.loader is not None
    timing_spec.loader.exec_module(timing)

    for offer_id, rel in snip.LANDINGS.items():
        cfg = OFFER_CFG[offer_id]
        lang = cfg["lang"]
        price_s = gen.fmt_price(cfg["price"], cfg["currency"])
        patch_landing(rel, lang, timing)
        geo_slug = rel.rsplit("/", 1)[0]
        patch_thank_you(geo_slug, lang, price_s, timing)
        print("PATCH", rel, "+ thank-you")

    patch_it_source()
    print("PATCH it/luno/landing.html")


if __name__ == "__main__":
    main()
