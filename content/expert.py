"""Niveau 4 — Expert."""

LEVEL = {
    "id": "expert",
    "title": "4 · Expert",
    "lessons": [
        {
            "id": "exp-01",
            "title": "Gestionnaires de contexte (with)",
            "content": """## Le protocole `with`

Le mot-clé `with` garantit qu'une ressource est correctement libérée
(fichier fermé, verrou relâché…), même en cas d'erreur. On crée son
propre gestionnaire avec `__enter__` et `__exit__`.

```
class Section:
    def __init__(self, nom):
        self.nom = nom
    def __enter__(self):
        print(f"-> entrée {self.nom}")
        return self
    def __exit__(self, exc_type, exc, tb):
        print(f"<- sortie {self.nom}")
        return False   # ne masque pas les exceptions

with Section("bloc"):
    print("travail en cours")
```

`contextlib.contextmanager` permet d'en écrire un avec un simple
générateur (un `yield` au milieu).

## Exercice

Écris une classe `Capture` : son `__enter__` renvoie une liste vide
stockée dans `self.log`, et la méthode `note(x)` y ajoute `x`.
(Le test vérifie l'usage avec `with`.)""",
            "starter": "class Capture:\n    def __enter__(self):\n        self.log = []\n        return self\n    def __exit__(self, *a):\n        return False\n    # ajoute note(self, x)\n",
            "check": "with Capture() as c:\n    c.note(1)\n    c.note(2)\nassert c.log == [1, 2]\n",
            "solution": "class Capture:\n    def __enter__(self):\n        self.log = []\n        return self\n    def __exit__(self, *a):\n        return False\n    def note(self, x):\n        self.log.append(x)\n",
        },
        {
            "id": "exp-02",
            "title": "Type hints et dataclasses",
            "content": """## Annoter les types

Les annotations documentent les types attendus (sans les imposer à
l'exécution) et alimentent les outils comme mypy ou ton IDE.

```
def addition(a: int, b: int) -> int:
    return a + b

prenoms: list[str] = ["Ada", "Alan"]
```

## Les dataclasses

`@dataclass` génère automatiquement `__init__`, `__repr__`, `__eq__`…
à partir des champs annotés.

```
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)            # Point(x=1, y=2)
print(p == Point(1, 2))  # True
```

## Exercice

Crée une dataclass `Livre` avec les champs `titre: str` et
`pages: int`. Le test compare deux instances identiques.""",
            "starter": "from dataclasses import dataclass\n\n@dataclass\nclass Livre:\n    ...\n",
            "check": 'a = Livre("Roncevaux", 320)\nb = Livre("Roncevaux", 320)\nassert a == b\nassert a.pages == 320\n',
            "solution": "from dataclasses import dataclass\n\n@dataclass\nclass Livre:\n    titre: str\n    pages: int\n",
        },
        {
            "id": "exp-03",
            "title": "Programmation fonctionnelle : functools",
            "content": """## Composer des traitements

`map`, `filter` et le module `functools` favorisent un style
déclaratif.

```
from functools import reduce

nombres = [1, 2, 3, 4]
produit = reduce(lambda acc, x: acc * x, nombres, 1)   # 24
```

`functools.lru_cache` mémorise les résultats d'une fonction coûteuse :

```
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))      # instantané grâce au cache
```

## Exercice

À l'aide de `reduce`, range dans `pgcd_resultat` le PGCD de la liste
`[48, 36, 60]`. Indice : `math.gcd` calcule le PGCD de deux nombres.""",
            "starter": "from functools import reduce\nimport math\nnombres = [48, 36, 60]\npgcd_resultat = ...\n",
            "check": "assert pgcd_resultat == 12\n",
            "solution": "from functools import reduce\nimport math\nnombres = [48, 36, 60]\npgcd_resultat = reduce(math.gcd, nombres)\n",
        },
        {
            "id": "exp-04",
            "title": "Décorateurs paramétrés",
            "content": """## Un décorateur qui prend des arguments

Pour qu'un décorateur accepte des paramètres, on ajoute un niveau
d'emboîtement. `functools.wraps` préserve le nom et la docstring de la
fonction d'origine.

```
import functools

def repeter(n):
    def decorateur(fonction):
        @functools.wraps(fonction)
        def emballage(*args, **kwargs):
            resultat = None
            for _ in range(n):
                resultat = fonction(*args, **kwargs)
            return resultat
        return emballage
    return decorateur

@repeter(3)
def coucou():
    print("hop")

coucou()            # affiche "hop" trois fois
```

## Exercice

Écris un décorateur paramétré `multiplier(facteur)` qui multiplie la
valeur de retour de la fonction par `facteur`.""",
            "starter": "def multiplier(facteur):\n    ...\n\n@multiplier(3)\ndef valeur():\n    return 10\n",
            "check": "assert valeur() == 30\n\n@multiplier(5)\ndef base():\n    return 2\nassert base() == 10\n",
            "solution": "def multiplier(facteur):\n    def deco(fonction):\n        def emballage(*a, **k):\n            return fonction(*a, **k) * facteur\n        return emballage\n    return deco\n\n@multiplier(3)\ndef valeur():\n    return 10\n",
        },
        {
            "id": "exp-05",
            "title": "L'asynchrone : async / await",
            "content": """## Concurrence coopérative

`asyncio` permet d'exécuter plusieurs tâches « en même temps » sur un
seul thread, en libérant la main pendant les attentes (réseau, I/O).
Une fonction `async def` est une coroutine ; `await` suspend jusqu'à ce
qu'un résultat soit prêt.

```
import asyncio

async def tache(nom, delai):
    await asyncio.sleep(delai)
    return f"{nom} terminée"

async def principal():
    resultats = await asyncio.gather(
        tache("A", 0.1),
        tache("B", 0.1),
    )
    return resultats

print(asyncio.run(principal()))
```

Les deux tâches s'exécutent en parallèle logique : le total dure ~0,1 s,
pas 0,2 s.

## Exercice

Complète la coroutine `calcul(x)` pour qu'elle renvoie `x * 10` après
un `await asyncio.sleep(0)`. Le test l'exécute via `asyncio.run`.""",
            "starter": "import asyncio\n\nasync def calcul(x):\n    ...\n",
            "check": "import asyncio\nassert asyncio.run(calcul(4)) == 40\n",
            "solution": "import asyncio\n\nasync def calcul(x):\n    await asyncio.sleep(0)\n    return x * 10\n",
        },
        {
            "id": "exp-06",
            "title": "Idiomes et bonnes pratiques",
            "content": """## Écrire du code « pythonique »

Quelques réflexes qui distinguent un code expert :

Préférer l'itération directe à l'indexation :
```
for fruit in fruits:        # oui
for i in range(len(fruits)): # à éviter
```

`enumerate` quand on a besoin de l'indice ET de la valeur :
```
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

`zip` pour parcourir deux séquences en parallèle :
```
for nom, age in zip(noms, ages):
    ...
```

L'opérateur ternaire, le « truthiness » (`if liste:` plutôt que
`if len(liste) > 0:`), les f-strings, le déballage : autant de marques
de maîtrise. La référence ultime tient en une commande : `import this`.

## Exercice

En une seule ligne avec `zip` et une compréhension de dictionnaire,
construis `assoc` qui associe chaque clé de `cles` à la valeur de même
position dans `valeurs`.""",
            "starter": 'cles = ["a", "b", "c"]\nvaleurs = [1, 2, 3]\nassoc = ...\n',
            "check": 'assert assoc == {"a": 1, "b": 2, "c": 3}\n',
            "solution": 'cles = ["a", "b", "c"]\nvaleurs = [1, 2, 3]\nassoc = {k: v for k, v in zip(cles, valeurs)}\n',
        },
        {
            "id": "exp-07",
            "title": "Duck typing et classes abstraites",
            "content": """## « Si ça cancane comme un canard… »

Python ne vérifie pas le type, mais le **comportement** : peu importe la
classe, du moment que l'objet possède les méthodes attendues. C'est le
*duck typing*.

Pour imposer un contrat (forcer la présence de certaines méthodes), on
utilise une classe de base abstraite (`ABC`) :

```
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        ...

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote
    def aire(self):
        return self.cote ** 2

# Forme() lèverait une TypeError : méthode abstraite non implémentée
```

## Exercice

Crée `Animal` (ABC avec méthode abstraite `cri`) et `Chien` qui
l'implémente en renvoyant `"Ouaf"`. Le test vérifie qu'on ne peut pas
instancier `Animal` directement.""",
            "starter": "from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    ...\n\nclass Chien(Animal):\n    ...\n",
            "check": "assert Chien().cri() == \"Ouaf\"\ntry:\n    Animal()\n    raise SystemExit('Animal ne devrait pas etre instanciable')\nexcept TypeError:\n    pass\n",
            "solution": "from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def cri(self):\n        ...\n\nclass Chien(Animal):\n    def cri(self):\n        return \"Ouaf\"\n",
        },
        {
            "id": "exp-08",
            "title": "Tests unitaires (unittest)",
            "content": """## Vérifier son code automatiquement

Le module `unittest` (intégré) structure les tests en classes. Chaque
méthode `test_*` vérifie un comportement à l'aide d'assertions
(`assertEqual`, `assertTrue`, `assertRaises`…).

```
import unittest

def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_positifs(self):
        self.assertEqual(addition(2, 3), 5)
    def test_negatifs(self):
        self.assertEqual(addition(-1, -1), -2)

# En pratique on lance : python -m unittest
```

Écrire des tests, c'est garantir qu'une modification future ne casse
rien (non-régression).

## Exercice

Écris la fonction `inverse(s)` qui renvoie la chaîne à l'envers.
Une suite `unittest` la validera automatiquement.""",
            "starter": "def inverse(s):\n    ...\n",
            "check": "import unittest\n"
                     "class T(unittest.TestCase):\n"
                     "    def test_a(self):\n        self.assertEqual(inverse('abc'), 'cba')\n"
                     "    def test_vide(self):\n        self.assertEqual(inverse(''), '')\n"
                     "res = unittest.TextTestRunner(verbosity=0).run(\n"
                     "    unittest.TestLoader().loadTestsFromTestCase(T))\n"
                     "assert res.wasSuccessful(), 'des tests ont échoué'\n",
            "solution": "def inverse(s):\n    return s[::-1]\n",
        },
        {
            "id": "exp-09",
            "title": "Exceptions personnalisées et chaînage",
            "content": """## Des erreurs sur mesure

On définit ses propres exceptions en héritant d'`Exception`. Le
chaînage (`raise ... from ...`) conserve la cause d'origine, précieux
pour le débogage.

```
class SoldeInsuffisant(Exception):
    pass

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisant(f"manque {montant - solde} €")
    return solde - montant

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("conversion impossible") from e
```

## Exercice

Définis une exception `AgeInvalide` et une fonction `valider_age(n)`
qui lève cette exception si `n` est négatif, sinon renvoie `n`.""",
            "starter": "class AgeInvalide(Exception):\n    pass\n\ndef valider_age(n):\n    ...\n",
            "check": "assert valider_age(30) == 30\n"
                     "try:\n    valider_age(-5)\n    raise SystemExit('aurait du lever AgeInvalide')\n"
                     "except AgeInvalide:\n    pass\n",
            "solution": "class AgeInvalide(Exception):\n    pass\n\ndef valider_age(n):\n    if n < 0:\n        raise AgeInvalide('âge négatif')\n    return n\n",
        },
        {
            "id": "exp-10",
            "title": "itertools : pipelines de données",
            "content": """## Composer des flux

`itertools` fournit des briques pour enchaîner des traitements de façon
paresseuse (sans tout charger en mémoire).

```
import itertools as it

# Compteur infini, coupé par islice
premiers_pairs = it.islice((n for n in it.count() if n % 2 == 0), 5)
print(list(premiers_pairs))      # [0, 2, 4, 6, 8]

# Regrouper des éléments consécutifs
data = "aaabbbcca"
groupes = [(k, len(list(g))) for k, g in it.groupby(data)]
# [('a', 3), ('b', 3), ('c', 2), ('a', 1)]

# Aplatir une liste de listes
plat = list(it.chain.from_iterable([[1, 2], [3, 4]]))
```

`accumulate`, `product`, `permutations`, `takewhile` complètent la
panoplie.

## Exercice

À l'aide de `itertools.accumulate`, range dans `cumul` la liste des
sommes cumulées de `[1, 2, 3, 4]` (soit `[1, 3, 6, 10]`).""",
            "starter": "import itertools as it\ncumul = ...\n",
            "check": "assert cumul == [1, 3, 6, 10]\n",
            "solution": "import itertools as it\ncumul = list(it.accumulate([1, 2, 3, 4]))\n",
        },
    ],
}
