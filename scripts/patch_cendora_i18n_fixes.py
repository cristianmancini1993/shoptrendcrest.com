#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off: CENDORA copy fixes (Oct 2026). Run from scripts/."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from _cendora_it_strings import IT_STRINGS

ROOT = Path(__file__).resolve().parents[1]
LOC = ROOT / "content/cendora/locales"

FORM_BLOCKED: dict[str, str] = {
    "it": "Le richieste online per questa offerta sono temporaneamente non disponibili. Scrivi a info@shoptrendcrest.com.",
    "de": "Online-Bestellungen für dieses Angebot sind vorübergehend nicht möglich. Schreiben Sie an info@shoptrendcrest.com.",
    "ro": "Comenzile online pentru această ofertă sunt temporar indisponibile. Scrieți la info@shoptrendcrest.com.",
    "pt": "Os pedidos online para esta oferta estão temporariamente indisponíveis. Escreva para info@shoptrendcrest.com.",
    "sk": "Online objednávky pre túto ponuku sú dočasne nedostupné. Napíšte na info@shoptrendcrest.com.",
    "sl": "Spletna naročila za to ponudbo so začasno nedosegljiva. Pišite na info@shoptrendcrest.com.",
    "hr": "Online narudžbe za ovu ponudu privremeno nisu dostupne. Pišite na info@shoptrendcrest.com.",
    "hu": "Az online rendelés ehhez az ajánlathoz átmenetileg nem elérhető. Írjon az info@shoptrendcrest.com címre.",
    "es": "Los pedidos online de esta oferta no están disponibles temporalmente. Escriba a info@shoptrendcrest.com.",
    "lt": "Šios akcijos užklausos internetu laikinai nepasiekiamos. Rašykite info@shoptrendcrest.com.",
    "pl": "Zamówienia online dla tej oferty są tymczasowo niedostępne. Napisz na info@shoptrendcrest.com.",
    "cs": "Online objednávky pro tuto nabídku jsou dočasně nedostupné. Napište na info@shoptrendcrest.com.",
    "lv": "Šī piedāvājuma pieteikumi tiešsaistē īslaicīgi nav pieejami. Rakstiet uz info@shoptrendcrest.com.",
}

KIT: dict[str, dict[str, str]] = {
    "de": {
        "kit_h": "CENDORA™ — 12 Teile Töpfe und Pfannen, einsatzbereit",
        "kit_li1": "Topf 7 L",
        "kit_li2": "Glasdeckel für Topf 7 L",
        "kit_li3": "Topf 3 L",
        "kit_li4": "Glasdeckel für Topf 3 L",
        "kit_li5": "Kasserolle 1,5 L",
        "kit_li6": "Glasdeckel für Kasserolle 1,5 L",
        "kit_li7": "Bratpfanne 3,5 L mit Stützgriff",
        "kit_li8": "Glasdeckel für Bratpfanne 3,5 L",
        "kit_li9": "Pfanne 20 cm",
        "kit_li10": "Pfanne 28 cm",
        "kit_li11": "Dämpfeinsatz",
        "kit_li12": "Deckel für Dämpfeinsatz",
        "kit_supplement": "Außerdem enthalten: verstärkte Griffe, Bedienungsanleitung und Garantiezertifikat (24 Monate Herstellergarantie).",
    },
    "ro": {
        "kit_h": "Set CENDORA™ — 12 piese de vase, gata de folosit",
        "kit_li1": "Oală 7 L",
        "kit_li2": "Capac din sticlă pentru oala de 7 L",
        "kit_li3": "Oală 3 L",
        "kit_li4": "Capac din sticlă pentru oala de 3 L",
        "kit_li5": "Tigaie 1,5 L",
        "kit_li6": "Capac din sticlă pentru tigaia de 1,5 L",
        "kit_li7": "Tigaie adâncă 3,5 L cu mâner de susținere",
        "kit_li8": "Capac din sticlă pentru tigaia de 3,5 L",
        "kit_li9": "Tigaie 20 cm",
        "kit_li10": "Tigaie 28 cm",
        "kit_li11": "Coș pentru gătire la abur",
        "kit_li12": "Capac pentru coșul de abur",
        "kit_supplement": "Sunt incluse și mânere întărite, broșura de instrucțiuni și certificatul de garanție (garanție producător 24 luni).",
    },
    "pt": {
        "kit_h": "Conjunto CENDORA™ — 12 peças de panelas e frigideiras, pronto a usar",
        "kit_li1": "Panela 7 L",
        "kit_li2": "Tampa de vidro para panela de 7 L",
        "kit_li3": "Panela 3 L",
        "kit_li4": "Tampa de vidro para panela de 3 L",
        "kit_li5": "Caçarola 1,5 L",
        "kit_li6": "Tampa de vidro para caçarola de 1,5 L",
        "kit_li7": "Caçarola funda 3,5 L com pega de apoio",
        "kit_li8": "Tampa de vidro para caçarola de 3,5 L",
        "kit_li9": "Frigideira 20 cm",
        "kit_li10": "Frigideira 28 cm",
        "kit_li11": "Cesto para cozedura a vapor",
        "kit_li12": "Tampa para cesto a vapor",
        "kit_supplement": "Incluem-se ainda pegas reforçadas, manual de instruções e certificado de garantia (garantia de 24 meses).",
    },
    "sk": {
        "kit_h": "Sada CENDORA™ — 12 dielov hrncov a panvíc, pripravená na použitie",
        "kit_li1": "Hrniec 7 l",
        "kit_li2": "Sklenená pokrievka pre hrniec 7 l",
        "kit_li3": "Hrniec 3 l",
        "kit_li4": "Sklenená pokrievka pre hrniec 3 l",
        "kit_li5": "Rondlík 1,5 l",
        "kit_li6": "Sklenená pokrievka pre rondlík 1,5 l",
        "kit_li7": "Panvica 3,5 l s podporným úchytom",
        "kit_li8": "Sklenená pokrievka pre panvicu 3,5 l",
        "kit_li9": "Panvica 20 cm",
        "kit_li10": "Panvica 28 cm",
        "kit_li11": "Kôš na varenie v pare",
        "kit_li12": "Pokrievka pre parný kôš",
        "kit_supplement": "Súčasťou balenia sú aj zosilnené úchyty, návod a záručný certifikát (záruka výrobcu 24 mesiacov).",
    },
    "sl": {
        "kit_h": "Komplet CENDORA™ — 12 delov posode, pripravljen za uporabo",
        "kit_li1": "Lonec 7 L",
        "kit_li2": "Steklen pokrov za lonec 7 L",
        "kit_li3": "Lonec 3 L",
        "kit_li4": "Steklen pokrov za lonec 3 L",
        "kit_li5": "Kozica 1,5 L",
        "kit_li6": "Steklen pokrov za kozico 1,5 L",
        "kit_li7": "Ponev 3,5 L s podpornim ročajem",
        "kit_li8": "Steklen pokrov za ponev 3,5 L",
        "kit_li9": "Ponev 20 cm",
        "kit_li10": "Ponev 28 cm",
        "kit_li11": "Košarica za kuhanje na pari",
        "kit_li12": "Pokrov za parno košarico",
        "kit_supplement": "Priloženi so tudi ojačani ročaji, navodila in garancijski certifikat (24-mesečna garancija proizvajalca).",
    },
    "hr": {
        "kit_h": "Set CENDORA™ — 12 dijelova posuđa, spreman za uporabu",
        "kit_li1": "Lonac 7 l",
        "kit_li2": "Stakleni poklopac za lonac 7 l",
        "kit_li3": "Lonac 3 l",
        "kit_li4": "Stakleni poklopac za lonac 3 l",
        "kit_li5": "Šerpa 1,5 l",
        "kit_li6": "Stakleni poklopac za šerpu 1,5 l",
        "kit_li7": "Duboka tava 3,5 l s pomoćnom ručkom",
        "kit_li8": "Stakleni poklopac za duboku tavu 3,5 l",
        "kit_li9": "Tava 20 cm",
        "kit_li10": "Tava 28 cm",
        "kit_li11": "Košarica za kuhanje na pari",
        "kit_li12": "Poklopac za parnu košaricu",
        "kit_supplement": "Uključene su i ojačane ručke, upute i jamstveni certifikat (jamstvo proizvođača 24 mjeseca).",
    },
    "hu": {
        "kit_h": "CENDORA™ — 12 darabos edény- és serpenyőkészlet, használatra kész",
        "kit_li1": "7 l-es fazék",
        "kit_li2": "Üvegfedő a 7 l-es fazékhoz",
        "kit_li3": "3 l-es fazék",
        "kit_li4": "Üvegfedő a 3 l-es fazékhoz",
        "kit_li5": "1,5 l-es lábas — köretekhez és egyszemélyes adagokhoz",
        "kit_li6": "Üvegfedő az 1,5 l-es lábashoz",
        "kit_li7": "3,5 l-es mély serpenyő tartófogóval",
        "kit_li8": "Üvegfedő a 3,5 l-es serpenyőhöz",
        "kit_li9": "20 cm-es serpenyő",
        "kit_li10": "28 cm-es serpenyő",
        "kit_li11": "Párolókosár",
        "kit_li12": "Fedő a párolókosárhoz",
        "kit_supplement": "A csomag tartalmazza továbbá a megerősített edényfüleket, a használati útmutatót és a garanciajegyet (24 hónap gyártói garancia).",
    },
    "es": {
        "kit_h": "Batería CENDORA™ — 12 piezas de ollas y sartenes, lista para usar",
        "kit_li1": "Olla 7 L",
        "kit_li2": "Tapa de vidrio para olla de 7 L",
        "kit_li3": "Olla 3 L",
        "kit_li4": "Tapa de vidrio para olla de 3 L",
        "kit_li5": "Cacerola 1,5 L",
        "kit_li6": "Tapa de vidrio para cacerola de 1,5 L",
        "kit_li7": "Cazuela 3,5 L con asa de apoyo",
        "kit_li8": "Tapa de vidrio para cazuela de 3,5 L",
        "kit_li9": "Sartén 20 cm",
        "kit_li10": "Sartén 28 cm",
        "kit_li11": "Cesta para cocción al vapor",
        "kit_li12": "Tapa para cesta al vapor",
        "kit_supplement": "También incluye mangos reforzados, folleto de instrucciones y certificado de garantía (garantía de 24 meses).",
    },
    "lt": {
        "kit_h": "CENDORA™ 12 dalių rinkinys — paruoštas naudoti",
        "kit_li1": "7 l puodas",
        "kit_li2": "Stiklo dangtis 7 l puodui",
        "kit_li3": "3 l puodas",
        "kit_li4": "Stiklo dangtis 3 l puodui",
        "kit_li5": "1,5 l kastrulė",
        "kit_li6": "Stiklo dangtis 1,5 l kastrolei",
        "kit_li7": "Gili keptuvė 3,5 l su atramos rankena",
        "kit_li8": "Stiklo dangtis 3,5 l keptuvei",
        "kit_li9": "Keptuvė 20 cm",
        "kit_li10": "Keptuvė 28 cm",
        "kit_li11": "Garų krepšelis",
        "kit_li12": "Dangtis garų krepšeliui",
        "kit_supplement": "Taip pat į komplektą įeina sustiprintos rankenos, instrukcija ir garantijos sertifikatas (24 mėn. gamintojo garantija).",
    },
    "pl": {
        "kit_h": "Zestaw CENDORA™ — 12 elementów garnków i patelni, gotowy do użycia",
        "kit_li1": "Garnek 7 L",
        "kit_li2": "Szklana pokrywka do garnka 7 L",
        "kit_li3": "Garnek 3 L",
        "kit_li4": "Szklana pokrywka do garnka 3 L",
        "kit_li5": "Rondel 1,5 L",
        "kit_li6": "Szklana pokrywka do rondla 1,5 L",
        "kit_li7": "Patelnia głęboka 3,5 L z uchwytem pomocniczym",
        "kit_li8": "Szklana pokrywka do patelni 3,5 L",
        "kit_li9": "Patelnia 20 cm",
        "kit_li10": "Patelnia 28 cm",
        "kit_li11": "Koszyk do gotowania na parze",
        "kit_li12": "Pokrywka do koszyka na parę",
        "kit_supplement": "W zestawie są też wzmocnione uchwyty, instrukcja i certyfikat gwarancji (24 miesiące gwarancji producenta).",
    },
    "cs": {
        "kit_h": "12dílná sada CENDORA™, připravená k okamžitému použití",
        "kit_li1": "Hrnec 7 l",
        "kit_li2": "Skleněná poklice pro hrnec 7 l",
        "kit_li3": "Hrnec 3 l",
        "kit_li4": "Skleněná poklice pro hrnec 3 l",
        "kit_li5": "Rondlík 1,5 l",
        "kit_li6": "Skleněná poklice pro rondlík 1,5 l",
        "kit_li7": "Hluboká pánev 3,5 l s pomocnou rukojetí",
        "kit_li8": "Skleněná poklice pro pánev 3,5 l",
        "kit_li9": "Pánev 20 cm",
        "kit_li10": "Pánev 28 cm",
        "kit_li11": "Pařák",
        "kit_li12": "Poklice pro pařák",
        "kit_supplement": "Součástí balení jsou také zesílené rukojeti, návod a certifikát záruky (záruka výrobce 24 měsíců).",
    },
    "lv": {
        "kit_h": "CENDORA™ 12 gabalu komplekts — gatavs lietošanai",
        "kit_li1": "7 l katls",
        "kit_li2": "Stikla vāks 7 l katlam",
        "kit_li3": "3 l katls",
        "kit_li4": "Stikla vāks 3 l katlam",
        "kit_li5": "1,5 l katls",
        "kit_li6": "Stikla vāks 1,5 l katlam",
        "kit_li7": "Dziļa panna 3,5 l ar atbalsta rokturi",
        "kit_li8": "Stikla vāks 3,5 l pandai",
        "kit_li9": "Panna 20 cm",
        "kit_li10": "Panna 28 cm",
        "kit_li11": "Tvaika grozs",
        "kit_li12": "Vāks tvaika grozam",
        "kit_supplement": "Komplektā arī pastiprināti rokturi, instrukcija un garantijas apliecība (24 mēnešu ražotāja garantija).",
    },
    "it": {
        "kit_h": IT_STRINGS["kit_h"],
        "kit_li1": IT_STRINGS["kit_li1"],
        "kit_li2": IT_STRINGS["kit_li2"],
        "kit_li3": IT_STRINGS["kit_li3"],
        "kit_li4": IT_STRINGS["kit_li4"],
        "kit_li5": IT_STRINGS["kit_li5"],
        "kit_li6": IT_STRINGS["kit_li6"],
        "kit_li7": IT_STRINGS["kit_li7"],
        "kit_li8": IT_STRINGS["kit_li8"],
        "kit_li9": IT_STRINGS["kit_li9"],
        "kit_li10": IT_STRINGS["kit_li10"],
        "kit_li11": IT_STRINGS["kit_li11"],
        "kit_li12": IT_STRINGS["kit_li12"],
        "kit_supplement": IT_STRINGS["kit_supplement"],
    },
}

PATCHES: dict[str, dict[str, Any]] = {
    "lt": {
        "title": "CENDORA™ — Puodų rinkinys su nepridegančia danga, 12 dalių",
        "description": "CENDORA™: 12 dalių rinkinys su nepridegančia danga su akmens efektu, tolygiai įkaistančiu dugnu, tinkamas indukcijai ir indaplovei. Apmokėjimas pristatymo metu Lietuvoje.",
        "og_description": "Neprideganti danga be PTFE ir PFOA: mažiau riebalų, tolygus kepimas, greitas valymas, suderinama su dujomis, stiklo keramika ir indukcija.",
        "h1_desktop": "Su įprastomis nepridegančiomis keptuvėmis iki <span class=\"hl\">9 000 plastiko dalelių</span> gali patekti į artimųjų lėkštę. Apsaugokite šeimą: pereikite prie CENDORA™.",
        "lead": "Neprideganti danga su akmens efektu, be PTFE ir PFOA. Maistas neprilimpa, reikia mažiau aliejaus, šiluma pasiskirsto tolygiai. Suderinama su visomis kaitlentėmis, įskaitant indukciją. Oficiali 24 mėn. garantija.",
        "f3_p": "Neprideganti danga kasdieniam naudojimui",
        "why1_h": "Nepridegantis paviršius, kuriuo maistas slysta be plyšimo",
        "why1_p1": "Aliumininis dugnas tolygiai skleidžia šilumą; neprideganti danga neleidžia kiaušiniams, mėsai ir daržovėms prilipti net vidutinėje ugnyje.",
        "why3_t1": "Neprideganti",
        "cmp_row_adh": "Nepridegančios savybės",
        "cmp_old_care": "Praranda blizgesį",
        "cmp_win_adh": "Neprideganti danga su akmens efektu, ilgaamžė",
        "rev1_p": "«Užauginau tris vaikus ir keičiau puodus ne kartą. Su CENDORA™ kepame tolygiai net mažoje ugnyje ir iš karto nuplaunama. Už kainą kokybė nustebino.»",
        "rev3_h": "Naudoju kasdien ir nesigailiu.",
        "faq4_a": "Taip, iki 230°C — tinka gratinuoti arba baigti kepimą tame pačiame inde.",
        "ty_product": "CENDORA™ — Puodų rinkinys su nepridegančia danga, 12 dalių",
    },
    "cs": {
        "cmp_old_care": "Ztrácí lesk",
        "live": "CENDORA™ si právě prohlíží <strong>{n} lidí</strong>",
        "live0": "CENDORA™ si právě prohlíží <strong>34 lidí</strong>",
        "rev2_p": "«Když přijdou děti a vnoučata, vařím pro mnoho lidí. Objemy jsou praktické, rukojeti působí spolehlivě, poklice dobře sedí. Takovou kvalitu jsem za tuto cenu nečekala.»",
        "why1_p1": "Hliníkové dno rovnoměrně rozkládá teplo po celé ploše; nepřilnavá úprava zabraňuje přichycení vajec, masa a zeleniny i na středním plameni.",
    },
    "hu": {
        "h1_mobile": "Akár <span class=\"hl\">9 000 mikroműanyag-részecske</span> kerülhet az asztalra tálalt ételbe: ideje edényt cserélni.",
        "h1_desktop": "A hétköznapi tapadásmentes serpenyőkkel akár <span class=\"hl\">9 000 műanyag-részecske</span> kerülhet szerettei tányérjára. Védje családját: váltson CENDORA™-ra.",
        "og_description": "Tapadásmentes PTFE és PFOA nélkül: kevesebb zsír, egyenletes főzés, gyors tisztítás, gáz-, üvegkerámia- és indukciós főzőlapokkal kompatibilis.",
        "why2_t3": "Ergonomikus edényfülek",
        "cmp_win_compat": "Gáz, villany, üvegkerámia és indukció",
        "cmp_old_care": "Elveszíti a fényét",
        "rev2_p": "«Ha jönnek a gyerekek és unokák, sok embernek főzök. A kapacitások praktikusak, az edényfülek megbízhatóak, a fedők jól záródnak. Ilyen minőséget nem vártam ezen az áron.»",
        "faq3_a": "Igen. A kompatibilis alj gáz-, villany-, üvegkerámia- és indukciós lapokon is használható.",
    },
    "lv": {
        "title": "CENDORA™ — Trauku komplekts ar nepiedegošu pārklājumu, 12 gabali",
        "description": "CENDORA™: 12 gabalu komplekts ar akmens efekta nepiedegošu pārklājumu, vienmērīgi uzsilstošu pamatni, piemērots indukcijai un trauku mazgājamai. Apmaksa pie piegādes Latvijā.",
        "og_description": "Nepiedegošs pārklājums bez PTFE un PFOA: mazāk tauku, vienmērīga gatavošana, ātra tīrīšana un saderība ar gāzi, stikla keramiku un indukciju.",
        "h1_desktop": "Ar parastajām pannām ar nepiedegošu pārklājumu līdz <span class=\"hl\">9 000 plastmasas daļiņām</span> var nonākt mīļoto ēdienā. Pasargājiet ģimeni: pārejiet uz CENDORA™.",
        "lead": "Akmens efekta nepiedegošs pārklājums, bez PTFE un PFOA. Ēdiens nepielīp, vajag mazāk eļļas, siltums sadalās vienmērīgi. Saderīgs ar visām plītēm, arī indukciju. Oficiāla 24 mēnešu garantija.",
        "f3_p": "Nepiedegošs pārklājums ikdienas lietošanai",
        "why1_h": "Nepiedegoša virsma, pa kuru ēdiens slīd bez plīšanas",
        "why1_t3": "Vienmērīgs siltums",
        "why1_p1": "Alumīnija pamatne vienmērīgi izkliedē siltumu; nepiedegošs pārklājums neļauj olām, gaļai un dārzeņiem pielīpt pat vidējā liesmā.",
        "why2_t3": "Ergonomiski rokturi",
        "why3_t1": "Nepiedegošs",
        "cmp_row_adh": "Nepiedegošas īpašības",
        "cmp_win_adh": "Nepiedegošs pārklājums ar akmens efektu, izturīgs",
        "rev1_p": "«Esmu izaudzinājusi trīs bērnus un vairākkārt mainījusi traukus. Ar CENDORA™ gatavoju vienmērīgi pat mazā liesmā un uzreiz nomazgājas. Par šo cenu kvalitāte pārsteidza.»",
        "rev3_h": "Lietoju katru dienu un nenožēloju.",
        "ty_product": "CENDORA™ — Trauku komplekts ar nepiedegošu pārklājumu, 12 gabali",
    },
    "sl": {
        "h1_mobile": "Do <span class=\"hl\">9.000 delcev mikroplastike</span> lahko pride v hrano na mizi — čas je za novo posodo.",
        "live0": "<strong>34 oseb</strong> si zdaj ogleduje CENDORA™",
        "rev1_p": "«Vzgojila sem tri otroke in večkrat menjala posodo. S CENDORA™ kuham enakomerno tudi na majhnem ognju in operem v trenutku. Za ceno, ki sem jo plačala, me je kakovost presenetila.»",
    },
    "sk": {
        "topbar": "🔥 −50% NA KUCHYNSKÚ SADU — LEN DNES — PLATBA PRI DORUČENÍ · DOPRAVA ZDARMA 🔥",
        "form_note_hero": "🔒 Rýchle doručenie · Platíte kuriérovi · Vrátenie do 30 dní",
        "faq2_a": "Pri doručení odovzdáte kuriérovi {price} v hotovosti.",
        "rev3_h": "Používam denne a neľutujem.",
        "faq5_a": "Máte 30 dní od doručenia na požiadanie o vrátenie tovaru podľa našej refundačnej politiky.",
    },
    "pt": {
        "why1_p1": "O fundo em alumínio distribui o calor por toda a base; o revestimento antiaderente evita que ovos, carne e legumes se colem mesmo em lume médio.",
        "faq2_a": "Paga {price} em numerário ao estafeta quando receber a encomenda.",
    },
    "hr": {
        "description": "CENDORA™: set od 12 dijelova s neprijanjajućim premazom s efektom kamena, ravnomjerno zagrijavanje, prikladno za indukciju i perilicu. Plaćanje pouzećem u Hrvatskoj.",
        "h1_mobile": "Do <span class=\"hl\">9.000 čestica mikroplastike</span> može završiti u hrani na stolu: vrijeme je za novi lonac.",
        "lead": "Neprijanjajući premaz s efektom kamena, bez PTFE i PFOA. Hrana se ne lijepi, treba manje ulja, a toplina se ravnomjerno raspodjeljuje. Kompatibilno sa svim pločama, uključujući indukciju. Službena garancija 24 mjeseca.",
        "why2_p1": "Ojačana podloga kompatibilna je s najčešćim pločama. Sa štednjaka u pećnicu do 230°C bez mijenjanja posude.",
        "cmp_win_adh": "Premaz s efektom kamena, izdržljiv",
    },
    "ro": {
        "rev1_h": "Ani de gătit zilnic: în sfârșit un set care ține piept provocărilor.",
    },
    "pl": {
        "description": "CENDORA™: 12-elementowy zestaw z powłoką nieprzywierającą z efektem kamienia, dnem równomiernie nagrzewającym się, nadającym się do indukcji i zmywarki. Płatność przy odbiorze w Polsce.",
        "lead": "Powłoka nieprzywierająca z efektem kamienia, bez PTFE i PFOA. Jedzenie nie przywiera, potrzebujesz mniej oleju, a ciepło rozkłada się równomiernie. Kompatybilna ze wszystkimi płytami, w tym indukcją. Oficjalna gwarancja 24 miesiące.",
        "why2_h": "Kuchenki gazowe, elektryczne, ceramiczne lub indukcyjne: jeden komplet, bez dodatków",
        "cmp_win_compat": "Kuchenki gazowe, elektryczne, ceramiczne i indukcyjne",
        "faq3_a": "Tak. Kompatybilne dno pasuje do kuchenek gazowych, elektrycznych, ceramicznych i indukcyjnych.",
    },
    "it": {
        "why1_eye": IT_STRINGS["why1_eye"],
        "cmp_win_handle": IT_STRINGS["cmp_win_handle"],
        "rev1_p": IT_STRINGS["rev1_p"],
        "faq2_a": IT_STRINGS["faq2_a"],
        "form_blocked_msg": IT_STRINGS["form_blocked_msg"],
    },
    "es": {
        "faq2_a": "Pagas {price} en efectivo al mensajero cuando recibes el pedido.",
    },
}


def it_to_jsonable() -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in IT_STRINGS.items():
        if isinstance(v, (list, tuple)):
            out[k] = list(v)
        else:
            out[k] = v
    return out


def main() -> None:
    it_json = it_to_jsonable()
    (LOC / "it.json").write_text(
        json.dumps(it_json, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for path in sorted(LOC.glob("*.json")):
        if path.stem == "it":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        stem = path.stem
        if stem in PATCHES:
            data.update(PATCHES[stem])
        if stem in KIT:
            data.update(KIT[stem])
        if stem in FORM_BLOCKED:
            data["form_blocked_msg"] = FORM_BLOCKED[stem]
        # align keys with IT
        for key, val in it_json.items():
            if key not in data:
                data[key] = val
        for key in list(data.keys()):
            if key not in it_json:
                del data[key]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"updated {path.name}")


if __name__ == "__main__":
    main()
