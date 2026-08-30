"""
Détection des clés de traduction dupliquées.

Une clé écrite deux fois dans un même dictionnaire ne provoque aucune
erreur : Python garde silencieusement la DERNIÈRE valeur. Le texte prévu
disparaît sans que rien ne le signale.

Ce n'est pas un détail de style. Le cas qui a motivé ce test :
« dlg_reset_msg » servait à la fois au bouton qui efface TOUTE la
progression et à celui qui remet un exercice à son état de départ. La
seconde définition écrasant la première, le bouton destructeur affichait
« Réinitialiser le code de cet exercice ? » — l'utilisateur croyait
remettre un exercice à zéro et perdait tout son travail.

Le doublon étant invisible une fois le dictionnaire construit, on lit le
fichier source lui-même.
"""

import ast
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RACINE = Path(__file__).resolve().parent.parent


def cles_dupliquees(chemin):
    """Clés littérales écrites plusieurs fois dans un même dictionnaire.

    Renvoie une liste de (ligne, clé) pour chaque doublon rencontré.
    """
    arbre = ast.parse(Path(chemin).read_text(encoding="utf-8"))
    doublons = []
    for noeud in ast.walk(arbre):
        if not isinstance(noeud, ast.Dict):
            continue
        vues = {}
        for cle in noeud.keys:
            if not isinstance(cle, ast.Constant) or not isinstance(cle.value, str):
                continue
            if cle.value in vues:
                doublons.append((cle.lineno, cle.value))
            else:
                vues[cle.value] = cle.lineno
    return doublons


class TestClesUniques(unittest.TestCase):

    FICHIERS = [
        "app/i18n.py",
        "content/traductions.py",
        "content/quiz_parcours.py",
        "content/hints.py",
    ]

    def test_aucune_cle_dupliquee(self):
        for fichier in self.FICHIERS:
            chemin = RACINE / fichier
            if not chemin.exists():
                continue
            with self.subTest(fichier=fichier):
                doublons = cles_dupliquees(chemin)
                details = ", ".join(f"« {cle} » ligne {ligne}"
                                    for ligne, cle in doublons)
                self.assertEqual(
                    doublons, [],
                    f"{fichier} : clé(s) écrite(s) deux fois — la première "
                    f"valeur est silencieusement perdue : {details}")

    def test_le_detecteur_fonctionne(self):
        """Un test de détection qui ne détecte rien ne sert à rien."""
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                         encoding="utf-8") as f:
            f.write('D = {"a": 1, "b": 2, "a": 3}\n')
            piege = f.name
        try:
            doublons = cles_dupliquees(piege)
            self.assertEqual([cle for _, cle in doublons], ["a"])
        finally:
            os.unlink(piege)


class TestActionsDistinctes(unittest.TestCase):
    """Deux actions aux conséquences différentes ne partagent pas leurs textes."""

    def test_effacer_la_progression_et_recommencer_un_exercice(self):
        from app.i18n import LANGUES, STRINGS
        for langue in LANGUES:
            with self.subTest(langue=langue):
                textes = STRINGS[langue]
                for cle in ("dlg_reset_title", "dlg_reset_msg",
                            "dlg_reset_exo_title", "dlg_reset_exo_msg"):
                    self.assertIn(cle, textes, f"{cle} manquante en {langue}")
                self.assertNotEqual(
                    textes["dlg_reset_msg"], textes["dlg_reset_exo_msg"],
                    "effacer toute la progression et recommencer un exercice "
                    "ne peuvent pas afficher le même avertissement")


if __name__ == "__main__":
    unittest.main()
