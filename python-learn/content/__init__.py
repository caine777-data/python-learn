"""
Curriculum complet, assemblé à partir des quatre niveaux.

Pour AJOUTER une leçon : éditez le fichier du niveau concerné
(debutant.py, intermediaire.py, avance.py, expert.py) et ajoutez un
dictionnaire à la liste `lessons`. Aucune autre modification n'est
nécessaire : l'interface se met à jour automatiquement.

Structure d'une leçon :
    {
        "id": "uniq-01",          # identifiant unique (obligatoire)
        "title": "Titre",         # titre affiché (obligatoire)
        "content": "...",         # texte de la leçon (markup léger)
        "starter": "...",         # code pré-rempli dans l'éditeur
        "expected_output": "...", # (option) sortie attendue à comparer
        "check": "assert ...",    # (option) code de test exécuté ensuite
        "stdin": ["ligne1"],      # (option) entrées simulées pour input()
        "solution": "...",        # (option) solution révélable
    }
"""

from . import (debutant, intermediaire, avance, expert,
               scripts, interfaces, web, admin)

CURRICULUM = [
    debutant.LEVEL,
    intermediaire.LEVEL,
    avance.LEVEL,
    expert.LEVEL,
    scripts.LEVEL,
    interfaces.LEVEL,
    web.LEVEL,
    admin.LEVEL,
]


def all_lessons():
    """Itère sur (niveau, leçon) pour tout le curriculum."""
    for level in CURRICULUM:
        for lesson in level["lessons"]:
            yield level, lesson


def total_count():
    return sum(len(level["lessons"]) for level in CURRICULUM)


def find_lesson(lesson_id):
    for _, lesson in all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None
