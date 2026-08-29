"""Tests du moteur d'exécution (inspecteur de variables, pas-à-pas)."""

import sys
import unittest

from app.runner import inspecter, run_code, tracer, zombies_actifs


class TestRunner(unittest.TestCase):

    def test_inspecter_filtre(self):
        ns = {"x": 5, "noms": ["a", "b"], "__truc__": 1,
              "f": lambda: 1, "mod": __import__("math")}
        d = dict(inspecter(ns))
        self.assertEqual(d["x"], "5")
        self.assertEqual(d["noms"], "['a', 'b']")
        self.assertNotIn("__truc__", d)
        self.assertNotIn("f", d)      # fonctions exclues
        self.assertNotIn("mod", d)    # modules exclus

    def test_tracer_lignes_et_vars(self):
        etapes, err = tracer("x = 1\ny = x + 1\nprint(y)\n")
        self.assertIsNone(err)
        lignes = [e["ligne"] for e in etapes if e["ligne"]]
        self.assertEqual(lignes, [1, 2, 3])
        final = dict(etapes[-1]["vars"])
        self.assertEqual(final["y"], "2")
        self.assertIn("2", etapes[-1]["sortie"])

    def test_tracer_boucle_bornee(self):
        etapes, err = tracer("while True:\n    pass\n", max_steps=50)
        self.assertTrue(len(etapes) <= 52)
        self.assertIn("trop d'étapes", err or "")

    def test_tracer_syntaxe(self):
        etapes, err = tracer("def (:\n")
        self.assertTrue(err and "syntaxe" in err.lower())

    def test_sandbox_bloque_modules_dangereux(self):
        for mauvais in ("import os", "import subprocess", "import socket"):
            res, _ = run_code(mauvais + "\n", safe=True)
            self.assertIsNotNone(res.error)
            self.assertIn("non autorisé", res.error)

    def test_sandbox_autorise_modules_surs(self):
        res, _ = run_code("import math\nprint(math.factorial(5))\n", safe=True)
        self.assertIsNone(res.error)
        self.assertIn("120", res.output)

    def test_sandbox_retire_open(self):
        res, _ = run_code("open('x', 'w')\n", safe=True)
        self.assertIsNotNone(res.error)

    def test_mode_normal_autorise_os(self):
        res, _ = run_code("import os\nx = os.sep\n", safe=False)
        self.assertIsNone(res.error)


class TestInterruption(unittest.TestCase):
    """Une boucle infinie ne doit jamais figer l'application.

    Ces boucles dorment quelques millisecondes à chaque tour plutôt que de
    tourner à plein régime. Si l'interruption venait à échouer sur une
    version de Python, le thread survivant ne monopoliserait pas un cœur
    pendant tout le reste de la suite — l'échec resterait lisible au lieu
    de tout ralentir jusqu'au blocage.
    """

    BOUCLE = ("import time\n"
              "while True:\n"
              "    time.sleep(0.005)\n")

    BOUCLE_QUI_ATTRAPE = ("import time\n"
                          "while True:\n"
                          "    try:\n"
                          "        time.sleep(0.005)\n"
                          "    except Exception:\n"
                          "        pass\n")

    def tearDown(self):
        self.assertEqual(
            zombies_actifs(), 0,
            "une exécution n'a pas pu être arrêtée : elle continuerait de "
            "tourner en arrière-plan")

    def test_boucle_infinie_est_interrompue(self):
        res, _ = run_code(self.BOUCLE, timeout=1.0)
        self.assertTrue(res.timed_out)
        self.assertTrue(res.error.startswith("TimeoutError"))

    def test_boucle_qui_attrape_les_exceptions_est_interrompue(self):
        """« except Exception » n'arrête ni KeyboardInterrupt ni SystemExit."""
        res, _ = run_code(self.BOUCLE_QUI_ATTRAPE, timeout=1.0)
        self.assertTrue(res.timed_out)

    def test_boucle_de_calcul_pur_est_interrompue(self):
        """Le cas le plus courant : une boucle qui ne rend jamais la main."""
        res, _ = run_code("while True:\n    pass\n", timeout=1.0)
        self.assertTrue(res.timed_out)

    def test_code_normal_ne_laisse_rien_tourner(self):
        run_code("x = sum(range(1000))\n")
        self.assertEqual(zombies_actifs(), 0)

    def test_la_sortie_standard_revient_au_programme(self):
        """Un thread bloqué ne doit pas rendre le reste du programme muet.

        contextlib détourne sys.stdout globalement : un thread qui ne meurt
        jamais ne ressort jamais de son bloc « with », et tout le programme
        cesserait alors d'afficher quoi que ce soit.
        """
        avant = sys.stdout
        run_code("while True:\n    pass\n", timeout=0.5)
        self.assertIs(sys.stdout, avant)


if __name__ == "__main__":
    unittest.main()
