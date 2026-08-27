"""
Traduit les erreurs Python courantes en explications pédagogiques (FR).

`expliquer(texte_erreur)` reçoit le message brut renvoyé par le runner
(ex. "NameError: name 'x' is not defined") et renvoie un conseil
compréhensible, ou None si l'erreur n'est pas reconnue.
"""

_CONSEILS = {
    "SyntaxError":
        "Erreur de syntaxe : Python n'arrive pas à lire cette ligne. "
        "Vérifie les deux-points « : » en fin de if/for/while/def, "
        "les parenthèses/guillemets bien fermés, et les virgules.",
    "IndentationError":
        "Problème d'indentation : le décalage des lignes ne va pas. "
        "Chaque bloc (après un « : ») doit être décalé de 4 espaces, "
        "et tout le bloc doit avoir le même décalage.",
    "TabError":
        "Tu mélanges des tabulations et des espaces pour l'indentation. "
        "Utilise uniquement des espaces (la touche Tab en insère 4 ici).",
    "NameError":
        "Tu utilises un nom que Python ne connaît pas. Causes fréquentes : "
        "une faute de frappe, une variable pas encore créée, ou des "
        "guillemets oubliés autour d'un texte.",
    "TypeError":
        "Opération entre types incompatibles (par ex. additionner un "
        "nombre et du texte). Pense à convertir avec int(), str() ou float().",
    "ValueError":
        "La valeur n'a pas le bon format pour l'opération. Typique : "
        "int(\"abc\") échoue car « abc » n'est pas un nombre.",
    "ZeroDivisionError":
        "Division par zéro : on ne peut pas diviser par 0. Vérifie le "
        "diviseur avant de diviser.",
    "IndexError":
        "Indice hors limites : tu demandes un élément qui n'existe pas "
        "dans la liste. Rappel : les indices vont de 0 à len(liste) - 1.",
    "KeyError":
        "Clé absente du dictionnaire. Vérifie l'orthographe de la clé, "
        "ou utilise dico.get(cle) pour éviter l'erreur.",
    "AttributeError":
        "Tu appelles une méthode ou un attribut qui n'existe pas sur cet "
        "objet. Vérifie le nom de la méthode et le type de la variable.",
    "ModuleNotFoundError":
        "Module introuvable : nom mal orthographié, ou module non installé. "
        "Vérifie ton « import ».",
    "ImportError":
        "Import impossible : l'élément demandé n'existe pas dans ce module.",
    "RecursionError":
        "Récursion infinie : une fonction s'appelle elle-même sans condition "
        "d'arrêt. Ajoute un cas de base qui stoppe la récursion.",
    "AssertionError":
        "Un test (assert) a échoué : le résultat obtenu ne correspond pas "
        "à ce qui était attendu. Relis bien l'énoncé.",
}


def expliquer(texte_erreur):
    if not texte_erreur:
        return None
    premier = texte_erreur.split(":", 1)[0].strip()
    # On gère aussi "(boucle infinie ?)" déjà formaté par le runner.
    if premier.startswith("Exécution interrompue"):
        return ("Ton programme a tourné trop longtemps. Cherche une boucle "
                "« while » dont la condition ne devient jamais fausse.")
    return _CONSEILS.get(premier)
