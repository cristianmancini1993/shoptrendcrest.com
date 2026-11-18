"""Localized AI image disclaimer for landing footers (visible paragraph, not a link)."""
from __future__ import annotations

import re
from xml.sax.saxutils import escape

try:
    from ai_image_notice_i18n import BY_LANG, notice_text_for_lang, strip_ai_notice_paragraphs
except ImportError:
    from scripts.ai_image_notice_i18n import BY_LANG, notice_text_for_lang, strip_ai_notice_paragraphs

MARKER = "<!-- AI_MEDIA_NOTICE -->"
PARAGRAPH_CLASS_DEFAULT = "site-footer__ai-notice"
PARAGRAPH_CLASS_VARENO = "hubaura-standalone-footer__ai-media-notice"

FOOT_AI_MEDIA_NOTICE: dict[str, str] = BY_LANG


def foot_ai_text(locale_key: str) -> str:
    return notice_text_for_lang(locale_key)


def paragraph_html(text: str, paragraph_class: str = PARAGRAPH_CLASS_DEFAULT) -> str:
    if not (text or "").strip():
        return ""
    if paragraph_class == PARAGRAPH_CLASS_DEFAULT:
        return f'<p class="{paragraph_class}" data-ai-disclosure="1">{escape(text.strip())}</p>'
    return f'<p class="{paragraph_class}">{escape(text.strip())}</p>'


def patch_footer_ai_notice(
    html: str,
    locale_key: str,
    *,
    text_override: str | None = None,
    paragraph_class: str = PARAGRAPH_CLASS_DEFAULT,
    include_standalone_vareno: bool = False,
) -> str:
    text = (text_override or "").strip() or foot_ai_text(locale_key)
    para = paragraph_html(text, paragraph_class)
    if MARKER in html:
        return html.replace(MARKER, para, 1)
    pattern = re.compile(
        rf'<p class="{re.escape(paragraph_class)}"[^>]*>[\s\S]*?</p>\s*',
        re.IGNORECASE,
    )
    if pattern.search(html):
        return pattern.sub(para + "\n", html, count=1) if para else pattern.sub("", html, count=1)
    if para and '</p>\n      </div>\n      <div>\n        <h4 class="site-footer__heading">' in html:
        return html.replace(
            '</p>\n      </div>\n      <div>\n        <h4 class="site-footer__heading">',
            f'</p>\n        {para}\n      </div>\n      <div>\n        <h4 class="site-footer__heading">',
            1,
        )
    if para:
        blurb_m = re.search(
            r'(<p class="site-footer__blurb">[\s\S]*?</p>)(\s*)',
            html,
        )
        if blurb_m and paragraph_class not in html[blurb_m.end() : blurb_m.end() + 500]:
            return (
                html[: blurb_m.end()]
                + "\n        "
                + para
                + html[blurb_m.end() :]
            )
    if include_standalone_vareno:
        html = patch_vareno_standalone_footer(html, locale_key)
    return html


def patch_ai_media_notice(html: str, lang: str, loc: dict | None = None, **kwargs) -> str:
    override = ((loc or {}).get("foot_ai_media_notice") or "").strip() or None
    return patch_footer_ai_notice(html, lang, text_override=override, **kwargs)


def strip_ai_media_notice(html: str) -> str:
    html = strip_ai_notice_paragraphs(html)
    return html.replace(MARKER, "")


def patch_vareno_standalone_footer(html: str, locale_key: str) -> str:
    text = foot_ai_text(locale_key)
    para = paragraph_html(text, PARAGRAPH_CLASS_VARENO)
    if not para:
        return html
    needle = '</p>\n      </div>\n      <div>\n        <h4 class="hubaura-standalone-footer__heading">'
    if needle in html and f'class="{PARAGRAPH_CLASS_VARENO}"' not in html:
        return html.replace(
            needle,
            f"</p>\n        {para}\n      </div>\n      <div>\n        <h4 class=\"hubaura-standalone-footer__heading\">",
            2,
        )
    return html


def patch_fold360_footer_blurb(html: str, locale_key: str) -> str:
    text = foot_ai_text(locale_key)
    para = paragraph_html(text, PARAGRAPH_CLASS_DEFAULT)
    if not para:
        return html
    m = re.search(
        r'(<p style="margin-top:1rem;max-width:340px">[\s\S]*?</p>)(\s*)',
        html,
    )
    if m and PARAGRAPH_CLASS_DEFAULT not in html[m.end() : m.end() + 400]:
        return html[: m.end()] + "\n        " + para + html[m.end() :]
    return html
