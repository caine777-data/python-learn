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

    def test_tous_les_parcours_entierement_traduits(self):
        rapport = {ligne["id"]: ligne for ligne in etat_traduction("en")}
        for niveau in CURRICULUM:
            nid = niveau["id"]
            self.assertEqual(
                rapport[nid]["traduites"], rapport[nid]["total"],
                f"le parcours {nid} doit être traduit à 100%"
            )

    def test_glossaire_et_cheatsheet_bilingues(self):
        from content.cheatsheet import get_cheatsheet
        from content.glossaire import get_glossaire
        gl_fr = get_glossaire("fr")
        gl_en = get_glossaire("en")
        self.assertEqual(len(gl_fr), len(gl_en))
        self.assertGreater(len(gl_fr), 0)

        cs_fr = get_cheatsheet("fr")
        cs_en = get_cheatsheet("en")
        self.assertEqual(len(cs_fr), len(cs_en))
        self.assertGreater(len(cs_fr), 0)

    def test_badge_svg_generation(self):
        from app.stats import badge_svg
        svg_fr = badge_svg(streak=5, termines=40, total=133, lang="fr")
        svg_en = badge_svg(streak=5, termines=40, total=133, lang="en")
        self.assertTrue(svg_fr.startswith("<svg") and svg_fr.endswith("</svg>"))
        self.assertTrue(svg_en.startswith("<svg") and svg_en.endswith("</svg>"))
        self.assertIn("Profil", svg_fr)
        self.assertIn("Profile", svg_en)

    def test_certificat_et_cheatsheet_html(self):
        from app.stats import certificat_html, cheatsheet_html
        from content.cheatsheet import get_cheatsheet
        cert_fr = certificat_html("Sam", "Débutant", "01/01/2026", lang="fr")
        cert_en = certificat_html("Sam", "Beginner", "01/01/2026", lang="en")
        self.assertIn("Certificat de réussite", cert_fr)
        self.assertIn("Certificate of Completion", cert_en)

        cs_fr = cheatsheet_html("Antisèche", get_cheatsheet("fr"), lang="fr")
        cs_en = cheatsheet_html("Cheat Sheet", get_cheatsheet("en"), lang="en")
        self.assertIn("mémo imprimable", cs_fr)
        self.assertIn("printable cheat sheet", cs_en)

    def test_langue_absente_donne_zero(self):
        for ligne in etat_traduction("klingon"):
            self.assertEqual(ligne["traduites"], 0)


if __name__ == "__main__":
    unittest.main()

