"""Parcours — Algorithmes & structures de données."""

LEVEL = {
    "id": "algos",
    "title": "11 · Algorithmes & structures de données",
    "lessons": [
        {
            "id": "alg-01",
            "title": "Recherche linéaire",
            "content": """## Chercher un élément

L'algorithme le plus simple : parcourir la liste du début à la fin
jusqu'à trouver l'élément cherché.

```
def trouver(liste, cible):
    for i, valeur in enumerate(liste):
        if valeur == cible:
            return i
    return -1
```

On renvoie l'**indice** trouvé, ou `-1` si l'élément est absent. C'est
de complexité O(n) : dans le pire cas, on regarde tout.

## À toi

Écris `trouver(liste, cible)` qui renvoie l'indice de la première
occurrence de `cible`, ou `-1` si elle n'y est pas.""",
            "starter": "def trouver(liste, cible):\n    ...\n",
            "check": "assert trouver([10, 20, 30], 20) == 1\n"
                     "assert trouver([10, 20, 30], 99) == -1\n"
                     "assert trouver([], 1) == -1\n"
                     "assert trouver([5, 5], 5) == 0\n",
            "solution": "def trouver(liste, cible):\n"
                        "    for i, valeur in enumerate(liste):\n"
                        "        if valeur == cible:\n            return i\n    return -1\n",
            "hints": ["enumerate(liste) donne (indice, valeur).",
                      "Renvoie i dès que valeur == cible ; sinon -1 à la fin."],
        },
        {
            "id": "alg-02",
            "title": "Recherche dichotomique",
            "content": """## Diviser pour chercher plus vite

Sur une liste **déjà triée**, on peut faire bien mieux que tout
parcourir : on regarde l'élément du milieu, et on élimine la moitié qui
ne peut pas contenir la cible. Complexité O(log n).

```
def recherche_binaire(liste, cible):
    bas, haut = 0, len(liste) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if liste[milieu] == cible:
            return milieu
        elif liste[milieu] < cible:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1
```

## À toi

Implémente `recherche_binaire(liste, cible)` (la liste est triée par
ordre croissant). Renvoie l'indice, ou `-1`.""",
            "starter": "def recherche_binaire(liste, cible):\n    ...\n",
            "check": "assert recherche_binaire([1, 3, 5, 7, 9], 7) == 3\n"
                     "assert recherche_binaire([1, 3, 5, 7, 9], 1) == 0\n"
                     "assert recherche_binaire([1, 3, 5, 7, 9], 8) == -1\n"
                     "assert recherche_binaire([], 1) == -1\n",
            "solution": "def recherche_binaire(liste, cible):\n"
                        "    bas, haut = 0, len(liste) - 1\n"
                        "    while bas <= haut:\n        milieu = (bas + haut) // 2\n"
                        "        if liste[milieu] == cible:\n            return milieu\n"
                        "        elif liste[milieu] < cible:\n            bas = milieu + 1\n"
                        "        else:\n            haut = milieu - 1\n    return -1\n",
            "hints": ["Garde deux bornes bas et haut.",
                      "Compare l'élément du milieu à la cible et resserre la bonne moitié.",
                      "milieu = (bas + haut) // 2"],
        },
        {
            "id": "alg-03",
            "title": "Le tri à bulles",
            "content": """## Trier soi-même

`sorted()` existe, mais comprendre **comment** on trie est essentiel. Le
tri à bulles compare les éléments voisins et les échange si besoin, en
répétant jusqu'à ce que tout soit en ordre.

```
def tri_bulles(liste):
    l = list(liste)            # copie, pour ne pas modifier l'original
    n = len(l)
    for i in range(n):
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l
```

## À toi

Implémente `tri_bulles(liste)` qui renvoie une **nouvelle** liste triée
par ordre croissant (sans utiliser sorted()).""",
            "starter": "def tri_bulles(liste):\n    ...\n",
            "check": "assert tri_bulles([3, 1, 2]) == [1, 2, 3]\n"
                     "assert tri_bulles([]) == []\n"
                     "assert tri_bulles([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]\n"
                     "src = [2, 1]\ntri_bulles(src)\nassert src == [2, 1]  # original intact\n",
            "solution": "def tri_bulles(liste):\n    l = list(liste)\n    n = len(l)\n"
                        "    for i in range(n):\n        for j in range(n - 1 - i):\n"
                        "            if l[j] > l[j + 1]:\n"
                        "                l[j], l[j + 1] = l[j + 1], l[j]\n    return l\n",
            "hints": ["Travaille sur une copie : l = list(liste).",
                      "Deux boucles imbriquées ; échange les voisins mal ordonnés.",
                      "Échange Python : a, b = b, a"],
        },
        {
            "id": "alg-04",
            "title": "Récursivité : la factorielle",
            "content": """## Une fonction qui s'appelle elle-même

Une fonction **récursive** se définit en fonction d'elle-même, avec un
**cas de base** qui arrête la descente.

```
def factorielle(n):
    if n <= 1:        # cas de base
        return 1
    return n * factorielle(n - 1)   # cas récursif
```

`factorielle(4)` = 4 × 3 × 2 × 1 = 24.

## À toi

Écris `factorielle(n)` de façon **récursive** (n est un entier ≥ 0).""",
            "starter": "def factorielle(n):\n    ...\n",
            "check": "assert factorielle(0) == 1\nassert factorielle(1) == 1\n"
                     "assert factorielle(5) == 120\nassert factorielle(6) == 720\n",
            "solution": "def factorielle(n):\n    if n <= 1:\n        return 1\n"
                        "    return n * factorielle(n - 1)\n",
            "hints": ["Cas de base : n <= 1 renvoie 1.",
                      "Cas récursif : n * factorielle(n - 1)."],
        },
        {
            "id": "alg-05",
            "title": "Récursivité : Fibonacci",
            "content": """## La suite de Fibonacci

Chaque terme est la somme des deux précédents : 0, 1, 1, 2, 3, 5, 8, 13…
Deux cas de base (`fib(0) = 0`, `fib(1) = 1`), puis la règle récursive.

```
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

## À toi

Écris `fib(n)` qui renvoie le n-ième terme (`fib(0) = 0`, `fib(1) = 1`).""",
            "starter": "def fib(n):\n    ...\n",
            "check": "assert fib(0) == 0\nassert fib(1) == 1\nassert fib(7) == 13\n"
                     "assert fib(10) == 55\n",
            "solution": "def fib(n):\n    if n < 2:\n        return n\n"
                        "    return fib(n - 1) + fib(n - 2)\n",
            "hints": ["Deux cas de base : fib(0)=0 et fib(1)=1 (donc return n si n<2).",
                      "Sinon : fib(n-1) + fib(n-2)."],
        },
        {
            "id": "alg-06",
            "title": "La pile (LIFO)",
            "content": """## Dernier arrivé, premier servi

Une **pile** (stack) fonctionne comme une pile d'assiettes : on ajoute
et on retire par le haut. Dernier entré, premier sorti (LIFO). On
l'implémente facilement avec une liste.

```
class Pile:
    def __init__(self):
        self.elements = []
    def empiler(self, x):
        self.elements.append(x)
    def depiler(self):
        return self.elements.pop()
    def est_vide(self):
        return len(self.elements) == 0
```

## À toi

Écris la classe `Pile` avec `empiler(x)`, `depiler()` (renvoie et retire
le sommet) et `est_vide()`.""",
            "starter": "class Pile:\n    def __init__(self):\n        ...\n",
            "check": "p = Pile()\nassert p.est_vide() is True\n"
                     "p.empiler(1)\np.empiler(2)\nassert p.est_vide() is False\n"
                     "assert p.depiler() == 2\nassert p.depiler() == 1\n"
                     "assert p.est_vide() is True\n",
            "solution": "class Pile:\n    def __init__(self):\n        self.elements = []\n"
                        "    def empiler(self, x):\n        self.elements.append(x)\n"
                        "    def depiler(self):\n        return self.elements.pop()\n"
                        "    def est_vide(self):\n        return len(self.elements) == 0\n",
            "hints": ["Stocke les éléments dans une liste self.elements.",
                      "empiler = append ; depiler = pop() (retire le dernier)."],
        },
        {
            "id": "alg-07",
            "title": "La file (FIFO)",
            "content": """## Premier arrivé, premier servi

Une **file** (queue) fonctionne comme une file d'attente : on ajoute à
la fin, on retire au début. Premier entré, premier sorti (FIFO).

```
from collections import deque   # deque est plus efficace pour une file

class File:
    def __init__(self):
        self.elements = []
    def enfiler(self, x):
        self.elements.append(x)
    def defiler(self):
        return self.elements.pop(0)
    def est_vide(self):
        return not self.elements
```

## À toi

Écris la classe `File` avec `enfiler(x)`, `defiler()` (renvoie et retire
le **premier**) et `est_vide()`.""",
            "starter": "class File:\n    def __init__(self):\n        ...\n",
            "check": "f = File()\nassert f.est_vide() is True\n"
                     "f.enfiler('a')\nf.enfiler('b')\nf.enfiler('c')\n"
                     "assert f.defiler() == 'a'\nassert f.defiler() == 'b'\n"
                     "assert f.est_vide() is False\nassert f.defiler() == 'c'\n"
                     "assert f.est_vide() is True\n",
            "solution": "class File:\n    def __init__(self):\n        self.elements = []\n"
                        "    def enfiler(self, x):\n        self.elements.append(x)\n"
                        "    def defiler(self):\n        return self.elements.pop(0)\n"
                        "    def est_vide(self):\n        return not self.elements\n",
            "hints": ["enfiler = append (à la fin).",
                      "defiler = pop(0) (retire le premier élément)."],
        },
    ],
}
