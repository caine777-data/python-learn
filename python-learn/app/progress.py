"""
Sauvegarde et chargement de la progression de l'apprenant.

Les données sont stockées dans le dossier personnel de l'utilisateur
(~/.python-learn/progress.json), ce qui fonctionne aussi bien depuis
les sources que depuis l'exécutable empaqueté.
"""

import json
from pathlib import Path

DATA_DIR = Path.home() / ".python-learn"
PROGRESS_FILE = DATA_DIR / "progress.json"

_DEFAULT = {"completed": [], "code": {}, "badges": [], "theme": "dark",
            "vu_accueil": False, "historique": {}, "objectif_quotidien": 3,
            "srs": {}, "nom": "", "langue": "fr",
            "notes": {}, "favoris": [], "objectif_hebdo": 15, "echecs": {}}


def normaliser(data):
    """Complète un dict de progression avec les clés par défaut manquantes."""
    for cle, valeur in _DEFAULT.items():
        data.setdefault(cle, valeur.copy() if isinstance(valeur, (dict, list)) else valeur)
    return data


def load_progress():
    """Charge la progression. Retourne une structure par défaut si absente."""
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    return normaliser(data)


def save_progress(data):
    """Écrit la progression sur disque (silencieux en cas d'échec)."""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        PROGRESS_FILE.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except Exception:
        pass


def mark_completed(data, lesson_id):
    if lesson_id not in data["completed"]:
        data["completed"].append(lesson_id)
        save_progress(data)


def store_code(data, lesson_id, code):
    data["code"][lesson_id] = code
    save_progress(data)


def award_badge(data, level_id):
    """Enregistre un badge de niveau s'il n'existe pas déjà. Renvoie True si nouveau."""
    if level_id not in data["badges"]:
        data["badges"].append(level_id)
        save_progress(data)
        return True
    return False


def set_theme(data, theme):
    data["theme"] = theme
    save_progress(data)


def marquer_accueil_vu(data):
    data["vu_accueil"] = True
    save_progress(data)


def enregistrer_activite(data, date_iso):
    """Incrémente le compteur d'exercices du jour."""
    data["historique"][date_iso] = data["historique"].get(date_iso, 0) + 1
    save_progress(data)


def set_nom(data, nom):
    data["nom"] = nom
    save_progress(data)


def set_objectif(data, n):
    data["objectif_quotidien"] = max(1, n)
    save_progress(data)


def set_langue(data, lang):
    data["langue"] = lang
    save_progress(data)


def set_note(data, item_id, texte):
    """Enregistre (ou efface) la note personnelle d'une leçon."""
    if texte.strip():
        data["notes"][item_id] = texte
    else:
        data["notes"].pop(item_id, None)
    save_progress(data)


def toggle_favori(data, item_id):
    """Ajoute/retire une leçon des favoris. Renvoie l'état après bascule."""
    if item_id in data["favoris"]:
        data["favoris"].remove(item_id)
        actif = False
    else:
        data["favoris"].append(item_id)
        actif = True
    save_progress(data)
    return actif


def set_objectif_hebdo(data, n):
    data["objectif_hebdo"] = max(1, n)
    save_progress(data)


def enregistrer_echec(data, item_id):
    """Compte un échec sur un exercice (pour la recommandation adaptative)."""
    data["echecs"][item_id] = data["echecs"].get(item_id, 0) + 1
    save_progress(data)


def exporter_json(data):
    """Renvoie la progression sérialisée (pour sauvegarde externe)."""
    return json.dumps(data, ensure_ascii=False, indent=2)


def importer_json(texte):
    """Construit une progression valide à partir d'un JSON. Lève ValueError si invalide."""
    charge = json.loads(texte)
    if not isinstance(charge, dict) or "completed" not in charge:
        raise ValueError("Fichier de progression non reconnu.")
    return normaliser(charge)


def reset_progress():
    """Efface toute la progression."""
    try:
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()
    except Exception:
        pass
