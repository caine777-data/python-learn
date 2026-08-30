"""Parcours 18 — Mathématiques, Sciences & Simulations."""

LEVEL = {
    "id": "maths_sciences",
    "title": "18 · Mathématiques, Sciences & Simulations",
    "lessons": [
        {
            "id": "mat-01",
            "title": "Nombres premiers & Crible d'Ératosthène",
            "content": """## Le crible d'Ératosthène

Un nombre premier est un entier supérieur à 1 divisible uniquement par 1 et par
lui-même. Pour trouver tous les nombres premiers jusqu'à `n`, le crible
d'Ératosthène élimine successivement les multiples de chaque nombre premier
découvert :

```python
def premiers(n):
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False
    for p in range(2, int(n**0.5) + 1):
        if est_premier[p]:
            for multiple in range(p * p, n + 1, p):
                est_premier[multiple] = False
    return [i for i, p in enumerate(est_premier) if p]
```

## À toi

Écris `premiers_jusqua(n)` qui renvoie la liste ordonnée de tous les nombres
premiers inférieurs ou égaux à `n`.""",
            "starter": "def premiers_jusqua(n):\n    ...\n",
            "check": "assert premiers_jusqua(10) == [2, 3, 5, 7]\n"
                     "assert premiers_jusqua(20) == [2, 3, 5, 7, 11, 13, 17, 19]\n"
                     "assert premiers_jusqua(1) == []\n",
            "solution": "def premiers_jusqua(n):\n"
                        "    if n < 2:\n        return []\n"
                        "    est_p = [True] * (n + 1)\n"
                        "    est_p[0] = est_p[1] = False\n"
                        "    for p in range(2, int(n**0.5) + 1):\n"
                        "        if est_p[p]:\n"
                        "            for m in range(p * p, n + 1, p):\n"
                        "                est_p[m] = False\n"
                        "    return [i for i, p in enumerate(est_p) if p]\n",
            "hints": [
                "Crée une liste de booléens de taille n + 1 initialisée à True.",
                "Mets les indices 0 et 1 à False, puis marque les multiples à False."
            ],
        },
        {
            "id": "mat-02",
            "title": "Précision exacte avec Decimal et Fraction",
            "content": """## Le problème des nombres flottants

En informatique binaire, certains nombres décimaux simples ne peuvent pas être
représentés exactement (ex: `0.1 + 0.2` donne `0.30000000000000004`).

Pour les calculs financiers et scientifiques de haute précision, Python
propose les modules `decimal` et `fractions` :

```python
from decimal import Decimal
from fractions import Fraction

# Précision financière exacte (passer les nombres en chaînes de caractères !)
prix = Decimal("0.1") + Decimal("0.2")  # Decimal('0.3')

# Calcul fractionnaire exact sans perte
f = Fraction(1, 3) + Fraction(1, 6)     # Fraction(1, 2)
```

## À toi

Écris `calculer_total_facture(prix_lignes: list[str], taux_tva: str) -> Decimal`
qui additionne les prix (fournis sous forme de chaînes de caractères `Decimal`),
applique le taux de TVA (ex: `"0.20"` pour 20%), et renvoie le montant total TTC
sous forme d'un objet `Decimal`.""",
            "starter": "from decimal import Decimal\n\ndef calculer_total_facture(prix_lignes: list[str], taux_tva: str) -> Decimal:\n    ...\n",
            "check": "total = calculer_total_facture(['10.50', '20.00', '9.50'], '0.20')\n"
                     "assert total == Decimal('48.00')\n"
                     "assert isinstance(total, Decimal)\n",
            "solution": "from decimal import Decimal\n\ndef calculer_total_facture(prix_lignes: list[str], taux_tva: str) -> Decimal:\n"
                        "    ht = sum(Decimal(p) for p in prix_lignes)\n"
                        "    tva = Decimal(taux_tva)\n"
                        "    return ht * (Decimal('1') + tva)\n",
            "hints": [
                "Convertis chaque montant avec Decimal(p).",
                "Total TTC = HT * (1 + TVA)."
            ],
        },
        {
            "id": "mat-03",
            "title": "Simulation de Monte-Carlo (Calcul de Pi)",
            "content": r"""## Estimer Pi par le hasard

Imaginez un quart de cercle de rayon 1 inscrit dans un carré de côté 1.
L'aire du carré vaut 1, celle du quart de cercle vaut \(\pi / 4\).

Si l'on tire aléatoirement \(N\) points \((x, y)\) dans le carré, la proportion
de points tombant dans le quart de cercle (\(x^2 + y^2 \le 1\)) se rapproche de
\(\pi / 4\). D'où : \(\pi \approx 4 \times \frac{\text{points dans le cercle}}{\text{points totaux}}\).

## À toi

Écris `estimer_pi(points: list[tuple[float, float]]) -> float` qui prend une
liste de coordonnées \((x, y)\) toutes comprises entre 0 et 1, compte celles
vérifiant \(x^2 + y^2 \le 1.0\), et renvoie l'estimation \(4 \times \frac{\text{dans}}{\text{total}}\).
Si la liste est vide, renvoie `0.0`.""",
            "starter": "def estimer_pi(points: list[tuple[float, float]]) -> float:\n    ...\n",
            "check": "pts = [(0.2, 0.3), (0.5, 0.5), (0.9, 0.9), (0.1, 0.8)]\n"
                     "# (0.2^2 + 0.3^2 = 0.13 <= 1), (0.5^2+0.5^2=0.5<=1), (0.9^2+0.9^2=1.62>1), (0.1^2+0.8^2=0.65<=1)\n"
                     "# 3 dans le cercle sur 4 -> 4 * (3/4) = 3.0\n"
                     "assert estimer_pi(pts) == 3.0\n"
                     "assert estimer_pi([]) == 0.0\n",
            "solution": "def estimer_pi(points: list[tuple[float, float]]) -> float:\n"
                        "    if not points:\n        return 0.0\n"
                        "    dans = sum(1 for x, y in points if x*x + y*y <= 1.0)\n"
                        "    return 4.0 * dans / len(points)\n",
            "hints": [
                "Vérifie la condition x*x + y*y <= 1.0 pour chaque point (x, y).",
                "Renvoie 4.0 * dans / len(points)."
            ],
        },
        {
            "id": "mat-04",
            "title": "Calcul vectoriel & Produit scalaire",
            "content": r"""## Les vecteurs en géométrie et en physique

Un vecteur \(\vec{u} = (x_1, y_1)\) et un vecteur \(\vec{v} = (x_2, y_2)\) ont
pour produit scalaire :
\[ \vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 \]

La norme (longueur) d'un vecteur vaut \(\|\vec{u}\| = \sqrt{x_1^2 + y_1^2}\).

Deux vecteurs non nuls sont **orthogonaux** (perpendiculaires) si et seulement
si leur produit scalaire est nul (\(\vec{u} \cdot \vec{v} = 0\)).

## À toi

Écris deux fonctions :
1. `produit_scalaire(u, v) -> float` : calcule la somme des produits \(u_i \times v_i\).
2. `sont_orthogonaux(u, v) -> bool` : renvoie `True` si le produit scalaire est nul (avec une tolérance de `1e-9`).""",
            "starter": "def produit_scalaire(u: tuple, v: tuple) -> float:\n    ...\n\ndef sont_orthogonaux(u: tuple, v: tuple) -> bool:\n    ...\n",
            "check": "assert produit_scalaire((1, 2), (3, 4)) == 11\n"
                     "assert produit_scalaire((1, 0), (0, 1)) == 0\n"
                     "assert sont_orthogonaux((1, 0), (0, 1)) is True\n"
                     "assert sont_orthogonaux((1, 2), (3, 4)) is False\n",
            "solution": "def produit_scalaire(u: tuple, v: tuple) -> float:\n"
                        "    return sum(a * b for a, b in zip(u, v))\n\n"
                        "def sont_orthogonaux(u: tuple, v: tuple) -> bool:\n"
                        "    return abs(produit_scalaire(u, v)) < 1e-9\n",
            "hints": [
                "Utilise zip(u, v) pour associer les coordonnées composante par composante.",
                "Le produit scalaire est sum(a * b for a, b in zip(u, v))."
            ],
        },
        {
            "id": "mat-05",
            "title": "Résolution d'équations par dichotomie",
            "content": r"""## Trouver la racine d'une fonction f(x) = 0

Le théorème des valeurs intermédiaires garantit que si une fonction continue
\(f\) change de signe sur un intervalle \([a, b]\) (c'est-à-dire \(f(a) \times f(b) \le 0\)),
alors il existe au moins une racine \(c\) telle que \(f(c) = 0\).

La méthode de dichotomie coupe l'intervalle en deux à chaque étape au milieu
\(m = (a + b) / 2\) et resserre l'étau jusqu'à atteindre la précision voulue.

## À toi

Écris `resoudre_dichotomie(f, a, b, precision=1e-5)` qui renvoie la valeur
approchée de \(x\) telle que \(f(x) \approx 0\).""",
            "starter": "def resoudre_dichotomie(f, a, b, precision=1e-5) -> float:\n    ...\n",
            "check": "f = lambda x: x**2 - 2  # racine = sqrt(2) ~ 1.414213\n"
                     "r = resoudre_dichotomie(f, 0.0, 2.0, 1e-5)\n"
                     "assert abs(r - 1.414213) < 1e-4\n",
            "solution": "def resoudre_dichotomie(f, a, b, precision=1e-5) -> float:\n"
                        "    while (b - a) > precision:\n"
                        "        m = (a + b) / 2.0\n"
                        "        if f(a) * f(m) <= 0:\n"
                        "            b = m\n"
                        "        else:\n"
                        "            a = m\n"
                        "    return (a + b) / 2.0\n",
            "hints": [
                "Tant que (b - a) > precision, calcule le milieu m = (a + b) / 2.",
                "Si f(a) * f(m) <= 0, la racine est dans [a, m] donc b = m, sinon a = m."
            ],
        },
        {
            "id": "mat-06",
            "title": "Suite de Syracuse (Conjecture de Collatz)",
            "content": r"""## La conjecture 3n + 1

Pour tout entier positif \(n\) :
- S'il est pair, on le divise par 2 (\(n / 2\)).
- S'il est impair, on le multiplie par 3 et on ajoute 1 (\(3n + 1\)).

La célèbre conjecture affirme qu'en répétant ce processus, on finit toujours
par atteindre le chiffre 1.

Exemple pour 6 : 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (longueur du vol = 9 étapes).

## À toi

Écris `vol_syracuse(n: int) -> list[int]` qui renvoie la suite complète des
nombres visités en partant de `n` jusqu'à atteindre 1 inclus.""",
            "starter": "def vol_syracuse(n: int) -> list[int]:\n    ...\n",
            "check": "assert vol_syracuse(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]\n"
                     "assert vol_syracuse(1) == [1]\n"
                     "assert vol_syracuse(4) == [4, 2, 1]\n",
            "solution": "def vol_syracuse(n: int) -> list[int]:\n"
                        "    res = [n]\n"
                        "    while n > 1:\n"
                        "        n = n // 2 if n % 2 == 0 else 3 * n + 1\n"
                        "        res.append(n)\n"
                        "    return res\n",
            "hints": [
                "Commence avec une liste [n].",
                "Dans une boucle while n > 1, calcule le terme suivant et ajoute-le."
            ],
        },
        {
            "id": "qz-mat",
            "type": "quiz",
            "title": "Quiz — Mathématiques & Sciences",
            "question": "Quelle est la cause de l'erreur `0.1 + 0.2 != 0.3` avec les types `float` classiques en Python ?",
            "options": [
                "Un bogue connu du compilateur CPython.",
                "L'impossibilité de représenter certaines fractions décimales de manière finie en base 2 (IEEE 754).",
                "Le fait que Python arrondit toujours vers le bas par défaut.",
                "La limitation de la mémoire RAM du processeur."
            ],
            "answer": 1,
            "explanation": "Les ordinateurs représentent les nombres flottants en binaire (base 2). Tout comme 1/3 n'a pas d'écriture décimale finie en base 10 (0.333...), 1/10 n'a pas d'écriture binaire finie en base 2."
        }
    ]
}
