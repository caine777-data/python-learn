"""Tests de la logique de motivation (streak, SRS, certificat)."""

import datetime
import unittest

from app import stats


class TestStats(unittest.TestCase):

    def test_streak(self):
        t = datetime.date(2026, 6, 27)
        h = {"2026-06-27": 2, "2026-06-26": 1, "2026-06-25": 3}
        self.assertEqual(stats.streak(h, t), 3)
        # inactif aujourd'hui mais actif hier : la série tient
        h2 = {"2026-06-26": 1, "2026-06-25": 1}
        self.assertEqual(stats.streak(h2, t), 2)
        # trou : la série s'arrête
        h3 = {"2026-06-27": 1, "2026-06-25": 1}
        self.assertEqual(stats.streak(h3, t), 1)

    def test_meilleur_streak(self):
        h = {"2026-06-01": 1, "2026-06-02": 1, "2026-06-03": 1,
             "2026-06-10": 1, "2026-06-11": 1}
        self.assertEqual(stats.meilleur_streak(h), 3)

    def test_intervalle_progressif(self):
        self.assertEqual(stats.prochain_intervalle(0), 1)
        self.assertEqual(stats.prochain_intervalle(1), 3)
        self.assertEqual(stats.prochain_intervalle(7), 16)
        self.assertEqual(stats.prochain_intervalle(90), 90)

    def test_planifier_et_dus(self):
        t = datetime.date(2026, 6, 27)
        srs = {}
        stats.planifier(srs, "deb-00", t, reussi=True)
        self.assertEqual(srs["deb-00"]["interval"], 1)
        self.assertEqual(srs["deb-00"]["due"], "2026-06-28")
        # pas encore dû aujourd'hui
        self.assertEqual(stats.dus(srs, t, {"deb-00"}), [])
        # dû demain
        self.assertEqual(stats.dus(srs, t + datetime.timedelta(days=1), {"deb-00"}),
                         ["deb-00"])

    def test_certificat_html(self):
        html = stats.certificat_html("Ada Lovelace", "Débutant", "27/06/2026")
        self.assertIn("Ada Lovelace", html)
        self.assertIn("Débutant", html)
        self.assertIn("<!DOCTYPE html>", html)

    def test_xp_et_niveau(self):
        self.assertEqual(stats.xp_total([], []), 0)
        self.assertEqual(stats.xp_total(["a", "b"], ["x"]), 10 * 2 + 50)
        n = stats.niveau(0)
        self.assertEqual(n["niveau"], 1)
        n = stats.niveau(250)
        self.assertEqual(n["niveau"], 3)
        self.assertEqual(n["dans_niveau"], 50)

    def test_cette_semaine(self):
        # mercredi 2026-06-24 ; lundi de la semaine = 2026-06-22
        today = datetime.date(2026, 6, 24)
        hist = {"2026-06-22": 2, "2026-06-24": 3, "2026-06-21": 9}  # 21 = dimanche d'avant
        self.assertEqual(stats.cette_semaine(hist, today), 5)

    def test_prochaine_action(self):
        ordre = ["a", "b", "c", "d"]
        # révision prioritaire
        self.assertEqual(stats.prochaine_action(ordre, ["a"], ["b"]),
                         ("revision", "b"))
        # sinon première non faite
        self.assertEqual(stats.prochaine_action(ordre, ["a"], []),
                         ("nouvelle", "b"))
        # tout fait
        self.assertEqual(stats.prochaine_action(ordre, ordre, []),
                         ("termine", None))

    def test_cheatsheet_html(self):
        sections = [("Bases", [("x = 1", "entier"), ('s = "hi"', "chaîne")])]
        html = stats.cheatsheet_html("Antisèche", sections)
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("Bases", html)
        self.assertIn("&quot;", html)          # guillemets échappés
        self.assertEqual(html.count("<section>"), 1)


if __name__ == "__main__":
    unittest.main()
