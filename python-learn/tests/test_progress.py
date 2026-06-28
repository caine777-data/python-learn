import os
import sys
import json
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import progress as prog


class TestProgress(unittest.TestCase):
    def setUp(self):
        self._dir = Path(tempfile.mkdtemp())
        prog.DATA_DIR = self._dir
        prog.PROGRESS_FILE = self._dir / "progress.json"

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


if __name__ == "__main__":
    unittest.main()
