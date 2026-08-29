"""Tests des exercices « prédis la sortie » et « remets dans l'ordre »."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import exercices


class TestPrediction(unittest.TestCase):

    def test_prediction_juste(self):
        reussi, sortie, erreur = exercices.verifier_prediction(
            "print(2 + 3)\n", "5")
        self.assertTrue(reussi)
        self.assertIsNone(erreur)
        self.assertEqual(sortie.strip(), "5")

    def test_prediction_fausse(self):
        reussi, _, _ = exercices.verifier_prediction("print(2 + 3)\n", "23")
        self.assertFalse(reussi)

    def test_le_piege_classique_de_la_concatenation(self):
        """print('2' + '3') affiche 23, pas 5 : c'est tout l'intérêt."""
        juste, _, _ = exercices.verifier_prediction("print('2' + '3')\n", "23")
        faux, _, _ = exercices.verifier_prediction("print('2' + '3')\n", "5")
        self.assertTrue(juste)
        self.assertFalse(faux)

    def test_espaces_et_lignes_vides_tolerees(self):
        reussi, _, _ = exercices.verifier_prediction(
            "print('a')\nprint('b')\n", "  a  \n b \n\n\n")
        self.assertTrue(reussi)

    def test_ordre_des_lignes_respecte(self):
        reussi, _, _ = exercices.verifier_prediction(
            "print('a')\nprint('b')\n", "b\na")
        self.assertFalse(reussi)

    def test_programme_en_erreur_est_signale(self):
        reussi, _, erreur = exercices.verifier_prediction("1 / 0\n", "")
        self.assertFalse(reussi)
        self.assertIn("ZeroDivisionError", erreur)

    def test_entrees_clavier_simulees(self):
        reussi, _, _ = exercices.verifier_prediction(
            "nom = input()\nprint('Bonjour ' + nom)\n", "Bonjour Zoé",
            stdin_lines=["Zoé"])
        self.assertTrue(reussi)

    def test_premiere_difference(self):
        self.assertIsNone(exercices.premiere_difference("a\nb", "a\nb"))
        self.assertEqual(exercices.premiere_difference("a\nX", "a\nb"), 2)
        self.assertEqual(exercices.premiere_difference("a", "a\nb"), 2)


class TestRemiseEnOrdre(unittest.TestCase):

    LIGNES = ["total = 0",
              "for n in [1, 2, 3]:",
              "    total = total + n",
              "print(total)"]

    def lecon(self, **extra):
        base = {"id": "ord-01", "type": "ordre", "lignes": self.LIGNES}
        base.update(extra)
        return base

    def test_melange_reproductible(self):
        a = exercices.melanger(self.LIGNES, "ord-01")
        b = exercices.melanger(self.LIGNES, "ord-01")
        self.assertEqual(a, b, "le même exercice doit toujours être présenté pareil")

    def test_melange_jamais_dans_le_bon_ordre(self):
        """Un exercice déjà résolu à l'ouverture n'apprendrait rien."""
        for graine in range(60):
            melange = exercices.melanger(self.LIGNES, f"graine-{graine}")
            self.assertNotEqual(melange, self.LIGNES)

    def test_melange_conserve_toutes_les_lignes(self):
        melange = exercices.melanger(self.LIGNES, "ord-01")
        self.assertEqual(sorted(melange), sorted(self.LIGNES))

    def test_une_seule_ligne_reste_telle_quelle(self):
        self.assertEqual(exercices.melanger(["print('x')"], "g"), ["print('x')"])

    def test_bon_ordre_accepte(self):
        reussi, _ = exercices.verifier_ordre(self.LIGNES, self.lecon())
        self.assertTrue(reussi)

    def test_mauvais_ordre_refuse(self):
        reussi, _ = exercices.verifier_ordre(
            list(reversed(self.LIGNES)), self.lecon())
        self.assertFalse(reussi)

    def test_validation_par_execution_accepte_un_autre_ordre(self):
        """Deux affectations indépendantes peuvent venir dans les deux sens."""
        lignes = ["a = 2", "b = 3", "print(a + b)"]
        lecon = {"id": "ord-02", "type": "ordre", "lignes": lignes,
                 "expected_output": "5"}
        autre_ordre = ["b = 3", "a = 2", "print(a + b)"]
        reussi, _ = exercices.verifier_ordre(autre_ordre, lecon)
        self.assertTrue(reussi, "un ordre différent mais correct doit passer")

    def test_validation_par_execution_refuse_un_ordre_casse(self):
        lignes = ["a = 2", "b = 3", "print(a + b)"]
        lecon = {"id": "ord-03", "type": "ordre", "lignes": lignes,
                 "expected_output": "5"}
        reussi, _ = exercices.verifier_ordre(
            ["print(a + b)", "a = 2", "b = 3"], lecon)
        self.assertFalse(reussi)

    def test_code_reconstitue(self):
        self.assertEqual(exercices.code_depuis_lignes(["a = 1", "print(a)"]),
                         "a = 1\nprint(a)\n")

    def test_premiere_ligne_fautive(self):
        self.assertIsNone(
            exercices.premiere_ligne_fautive(self.LIGNES, self.lecon()))
        melange = [self.LIGNES[1], self.LIGNES[0]] + self.LIGNES[2:]
        self.assertEqual(
            exercices.premiere_ligne_fautive(melange, self.lecon()), 1)

    def test_est_special(self):
        self.assertTrue(exercices.est_special({"type": "predire"}))
        self.assertTrue(exercices.est_special({"type": "ordre"}))
        self.assertFalse(exercices.est_special({"type": "quiz"}))
        self.assertFalse(exercices.est_special({}))


if __name__ == "__main__":
    unittest.main()
