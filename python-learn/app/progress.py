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

_DEFAULT = {"completed": [], "code": {}, "badges": [], "theme": "dark"}


def load_progress():
    """Charge la progression. Retourne une structure par défaut si absente."""
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        data.setdefault("completed", [])
        data.setdefault("code", {})
        data.setdefault("badges", [])
        data.setdefault("theme", "dark")
        return data
    except Exception:
        return {"completed": [], "code": {}, "badges": [], "theme": "dark"}


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


def reset_progress():
    """Efface toute la progression."""
    try:
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()
    except Exception:
        pass
