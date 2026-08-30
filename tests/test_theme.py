"""
Tests des thèmes et palettes de couleurs de l'application.
"""

import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.theme import THEME_ORDER, THEMES, assombrir, eclaircir, melange

_HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")

REQUIRED_KEYS = {
    "label", "label_en", "bg", "panel", "editor", "console",
    "fg", "accent", "ok", "err", "muted", "heading", "code",
    "code_bg", "sel_fg", "curline", "kw", "builtin", "num",
    "deff", "str", "com"
}


class TestThemes(unittest.TestCase):

    def test_theme_order_contient_tous_les_themes(self):
        self.assertEqual(set(THEME_ORDER), set(THEMES.keys()))

    def test_tous_les_themes_ont_les_cles_requises(self):
        for nom, t in THEMES.items():
            with self.subTest(theme=nom):
                manquantes = REQUIRED_KEYS - set(t.keys())
                self.assertFalse(manquantes, f"Clés manquantes dans {nom} : {manquantes}")

    def test_validite_des_couleurs_hex(self):
        for nom, t in THEMES.items():
            for cle, val in t.items():
                if cle in ("label", "label_en"):
                    continue
                with self.subTest(theme=nom, key=cle):
                    self.assertTrue(_HEX_COLOR.match(val), f"Couleur invalide pour {nom}.{cle} : {val}")

    def test_melange_et_assombrir_eclaircir(self):
        c1 = "#000000"
        c2 = "#ffffff"
        self.assertEqual(melange(c1, c2, 0.5), "#808080")
        self.assertTrue(_HEX_COLOR.match(eclaircir("#1a1b26", 0.1)))
        self.assertTrue(_HEX_COLOR.match(assombrir("#1a1b26", 0.1)))


if __name__ == "__main__":
    unittest.main()
