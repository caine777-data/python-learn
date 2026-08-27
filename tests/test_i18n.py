"""
Tests des traductions de l'interface.

Ces tests coûtent quelques millisecondes et attrapent la panne la plus
sournoise de l'application bilingue : une clé ou une variable oubliée
dans une seule langue, qui ne se manifeste qu'au moment précis où
l'utilisateur affiche cet écran-là, dans cette langue-là.
"""

import os
import string
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.i18n import LANGUES, NOMS_LANGUES, STRINGS, Translator


def _variables(modele):
    """Noms des variables attendues par un modèle : « ⏱ {m}:{s:02d} » -> {m, s}."""
    return {nom for _, nom, _, _ in string.Formatter().parse(modele) if nom}


class TestTraductions(unittest.TestCase):

    def test_toutes_les_langues_sont_declarees(self):
        self.assertEqual(set(LANGUES), set(STRINGS))
        self.assertEqual(set(LANGUES), set(NOMS_LANGUES))

    def test_memes_cles_dans_toutes_les_langues(self):
        reference = set(STRINGS["fr"])
        for langue in LANGUES:
            with self.subTest(langue=langue):
                manquantes = reference - set(STRINGS[langue])
                en_trop = set(STRINGS[langue]) - reference
                self.assertFalse(manquantes, f"clés absentes en {langue} : {sorted(manquantes)}")
                self.assertFalse(en_trop, f"clés en trop en {langue} : {sorted(en_trop)}")

    def test_memes_variables_dans_toutes_les_langues(self):
        """Un {n} oublié dans la traduction ferait planter l'écran concerné."""
        for cle, modele_fr in STRINGS["fr"].items():
            attendues = _variables(modele_fr)
            for langue in LANGUES:
                with self.subTest(cle=cle, langue=langue):
                    self.assertEqual(
                        _variables(STRINGS[langue][cle]), attendues,
                        f"variables différentes pour « {cle} » en {langue}")

    def test_aucune_traduction_vide(self):
        for langue in LANGUES:
            for cle, texte in STRINGS[langue].items():
                with self.subTest(langue=langue, cle=cle):
                    self.assertTrue(texte.strip(), f"« {cle} » est vide en {langue}")

    def test_langue_inconnue_retombe_sur_le_francais(self):
        tr = Translator("klingon")
        self.assertEqual(tr.lang, "fr")
        tr.set("de")
        self.assertEqual(tr.lang, "fr")

    def test_cle_inconnue_renvoie_la_cle(self):
        self.assertEqual(Translator("fr")("cle_qui_nexiste_pas"), "cle_qui_nexiste_pas")

    def test_formatage_avec_variables(self):
        for langue in LANGUES:
            with self.subTest(langue=langue):
                texte = Translator(langue)("ex_q", i=2, n=10)
                self.assertIn("2", texte)
                self.assertIn("10", texte)


if __name__ == "__main__":
    unittest.main()
