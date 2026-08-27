"""Contenu de l'antisèche (cheat-sheet) imprimable : la syntaxe essentielle.

Chaque section = (titre, [(code, explication), ...]).
Le rendu HTML est produit par stats.cheatsheet_html().
"""

CHEATSHEET = [
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
