"""Niveau 3 — Avancé."""

LEVEL = {
    "id": "avance",
    "title": "3 · Avancé",
    "lessons": [
        {
            "id": "adv-01",
            "title": "Les générateurs : yield",
            "content": """## Produire des valeurs à la demande

Un générateur produit ses valeurs une à une, sans tout garder en
mémoire. Le mot-clé `yield` remplace `return` et « met en pause » la
fonction.

```
def compte_a_rebours(n):
    while n > 0:
        yield n
        n -= 1

for x in compte_a_rebours(3):
    print(x)        # 3 2 1
```

C'est idéal pour des flux de données potentiellement infinis ou
volumineux. L'expression génératrice en est la version courte :

```
total = sum(x * x for x in range(1000000))
```

## Exercice

Écris un générateur `pairs(limite)` qui produit les nombres pairs
de 0 (inclus) jusqu'à `limite` (exclu).""",
            "starter": "def pairs(limite):\n    ...\n",
            "check": "assert list(pairs(10)) == [0, 2, 4, 6, 8]\nassert list(pairs(1)) == [0]\n",
            "solution": "def pairs(limite):\n    for n in range(0, limite, 2):\n        yield n\n",
        },
        {
            "id": "adv-02",
            "title": "Programmation orientée objet : les classes",
            "content": """## Définir un objet

Une classe est un moule à objets. `__init__` est le constructeur ;
`self` désigne l'instance courante.

```
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise ValueError("solde insuffisant")
        self.solde -= montant

c = Compte(100)
c.deposer(50)
print(c.solde)      # 150
```

## Exercice

Crée une classe `Chrono` avec un attribut `secondes` initialisé à 0
et une méthode `ajouter(s)` qui l'incrémente de `s`.""",
            "starter": "class Chrono:\n    ...\n",
            "check": "ch = Chrono()\nassert ch.secondes == 0\nch.ajouter(30)\nch.ajouter(15)\nassert ch.secondes == 45\n",
            "solution": "class Chrono:\n    def __init__(self):\n        self.secondes = 0\n\n    def ajouter(self, s):\n        self.secondes += s\n",
        },
        {
            "id": "adv-03",
            "title": "Héritage et polymorphisme",
            "content": """## Réutiliser et spécialiser

Une classe peut hériter d'une autre, récupérer ses méthodes et les
redéfinir. `super()` appelle la version parente.

```
class Animal:
    def __init__(self, nom):
        self.nom = nom
    def cri(self):
        return "..."

class Chien(Animal):
    def cri(self):
        return "Ouaf"

class Chat(Animal):
    def cri(self):
        return "Miaou"

for a in [Chien("Rex"), Chat("Felix")]:
    print(a.nom, ":", a.cri())
```

C'est le polymorphisme : un même appel (`a.cri()`) se comporte
différemment selon le type réel de l'objet.

## Exercice

Crée `Carre` héritant de `Forme`. `Forme` a une méthode `aire()` qui
renvoie 0. `Carre.__init__(self, cote)` stocke `cote` et `aire()`
renvoie l'aire du carré.""",
            "starter": "class Forme:\n    def aire(self):\n        return 0\n\nclass Carre(Forme):\n    ...\n",
            "check": "f = Forme()\nassert f.aire() == 0\nc = Carre(5)\nassert c.aire() == 25\nassert isinstance(c, Forme)\n",
            "solution": "class Forme:\n    def aire(self):\n        return 0\n\nclass Carre(Forme):\n    def __init__(self, cote):\n        self.cote = cote\n    def aire(self):\n        return self.cote ** 2\n",
        },
        {
            "id": "adv-04",
            "title": "Les méthodes spéciales (dunder)",
            "content": """## Rendre ses objets « pythoniques »

Les méthodes entourées de doubles soulignés (`__...__`) permettent à
tes objets de réagir aux opérateurs et fonctions natives.

```
class Vecteur:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)
    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

v = Vecteur(1, 2) + Vecteur(3, 4)
print(v)            # Vecteur(4, 6)
```

Quelques classiques : `__str__`, `__repr__`, `__len__`, `__eq__`,
`__getitem__`.

## Exercice

Ajoute à `Panier` la méthode `__len__` pour que `len(panier)` renvoie
le nombre d'articles stockés dans `self.articles`.""",
            "starter": "class Panier:\n    def __init__(self):\n        self.articles = []\n    def ajouter(self, a):\n        self.articles.append(a)\n    # ... ajoute __len__\n",
            "check": 'p = Panier()\np.ajouter("pain")\np.ajouter("lait")\nassert len(p) == 2\n',
            "solution": "class Panier:\n    def __init__(self):\n        self.articles = []\n    def ajouter(self, a):\n        self.articles.append(a)\n    def __len__(self):\n        return len(self.articles)\n",
        },
        {
            "id": "adv-05",
            "title": "Les décorateurs",
            "content": """## Envelopper une fonction

Un décorateur est une fonction qui prend une fonction et en renvoie une
version « augmentée ». La syntaxe `@` l'applique.

```
def crier(fonction):
    def emballage(*args, **kwargs):
        return fonction(*args, **kwargs).upper()
    return emballage

@crier
def saluer(nom):
    return f"bonjour {nom}"

print(saluer("ada"))    # BONJOUR ADA
```

C'est la mécanique derrière `@property`, `@staticmethod`, ou les routes
d'un framework web.

## Exercice

Écris un décorateur `double` qui multiplie par 2 la valeur renvoyée par
la fonction décorée.""",
            "starter": "def double(fonction):\n    ...\n\n@double\ndef valeur():\n    return 21\n",
            "check": "assert valeur() == 42\n\n@double\ndef somme(a, b):\n    return a + b\nassert somme(3, 4) == 14\n",
            "solution": "def double(fonction):\n    def emballage(*args, **kwargs):\n        return fonction(*args, **kwargs) * 2\n    return emballage\n\n@double\ndef valeur():\n    return 21\n",
        },
        {
            "id": "adv-06",
            "title": "La bibliothèque standard : collections, itertools",
            "content": """## Ne pas réinventer la roue

Python est livré « piles incluses ». Quelques pépites :

```
from collections import Counter, defaultdict

mots = "a b a c b a".split()
print(Counter(mots))          # Counter({'a': 3, 'b': 2, 'c': 1})

groupes = defaultdict(list)
groupes["pairs"].append(2)    # pas besoin d'initialiser la clé
```

```
import itertools as it
print(list(it.combinations([1, 2, 3], 2)))  # [(1,2),(1,3),(2,3)]
```

`Counter` compte, `defaultdict` fournit une valeur par défaut,
`itertools` enchaîne, combine, accumule.

## Exercice

À l'aide de `Counter`, range dans `plus_courant` le caractère le plus
fréquent de la chaîne `"mississippi"` (utilise `.most_common(1)`).""",
            "starter": "from collections import Counter\ntexte = \"mississippi\"\nplus_courant = ...\n",
            "check": 'assert plus_courant == "i" or plus_courant == "s"\n'
                     'from collections import Counter as _C\n'
                     'assert plus_courant == _C("mississippi").most_common(1)[0][0]\n',
            "solution": 'from collections import Counter\ntexte = "mississippi"\nplus_courant = Counter(texte).most_common(1)[0][0]\n',
        },
        {
            "id": "adv-07",
            "title": "@property et encapsulation",
            "content": """## Contrôler l'accès aux attributs

Le décorateur `@property` transforme une méthode en attribut « calculé »,
et permet de valider les affectations via un *setter*.

```
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        if valeur < -273.15:
            raise ValueError("sous le zéro absolu")
        self._celsius = valeur

t = Temperature(25)
print(t.fahrenheit)     # 77.0
t.celsius = 30          # passe par le setter
```

## Exercice

Ajoute à `Cercle` une propriété `aire` (lecture seule) qui renvoie
π·r² (utilise `math.pi`).""",
            "starter": "import math\n\nclass Cercle:\n    def __init__(self, rayon):\n        self.rayon = rayon\n    # ajoute la propriété aire\n",
            "check": "c = Cercle(2)\nimport math\nassert abs(c.aire - math.pi * 4) < 1e-9\n",
            "solution": "import math\n\nclass Cercle:\n    def __init__(self, rayon):\n        self.rayon = rayon\n    @property\n    def aire(self):\n        return math.pi * self.rayon ** 2\n",
        },
        {
            "id": "adv-08",
            "title": "Méthodes de classe et statiques",
            "content": """## Trois types de méthodes

- une **méthode d'instance** reçoit `self` (l'objet) ;
- une **méthode de classe** (`@classmethod`) reçoit `cls` (la classe) :
  pratique pour des constructeurs alternatifs ;
- une **méthode statique** (`@staticmethod`) ne reçoit ni l'un ni
  l'autre : c'est une simple fonction rangée dans la classe.

```
class Date:
    def __init__(self, jour, mois):
        self.jour, self.mois = jour, mois

    @classmethod
    def depuis_chaine(cls, texte):
        j, m = texte.split("/")
        return cls(int(j), int(m))

    @staticmethod
    def est_valide(mois):
        return 1 <= mois <= 12

d = Date.depuis_chaine("14/07")
print(Date.est_valide(13))   # False
```

## Exercice

Ajoute à `Vecteur` une méthode de classe `origine()` qui renvoie un
`Vecteur(0, 0)`.""",
            "starter": "class Vecteur:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    # ajoute origine()\n",
            "check": "o = Vecteur.origine()\nassert o.x == 0 and o.y == 0\nassert isinstance(o, Vecteur)\n",
            "solution": "class Vecteur:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    @classmethod\n    def origine(cls):\n        return cls(0, 0)\n",
        },
        {
            "id": "adv-09",
            "title": "Lire et écrire des fichiers",
            "content": """## Manipuler des fichiers

On ouvre un fichier avec `open()`, idéalement via `with` pour garantir
sa fermeture. Le mode : `"r"` (lecture), `"w"` (écriture, écrase),
`"a"` (ajout).

```
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("ligne 1\\n")
    f.write("ligne 2\\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    # ou : for ligne in f: ...
```

Toujours préciser `encoding="utf-8"` pour éviter les surprises avec les
accents.

## Exercice

Complète `ecrire_lire(chemin, lignes)` : écris chaque élément de
`lignes` sur sa propre ligne dans le fichier, puis relis le fichier et
renvoie la liste des lignes **sans le retour à la ligne final**.""",
            "starter": "def ecrire_lire(chemin, lignes):\n    ...\n",
            "check": "import tempfile, os\n"
                     "p = os.path.join(tempfile.mkdtemp(), 'test.txt')\n"
                     "res = ecrire_lire(p, ['a', 'b', 'c'])\n"
                     "assert res == ['a', 'b', 'c'], res\n",
            "solution": "def ecrire_lire(chemin, lignes):\n"
                        "    with open(chemin, 'w', encoding='utf-8') as f:\n"
                        "        for ligne in lignes:\n"
                        "            f.write(ligne + '\\n')\n"
                        "    with open(chemin, 'r', encoding='utf-8') as f:\n"
                        "        return [l.rstrip('\\n') for l in f]\n",
        },
        {
            "id": "adv-10",
            "title": "Les expressions régulières (re)",
            "content": """## Rechercher des motifs

Le module `re` permet de chercher, extraire et remplacer du texte selon
des motifs.

```
import re

texte = "Appelle le 06 12 34 56 78 ou le 05 99 88 77 66"
nombres = re.findall(r"\\d+", texte)   # ['06', '12', ...]

if re.search(r"\\d{2}", texte):
    print("contient au moins 2 chiffres")

propre = re.sub(r"\\s+", " ", "trop   d'  espaces")
```

Motifs courants : `\\d` chiffre, `\\w` caractère de mot, `\\s` espace,
`+` une ou plusieurs fois, `*` zéro ou plus, `{n}` exactement n fois.

## Exercice

À l'aide de `re.findall`, extrais tous les nombres entiers de la chaîne
`"il y a 3 chats, 12 chiens et 1 lapin"` sous forme de liste d'entiers
dans `nombres`.""",
            "starter": 'import re\ntexte = "il y a 3 chats, 12 chiens et 1 lapin"\nnombres = ...\n',
            "check": "assert nombres == [3, 12, 1]\n",
            "solution": 'import re\ntexte = "il y a 3 chats, 12 chiens et 1 lapin"\n'
                        'nombres = [int(n) for n in re.findall(r"\\d+", texte)]\n',
        },
    ],
}
