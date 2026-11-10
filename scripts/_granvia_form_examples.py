#!/usr/bin/env python3
"""Canonical Granvia™ geo form labels + local placeholder examples (single source of truth)."""
from __future__ import annotations

# Buyer-confirmed examples — placeholders only, never input values.
GRANVIA_FORM_EXAMPLES: dict[str, dict[str, str]] = {
    "es": {
        "ph_name": "María García López",
        "ph_tel": "+34 612 34 56 78",
        "ph_addr": "Calle Mayor 12, 28013 Madrid",
    },
    "pt": {
        "ph_name": "João Silva Santos",
        "ph_tel": "+351 912 345 678",
        "ph_addr": "Rua Augusta 45, 1100-053 Lisboa",
    },
    "de": {
        "ph_name": "Hans Müller",
        "ph_tel": "+49 151 23456789",
        "ph_addr": "Friedrichstraße 12, 10117 Berlin",
    },
    "lt": {
        "ph_name": "Jonas Kazlauskas",
        "ph_tel": "+370 612 34567",
        "ph_addr": "Gedimino pr. 12, 01103 Vilnius",
    },
    "hu": {
        "ph_name": "Kovács Anna",
        "ph_tel": "+36 30 123 4567",
        "ph_addr": "Váci utca 15, 1052 Budapest",
    },
    "cs": {
        "ph_name": "Jan Novák",
        "ph_tel": "+420 777 123 456",
        "ph_addr": "Václavské náměstí 12, 110 00 Praha",
    },
}

GRANVIA_NAME_LABEL_OVERRIDES: dict[str, str] = {
    "cs": "Jméno a příjmení*",
}

FIELD_ORDER = ("name", "tel", "street-address")
