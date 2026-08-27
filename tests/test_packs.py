"""
Tests des packs de leçons ajoutés par l'utilisateur.

Deux exigences guident ces tests :
  1. un pack correct doit fonctionner exactement comme un parcours livré ;
  2. un pack incorrect ne doit JAMAIS casser l'application — au pire il est
     écarté, avec un message que son auteur peut comprendre.
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.runner import run_exercise
from content import packs


def pack_minimal(**extra):
    """Un pack valide, que chaque test déforme à sa guise."""
    base = {
        "id": "essai",
        "titre": "Parcours d'essai",
        "lecons": [
            {"id": "essai-01", "title": "Une leçon", "check": "assert True"},
        ],
    }
    base.update(extra)
    return base


class TestModele(unittest.TestCase):
    """Le pack d'exemple est ce que découvrira tout nouvel auteur."""

    def setUp(self):
        self.modele = json.loads(packs.modele_pack())

    def test_le_modele_est_valide(self):
        parcours, problemes = packs.valider_pack(self.modele)
        self.assertIsNotNone(parcours)
        self.assertEqual(problemes, [], f"le modèle devrait être irréprochable : {problemes}")

    def test_les_solutions_du_modele_passent_leurs_tests(self):
        for lecon in self.modele["lecons"]:
            if lecon.get("type") == "quiz":
                continue
            with self.subTest(lecon=lecon["id"]):
                _, reussi, message = run_exercise(
                    lecon.get("solution", ""),
                    check_code=lecon.get("check"),
                    expected_output=lecon.get("expected_output"))
                self.assertTrue(reussi, message)

    def test_le_fichier_exemple_du_depot_suit_le_modele(self):
        """exemples/mon-cours.json est ce que les gens téléchargeront.

        Il est produit à partir de modele_pack() : ce test empêche les deux
        de diverger silencieusement au fil des versions.
        """
        depot = Path(__file__).resolve().parent.parent / "exemples" / "mon-cours.json"
        self.assertTrue(depot.exists(), "le pack d'exemple du dépôt a disparu")
        self.assertEqual(
            depot.read_text(encoding="utf-8"), packs.modele_pack(),
            "exemples/mon-cours.json ne correspond plus à modele_pack() ; "
            "régénère-le avec : python main.py --exemple-pack")

    def test_le_quiz_du_modele_est_coherent(self):
        quiz = [lecon for lecon in self.modele["lecons"]
                if lecon.get("type") == "quiz"]
        self.assertTrue(quiz, "le modèle devrait montrer un quiz")
        for question in quiz:
            self.assertTrue(0 <= question["answer"] < len(question["options"]))


class TestValidation(unittest.TestCase):

    def test_pack_correct_est_accepte(self):
        parcours, problemes = packs.valider_pack(pack_minimal())
        self.assertEqual(parcours["id"], "essai")
        self.assertEqual(len(parcours["lessons"]), 1)
        self.assertTrue(parcours["pack"])
        self.assertEqual(problemes, [])

    def test_titre_prefixe_pour_etre_reconnaissable(self):
        parcours, _ = packs.valider_pack(pack_minimal())
        self.assertTrue(parcours["title"].startswith(packs.PREFIXE_TITRE))

    def test_pack_sans_titre_est_rejete(self):
        donnees = pack_minimal()
        del donnees["titre"]
        parcours, problemes = packs.valider_pack(donnees)
        self.assertIsNone(parcours)
        self.assertTrue(problemes)

    def test_pack_sans_lecon_est_rejete(self):
        parcours, _ = packs.valider_pack(pack_minimal(lecons=[]))
        self.assertIsNone(parcours)

    def test_format_trop_recent_est_rejete(self):
        parcours, problemes = packs.valider_pack(
            pack_minimal(format=packs.FORMAT_ACTUEL + 1))
        self.assertIsNone(parcours)
        self.assertIn("format", problemes[0])

    def test_identifiant_deja_pris_est_ecarte(self):
        parcours, problemes = packs.valider_pack(pack_minimal(), {"essai-01"})
        self.assertIsNone(parcours)          # c'était la seule leçon
        self.assertTrue(any("déjà utilisé" in p for p in problemes))

    def test_quiz_injouable_est_ecarte(self):
        """Une bonne réponse hors des options rendrait le quiz impossible."""
        donnees = pack_minimal(lecons=[
            {"id": "q1", "title": "Quiz", "type": "quiz", "question": "?",
             "options": ["a", "b"], "answer": 7},
            {"id": "q2", "title": "OK", "check": "assert True"},
        ])
        parcours, problemes = packs.valider_pack(donnees)
        self.assertEqual([lec["id"] for lec in parcours["lessons"]], ["q2"])
        self.assertTrue(any("answer" in p for p in problemes))

    def test_champ_mal_forme_est_retire(self):
        """Un « hints » en texte serait parcouru lettre par lettre par l'interface."""
        donnees = pack_minimal(lecons=[
            {"id": "x1", "title": "X", "check": "assert True",
             "hints": "un seul texte au lieu d'une liste"},
        ])
        parcours, problemes = packs.valider_pack(donnees)
        self.assertNotIn("hints", parcours["lessons"][0])
        self.assertTrue(any("hints" in p for p in problemes))

    def test_exercice_sans_verification_est_signale(self):
        donnees = pack_minimal(lecons=[{"id": "y1", "title": "Y"}])
        parcours, problemes = packs.valider_pack(donnees)
        self.assertIsNotNone(parcours)       # utilisable, mais signalé
        self.assertTrue(any("vérification" in p for p in problemes))

    def test_diese_interdit_dans_un_identifiant(self):
        """« # » sépare la leçon de son sous-exercice : il est réservé."""
        donnees = pack_minimal(lecons=[
            {"id": "mauvais#1", "title": "M", "check": "assert True"}])
        parcours, problemes = packs.valider_pack(donnees)
        self.assertIsNone(parcours)
        self.assertTrue(any("#" in p for p in problemes))


class TestChargementFichiers(unittest.TestCase):

    def setUp(self):
        self.dossier = Path(tempfile.mkdtemp())

    def ecrire(self, nom, contenu):
        chemin = self.dossier / nom
        if isinstance(contenu, str):
            chemin.write_text(contenu, encoding="utf-8")
        else:
            chemin.write_text(json.dumps(contenu, ensure_ascii=False),
                              encoding="utf-8")
        return chemin

    def test_dossier_absent_ne_pose_pas_probleme(self):
        parcours, problemes = packs.charger_packs(self.dossier / "nulle-part")
        self.assertEqual(parcours, [])
        self.assertEqual(problemes, [])

    def test_dossier_vide(self):
        parcours, problemes = packs.charger_packs(self.dossier)
        self.assertEqual(parcours, [])
        self.assertEqual(problemes, [])

    def test_chargement_normal(self):
        self.ecrire("a.json", pack_minimal())
        parcours, problemes = packs.charger_packs(self.dossier)
        self.assertEqual(len(parcours), 1)
        self.assertEqual(problemes, [])

    def test_json_casse_est_signale_avec_la_ligne(self):
        self.ecrire("casse.json", '{"id": "x", "titre": "T",}')
        parcours, problemes = packs.charger_packs(self.dossier)
        self.assertEqual(parcours, [])
        self.assertIn("casse.json", problemes[0])
        self.assertIn("ligne", problemes[0])

    def test_un_pack_casse_n_empeche_pas_les_autres(self):
        self.ecrire("1-casse.json", "pas du json")
        self.ecrire("2-bon.json", pack_minimal())
        parcours, problemes = packs.charger_packs(self.dossier)
        self.assertEqual(len(parcours), 1, "le pack valide devait être chargé")
        self.assertTrue(problemes)

    def test_deux_packs_de_meme_identifiant(self):
        self.ecrire("1.json", pack_minimal())
        self.ecrire("2.json", pack_minimal(lecons=[
            {"id": "autre-01", "title": "Autre", "check": "assert True"}]))
        parcours, problemes = packs.charger_packs(self.dossier)
        self.assertEqual(len(parcours), 1)
        self.assertTrue(any("identifiant" in p for p in problemes))

    def test_conflit_avec_le_curriculum_officiel(self):
        self.ecrire("a.json", pack_minimal(lecons=[
            {"id": "deb-00", "title": "Collision", "check": "assert True"}]))
        parcours, problemes = packs.charger_packs(self.dossier,
                                                  ids_existants={"deb-00"})
        self.assertEqual(parcours, [])
        self.assertTrue(any("déjà utilisé" in p for p in problemes))

    def test_les_fichiers_non_json_sont_ignores(self):
        self.ecrire("notes.txt", "ceci n'est pas un pack")
        self.ecrire("a.json", pack_minimal())
        parcours, problemes = packs.charger_packs(self.dossier)
        self.assertEqual(len(parcours), 1)
        self.assertEqual(problemes, [])


if __name__ == "__main__":
    unittest.main()
