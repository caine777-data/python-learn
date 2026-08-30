"""Contenu de l'antisèche (cheat-sheet) imprimable : la syntaxe essentielle.

Chaque section = (titre, [(code, explication), ...]).
Le rendu HTML est produit par stats.cheatsheet_html().
"""

CHEATSHEET_FR = [
    ("Variables & types", [
        ("x = 5", "entier (int)"),
        ("pi = 3.14", "flottant (float)"),
        ('s = "texte"', "chaîne (str)"),
        ("ok = True", "booléen (bool)"),
        ("rien = None", "absence de valeur"),
        ("type(x)", "type d'une valeur"),
        ("int('3'), str(3)", "conversions"),
    ]),
    ("Chaînes de caractères", [
        ('f"Bonjour {nom}"', "insérer une variable (f-string)"),
        ('"abc".upper()', "→ 'ABC'"),
        ('"A,B".split(",")', "→ ['A', 'B']"),
        ('", ".join(liste)', "joindre une liste"),
        ("len(s)", "longueur"),
        ("s[0], s[-1]", "premier / dernier caractère"),
        ("s[::-1]", "inverser"),
        ('"py" in s', "contient ?"),
    ]),
    ("Listes", [
        ("l = [1, 2, 3]", "créer"),
        ("l.append(4)", "ajouter à la fin"),
        ("l.pop()", "retirer le dernier"),
        ("l[1:3]", "tranche (slicing)"),
        ("len(l)", "taille"),
        ("sorted(l)", "trier (copie)"),
        ("[x * 2 for x in l]", "compréhension de liste"),
        ("sum(l), max(l), min(l)", "agrégats"),
    ]),
    ("Dictionnaires", [
        ("d = {'a': 1}", "créer"),
        ("d['a']", "accès par clé"),
        ("d.get('b', 0)", "valeur par défaut si absente"),
        ("d['b'] = 2", "ajouter / modifier"),
        ("for k, v in d.items():", "parcourir clés/valeurs"),
        ("d.keys(), d.values()", "clés / valeurs"),
        ("'a' in d", "clé présente ?"),
    ]),
    ("Conditions", [
        ("if x > 0:", "si"),
        ("elif x == 0:", "sinon si"),
        ("else:", "sinon"),
        ("a and b / a or b", "et / ou"),
        ("not a", "négation"),
        ("x in liste", "appartenance"),
        ("y if cond else z", "expression conditionnelle"),
    ]),
    ("Boucles", [
        ("for i in range(5):", "i de 0 à 4"),
        ("for x in liste:", "chaque élément"),
        ("while condition:", "tant que"),
        ("break / continue", "sortir / passer au suivant"),
        ("enumerate(l)", "(indice, valeur)"),
        ("zip(a, b)", "parcourir en parallèle"),
    ]),
    ("Fonctions", [
        ("def f(x):", "définir"),
        ("return x", "renvoyer une valeur"),
        ("def f(x=1):", "argument par défaut"),
        ("def f(*args, **kwargs):", "arguments variables"),
        ("lambda x: x + 1", "fonction anonyme"),
    ]),
    ("Classes", [
        ("class Chat:", "définir une classe"),
        ("def __init__(self, nom):", "constructeur"),
        ("self.nom = nom", "attribut d'instance"),
        ("def miauler(self):", "méthode"),
        ("c = Chat('Félix')", "instancier"),
    ]),
    ("Fichiers", [
        ("with open('f.txt') as f:", "ouvrir en lecture"),
        ("f.read()", "tout lire"),
        ("for ligne in f:", "ligne par ligne"),
        ("open('f.txt', 'w')", "ouvrir en écriture"),
        ("f.write(texte)", "écrire"),
    ]),
    ("Erreurs", [
        ("try:", "essayer"),
        ("except ValueError:", "attraper une erreur"),
        ("finally:", "exécuté dans tous les cas"),
        ("raise ValueError('msg')", "lever une erreur"),
        ("assert x == 1", "vérifier une hypothèse"),
    ]),
    ("Modules utiles", [
        ("import math", "racine, pi, factorielle…"),
        ("import random", "aléatoire (choice, randint)"),
        ("import json", "lire/écrire du JSON"),
        ("from collections import Counter", "compter des occurrences"),
        ("import statistics", "moyenne, médiane…"),
        ("from datetime import date", "dates"),
    ]),
]

CHEATSHEET_EN = [
    ("Variables & types", [
        ("x = 5", "integer (int)"),
        ("pi = 3.14", "float (float)"),
        ('s = "text"', "string (str)"),
        ("ok = True", "boolean (bool)"),
        ("nothing = None", "null / absence of value"),
        ("type(x)", "type of a value"),
        ("int('3'), str(3)", "type conversions"),
    ]),
    ("Strings", [
        ('f"Hello {name}"', "variable insertion (f-string)"),
        ('"abc".upper()', "→ 'ABC'"),
        ('"A,B".split(",")', "→ ['A', 'B']"),
        ('", ".join(liste)', "join a list"),
        ("len(s)", "length"),
        ("s[0], s[-1]", "first / last character"),
        ("s[::-1]", "reverse string"),
        ('"py" in s', "contains substring?"),
    ]),
    ("Lists", [
        ("l = [1, 2, 3]", "create list"),
        ("l.append(4)", "append to end"),
        ("l.pop()", "remove & return last item"),
        ("l[1:3]", "slicing"),
        ("len(l)", "length / size"),
        ("sorted(l)", "sort (new copy)"),
        ("[x * 2 for x in l]", "list comprehension"),
        ("sum(l), max(l), min(l)", "aggregates"),
    ]),
    ("Dictionaries", [
        ("d = {'a': 1}", "create dict"),
        ("d['a']", "access by key"),
        ("d.get('b', 0)", "default value if key missing"),
        ("d['b'] = 2", "add / update key"),
        ("for k, v in d.items():", "iterate over key/value pairs"),
        ("d.keys(), d.values()", "keys / values"),
        ("'a' in d", "is key in dict?"),
    ]),
    ("Conditions", [
        ("if x > 0:", "if"),
        ("elif x == 0:", "else if"),
        ("else:", "else"),
        ("a and b / a or b", "and / or"),
        ("not a", "negation (not)"),
        ("x in liste", "membership test"),
        ("y if cond else z", "ternary conditional expression"),
    ]),
    ("Loops", [
        ("for i in range(5):", "i from 0 to 4"),
        ("for x in liste:", "iterate each element"),
        ("while condition:", "while loop"),
        ("break / continue", "exit loop / skip to next"),
        ("enumerate(l)", "(index, value) tuples"),
        ("zip(a, b)", "iterate in parallel"),
    ]),
    ("Functions", [
        ("def f(x):", "define function"),
        ("return x", "return a value"),
        ("def f(x=1):", "default argument"),
        ("def f(*args, **kwargs):", "variable arguments"),
        ("lambda x: x + 1", "anonymous lambda function"),
    ]),
    ("Classes", [
        ("class Chat:", "define a class"),
        ("def __init__(self, nom):", "constructor"),
        ("self.nom = nom", "instance attribute"),
        ("def miauler(self):", "instance method"),
        ("c = Chat('Felix')", "instantiate"),
    ]),
    ("Files", [
        ("with open('f.txt') as f:", "open in read mode"),
        ("f.read()", "read whole file"),
        ("for ligne in f:", "line by line iteration"),
        ("open('f.txt', 'w')", "open in write mode"),
        ("f.write(texte)", "write string"),
    ]),
    ("Error Handling", [
        ("try:", "try block"),
        ("except ValueError:", "catch error"),
        ("finally:", "always executed"),
        ("raise ValueError('msg')", "raise custom error"),
        ("assert x == 1", "verify assumption"),
    ]),
    ("Standard Modules", [
        ("import math", "sqrt, pi, factorial…"),
        ("import random", "randomness (choice, randint)"),
        ("import json", "read/write JSON"),
        ("from collections import Counter", "tally occurrences"),
        ("import statistics", "mean, median…"),
        ("from datetime import date", "dates & timestamps"),
    ]),
]

CHEATSHEET = CHEATSHEET_FR


def get_cheatsheet(lang="fr"):
    """Renvoie l'antisèche dans la langue demandée (par défaut français)."""
    return CHEATSHEET_EN if lang == "en" else CHEATSHEET_FR

