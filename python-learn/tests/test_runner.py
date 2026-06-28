"""Tests du moteur d'exécution (inspecteur de variables, pas-à-pas)."""

import unittest
from app.runner import inspecter, tracer, run_code


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


if __name__ == "__main__":
    unittest.main()
