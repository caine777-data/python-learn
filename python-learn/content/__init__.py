"""
Curriculum complet, assemblé à partir des parcours.

Schéma d'une leçon (tous les champs marqués (option) sont facultatifs) :
    {
        "id": "uniq-01",
        "title": "Titre",
        "content": "...",            # texte (balisage léger : ## `code` **gras** -)
        "type": "quiz",              # (option) leçon de type QCM
        # --- cas leçon-exercice simple ---
        "starter": "...",
        "expected_output": "...",    # (option) sortie attendue
        "check": "assert ...",       # (option) tests
        "stdin": ["..."],            # (option) entrées simulées
        "solution": "...",           # (option)
        "hints": ["..."],            # (option) indices
        # --- cas multi-exercices ---
        "exercices": [ {prompt, starter, check/expected/stdin, solution, hints}, ... ],
        # --- cas quiz ---
        "question": "...", "options": [...], "answer": 0, "explanation": "...",
    }
"""

from . import (debutant, intermediaire, avance, expert,
               scripts, interfaces, web, admin, sqlite_db, dessin, projets,
               entrainement, algos, donnees, tests_tdd)
from .hints import HINTS
from .glossaire import GLOSSAIRE
from .quiz_parcours import QUIZ

CURRICULUM = [
    debutant.LEVEL,
    intermediaire.LEVEL,
    avance.LEVEL,
    expert.LEVEL,
    scripts.LEVEL,
    interfaces.LEVEL,
    web.LEVEL,
    admin.LEVEL,
    sqlite_db.LEVEL,
    dessin.LEVEL,
    algos.LEVEL,
    donnees.LEVEL,
    tests_tdd.LEVEL,
    projets.LEVEL,
    entrainement.LEVEL,
]

# Ajoute le quiz de fin à chaque parcours concerné (idempotent).
for _level in CURRICULUM:
    _quiz = QUIZ.get(_level["id"])
    if _quiz and not any(l["id"] == _quiz["id"] for l in _level["lessons"]):
        _level["lessons"].append(_quiz)


def all_lessons():
    for level in CURRICULUM:
        for lesson in level["lessons"]:
            yield level, lesson


def lesson_items(lesson):
    """Identifiants des sous-éléments validables d'une leçon."""
    if lesson.get("type") == "quiz":
        return [lesson["id"]]
    exos = lesson.get("exercices")
    if exos:
        return [f"{lesson['id']}#{i}" for i in range(len(exos))]
    return [lesson["id"]]


def get_exercice(lesson, index):
    """Renvoie le dict d'exercice (multi) ou la leçon elle-même (simple)."""
    exos = lesson.get("exercices")
    if exos:
        return exos[index]
    return lesson


def exercice_count(lesson):
    exos = lesson.get("exercices")
    return len(exos) if exos else 1


def hints_for(lesson, exercice=None):
    """Indices : ceux de l'exercice, sinon de la leçon, sinon du fichier hints."""
    if exercice is not None and exercice.get("hints"):
        return exercice["hints"]
    if lesson.get("hints"):
        return lesson["hints"]
    return HINTS.get(lesson["id"], [])


def total_count():
    """Nombre total d'éléments validables (exercices + quiz)."""
    return sum(len(lesson_items(l)) for _, l in all_lessons())


def lesson_done(lesson, completed):
    return all(i in completed for i in lesson_items(lesson))


def find_lesson(lesson_id):
    for _, lesson in all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None
