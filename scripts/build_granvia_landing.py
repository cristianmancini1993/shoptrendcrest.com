#!/usr/bin/env python3
"""Clone Fortifero MeatForce LP → shoptrendcrest Granvia (IT), full template + PAGE_DATA."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_HTML = ROOT / "scripts" / "_tmp_meatforce.html"
OUT_HTML = ROOT / "it" / "granvia" / "index.html"
IMG_DIR = ROOT / "assets" / "img" / "products" / "granvia"
FORT_BASE = "https://fortifero.com/page/meatforce-pro-1800-es-9myz1/"
IMG_ASSET = "/assets/img/products/granvia"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
TY_URL = "https://shoptrendcrest.com/it/granvia/thank-you.html"

FORM_IFRAME_IT = r"""<style>.kitform-wrap{max-width:520px;margin:0 auto;background:#fff;border:1px solid #e7e9ec;border-radius:18px;padding:28px 24px 22px;box-shadow:0 10px 30px rgba(15,23,42,.06);text-align:left;color:#111}.kitform-title{margin:0 0 8px;text-align:center;font-size:21px;line-height:1.35;font-weight:800;letter-spacing:.3px;text-transform:uppercase;color:#111}.kitform-sub{margin:0 0 22px;text-align:center;font-size:13px;font-weight:600;color:#6b7280}.kitform-sub b{color:#d90429;font-weight:800}.kitform-group{margin-bottom:18px}.kitform-group label{display:block;margin-bottom:8px;font-size:15px;font-weight:800;color:#111}.kitform-group input{width:100%;box-sizing:border-box;min-height:54px;padding:14px 16px;font-size:16px;border:1.5px solid #e3e3dd;border-radius:12px;background:#f8f8f5;color:#111;outline:none;transition:border-color .15s,box-shadow .15s,background .15s}.kitform-group input::placeholder{color:#8a8f98;font-weight:500}.kitform-group input:focus{border-color:#1e8a3a;background:#fff;box-shadow:0 0 0 4px rgba(30,138,58,.14)}.kitform-btn{position:relative;display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:60px;margin-top:26px;padding:16px;border:0;border-radius:12px;background:#1e8a3a;color:#fff;font-size:17px;font-weight:800;letter-spacing:.3px;text-transform:uppercase;cursor:pointer;box-shadow:0 10px 24px rgba(30,138,58,.35);transition:transform .1s,background .15s}.kitform-btn:hover{background:#18752f}.kitform-btn:active{transform:scale(.98)}.kitform-btn.is-sending{opacity:.85;cursor:wait}.kitform-spinner{width:20px;height:20px;border:3px solid rgba(255,255,255,.4);border-top-color:#fff;border-radius:50%;animation:kfspin .8s linear infinite}@keyframes kfspin{to{transform:rotate(360deg)}}.kitform-note{margin:12px 0 0;text-align:center;font-size:12.5px;color:#6b7280}.kitform-trust{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 22px;margin-top:16px;font-size:12.5px;font-weight:600;color:#6b7280}@media(max-width:420px){.kitform-wrap{padding:22px 16px 18px}.kitform-title{font-size:18px}.kitform-btn{font-size:15px}}</style><div class=\"kitform-wrap\"><h3 class=\"kitform-title\">COMPILA IL MODULO E ORDINA GRANVIA™</h3><p class=\"kitform-sub\">Spedizione veloce · Pagamento alla consegna · <b>-40% OGGI</b></p><form id=\"orderForm\" autocomplete=\"on\"><div class=\"kitform-group\"><label for=\"orderName\">Nome e cognome *</label><input id=\"orderName\" type=\"text\" name=\"name\" required autocomplete=\"name\" placeholder=\"Mario Rossi\"></div><div class=\"kitform-group\"><label for=\"orderPhone\">Telefono *</label><input id=\"orderPhone\" type=\"tel\" name=\"phone\" required autocomplete=\"tel\"></div><div class=\"kitform-group\"><label for=\"orderAddress\">Indirizzo di consegna *</label><input id=\"orderAddress\" type=\"text\" name=\"address\" required autocomplete=\"street-address\" placeholder=\"Via Roma 15, 20121 Milano\"></div><button type=\"submit\" class=\"kitform-btn\"><span class=\"kitform-btn-label\">ORDINA ORA – PAGAMENTO ALLA CONSEGNA</span></button></form><p class=\"kitform-note\">Ti richiameremo per confermare l'ordine.</p><div class=\"kitform-trust\"><span>Ordine protetto</span><span>Spedizione veloce</span><span>Reso 30 giorni</span></div></div><script>/* orderForm config */ var LP_FORM_CFG = { webhook: \"""" + WEBHOOK + r"""\" }; if (false) { location.href = \"""" + TY_URL + r"""\"; }<\\/script>"""

PAGE_DATA = {
    "lang": "it",
    "product_name": "Granvia PRO 1800™",
    "meta_description": "Tritacarne elettrico Granvia PRO 1800™ da 1800 W con 3 dischi in acciaio, imbottigliatrice per salsicce e funzione reverse. Hamburger e salumi fatti in casa.",
    "page_title": "Granvia PRO 1800™ — Tritacarne elettrico 1800 W con 3 dischi",
    "hero_title": "Tritacarne elettrico 1800 W, 3 dischi in acciaio per tritatura fine, media e grossa, imbottigliatrice per salsicce, funzione reverse",
    "hero_description": "Prepara a casa carne tritata fresca, hamburger, polpette e salsicce scegliendo tu la carne e le spezie, senza lo sforzo di tritare a mano.",
    "price_new": "89",
    "discount_percent": 40,
    "currency": "€",
    "platform": "adrice",
    "shipping_price": "",
    "shipping_text": "",
    "image_hero": f"{IMG_ASSET}/image_hero.webp",
    "image_content_1": f"{IMG_ASSET}/image_content_1.webp",
    "image_content_2": f"{IMG_ASSET}/image_content_2.webp",
    "image_content_3": f"{IMG_ASSET}/image_content_3.webp",
    "image_advantage": f"{IMG_ASSET}/image_advantage.webp",
    "image_summary": f"{IMG_ASSET}/image_summary.webp",
    "content_main_title": "✅ Perché ti piacerà",
    "content_1_title": "🥩 Carne tritata fresca, come la vuoi tu",
    "content_1_text": "Con Granvia PRO 1800™ scegli tu i tagli di carne da tritare. Decidi quanta magra e quanto grasso mettere in ogni preparazione. Sai esattamente cosa finisce nei tuoi hamburger, nelle polpette o nel ragù. Il motore da <strong>1800 W</strong> lavora in fretta e ti evita lo sforzo di farlo tutto a mano.",
    "content_2_title": "🌭 Salsicce e salumi fatti in casa",
    "content_2_text": "L'accessorio imbottigliatore trasforma la carne tritata in salsicce casalinghe. Scegli la carne, aggiungi sale, pepe e le spezie che preferisci, poi riempi i budelli alimentari con l'accessorio incluso. Con i <strong>3 dischi intercambiabili</strong> (fine, medio e grosso) ottieni la consistenza giusta per ogni ricetta.",
    "content_3_title": "🧼 Comodo da usare e facile da pulire",
    "content_3_text": "La tramoggia superiore ti permette di inserire i pezzi di carne comodamente; lo spintore li guida senza avvicinare le mani al meccanismo. Se la carne si blocca, la funzione reverse aiuta a liberare il meccanismo senza smontare tutto. Al termine, i pezzi si smontano e puoi pulirli con lo spazzolino incluso.",
    "benefits": [
        {"emoji": "⚡", "text": "<strong>Motore da 1800 W</strong> — Trita la carne rapidamente con pochissimo sforzo"},
        {"emoji": "⚙️", "text": "<strong>3 dischi in acciaio</strong> — Tritatura fine, media o grossa per ogni ricetta"},
        {"emoji": "🌭", "text": "<strong>Imbottigliatrice inclusa</strong> — Salsicce casalinghe con le spezie che preferisci"},
        {"emoji": "🔄", "text": "<strong>Funzione reverse</strong> — Sblocca il meccanismo quando la carne si incastra"},
        {"emoji": "🥩", "text": "<strong>Carne a tuo gusto</strong> — Tagli, grasso e ingredienti li decidi tu"},
        {"emoji": "🖐️", "text": "<strong>Uso controllato</strong> — Struttura stabile e spintore per tenere le mani lontane"},
        {"emoji": "🧽", "text": "<strong>Facile da pulire</strong> — Pezzi smontabili e spazzolino incluso"},
    ],
    "summary_items": [
        "Tritacarne elettrico con motore da 1800 W per carne tritata fresca in cucina.",
        "Tre dischi in acciaio per tritatura fine, media o grossa.",
        "Accessorio imbottigliatore per salsicce con carne e spezie a scelta.",
        "Funzione reverse, tramoggia e spintore per un lavoro più comodo.",
        "Kit completo con tramoggia, spintore e spazzolino — niente accessori extra da comprare.",
    ],
    "review_1_name": "Carmela R.",
    "review_1_avatar": "women/44.jpg",
    "review_1_text": "Prima compravo la carne già tritata e ora preparo hamburger e polpette in casa. È velocissima e i tre dischi vanno benissimo per ogni ricetta. Pulirla è semplice con lo spazzolino incluso.",
    "review_2_name": "Giuseppe M.",
    "review_2_avatar": "men/52.jpg",
    "review_2_text": "Ho provato a fare salsicce casalinghe con l'imbottigliatore e la famiglia è entusiasta. Scelgo carne e spezie io. La funzione reverse è utilissima quando qualcosa si blocca.",
    "form_iframe": FORM_IFRAME_IT,
    "comparison": {
        "competitor_label": "Tritacarne base",
        "rows": [
            {"label": "Potenza", "them": "Motore debole o manuale", "us": "Motore da 1800 W"},
            {"label": "Tipi di tritatura", "them": "Un solo tipo", "us": "3 dischi in acciaio"},
            {"label": "Salsicce", "them": "Senza imbottigliatore", "us": "Imbottigliatrice inclusa"},
            {"label": "Blocchi", "them": "Smontare tutto", "us": "Funzione reverse"},
            {"label": "Pulizia", "them": "Pezzi scomodi", "us": "Pezzi smontabili e spazzolino"},
        ],
    },
}


def extract_page_data_blob(html: str) -> tuple[str, str, str]:
    m = re.search(r"(const PAGE_DATA = )\{", html)
    if not m:
        raise SystemExit("PAGE_DATA not found")
    start = m.end() - 1
    depth = 0
    for i, ch in enumerate(html[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return (
                    html[: m.start(1)],
                    m.group(1) + json.dumps(PAGE_DATA, ensure_ascii=False, separators=(",", ":")),
                    html[i + 1 :],
                )
    raise SystemExit("unclosed PAGE_DATA")


def main() -> None:
    if not SRC_HTML.is_file():
        raise SystemExit(f"Missing {SRC_HTML} — download fortifero index first")

    html = SRC_HTML.read_text(encoding="utf-8")
    pre, pdata, post = extract_page_data_blob(html)
    html = pre + pdata + post
    if "const PAGE_DATA = {" not in html:
        raise SystemExit("PAGE_DATA assignment missing after patch")

    html = html.replace("<html>", '<html lang="it">', 1)
    html = re.sub(
        r"window\.LP_CFG = \{[\s\S]*?\};",
        f"""window.LP_CFG = {{
  pixelId:   '',
  tiktokId:  '',
  capi:      '',
  googleAds: 'AW-18510622150',
  consentDefault: '',
  tmfp:      true,
  value:     15,
  currency:  'EUR',
  webhook:   '{WEBHOOK}',
  tyUrl:     '{TY_URL}'
}};""",
        html,
        count=1,
    )

    repl = [
        ("MeatForce PRO 1800™", "Granvia PRO 1800™"),
        ("MeatForce PRO 1800", "Granvia PRO 1800"),
        ("MeatForce", "Granvia"),
        ("meatforce", "granvia"),
        ("fortifero.com", "shoptrendcrest.com"),
        ("info@fortifero.com", "info@shoptrendcrest.com"),
        ("Christafaro Italia S.r.l.", "WHATECH MOBILE CO., LIMITED"),
        ("Via Brescia, 23<br>20063 Cernusco sul Naviglio (MI)", "Room 505, 5th floor, Beverley Commercial Centre<br>87-105 Chatham Road South<br>Tsim Sha Tsui, Kowloon, Hong Kong"),
        ("81643920155", "—"),
    ]
    for a, b in repl:
        html = html.replace(a, b)

    if 'rel="canonical"' not in html:
        html = html.replace(
            '<meta name="viewport"',
            '<link rel="canonical" href="https://shoptrendcrest.com/it/granvia/">\n<meta name="viewport"',
            1,
        )

    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    print("Wrote", OUT_HTML)

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    import urllib.request

    for name in (
        "image_hero.webp",
        "image_content_1.webp",
        "image_content_2.webp",
        "image_content_3.webp",
        "image_advantage.webp",
        "image_summary.webp",
    ):
        dest = IMG_DIR / name
        if dest.is_file() and dest.stat().st_size > 1000:
            continue
        url = FORT_BASE + name
        print("fetch", url)
        urllib.request.urlretrieve(url, dest)


if __name__ == "__main__":
    main()
