"""
Tests automatiques du curriculum.

Vérifie que CHAQUE solution proposée passe bien son propre test, et que
chaque quiz a une réponse cohérente. Lancé en local et par la CI :

    python -m unittest discover -s tests -v
"""

import unittest

from app import exercices
from app.runner import run_exercise
from content import CURRICULUM, exercice_count, get_exercice, lesson_items


class TestCurriculum(unittest.TestCase):

    def test_solutions_passent_leurs_tests(self):
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                if lesson.get("type") == "quiz":
                    continue
                for i in range(exercice_count(lesson)):
                    exo = get_exercice(lesson, i)
                    sol = exo.get("solution")
                    if sol is None:
                        continue
                    with self.subTest(item=lesson_items(lesson)[i]):
                        _, ok, msg = run_exercise(
                            sol,
                            check_code=exo.get("check"),
                            expected_output=exo.get("expected_output"),
                            stdin_lines=exo.get("stdin"),
                        )
                        self.assertTrue(ok, msg)

    def test_quiz_coherents(self):
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                if lesson.get("type") != "quiz":
                    continue
                with self.subTest(quiz=lesson["id"]):
                    self.assertIn("answer", lesson)
                    self.assertIsInstance(lesson["answer"], int)
                    self.assertTrue(0 <= lesson["answer"] < len(lesson["options"]))

    def test_exercices_predire_sont_lisibles(self):
        """Le programme a prédire doit s'exécuter et afficher quelque chose."""
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                if lesson.get("type") != "predire":
                    continue
                with self.subTest(lecon=lesson["id"]):
                    code = lesson.get("code", "")
                    self.assertTrue(code.strip(), "champ « code » vide")
                    _, sortie, erreur = exercices.verifier_prediction(code, "")
                    self.assertIsNone(erreur, f"le programme échoue : {erreur}")
                    self.assertTrue(
                        sortie.strip(),
                        "le programme n'affiche rien : il n'y a rien à prédire")

    def test_exercices_ordre_sont_resolubles(self):
        """L'ordre annoncé doit être une solution, et le mélange ne pas la donner."""
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                if lesson.get("type") != "ordre":
                    continue
                with self.subTest(lecon=lesson["id"]):
                    lignes = exercices.lignes_de(lesson)
                    self.assertGreaterEqual(len(lignes), 2)
                    reussi, message = exercices.verifier_ordre(lignes, lesson)
                    self.assertTrue(reussi, message)
                    self.assertNotEqual(
                        exercices.melanger(lignes, lesson["id"]), lignes,
                        "l'exercice serait déjà résolu à l'ouverture")

    def test_identifiants_uniques(self):
        vus = set()
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                self.assertNotIn(lesson["id"], vus, f"id dupliqué : {lesson['id']}")
                vus.add(lesson["id"])


    def test_modes_debug_et_trous_coherents(self):
        from app.runner import run_exercise
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                mode = lesson.get("mode")
                if mode == "trous":
                    with self.subTest(trous=lesson["id"]):
                        self.assertIn("____", lesson.get("starter", ""),
                                      "un exercice à trous doit contenir ____")
                elif mode == "debug":
                    with self.subTest(debug=lesson["id"]):
                        starter = lesson.get("starter", "")
                        _, ok, _ = run_exercise(starter, check_code=lesson.get("check"),
                                                expected_output=lesson.get("expected_output"))
                        self.assertFalse(ok, "le starter d'un exo débogue doit échouer (bug réel)")


if __name__ == "__main__":
    unittest.main()
