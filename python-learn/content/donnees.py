"""Parcours — Manipuler des données (statistics, collections, CSV)."""

LEVEL = {
    "id": "donnees",
    "title": "12 · Manipuler des données",
    "lessons": [
        {
            "id": "don-01",
            "title": "Statistiques : la moyenne",
            "content": """## Le module statistics

Plutôt que de tout recalculer à la main, le module **statistics** offre
les mesures usuelles : `mean` (moyenne), `median` (médiane), `mode`,
`stdev` (écart-type)…

```
import statistics
print(statistics.mean([10, 20, 30]))   # 20
```

## À toi

Écris `moyenne(valeurs)` qui renvoie la moyenne, en utilisant
`statistics.mean`.""",
            "starter": "import statistics\n\ndef moyenne(valeurs):\n    ...\n",
            "check": "assert moyenne([10, 20, 30]) == 20\n"
                     "assert moyenne([4, 8]) == 6\n"
                     "assert moyenne([5]) == 5\n",
            "solution": "import statistics\n\ndef moyenne(valeurs):\n"
                        "    return statistics.mean(valeurs)\n",
            "hints": ["Appelle statistics.mean(valeurs).",
                      "return statistics.mean(valeurs)"],
        },
        {
            "id": "don-02",
            "title": "Statistiques : la médiane",
            "content": """## Au milieu des données

La **médiane** est la valeur du milieu une fois les données triées :
elle résiste mieux aux valeurs extrêmes que la moyenne.

```
import statistics
print(statistics.median([1, 2, 100]))   # 2
```

## À toi

Écris `mediane(valeurs)` avec `statistics.median`.""",
            "starter": "import statistics\n\ndef mediane(valeurs):\n    ...\n",
            "check": "assert mediane([1, 2, 100]) == 2\n"
                     "assert mediane([3, 1, 2]) == 2\n"
                     "assert mediane([1, 2, 3, 4]) == 2.5\n",
            "solution": "import statistics\n\ndef mediane(valeurs):\n"
                        "    return statistics.median(valeurs)\n",
            "hints": ["Appelle statistics.median(valeurs).",
                      "La fonction trie les données pour toi."],
        },
        {
            "id": "don-03",
            "title": "Compter avec Counter",
            "content": """## Compter en une ligne

`collections.Counter` compte les occurrences automatiquement, et sait
donner les plus fréquentes avec `most_common`.

```
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(1))   # [('a', 5)]
```

## À toi

Écris `mot_le_plus_frequent(texte)` qui renvoie le mot (séparé par des
espaces) le plus fréquent.""",
            "starter": "from collections import Counter\n\ndef mot_le_plus_frequent(texte):\n    ...\n",
            "check": 'assert mot_le_plus_frequent("le chat le chien le") == "le"\n'
                     'assert mot_le_plus_frequent("a b b c b") == "b"\n',
            "solution": "from collections import Counter\n\n"
                        "def mot_le_plus_frequent(texte):\n"
                        "    return Counter(texte.split()).most_common(1)[0][0]\n",
            "hints": ["Découpe le texte en mots avec texte.split().",
                      "Counter(...).most_common(1) renvoie [(mot, nombre)].",
                      "Le mot est à l'indice [0][0]."],
        },
        {
            "id": "don-04",
            "title": "Regrouper avec defaultdict",
            "content": """## Des groupes sans effort

`collections.defaultdict` crée automatiquement une valeur par défaut
quand une clé est absente — idéal pour regrouper.

```
from collections import defaultdict
groupes = defaultdict(list)
for mot in ["ada", "alan", "bob"]:
    groupes[mot[0]].append(mot)
# {'a': ['ada', 'alan'], 'b': ['bob']}
```

## À toi

Écris `grouper_par_initiale(mots)` qui renvoie un **dictionnaire**
(normal) associant chaque initiale à la liste des mots correspondants.""",
            "starter": "from collections import defaultdict\n\n"
                       "def grouper_par_initiale(mots):\n    ...\n",
            "check": "r = grouper_par_initiale(['ada', 'alan', 'bob'])\n"
                     "assert r == {'a': ['ada', 'alan'], 'b': ['bob']}\n"
                     "assert grouper_par_initiale([]) == {}\n",
            "solution": "from collections import defaultdict\n\n"
                        "def grouper_par_initiale(mots):\n"
                        "    groupes = defaultdict(list)\n"
                        "    for mot in mots:\n        groupes[mot[0]].append(mot)\n"
                        "    return dict(groupes)\n",
            "hints": ["defaultdict(list) crée une liste vide pour chaque nouvelle clé.",
                      "La clé est l'initiale mot[0].",
                      "Convertis en dict normal à la fin : dict(groupes)."],
        },
        {
            "id": "don-05",
            "title": "Lire un CSV",
            "content": """## Le format des tableurs

Le **CSV** (valeurs séparées par des virgules) est le format d'échange
de données le plus courant. Le module `csv` le lit pour toi ; avec
`DictReader`, chaque ligne devient un dictionnaire.

```
import csv, io
texte = "nom,age\\nAda,30\\nBob,25\\n"
for ligne in csv.DictReader(io.StringIO(texte)):
    print(ligne["nom"], ligne["age"])
```

(`io.StringIO` fait passer une chaîne pour un fichier.)

## À toi

Écris `lire_csv(texte)` qui renvoie la **liste des lignes** sous forme
de dictionnaires.""",
            "starter": "import csv, io\n\ndef lire_csv(texte):\n    ...\n",
            "check": 'data = lire_csv("nom,age\\nAda,30\\nBob,25\\n")\n'
                     'assert len(data) == 2\n'
                     'assert data[0]["nom"] == "Ada" and data[0]["age"] == "30"\n'
                     'assert data[1]["nom"] == "Bob"\n',
            "solution": "import csv, io\n\ndef lire_csv(texte):\n"
                        "    return list(csv.DictReader(io.StringIO(texte)))\n",
            "hints": ["Enveloppe le texte avec io.StringIO(texte).",
                      "csv.DictReader(...) produit un dict par ligne ; convertis en list."],
        },
        {
            "id": "don-06",
            "title": "Agréger des données",
            "content": """## Synthétiser un tableau

Une fois les données lues, on les **agrège** : totaux par catégorie,
moyennes par groupe… C'est le cœur de l'analyse de données.

On reçoit une liste de lignes (dictionnaires) avec les clés `ville` et
`ventes` (du texte, comme issu d'un CSV).

## À toi

Écris `total_par_ville(lignes)` qui renvoie un dictionnaire
`{ville: total_des_ventes}` (pense à convertir les ventes en entier).""",
            "starter": "def total_par_ville(lignes):\n    ...\n",
            "check": "lignes = [{'ville': 'Lyon', 'ventes': '10'},\n"
                     "          {'ville': 'Paris', 'ventes': '5'},\n"
                     "          {'ville': 'Lyon', 'ventes': '7'}]\n"
                     "assert total_par_ville(lignes) == {'Lyon': 17, 'Paris': 5}\n"
                     "assert total_par_ville([]) == {}\n",
            "solution": "def total_par_ville(lignes):\n    totaux = {}\n"
                        "    for ligne in lignes:\n        ville = ligne['ville']\n"
                        "        totaux[ville] = totaux.get(ville, 0) + int(ligne['ventes'])\n"
                        "    return totaux\n",
            "hints": ["Parcours les lignes et accumule dans un dict.",
                      "totaux.get(ville, 0) donne 0 si la ville n'est pas encore vue.",
                      "Convertis les ventes avec int(...)."],
        },
    ],
}
