"""
Parcours — Décoder les erreurs.

La compétence qui débloque un débutant n'est pas d'écrire du code sans
faute : c'est de savoir lire le message quand ça casse. Tant qu'une
erreur reste un mur rouge incompréhensible, on avance par tâtonnement.

Chaque leçon présente un message d'erreur réel, apprend à en repérer les
trois informations utiles (le TYPE, le MESSAGE, la LIGNE), puis fait
corriger un programme qui échoue vraiment.

Ce parcours peut être suivi dès la fin du niveau débutant : il ne
suppose que les variables, les listes et les fonctions.
"""

LEVEL = {
    "id": "erreurs",
    "title": "16 · Décoder les erreurs",
    "lessons": [
        {
            "id": "err-01",
            "title": "Lire un message d'erreur",
            "content": """## Trois informations, toujours les mêmes

Quand Python s'arrête, il ne se moque pas de toi : il explique très
précisément ce qui l'a bloqué. Encore faut-il savoir où regarder.

```
Traceback (most recent call last):
  File "<exercice>", line 3, in <module>
    print(totl)
NameError: name 'totl' is not defined
```

Trois choses à repérer, et une seule à lire en premier :

- **la dernière ligne** : le TYPE d'erreur (`NameError`) et son
  explication (`name 'totl' is not defined`) ;
- **le numéro de ligne** (`line 3`) : où Python s'est arrêté ;
- **la ligne de code recopiée** : ce qu'il essayait de faire.

**On lit toujours la dernière ligne en premier.** Le reste, c'est le
chemin parcouru pour y arriver.

- **Exercice** : ce programme s'arrête. Lis l'erreur, corrige la faute
  de frappe.""",
            "mode": "debug",
            "starter": """prix = 10
quantite = 3
total = prix * quantite
print(totl)
""",
            "expected_output": "30",
            "solution": """prix = 10
quantite = 3
total = prix * quantite
print(total)
""",
            "hints": [
                "Lis la dernière ligne du message : quel nom Python ne connaît pas ?",
                "Compare le nom écrit dans print() avec celui de la ligne 3.",
                "« totl » n'existe pas : la variable s'appelle « total ».",
            ],
        },
        {
            "id": "err-02",
            "type": "predire",
            "title": "Quel type d'erreur va apparaître ?",
            "content": """## Reconnaître avant de corriger

Chaque type d'erreur correspond à une famille de causes. Les connaître
fait gagner un temps considérable :

- `NameError` — un nom que Python ne connaît pas
- `TypeError` — une opération entre choses incompatibles
- `ValueError` — le bon type, mais une valeur impossible
- `IndexError` — un élément demandé hors de la liste
- `KeyError` — une clé absente d'un dictionnaire
- `ZeroDivisionError` — une division par zéro

Ici, le programme fonctionne. Prédis simplement ce qu'il affiche : c'est
un rappel de ce que fait `type()`, qui sert souvent à comprendre un
`TypeError`.""",
            "code": """print(type(3))
print(type('3'))
print(type([3]))
""",
            "explanation": (
                "Un TypeError vient presque toujours de là : deux valeurs qui "
                "se ressemblent à l'écran (3 et '3') mais ne sont pas du même "
                "type. En cas de doute, affiche type(ma_variable)."
            ),
        },
        {
            "id": "err-03",
            "title": "TypeError : additionner des choux et des carottes",
            "content": """## Le type compte plus que l'apparence

```
TypeError: can only concatenate str (not "int") to str
```

Ce message dit : « je sais coller du texte à du texte, mais pas un
nombre à du texte ». Python ne devine jamais ce que tu voulais dire.

La solution est presque toujours une **conversion** :

- `str(42)` transforme le nombre 42 en texte `"42"`
- `int("42")` transforme le texte `"42"` en nombre 42

```
age = 30
print("J'ai " + str(age) + " ans")
```

- **Exercice** : ce programme plante. Convertis ce qu'il faut pour qu'il
  affiche `Il reste 5 places`.""",
            "mode": "debug",
            "starter": """places = 5
print("Il reste " + places + " places")
""",
            "expected_output": "Il reste 5 places",
            "solution": """places = 5
print("Il reste " + str(places) + " places")
""",
            "hints": [
                "Le message dit qu'on ne peut coller que du texte à du texte.",
                "Quelle est la seule valeur qui n'est pas du texte, ici ?",
                "Entoure places de str(...).",
            ],
        },
        {
            "id": "err-04",
            "title": "IndexError et KeyError : ça n'existe pas",
            "content": """## Compter à partir de zéro

```
IndexError: list index out of range
```

Le premier élément d'une liste porte l'indice **0**. Une liste de 3
éléments a donc les indices 0, 1 et 2 — jamais 3.

```
couleurs = ["rouge", "vert", "bleu"]
print(couleurs[0])    # rouge
print(couleurs[2])    # bleu
print(couleurs[3])    # IndexError
```

Le dernier élément s'obtient avec `liste[-1]`, ou `liste[len(liste) - 1]`.

Pour un dictionnaire, l'erreur s'appelle `KeyError` : la clé demandée
n'existe pas. `dico.get("cle")` renvoie `None` au lieu de planter.

- **Exercice** : ce programme veut afficher la dernière note. Corrige-le.""",
            "mode": "debug",
            "starter": """notes = [12, 15, 18]
print(notes[3])
""",
            "expected_output": "18",
            "solution": """notes = [12, 15, 18]
print(notes[-1])
""",
            "hints": [
                "La liste a 3 éléments : quels sont les indices valables ?",
                "Le dernier élément est à l'indice 2, pas 3.",
                "notes[-1] désigne toujours le dernier élément.",
            ],
        },
        {
            "id": "err-05",
            "title": "SyntaxError : l'erreur est souvent AVANT",
            "content": """## Le piège du numéro de ligne

Pour une erreur de syntaxe, Python signale l'endroit où il a **compris
que ça n'allait pas** — pas toujours l'endroit de la faute.

```
  File "<exercice>", line 2
    print("bonjour")
    ^^^^^
SyntaxError: invalid syntax
```

Si la ligne signalée paraît correcte, **regarde la ligne du dessus** :
une parenthèse jamais refermée, un guillemet manquant, ou les deux-points
oubliés en fin de `if`, `for`, `while` ou `def`.

C'est aussi la seule famille d'erreurs que Python détecte **avant**
d'exécuter quoi que ce soit : si tu ne vois aucun affichage, même pas
celui des premières lignes, c'est presque toujours une SyntaxError.

- **Exercice** : répare ce programme pour qu'il affiche `7`.""",
            "mode": "debug",
            "starter": """resultat = (3 + 4
print(resultat)
""",
            "expected_output": "7",
            "solution": """resultat = (3 + 4)
print(resultat)
""",
            "hints": [
                "L'erreur est signalée ligne 2, mais la ligne 2 est correcte.",
                "Regarde la ligne 1 : compte les parenthèses ouvertes et fermées.",
                "Il manque une parenthèse fermante après le 4.",
            ],
        },
        {
            "id": "err-06",
            "title": "ValueError : le bon type, la mauvaise valeur",
            "content": """## Quand la conversion échoue

```
ValueError: invalid literal for int() with base 10: 'douze'
```

`int()` attend bien du texte — c'est donc le bon **type**. Mais « douze »
n'est pas une écriture de nombre : c'est la **valeur** qui ne convient
pas. D'où `ValueError` et non `TypeError`.

Cette erreur est très fréquente avec `input()`, qui renvoie toujours du
texte : si l'utilisateur tape autre chose qu'un nombre, `int()` échoue.

- **Exercice** : ce programme doit afficher le double de 12. Corrige la
  valeur pour que la conversion réussisse.""",
            "mode": "debug",
            "starter": """texte = "douze"
nombre = int(texte)
print(nombre * 2)
""",
            "expected_output": "24",
            "solution": """texte = "12"
nombre = int(texte)
print(nombre * 2)
""",
            "hints": [
                "int() sait lire « 12 », mais pas « douze ».",
                "Écris le nombre en chiffres, entre guillemets.",
            ],
        },
        {
            "id": "err-07",
            "title": "Remonter un traceback",
            "content": """## Suivre le chemin

Quand l'erreur se produit dans une fonction, Python affiche tout le
chemin parcouru :

```
Traceback (most recent call last):
  File "<exercice>", line 7, in <module>
    print(moyenne([]))
  File "<exercice>", line 4, in moyenne
    return total / len(valeurs)
ZeroDivisionError: division by zero
```

Deux niveaux, à lire **de bas en haut** :

- l'erreur s'est produite **ligne 4**, dans la fonction `moyenne` ;
- cette fonction avait été appelée **ligne 7**.

La cause est souvent en haut (l'appel fautif : une liste vide), le
symptôme en bas (la division). C'est pour cela qu'on lit d'abord la
dernière ligne, puis qu'on remonte.

- **Exercice** : protège la fonction pour qu'une liste vide renvoie `0`
  au lieu de planter.""",
            "mode": "debug",
            "starter": """def moyenne(valeurs):
    total = 0
    for v in valeurs:
        total = total + v
    return total / len(valeurs)

print(moyenne([]))
""",
            "expected_output": "0",
            "solution": """def moyenne(valeurs):
    if len(valeurs) == 0:
        return 0
    total = 0
    for v in valeurs:
        total = total + v
    return total / len(valeurs)

print(moyenne([]))
""",
            "hints": [
                "L'erreur vient de la division par len(valeurs), qui vaut 0.",
                "Traite le cas de la liste vide AVANT de diviser.",
                "Ajoute au début : if len(valeurs) == 0: return 0",
            ],
        },
        {
            "id": "err-08",
            "type": "ordre",
            "title": "Remets dans l'ordre : une saisie sous contrôle",
            "content": """## Le bon ordre pour se protéger

Voici la façon habituelle de convertir une saisie sans risquer un
`ValueError` : on tente la conversion, et on prévoit le cas où elle
échoue.

Remets les lignes dans l'ordre pour que le programme affiche `nombre
invalide` sans planter.""",
            "lignes": [
                "texte = 'douze'",
                "try:",
                "    nombre = int(texte)",
                "    print(nombre)",
                "except ValueError:",
                "    print('nombre invalide')",
            ],
            "expected_output": "nombre invalide",
        },
    ],
}
