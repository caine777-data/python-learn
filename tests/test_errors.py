"""
Tests des explications pédagogiques d'erreurs.

Le test qui compte vraiment est le dernier : il provoque de véritables
erreurs dans le moteur d'exécution, puis vérifie qu'un conseil existe
pour chacune. C'est ce qui garantit qu'un apprenant bloqué reçoit une
explication, et pas seulement le message brut de l'interpréteur.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.errors import CONSEILS, expliquer
from app.i18n import LANGUES
from app.runner import run_code

# Un bout de code fautif par type d'erreur courant chez un débutant.
CODES_FAUTIFS = [
    ("NameError", "print(variable_inconnue)"),
    ("TypeError", "resultat = 1 + 'texte'"),
    ("ValueError", "nombre = int('abc')"),
    ("ZeroDivisionError", "resultat = 1 / 0"),
    ("IndexError", "liste = [1, 2]\nprint(liste[5])"),
    ("KeyError", "dico = {'a': 1}\nprint(dico['b'])"),
    ("AttributeError", "texte = 'salut'\ntexte.methode_inexistante()"),
    ("ModuleNotFoundError", "import module_qui_nexiste_pas"),
    ("AssertionError", "assert 1 == 2"),
    ("SyntaxError", "if True\n    print('oui')"),
    ("IndentationError", "if True:\nprint('oui')"),
    ("RecursionError", "def f():\n    return f()\nf()"),
]


class TestExplications(unittest.TestCase):

    def test_memes_erreurs_couvertes_dans_toutes_les_langues(self):
        reference = set(CONSEILS["fr"])
        for langue in LANGUES:
            with self.subTest(langue=langue):
                self.assertIn(langue, CONSEILS, f"langue {langue} absente")
                self.assertEqual(set(CONSEILS[langue]), reference)

    def test_aucun_conseil_vide(self):
        for langue, conseils in CONSEILS.items():
            for erreur, texte in conseils.items():
                with self.subTest(langue=langue, erreur=erreur):
                    self.assertTrue(texte.strip())

    def test_erreur_inconnue_renvoie_none(self):
        self.assertIsNone(expliquer("ErreurQuiNexistePas: détail"))
        self.assertIsNone(expliquer(""))
        self.assertIsNone(expliquer(None))

    def test_langue_inconnue_retombe_sur_le_francais(self):
        self.assertEqual(expliquer("NameError: x", "klingon"),
                         expliquer("NameError: x", "fr"))

    def test_erreurs_reelles_du_moteur_sont_toutes_expliquees(self):
        """Chaque erreur qu'un débutant peut provoquer doit être expliquée."""
        for attendu, code in CODES_FAUTIFS:
            with self.subTest(erreur=attendu):
                resultat, _ = run_code(code)
                self.assertIsNotNone(resultat.error, f"{code!r} aurait dû échouer")
                self.assertIn(attendu, resultat.error,
                              f"attendu {attendu}, obtenu : {resultat.error}")
                for langue in LANGUES:
                    conseil = expliquer(resultat.error, langue)
                    self.assertIsNotNone(conseil, f"conseil manquant en {langue} pour {attendu}")
                    self.assertTrue(len(conseil) > 10, f"conseil trop court en {langue} pour {attendu}")
                    # Vérifie aussi le conseil générique direct
                    self.assertEqual(expliquer(f"{attendu}: msg", langue), CONSEILS[langue][attendu])

    def test_astuces_syntaxe_et_noms_intelligentes(self):
        msg_eq = "SyntaxError: invalid syntax. Maybe you meant '==' instead of '='?"
        self.assertIn("==", expliquer(msg_eq, "fr"))
        self.assertIn("==", expliquer(msg_eq, "en"))

        msg_colon = "SyntaxError: expected ':'"
        self.assertIn(":", expliquer(msg_colon, "fr"))
        self.assertIn(":", expliquer(msg_colon, "en"))

        msg_name = "NameError: name 'longuer' is not defined. Did you mean: 'longueur'?"
        self.assertIn("longueur", expliquer(msg_name, "fr"))
        self.assertIn("longueur", expliquer(msg_name, "en"))

    def test_boucle_infinie_est_interrompue_et_expliquee(self):
        resultat, _ = run_code("while True:\n    pass\n", timeout=1.0)
        self.assertTrue(resultat.timed_out)
        self.assertTrue(resultat.error.startswith("TimeoutError"))
        for langue in LANGUES:
            self.assertIsNotNone(expliquer(resultat.error, langue))


class TestSuggestionDeNom(unittest.TestCase):
    """Une faute de frappe est la première cause de NameError chez un débutant.

    Python ne fournit la suggestion « Did you mean » qu'au formatage
    complet du traceback : le runner la recalcule à partir des noms
    réellement disponibles.
    """

    def test_faute_sur_une_fonction_integree(self):
        resultat, _ = run_code("prin('a')\n")
        self.assertIn("Did you mean: 'print'?", resultat.error)

    def test_faute_sur_une_variable_de_l_apprenant(self):
        resultat, _ = run_code("total = 1\nprint(totl)\n")
        self.assertIn("Did you mean: 'total'?", resultat.error)

    def test_le_conseil_nomme_la_correction(self):
        resultat, _ = run_code("prin('a')\n")
        self.assertIn("print", expliquer(resultat.error, "fr"))
        self.assertIn("print", expliquer(resultat.error, "en"))

    def test_aucun_nom_proche_reste_generique(self):
        """Inventer une suggestion absurde serait pire que rien."""
        resultat, _ = run_code("print(xyzzy_totalement_inconnu)\n")
        self.assertNotIn("Did you mean", resultat.error)
        self.assertIsNotNone(expliquer(resultat.error, "fr"))

    def test_les_autres_erreurs_ne_sont_pas_touchees(self):
        resultat, _ = run_code("1 / 0\n")
        self.assertEqual(resultat.error.strip(),
                         "ZeroDivisionError: division by zero")


class TestDetectionsFines(unittest.TestCase):
    """Les erreurs de syntaxe fréquentes méritent mieux qu'un conseil général."""

    def test_confusion_egal_et_double_egal(self):
        resultat, _ = run_code("if x = 3:\n    pass\n")
        self.assertIn("==", expliquer(resultat.error, "fr"))

    def test_deux_points_manquants(self):
        resultat, _ = run_code("if True\n    pass\n")
        self.assertIn("deux-points", expliquer(resultat.error, "fr"))

    def test_parenthese_non_fermee(self):
        resultat, _ = run_code("x = (1 + 2\n")
        conseil = expliquer(resultat.error, "fr")
        self.assertTrue("parenthèse" in conseil or "refermé" in conseil)


if __name__ == "__main__":
    unittest.main()
