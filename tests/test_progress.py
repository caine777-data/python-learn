import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import progress as prog


class BaseProgress(unittest.TestCase):
    """Redirige les fichiers de progression vers un dossier jetable."""

    def setUp(self):
        self._dir = Path(tempfile.mkdtemp())
        prog.DATA_DIR = self._dir
        prog.PROGRESS_FILE = self._dir / "progress.json"
        prog.BACKUP_FILE = self._dir / "progress.bak.json"


class TestProgress(BaseProgress):
    def test_normaliser_complete_les_cles(self):
        d = prog.normaliser({"completed": ["a"]})
        for cle in ("notes", "favoris", "objectif_hebdo", "echecs", "langue"):
            self.assertIn(cle, d)

    def test_toggle_favori(self):
        d = prog.load_progress()
        self.assertTrue(prog.toggle_favori(d, "deb-00"))
        self.assertIn("deb-00", d["favoris"])
        self.assertFalse(prog.toggle_favori(d, "deb-00"))
        self.assertNotIn("deb-00", d["favoris"])

    def test_set_note(self):
        d = prog.load_progress()
        prog.set_note(d, "deb-00", "ma note")
        self.assertEqual(d["notes"]["deb-00"], "ma note")
        prog.set_note(d, "deb-00", "   ")   # vide -> efface
        self.assertNotIn("deb-00", d["notes"])

    def test_enregistrer_echec(self):
        d = prog.load_progress()
        prog.enregistrer_echec(d, "alg-01")
        prog.enregistrer_echec(d, "alg-01")
        self.assertEqual(d["echecs"]["alg-01"], 2)

    def test_export_import_roundtrip(self):
        d = prog.load_progress()
        d["completed"] = ["a", "b"]
        d["favoris"] = ["a"]
        texte = prog.exporter_json(d)
        rejoue = prog.importer_json(texte)
        self.assertEqual(rejoue["completed"], ["a", "b"])
        self.assertEqual(rejoue["favoris"], ["a"])

    def test_import_invalide(self):
        with self.assertRaises(ValueError):
            prog.importer_json(json.dumps({"pas": "bon"}))


class TestEcritureSure(BaseProgress):
    """La progression d'un apprenant ne doit jamais disparaître en silence."""

    def test_sauvegarde_puis_relecture(self):
        d = prog.load_progress()
        d["completed"] = ["deb-01"]
        self.assertTrue(prog.save_progress(d))
        self.assertEqual(prog.load_progress()["completed"], ["deb-01"])
        self.assertIsNone(prog.dernier_incident())

    def test_aucun_fichier_temporaire_ne_traine(self):
        prog.save_progress(prog.normaliser({}))
        restes = [f.name for f in self._dir.iterdir() if f.suffix == ".tmp"]
        self.assertEqual(restes, [], f"temporaires oubliés : {restes}")

    def test_l_ancienne_version_devient_la_sauvegarde(self):
        d = prog.normaliser({"completed": ["premier"]})
        prog.save_progress(d)
        d["completed"] = ["second"]
        prog.save_progress(d)
        secours = json.loads(prog.BACKUP_FILE.read_text(encoding="utf-8"))
        self.assertEqual(secours["completed"], ["premier"])

    def test_fichier_tronque_restaure_la_sauvegarde(self):
        prog.save_progress(prog.normaliser({"completed": ["travail"]}))
        prog.save_progress(prog.normaliser({"completed": ["travail", "suite"]}))
        # simule une coupure de courant en pleine écriture
        prog.PROGRESS_FILE.write_text('{"completed": ["trav', encoding="utf-8")

        recharge = prog.load_progress()
        self.assertEqual(recharge["completed"], ["travail"])
        incident, _ = prog.dernier_incident()
        self.assertEqual(incident, prog.INCIDENT_RESTAURE)

    def test_fichier_illisible_sans_secours_est_mis_de_cote(self):
        prog.PROGRESS_FILE.write_text("ceci n'est pas du JSON", encoding="utf-8")

        recharge = prog.load_progress()
        self.assertEqual(recharge["completed"], [])
        incident, chemin = prog.dernier_incident()
        self.assertEqual(incident, prog.INCIDENT_PERDU)
        self.assertTrue(Path(chemin).exists(), "le fichier abîmé doit être conservé")

    def test_json_valide_mais_pas_un_dictionnaire(self):
        prog.PROGRESS_FILE.write_text("[1, 2, 3]", encoding="utf-8")
        recharge = prog.load_progress()
        self.assertEqual(recharge["completed"], [])
        self.assertIsNotNone(prog.dernier_incident())

    def test_premier_lancement_ne_signale_aucun_incident(self):
        self.assertEqual(prog.load_progress()["completed"], [])
        self.assertIsNone(prog.dernier_incident())

    def test_reset_efface_aussi_la_sauvegarde(self):
        prog.save_progress(prog.normaliser({"completed": ["a"]}))
        prog.save_progress(prog.normaliser({"completed": ["b"]}))
        self.assertTrue(prog.BACKUP_FILE.exists())
        prog.reset_progress()
        self.assertFalse(prog.PROGRESS_FILE.exists())
        self.assertFalse(prog.BACKUP_FILE.exists())


if __name__ == "__main__":
    unittest.main()
