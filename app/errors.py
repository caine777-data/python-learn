"""
Traduit les erreurs Python courantes en explications pédagogiques.

`expliquer(texte_erreur, langue)` reçoit le message brut renvoyé par le
runner (ex. « NameError: name 'x' is not defined ») et renvoie un conseil
compréhensible dans la langue de l'interface, ou None si l'erreur n'est
pas reconnue.

Les explications sont volontairement écrites pour un débutant : ce qui
s'est passé, puis les causes les plus fréquentes — jamais le vocabulaire
de l'interpréteur.
"""

CONSEILS = {
    "fr": {
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
        "TimeoutError":
            "Ton programme a tourné trop longtemps. Cherche une boucle "
            "« while » dont la condition ne devient jamais fausse.",
    },
    "en": {
        "SyntaxError":
            "Syntax error: Python cannot read this line. Check the colon "
            "« : » at the end of if/for/while/def, that brackets and quotes "
            "are properly closed, and the commas.",
        "IndentationError":
            "Indentation problem: the lines are not lined up correctly. "
            "Every block (after a « : ») must be indented by 4 spaces, and "
            "the whole block must share the same indentation.",
        "TabError":
            "You are mixing tabs and spaces for indentation. Use spaces "
            "only (the Tab key inserts 4 of them here).",
        "NameError":
            "You are using a name Python does not know. Common causes: a "
            "typo, a variable that has not been created yet, or missing "
            "quotes around a piece of text.",
        "TypeError":
            "Operation between incompatible types (for example adding a "
            "number and some text). Convert with int(), str() or float().",
        "ValueError":
            "The value has the wrong format for this operation. A classic: "
            "int(\"abc\") fails because « abc » is not a number.",
        "ZeroDivisionError":
            "Division by zero: dividing by 0 is not possible. Check the "
            "divisor before dividing.",
        "IndexError":
            "Index out of range: you are asking for an item that does not "
            "exist in the list. Remember: indexes go from 0 to len(list) - 1.",
        "KeyError":
            "Key missing from the dictionary. Check the spelling of the key, "
            "or use my_dict.get(key) to avoid the error.",
        "AttributeError":
            "You are calling a method or attribute that does not exist on "
            "this object. Check the method name and the type of the variable.",
        "ModuleNotFoundError":
            "Module not found: misspelled name, or module not installed. "
            "Check your « import ».",
        "ImportError":
            "Import failed: the item you asked for does not exist in that module.",
        "RecursionError":
            "Infinite recursion: a function calls itself with no stopping "
            "condition. Add a base case that ends the recursion.",
        "AssertionError":
            "A test (assert) failed: the result does not match what was "
            "expected. Read the instructions again carefully.",
        "TimeoutError":
            "Your program ran for too long. Look for a « while » loop whose "
            "condition never becomes false.",
    },
}


def expliquer(texte_erreur, langue="fr"):
    """Conseil pédagogique correspondant à une erreur, ou None si inconnue.

    `texte_erreur` est de la forme « TypeErreur: détail » : seul le type
    nous intéresse, il suffit à choisir l'explication.
    """
    if not texte_erreur:
        return None
    conseils = CONSEILS.get(langue) or CONSEILS["fr"]

    # Le type d'exception est toujours sur la DERNIERE ligne du message.
    # Les erreurs de syntaxe et d'indentation - les plus frequentes chez un
    # debutant - sont en effet formatees sur plusieurs lignes par Python :
    #     File "<exercice>", line 2
    #         print('oui')
    #         ^^^^^
    #     IndentationError: expected an indented block
    # Lire la premiere ligne les laisserait sans explication.
    lignes = [ligne for ligne in texte_erreur.strip().splitlines() if ligne.strip()]
    if not lignes:
        return None
    type_erreur = lignes[-1].split(":", 1)[0].strip()
    return conseils.get(type_erreur)
