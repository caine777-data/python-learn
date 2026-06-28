"""
Tests automatiques du curriculum.

Vérifie que CHAQUE solution proposée passe bien son propre test, et que
chaque quiz a une réponse cohérente. Lancé en local et par la CI :

    python -m unittest discover -s tests -v
"""

import unittest

from content import CURRICULUM, get_exercice, exercice_count, lesson_items
from app.runner import run_exercise


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

    def test_identifiants_uniques(self):
        vus = set()
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                self.assertNotIn(lesson["id"], vus, f"id dupliqué : {lesson['id']}")
                vus.add(lesson["id"])


if __name__ == "__main__":
    unittest.main()
