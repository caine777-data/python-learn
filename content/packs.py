"""
Packs de leçons : ajouter ses propres exercices sans toucher au code.

Un pack est un simple fichier JSON déposé dans ~/.python-learn/lessons/.
Il décrit un parcours entier — titre, auteur, liste de leçons — et vient
s'ajouter aux 15 parcours livrés avec l'application. C'est ce qui permet
à un enseignant de composer ses propres exercices, puis de les partager
en envoyant un seul fichier.

⚠️ Un pack contient du code Python (les champs « check » et « solution »)
qui sera exécuté sur la machine de l'apprenant lorsqu'il cliquera sur
« Vérifier » ou « Solution ». Il ne faut donc installer que des packs
dont on connaît la provenance, exactement comme pour un programme. Rien
n'est exécuté au chargement : la validation ci-dessous ne fait que lire
la structure du fichier.

La validation est volontairement bavarde. Celui qui écrit un pack n'est
pas forcément programmeur : un message précis (« leçon 3 : answer vaut 5
mais il n'y a que 3 options ») vaut mieux qu'une exception.
"""

import json
from pathlib import Path

FORMAT_ACTUEL = 1
DOSSIER_PACKS = Path.home() / ".python-learn" / "lessons"

# Marqueur affiché devant le titre, pour distinguer d'un coup d'œil un
# parcours ajouté par l'utilisateur des parcours d'origine.
PREFIXE_TITRE = "📦 "

_CHAMPS_TEXTE = ("content", "starter", "solution", "check",
                 "expected_output", "prompt", "explanation", "mode")
_CHAMPS_LISTE = ("hints", "stdin")


def _est_texte(valeur):
    return isinstance(valeur, str)


def _valider_exercice(exo, ou, problemes):
    """Contrôle les champs d'un exercice (leçon simple ou sous-exercice).

    Un champ mal formé est RETIRÉ plutôt que laissé en place : l'interface
    ne doit jamais recevoir, par exemple, un « hints » qui serait un texte
    au lieu d'une liste — elle en parcourrait les lettres une à une.
    """
    for champ in _CHAMPS_TEXTE:
        if champ in exo and not _est_texte(exo[champ]):
            problemes.append(f"{ou} : « {champ} » doit être du texte, champ ignoré.")
            exo.pop(champ)
    for champ in _CHAMPS_LISTE:
        if champ in exo:
            valeur = exo[champ]
            if not isinstance(valeur, list) or not all(_est_texte(v) for v in valeur):
                problemes.append(
                    f"{ou} : « {champ} » doit être une liste de textes, "
                    "champ ignoré.")
                exo.pop(champ)
    if exo.get("check") is None and exo.get("expected_output") is None:
        problemes.append(
            f"{ou} : aucune vérification (« check » ou « expected_output »). "
            "L'exercice sera validé dès qu'il s'exécute sans erreur.")


def _valider_quiz(lecon, ou, problemes):
    """Contrôle un quiz. Renvoie False s'il est injouable.

    Un quiz dont la bonne réponse est hors des options est pire qu'absent :
    l'apprenant ne pourrait jamais le réussir. On l'écarte.
    """
    question = lecon.get("question")
    options = lecon.get("options")
    reponse = lecon.get("answer")

    if not _est_texte(question) or not question.strip():
        problemes.append(f"{ou} : un quiz doit avoir une « question ».")
        return False
    if not isinstance(options, list) or len(options) < 2:
        problemes.append(f"{ou} : un quiz doit avoir au moins deux « options ».")
        return False
    if not all(_est_texte(o) for o in options):
        problemes.append(f"{ou} : les « options » doivent être des textes.")
        return False
    if not isinstance(reponse, int) or isinstance(reponse, bool):
        problemes.append(
            f"{ou} : « answer » doit être le numéro de la bonne option "
            f"(0 pour la première, {len(options) - 1} pour la dernière).")
        return False
    if not 0 <= reponse < len(options):
        problemes.append(
            f"{ou} : « answer » vaut {reponse}, mais il n'y a que "
            f"{len(options)} options (numérotées de 0 à {len(options) - 1}). "
            "Quiz écarté : personne ne pourrait le réussir.")
        return False
    return True


def _valider_lecon(lecon, rang, ids_pris, problemes):
    """Contrôle une leçon. Renvoie True si elle est utilisable."""
    ou = f"leçon {rang}"
    if not isinstance(lecon, dict):
        problemes.append(f"{ou} : ce n'est pas un objet JSON (accolades).")
        return False

    identifiant = lecon.get("id")
    titre = lecon.get("title")
    if not _est_texte(identifiant) or not identifiant.strip():
        problemes.append(f"{ou} : « id » manquant (un identifiant unique).")
        return False
    ou = f"leçon {rang} (« {identifiant} »)"

    if identifiant in ids_pris:
        problemes.append(
            f"{ou} : cet identifiant est déjà utilisé. Choisis-en un autre, "
            "par exemple en le préfixant du nom de ton pack.")
        return False
    if "#" in identifiant:
        problemes.append(f"{ou} : le caractère « # » est réservé dans un id.")
        return False
    if not _est_texte(titre) or not titre.strip():
        problemes.append(f"{ou} : « title » manquant (le titre affiché).")
        return False

    if lecon.get("type") == "quiz":
        if not _valider_quiz(lecon, ou, problemes):
            return False
        ids_pris.add(identifiant)
        return True

    exercices = lecon.get("exercices")
    if exercices is not None:
        if not isinstance(exercices, list) or not exercices:
            problemes.append(f"{ou} : « exercices » doit être une liste non vide.")
            return False
        for i, exo in enumerate(exercices):
            if not isinstance(exo, dict):
                problemes.append(f"{ou}, exercice {i + 1} : ce n'est pas un objet JSON.")
                return False
            _valider_exercice(exo, f"{ou}, exercice {i + 1}", problemes)
    else:
        _valider_exercice(lecon, ou, problemes)

    ids_pris.add(identifiant)
    return True


def valider_pack(donnees, ids_pris=None):
    """Contrôle un pack déjà décodé. Renvoie (parcours, problèmes).

    `parcours` est None si le pack est inutilisable. `problèmes` peut être
    non vide même quand le pack est utilisable : ce sont alors des
    avertissements sur des leçons écartées.
    """
    problemes = []
    ids_pris = set() if ids_pris is None else set(ids_pris)

    if not isinstance(donnees, dict):
        return None, ["Le fichier doit contenir un objet JSON (des accolades)."]

    version = donnees.get("format", FORMAT_ACTUEL)
    if not isinstance(version, int) or version > FORMAT_ACTUEL:
        return None, [
            f"Ce pack annonce le format {version}, mais cette version de "
            f"PythonLearn ne connaît que le format {FORMAT_ACTUEL}. "
            "Mets l'application à jour."]

    identifiant = donnees.get("id")
    titre = donnees.get("titre") or donnees.get("title")
    if not _est_texte(identifiant) or not identifiant.strip():
        return None, ["« id » manquant : donne un identifiant à ton pack."]
    if not _est_texte(titre) or not titre.strip():
        return None, ["« titre » manquant : c'est le nom affiché du parcours."]

    lecons = donnees.get("lecons") or donnees.get("lessons")
    if not isinstance(lecons, list) or not lecons:
        return None, ["« lecons » manquant ou vide : un pack doit contenir "
                      "au moins une leçon."]

    retenues = []
    for rang, lecon in enumerate(lecons, start=1):
        if _valider_lecon(lecon, rang, ids_pris, problemes):
            retenues.append(lecon)

    if not retenues:
        problemes.append("Aucune leçon utilisable dans ce pack.")
        return None, problemes

    auteur = donnees.get("auteur") or donnees.get("author")
    parcours = {
        "id": identifiant,
        "title": PREFIXE_TITRE + titre,
        "lessons": retenues,
        "pack": True,
    }
    if _est_texte(auteur) and auteur.strip():
        parcours["auteur"] = auteur
    return parcours, problemes


def lire_pack(chemin, ids_pris=None):
    """Lit et valide un fichier de pack. Renvoie (parcours, problèmes)."""
    try:
        texte = Path(chemin).read_text(encoding="utf-8")
    except OSError as exc:
        return None, [f"Fichier illisible : {exc}"]
    try:
        donnees = json.loads(texte)
    except json.JSONDecodeError as exc:
        return None, [
            f"JSON invalide, ligne {exc.lineno} : {exc.msg}. "
            "Vérifie les virgules et les guillemets."]
    return valider_pack(donnees, ids_pris)


def charger_packs(dossier=None, ids_existants=()):
    """Charge tous les packs d'un dossier, dans l'ordre alphabétique.

    Renvoie (parcours, problèmes) où `problèmes` est une liste de textes
    prêts à être affichés, chacun préfixé du nom du fichier concerné.
    """
    dossier = Path(dossier) if dossier else DOSSIER_PACKS
    if not dossier.is_dir():
        return [], []

    ids_pris = set(ids_existants)
    parcours, problemes = [], []

    for fichier in sorted(dossier.glob("*.json")):
        niveau, soucis = lire_pack(fichier, ids_pris)
        for souci in soucis:
            problemes.append(f"{fichier.name} — {souci}")
        if niveau is None:
            continue
        if niveau["id"] in ids_pris:
            problemes.append(
                f"{fichier.name} — un parcours porte déjà l'identifiant "
                f"« {niveau['id']} » : pack ignoré.")
            continue
        ids_pris.add(niveau["id"])
        for lecon in niveau["lessons"]:
            ids_pris.add(lecon["id"])
        parcours.append(niveau)

    return parcours, problemes


def modele_pack():
    """Renvoie un pack d'exemple complet, prêt à être modifié."""
    exemple = {
        "format": FORMAT_ACTUEL,
        "id": "mon-cours",
        "titre": "Mon cours",
        "auteur": "Prénom Nom",
        "lecons": [
            {
                "id": "moncours-01",
                "title": "Afficher un message",
                "content": (
                    "## Afficher du texte\n\n"
                    "La fonction `print()` affiche ce qu'on lui donne.\n\n"
                    "```\nprint('Bonjour')\n```\n\n"
                    "- le texte va entre guillemets\n"
                    "- **Exercice** : affiche `Bonjour la classe`"
                ),
                "starter": "# Écris ton code ici\n",
                "expected_output": "Bonjour la classe",
                "solution": "print('Bonjour la classe')\n",
                "hints": [
                    "Utilise print(...).",
                    "Le texte doit être entre guillemets.",
                ],
            },
            {
                "id": "moncours-02",
                "title": "Calculer une moyenne",
                "content": (
                    "## Calculer\n\n"
                    "Range le résultat dans une variable nommée `moyenne`.\n\n"
                    "- **Exercice** : la moyenne de 12, 15 et 18"
                ),
                "starter": "notes = [12, 15, 18]\nmoyenne = \n",
                "check": "assert moyenne == 15, 'la moyenne devrait valoir 15'",
                "solution": "notes = [12, 15, 18]\nmoyenne = sum(notes) / len(notes)\n",
            },
            {
                "id": "moncours-quiz",
                "type": "quiz",
                "title": "Quiz de fin",
                "content": "Une question pour vérifier que tout est clair.",
                "question": "Que fait print('2' + '3') ?",
                "options": ["Affiche 5", "Affiche 23", "Provoque une erreur"],
                "answer": 1,
                "explanation": (
                    "Entre guillemets, ce sont des textes : « + » les colle "
                    "bout à bout au lieu de les additionner."
                ),
            },
        ],
    }
    return json.dumps(exemple, ensure_ascii=False, indent=2) + "\n"
