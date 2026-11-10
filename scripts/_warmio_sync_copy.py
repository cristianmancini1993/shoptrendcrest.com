#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch WARMIO locale JSON + IT strings for delivery, warranty, translations."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JSON_DIR = ROOT / "_warmio_json"

# Per-locale product-copy patches (keys in JSON bundles).
PATCHES: dict[str, dict[str, str]] = {
    "it": {
        "f1_p": "Consegna in tutta Italia in 2–4 giorni lavorativi dalla spedizione",
        "faq1_a": "Di solito 2–4 giorni lavorativi dalla spedizione. Dopo l'ordine ti chiamiamo per confermare indirizzo e tempi.",
        "ty2": "Prepariamo il pacco entro <strong>24–48 ore</strong> dalla conferma telefonica",
        "ty3": "Consegna in <strong>2–4 giorni lavorativi</strong> dopo l'invio e <strong>pagamento in contanti al corriere</strong>",
        "form_note_hero": "🔒 Spedizione veloce · Pagamento al corriere · Garanzia 4 anni",
        "form_note_form": "🔒 Paghi al corriere · Garanzia 4 anni",
    },
    "ro": {
        "why2_eye": "02 — Mai puțină umiditate, mai puțin mucegai",
        "why2_t3": "Mai puține bacterii și mai puțini alergeni",
        "cmp_old_air": "Usucă aerul și ridică praful",
        "cta": "COMANDAȚI WARMIO™ →",
        "cta_inline": "COMANDAȚI WARMIO™ →",
        "submit_btn": "Trimiteți comanda",
        "f1_p": "Livrare în toată România în 2–4 zile lucrătoare de la expediere",
        "faq1_a": "De regulă 2–4 zile lucrătoare de la expediere. După comandă vă sunăm pentru adresă și termene.",
        "ty2": "Pregătim coletul în <strong>24–48 de ore</strong> de la confirmarea telefonică",
        "ty3": "Livrare în <strong>2–4 zile lucrătoare</strong> după expediere și <strong>plată cash la curier</strong>",
    },
    "si": {
        "h1_desktop": "TO ZIMO NE VKLOPITE KOTLA: OGREJE VAS V MINUTAH, Z DO 93 % MANJ ENERGIJE.",
        "why2_h": "Zarošena okna zjutraj? To ni rutina — znak, da vlaga zmaguje.",
        "cmp_win_air": "Tristopenjska filtracija HEPA H13",
        "rev1_p": "«Namestila sem ga nad televizor, priključila v električno vtičnico in z daljinskim upravljalnikom nastavim temperaturo, ne da bi vstala. Zvečer pred TV me ne zebe več v hrbet. V primerjavi s prenosnim grelnikom je to druga raven.»",
        "f1_p": "Dostava po Sloveniji v 2–4 delovnih dneh po odpremi",
        "faq1_a": "Običajno 2–4 delovne dni po odpremi. Po naročilu vas pokličemo za naslov in roke.",
        "ty2": "Paket pripravimo v <strong>24–48 urah</strong> po telefonski potrditvi",
        "ty3": "Dostava v <strong>2–4 delovnih dneh</strong> po odpremi in <strong>plačilo po povzetju</strong>",
    },
    "hr": {
        "h1_desktop": "OVE ZIME NE PALITE KOTAO: ZAGRIJAVA VAS ZA MINUTE, S DO 93 % MANJE ENERGIJE.",
        "form_h2": "Pošaljite narudžbu sada, prije nego što nestanu promotivne zalihe",
        "why2_h": "Zamagljena stakla ujutro? To nije rutina — znak je da vlaga pobjeđuje.",
        "why2_p1": "Uz zatvorene prozore vlaga ostaje u zidovima, odjeći i zraku. Idealna razina se sama regulira, smanjujući kondenzaciju, mirise i mrlje u kutovima. Filtri pročišćavaju zrak i zadržavaju mikrobe i alergene.",
        "rev3_h": "U spavaćoj sobi je tiho i ujutro mi više nije hladno.",
        "f1_p": "Dostava u cijeloj Hrvatskoj u 2–4 radna dana nakon otpreme",
        "faq1_a": "Obično 2–4 radna dana nakon otpreme. Nakon narudžbe zovemo za adresu i rokove.",
        "ty2": "Paket pripremamo u <strong>24–48 sati</strong> nakon telefonske potvrde",
        "ty3": "Dostava u <strong>2–4 radna dana</strong> nakon otpreme i <strong>plaćanje pouzećem</strong>",
    },
    "es": {
        "topbar": "🔥 PROMO OTOÑO — SOLO HOY · CONTRA REEMBOLSO · ENVÍO GRATIS 🔥",
        "f4_h": "Contra reembolso",
        "form_note_hero": "🔒 Envío rápido · Pago contra reembolso · Garantía 4 años",
        "form_note_form": "🔒 Pagas contra reembolso · Garantía 4 años",
        "why2_t1": "Deshumidificación automática",
        "ty_pay": "Contra reembolso en la entrega: {price}",
        "f1_p": "Entrega en toda España en 2–4 días laborables desde el envío",
        "faq1_a": "Suele ser 2–4 días laborables desde el envío. Tras el pedido te llamamos para confirmar dirección y plazos.",
        "ty2": "Preparamos el paquete en <strong>24–48 horas</strong> tras la confirmación telefónica",
        "ty3": "Entrega en <strong>2–4 días laborables</strong> tras el envío y <strong>pago en efectivo al mensajero</strong>",
    },
    "pl": {
        "form_note_hero": "🔒 Szybka wysyłka · Płatność kurierowi · 4-letnia gwarancja",
        "form_note_form": "🔒 Płatność kurierowi · 4-letnia gwarancja",
        "f3_h": "4-letnia gwarancja",
        "kit_li6": "Oficjalna 4-letnia gwarancja",
        "description": "Ogrzewa tylko pomieszczenie, którego używasz, obniża wilgotność i oczyszcza powietrze. Gotowe w 5 minut, bez instalatora. Płatność przy odbiorze.",
        "og_description": "Ogrzewa tylko pomieszczenie, którego używasz, obniża wilgotność i oczyszcza powietrze. Gotowe w 5 minut, bez instalatora. Płatność przy odbiorze.",
        "h1_mobile": "Płacisz za centralne ogrzewanie, a mieszkasz w jednym pokoju: od dziś wieczorem możesz przestać marnować.",
        "form_h2": "Złóż zamówienie teraz, zanim skończy się zapas promocyjny",
        "form_p": "Wypełnij pola: wkrótce zadzwonimy, aby potwierdzić dane, zamówienie i dostawę do domu.",
        "cta": "ZAMÓW WARMIO™ →",
        "cta_inline": "ZAMÓW WARMIO™ →",
        "submit_btn": "Zamów teraz",
        "rev2_p": "«Dziś dotarło: urządzenie, instrukcja, kabel i wszystko potrzebne. W salonie na stole, dwie strony czytania i w mniej niż dziesięć minut na ścianie. Solidniejsze i bardziej eleganckie, niż myślałam.»",
        "lead": "Jedno urządzenie na ciepło, osuszanie i czystsze powietrze — bez remontu. Zastępuje grzejnik, osuszacz, oczyszczacz i klimatyzator: taniej niż kupno osobno. Zużywa do 93% mniej energii niż tradycyjne klimatyzatory. Promocyjne sztuki się kończą.",
        "faq2_a": "Przy odbiorze: {price} gotówką kurierowi, gdy otrzymasz paczkę.",
        "faq5_a": "Nie. AI dopasowuje moc do temperatury w pomieszczeniu. W aplikacji możesz zaplanować godziny, gdy jesteś w domu.",
        "f1_p": "Dostawa w całej Polsce w 2–4 dni robocze od wysyłki",
        "faq1_a": "Zwykle 2–4 dni robocze od wysyłki. Po zamówieniu dzwonimy, by potwierdzić adres i terminy.",
        "ty2": "Pakujemy przesyłkę w ciągu <strong>24–48 godzin</strong> po potwierdzeniu telefonicznym",
        "ty3": "Dostawa w <strong>2–4 dni robocze</strong> po wysyłce i <strong>płatność gotówką kurierowi</strong>",
    },
    "sk": {
        "rating": "<strong>4,9/5</strong> — Viac ako <strong>6 500</strong> domácností na Slovensku už kúri s WARMIO™",
        "why2_h": "Zarosené okná ráno? To nie je rutina — je to signál, že vlhkosť víťazí.",
        "form_h2": "Odošlite objednávku teraz, kým sa nevypredajú akciové zásoby",
        "why3_p1": "Pripevníte na stenu, zapojíte do zásuvky — a ide. Koniec prenášania ohrievačov a káblov po podlahe. V lete ten istý prístroj chladí.",
        "f1_p": "Doručenie na celé Slovensko do 2–4 pracovných dní od odoslania",
        "faq1_a": "Zvyčajne 2–4 pracovné dni od odoslania. Po objednávke voláme kvôli adrese a termínom.",
        "ty2": "Balík pripravíme do <strong>24–48 hodín</strong> po telefonickej potvrdení",
        "ty3": "Doručenie do <strong>2–4 pracovných dní</strong> po odoslaní a <strong>platba na dobierku</strong>",
    },
    "lv": {
        "topbar": "🔥 RUDENS AKCIJA — TIKAI ŠODIEN · APMAKSA SAŅEMŠANAS BRĪDĪ · BEZMAKSAS PIEGĀDE 🔥",
        "h1_desktop": "ŠOZIEM NEIESLĒDZIET KATLU: SASILDA JŪS DAŽU MINŪŠU LAIKĀ, PATĒRĒJOT LĪDZ 93 % MAZĀK ENERĢIJAS.",
        "alt_hero_desktop": "WARMIO™ uz sienas, bez ārējā bloka",
        "why3_t2": "Bez ārējā bloka",
        "rev2_p": "«Šodien atnāca: ierīce, ilustrēta rokasgrāmata, kabelis un viss nepieciešamais. Viesistabā uz galda, divas lapas lasīšanas un mazāk nekā desmit minūtēs jau uz sienas. Izturīgāka un elegantāka, nekā domāju.»",
        "why2_p1": "Aizvērtiem logiem mitrums paliek sienās, drēbēs un gaisā. Ideāls līmenis regulējas pats, ierobežojot kondensāciju, smakas un traipus stūros. Filtri attīra gaisu un aiztur mikrobus un alergēnus.",
        "cmp_win_hum": "Automātiska gaisa sausināšana",
        "f1_p": "Piegāde visā Latvijā 2–4 darba dienu laikā pēc nosūtīšanas",
        "faq1_a": "Parasti 2–4 darba dienas pēc nosūtīšanas. Pēc pasūtījuma zvanām, lai apstiprinātu adresi un termiņus.",
        "ty2": "Sagatavojam paku <strong>24–48 stundu</strong> laikā pēc telefona apstiprinājuma",
        "ty3": "Piegāde <strong>2–4 darba dienu</strong> laikā pēc nosūtīšanas un <strong>apmaksa saņemšanas brīdī</strong>",
    },
    "de": {
        "f1_p": "Lieferung in ganz Deutschland in 2–4 Werktagen nach Versand",
        "faq1_a": "In der Regel 2–4 Werktage nach Versand. Nach der Bestellung rufen wir an, um Adresse und Termine zu bestätigen.",
        "ty2": "Wir packen das Paket innerhalb von <strong>24–48 Stunden</strong> nach telefonischer Bestätigung",
        "ty3": "Lieferung in <strong>2–4 Werktagen</strong> nach Versand und <strong>Barzahlung an den Boten</strong>",
        "form_note_hero": "🔒 Schneller Versand · Zahlung beim Boten · 4 Jahre Garantie",
        "form_note_form": "🔒 Zahlung beim Boten · 4 Jahre Garantie",
    },
    "hu": {
        "f1_p": "Szállítás egész Magyarországon 2–4 munkanapon belül a feladást követően",
        "faq1_a": "Általában 2–4 munkanap a feladástól. Rendelés után felhívjuk a szállítási cím és az időpont egyeztetése céljából.",
        "ty2": "A csomagot a telefonos visszaigazolás után <strong>24–48 órán</strong> belül összekészítjük",
        "ty3": "Kiszállítás <strong>2–4 munkanapon</strong> belül a feladás után, <strong>utánvétes fizetés</strong>",
        "f3_h": "4 év garancia",
        "kit_li6": "Hivatalos 4 év garancia",
    },
    "pt": {
        "f1_p": "Entrega em todo Portugal em 2–4 dias úteis após envio",
        "faq1_a": "Normalmente 2–4 dias úteis após envio. Após a encomenda ligamos para confirmar morada e prazos.",
        "ty2": "Preparamos a encomenda em <strong>24–48 horas</strong> após confirmação telefónica",
        "ty3": "Entrega em <strong>2–4 dias úteis</strong> após envio e <strong>pagamento à cobrança</strong>",
    },
    "cs": {
        "f1_p": "Doručení v celé ČR do 2–4 pracovních dnů od odeslání",
        "faq1_a": "Obvykle 2–4 pracovní dny od odeslání. Po objednávce voláme kvůli adrese a termínům.",
        "ty2": "Balíček připravíme do <strong>24–48 hodin</strong> po telefonickém potvrzení",
        "ty3": "Doručení do <strong>2–4 pracovních dnů</strong> po odeslání a <strong>platba na dobírku</strong>",
    },
    "lt": {
        "why1_t3": "Tolygus šilumos paskirstymas",
        "why2_p1": "Uždarius langus drėgmė lieka sienose, drabužiuose ir ore. Idealus lygis reguliuojasi pats, ribodamas kondensaciją, kvapus ir dėmes kampuose. Filtrai valo orą ir sulaiko mikrobus bei alergenus.",
        "rev2_p": "«Šiandien atėjo: prietaisas, iliustruotas vadovas, laidas ir viskas reikalinga. Svetainėje ant stalo, du puslapiai skaitymo ir per mažiau nei dešimt minučių ant sienos. Tvirtesnis ir elegantiškesnis nei galvojau.»",
        "kit_li2": "Nuotolinio valdymo pultelis komplekte",
        "form_h2": "Pateikite užsakymą dabar, kol dar yra akcinių prekių",
        "f1_p": "Pristatymas visoje Lietuvoje per 2–4 darbo dienas nuo išsiuntimo",
        "faq1_a": "Paprastai 2–4 darbo dienos nuo išsiuntimo. Po užsakymo skambiname patvirtinti adresą ir terminus.",
        "ty2": "Paketą paruošiame per <strong>24–48 valandas</strong> po telefono patvirtinimo",
        "ty3": "Pristatymas per <strong>2–4 darbo dienas</strong> po išsiuntimo ir <strong>mokėjimas pristatymo metu</strong>",
    },
}

DELIVERY_DEFAULTS = {
    "f1_p": "Delivery in 2–4 business days after dispatch",
    "faq1_a": "Usually 2–4 business days after dispatch. We call after your order to confirm address and timing.",
    "ty2": "We prepare your parcel within <strong>24–48 hours</strong> after phone confirmation",
    "ty3": "Delivery in <strong>2–4 business days</strong> after dispatch and <strong>cash on delivery</strong>",
}


def patch_json(lang: str, data: dict) -> dict:
    if lang in PATCHES:
        data.update(PATCHES[lang])
    return data


def main() -> None:
    for path in sorted(JSON_DIR.glob("*.json")):
        lang = path.stem
        data = json.loads(path.read_text(encoding="utf-8"))
        data = patch_json(lang, data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
        print(f"Patched {path.name}")


if __name__ == "__main__":
    main()
