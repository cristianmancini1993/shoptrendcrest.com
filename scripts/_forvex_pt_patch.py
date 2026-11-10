# -*- coding: utf-8 -*-
"""European Portuguese copy overrides for FORVEX."""

PT_PATCH: dict[str, str] = {
    "cta": "ENCOMENDAR FORVEX™ AGORA →",
    "label_name": "Nome completo*",
    "ph_name": "Nome completo",
    "label_addr": "Morada*",
    "ph_addr": "Morada",
    "submit_btn": "Encomendar agora",
    "form_p": "Indique nome, telefone e morada. Ligamos em 24 h para combinar a entrega — não cobramos nada antecipadamente.",
    "gift": "🔋 Pack: dupla bateria, carregador rápido e acessórios de oferta",
    "topbar": "PROMO FLASH · −50 % · ENVIO GRÁTIS · PAGAMENTO À COBRANÇA",
    "f1_p": "Entrega em todo Portugal",
    "f2_p": "Só dinheiro, sem cartão",
    "faq2_q": "Pago online?",
    "faq2_a": "Não: {price} em dinheiro ao estafeta quando recebe o FORVEX™.",
    "form_note": "💶 Sem pagamento online: paga {price} ao estafeta ao abrir a encomenda",
}


def apply_pt_patch(bundle: dict) -> dict:
    out = dict(bundle)
    out.update(PT_PATCH)
    return out
