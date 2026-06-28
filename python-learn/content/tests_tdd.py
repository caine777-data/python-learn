"""Parcours — Tests & TDD (unittest, écrire et lire des tests)."""

LEVEL = {
    "id": "tests_tdd",
    "title": "13 · Tests & TDD",
    "lessons": [
        {
            "id": "tdd-01",
            "title": "assert : la brique de base",
            "content": """## Vérifier une affirmation

`assert` vérifie qu'une condition est vraie. Si oui, rien ne se passe ;
si non, le programme s'arrête avec une `AssertionError`. C'est la base
de tous les tests.

```
assert 2 + 2 == 4        # ok, rien ne se passe
assert "abc".upper() == "ABC"
```

## À toi

Écris `aire_rectangle(largeur, hauteur)` qui renvoie l'aire. Tes tests
(ci-dessous, invisibles) vérifieront quelques cas.""",
            "starter": "def aire_rectangle(largeur, hauteur):\n    ...\n",
            "check": "assert aire_rectangle(2, 3) == 6\n"
                     "assert aire_rectangle(5, 5) == 25\n"
                     "assert aire_rectangle(0, 9) == 0\n",
            "solution": "def aire_rectangle(largeur, hauteur):\n    return largeur * hauteur\n",
            "hints": ["L'aire d'un rectangle est largeur × hauteur.",
                      "return largeur * hauteur"],
        },
        {
            "id": "tdd-02",
            "title": "Lire un test comme une spécification",
            "content": """## Les tests décrivent ce qu'il faut faire

Avec `unittest`, on regroupe les vérifications dans une classe. Ce test
**spécifie** le comportement attendu de la fonction `prix_ttc` :

```
import unittest

class TestPrix(unittest.TestCase):
    def test_tva_20(self):
        self.assertEqual(prix_ttc(100, 20), 120)
    def test_zero(self):
        self.assertEqual(prix_ttc(0, 20), 0)
```

Pas besoin d'inventer : les tests te disent exactement quoi coder.
`prix_ttc(ht, taux)` ajoute `taux` % au prix hors taxe.

## À toi

Implémente `prix_ttc(ht, taux)` pour satisfaire la spécification.""",
            "starter": "def prix_ttc(ht, taux):\n    ...\n",
            "check": "assert prix_ttc(100, 20) == 120\n"
                     "assert prix_ttc(0, 20) == 0\n"
                     "assert prix_ttc(50, 10) == 55\n",
            "solution": "def prix_ttc(ht, taux):\n    return ht + ht * taux / 100\n",
            "hints": ["Ajouter taux % revient à ajouter ht * taux / 100.",
                      "return ht + ht * taux / 100"],
        },
        {
            "id": "tdd-03",
            "title": "Penser aux cas limites",
            "content": """## Les bords, là où ça casse

Un bon test couvre les cas « normaux » **et** les cas limites : liste
vide, valeur nulle, doublons… `maximum(liste)` doit renvoyer le plus
grand élément, mais que faire si la liste est vide ? Ici : renvoyer
`None`.

## À toi

Écris `maximum(liste)` qui renvoie le plus grand élément, ou `None` si
la liste est vide.""",
            "starter": "def maximum(liste):\n    ...\n",
            "check": "assert maximum([3, 7, 2]) == 7\n"
                     "assert maximum([5]) == 5\n"
                     "assert maximum([]) is None\n"
                     "assert maximum([-1, -9, -3]) == -1\n",
            "solution": "def maximum(liste):\n    if not liste:\n        return None\n"
                        "    return max(liste)\n",
            "hints": ["Traite d'abord le cas de la liste vide : if not liste: return None.",
                      "Sinon, max(liste) fait le travail."],
        },
        {
            "id": "tdd-04",
            "title": "Rouge, vert, refactor",
            "content": """## Le cycle TDD

En **TDD** (développement piloté par les tests), on écrit d'abord le
test (il échoue : *rouge*), puis le code minimal pour le faire passer
(*vert*), puis on améliore (*refactor*). Implémentons `palindrome(mot)` :
vrai si le mot se lit pareil à l'endroit et à l'envers (en ignorant la
casse).

```
class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(palindrome("kayak"))
    def test_casse(self):
        self.assertTrue(palindrome("Radar"))
    def test_non(self):
        self.assertFalse(palindrome("python"))
```

## À toi

Écris `palindrome(mot)` (insensible à la casse).""",
            "starter": "def palindrome(mot):\n    ...\n",
            "check": 'assert palindrome("kayak") is True\n'
                     'assert palindrome("Radar") is True\n'
                     'assert palindrome("python") is False\n'
                     'assert palindrome("") is True\n',
            "solution": "def palindrome(mot):\n    bas = mot.lower()\n"
                        "    return bas == bas[::-1]\n",
            "hints": ["Mets le mot en minuscules avec .lower().",
                      "Un mot inversé s'écrit mot[::-1].",
                      "Compare le mot à son inverse."],
        },
        {
            "id": "tdd-05",
            "title": "Écrire ses propres tests",
            "mode": "trous",
            "content": """## À ton tour de tester

Maintenant, c'est toi qui écris les tests. La fonction `inverser` est
déjà écrite. Complète les `____` avec les **résultats attendus** pour
que toutes les assertions passent (un test juste vérifie une vérité !).

Astuce : `inverser("abc")` renvoie `"cba"`.""",
            "starter": 'def inverser(texte):\n    return texte[::-1]\n\n'
                       '# Complète les résultats attendus :\n'
                       'assert inverser("abc") == ____\n'
                       'assert inverser("") == ____\n'
                       'assert inverser("Python") == ____\n',
            "check": None,
            "solution": 'def inverser(texte):\n    return texte[::-1]\n\n'
                        'assert inverser("abc") == "cba"\n'
                        'assert inverser("") == ""\n'
                        'assert inverser("Python") == "nohtyP"\n',
            "hints": ["inverser renverse la chaîne : \"abc\" → \"cba\".",
                      "Une chaîne vide inversée reste vide : \"\".",
                      "\"Python\" inversé donne \"nohtyP\"."],
        },
    ],
}
