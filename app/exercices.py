"""
Deux types d'exercices qui font travailler autre chose que l'écriture de code.

« prédis la sortie » (type "predire")
    On montre un programme, l'apprenant écrit ce qu'il pense qu'il va
    afficher, PUIS on l'exécute. C'est l'antidote au tâtonnement : sans
    cela, rien n'empêche de modifier son code au hasard jusqu'à ce que la
    vérification passe, sans jamais avoir lu ce qu'on écrivait.

« remets dans l'ordre » (type "ordre", dits « problèmes de Parsons »)
    Les lignes d'un programme correct sont mélangées ; il faut les
    remettre en ordre. On travaille la logique et la structure sans avoir
    à produire la syntaxe — ce qui allège beaucoup la marche pour un
    débutant, et permet d'aborder des programmes plus ambitieux que ce
    qu'il saurait écrire seul.

Ce module ne contient que la logique : il est donc testable sans écran,
et les deux types fonctionnent aussi bien dans les parcours livrés que
dans les packs de leçons créés par les utilisateurs.
"""

import random

from app.runner import run_code, run_exercise

TYPES = ("predire", "ordre")


def est_special(lecon):
    """Vrai si la leçon relève d'un de ces types particuliers."""
    return lecon.get("type") in TYPES


# --------------------------------------------------------- prédis la sortie
def normaliser_sortie(texte):
    """Réduit une sortie à ce qui compte pour la comparer.

    On ignore les espaces en début et fin de ligne ainsi que les lignes
    vides finales : un apprenant ne doit pas échouer pour un espace en
    trop. En revanche l'ordre et le contenu des lignes comptent.
    """
    lignes = [ligne.strip() for ligne in (texte or "").strip().splitlines()]
    while lignes and not lignes[-1]:
        lignes.pop()
    return lignes


def verifier_prediction(code, prediction, stdin_lines=None, timeout=6.0):
    """Compare la sortie annoncée par l'apprenant à la sortie réelle.

    Renvoie (reussi, sortie_reelle, erreur) — `erreur` est le message
    d'exécution si le programme a échoué, None sinon.
    """
    namespace = {}
    if stdin_lines is not None:
        entrees = iter(stdin_lines)
        namespace["input"] = lambda invite="": next(entrees, "")

    resultat, _ = run_code(code, namespace, timeout=timeout)
    if not resultat.ok:
        return False, resultat.output, resultat.error

    reussi = normaliser_sortie(prediction) == normaliser_sortie(resultat.output)
    return reussi, resultat.output, None


def premiere_difference(prediction, sortie_reelle):
    """Numéro de la première ligne qui diffère, ou None si tout concorde.

    Sert à pointer l'endroit exact où le raisonnement a dévié, plutôt que
    de renvoyer un « faux » sans explication.
    """
    attendue = normaliser_sortie(sortie_reelle)
    proposee = normaliser_sortie(prediction)
    for i in range(max(len(attendue), len(proposee))):
        a = attendue[i] if i < len(attendue) else None
        p = proposee[i] if i < len(proposee) else None
        if a != p:
            return i + 1
    return None


# ------------------------------------------------------ remets dans l'ordre
def lignes_de(lecon):
    """Les lignes attendues d'un exercice de remise en ordre."""
    lignes = lecon.get("lignes")
    if isinstance(lignes, list):
        return [ligne for ligne in lignes if isinstance(ligne, str)]
    return []


def melanger(lignes, graine):
    """Mélange les lignes de façon reproductible, jamais dans le bon ordre.

    Reproductible : la même leçon présente toujours le même mélange, sinon
    revenir sur un exercice donnerait l'impression que tout a changé.
    Jamais dans le bon ordre : un exercice déjà résolu à l'ouverture
    n'apprendrait rien.
    """
    if len(lignes) < 2:
        return list(lignes)

    tirage = random.Random(graine)
    melange = list(lignes)
    for _ in range(20):
        tirage.shuffle(melange)
        if melange != list(lignes):
            return melange
    # Toutes les lignes sont identiques : on renvoie une permutation simple.
    return list(lignes[1:]) + [lignes[0]]


def code_depuis_lignes(lignes):
    """Reconstitue un programme à partir des lignes ordonnées."""
    return "\n".join(lignes) + "\n"


def verifier_ordre(proposition, lecon, timeout=6.0):
    """Contrôle une remise en ordre. Renvoie (reussi, message).

    Deux façons de valider, de la plus souple à la plus stricte :
      - si la leçon fournit « check » ou « expected_output », on exécute le
        programme reconstitué : plusieurs ordres peuvent alors être justes,
        ce qui est plus honnête (deux affectations indépendantes peuvent
        être écrites dans n'importe quel sens) ;
      - sinon, on compare à l'ordre d'origine.
    """
    attendues = lignes_de(lecon)
    if lecon.get("check") or lecon.get("expected_output") is not None:
        _, reussi, message = run_exercise(
            code_depuis_lignes(proposition),
            check_code=lecon.get("check"),
            expected_output=lecon.get("expected_output"),
            stdin_lines=lecon.get("stdin"),
            timeout=timeout)
        return reussi, message

    if list(proposition) == attendues:
        return True, "Bon ordre, bravo !"
    return False, "Ce n'est pas encore le bon ordre."


def premiere_ligne_fautive(proposition, lecon):
    """Rang de la première ligne mal placée, ou None. Sert d'indice."""
    attendues = lignes_de(lecon)
    for i, ligne in enumerate(proposition):
        if i >= len(attendues) or ligne != attendues[i]:
            return i + 1
    return None
