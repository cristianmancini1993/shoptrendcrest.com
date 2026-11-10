# -*- coding: utf-8 -*-
from _taigor_assemble import build_locale
from _taigor_phrases_all import PHRASES

TAIGOR_CORE = {code: build_locale(PHRASES[code]) for code in PHRASES}
