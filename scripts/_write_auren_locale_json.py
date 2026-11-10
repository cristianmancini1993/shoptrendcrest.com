#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write AUREN fireplace locale JSON files (one-off bootstrap)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "locales" / "auren_fireplace"

# Shared structure — per-lang overrides in LOCALES
BASE_KEYS = [
    "title", "meta_desc", "og_title", "og_desc", "cookie_text", "cookie_accept", "cookie_learn",
    "topbar", "rating", "gift", "h1_mobile", "h1_desktop", "lead", "alt_hero", "ship_cod",
    "cta_order", "form_note_hero", "f1_h", "f1_p", "f2_h", "f2_p", "f3_h", "f3_p", "f4_h", "f4_p",
    "countdown", "hours", "mins", "secs", "stock_l", "stock_r", "live_tpl", "form_h2", "form_p",
    "label_name", "label_tel", "label_addr", "ph_name", "ph_tel", "ph_addr", "btn_submit", "form_note",
    "alt_w1", "w1_eye", "w1_h", "w1_t1", "w1_t2", "w1_t3", "w1_p", "w1_i",
    "alt_w2", "w2_eye", "w2_h", "w2_t1", "w2_t2", "w2_t3", "w2_p", "w2_i",
    "alt_w3", "w3_eye", "w3_h", "w3_t1", "w3_t2", "w3_t3", "w3_p", "w3_i", "cta_offer",
    "cmp_label", "cmp_h2", "cmp_aria", "th_trad", "th_auren",
    "cmp_r1_l", "cmp_r1_a", "cmp_r1_b", "cmp_r2_l", "cmp_r2_a", "cmp_r2_b",
    "cmp_r3_l", "cmp_r3_a", "cmp_r3_b", "cmp_r4_l", "cmp_r4_a", "cmp_r4_b",
    "cmp_r5_l", "cmp_r5_a", "cmp_r5_b",
    "test_eye", "test_h2", "alt_t1", "t1_h", "t1_p", "t1_auth", "alt_t2", "t2_h", "t2_p", "t2_auth",
    "alt_t3", "t3_h", "t3_p", "t3_auth",
    "kit_eye", "kit_h2", "alt_kit", "kit_i1", "kit_i2", "kit_i3", "kit_i4", "kit_i5", "kit_i6", "kit_i7", "kit_ship", "cta_kit",
    "faq_h2", "faq1_q", "faq1_a", "faq2_q", "faq2_a", "faq3_q", "faq3_a", "faq4_q", "faq4_a",
    "faq5_q", "faq5_a", "faq6_q", "faq6_a", "faq7_q", "faq7_a", "faq8_q", "faq8_a",
    "footer_blurb", "footer_info", "footer_about", "footer_contact", "footer_privacy", "footer_terms",
    "footer_cookie", "footer_shipping", "footer_refund", "footer_contacts", "footer_us",
    "footer_privacy_ty", "footer_terms_ty", "footer_cookie_ty", "footer_shipping_ty", "footer_refund_ty",
    "ty_title", "ty_meta", "ty_h1", "ty_sub", "ty_img_alt", "ty_act_eye", "ty_act_title", "ty_act_body", "ty_act_warn",
    "ty_hours_h", "ty_hours", "ty_steps_h", "ty_s1", "ty_s2", "ty_s3", "ty_b1", "ty_b2", "ty_b3",
]

LOCALES: dict[str, dict] = {}

def L(lang: str, **kwargs: str) -> None:
    LOCALES[lang] = kwargs

# --- PL ---
L("pl",
    title="AUREN™ | Kominek elektryczny LED 3D, do 80 m² | -50% | Polska",
    meta_desc="AUREN™: kominek elektryczny z efektem płomienia LED 3D, szybkie ciepło do 80 m². Aplikacja, pilot i panel. Bez montażu. Wysyłka 24–48 h po potwierdzeniu telefonicznym i pobranie {price}.",
    og_title="AUREN™ | Kominek elektryczny LED 3D | -50%",
    og_desc="Szybkie ogrzewanie, efekt kominka i sterowanie ze smartfona. {price} za pobraniem.",
    cookie_text="Używamy plików cookie technicznych i od podmiotów trzecich, aby poprawić Twoje doświadczenia oraz do analiz.",
    cookie_accept="Akceptuję", cookie_learn="Dowiedz się więcej",
    topbar="🔥 TYLKO DZIŚ: −50% + DARMOWA DOSTAWA · PŁATNOŚĆ ZA POBRANIEM 🔥",
    rating="<strong>4,8/5</strong> · Ponad <strong>8 700</strong> klientów wybrało już kominek elektryczny do salonu",
    gift="🎁 W ZESTAWIE: PILOT + APLIKACJA DO STEROWANIA KOMINKIEM ZE SMARTFONA",
    h1_mobile='<span class="hl">Cieplejszy, przytulniejszy salon</span>, szybkie ciepło bez kotła i remontu.',
    h1_desktop='<span class="hl">Cieplejszy, przytulniejszy salon</span>, szybkie ciepło bez kotła i remontu.',
    lead="<strong>AUREN™</strong> łączy atmosferę prawdziwego ognia z komfortem elektrycznym: moc 2000 W, ciepło do 80 m², 3 poziomy (800 / 1500 / 2000 W) i klasa energetyczna A+++. Płomień LED 3D za ok. 0,20 € dziennie, timer, aplikacja WiFi i pilot. Bez instalatora i pelletu: włącz do gniazdka — salon nagrzewa się w kilka minut.",
    alt_hero="Kominek elektryczny z płomieniem LED 3D, aplikacją i pilotem",
    ship_cod="za pobraniem",
    cta_order="ZAMÓW TERAZ I PŁAĆ PRZY ODBIORZE →",
    form_note_hero="🔒 Bez zaliczki · Bez karty · Płacisz dopiero po otrzymaniu paczki",
    f1_h="Ciepło do 80 m²", f1_p="Odczucie ciepła w kilka minut, bez długiego oczekiwania",
    f2_h="Plug & play", f2_p="Podłącz i używaj od razu, bez fachowca",
    f3_h="Aplikacja · WiFi · pilot", f3_p="Ustaw temperaturę i timer zdalnie",
    f4_h="Wbudowane bezpieczeństwo", f4_p="Automatyczne wyłączenie przy przegrzaniu",
    countdown="⏰ Rabat 50% obowiązuje do wyczerpania zapasów promocyjnych",
    hours="Godz.", mins="Min", secs="Sek",
    stock_l="Dostępność", stock_r="Zostały 3 szt. w cenie promo",
    live_tpl="<strong>{n} osób</strong> ogląda tę promocję właśnie teraz",
    form_h2="Wyślij zapytanie: AUREN™ za {price}", form_p="Podaj imię, telefon i adres: skontaktujemy się, aby potwierdzić dostawę — bez płatności z góry.",
    label_name="Imię i nazwisko*", label_tel="Telefon*", label_addr="Adres*",
    ph_name="Jan Kowalski", ph_tel="+48 512 345 678", ph_addr="ul. Marszałkowska 10/5, 00-590 Warszawa",
    btn_submit="POTWIERDŹ ZAMÓWIENIE", form_note="🔒 Bez zaliczki · Bez karty · Płacisz tylko przy odbiorze",
    alt_w1="Kominek w salonie: ciepło i atmosfera",
    w1_eye="01 · Natychmiastowe ciepło", w1_h="Wyczuwalne ciepło w kilka minut, powierzchnia do 80 m²",
    w1_t1="Minuty", w1_t2="Do 80 m²", w1_t3="Bez instalacji wodnej",
    w1_p="Grzejniki często potrzebują <strong>1–2 godzin</strong>. <strong>AUREN™</strong> nagrzewa w <strong>kilka minut</strong> na <strong>do 80 m²</strong>, bez strat w instalacji centralnej.",
    w1_i="Słabo ocieplone mieszkanie lub dom: jeden kompaktowy element dla większego komfortu.",
    alt_w2="Podłączenie do gniazdka w kilka sekund",
    w2_eye="02 · Bez robót", w2_h="Gniazdko i gotowe, bez montera",
    w2_t1="Tylko gniazdo", w2_t2="Przenośny", w2_t3="Bez komina",
    w2_p="Bez kotła, rur czy komina: <strong>rozpakuj, podłącz i włącz</strong>. Przenosisz tam, gdzie potrzebujesz.",
    w2_i="Z <strong>AUREN™</strong> ograniczasz koszty gazu i montażu, zachowując efekt kominka w salonie.",
    alt_w3="Płomień LED 3D i sterowanie pilotem",
    w3_eye="03 · Płomień i sterowanie", w3_h="2000 W, płomień LED 3D premium",
    w3_t1="2000 W", w3_t2="Aplikacja · WiFi", w3_t3="Pilot IR",
    w3_p="Moc do <strong>2000 W</strong> dla dużych pomieszczeń w bezpieczny sposób. <strong>Płomień LED 3D</strong> także bez grzania: zero dymu, popiołu i drewna. Timer, tryby i temperatura z aplikacji lub pilota IR.",
    w3_i="Efekt płomienia i ciepło osobno: atmosfera kominka przez cały rok.",
    cta_offer="TAK, CHCĘ OFERTĘ →",
    cmp_label="Dlaczego AUREN™ ma sens wobec kotła i pelletu",
    cmp_h2="Centrala i grzejniki vs AUREN™",
    cmp_aria="Porównanie tradycyjnego ogrzewania i kominka elektrycznego AUREN",
    th_trad="Centrala i grzejniki", th_auren="AUREN™",
    cmp_r1_l="Czas do odczucia ciepła", cmp_r1_a="❌ 1–2 godziny", cmp_r1_b="✅ Kilka minut",
    cmp_r2_l="Montaż", cmp_r2_a="❌ Tysiące zł i roboty", cmp_r2_b="✅ Tylko gniazdo",
    cmp_r3_l="Gaz i serwis", cmp_r3_a="❌ Wysokie rachunki i przeglądy", cmp_r3_b="✅ Efektywna energia A+++",
    cmp_r4_l="Atmosfera kominka", cmp_r4_a="❌ Jej nie daje", cmp_r4_b="✅ Regulowany płomień LED 3D",
    cmp_r5_l="Sterowanie", cmp_r5_a="❌ Ręczne grzejniki", cmp_r5_b="✅ Aplikacja · WiFi · pilot IR",
    test_eye="★ 4,8/5 · Zweryfikowany zakup · Moderowane opinie",
    test_h2="Dziesiątki rodzin wybrało AUREN™. Ich wrażenia:",
    alt_t1="Rozpakowanie z pilotem", t1_h="Kompletne opakowanie, wszystko na miejscu",
    t1_p="«Rozpakowałam paczkę — kominek, pilot i instrukcja po polsku. W minutę działał; płaciłam tylko kurierowi, zero zaliczek. Za {price} komplet to okazja, której nie chciałam przegapić.»",
    t1_auth="Elena W., Kraków, Zweryfikowany zakup",
    alt_t2="Lucja z pilotem", t2_h="Bez wycen na pięć zer",
    t2_p="«Pellet i tradycyjny kominek były poza budżetem. Grzeje całą strefę dzienną w rozsądnej cenie; włączam z aplikacji przed powrotem. Bez wycen na tysiące — zamówiłam od razu.»",
    t2_auth="Lucja M., Warszawa, Zweryfikowany zakup",
    alt_t3="Marek w salonie", t3_h="Mniej gazu na rachunku",
    t3_p="«85 m² i wolne grzejniki, gaz zbyt drogi. Za {price} zamiast {was_price} nagrzewa w minuty, efekt płomienia piękny. Zapłacone kurierowi, dostawa w dwa dni — trafiony wybór.»",
    t3_auth="Marek R., Wrocław, Zweryfikowany zakup",
    kit_eye="W paczce", kit_h2="📦 Komplet AUREN™: włącz od pierwszego użycia",
    alt_kit="Kominek elektryczny z aplikacją i pilotem",
    kit_i1="<strong>1× AUREN™</strong> kominek elektryczny 2000 W, klasa energetyczna A+++",
    kit_i2="Pilot IR w zestawie: płomień i ciepło z kanapy",
    kit_i3="Aplikacja z WiFi: sterowanie ze smartfona",
    kit_i4="3 poziomy mocy: 800 / 1500 / 2000 W",
    kit_i5="Regulowany efekt płomienia LED 3D, grzanie opcjonalne",
    kit_i6="Wbudowana ochrona przed przegrzaniem",
    kit_i7="Instrukcja po polsku",
    kit_ship="Darmowa wysyłka 24–48 h robocze po potwierdzeniu telefonicznym · Pobranie · 30 dni satysfakcji lub zwrot",
    cta_kit="ZAMÓW TERAZ →",
    faq_h2="Najczęstsze pytania",
    faq1_q="Jak złożyć zamówienie?", faq1_a="Wypełnij formularz — oddzwonimy, aby ustalić dostawę.",
    faq2_q="Czy mogę płacić przy odbiorze?", faq2_a="Tak. {price} kurierowi przy dostawie — wygodnie i bezpiecznie, bez zaliczki.",
    faq3_q="Ile trwa wysyłka?", faq3_a="Ekspres zwykle <strong>24–48 h robocze</strong> po <strong>telefonicznym potwierdzeniu</strong> zamówienia.",
    faq4_q="Ile m² obejmuje AUREN™?", faq4_a="Do <strong>80 m²</strong> w kilka minut, zależnie od izolacji i wysokości sufitów.",
    faq5_q="Czy potrzebny jest monter?", faq5_a="Nie. Standardowe gniazdo 230 V, bez rur, kanałów i wierceń.",
    faq6_q="Czy mogę używać tylko płomienia bez ciepła?", faq6_a="Tak. <strong>Płomień LED 3D i grzanie są niezależne</strong> — atmosfera przez cały rok.",
    faq7_q="Czy moje dane są chronione?", faq7_a="Tak. Dane przetwarzamy zgodnie z polityką prywatności i przekazujemy tylko kurierowi.",
    faq8_q="Co jeśli nie będę zadowolony?", faq8_a="Masz <strong>30 dni</strong> od dostawy na pełny zwrot oraz gwarancję na wady fabryczne.",
    footer_blurb="Rozwiązania do domu, szybka wysyłka i płatność za pobraniem.",
    footer_info="Informacje", footer_about="O nas", footer_contact="Kontakt",
    footer_privacy="Polityka prywatności", footer_terms="Regulamin",
    footer_cookie="Polityka cookies", footer_shipping="Polityka wysyłki", footer_refund="Polityka zwrotów",
    footer_contacts="Kontakt", footer_us="Stany Zjednoczone",
    footer_privacy_ty="Polityka prywatności", footer_terms_ty="Regulamin",
    footer_cookie_ty="Polityka cookies", footer_shipping_ty="Polityka wysyłki", footer_refund_ty="Polityka zwrotów",
    ty_title="Zamówienie przyjęte — czekaj na telefon potwierdzający | AUREN™",
    ty_meta="Twoje zamówienie AUREN™ zostało przyjęte. Został jeden krok: odebrać telefon od operatora i potwierdzić dane.",
    ty_h1="Twoje zamówienie zostało poprawnie zarejestrowane!",
    ty_sub="Świetnie — zamówienie jest w realizacji. Aby je dokończyć i wysłać paczkę, brakuje tylko <strong>potwierdzenia telefonicznego</strong>.",
    ty_img_alt="Zespół gadgetshifthub: infolinia i logistyka za pobraniem",
    ty_act_eye="👇 Co zrobić teraz", ty_act_title="📞 Odbierz telefon potwierdzający",
    ty_act_body="Operator zadzwoni <strong>w najbliższych godzinach</strong>, aby potwierdzić zamówienie i dostawę.",
    ty_act_warn="Jeśli nie odbierzesz, zamówienie nie zostanie potwierdzone i zostanie anulowane.",
    ty_hours_h="🕒 Godziny kontaktu", ty_hours="<strong>Poniedziałek – sobota</strong> · 9:00 – 18:00",
    ty_steps_h="📋 Co dalej", ty_s1="Odbierz telefon i <strong>potwierdź dane</strong>",
    ty_s2="Zamówienie zostanie przygotowane w <strong>24–48 godzin</strong>",
    ty_s3="Otrzymujesz paczkę i <strong>płacisz przy odbiorze</strong>",
    ty_b1="🔒 Płatność przy odbiorze", ty_b2="🛡️ Gwarancja 24 miesiące", ty_b3="🔐 Ochrona SSL",
)

# Due to length, remaining locales loaded from companion module
from _auren_locale_bodies import CS, ES, PT, DE, HU, SK, LV  # noqa: E402

LOCALES["cs"] = CS
LOCALES["es"] = ES
LOCALES["pt"] = PT
LOCALES["de"] = DE
LOCALES["hu"] = HU
LOCALES["sk"] = SK
LOCALES["lv"] = LV


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for lang, data in LOCALES.items():
        missing = [k for k in BASE_KEYS if k not in data]
        if missing:
            raise SystemExit(f"{lang}: missing keys {missing}")
        path = ROOT / f"{lang}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
