"""
Tests de la traduction du contenu des leçons.

Le point sensible d'un chantier de traduction mené sur la durée est le
décrochage silencieux : une leçon renommée, et sa traduction ne
s'applique plus à rien sans que personne ne s'en aperçoive. Le test des
identifiants orphelins existe pour cela.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from content import CURRICULUM, etat_traduction, find_lesson, traduit
from content.traductions import TRADUCTIONS, appliquer


class TestChampTraduit(unittest.TestCase):

    LECON = {"title": "Bonjour", "title_en": "Hello", "content": "Texte"}

    def test_langue_traduite(self):
        self.assertEqual(traduit(self.LECON, "title", "en"), "Hello")

    def test_francais_par_defaut(self):
        self.assertEqual(traduit(self.LECON, "title"), "Bonjour")
        self.assertEqual(traduit(self.LECON, "title", "fr"), "Bonjour")

    def test_repli_quand_la_traduction_manque(self):
        """Une leçon non traduite doit rester lisible, pas disparaître."""
        self.assertEqual(traduit(self.LECON, "content", "en"), "Texte")

    def test_langue_inconnue_retombe_sur_le_francais(self):
        self.assertEqual(traduit(self.LECON, "title", "klingon"), "Bonjour")

    def test_champ_absent(self):
        self.assertIsNone(traduit(self.LECON, "inexistant", "en"))
        self.assertEqual(traduit(self.LECON, "inexistant", "en", []), [])

    def test_element_absent(self):
        self.assertIsNone(traduit(None, "title", "en"))

    def test_traduction_vide_ne_masque_pas_le_francais(self):
        lecon = {"title": "Bonjour", "title_en": ""}
        self.assertEqual(traduit(lecon, "title", "en"), "Bonjour")


class TestApplication(unittest.TestCase):

    def test_les_traductions_sont_injectees(self):
        lecon = find_lesson("err-01")
        self.assertTrue(lecon.get("title_en"), "err-01 devrait être traduite")
        self.assertNotEqual(traduit(lecon, "title", "en"),
                            traduit(lecon, "title", "fr"))

    def test_le_quiz_de_fin_est_traduit(self):
        """Les quiz sont injectés après les cours : l'ordre compte."""
        quiz = find_lesson("qz-err")
        self.assertTrue(quiz.get("title_en"),
                        "le quiz de fin doit être traduit lui aussi")

    def test_application_idempotente(self):
        avant = find_lesson("err-01")["title_en"]
        appliquer(CURRICULUM)
        appliquer(CURRICULUM)
        self.assertEqual(find_lesson("err-01")["title_en"], avant)

    def test_aucun_identifiant_orphelin(self):
        """Une traduction qui ne correspond à rien ne sert plus à personne."""
        connus = set()
        for niveau in CURRICULUM:
            connus.add(niveau["id"])
            for lecon in niveau["lessons"]:
                connus.add(lecon["id"])
        for langue, entrees in TRADUCTIONS.items():
            orphelins = sorted(set(entrees) - connus)
            self.assertEqual(
                orphelins, [],
                f"traductions « {langue} » sans leçon correspondante : "
                f"{orphelins}")

    def test_les_options_de_quiz_gardent_le_meme_nombre(self):
        """Traduire un quiz ne doit pas changer le numéro de la bonne réponse."""
        for niveau in CURRICULUM:
            for lecon in niveau["lessons"]:
                if lecon.get("type") != "quiz" or "options_en" not in lecon:
                    continue
                with self.subTest(quiz=lecon["id"]):
                    self.assertEqual(len(lecon["options_en"]),
                                     len(lecon["options"]))


class TestEtatTraduction(unittest.TestCase):

    def test_rapport_couvre_tous_les_parcours(self):
        rapport = etat_traduction("en")
        self.assertEqual(len(rapport), len(CURRICULUM))
        for ligne in rapport:
            self.assertLessEqual(ligne["traduites"], ligne["total"])

    def test_parcours_erreurs_entierement_traduit(self):
        rapport = {ligne["id"]: ligne for ligne in etat_traduction("en")}
        erreurs = rapport["erreurs"]
        self.assertEqual(erreurs["traduites"], erreurs["total"],
                         "le parcours « Décoder les erreurs » sert de modèle")

    def test_langue_absente_donne_zero(self):
        for ligne in etat_traduction("klingon"):
            self.assertEqual(ligne["traduites"], 0)


if __name__ == "__main__":
    unittest.main()
