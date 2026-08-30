"""Parcours 20 — Intelligence Artificielle (de zéro)."""

LEVEL = {
    "id": "ia_ml",
    "title": "20 · Intelligence Artificielle (de zéro)",
    "lessons": [
        {
            "id": "ia-01",
            "title": "Les k plus proches voisins (k-NN)",
            "content": r"""## Classifier par la proximité

L'algorithme **k-NN** (k-Nearest Neighbors) est l'un des algorithmes d'apprentissage
supervisé les plus intuitifs : pour prédire la catégorie d'un nouvel élément, on
trouve les `k` éléments connus les plus proches géométriquement et on prend la
catégorie majoritaire.

La distance euclidienne entre \((x_1, y_1)\) et \((x_2, y_2)\) vaut :
\[ d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} \]

## À toi

Écris `knn_classifier(points_connus: list[tuple[float, float, str]], point_cible: tuple[float, float], k=3) -> str`
où chaque point connu est `(x, y, etiquette)`. La fonction calcule les distances,
garde les `k` plus proches et renvoie l'étiquette la plus fréquente (en cas d'égalité,
celle apparue en premier parmi les plus proches).""",
            "starter": "from collections import Counter\n\ndef knn_classifier(points_connus: list[tuple[float, float, str]], point_cible: tuple[float, float], k=3) -> str:\n    ...\n",
            "check": "donnees = [\n"
                     "    (1.0, 1.0, 'rouge'),\n"
                     "    (1.2, 0.9, 'rouge'),\n"
                     "    (5.0, 5.0, 'bleu'),\n"
                     "    (5.2, 4.8, 'bleu'),\n"
                     "]\n"
                     "assert knn_classifier(donnees, (1.1, 1.0), k=2) == 'rouge'\n"
                     "assert knn_classifier(donnees, (5.1, 4.9), k=2) == 'bleu'\n",
            "solution": "from collections import Counter\n\ndef knn_classifier(points_connus: list[tuple[float, float, str]], point_cible: tuple[float, float], k=3) -> str:\n"
                        "    xt, yt = point_cible\n"
                        "    distances = []\n"
                        "    for x, y, label in points_connus:\n"
                        "        d = ((x - xt)**2 + (y - yt)**2)**0.5\n"
                        "        distances.append((d, label))\n"
                        "    distances.sort(key=lambda item: item[0])\n"
                        "    k_voisins = [label for _, label in distances[:k]]\n"
                        "    return Counter(k_voisins).most_common(1)[0][0]\n",
            "hints": [
                "Calcule pour chaque point la distance ((x - xt)**2 + (y - yt)**2)**0.5.",
                "Trie par distance croissante, prends les k premiers labels, puis utilise Counter(k_voisins).most_common(1)[0][0]."
            ],
        },
        {
            "id": "ia-02",
            "title": "Régression linéaire par les moindres carrés",
            "content": r"""## Trouver la droite de tendance y = ax + b

La régression linéaire permet de prédire une valeur continue (ex: le prix d'un
logement selon sa surface). La méthode des moindres carrés calcule la pente \(a\)
et l'ordonnée à l'origine \(b\) :
\[ a = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} \]
\[ b = \bar{y} - a \bar{x} \]
où \(\bar{x}\) et \(\bar{y}\) sont les moyennes de \(x\) et de \(y\).

## À toi

Écris `regression_lineaire(points: list[tuple[float, float]]) -> tuple[float, float]`
qui calcule et renvoie `(a, b)` sous forme d'un couple de flottants.""",
            "starter": "def regression_lineaire(points: list[tuple[float, float]]) -> tuple[float, float]:\n    ...\n",
            "check": "pts = [(1.0, 2.0), (2.0, 4.0), (3.0, 6.0)]  # y = 2x + 0\n"
                     "a, b = regression_lineaire(pts)\n"
                     "assert abs(a - 2.0) < 1e-5\n"
                     "assert abs(b - 0.0) < 1e-5\n",
            "solution": "def regression_lineaire(points: list[tuple[float, float]]) -> tuple[float, float]:\n"
                        "    n = len(points)\n"
                        "    x_bar = sum(x for x, y in points) / n\n"
                        "    y_bar = sum(y for x, y in points) / n\n"
                        "    num = sum((x - x_bar) * (y - y_bar) for x, y in points)\n"
                        "    den = sum((x - x_bar)**2 for x, y in points)\n"
                        "    a = num / den if den != 0 else 0.0\n"
                        "    b = y_bar - a * x_bar\n"
                        "    return a, b\n",
            "hints": [
                "Calcule d'abord x_bar et y_bar.",
                "Calcule le numérateur num = sum((x - x_bar) * (y - y_bar)) et le dénominateur den = sum((x - x_bar)**2)."
            ],
        },
        {
            "id": "ia-03",
            "title": "Arbre de décision logique",
            "content": """## Les règles de branchement

Un arbre de décision classe des données en posant une suite de questions
successives sous forme de conditions logiques (if / else).

Exemple pour accorder un prêt bancaire :
1. Si les revenus sont inférieurs à 1500€ → `"refus"`
2. Sinon, si le demandeur a des dettes actives et un apport < 5000€ → `"refus"`
3. Dans tous les autres cas → `"accord"`

## À toi

Écris `evaluer_pret(revenu: float, apport: float, a_dettes: bool) -> str`
qui applique exactement ces règles et renvoie `"accord"` ou `"refus"`.""",
            "starter": "def evaluer_pret(revenu: float, apport: float, a_dettes: bool) -> str:\n    ...\n",
            "check": "assert evaluer_pret(1200, 10000, False) == 'refus'\n"
                     "assert evaluer_pret(2500, 2000, True) == 'refus'\n"
                     "assert evaluer_pret(2500, 8000, True) == 'accord'\n"
                     "assert evaluer_pret(3000, 0, False) == 'accord'\n",
            "solution": "def evaluer_pret(revenu: float, apport: float, a_dettes: bool) -> str:\n"
                        "    if revenu < 1500:\n        return 'refus'\n"
                        "    if a_dettes and apport < 5000:\n        return 'refus'\n"
                        "    return 'accord'\n",
            "hints": [
                "Traite d'abord la condition sur le revenu.",
                "Puis la condition combinée a_dettes and apport < 5000."
            ],
        },
        {
            "id": "ia-04",
            "title": "Le Perceptron (neurone artificiel)",
            "content": r"""## Le bloc de base des réseaux de neurones

Un **perceptron** reçoit un vecteur d'entrées \((x_1, x_2, \dots, x_n)\),
multiplie chaque entrée par un poids associé \((w_1, w_2, \dots, w_n)\),
ajoute un biais \(b\), et applique une fonction d'activation :
\[ z = \sum_{i} x_i w_i + b \]

Si \(z \ge 0\), le neurone s'active et renvoie `1`, sinon il reste inactif et renvoie `0`.

## À toi

Écris `activer_perceptron(entrees: list[float], poids: list[float], biais: float) -> int`
qui calcule la somme pondérée \(z = \sum x_i w_i + b\) et renvoie `1` si \(z \ge 0\)
sinon `0`.""",
            "starter": "def activer_perceptron(entrees: list[float], poids: list[float], biais: float) -> int:\n    ...\n",
            "check": "# Simule la porte logique ET (AND) : poids = [1, 1], biais = -1.5\n"
                     "assert activer_perceptron([0, 0], [1.0, 1.0], -1.5) == 0\n"
                     "assert activer_perceptron([1, 0], [1.0, 1.0], -1.5) == 0\n"
                     "assert activer_perceptron([1, 1], [1.0, 1.0], -1.5) == 1\n",
            "solution": "def activer_perceptron(entrees: list[float], poids: list[float], biais: float) -> int:\n"
                        "    z = sum(x * w for x, w in zip(entrees, poids)) + biais\n"
                        "    return 1 if z >= 0 else 0\n",
            "hints": [
                "Utilise zip(entrees, poids) pour calculer sum(x * w).",
                "Ajoute le biais et renvoie 1 si z >= 0 sinon 0."
            ],
        },
        {
            "id": "ia-05",
            "title": "Analyse de sentiments textuelle",
            "content": """## Classifier le ton d'un message

L'analyse de sentiment lexicale (par dictionnaire) compte les occurrences de
mots à polarité positive (+1) et négative (-1) dans un texte nettoyé.

Score global = `nb_positifs - nb_negatifs`
- Si score > 0 → `"positif"`
- Si score < 0 → `"negatif"`
- Si score == 0 → `"neutre"`

## À toi

Écris `analyser_sentiment(texte: str, mots_positifs: set, mots_negatifs: set) -> str`
qui découpe `texte` en mots minuscules (en nettoyant la ponctuation basique) et
renvoie `"positif"`, `"negatif"` ou `"neutre"`.""",
            "starter": "import re\n\ndef analyser_sentiment(texte: str, mots_positifs: set, mots_negatifs: set) -> str:\n    ...\n",
            "check": "pos = {'super', 'genial', 'bravo', 'adore', 'bon'}\n"
                     "neg = {'nul', 'mauvais', 'horrible', 'lent', 'bug'}\n"
                     "assert analyser_sentiment('Ce produit est genial et super bon !', pos, neg) == 'positif'\n"
                     "assert analyser_sentiment('Trop nul et plein de bugs...', pos, neg) == 'negatif'\n"
                     "assert analyser_sentiment('Le paquet est arrive mardi.', pos, neg) == 'neutre'\n",
            "solution": "import re\n\ndef analyser_sentiment(texte: str, mots_positifs: set, mots_negatifs: set) -> str:\n"
                        "    mots = re.findall(r'\\w+', texte.lower())\n"
                        "    score = sum(1 for m in mots if m in mots_positifs) - sum(1 for m in mots if m in mots_negatifs)\n"
                        "    if score > 0:\n        return 'positif'\n"
                        "    elif score < 0:\n        return 'negatif'\n"
                        "    return 'neutre'\n",
            "hints": [
                "Utilise re.findall(r'\\w+', texte.lower()) pour extraire les mots propres.",
                "Calcule les scores positifs et négatifs puis compare."
            ],
        },
        {
            "id": "ia-06",
            "title": "Moteur de recommandation (Similarité cosinus)",
            "content": r"""## Comparer les goûts de deux utilisateurs

Pour savoir si deux profils ont des affinités (pour leur recommander des films
ou des livres), on mesure le cosinus de l'angle entre leurs vecteurs de notes :
\[ \text{similarité}(u, v) = \frac{u \cdot v}{\|u\| \times \|v\|} = \frac{\sum u_i v_i}{\sqrt{\sum u_i^2} \times \sqrt{\sum v_i^2}} \]

Un score proche de `1.0` indique des préférences identiques.

## À toi

Écris `similarite_cosinus(u: list[float], v: list[float]) -> float` qui renvoie
la similarité cosinus entre deux vecteurs de même taille (renvoie `0.0` si l'une
des normes est nulle).""",
            "starter": "import math\n\ndef similarite_cosinus(u: list[float], v: list[float]) -> float:\n    ...\n",
            "check": "assert abs(similarite_cosinus([1.0, 1.0], [1.0, 1.0]) - 1.0) < 1e-5\n"
                     "assert abs(similarite_cosinus([1.0, 0.0], [0.0, 1.0]) - 0.0) < 1e-5\n"
                     "assert abs(similarite_cosinus([2.0, 0.0], [4.0, 0.0]) - 1.0) < 1e-5\n",
            "solution": "import math\n\ndef similarite_cosinus(u: list[float], v: list[float]) -> float:\n"
                        "    dot = sum(a * b for a, b in zip(u, v))\n"
                        "    norm_u = math.sqrt(sum(a * a for a in u))\n"
                        "    norm_v = math.sqrt(sum(b * b for b in v))\n"
                        "    if norm_u == 0 or norm_v == 0:\n        return 0.0\n"
                        "    return dot / (norm_u * norm_v)\n",
            "hints": [
                "Calcule le produit scalaire sum(a * b for a, b in zip(u, v)).",
                "Divise par sqrt(sum(a*a)) * sqrt(sum(b*b))."
            ],
        },
        {
            "id": "qz-ia",
            "type": "quiz",
            "title": "Quiz — Intelligence Artificielle",
            "question": "Dans l'algorithme des k plus proches voisins (k-NN), que représente la lettre 'k' ?",
            "options": [
                "Le nombre de dimensions géométriques du problème.",
                "Le nombre de voisins pris en compte pour effectuer le vote majoritaire.",
                "Le taux d'apprentissage de l'algorithme d'optimisation.",
                "Le nombre de neurones de la couche cachée."
            ],
            "answer": 1,
            "explanation": "k désigne le nombre d'éléments les plus proches à consulter pour déterminer la classe ou la valeur prédite."
        }
    ]
}
