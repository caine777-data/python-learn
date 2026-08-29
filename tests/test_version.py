"""
Cohérence du numéro de version.

Il apparaît à trois endroits qui ne peuvent pas s'importer les uns les
autres : le code Python, les métadonnées du projet, et le script de
l'installateur Windows. Rien n'empêche donc de n'en mettre qu'un à jour —
et l'oubli ne se verrait qu'au moment de publier, quand la CI refuse le
tag ou, pire, quand l'installateur annonce une version périmée.

Ces tests lisent les fichiers en texte brut, sans tomllib : le projet
prend en charge Python 3.10, qui ne l'a pas.
"""

import os
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.version import __version__

RACINE = Path(__file__).resolve().parent.parent


def _extraire(fichier, motif):
    texte = (RACINE / fichier).read_text(encoding="utf-8")
    trouve = re.search(motif, texte, re.MULTILINE)
    return trouve.group(1) if trouve else None


class TestVersion(unittest.TestCase):

    def test_format_semantique(self):
        self.assertRegex(__version__, r"^\d+\.\d+\.\d+$",
                         "la version doit s'écrire X.Y.Z (le tag Git en dépend)")

    def test_pyproject_est_aligne(self):
        declaree = _extraire("pyproject.toml", r'^version\s*=\s*"([^"]+)"')
        self.assertEqual(
            declaree, __version__,
            "pyproject.toml et app/version.py annoncent des versions différentes")

    def test_installateur_windows_est_aligne(self):
        declaree = _extraire("packaging/installer.iss",
                             r'#define\s+MaVersion\s+"([^"]+)"')
        self.assertEqual(
            declaree, __version__,
            "packaging/installer.iss et app/version.py divergent : "
            "l'installateur afficherait un mauvais numéro")

    def test_identite_complete(self):
        from app.version import APP_NAME, AUTEUR, DEPOT
        for nom, valeur in (("APP_NAME", APP_NAME), ("AUTEUR", AUTEUR),
                            ("DEPOT", DEPOT)):
            with self.subTest(champ=nom):
                self.assertTrue(valeur and valeur.strip(), f"{nom} est vide")


if __name__ == "__main__":
    unittest.main()
