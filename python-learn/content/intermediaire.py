"""Niveau 2 — Intermédiaire."""

LEVEL = {
    "id": "intermediaire",
    "title": "2 · Intermédiaire",
    "lessons": [
        {
            "id": "int-01",
            "title": "Slicing et compréhensions de liste",
            "content": """## Découper une séquence

La syntaxe `liste[debut:fin:pas]` extrait une sous-partie.

```
lettres = list("PYTHON")
print(lettres[1:4])    # ['Y', 'T', 'H']
print(lettres[::-1])   # à l'envers
```

## Les compréhensions de liste

Une façon concise et idiomatique de construire une liste :

```
carres = [x * x for x in range(1, 6)]   # [1, 4, 9, 16, 25]
pairs = [n for n in range(20) if n % 2 == 0]
```

## Exercice

Avec une compréhension, range dans `cubes` la liste des cubes
(x³) des nombres de 1 à 10 inclus.""",
            "starter": "cubes = [...]\n",
            "check": "assert cubes == [x**3 for x in range(1, 11)]\n",
            "solution": "cubes = [x**3 for x in range(1, 11)]\n",
        },
        {
            "id": "int-02",
            "title": "Tuples et déballage",
            "content": """## Le tuple : une séquence immuable

Un tuple ressemble à une liste mais ne peut pas être modifié.
On l'écrit avec des parenthèses (ou sans).

```
point = (3, 4)
x, y = point          # déballage
print(x, y)           # 3 4
```

Le déballage est très pythonique. Il permet d'échanger deux variables
sans variable temporaire :

```
a, b = 1, 2
a, b = b, a           # a vaut 2, b vaut 1
```

## Exercice

Avec un seul déballage, affecte `mini` au plus petit et `maxi` au plus
grand de `(42, 7)`. Utilise la fonction `min()` et `max()`.""",
            "starter": "couple = (42, 7)\nmini, maxi = ...\n",
            "check": "assert mini == 7 and maxi == 42\n",
            "solution": "couple = (42, 7)\nmini, maxi = min(couple), max(couple)\n",
        },
        {
            "id": "int-03",
            "title": "Les dictionnaires",
            "content": """## Associer clés et valeurs

Un dictionnaire stocke des paires clé → valeur, entre accolades.

```
personne = {"nom": "Monna", "ville": "Le Fauga"}
print(personne["nom"])          # Monna
personne["metier"] = "auteur"   # ajout
```

On le parcourt avec `.items()`, `.keys()`, `.values()` :

```
for cle, valeur in personne.items():
    print(cle, "->", valeur)
```

`.get(cle, defaut)` évite l'erreur si la clé n'existe pas.

## Exercice

À partir de la phrase `"le chat le chien le chat"`, construis un
dictionnaire `freq` qui compte les occurrences de chaque mot.
Indice : `phrase.split()` découpe en mots.""",
            "starter": 'phrase = "le chat le chien le chat"\nfreq = {}\n# ...\n',
            "check": 'assert freq == {"le": 3, "chat": 2, "chien": 1}\n',
            "solution": 'phrase = "le chat le chien le chat"\nfreq = {}\n'
                        'for mot in phrase.split():\n'
                        '    freq[mot] = freq.get(mot, 0) + 1\n',
        },
        {
            "id": "int-04",
            "title": "Les fonctions",
            "content": """## Factoriser son code

Une fonction encapsule un traitement réutilisable. `def` la définit,
`return` renvoie un résultat.

```
def aire_rectangle(largeur, hauteur):
    return largeur * hauteur

print(aire_rectangle(3, 4))   # 12
```

On peut donner des valeurs par défaut aux paramètres :

```
def saluer(nom, politesse="Bonjour"):
    return f"{politesse} {nom}"

print(saluer("Ada"))                 # Bonjour Ada
print(saluer("Ada", "Coucou"))       # Coucou Ada
```

## Exercice

Écris une fonction `est_pair(n)` qui renvoie `True` si `n` est pair,
`False` sinon.""",
            "starter": "def est_pair(n):\n    ...\n",
            "check": "assert est_pair(4) is True\nassert est_pair(7) is False\nassert est_pair(0) is True\n",
            "solution": "def est_pair(n):\n    return n % 2 == 0\n",
        },
        {
            "id": "int-05",
            "title": "*args, **kwargs et lambda",
            "content": """## Nombre variable d'arguments

`*args` capture une liste d'arguments positionnels, `**kwargs` un
dictionnaire d'arguments nommés.

```
def total(*nombres):
    return sum(nombres)

print(total(1, 2, 3, 4))     # 10
```

## Les fonctions lambda

Une mini-fonction anonyme, sur une ligne :

```
double = lambda x: x * 2
print(double(21))            # 42
```

Très utile avec `sorted`, `map`, `filter` :

```
mots = ["python", "go", "rust"]
print(sorted(mots, key=lambda m: len(m)))  # ['go', 'rust', 'python']
```

## Exercice

Écris `moyenne(*notes)` qui renvoie la moyenne des notes reçues
(et `0` si aucune note).""",
            "starter": "def moyenne(*notes):\n    ...\n",
            "check": "assert moyenne(10, 20) == 15\nassert moyenne() == 0\nassert moyenne(12) == 12\n",
            "solution": "def moyenne(*notes):\n    if not notes:\n        return 0\n    return sum(notes) / len(notes)\n",
        },
        {
            "id": "int-06",
            "title": "Gérer les erreurs : try / except",
            "content": """## Attraper les exceptions

Quand une opération échoue, Python lève une exception. On l'intercepte
avec `try` / `except` pour éviter un plantage.

```
try:
    resultat = 10 / 0
except ZeroDivisionError:
    resultat = None
    print("Division par zéro évitée")
```

On peut lever soi-même une exception avec `raise` :

```
def racine(x):
    if x < 0:
        raise ValueError("nombre négatif")
    return x ** 0.5
```

`finally` s'exécute toujours, qu'il y ait eu erreur ou non.

## Exercice

Écris `division_sure(a, b)` qui renvoie `a / b`, mais renvoie la chaîne
`"erreur"` si `b` vaut 0.""",
            "starter": "def division_sure(a, b):\n    ...\n",
            "check": 'assert division_sure(10, 2) == 5\nassert division_sure(5, 0) == "erreur"\n',
            "solution": "def division_sure(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return \"erreur\"\n",
        },
        {
            "id": "int-07",
            "title": "Les ensembles (set)",
            "content": """## Des valeurs uniques

Un `set` est une collection **non ordonnée** d'éléments **uniques**.
Idéal pour dédoublonner ou tester l'appartenance très vite.

```
nombres = {1, 2, 2, 3, 3, 3}
print(nombres)          # {1, 2, 3}
print(2 in nombres)     # True
```

Les opérations ensemblistes sont natives :

```
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)   # intersection : {2, 3}
print(a | b)   # union        : {1, 2, 3, 4}
print(a - b)   # différence   : {1}
```

## Exercice

À partir de la liste `doublons = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]`,
range dans `uniques` le **nombre** de valeurs distinctes.""",
            "starter": "doublons = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\nuniques = ...\n",
            "check": "assert uniques == 7\n",
            "solution": "doublons = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\nuniques = len(set(doublons))\n",
        },
        {
            "id": "int-08",
            "title": "Modules et imports",
            "content": """## Réutiliser du code existant

Un module est un fichier de code que l'on importe. La bibliothèque
standard en regorge.

```
import math
print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.1415...

from random import randint
print(randint(1, 6))     # un dé

import datetime as dt
print(dt.date.today())
```

Trois formes : `import module`, `from module import nom`,
`import module as alias`.

## Exercice

À l'aide du module `math`, range dans `resultat` la partie entière
inférieure (plancher) de `7.8` (fonction `math.floor`).""",
            "starter": "import math\nresultat = ...\n",
            "check": "assert resultat == 7\n",
            "solution": "import math\nresultat = math.floor(7.8)\n",
        },
        {
            "id": "int-09",
            "title": "Trier avec sorted() et key",
            "content": """## Ordonner finement

`sorted()` renvoie une nouvelle liste triée ; `.sort()` trie sur place.
Le paramètre `key` indique **selon quel critère** trier, et `reverse`
inverse l'ordre.

```
mots = ["banane", "kiwi", "pomme"]
print(sorted(mots, key=len))          # par longueur
print(sorted(mots, reverse=True))     # ordre décroissant

gens = [("Ada", 36), ("Alan", 41)]
print(sorted(gens, key=lambda p: p[1]))   # par âge
```

## Exercice

Trie la liste de couples `scores = [("A", 9), ("B", 3), ("C", 7)]`
par score **décroissant** et range le résultat dans `classement`.""",
            "starter": 'scores = [("A", 9), ("B", 3), ("C", 7)]\nclassement = ...\n',
            "check": 'assert classement == [("A", 9), ("C", 7), ("B", 3)]\n',
            "solution": 'scores = [("A", 9), ("B", 3), ("C", 7)]\n'
                        'classement = sorted(scores, key=lambda p: p[1], reverse=True)\n',
        },
        {
            "id": "int-10",
            "title": "Compréhensions de dictionnaire",
            "content": """## Construire un dictionnaire en une ligne

Même principe que les compréhensions de liste, mais avec `clé: valeur`.

```
carres = {n: n * n for n in range(1, 5)}
# {1: 1, 2: 4, 3: 9, 4: 16}

prix = {"pain": 1.2, "lait": 0.9}
promo = {produit: p * 0.8 for produit, p in prix.items()}
```

On peut y ajouter une condition :

```
pairs = {n: "pair" for n in range(6) if n % 2 == 0}
```

## Exercice

À partir de `mots = ["python", "go", "rust"]`, construis `longueurs`,
un dictionnaire associant chaque mot à sa longueur.""",
            "starter": 'mots = ["python", "go", "rust"]\nlongueurs = ...\n',
            "check": 'assert longueurs == {"python": 6, "go": 2, "rust": 4}\n',
            "solution": 'mots = ["python", "go", "rust"]\nlongueurs = {m: len(m) for m in mots}\n',
        },
    ],
}
