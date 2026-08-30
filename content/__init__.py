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

from . import (
    admin,
    algos,
    avance,
    debutant,
    dessin,
    donnees,
    entrainement,
    erreurs,
    expert,
    interfaces,
    intermediaire,
    packs,
    projets,
    scripts,
    sqlite_db,
    tests_tdd,
    web,
)
from .glossaire import GLOSSAIRE
from .hints import HINTS
from .quiz_parcours import QUIZ
from .traductions import appliquer as _appliquer_traductions

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
    erreurs.LEVEL,
]

# Ajoute le quiz de fin à chaque parcours concerné (idempotent).
for _level in CURRICULUM:
    _quiz = QUIZ.get(_level["id"])
    if _quiz and not any(l["id"] == _quiz["id"] for l in _level["lessons"]):
        _level["lessons"].append(_quiz)

# Les traductions sont injectées APRÈS les quiz de fin : ceux-ci sont
# ajoutés ci-dessus, et ne seraient donc pas traduits dans l'autre ordre.
_appliquer_traductions(CURRICULUM)


# Les packs de l'utilisateur ne sont chargés qu'une fois, et seulement
# sur demande explicite (voir ajouter_packs).
_packs_charges = False


def ids_utilises():
    """Tous les identifiants déjà pris, parcours et leçons confondus."""
    pris = set()
    for niveau in CURRICULUM:
        pris.add(niveau["id"])
        for lecon in niveau["lessons"]:
            pris.add(lecon["id"])
    return pris


def ajouter_packs(dossier=None):
    """Ajoute au curriculum les packs de leçons de l'utilisateur.

    Appelé au démarrage de l'application, et non à l'import du module :
    les tests et l'intégration continue travaillent ainsi toujours sur le
    curriculum officiel, quoi que contienne le dossier personnel.

    Renvoie (parcours ajoutés, problèmes rencontrés).
    """
    global _packs_charges
    if _packs_charges:
        return [], []
    nouveaux, problemes = packs.charger_packs(dossier, ids_utilises())
    CURRICULUM.extend(nouveaux)
    _packs_charges = True
    return nouveaux, problemes


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


def traduit(element, champ, langue="fr", defaut=None):
    """Version traduite d'un champ de leçon, avec repli sur le français.

    Le contenu s'écrit en français ; une traduction s'ajoute en suffixant
    le champ par la langue — « title » devient « title_en ». Tant qu'elle
    n'existe pas, le français reste affiché : on peut donc traduire leçon
    par leçon sans jamais casser l'application ni laisser un trou.
    """
    if element is None:
        return defaut
    if langue and langue != "fr":
        valeur = element.get(f"{champ}_{langue}")
        if valeur:
            return valeur
    valeur = element.get(champ)
    return defaut if valeur is None else valeur


def etat_traduction(langue="en"):
    """Avancement de la traduction, parcours par parcours.

    Renvoie une liste de dicts {id, titre, traduites, total}, où l'on
    compte comme traduite une leçon dont le contenu ET le titre existent
    dans la langue visée.
    """
    rapport = []
    for niveau in CURRICULUM:
        traduites = 0
        for lecon in niveau["lessons"]:
            titre_ok = bool(lecon.get(f"title_{langue}"))
            corps_ok = bool(lecon.get(f"content_{langue}"))
            if titre_ok and corps_ok:
                traduites += 1
        rapport.append({
            "id": niveau["id"],
            "titre": niveau["title"],
            "traduites": traduites,
            "total": len(niveau["lessons"]),
        })
    return rapport


def hints_for(lesson, exercice=None, langue="fr"):
    """Indices : ceux de l'exercice, sinon de la leçon, sinon du fichier hints."""
    if exercice is not None and exercice.get("hints"):
        return traduit(exercice, "hints", langue)
    if lesson.get("hints"):
        return traduit(lesson, "hints", langue)
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
