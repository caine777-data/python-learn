"""
Sauvegarde et chargement de la progression de l'apprenant.

Les données sont stockées dans le dossier personnel de l'utilisateur
(~/.python-learn/progress.json), ce qui fonctionne aussi bien depuis
les sources que depuis l'exécutable empaqueté.

L'écriture est ATOMIQUE : on écrit d'abord un fichier temporaire complet,
puis on le met en place d'un seul geste (os.replace). Une coupure de
courant ou une fermeture brutale ne peut donc jamais laisser un
progress.json tronqué. L'ancienne version est conservée en .bak et sert
de filet de secours au chargement.
"""

import json
import os
import tempfile
from pathlib import Path

DATA_DIR = Path.home() / ".python-learn"
PROGRESS_FILE = DATA_DIR / "progress.json"
BACKUP_FILE = DATA_DIR / "progress.bak.json"

_DEFAULT = {"completed": [], "code": {}, "badges": [], "theme": "dark",
            "vu_accueil": False, "historique": {}, "objectif_quotidien": 3,
            "srs": {}, "nom": "", "langue": "fr",
            "notes": {}, "favoris": [], "objectif_hebdo": 15, "echecs": {}}

# Renseigné par load_progress() quand le chargement ne s'est pas passé
# normalement, pour que l'interface puisse prévenir l'apprenant au lieu
# de repartir de zéro en silence. Voir dernier_incident().
_INCIDENT = None

INCIDENT_RESTAURE = "restaure"    # progress.json illisible, .bak utilisé
INCIDENT_PERDU = "perdu"          # les deux fichiers sont illisibles


def dernier_incident():
    """Décrit le dernier problème de chargement, ou None si tout allait bien.

    Renvoie un couple (code, detail) où `code` vaut INCIDENT_RESTAURE ou
    INCIDENT_PERDU. L'interface s'en sert pour afficher un avertissement.
    """
    return _INCIDENT


def normaliser(data):
    """Complète un dict de progression avec les clés par défaut manquantes."""
    for cle, valeur in _DEFAULT.items():
        data.setdefault(cle, valeur.copy() if isinstance(valeur, (dict, list)) else valeur)
    return data


def _lire(chemin):
    """Lit un fichier de progression. Renvoie le dict, ou None si inutilisable."""
    try:
        data = json.loads(chemin.read_text(encoding="utf-8"))
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def load_progress():
    """Charge la progression.

    Essaie d'abord le fichier principal, puis la sauvegarde .bak, et ne
    repart d'une structure vierge qu'en dernier recours. Un éventuel
    problème est consigné et lisible via dernier_incident().
    """
    global _INCIDENT
    _INCIDENT = None

    principal_existe = PROGRESS_FILE.exists()
    if principal_existe:
        data = _lire(PROGRESS_FILE)
        if data is not None:
            return normaliser(data)

    secours = _lire(BACKUP_FILE) if BACKUP_FILE.exists() else None
    if secours is not None:
        if principal_existe:
            _INCIDENT = (INCIDENT_RESTAURE, str(BACKUP_FILE))
        return normaliser(secours)

    if principal_existe:
        # Le fichier existe mais est illisible, et aucune sauvegarde ne
        # peut le remplacer : on le met de côté plutôt que de l'écraser.
        try:
            os.replace(PROGRESS_FILE, PROGRESS_FILE.with_suffix(".corrompu.json"))
            _INCIDENT = (INCIDENT_PERDU, str(PROGRESS_FILE.with_suffix(".corrompu.json")))
        except OSError:
            _INCIDENT = (INCIDENT_PERDU, str(PROGRESS_FILE))

    return normaliser({})


def _ecrire_temporaire(texte):
    """Écrit `texte` dans un fichier temporaire complet et synchronisé sur disque.

    Renvoie le chemin du temporaire, prêt à être mis en place par os.replace
    (qui est atomique tant que source et destination sont sur le même volume,
    d'où le dir=DATA_DIR).
    """
    fd, tmp = tempfile.mkstemp(dir=str(DATA_DIR), prefix=".progress-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(texte)
            f.flush()
            os.fsync(f.fileno())
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return tmp


def save_progress(data):
    """Écrit la progression sur disque de façon atomique.

    Renvoie True si l'écriture a réussi. En cas d'échec on ne touche pas
    au fichier existant : la progression déjà enregistrée reste intacte.
    """
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        tmp = _ecrire_temporaire(json.dumps(data, ensure_ascii=False, indent=2))
    except Exception:
        return False

    try:
        # Rotation gratuite : l'ancien fichier devient la sauvegarde.
        if PROGRESS_FILE.exists():
            os.replace(PROGRESS_FILE, BACKUP_FILE)
        os.replace(tmp, PROGRESS_FILE)
        return True
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        return False


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
    """Efface toute la progression, sauvegarde de secours comprise."""
    for chemin in (PROGRESS_FILE, BACKUP_FILE):
        try:
            if chemin.exists():
                chemin.unlink()
        except Exception:
            pass
