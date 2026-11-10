#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix remaining mixed-language strings in _trimex_locale_patches.py."""
from __future__ import annotations

import copy
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATCHES_PATH = ROOT / "_trimex_locale_patches.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def apply_replacements(text: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        text = text.replace(old, new)
    return text


def fix_cs(cs: dict) -> None:
    fixes = {
        "w1_t2": "Ocelové nože v balení",
        "w2_h": "Dvě baterie a jen 2 kg: dokončíte práci bez bolesti zad",
        "alt_w2": "Rychlá výměna baterie v křovinořezu TRIMEX™",
        "cmp_r2_b": "Jen 2 kg, lehký a vyvážený",
        "cmp_r5_a": "Startovací lanko opakovaně",
        "cmp_r7_b": "Kompletní sada + záruka 2 roky",
        "kit_i4": "Ocelové nože — trní, keře a větvičky",
        "kit_i5": "Plastové nože — tráva a okraje trávníku",
        "faq4_q": "Řeže i tvrdé trní a plevel?",
        "alt_t3": "Starší muž používá křovinořez TRIMEX™ na zahradě",
    }
    cs.update(fixes)


def cs_to_sk(cs: dict) -> dict:
    sk = copy.deepcopy(cs)
    pairs = [
        ("křovinořez", "krovinorez"),
        ("Křovinořez", "Krovinorez"),
        ("řeže", "reže"),
        ("Řeže", "Reže"),
        ("řežete", "režete"),
        ("řezání", "rezanie"),
        ("záhonů", "záhonov"),
        ("záhonů", "záhonov"),
        ("kapky", "kvapky"),
        ("kapku", "kvapku"),
        ("láhev", "fľaša"),
        ("2litrová", "2-litrová"),
        ("CHCI", "CHCEM"),
        ("zahradu", "záhradu"),
        ("zahradě", "záhrade"),
        ("Zahradu", "Záhradu"),
        ("Praha", "Bratislava"),
        ("Brno", "Košice"),
        ("ověřený", "overený"),
        ("nákup", "nákup"),
        ("při převzetí", "pri prevzatí"),
        ("Při převzetí", "Pri prevzatí"),
        ("připravený", "pripravený"),
        ("Kompletní", "Kompletná"),
        ("kompletní", "kompletná"),
        ("sada", "sada"),
        ("Jen ", "Len "),
        ("jen ", "len "),
        ("Zbývá", "Zostáva"),
        ("právě", "práve"),
        ("prohlíží", "pozerá"),
        ("nejtvrdší", "najtvrdší"),
        ("námahy", "námahy"),
        ("vyvážený", "vyvážený"),
        ("Doručení po celé České republice", "Doručenie po celom Slovensku"),
        ("Jan Novák", "Ján Novák"),
        ("Václavské náměstí 10, Praha", "Hlavná 15, Bratislava"),
    ]
    for key, val in list(sk.items()):
        if not isinstance(val, str):
            continue
        if key in ("title", "description", "topbar"):
            continue
        sk[key] = apply_replacements(val, pairs)
    sk["title"] = "TRIMEX™ — Akumulátorový krovinorez bez benzínu | -50% dnes"
    sk["description"] = (
        "Krovinorez TRIMEX™ s motorom 2880 W, 2 batérie 60 W v balení a len 2 kg. "
        "Bez benzínu, dymu a káblov. Platba pri prevzatí."
    )
    sk["topbar"] = "🔥 LEN DNES: -50% NA TRIMEX™ + 2 BATÉRIE 60 W V BALENÍ 🔥"
    sk["f1_p"] = "Doručenie po celom Slovensku"
    sk["ph_name"] = "Ján Novák"
    sk["ph_addr"] = "Hlavná 15, Bratislava"
    sk.update(
        {
            "w3_eye": "03 — TRIMEX™: Ticho a pripravený hneď po rozbalení",
            "cmp_r1_l": "Napájanie",
            "cmp_r1_a": "Benzín a zmes na kúpu",
            "cmp_r1_b": "Akumulátor, žiadne palivo",
            "cmp_r2_l": "Hmotnosť",
            "cmp_r2_a": "Ťažký, unavuje ramená a chrbát",
            "cmp_r2_b": "Len 2 kg, ľahký a vyvážený",
            "cmp_r3_l": "Hluk",
            "cmp_r3_a": "Ohlušujúci, ruší susedov",
            "cmp_r3_b": "Tichý",
            "cmp_r4_l": "Dym a zápach",
            "cmp_r4_a": "Výfukové plyny a zápach benzínu",
            "cmp_r4_b": "Bez emisií",
            "cmp_r5_l": "Štart",
            "cmp_r5_a": "Štartovacie lanko opakovane",
            "cmp_r5_b": "Spustenie jedným tlačidlom",
            "cmp_r6_l": "Výdrž",
            "cmp_r6_a": "Prestávky na tankovanie",
            "cmp_r6_b": "2 batérie 60 W, výmena počas sekúnd",
            "cmp_r7_l": "Nákup",
            "cmp_r7_a": "Príslušenstvo často osobno",
            "cmp_r7_b": "Kompletná sada + záruka 2 roky",
        }
    )
    return sk


def cs_to_sl(cs: dict) -> dict:
    sl = copy.deepcopy(cs)
    pairs = [
        ("křovinořez", "trimer"),
        ("Křovinořez", "Trimer"),
        ("řeže", "reže"),
        ("Řeže", "Reže"),
        ("řežete", "režete"),
        ("bez benzínu", "brez bencina"),
        ("Benzínu", "bencina"),
        ("benzínu", "bencina"),
        ("Benzín", "Bencin"),
        ("benzínu", "bencina"),
        ("kapky", "kapljice"),
        ("kapku", "kapljico"),
        ("láhev vody", "steklenica vode"),
        ("Lehký jako", "Lahka kot"),
        ("CHCI", "ŽELIM"),
        ("zahradu", "vrt"),
        ("zahradě", "vrtu"),
        ("Zahradu", "Vrt"),
        ("plotu", "ograje"),
        ("stromů", "dreves"),
        ("záhonů", "gredic"),
        ("sekačka", "kosilnica"),
        ("Záruka", "Garancija"),
        ("Praha", "Ljubljana"),
        ("Brno", "Maribor"),
        ("ověřený nákup", "preverjen nakup"),
        ("Motor", "Motor"),
        ("Jen 2 kg", "Samo 2 kg"),
        ("Jen ", "Samo "),
        ("jen ", "samo "),
        ("Zbývá", "Na zalogi je le še"),
        ("kusů skladem", "nekaj kosov"),
        ("právě prohlíží", "si ogleduje"),
        ("sousedy", "sosede"),
        ("Můžete pracovat na zahradě", "Lahko delate na vrtu"),
        ("neděli ráno", "nedeljsko jutro"),
        ("Kompletní sada", "Poln komplet"),
        ("kompletní sada", "poln komplet"),
        ("Přímé srovnání", "Neposredna primerjava"),
        ("Doručení po celé České republice", "Dostava po vsej Sloveniji"),
        ("Jan Novák", "Janez Novak"),
        ("Václavské náměstí 10, Praha", "Slovenska cesta 15, Ljubljana"),
        ("Platba při převzetí", "Plačilo ob prevzemu"),
        ("bezkartáčový", "brezžični"),
        ("v balení", "v kompletu"),
        ("ocelové", "jeklena"),
        ("Ocelové", "Jeklena"),
        ("plastové", "plastična"),
        ("Plastové", "Plastična"),
        ("nože", "rezila"),
        ("Nože", "Rezila"),
        ("trávníku", "trate"),
        ("trávu", "travo"),
        ("tráva", "trava"),
        ("plevel", "plevel"),
        ("trní", "trnje"),
        ("keře", "grmovje"),
        ("větvičky", "vejice"),
    ]
    for key, val in list(sl.items()):
        if not isinstance(val, str):
            continue
        if key in ("title", "description", "topbar"):
            continue
        sl[key] = apply_replacements(val, pairs)
    sl["title"] = "TRIMEX™ — Akumulatorski trimer brez bencina | -50% danes"
    sl["description"] = (
        "Trimer TRIMEX™ z motorjem 2880 W, 2 bateriji 60 W v kompletu in samo 2 kg. "
        "Brez bencina, dima in kablov. Plačilo ob prevzemu."
    )
    sl["topbar"] = "🔥 SAMO DANES: -50% NA TRIMEX™ + 2 BATERIJI 60 W V KOMPLETU 🔥"
    sl["lead"] = (
        "<strong>TRIMEX™</strong> — brezžični motor 2880 W in 2 bateriji 60 W v kompletu. "
        "Reže tam, kjer kosilnica ne pride: po ograji, okoli dreves in gredic. Garancija 2 leti."
    )
    sl["h1_m"] = (
        "Lahka kot 2-litrsna steklenica vode, a reže trnje, plevel in grmovje brez kapljice bencina."
    )
    sl["f3_p"] = "Zmogljiv motor in trdni materiali"
    sl["stock_r"] = "Na zalogi je le še nekaj kosov"
    sl["live_tpl"] = "<strong>{n} oseb</strong> si ogleduje TRIMEX™ prav zdaj"
    sl["w1_eye"] = "01 — TRIMEX™: Moč za najtrdovratnejši plevel, brez bencina"
    sl["w1_h"] = "Visoka trava, trnje, plevel in vejice: vse rezate brez napora"
    sl["w1_t3"] = "Brez bencina in dima"
    sl["w1_i"] = "Vrt urejate hitreje – brez trganja in dima."
    sl["w2_h"] = "Dve bateriji in samo 2 kg: končate brez bolečin v hrbtu"
    sl["w2_t3"] = "Nastavljiv ročaj"
    sl["w2_p"] = (
        "Ko se baterija izprazni, jo zamenjate v nekaj sekundah in nadaljujete. TRIMEX™ je lahek in "
        "uravnotežen, teleskopski ročaj se nastavi do 2 metrov, protizdrsni ročaj zmanjšuje vibracije – "
        "roke, ramena in hrbet ne trpijo niti po več urah."
    )
    sl["w2_i"] = "Več opravljenega, manj utrujenosti. Idealno tudi, če nimate več toliko moči."
    sl["w3_h"] = "Brez glasnega hrupa, brez dodatne opreme"
    sl["w3_t1"] = "Tiho delovanje"
    sl["w3_t3"] = "Montaža v nekaj minutah"
    sl["w3_p"] = (
        "Lahko delate na vrtu tudi v nedeljsko jutro, ne da bi motili sosede. V škatli je vse: baterije, "
        "polnilnik, jeklena in plastična rezila, rezni disk in montažno orodje. Odprete, sestavite v nekaj "
        "minutah – in ste na vrtu."
    )
    sl["w3_i"] = "Brez presenečenj in dodatnih stroškov – samo urejen vrt."
    sl["cmp_h2"] = "Bencinski trimer ali TRIMEX™? Poglejte razliko"
    sl["cmp_aria"] = "Primerjava bencinskega trimerja in TRIMEX"
    sl["test_h2"] = "Tisoče strank je izbralo TRIMEX™ za svoj vrt"
    sl["t2_h"] = "Rezervna baterija naredi razliko."
    sl["t2_p"] = (
        "«Imam veliko parcelo, visoka trava ob ograji je bila nočna mora. Ko prva baterija ugasne, v nekaj "
        "sekundah vstavim drugo in nadaljujem. Končno vse končam na enkrat.»"
    )
    sl["t3_h"] = "Kupila sem staršem v dar."
    sl["t3_p"] = (
        "«Oče ima 72 let in nisem ga več hotela videti s bencinskim trimerjem na hrbtu. Ta je lahek, "
        "takoj zažene, ročaj se dobro nastavi. Zdaj ga uporablja sam brez težav.»"
    )
    sl["kit_h2"] = "Poln komplet TRIMEX™, pripravljen za vaš vrt"
    sl["kit_i3"] = "Hitri polnilnik"
    sl["kit_i8"] = "Montažno orodje in navodila"
    sl["kit_i9"] = "Uradna 2-letna garancija"
    sl["faq1_a"] = "Po telefonski potrditvi naročila paket prispe v 24–48 delovnih urah."
    sl["faq2_a"] = "Plačate neposredno dostavljalcu ob prevzemu. Brez predplačila in podatkov o kartici."
    sl["faq3_q"] = "Kako dolgo traja baterija?"
    sl["faq4_q"] = "Ali reže trdovratno trnje in plevel?"
    sl["faq5_q"] = "Ali je težek? Ali ga lahko uporablja starejša oseba?"
    sl["faq5_a"] = (
        "Tehta le 2 kg in je dobro uravnotežen. Nastavljiv ročaj in protizdrsni ročaj olajšata delo, "
        "tudi če imate manj moči."
    )
    sl["faq6_q"] = "Kaj če mi ne ustreza?"
    sl["faq6_a"] = "Imate 30 dni za vračilo. Obrnite se na podporo strankam – vodimo vas korak za korakom."
    sl["ty_title"] = "Naročilo sprejeto — počakajte na potrditveni klic | TRIMEX™"
    sl["f1_p"] = "Dostava po vsej Sloveniji"
    sl["ph_name"] = "Janez Novak"
    sl["ph_addr"] = "Slovenska cesta 15, Ljubljana"
    sl.update(
        {
            "w3_eye": "03 — TRIMEX™: Tiše in pripravljen takoj po razpakiranju",
            "alt_w3": "Poln komplet TRIMEX™ pripravljen takoj po odprtju",
            "cmp_r1_l": "Napajanje",
            "cmp_r1_a": "Bencin in mešanica za nakup",
            "cmp_r1_b": "Akumulator, brez goriva",
            "cmp_r2_l": "Teža",
            "cmp_r2_a": "Težek, utruja ramena in hrbet",
            "cmp_r2_b": "Samo 2 kg, lahek in uravnotežen",
            "cmp_r3_l": "Hrup",
            "cmp_r3_a": "Oglašujoč, moti sosede",
            "cmp_r3_b": "Tiho",
            "cmp_r4_l": "Dim in vonj",
            "cmp_r4_a": "Izpuhni plini in vonj bencina",
            "cmp_r4_b": "Brez emisij",
            "cmp_r5_l": "Zagon",
            "cmp_r5_a": "Starter večkrat potegniti",
            "cmp_r5_b": "Vklop z enim gumbom",
            "cmp_r6_l": "Delovni čas",
            "cmp_r6_a": "Pavze za polnjenje",
            "cmp_r6_b": "2 bateriji 60 W, menjava v sekundah",
            "cmp_r7_l": "Nakup",
            "cmp_r7_a": "Dodatna oprema pogosto posebej",
            "cmp_r7_b": "Poln komplet + 2-letna garancija",
            "t1_h": "Izgledalo je kot igrača – dokler nisem preizkusil.",
            "t1_p": (
                "«Po razpakiranju sem bil skeptičen: tako lahek, v primerjavi s starim bencinskim, je izgledal kot "
                "igrača. Potem sem ga preizkusil na trnju in vejah nad centimeter – rezal brez težav.»"
            ),
            "t1_auth": "Marco T. — Ljubljana, preverjen nakup",
            "t2_auth": "Giuseppe L. — Maribor, preverjen nakup",
            "t3_auth": "Francesca D. — Ljubljana, preverjen nakup",
            "alt_t1": "Trimer TRIMEX™ po rezani trnja na vrtu",
            "alt_t2": "Visoka trava ob ograji pokošana s TRIMEX™",
            "alt_t3": "Starejši moški uporablja trimer TRIMEX™ na vrtu",
            "kit_i1": "Trimer TRIMEX™ z motorjem 2880 W",
            "kit_i2": "2 bateriji 60 W — delo brez prekinitev",
            "kit_i6": "Rezni disk — gosta rastlinje",
            "kit_i7": "Teleskopski ročaj s protizdrsnim ročajem",
        }
    )
    return sl


def cs_to_hr(cs: dict) -> dict:
    hr = copy.deepcopy(cs)
    pairs = [
        ("křovinořez", "trimer"),
        ("Křovinořez", "Trimer"),
        ("řeže", "reže"),
        ("Řeže", "Reže"),
        ("řežete", "režete"),
        ("bez benzínu", "bez benzina"),
        ("Benzínu", "benzina"),
        ("benzínu", "benzina"),
        ("Benzín", "Benzin"),
        ("kapky", "kapi"),
        ("kapku", "kap"),
        ("láhev vody", "boca vode"),
        ("Lehký jako", "Lagan kao"),
        ("CHCI", "ŽELIM"),
        ("zahradu", "vrt"),
        ("zahradě", "vrtu"),
        ("plotu", "ograde"),
        ("stromů", "stabala"),
        ("záhonů", "gredica"),
        ("sekačka", "kosilica"),
        ("Záruka", "Jamstvo"),
        ("Praha", "Zagreb"),
        ("Brno", "Split"),
        ("ověřený nákup", "verificirana kupnja"),
        ("Jen 2 kg", "Samo 2 kg"),
        ("Jen ", "Samo "),
        ("jen ", "samo "),
        ("Zbývá", "Ostalo je samo"),
        ("kusů skladem", "komada na skladištu"),
        ("právě prohlíží", "gleda"),
        ("sousedy", "susjede"),
        ("Kompletní sada", "Potpuni komplet"),
        ("kompletní sada", "potpuni komplet"),
        ("Přímé srovnání", "Izravna usporedba"),
        ("Doručení po celé České republice", "Dostava u cijeloj Hrvatskoj"),
        ("Jan Novák", "Ivan Horvat"),
        ("Václavské náměstí 10, Praha", "Ilica 15, Zagreb"),
        ("Platba při převzetí", "Plaćanje pri dostavi"),
        ("bezkartáčový", "bezčetkasti"),
        ("v balení", "u kompletu"),
        ("ocelové", "čelične"),
        ("Ocelové", "Čelične"),
        ("plastové", "plastične"),
        ("trávníku", "travnjaka"),
        ("trávu", "travu"),
        ("tráva", "trava"),
        ("plevel", "korov"),
        ("trní", "trnje"),
        ("keře", "grmlje"),
        ("větvičky", "grančice"),
    ]
    for key, val in list(hr.items()):
        if not isinstance(val, str):
            continue
        if key in ("title", "description", "topbar"):
            continue
        hr[key] = apply_replacements(val, pairs)
    hr["title"] = "TRIMEX™ — Akumulatorski trimer bez benzina | -50% danas"
    hr["description"] = (
        "Trimer TRIMEX™ s motorom od 2880 W, 2 baterije 60 W uključene i samo 2 kg. "
        "Bez benzina, dima i kabela. Plaćanje pouzećem."
    )
    hr["topbar"] = "🔥 SAMO DANAS: -50% NA TRIMEX™ + 2 BATERIJE 60 W UKLJUČENE 🔥"
    hr["lead"] = (
        "<strong>TRIMEX™</strong> — bezčetkasti motor 2880 W i 2 baterije 60 W u kompletu. "
        "Reže tamo gdje kosilica ne dođe: uz ogradu, oko stabala i gredica. Jamstvo 2 godine."
    )
    hr["h1_m"] = (
        "Lagan kao boca vode od 2 litre, ali reže trnje, korov i grmlje bez kapi benzina."
    )
    hr["f3_p"] = "Snažan motor i čvrsti materijali"
    hr["stock_r"] = "Ostalo je samo nekoliko komada na skladištu"
    hr["live_tpl"] = "<strong>{n} osoba</strong> gleda TRIMEX™ upravo sada"
    hr["w1_eye"] = "01 — TRIMEX™: Snaga za najtvrdokorniji korov, bez benzina"
    hr["w1_h"] = "Visoka trava, trnje, korov i grančice: sve režete bez napora"
    hr["w1_t3"] = "Bez benzina i dima"
    hr["w1_i"] = "Vrt uredite brže – bez trzanja i dima."
    hr["w2_h"] = "Dvije baterije i samo 2 kg: završite bez bolova u leđima"
    hr["w2_t3"] = "Podesiva drška"
    hr["w2_p"] = (
        "Kad se baterija isprazni, zamijenite je u nekoliko sekundi i nastavite. TRIMEX™ je lagan i "
        "uravnotežen, teleskopska drška podešava se do 2 metra, protuklizni rukohvat smanjuje vibracije – "
        "ruke, ramena i leđa ne pate ni nakon sati rada."
    )
    hr["w2_i"] = "Više obavljeno, manje umora. Idealno i kad nemate više snage."
    hr["w3_h"] = "Bez glasne buke, bez dodatne opreme"
    hr["w3_t1"] = "Tih rad"
    hr["w3_t3"] = "Montaža u nekoliko minuta"
    hr["w3_p"] = (
        "Možete raditi u vrtu i nedjeljom ujutro bez nerviranja susjeda. U kutiji je sve: baterije, punjač, "
        "čelične i plastične oštrice, rezni disk i montažni alat. Otvorite, sastavite u nekoliko minuta – i "
        "već ste u vrtu."
    )
    hr["w3_i"] = "Bez iznenađenja i dodatnih troškova – samo uredan vrt."
    hr["cmp_h2"] = "Benzinski trimer ili TRIMEX™? Pogledajte razliku"
    hr["cmp_aria"] = "Usporedba benzinskog trimerja i TRIMEX"
    hr["test_h2"] = "Tisuće kupaca odabralo je TRIMEX™ za svoj vrt"
    hr["t2_h"] = "Rezervna baterija pravi razliku."
    hr["t3_h"] = "Kupila sam roditeljima na poklon."
    hr["kit_h2"] = "Potpuni komplet TRIMEX™, spreman za vaš vrt"
    hr["kit_i3"] = "Brzi punjač"
    hr["kit_i8"] = "Montažni alat i upute"
    hr["kit_i9"] = "Službena 2-godišnja garancija"
    hr["faq1_a"] = "Nakon telefonske potvrde narudžbe paket stiže u 24–48 radnih sati."
    hr["faq2_a"] = "Plaćate izravno dostavljaču pri dostavi. Bez predujma i podataka o kartici."
    hr["faq3_q"] = "Koliko dugo traje baterija?"
    hr["faq4_q"] = "Reže li tvrdokorni trnje i korov?"
    hr["faq5_q"] = "Je li težak? Može li ga koristiti starija osoba?"
    hr["faq6_q"] = "Što ako mi ne odgovara?"
    hr["faq6_a"] = "Imate 30 dana za povrat. Kontaktirajte korisničku podršku – vodimo vas korak po korak."
    hr["ty_title"] = "Narudžba primljena — pričekajte potvrdni poziv | TRIMEX™"
    hr["f1_p"] = "Dostava u cijeloj Hrvatskoj"
    hr["ph_name"] = "Ivan Horvat"
    hr["ph_addr"] = "Ilica 15, Zagreb"
    hr.update(
        {
            "w3_eye": "03 — TRIMEX™: Tiho i spreman odmah nakon otvaranja",
            "alt_w3": "Potpuni komplet TRIMEX™ spreman odmah nakon otvaranja",
            "cmp_r1_l": "Napajanje",
            "cmp_r1_a": "Benzin i mješavina za kupnju",
            "cmp_r1_b": "Akumulator, bez goriva",
            "cmp_r2_l": "Težina",
            "cmp_r2_a": "Težak, opterećuje ramena i leđa",
            "cmp_r2_b": "Samo 2 kg, lagan i uravnotežen",
            "cmp_r3_l": "Buka",
            "cmp_r3_a": "Zaglušujuća, smeta susjedima",
            "cmp_r3_b": "Tiho",
            "cmp_r4_l": "Dim i miris",
            "cmp_r4_a": "Ispušni plinovi i miris benzina",
            "cmp_r4_b": "Bez emisija",
            "cmp_r5_l": "Pokretanje",
            "cmp_r5_a": "Starter konopac više puta",
            "cmp_r5_b": "Uključivanje jednim gumbom",
            "cmp_r6_l": "Radno vrijeme",
            "cmp_r6_a": "Pauze za punjenje",
            "cmp_r6_b": "2 baterije 60 W, zamjena u sekundama",
            "cmp_r7_l": "Kupnja",
            "cmp_r7_a": "Dodatna oprema često odvojeno",
            "cmp_r7_b": "Potpuni komplet + 2-godišnja garancija",
            "t1_h": "Izgledalo je kao igračka – dok nisam probao.",
            "t1_p": (
                "«Pri otvaranju sam bio skeptičan: tako lagan, u usporedbi sa starim benzinskim, izgledao je kao "
                "igračka. Zatim sam ga testirao na trnju i granama debljih od centimetar – rezao bez problema.»"
            ),
            "t1_auth": "Marco T. — Split, verificirana kupnja",
            "t2_p": (
                "«Imam veliko parcelu, a visoka trava uz ogradu bila je noćna mora. Kad prva baterija iscrpi, u nekoliko "
                "sekundi stavim drugu i nastavim. Konačno sve završim odjednom.»"
            ),
            "t2_auth": "Giuseppe L. — Rijeka, verificirana kupnja",
            "t3_p": (
                "«Tata ima 72 godine i nisam ga više htjela vidjeti s benzinskim trimerom na leđima. Ovaj je lagan, "
                "upaljuje se odmah, drška se dobro podešava. Sada ga koristi sam bez problema.»"
            ),
            "t3_auth": "Francesca D. — Zagreb, verificirana kupnja",
            "alt_t1": "Trimer TRIMEX™ nakon rezanja trnja u vrtu",
            "alt_t2": "Visoka trava uz ogradu pokošena TRIMEX™",
            "alt_t3": "Stariji muškarac koristi trimer TRIMEX™ u vrtu",
            "kit_h2": "Potpuni komplet TRIMEX™, spreman za vaš vrt",
            "alt_kit": "Potpuni komplet TRIMEX™",
            "kit_i1": "Trimer TRIMEX™ s motorom 2880 W",
            "kit_i2": "2 baterije 60 W — rad bez prekida",
            "kit_i4": "Čelične oštrice — trnje, grmlje i grančice",
            "kit_i5": "Plastične oštrice — trava i rubovi travnjaka",
            "kit_i6": "Rezni disk — gusta vegetacija",
            "kit_i7": "Teleskopska drška s protukliznim rukohvatom",
        }
    )
    return hr


def fix_lv(lv: dict) -> None:
    lv.update(
        {
            "cta": "JĀ, ES Gribu TRIMEX™ →",
            "cmp_r1_l": "Barošana",
            "cmp_r1_b": "Akumulators, bez degvielas",
            "cmp_r2_l": "Svars",
            "cmp_r2_a": "Smags, nogurina plecus un muguru",
            "cmp_r2_b": "Tikai 2 kg, viegls un līdzsvarots",
            "cmp_r3_l": "Troksnis",
            "cmp_r3_a": "Aizbāž ausis, tracina kaimiņus",
            "cmp_r3_b": "Kluss",
            "cmp_r4_l": "Dūmi un smaka",
            "cmp_r4_b": "Bez emisijām",
            "cmp_r5_l": "Iedarbināšana",
            "cmp_r5_a": "Startera aukla vairākas reizes",
            "cmp_r5_b": "Ieslēgšana ar vienu pogu",
            "cmp_r6_l": "Darba laiks",
            "cmp_r6_a": "Pauzes uzpildes laikā",
            "cmp_r6_b": "2 x 60 W baterijas, maiņa sekundēs",
            "cmp_r7_l": "Pirkums",
            "cmp_r7_a": "Piederumi bieži atsevišķi",
            "cmp_r7_b": "Pilns komplekts + 2 gadu garantija",
            "alt_t1": "TRIMEX™ trimmeris pēc dzeloņu pļaušanas dārzā",
            "alt_t2": "Augsta zāle gar žogu nopļauta ar TRIMEX™",
            "alt_t3": "Vecāks vīrietis lieto TRIMEX™ trimmeri dārzā",
            "kit_h2": "Pilns TRIMEX™ komplekts, gatavs jūsu dārzam",
            "alt_kit": "Pilns TRIMEX™ komplekts",
            "kit_i1": "TRIMEX™ trimmeris ar 2880 W motoru",
            "kit_i2": "2 x 60 W baterijas — darbs bez pārtraukumiem",
            "kit_i3": "Ātrs lādētājs",
            "kit_i4": "Tērauda asmeņi — dzeloņi, krūmi un zari",
            "kit_i5": "Plastmasas asmeņi — zāle un zāliena malas",
            "kit_i6": "Griešanas disks — blīva veģetācija",
            "kit_i7": "Teleskopiskais kāts ar neslīdošu rokturi",
            "kit_i8": "Montāžas rīki un rokasgrāmata",
            "kit_i9": "Oficiāla 2 gadu garantija",
            "faq1_a": "Pēc telefoniskās apstiprināšanas pakete nonāk mājās 24–48 darba stundu laikā.",
            "faq2_a": "Maksājat tieši kurjeram piegādes brīdī. Bez priekšapmaksas un kartes datiem.",
            "faq3_q": "Cik ilgi darbojas baterija?",
            "faq4_q": "Vai pļauj stingrus dzeloņus un nezāles?",
            "faq4_a": (
                "Jā. Pateicoties 2880 W motoram un komplektā iekļautajiem tērauda asmeņiem un diskam, "
                "pļauj augstu zāli, dzeloņus, nezāles un mazus krūmus."
            ),
            "faq5_q": "Vai tas ir smags? Vai to var lietot vecāks cilvēks?",
            "faq5_a": (
                "Sver tikai 2 kg un ir labi līdzsvarots. Regulējams kāts un neslīdošs rokturis atvieglo "
                "darbu arī ar mazāku spēku."
            ),
            "faq6_q": "Kas notiek, ja man neder?",
            "faq6_a": "Jums ir 30 dienas atgriešanai. Sazinieties ar klientu apkalpošanu – vedīsim soli pa solim.",
            "ty_title": "Pasūtījums saņemts — gaidiet apstiprinājuma zvanu | TRIMEX™",
        }
    )
    lv["cta"] = "JĀ, ES VĒLOS TRIMEX™ →"


def write_patches(patches: dict) -> None:
    header = (
        "# -*- coding: utf-8 -*-\n"
        '"""Native TRIMEX copy patches for cs, hu, lv, sl, hr, sk (keys match pl locale)."""\n\n'
    )
    body = pprint_patches(patches)
    PATCHES_PATH.write_text(header + "COPY_PATCHES = " + body + "\n", encoding="utf-8")


def pprint_patches(patches: dict) -> str:
    import pprint

    return pprint.pformat(patches, width=120, sort_dicts=False)


def main() -> None:
    mod = load_module(PATCHES_PATH, "_trimex_locale_patches")
    patches = mod.COPY_PATCHES
    cs = patches["cs"]
    fix_cs(cs)
    patches["sk"] = cs_to_sk(cs)
    patches["sl"] = cs_to_sl(cs)
    patches["hr"] = cs_to_hr(cs)
    fix_lv(patches["lv"])
    write_patches(patches)
    print("Repaired COPY_PATCHES")


if __name__ == "__main__":
    main()
