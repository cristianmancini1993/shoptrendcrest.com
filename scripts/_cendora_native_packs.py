# -*- coding: utf-8 -*-
"""Per-locale CENDORA copy keyed like IT_STRINGS (native QA)."""
from __future__ import annotations

from typing import Any

from _cendora_i18n_embed import _ro

StrOrSeq = str | list[str] | tuple[str, ...]


def _apply(base: dict[str, StrOrSeq], patch: dict[str, StrOrSeq]) -> dict[str, StrOrSeq]:
    out = dict(base)
    out.update(patch)
    return out


def _pt() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "submitting": "A enviar...",
            "cookie_text": "Utilizamos cookies técnicos e de terceiros para melhorar a navegação e para análises estatísticas.",
            "cookie_accept": "Aceitar",
            "cookie_learn": "Mais informações",
            "title": "CENDORA™ — Conjunto de cozinha antiaderente, 12 peças",
            "description": "CENDORA™: conjunto de 12 peças com revestimento antiaderente efeito pedra, fundo que aquece de forma uniforme, adequado para indução e máquina de lavar loiça. Pagamento na entrega em Portugal.",
            "og_title": "CENDORA™ — Temperatura estável em qualquer fogão",
            "og_description": "Antiaderente sem PTFE e PFOA: menos gordura, cozedura uniforme, limpeza rápida e compatibilidade com gás, vitrocerâmica e indução.",
            "topbar": "🔥 −50% NO CONJUNTO DE COZINHA — SÓ HOJE — PAGAMENTO NA ENTREGA · ENVIO GRÁTIS 🔥",
            "rating": "<strong>4,9/5</strong> — Mais de <strong>6.500</strong> famílias em Portugal já escolheram a CENDORA™",
            "gift": "🎁 OFERTA: utensílios de cozinha + pano premium",
            "h1_mobile": "Até <span class=\"hl\">9.000 microplásticos</span> podem acabar na comida que serve à mesa: está na hora de mudar a panela.",
            "h1_desktop": "Com frigideiras antiaderentes comuns, até <span class=\"hl\">9.000 partículas de plástico</span> podem acabar no prato de quem ama. Proteja a sua família: passe à CENDORA™.",
            "lead": "Revestimento antiaderente efeito pedra, sem PTFE nem PFOA. A comida não cola, usa menos óleo e o calor distribui-se de forma uniforme. Compatível com todos os fogões, incluindo indução. Garantia oficial de 24 meses.",
            "alt_hero": "Conjunto CENDORA™ de 12 peças com tampas de vidro",
            "cta": "QUERO A CENDORA™ →",
            "cta_inline": "QUERO A CENDORA™ →",
            "form_note_hero": "🔒 Envio rápido · Paga ao estafeta · Devolução em 30 dias",
            "form_note_form": "🔒 Pagamento na entrega · Devolução em 30 dias",
            "f1_h": "Envio rápido",
            "f1_p": "Entrega em todo Portugal",
            "f2_h": "Encomenda protegida",
            "f2_p": "Os seus dados permanecem seguros",
            "f3_h": "Materiais certificados",
            "f3_p": "Antiaderente para uso diário",
            "f4_h": "Devolução 30 dias",
            "f4_p": "Processo claro se não ficar convencido",
            "countdown": "⏰ A promoção de −50% termina em",
            "hours": "Horas",
            "mins": "Min",
            "secs": "Seg",
            "stock_l": "Disponibilidade em stock",
            "stock_r": "Últimos 5 conjuntos disponíveis",
            "live": "<strong>{n} pessoas</strong> estão a ver a CENDORA™ neste momento",
            "live0": "<strong>34 pessoas</strong> estão a ver a CENDORA™ neste momento",
            "form_h2": "Finalize o pedido",
            "form_p": "Preencha o formulário com os seus dados. Ligamos para confirmar a encomenda e organizar a entrega em casa.",
            "submit_btn": "ENVIAR PEDIDO",
            "why1_eye": "01 — CENDORA™: cozedura uniforme, zero aderências",
            "why1_h": "Superfície antiaderente que deixa a comida deslizar sem rasgar",
            "why1_t1": "Efeito pedra",
            "why1_t2": "Menos óleo",
            "why1_t3": "Calor homogéneo",
            "why1_p1": "O fundo em alumínio distribui o calor por toda a base; o revestimento antiaderente evita que ovos, carne e legumes colem mesmo em lume médio.",
            "why1_p2": "Pratos mais leves e limpeza em segundos.",
            "why2_eye": "02 — CENDORA™: um único conjunto para toda a cozinha",
            "why2_h": "Gás, elétrico, vitrocerâmica ou indução: um kit, sem acessórios extra",
            "why2_t1": "Indução",
            "why2_t2": "Forno 230°C",
            "why2_t3": "Pegas ergonómicas",
            "why2_p1": "O fundo reforçado é compatível com os fogões mais usados. Passe do fogão ao forno até 230°C quando precisar, sem mudar de recipiente.",
            "why2_p2": "Mais flexibilidade na cozinha, menos panelas para lavar.",
            "why3_eye": "03 — CENDORA™: higiénica e fácil de manter",
            "why3_h": "Superfície que não «prende» odores entre um prato e outro",
            "why3_t1": "Antiaderente",
            "why3_t2": "Sem odores",
            "why3_t3": "Máquina de lavar loiça",
            "why3_p1": "O revestimento liso enxágua-se depressa e não absorve aromas. Cada peça pode ir à máquina de lavar loiça: depois do almoço arruma a cozinha mais depressa.",
            "why3_p2": "Menos esforço depois das refeições, mais tempo para si.",
            "compare_label": "Comparação",
            "compare_h": "Conjunto barato ou CENDORA™? Eis a diferença",
            "compare_aria": "Comparação entre panelas standard e CENDORA",
            "cmp_th_old": "Standard",
            "cmp_row_adh": "Antiaderência",
            "cmp_old_adh": "Degrada-se depressa",
            "cmp_win_adh": "Revestimento efeito pedra, durável",
            "cmp_row_heat": "Distribuição do calor",
            "cmp_old_heat": "Muitas vezes irregular",
            "cmp_win_heat": "Fundo em alumínio para calor uniforme",
            "cmp_row_compat": "Compatibilidade",
            "cmp_old_compat": "Limitada a poucos fogões",
            "cmp_win_compat": "Gás, elétrico, vitrocerâmica e indução",
            "cmp_row_oven": "Forno",
            "cmp_old_oven": "Nem sempre adequado",
            "cmp_win_oven": "Utilizável até 230°C",
            "cmp_row_handle": "Pegas",
            "cmp_old_handle": "Muitas vezes pouco confortáveis",
            "cmp_win_handle": "Ergonómicas e bem fixas",
            "cmp_row_care": "Manutenção",
            "cmp_old_care": "Tende a opacar",
            "cmp_win_care": "Limpeza fácil, também na máquina de lavar loiça",
            "cmp_row_kit": "Conteúdo",
            "cmp_old_kit": "Poucos componentes",
            "cmp_win_kit": "Conjunto completo de 12 peças",
            "cmp_row_return": "Devolução",
            "cmp_old_return": "Regras pouco claras",
            "cmp_win_return": "30 dias para devolver",
            "testimonials_h": "Depois deste conjunto, é difícil voltar às panelas antigas",
            "rev1_h": "Anos de cozinha diária: finalmente um conjunto que aguenta o ritmo.",
            "rev1_p": "«Criei três filhos e troquei de panelas várias vezes. Com a CENDORA™ cozinham de forma uniforme mesmo em lume brando e lavam-se num instante. Pela quantia que paguei, a qualidade surpreendeu-me.»",
            "rev2_h": "Completo, sólido e com um preço que surpreende.",
            "rev2_p": "«Quando vêm filhos e netos, cozinho para muita gente. As capacidades são práticas, as pegas inspiram confiança e as tampas fecham bem. Não esperava qualidade tão alta por este valor.»",
            "rev3_h": "Uso todos os dias e não me arrependo.",
            "rev3_p": "«Mãe de dois rapazes já adultos, continuo a cozinhar para toda a família. O calor chega igual a todo o lado, nada cola ao centro e a lavagem é rápida. Resistentes, bonitas e económicas: voltaria a encomendar amanhã.»",
            "author1": "Chiara B. — Porto, compra verificada",
            "author2": "Giulia M. — Coimbra, compra verificada",
            "author3": "Elena R. — Faro, compra verificada",
            "alt_t1": "Unboxing do conjunto CENDORA™ de 12 peças",
            "alt_t2": "CENDORA™ no fogão durante o jantar",
            "alt_t3": "Cozinha do dia a dia com CENDORA™",
            "alt_w1": "CENDORA™ em uso: vários pratos a cozinhar em simultâneo",
            "alt_w2": "Fundo CENDORA™: calor distribuído uniformemente",
            "alt_w3": "CENDORA™: limpeza manual ou na máquina de lavar loiça",
            "kit_eye": "Conteúdo da caixa",
            "kit_h": "Conjunto CENDORA™ 12 peças, pronto a usar",
            "kit_li1": "Panela 7 L com tampa — caldos e porções grandes",
            "kit_li2": "Panela 3 L com tampa — molhos e pratos do dia a dia",
            "kit_li3": "Caçarola 1,5 L com tampa — acompanhamentos e doses individuais",
            "kit_li4": "Frigideira funda 3,5 L com pega de apoio",
            "kit_li5": "Duas frigideiras: 20 cm e 28 cm",
            "kit_li6": "Cesto para cozedura a vapor com tampa",
            "kit_li7": "Pegas reforçadas para pegada estável",
            "kit_li8": "Manual de instruções e certificado de garantia",
            "kit_li9": "Garantia do fabricante 24 meses",
            "alt_kit": "Lista completa do conjunto CENDORA™",
            "faq_h": "Perguntas frequentes",
            "faq1_q": "Quanto tempo demora a entrega?",
            "faq1_a": "Em geral 2–4 dias úteis. Após o pedido contactamo-lo para confirmar morada e envio.",
            "faq2_q": "Quando pago a encomenda?",
            "faq2_a": "Na entrega entrega {price} em dinheiro ao estafeta.",
            "faq3_q": "Funciona em indução?",
            "faq3_a": "Sim. O fundo compatível serve em gás, elétrico, vitrocerâmica e indução.",
            "faq4_q": "Posso usar as panelas no forno?",
            "faq4_a": "Sim, até 230°C — ideal para gratinar ou terminar a cozedura no mesmo recipiente.",
            "faq5_q": "E se não ficar convencido?",
            "faq5_a": "Tem 30 dias após a entrega para pedir devolução segundo a nossa política de reembolso.",
            "ty_title": "Encomenda registada — Aguarde a chamada de confirmação | CENDORA™",
            "ty_desc": "A sua encomenda CENDORA™ está registada. Para iniciar o envio, responda à chamada de confirmação do nosso operador.",
            "ty_h1": "Encomenda recebida com sucesso!",
            "ty_sub": "Ótimo — estamos a preparar o envio. Falta ainda <strong>um passo</strong>: a confirmação telefónica.",
            "ty_order_header": "🛒 A sua encomenda",
            "ty_product": "CENDORA™ — Conjunto de cozinha antiaderente de 12 peças",
            "ty_pay": "Pagamento na entrega: {price}",
            "ty_eyebrow": "👇 Próximo passo",
            "ty_action_title": "📞 Aguarde e atenda a chamada de confirmação",
            "ty_action_body": "Um operador ligará <strong>em breve</strong> para verificar os dados da encomenda.",
            "ty_action_warn": "Se não atender, a encomenda pode ser cancelada automaticamente.",
            "ty_hours_h": "🕒 Horário de contacto",
            "ty_hours": "<strong>Segunda – Sábado</strong> · 9:00 – 18:00",
            "ty_next_h": "📋 O que acontece a seguir",
            "ty_steps": [
                "Atenda à chamada e <strong>confirme os seus dados</strong>",
                "A encomenda será preparada em <strong>24–48 horas</strong>",
                "Receba a encomenda em casa e <strong>pague na entrega</strong>",
            ],
            "ty_badges": (
                "🔒 Pagamento na entrega",
                "🛡️ Garantia 24 meses",
                "🔐 Proteção SSL",
            ),
            "footer_tagline": "Produtos selecionados para casa, jardim e dia a dia. Pagamento na entrega em 18 países europeus.",
            "footer_powered_top": "shoptrendcrest.com — Oferecido por WHATECH MOBILE CO., LIMITED",
            "footer_powered_bottom": "shoptrendcrest.com — Oferecido por WHATECH MOBILE CO., LIMITED. Todos os direitos reservados.",
            "info": "Informações",
            "about": "Sobre nós",
            "contact": "Contacte-nos",
            "contacts": "Contactos",
            "privacy": "Política de privacidade",
            "terms": "Termos e condições",
            "cookie": "Política de cookies",
            "ship": "Política de envio",
            "refund": "Política de devolução",
            "rights": "Todos os direitos reservados",
        },
    )


# Additional locales: start from Romanian pack and apply full localized patches (same keys as IT_STRINGS).
# Slavic/Baltic copies reuse structure with localized country + form UI from align script.

def _es() -> dict[str, StrOrSeq]:
    return _apply(
        _pt(),
        {
            "title": "CENDORA™ — Batería de cocina antiadherente, 12 piezas",
            "description": "CENDORA™: batería de 12 piezas con revestimiento antiadherente efecto piedra, fondo que calienta de forma uniforme, apta para inducción y lavavajillas. Pago contra reembolso en España.",
            "rating": "<strong>4,9/5</strong> — Más de <strong>6.500</strong> familias en España ya han elegido CENDORA™",
            "topbar": "🔥 −50% EN LA BATERÍA DE COCINA — SOLO HOY — PAGO CONTRA REEMBOLSO · ENVÍO GRATIS 🔥",
            "f1_p": "Entrega en toda España",
            "cta": "QUIERO CENDORA™ →",
            "cta_inline": "QUIERO CENDORA™ →",
            "form_note_hero": "🔒 Envío rápido · Pagas al mensajero · Devolución en 30 días",
            "form_note_form": "🔒 Pago contra reembolso · Devolución en 30 días",
            "submit_btn": "ENVIAR SOLICITUD",
            "form_h2": "Finaliza tu solicitud",
            "form_p": "Rellena el formulario con tus datos. Te llamaremos para confirmar el pedido y organizar la entrega en casa.",
            "countdown": "⏰ La promoción del −50% termina en",
            "live": "<strong>{n} personas</strong> están viendo CENDORA™ ahora mismo",
            "live0": "<strong>34 personas</strong> están viendo CENDORA™ ahora mismo",
            "faq2_a": "En la entrega entregas {price} en efectivo al mensajero.",
            "ty_pay": "Pago contra reembolso: {price}",
            "ty_steps": [
                "Responde a la llamada y <strong>confirma tus datos</strong>",
                "Tu pedido se preparará en <strong>24–48 horas</strong>",
                "Recibe el paquete en casa y <strong>paga contra reembolso</strong>",
            ],
            "ty_badges": (
                "🔒 Pago contra reembolso",
                "🛡️ Garantía 24 meses",
                "🔐 Protección SSL",
            ),
            "footer_tagline": "Productos seleccionados para hogar, jardín y día a día. Pago contra reembolso en 18 países europeos.",
            "author1": "Chiara B. — Madrid, compra verificada",
            "author2": "Giulia M. — Valencia, compra verificada",
            "author3": "Elena R. — Sevilla, compra verificada",
        },
    )


def _de() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "submitting": "Wird gesendet...",
            "cookie_text": "Wir verwenden technische Cookies und Cookies von Drittanbietern, um die Navigation zu verbessern und für statistische Analysen.",
            "cookie_accept": "Akzeptieren",
            "cookie_learn": "Mehr erfahren",
            "title": "CENDORA™ — Antihaft-Küchenset, 12 Teile",
            "description": "CENDORA™: 12-teiliges Set mit Steinoptik-Antihaftbeschichtung, gleichmäßig erwärmender Boden, geeignet für Induktion und Spülmaschine. Zahlung bei Lieferung in Deutschland.",
            "og_title": "CENDORA™ — Stabile Temperatur auf jedem Herd",
            "og_description": "Antihaft ohne PTFE und PFOA: weniger Fett, gleichmäßiges Garen, schnelle Reinigung und Kompatibilität mit Gas, Ceran und Induktion.",
            "topbar": "🔥 −50% AUF DAS KÜCHENSET — NUR HEUTE — ZAHLUNG BEI LIEFERUNG · KOSTENLOSER VERSAND 🔥",
            "rating": "<strong>4,9/5</strong> — Mehr als <strong>6.500</strong> Familien in Deutschland haben CENDORA™ bereits gewählt",
            "gift": "🎁 GRATIS: Küchenutensilien + Premium-Tuch",
            "h1_mobile": "Bis zu <span class=\"hl\">9.000 Mikroplastikpartikel</span> können im Essen landen, das Sie servieren – Zeit, den Topf zu wechseln.",
            "h1_desktop": "Mit gewöhnlichen Antihaftpfannen können bis zu <span class=\"hl\">9.000 Plastikpartikel</span> auf dem Teller Ihrer Liebsten landen. Schützen Sie Ihre Familie: wechseln Sie zu CENDORA™.",
            "lead": "Steinoptik-Antihaftbeschichtung ohne PTFE und PFOA. Essen haftet nicht, Sie brauchen weniger Öl und die Hitze verteilt sich gleichmäßig. Für alle Herdarten, auch Induktion. Offizielle 24-Monate-Garantie.",
            "cta": "ICH WILL CENDORA™ →",
            "cta_inline": "ICH WILL CENDORA™ →",
            "form_note_hero": "🔒 Schneller Versand · Zahlung an den Boten · 30 Tage Rückgabe",
            "form_note_form": "🔒 Zahlung bei Lieferung · 30 Tage Rückgabe",
            "f1_h": "Schneller Versand",
            "f1_p": "Lieferung in ganz Deutschland",
            "f2_h": "Geschützte Bestellung",
            "f2_p": "Ihre Daten bleiben sicher",
            "f3_h": "Zertifizierte Materialien",
            "f3_p": "Antihaft für den täglichen Gebrauch",
            "f4_h": "30 Tage Rückgabe",
            "f4_p": "Klarer Ablauf, wenn Sie nicht überzeugt sind",
            "countdown": "⏰ Die −50%-Aktion endet in",
            "hours": "Std",
            "mins": "Min",
            "secs": "Sek",
            "stock_l": "Lagerbestand",
            "stock_r": "Nur noch 5 Sets verfügbar",
            "live": "<strong>{n} Personen</strong> sehen sich CENDORA™ gerade an",
            "live0": "<strong>34 Personen</strong> sehen sich CENDORA™ gerade an",
            "form_h2": "Anfrage abschließen",
            "form_p": "Füllen Sie das Formular aus. Wir rufen Sie an, um die Bestellung zu bestätigen und die Lieferung nach Hause zu organisieren.",
            "submit_btn": "ANFRAGE SENDEN",
            "faq2_a": "Bei Lieferung geben Sie dem Boten {price} in bar.",
            "ty_pay": "Zahlung bei Lieferung: {price}",
            "ty_steps": [
                "Nehmen Sie den Anruf an und <strong>bestätigen Sie Ihre Daten</strong>",
                "Ihre Bestellung wird innerhalb von <strong>24–48 Stunden</strong> vorbereitet",
                "Sie erhalten das Paket zu Hause und <strong>zahlen bei Lieferung</strong>",
            ],
            "ty_badges": (
                "🔒 Zahlung bei Lieferung",
                "🛡️ 24 Monate Garantie",
                "🔐 SSL-Schutz",
            ),
            "footer_tagline": "Ausgewählte Produkte für Haus, Garten und Alltag. Zahlung bei Lieferung in 18 europäischen Ländern.",
            "footer_powered_top": "shoptrendcrest.com — Angeboten von WHATECH MOBILE CO., LIMITED",
            "footer_powered_bottom": "shoptrendcrest.com — Angeboten von WHATECH MOBILE CO., LIMITED. Alle Rechte vorbehalten.",
            "info": "Informationen",
            "about": "Über uns",
            "contact": "Kontakt",
            "contacts": "Kontakt",
            "privacy": "Datenschutz",
            "terms": "AGB",
            "cookie": "Cookie-Richtlinie",
            "ship": "Versandrichtlinie",
            "refund": "Rückgaberichtlinie",
            "rights": "Alle Rechte vorbehalten",
        },
    )


# For remaining geos, use Romanian base with localized hero/legal/country strings.
def _sk() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — Súprava nepriľnavých hrncov, 12 dielov",
            "description": "CENDORA™: 12-dielna súprava s nepriľnavým povlakom s efektom kameňa, rovnomerne sa zahrievajúce dno, vhodná na indukciu a do umývačky. Platba na dobierku na Slovensku.",
            "rating": "<strong>4,9/5</strong> — Viac ako <strong>6 500</strong> domácností na Slovensku si už vybralo CENDORA™",
            "topbar": "🔥 −50% NA KUCHYNSKÚ SÚPRAVU — LEN DNES — PLATBA NA DOBIERKU · DOPRAVA ZADARMO 🔥",
            "f1_p": "Doručenie po celom Slovensku",
            "faq2_a": "Pri doručení odovzdáte kuriérovi {price} v hotovosti.",
            "ty_pay": "Platba na dobierku: {price}",
            "ty_badges": ("🔒 Platba na dobierku", "🛡️ 24 mesiacov záruky", "🔐 Ochrana SSL"),
        },
    )


def _si() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — Komplet nelepljive posode, 12 kosov",
            "description": "CENDORA™: 12-delni komplet z nelepljivo oblogo v videzu kamna, enakomerno segrevano dno, primerno za indukcijo in pomivalni stroj. Plačilo po povzetju v Sloveniji.",
            "rating": "<strong>4,9/5</strong> — Več kot <strong>6.500</strong> gospodinjstev v Sloveniji je že izbralo CENDORA™",
            "topbar": "🔥 −50% NA KUHINJSKI KOMPLET — SAMO DANES — PLAČILO PO POVZETJU · BREZPLAČNA DOSTAVA 🔥",
            "f1_p": "Dostava po vsej Sloveniji",
            "faq2_a": "Ob dostavi kurirju predate {price} v gotovini.",
            "ty_pay": "Plačilo po povzetju: {price}",
            "ty_badges": ("🔒 Plačilo po povzetju", "🛡️ 24 mesecev garancije", "🔐 Zaščita SSL"),
        },
    )


def _hr() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — Set neprijanjajućeg posuđa, 12 komada",
            "description": "CENDORA™: set od 12 komada s neprijanjajućim premazom efekta kamena, ravnomjerno zagrijano dno, prikladan za indukciju i perilicu posuđa. Plaćanje pouzećem u Hrvatskoj.",
            "rating": "<strong>4,9/5</strong> — Više od <strong>6.500</strong> obitelji u Hrvatskoj već je odabralo CENDORA™",
            "topbar": "🔥 −50% NA KUHINJSKI SET — SAMO DANAS — PLAĆANJE POUZEĆEM · BESPLATNA DOSTAVA 🔥",
            "f1_p": "Dostava u cijeloj Hrvatskoj",
            "faq2_a": "Pri dostavi kuriru predajte {price} u gotovini.",
            "ty_pay": "Plaćanje pouzećem: {price}",
            "ty_badges": ("🔒 Plaćanje pouzećem", "🛡️ Jamstvo 24 mjeseca", "🔐 SSL zaštita"),
        },
    )


def _hu() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — 12 részes bevonatos edényszett",
            "description": "CENDORA™: 12 részes készlet kőhatású bevonattal, egyenletesen melegedő talppal, indukcióhoz és mosogatógéphez is. Utánvét Magyarországon.",
            "rating": "<strong>4,9/5</strong> — Több mint <strong>6 500</strong> család választotta már a CENDORA™ terméket Magyarországon",
            "topbar": "🔥 −50% A KONYHAI SZETTRE — CSAK MA — UTÁNVÉT · INGYENES SZÁLLÍTÁS 🔥",
            "f1_p": "Szállítás egész Magyarországon",
            "faq2_a": "Átvételkor {price} összeget ad át készpénzben a futárnak.",
            "ty_pay": "Utánvét: {price}",
            "ty_badges": ("🔒 Utánvét", "🛡️ 24 hónap garancia", "🔐 SSL védelem"),
        },
    )


def _pl() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — Zestaw garnków z powłoką nieprzywierającą, 12 elementów",
            "description": "CENDORA™: 12-elementowy zestaw z powłoką nieprzywierającą o efekcie kamienia, równomiernie nagrzewającym się dnem, do indukcji i zmywarki. Płatność przy odbiorze w Polsce.",
            "rating": "<strong>4,9/5</strong> — Ponad <strong>6 500</strong> rodzin w Polsce wybrało już CENDORA™",
            "topbar": "🔥 −50% NA ZESTAW KUCHENNY — TYLKO DZIŚ — PŁATNOŚĆ PRZY ODBIORZE · DARMOWA DOSTAWA 🔥",
            "f1_p": "Dostawa w całej Polsce",
            "faq2_a": "Przy dostawie przekazujesz kurierowi {price} gotówką.",
            "ty_pay": "Płatność przy odbiorze: {price}",
            "ty_badges": ("🔒 Płatność przy odbiorze", "🛡️ Gwarancja 24 miesiące", "🔐 Ochrona SSL"),
        },
    )


def _cs() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — Sada nepřilnavého nádobí, 12 dílů",
            "description": "CENDORA™: 12dílná sada s nepřilnavým povlakem s efektem kamene, rovnoměrně se zahřívajícím dnem, vhodná pro indukci a myčku. Platba na dobírku v Česku.",
            "rating": "<strong>4,9/5</strong> — Více než <strong>6 500</strong> domácností v Česku si už vybralo CENDORA™",
            "topbar": "🔥 −50% NA KUCHYŇSKOU SADU — POUZE DNES — PLATBA NA DOBÍRKU · DOPRAVA ZDARMA 🔥",
            "f1_p": "Doručení po celé České republice",
            "faq2_a": "Při doručení předáte kurýrovi {price} v hotovosti.",
            "ty_pay": "Platba na dobírku: {price}",
            "ty_badges": ("🔒 Platba na dobírku", "🛡️ 24 měsíců záruky", "🔐 Ochrana SSL"),
        },
    )


def _lt() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — 12 dalių neprilimpančio indų rinkinys",
            "description": "CENDORA™: 12 dalių rinkinys su akmenėlės efekto neprilimančia danga, tolygiai įkaistančiu dugnu, tinkamas indukcijai ir indaplovei. Apmokėjimas pristatymo metu Lietuvoje.",
            "rating": "<strong>4,9/5</strong> — Daugiau nei <strong>6 500</strong> šeimų Lietuvoje jau pasirinko CENDORA™",
            "topbar": "🔥 −50% INDŲ RINKINIUI — TIK ŠIANDIEN — APMOKĖJIMAS PRISTATYMO METU · NEMOKAMAS PRISTATYMAS 🔥",
            "f1_p": "Pristatymas visoje Lietuvoje",
            "faq2_a": "Pristatymo metu kurjeriui įteikiate {price} grynaisiais.",
            "ty_pay": "Apmokėjimas pristatymo metu: {price}",
            "ty_badges": ("🔒 Apmokėjimas pristatymo metu", "🛡️ 24 mėn. garantija", "🔐 SSL apsauga"),
        },
    )


def _lv() -> dict[str, StrOrSeq]:
    return _apply(
        _ro(),
        {
            "title": "CENDORA™ — 12 daļu pannu un katlu komplekts ar antiaderentu pārklājumu",
            "description": "CENDORA™: 12 daļu komplekts ar akmens efekta antiaderentu pārklājumu, vienmērīgi uzkarstošu pamatni, piemērots indukcijai un trauku mašīnai. Apmaksa piegādes brīdī Latvijā.",
            "rating": "<strong>4,9/5</strong> — Vairāk nekā <strong>6 500</strong> ģimenes Latvijā jau ir izvēlējušās CENDORA™",
            "topbar": "🔥 −50% VIRTUVES KOMPLEKTAM — TIKAI ŠODIEN — APMAKSA PIEGĀDES BRĪDĪ · BEZMAKSAS PIEGĀDE 🔥",
            "f1_p": "Piegāde visā Latvijā",
            "faq2_a": "Piegādes brīdī kurjeram nododat {price} skaidrā naudā.",
            "ty_pay": "Apmaksa piegādes brīdī: {price}",
            "ty_badges": ("🔒 Maksa piegādes brīdī", "🛡️ 24 mēnešu garantija", "🔐 SSL aizsardzība"),
        },
    )


NATIVE_PACKS: dict[str, dict[str, Any]] = {
    "ro": _ro(),
    "pt": _pt(),
    "es": _es(),
    "de": _de(),
    "sk": _sk(),
    "si": _si(),
    "hr": _hr(),
    "hu": _hu(),
    "pl": _pl(),
    "cs": _cs(),
    "lt": _lt(),
    "lv": _lv(),
}
