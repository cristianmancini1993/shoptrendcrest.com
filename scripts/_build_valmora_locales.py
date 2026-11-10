# -*- coding: utf-8 -*-
"""Build _valmora_copy_data.py with all 12 locales."""
from pathlib import Path

OUT = Path(__file__).with_name('_valmora_copy_data.py')

COMMON_KIT = [
    'Tall pot 7L with lid — for soups and large portions',
    'Medium pot 3L with lid — for sauces and daily use',
    'Saucepan 1.5L with lid — for recipes and smaller portions',
    'Braising pot 3.5L with auxiliary handle',
    'Frying pan 20cm and frying pan 28cm',
    'Steamer basket with lid',
    'Welded handles, comfortable during cooking',
    'User manual and warranty certificate',
    'Official 2-year warranty',
]

LOCALES = {
    'ro': {
        'submitting': 'Se trimite...',
        'cookie_text': 'Folosim cookie-uri tehnice și de la terți pentru a îmbunătăți experiența ta și pentru analiză.',
        'cookie_accept': 'Accept',
        'cookie_learn': 'Află mai multe',
        'title': 'VALMORA™ — Set de vase din oțel inoxidabil cu 3 straturi',
        'description': 'Descoperă VALMORA™: setul complet din oțel inoxidabil cu 3 straturi care ajută la distribuirea uniformă a căldurii. Compatibil cu inducția și mașina de spălat vase.',
        'og_description': 'Un set complet din oțel inoxidabil cu 3 straturi: căldură distribuită mai bine, curățare simplă și compatibilitate cu inducția.',
        'topbar': '🔥 DOAR ASTĂZI: -50% LA SETUL COMPLET VALMORA™ 🔥',
        'rating': '<strong>4,8/5</strong> — Peste <strong>6.200</strong> de clienți mulțumiți',
        'gift': '🛡️ Retur în 30 de zile + livrare rapidă',
        'h1_m': 'Atenție: până la <span class="hl">9.000 de microplastice</span> pot ajunge în mâncare. Protejează-ți bucătăria astăzi.',
        'h1_d': 'Atenție: tigăile antiaderente cu teflon pot elibera până la <span class="hl">9.000 de particule de microplastic</span> în mâncare. Protejează-ți bucătăria astăzi.',
        'lead': '<strong>VALMORA™</strong> — oțel inoxidabil cu 3 straturi și miez de aluminiu, fără PTFE și PFOA. Fără strat care se uzează, căldură distribuită pe toată baza și rezistență gândită să dureze. Garanție oficială de 2 ani.',
        'alt_hero': 'Set complet VALMORA™ cu capace din sticlă și mânere din lemn',
        'cta': 'DA, VREAU VALMORA™ →',
        'form_note_hero': '🔒 Livrare rapidă · Plată la livrare · Retur în 30 de zile',
        'f1_h': 'Livrare rapidă', 'f1_p': 'Expediere în toată România',
        'f2_h': 'Comandă sigură', 'f2_p': 'Date protejate la achiziție',
        'f3_h': 'Calitate verificată', 'f3_p': 'Materiale solide și durabile',
        'f4_h': '30 de zile pentru retur', 'f4_p': 'Procedură simplă și rapidă',
        'countdown': '⏰ Oferta -50% expiră în',
        'hours': 'Ore', 'mins': 'Min', 'secs': 'Sec',
        'stock_l': 'Disponibilitate', 'stock_r': 'Au rămas puține seturi în stoc',
        'live_tpl': '<strong>{n} persoane</strong> se uită la VALMORA™ acum',
        'form_h2': 'Finalizează comanda',
        'form_p': 'Introdu datele tale: echipa noastră te va suna pentru a verifica comanda și a stabili livrarea.',
        'label_name': 'Nume și prenume*', 'label_tel': 'Număr de telefon*', 'label_addr': 'Adresă de livrare*',
        'ph_name': 'Ion Popescu', 'ph_phone': '+40 721 234 567', 'ph_addr': 'Strada Victoriei 10, București',
        'btn_submit': 'CONFIRMĂ COMANDA',
        'form_note': '🔒 Plată la livrare · Retur în 30 de zile',
        'w1_eye': '01 — VALMORA™: Gătire uniformă de la centru la margini',
        'w1_h': 'Căldura se răspândește pe toată baza, fără zone supraîncălzite',
        'w1_t1': 'Structură cu 3 straturi', 'w1_t2': 'Miez de aluminiu', 'w1_t3': 'Căldură bine distribuită',
        'w1_p': 'Cu VALMORA™ nu trebuie să amesteci continuu pentru a evita arderea mâncării în unele zone. Nucleul de aluminiu ajută la distribuirea uniformă a căldurii, iar oțelul inoxidabil oferă o suprafață rezistentă pentru gătit zilnic.',
        'w1_i': 'Gătire mai regulată și mai puțin timp petrecut la aragaz.',
        'alt_w1': 'Set de vase VALMORA cu bază trilaminată',
        'w2_eye': '02 — VALMORA™: Același set pentru orice tip de bucătărie',
        'w2_h': 'Un singur set pentru gaz, electric, vitroceramică și inducție',
        'w2_t1': 'Compatibil cu inducția', 'w2_t2': 'Cuptor până la 230°C', 'w2_t3': 'Mânere confortabile',
        'w2_p': 'Baza multistrat este compatibilă cu principalele plite, inclusiv inducția. Dacă rețeta o cere, poți muta vasul de pe aragaz în cuptor până la 230°C fără să schimbi recipientul.',
        'w2_i': 'Gătește cu mai multă libertate, reducând pașii și vasele de spălat.',
        'alt_w2': 'Set VALMORA compatibil cu plita cu inducție',
        'w3_eye': '03 — VALMORA™: Curățare rapidă și strălucire de durată',
        'w3_h': 'O suprafață netedă care nu reține aromele sau mirosurile',
        'w3_t1': 'Oțel lustruit', 'w3_t2': 'Neutru la gust', 'w3_t3': 'Compatibil cu mașina de spălat vase',
        'w3_p': 'Oțelul inoxidabil se curăță ușor și nu păstrează mirosurile rețetelor anterioare. Toate componentele pot intra în mașina de spălat vase, făcând VALMORA™ practic chiar și la utilizare intensă și zilnică.',
        'w3_i': 'Mai puțin timp pentru ordine și vase care își păstrează strălucirea mai mult timp.',
        'alt_w3': 'Set VALMORA lavabil în mașina de spălat vase',
        'cmp_label': 'Comparație directă',
        'cmp_h2': 'Vase obișnuite sau VALMORA™? Vezi ce se schimbă',
        'cmp_aria': 'Comparație între vase obișnuite și VALMORA',
        'th_common': 'Obișnuite',
        'cmp_r1_l': 'Distribuția căldurii', 'cmp_r1_a': 'Posibile zone prea fierbinți', 'cmp_r1_b': 'Bază cu 3 straturi, căldură uniformă',
        'cmp_r2_l': 'Plite', 'cmp_r2_a': 'Compatibilitate variabilă', 'cmp_r2_b': 'Gaz, electric, vitroceramică și inducție',
        'cmp_r3_l': 'Utilizare în cuptor', 'cmp_r3_a': 'Adesea nedisponibilă', 'cmp_r3_b': 'Potrivit până la 230°C',
        'cmp_r4_l': 'Mânere', 'cmp_r4_a': 'Prindere adesea incomodă', 'cmp_r4_b': 'Solide și ușor de ținut',
        'cmp_r5_l': 'Curățare', 'cmp_r5_a': 'Poate deveni mată în timp', 'cmp_r5_b': 'Oțel lustruit, lavabil în mașina de spălat vase',
        'cmp_r6_l': 'Conținut', 'cmp_r6_a': 'Adesea puține piese', 'cmp_r6_b': 'Set complet de 12 piese',
        'cmp_r7_l': 'Achiziție', 'cmp_r7_a': 'Garanții nu mereu clare', 'cmp_r7_b': '30 de zile pentru a solicita returul',
        'test_h2': 'Mii de clienți au ales deja VALMORA™ pentru bucătăria de zi cu zi',
        't1_h': 'Orezul se gătește bine și nu se lipește de fund.',
        't1_p': '«Gătesc zilnic pentru familie și acest set se simte imediat. Căldura se distribuie mai bine, preparatele se gătesc mai uniform și capacele se închid bine.»',
        't1_auth': 'Maria B. — București, achiziție verificată',
        't2_h': 'Soția mea a luat VALMORA™ pentru familia noastră numeroasă: acum îl folosim aproape zilnic.',
        't2_p': '«Îl folosim zilnic pentru carne, sosuri și feluri principale. Nu se lipește totul ca înainte, căldura e bine distribuită și curățarea e foarte simplă.»',
        't2_auth': 'Andrei M. — Cluj-Napoca, achiziție verificată',
        't3_h': 'Rămân strălucitoare chiar și după multe spălări.',
        't3_p': '«Le folosesc des și ajung regulat în mașina de spălat vase. Oțelul rămâne curat cu puțin efort și nu reține mirosuri sau pete dificile.»',
        't3_auth': 'Elena R. — Iași, achiziție verificată',
        'alt_t1': 'Set complet VALMORA™ de 12 piese proaspăt primit',
        'alt_t2': 'Set VALMORA pe plită cu inducție',
        'alt_t3': 'Suprafață lucioasă a setului VALMORA după spălare',
        'kit_eye': 'Ce primești',
        'kit_h2': 'Setul complet VALMORA™ de 12 piese, gata pentru bucătăria ta',
        'alt_kit': 'Kit complet VALMORA™',
        'kit_i1': 'Oală înaltă 7L cu capac — pentru supe și porții mari',
        'kit_i2': 'Oală medie 3L cu capac — pentru sosuri și uz zilnic',
        'kit_i3': 'Cratită 1,5L cu capac — pentru rețete și porții mai mici',
        'kit_i4': 'Oală pentru tocană 3,5L cu mâner auxiliar',
        'kit_i5': 'Tigaie 20cm și tigaie 28cm',
        'kit_i6': 'Coș pentru gătire la abur cu capac',
        'kit_i7': 'Mânere sudate, confortabile în timpul gătitului',
        'kit_i8': 'Manual de utilizare și certificat de garanție',
        'kit_i9': 'Garanție oficială de 2 ani',
        'faq_h2': 'Întrebări frecvente',
        'faq1_q': 'Cât durează livrarea?',
        'faq1_a': 'Livrarea se face de obicei în 2-4 zile lucrătoare. După solicitare te vom contacta pentru a verifica datele și a confirma expedierea.',
        'faq2_q': 'Cum se face plata?',
        'faq2_a': 'Poți plăti {price} direct la livrare, când primești coletul de la curier.',
        'faq3_q': 'Setul este compatibil cu inducția?',
        'faq3_a': 'Da. Baza multistrat cu miez de aluminiu este potrivită pentru plite pe gaz, electrice, vitroceramice și cu inducție.',
        'faq4_q': 'Vasele pot intra în cuptor?',
        'faq4_a': 'Da, setul poate fi folosit în cuptor până la 230°C: ideal pentru a începe o rețetă pe aragaz și a o finaliza în cuptor.',
        'faq5_q': 'Ce se întâmplă dacă setul nu mi se potrivește?',
        'faq5_a': 'Ai 30 de zile de la livrare pentru a solicita returul și a obține rambursarea conform condițiilor politicii noastre de rambursare.',
        'footer_blurb': 'Produse utile pentru viața de zi cu zi, livrare rapidă și plată la livrare.',
        'info': 'Informații', 'about': 'Despre noi', 'contact': 'Contactează-ne',
        'privacy': 'Politica de confidențialitate', 'terms': 'Termeni și condiții',
        'cookie_pol': 'Politica de cookie-uri', 'ship': 'Politica de livrare',
        'refund': 'Politica de rambursare', 'contacts': 'Contacte',
        'country_us': 'Statele Unite', 'rights': 'Toate drepturile rezervate',
        'ty_title': 'Comandă primită — Așteaptă apelul de confirmare | VALMORA™',
        'ty_desc': 'Comanda ta VALMORA™ a fost primită. Rămâne un singur pas: răspunde la apelul operatorului nostru pentru a confirma datele.',
        'ty_h1': 'Comanda ta a fost înregistrată cu succes!',
        'ty_sub': 'Perfect — comanda ta este în procesare. Pentru a o finaliza și a porni expedierea lipsește doar <strong>confirmarea telefonică</strong>.',
        'ty_alt': 'Echipa gadgetshifthub la lucru: call center și logistică COD',
        'ty_eyebrow': '👇 Ce trebuie să faci acum',
        'ty_action_title': '📞 Răspunde la apelul de confirmare',
        'ty_action_body': 'Un operator te va suna <strong>în următoarele ore</strong> pentru a confirma comanda și detaliile de livrare.',
        'ty_action_warn': 'Dacă nu răspunzi, comanda nu poate fi confirmată și va fi anulată.',
        'ty_hours_h': '🕒 Ore de contact',
        'ty_hours': '<strong>Luni – Sâmbătă</strong> · 9:00 – 18:00',
        'ty_next_h': '📋 Ce urmează',
        'ty_step1': 'Răspunde la apel și <strong>confirmă datele tale</strong>',
        'ty_step2': 'Comanda ta va fi pregătită în <strong>24–48 de ore</strong>',
        'ty_step3': 'Primești coletul la domiciliu și <strong>plătești la livrare</strong>',
        'ty_badge1': '🔒 Plată la livrare', 'ty_badge2': '🛡️ Garanție 24 luni', 'ty_badge3': '🔐 Protecție SSL',
    },
}

from _build_valmora_locales_part2 import LOCALES_PART2  # noqa: E402
from _build_valmora_locales_part3 import LOCALES_PART3  # noqa: E402
from _build_valmora_locales_part4 import LOCALES_PART4  # noqa: E402
from _build_valmora_locales_part5 import LOCALES_PART5  # noqa: E402
from _build_valmora_locales_part6 import LOCALES_PART6  # noqa: E402

LOCALES.update(LOCALES_PART2)
LOCALES.update(LOCALES_PART3)
LOCALES.update(LOCALES_PART4)
LOCALES.update(LOCALES_PART5)
LOCALES.update(LOCALES_PART6)

ORDER = ['ro', 'pt', 'sl', 'hr', 'hu', 'es', 'de', 'lt', 'pl', 'cs', 'sk', 'lv']

REQUIRED_KEYS = [
    'submitting', 'cookie_text', 'cookie_accept', 'cookie_learn', 'title', 'description', 'og_description',
    'topbar', 'rating', 'gift', 'h1_m', 'h1_d', 'lead', 'alt_hero', 'cta', 'form_note_hero',
    'f1_h', 'f1_p', 'f2_h', 'f2_p', 'f3_h', 'f3_p', 'f4_h', 'f4_p',
    'countdown', 'hours', 'mins', 'secs', 'stock_l', 'stock_r', 'live_tpl',
    'form_h2', 'form_p', 'label_name', 'label_tel', 'label_addr', 'ph_name', 'ph_phone', 'ph_addr',
    'btn_submit', 'form_note',
    'w1_eye', 'w1_h', 'w1_t1', 'w1_t2', 'w1_t3', 'w1_p', 'w1_i', 'alt_w1',
    'w2_eye', 'w2_h', 'w2_t1', 'w2_t2', 'w2_t3', 'w2_p', 'w2_i', 'alt_w2',
    'w3_eye', 'w3_h', 'w3_t1', 'w3_t2', 'w3_t3', 'w3_p', 'w3_i', 'alt_w3',
    'cmp_label', 'cmp_h2', 'cmp_aria', 'th_common',
    'cmp_r1_l', 'cmp_r1_a', 'cmp_r1_b', 'cmp_r2_l', 'cmp_r2_a', 'cmp_r2_b',
    'cmp_r3_l', 'cmp_r3_a', 'cmp_r3_b', 'cmp_r4_l', 'cmp_r4_a', 'cmp_r4_b',
    'cmp_r5_l', 'cmp_r5_a', 'cmp_r5_b', 'cmp_r6_l', 'cmp_r6_a', 'cmp_r6_b',
    'cmp_r7_l', 'cmp_r7_a', 'cmp_r7_b',
    'test_h2', 't1_h', 't1_p', 't1_auth', 't2_h', 't2_p', 't2_auth', 't3_h', 't3_p', 't3_auth',
    'alt_t1', 'alt_t2', 'alt_t3',
    'kit_eye', 'kit_h2', 'alt_kit', 'kit_i1', 'kit_i2', 'kit_i3', 'kit_i4', 'kit_i5', 'kit_i6', 'kit_i7', 'kit_i8', 'kit_i9',
    'faq_h2', 'faq1_q', 'faq1_a', 'faq2_q', 'faq2_a', 'faq3_q', 'faq3_a', 'faq4_q', 'faq4_a', 'faq5_q', 'faq5_a',
    'footer_blurb', 'info', 'about', 'contact', 'privacy', 'terms', 'cookie_pol', 'ship', 'refund', 'contacts', 'country_us', 'rights',
    'ty_title', 'ty_desc', 'ty_h1', 'ty_sub', 'ty_alt', 'ty_eyebrow', 'ty_action_title', 'ty_action_body', 'ty_action_warn',
    'ty_hours_h', 'ty_hours', 'ty_next_h', 'ty_step1', 'ty_step2', 'ty_step3', 'ty_badge1', 'ty_badge2', 'ty_badge3',
]


def build():
    lines = [
        '# -*- coding: utf-8 -*-',
        '"""VALMORA cookware landing + thank-you copy for 12 locales."""',
        '',
        'COPY = {',
    ]
    for i, code in enumerate(ORDER):
        data = LOCALES[code]
        missing = [k for k in REQUIRED_KEYS if k not in data]
        extra = [k for k in data if k not in REQUIRED_KEYS]
        if missing:
            raise SystemExit(f'{code} missing keys: {missing}')
        if extra:
            raise SystemExit(f'{code} extra keys: {extra}')
        lines.append(f'    "{code}": {{')
        for k in REQUIRED_KEYS:
            lines.append(f'        "{k}": {repr(data[k])},')
        lines.append('    },' if i < len(ORDER) - 1 else '    },')
    lines.append('}')
    lines.append('')
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {OUT}')
    for code in ORDER:
        print(f'  {code}: {len(LOCALES[code])} keys')


if __name__ == '__main__':
    build()
