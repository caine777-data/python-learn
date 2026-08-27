"""Parcours 5 — Scripts & automatisation."""

LEVEL = {
    "id": "scripts",
    "title": "5 · Scripts & automatisation",
    "lessons": [
        {
            "id": "scr-01",
            "title": "C'est quoi un script ?",
            "content": """## Un programme qu'on lance

Un **script** est simplement un fichier `.py` contenant une suite
d'instructions, qu'on exécute pour accomplir une tâche : renommer des
fichiers, envoyer un rapport, nettoyer un dossier...

On le lance depuis un **terminal** (l'invite de commande) :

```
python mon_script.py
```

Un bon script fait **une chose utile**, automatiquement, sans qu'on ait
à refaire les étapes à la main. C'est tout l'intérêt : on l'écrit une
fois, on le réutilise mille fois.

Un script peut recevoir des **arguments** (des informations passées au
lancement), par exemple un nom de dossier à traiter. On verra ça plus
tard ; pour l'instant, raisonnons avec une fonction.

## À toi

Écris une fonction `resumer(taches)` qui reçoit une liste de tâches
(des chaînes) et renvoie une phrase du type
`3 tâche(s) : ranger, coder, dormir`.""",
            "starter": "def resumer(taches):\n    ...\n",
            "check": 'assert resumer(["ranger", "coder", "dormir"]) == "3 tâche(s) : ranger, coder, dormir"\n'
                     'assert resumer(["test"]) == "1 tâche(s) : test"\n',
            "solution": 'def resumer(taches):\n    return f"{len(taches)} tâche(s) : " + ", ".join(taches)\n',
        },
        {
            "id": "scr-02",
            "title": "Les chemins de fichiers avec pathlib",
            "content": """## Manipuler des chemins proprement

Le module `pathlib` représente les chemins de fichiers comme des
objets, et fonctionne pareil sous Windows, macOS et Linux.

```
from pathlib import Path

chemin = Path("dossier") / "photo.png"   # on assemble avec /
print(chemin.name)      # photo.png      (le nom du fichier)
print(chemin.stem)      # photo          (sans l'extension)
print(chemin.suffix)    # .png           (l'extension)
print(chemin.parent)    # dossier        (le dossier parent)
```

Quelques actions courantes :

```
Path("rapport.txt").exists()     # True / False : le fichier existe ?
Path("mon_dossier").mkdir()      # crée un dossier
```

`pathlib` évite les erreurs de séparateurs (`/` vs `\\`) entre systèmes.

## À toi

Écris une fonction `extension(nom_fichier)` qui renvoie l'extension du
fichier (en minuscules, **sans le point**). Exemple :
`"Rapport.PDF"` → `"pdf"`.""",
            "starter": "from pathlib import Path\n\ndef extension(nom_fichier):\n    ...\n",
            "check": 'assert extension("Rapport.PDF") == "pdf"\n'
                     'assert extension("photo.JPG") == "jpg"\n'
                     'assert extension("archive.tar.gz") == "gz"\n',
            "solution": "from pathlib import Path\n\ndef extension(nom_fichier):\n"
                        "    return Path(nom_fichier).suffix.lstrip('.').lower()\n",
        },
        {
            "id": "scr-03",
            "title": "Lire et écrire des fichiers",
            "content": """## Sauvegarder des données

Pour écrire dans un fichier, on l'ouvre en mode `"w"` (write). Le bloc
`with` garantit que le fichier sera bien refermé.

```
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\\n")
    f.write("Deuxième ligne\\n")
```

Pour relire :

```
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())   # .strip() enlève le retour à la ligne
```

Précise toujours `encoding="utf-8"` pour gérer correctement les accents.

## À toi

Écris deux fonctions :
- `sauver(chemin, lignes)` : écrit chaque élément de `lignes` sur sa
  propre ligne dans le fichier ;
- `charger(chemin)` : relit le fichier et renvoie la liste des lignes
  **sans** les retours à la ligne.""",
            "starter": "def sauver(chemin, lignes):\n    ...\n\ndef charger(chemin):\n    ...\n",
            "check": "import tempfile, os\n"
                     "p = os.path.join(tempfile.mkdtemp(), 'data.txt')\n"
                     "sauver(p, ['un', 'deux', 'trois'])\n"
                     "assert charger(p) == ['un', 'deux', 'trois']\n",
            "solution": "def sauver(chemin, lignes):\n"
                        "    with open(chemin, 'w', encoding='utf-8') as f:\n"
                        "        for ligne in lignes:\n            f.write(ligne + '\\n')\n\n"
                        "def charger(chemin):\n"
                        "    with open(chemin, 'r', encoding='utf-8') as f:\n"
                        "        return [l.rstrip('\\n') for l in f]\n",
        },
        {
            "id": "scr-04",
            "title": "Le format JSON",
            "content": """## Échanger des données structurées

**JSON** est le format le plus répandu pour stocker et échanger des
données (configurations, réponses d'API web...). Il ressemble beaucoup
aux dictionnaires Python.

Le module `json` fait la traduction dans les deux sens :

```
import json

donnees = {"nom": "Ada", "langages": ["Python", "C"]}

# Python -> texte JSON
texte = json.dumps(donnees)

# texte JSON -> Python
retour = json.loads(texte)
print(retour["nom"])        # Ada
```

Pour lire/écrire directement un fichier `.json`, on utilise
`json.dump(obj, fichier)` et `json.load(fichier)`.

## À toi

On te donne une chaîne JSON dans `texte`. Décode-la et range dans
`ville` la valeur associée à la clé `"ville"`.""",
            "starter": 'import json\ntexte = \'{"nom": "Cédric", "ville": "Le Fauga"}\'\nville = ...\n',
            "check": 'assert ville == "Le Fauga"\n',
            "solution": 'import json\ntexte = \'{"nom": "Cédric", "ville": "Le Fauga"}\'\n'
                        'ville = json.loads(texte)["ville"]\n',
        },
        {
            "id": "scr-05",
            "title": "Lire un fichier CSV",
            "content": """## Les tableaux de données

Un **CSV** (valeurs séparées par des virgules) est le format des
tableurs : chaque ligne est un enregistrement, chaque colonne un champ.
C'est typiquement ce qu'on exporte depuis Excel.

Le module `csv` le lit proprement. `DictReader` donne chaque ligne sous
forme de dictionnaire (clé = nom de colonne) :

```
import csv, io

data = "nom,age\\nAda,36\\nAlan,41\\n"
lecteur = csv.DictReader(io.StringIO(data))
for ligne in lecteur:
    print(ligne["nom"], ligne["age"])
```

(Ici on lit depuis une chaîne via `io.StringIO`; avec un vrai fichier,
on ferait `open("fichier.csv")` à la place.)

## À toi

À partir du CSV fourni dans `data`, calcule la **somme des âges** dans
`total_age` (n'oublie pas : les valeurs lues sont du texte, à convertir
en `int`).""",
            "starter": 'import csv, io\ndata = "nom,age\\nAda,36\\nAlan,41\\nGrace,30\\n"\ntotal_age = ...\n',
            "check": "assert total_age == 107\n",
            "solution": 'import csv, io\ndata = "nom,age\\nAda,36\\nAlan,41\\nGrace,30\\n"\n'
                        'lecteur = csv.DictReader(io.StringIO(data))\n'
                        'total_age = sum(int(ligne["age"]) for ligne in lecteur)\n',
        },
        {
            "id": "scr-06",
            "title": "Dates, heures et planification",
            "content": """## Travailler avec le temps

Le module `datetime` gère dates et heures, indispensable pour des
scripts qui trient par date, calculent des échéances, etc.

```
from datetime import date, datetime, timedelta

aujourdhui = date.today()
print(aujourdhui)                 # 2026-06-26

dans_une_semaine = date.today() + timedelta(days=7)

debut = date(2026, 1, 1)
fin = date(2026, 12, 31)
print((fin - debut).days)         # 364 (différence en jours)
```

`datetime.now()` donne la date **et** l'heure. On formate un affichage
avec `.strftime("%d/%m/%Y")`.

## À toi

Calcule dans `ecart` le **nombre de jours** entre `debut` et `fin`
(un entier).""",
            "starter": "from datetime import date\ndebut = date(2026, 3, 1)\nfin = date(2026, 3, 15)\necart = ...\n",
            "check": "assert ecart == 14\n",
            "solution": "from datetime import date\ndebut = date(2026, 3, 1)\nfin = date(2026, 3, 15)\n"
                        "ecart = (fin - debut).days\n",
        },
    ],
}
