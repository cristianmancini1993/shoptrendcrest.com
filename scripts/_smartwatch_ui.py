# -*- coding: utf-8 -*-
"""Noventis smartwatch landing UI strings, forms, and body rendering."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from string import Formatter

from _ai_image_notice import footer_blurb_column_html
from _smartwatch_locale_sections import LOCALE_OVERRIDES, SECTIONS_IT

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
BODIES_DIR = SCRIPTS / "smartwatch_bodies"
BODY_TEMPLATE = (SCRIPTS / "_smartwatch_body_template.html").read_text(encoding="utf-8")

BRAND = "Noventis"
META_PIXEL = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405442415117529');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405442415117529&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

OFFERS: dict[str, dict] = {
    "586": {
        "geo": "hr",
        "lang": "hr",
        "body_locale": "hr",
        "tr": "hr",
        "price": 64.0,
        "was": "128 €",
        "now": "64 €",
        "currency": "EUR",
    },
    "779": {
        "geo": "si",
        "lang": "sl",
        "body_locale": "sl",
        "tr": "si",
        "price": 59.0,
        "was": "118 €",
        "now": "59 €",
        "currency": "EUR",
    },
    "1633": {
        "geo": "pt",
        "lang": "pt",
        "body_locale": "pt",
        "tr": "pt",
        "price": 66.0,
        "was": "132 €",
        "now": "66 €",
        "currency": "EUR",
    },
    "1636": {
        "geo": "lt",
        "lang": "lt",
        "body_locale": "lt",
        "tr": "lt",
        "price": 54.0,
        "was": "108 €",
        "now": "54 €",
        "currency": "EUR",
    },
    "1842": {
        "geo": "gr",
        "lang": "el",
        "body_locale": "el",
        "tr": "el",
        "price": 69.0,
        "was": "138 €",
        "now": "69 €",
        "currency": "EUR",
    },
    "1843": {
        "geo": "bg",
        "lang": "bg",
        "body_locale": "bg",
        "tr": "bg",
        "price": 69.0,
        "was": "138 €",
        "now": "69 €",
        "currency": "EUR",
    },
    "1844": {
        "geo": "ro",
        "lang": "ro",
        "body_locale": "ro",
        "tr": "ro",
        "price": 339.0,
        "was": "678 lei",
        "now": "339 lei",
        "currency": "RON",
    },
    "2297": {
        "geo": "es",
        "lang": "es",
        "body_locale": "es",
        "tr": "es",
        "price": 59.0,
        "was": "118 €",
        "now": "59 €",
        "currency": "EUR",
    },
    "2934": {
        "geo": "de",
        "lang": "de",
        "body_locale": "de",
        "tr": "de",
        "price": 69.0,
        "was": "138 €",
        "now": "69 €",
        "currency": "EUR",
    },
    "3141": {
        "geo": "pl",
        "lang": "pl",
        "body_locale": "pl",
        "tr": "pl",
        "price": 199.0,
        "was": "398 zł",
        "now": "199 zł",
        "currency": "PLN",
    },
    "3143": {
        "geo": "cz",
        "lang": "cs",
        "body_locale": "cs",
        "tr": "cz",
        "price": 1999.0,
        "was": "3 998 Kč",
        "now": "1 999 Kč",
        "currency": "CZK",
    },
    "3834": {
        "geo": "lv",
        "lang": "lv",
        "body_locale": "lv",
        "tr": "lv",
        "price": 69.0,
        "was": "138 €",
        "now": "69 €",
        "currency": "EUR",
        "lv_kit": True,
    },
}

FOOTER_EXTRA = {
    "el": {
        "footer_blurb": "Χρήσιμα προϊόντα για την καθημερινότητα, παράδοση σε 24–48 ώρες με αντικαταβολή.",
        "info": "Πληροφορίες",
        "about": "Σχετικά με εμάς",
        "contact": "Επικοινωνία",
        "privacy": "Πολιτική απορρήτου",
        "terms": "Όροι χρήσης",
        "cookie": "Πολιτική cookies",
        "ship": "Αποστολές",
        "refund": "Επιστροφές",
        "contacts": "Επικοινωνία",
        "rights": "Όλα τα δικαιώματα διατηρούνται.",
    },
    "bg": {
        "footer_blurb": "Полезни продукти за ежедневието, доставка за 24–48 часа с наложен платеж.",
        "info": "Информация",
        "about": "За нас",
        "contact": "Контакт",
        "privacy": "Политика за поверителност",
        "terms": "Общи условия",
        "cookie": "Политика за бисквитки",
        "ship": "Доставка",
        "refund": "Връщане",
        "contacts": "Контакт",
        "rights": "Всички права запазени.",
    },
}


def _load_net():
    spec = importlib.util.spec_from_file_location(
        "smartwatch_network_forms", SCRIPTS / "smartwatch_network_forms.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _load_chrome(tr_key: str) -> dict:
    spec = importlib.util.spec_from_file_location(
        "gen_yardmax_geos", SCRIPTS / "gen_yardmax_geos.py"
    )
    ym = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(ym)
    chrome = ym.load_chrome()
    if tr_key in chrome and chrome[tr_key].get("footer_blurb"):
        return dict(chrome[tr_key])
    return {}


def footer_tr(tr_key: str) -> dict:
    t = _load_chrome(tr_key)
    if tr_key in FOOTER_EXTRA:
        t.update(FOOTER_EXTRA[tr_key])
    return t


def slug_for(offer_id: str) -> str:
    return f"smartwatch-{offer_id}"


def ui_strings(body_locale: str) -> dict:
    base = dict(SECTIONS_IT)
    base.update(LOCALE_OVERRIDES.get(body_locale, {}))
    return base


def _format_template(template: str, mapping: dict) -> str:
    """Safe format: only replace known {keys}; leave CSS braces alone."""
    fields = {fn for _, fn, _, _ in Formatter().parse(template) if fn}
    data = {k: mapping[k] for k in fields if k in mapping}
    return template.format(**data)


def standard_kit_block(kit: dict, was: str, now: str, cta: str) -> str:
    items = "\n".join(f"          <li>{line}</li>" for line in kit["items"])
    return f"""  <!-- ===== KIT BOX ===== -->
  <section class="kit-section wrap">
    <div class="section-heading">
      <span class="eyebrow">{kit["eyebrow"]}</span>
      <h2>{kit["h2"]}</h2>
    </div>
    <div class="kit-box">
      <img src="/assets/img/products/noventis/hero.webp" alt="{kit["img_alt"]}">
      <div class="kit-content">
        <div class="price-block" style="margin-bottom:16px;">
          <span class="was">{was}</span>
          <span class="now">{now}</span>
          <span class="pct">-50%</span>
        </div>
        <ul>
{items}
        </ul>
        <a href="#order-form" class="cta-btn">{cta}</a>
      </div>
    </div>
  </section>
"""


def lv_kit_block(was: str, now: str, cta: str) -> str:
    return f"""  <!-- ===== KIT BOX ===== -->
  <section class="kit-section wrap">
    <div class="section-heading">
      <span class="eyebrow">Iepakojumā</span>
      <h2>Pilns Noventis™ komplekts, gatavs tūlītējai lietošanai</h2>
    </div>
    <div class="kit-box">
      <img src="/assets/img/products/noventis/hero.webp" alt="Pilns Noventis™ viedpulksteņa komplekts">
      <div class="kit-content">
        <div class="price-block" style="margin-bottom:16px;">
          <span class="was">{was}</span>
          <span class="now">{now}</span>
          <span class="pct">-50%</span>
        </div>
        <ul>
          <li>1 Noventis™ viedpulkstenis ar rūdītu stiklu</li>
          <li>1 Rezerves siksniņa</li>
          <li>1 Magnētiskais lādētājs</li>
          <li>1 Papildu aizsargplēve</li>
          <li>Saderība ar Android un iPhone</li>
          <li>AI skriešanas treneris iekļauts</li>
          <li>Lietošanas instrukcija un garantijas apliecība</li>
          <li>2 gadu garantija iekļauta</li>
        </ul>
        <a href="#order-form" class="cta-btn">{cta}</a>
      </div>
    </div>
  </section>
"""


def render_body_html(body_locale: str, was: str, now: str, lv_kit: bool = False) -> str:
    u = ui_strings(body_locale)
    cta = u["cta"]
    kit = lv_kit_block(was, now, cta) if lv_kit else standard_kit_block(u, was, now, cta)
    mapping = {**u, "kit_block": kit}
    return _format_template(BODY_TEMPLATE, mapping)


def write_body_files() -> None:
    BODIES_DIR.mkdir(parents=True, exist_ok=True)
    for offer_id, cfg in OFFERS.items():
        loc = cfg["body_locale"]
        path = BODIES_DIR / f"{loc}.html"
        html = render_body_html(loc, cfg["was"], cfg["now"], cfg.get("lv_kit", False))
        path.write_text(html, encoding="utf-8", newline="\n")
        print("body", path.name)


def form_html(offer_id: str) -> str:
    net = _load_net()
    cfg = OFFERS[offer_id]
    geo, slug = cfg["geo"], slug_for(offer_id)
    u = ui_strings(cfg["body_locale"])
    cred = net.FORMS[offer_id]
    ty = f"https://homeshopspot.com/{geo}/{slug}/thank-you.html"
    return f"""<form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">{u["form_name_label"]}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{u["form_name_ph"]}" required><br>
        <label for="tel">{u["form_tel_label"]}</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{u["form_tel_ph"]}" required><br>
        <label for="street-address">{u["form_addr_label"]}</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{u["form_addr_ph"]}" required><br>
        <input name="uid" type="hidden" value="{net.UID}" />
        <input name="offer" type="hidden" value="{offer_id}" />
        <input name="lp" type="hidden" value="{cred["lp"]}" />
        <input name="thankyoupage" type="hidden" value="{ty}"/>
        <input name="webhook" type="hidden" value="{net.WEBHOOK}" />
        <input name="_key" type="hidden" value="{cred["key"]}" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">{u["form_submit"]}</button>
        </div>
        <p class="form-note">{u["form_note_bottom"]}</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>"""


def build_footer(geo: str, t: dict, *, page_lang: str) -> str:
    first_col = footer_blurb_column_html(
        t["footer_blurb"], page_lang, show_ai_notice=True
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
{first_col}
      <div>
        <h4 class="site-footer__heading">{t["info"]}</h4>
        <ul class="site-footer__list">
          <li><a href="/{geo}/about-us.html">{t["about"]}</a></li>
          <li><a href="/{geo}/contact-us.html">{t["contact"]}</a></li>
          <li><a href="/{geo}/privacy-policy.html">{t["privacy"]}</a></li>
          <li><a href="/{geo}/terms-conditions.html">{t["terms"]}</a></li>
          <li><a href="/{geo}/cookie-policy.html">{t["cookie"]}</a></li>
          <li><a href="/{geo}/shipping-policy.html">{t["ship"]}</a></li>
          <li><a href="/{geo}/refund-policy.html">{t["refund"]}</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{t["contacts"]}</h4>
        <ul class="site-footer__list">
          <li><strong>Northstar Digital Growth LLC</strong></li>
          <li>32 N Gould St., Sheridan, WY 82801, United States</li>
          <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — {t["rights"]}
      <a href="/">homeshopspot.com</a>
    </div>
  </div>
</footer>
<script>document.querySelectorAll('[data-year]').forEach(function(el){{el.textContent=String(new Date().getFullYear());}});</script>"""


def landing_main_content(offer_id: str) -> str:
    cfg = OFFERS[offer_id]
    u = ui_strings(cfg["body_locale"])
    was, now = cfg["was"], cfg["now"]
    form = form_html(offer_id)
    return f"""
  <div class="topbar">{u["topbar"]}</div>

  <div class="rating-strip wrap">
    <div class="stars">★★★★★</div>
    <div class="rating-text">{u["rating_line"]}</div>
  </div>

  <section class="hero wrap">
    <div class="hero-copy">
      <span class="gift-strip">{u["gift_strip"]}</span>
      <h1 class="h1-mobile-only">{u["h1_mobile"]}</h1>
      <h1 class="h1-desktop-only">{u["h1_desktop"]}</h1>
      <p class="lead">{u["lead"]}</p>
      <div class="hero-image hero-image-mobile-only">
        <img src="/assets/img/products/noventis/hero.webp" alt="{u["hero_alt"]}">
      </div>
      <div class="price-block">
        <span class="was">{was}</span>
        <span class="now">{now}</span>
        <span class="pct">-50%</span>
      </div>
      <a href="#order-form" class="cta-btn">{u["cta"]}</a>
      <p class="form-note">{u["form_note_hero"]}</p>
    </div>
    <div class="hero-image hero-image-desktop-only">
      <img src="/assets/img/products/noventis/hero.webp" alt="{u["hero_alt"]}">
    </div>
  </section>

  <div class="wrap">
    <div class="feature-row">
      <div class="feature-item"><div class="ico">🚚</div><h4>{u["feat1_h"]}</h4><p>{u["feat1_p"]}</p></div>
      <div class="feature-item"><div class="ico">🔒</div><h4>{u["feat2_h"]}</h4><p>{u["feat2_p"]}</p></div>
      <div class="feature-item"><div class="ico">🛡️</div><h4>{u["feat3_h"]}</h4><p>{u["feat3_p"]}</p></div>
      <div class="feature-item"><div class="ico">↩️</div><h4>{u["feat4_h"]}</h4><p>{u["feat4_p"]}</p></div>
    </div>
  </div>

  <section class="order-section" id="order-form">
    <div class="wrap">
      <div class="urgency-strip">
        <div class="countdown-row">
          <div class="countdown-label">{u["timer_label"]}</div>
          <div class="countdown-timer" id="countdownTimer">
            <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">{u["timer_h"]}</div></div>
            <div class="sep">:</div>
            <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">{u["timer_m"]}</div></div>
            <div class="sep">:</div>
            <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">{u["timer_s"]}</div></div>
          </div>
        </div>
        <div class="stock-row">
          <div class="stock-label">
            <span class="left">{u["stock_left"]}</span>
            <span class="right">{u["stock_right"]}</span>
          </div>
          <div class="stock-bar"><div class="stock-bar-fill"></div></div>
        </div>
        <div class="live-row">
          <span class="dot"></span>
          <span id="liveCount">{u["live_count"]}</span>
        </div>
      </div>
      <div class="order-card">
        <h2>{u["order_h2"]}</h2>
        <p>{u["order_p"]}</p>
        {form}
      </div>
    </div>
  </section>
"""


def tail_scripts(body_locale: str) -> str:
    u = ui_strings(body_locale)
    live_js = u["live_count_js"]
    return f"""
<script>
  (function(){{
    const end = Date.now() + 15*60*1000;
    function tick(){{
      const diff = Math.max(0, end - Date.now());
      const h = Math.floor(diff/3600000);
      const m = Math.floor((diff%3600000)/60000);
      const s = Math.floor((diff%60000)/1000);
      document.getElementById('cd-h').textContent = String(h).padStart(2,'0');
      document.getElementById('cd-m').textContent = String(m).padStart(2,'0');
      document.getElementById('cd-s').textContent = String(s).padStart(2,'0');
      if(diff>0) setTimeout(tick,1000);
    }}
    tick();
  }})();

  (function(){{
    let count = 23;
    const el = document.getElementById('liveCount');
    setInterval(()=>{{
      count += (Math.random() > 0.5 ? 1 : -1) * Math.ceil(Math.random()*2);
      count = Math.min(30, Math.max(17, count));
      el.innerHTML = `{live_js}`;
    }}, 2000);
  }})();

  document.querySelectorAll('.faq-item').forEach(item=>{{
    item.querySelector('.faq-q').addEventListener('click', ()=>{{
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
      if(!isOpen) item.classList.add('open');
    }});
  }});
</script>
</body>
</html>
"""


def sync_form_snippets() -> None:
    """Rewrite _smartwatch_form_snippets.py from this module."""
    lines = [
        "# -*- coding: utf-8 -*-",
        '"""Smartwatch order forms (homeshopspot Adrice account)."""',
        "",
        "LANDINGS = {",
    ]
    for oid, cfg in OFFERS.items():
        lines.append(f'    "{oid}": "{cfg["geo"]}/{slug_for(oid)}/landing.html",')
    lines.append("}")
    lines.append("")
    lines.append("FORMS = {")
    for oid in OFFERS:
        form = form_html(oid).replace('class="tm-order-form order-form"', 'class="tm-order-form"')
        lines.append(f'    "{oid}": """{form}""",')
    lines.append("}")
    path = SCRIPTS / "_smartwatch_form_snippets.py"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("synced", path.name)
