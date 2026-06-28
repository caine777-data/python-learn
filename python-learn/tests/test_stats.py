"""Tests de la logique de motivation (streak, SRS, certificat)."""

import unittest
import datetime
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


if __name__ == "__main__":
    unittest.main()
