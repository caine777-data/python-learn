"""Parcours 8 — Administrer son PC."""

LEVEL = {
    "id": "admin",
    "title": "8 · Administrer son PC",
    "lessons": [
        {
            "id": "adm-01",
            "title": "Informations système : os, sys, platform",
            "content": """## Connaître la machine

Plusieurs modules intégrés renseignent sur l'environnement :

```
import platform, os, sys

print(platform.system())            # 'Windows', 'Linux' ou 'Darwin' (macOS)
print(platform.python_version())    # '3.12.10'
print(os.getcwd())                  # dossier de travail courant
print(sys.argv)                     # arguments passés au script
```

Le module `subprocess` permet même de **lancer des commandes système**
(comme dans un terminal) depuis Python :

```
import subprocess
resultat = subprocess.run(["ping", "localhost"], capture_output=True, text=True)
print(resultat.stdout)
```

> Note : dans une application empaquetée en `.exe`, `sys.executable`
> désigne l'application elle-même, pas l'interpréteur Python — à garder
> en tête si tu relances Python via `subprocess`.

## À toi

Écris une fonction `infos()` qui renvoie un dictionnaire avec deux clés :
`"systeme"` (le nom du système via `platform.system()`) et `"python"`
(la version via `platform.python_version()`).""",
            "starter": "import platform\n\ndef infos():\n    ...\n",
            "check": "d = infos()\nassert set(d.keys()) == {'systeme', 'python'}\n"
                     "assert isinstance(d['systeme'], str) and len(d['systeme']) > 0\n"
                     "assert d['python'].count('.') == 2\n",
            "solution": "import platform\n\ndef infos():\n"
                        "    return {'systeme': platform.system(),\n"
                        "            'python': platform.python_version()}\n",
        },
        {
            "id": "adm-02",
            "title": "Les variables d'environnement",
            "content": """## Lire la configuration du système

Les **variables d'environnement** stockent des réglages du système et
des utilisateurs : chemins, langue, dossiers personnels, clés secrètes
d'API... On les lit via `os.environ`.

```
import os

# Lecture sûre avec une valeur par défaut si la variable n'existe pas :
utilisateur = os.environ.get("USER") or os.environ.get("USERNAME")
chemin = os.environ.get("PATH", "")
print(utilisateur)
```

Utiliser `.get(nom, defaut)` plutôt que `os.environ[nom]` évite une
erreur si la variable est absente. C'est la bonne pratique, notamment
pour ne pas écrire de mots de passe en dur dans le code (on les met
dans l'environnement).

## À toi

Écris `lire_env(nom, defaut="absente")` qui renvoie la valeur de la
variable d'environnement `nom`, ou `defaut` si elle n'existe pas.""",
            "starter": "import os\n\ndef lire_env(nom, defaut=\"absente\"):\n    ...\n",
            "check": "import os\nos.environ['MA_VAR_TEST'] = 'coucou'\n"
                     "assert lire_env('MA_VAR_TEST') == 'coucou'\n"
                     "assert lire_env('VAR_INEXISTANTE_XYZ', 'rien') == 'rien'\n"
                     "assert lire_env('VAR_INEXISTANTE_XYZ') == 'absente'\n",
            "solution": "import os\n\ndef lire_env(nom, defaut=\"absente\"):\n"
                        "    return os.environ.get(nom, defaut)\n",
        },
        {
            "id": "adm-03",
            "title": "Parcourir des dossiers",
            "content": """## Explorer le disque

`pathlib` permet de lister et filtrer le contenu d'un dossier.

```
from pathlib import Path

dossier = Path(".")
for element in dossier.iterdir():       # tout le contenu
    print(element.name)

# Filtrer par motif :
for image in dossier.glob("*.png"):     # tous les .png
    print(image)

# Récursif (sous-dossiers compris) :
for fichier in dossier.rglob("*.txt"):
    print(fichier)
```

`glob("*.png")` ne garde que les fichiers correspondant au motif. C'est
la base de tout script qui trie, compte ou traite des fichiers en lot.

## À toi

Écris `compter_fichiers(dossier, extension)` qui renvoie le **nombre**
de fichiers d'une extension donnée dans le dossier. Exemple :
`compter_fichiers(chemin, ".txt")`.""",
            "starter": "from pathlib import Path\n\ndef compter_fichiers(dossier, extension):\n    ...\n",
            "check": "import tempfile, pathlib\n"
                     "d = pathlib.Path(tempfile.mkdtemp())\n"
                     "(d / 'a.txt').write_text('x'); (d / 'b.txt').write_text('x')\n"
                     "(d / 'c.log').write_text('x')\n"
                     "assert compter_fichiers(str(d), '.txt') == 2\n"
                     "assert compter_fichiers(str(d), '.log') == 1\n",
            "solution": "from pathlib import Path\n\ndef compter_fichiers(dossier, extension):\n"
                        "    return len(list(Path(dossier).glob(f'*{extension}')))\n",
        },
        {
            "id": "adm-04",
            "title": "Copier, déplacer, supprimer (shutil)",
            "content": """## Agir sur les fichiers

Le module `shutil` complète `pathlib` pour les opérations de fichiers :

```
import shutil

shutil.copy("source.txt", "copie.txt")       # copier
shutil.move("ancien.txt", "dossier/")        # déplacer
shutil.copytree("dossier", "dossier_copie")  # copier un dossier entier
```

Pour supprimer, on utilise `pathlib` ou `os` :

```
from pathlib import Path
Path("inutile.txt").unlink()        # supprime un fichier
shutil.rmtree("vieux_dossier")      # supprime un dossier et son contenu
```

> ⚠️ Ces opérations sont **définitives** : pas de corbeille. Teste tes
> scripts sur des copies avant de les lancer sur de vrais fichiers.

## À toi

Écris `sauvegarder(source, destination)` qui copie le fichier `source`
vers `destination` et renvoie `destination`.""",
            "starter": "import shutil\n\ndef sauvegarder(source, destination):\n    ...\n",
            "check": "import tempfile, pathlib\n"
                     "d = pathlib.Path(tempfile.mkdtemp())\n"
                     "src = d / 'original.txt'; src.write_text('contenu', encoding='utf-8')\n"
                     "dst = d / 'copie.txt'\n"
                     "r = sauvegarder(str(src), str(dst))\n"
                     "assert pathlib.Path(dst).exists()\n"
                     "assert pathlib.Path(dst).read_text(encoding='utf-8') == 'contenu'\n",
            "solution": "import shutil\n\ndef sauvegarder(source, destination):\n"
                        "    shutil.copy(source, destination)\n    return destination\n",
        },
        {
            "id": "adm-05",
            "title": "Mini-projet : ranger un dossier automatiquement",
            "content": """## Un vrai script utile

Assemblons tout pour résoudre un problème courant : un dossier de
téléchargements en bazar. On va **ranger chaque fichier dans un
sous-dossier nommé d'après son extension** (`jpg`, `pdf`, `txt`...).

Le plan :
1. parcourir les fichiers du dossier ;
2. pour chacun, trouver son extension ;
3. créer le sous-dossier correspondant s'il n'existe pas ;
4. y déplacer le fichier.

```
from pathlib import Path
import shutil

def ranger(dossier):
    base = Path(dossier)
    compte = {}
    for fichier in list(base.iterdir()):
        if fichier.is_file():
            ext = fichier.suffix.lstrip(".").lower() or "sans_extension"
            cible = base / ext
            cible.mkdir(exist_ok=True)
            shutil.move(str(fichier), str(cible / fichier.name))
            compte[ext] = compte.get(ext, 0) + 1
    return compte
```

C'est un script réellement utilisable au quotidien.

## À toi

Écris la fonction `ranger(dossier)` décrite ci-dessus : elle range les
fichiers par extension (en minuscules) et renvoie un dictionnaire
`{extension: nombre_de_fichiers_déplacés}`.""",
            "starter": "from pathlib import Path\nimport shutil\n\ndef ranger(dossier):\n    ...\n",
            "check": "import tempfile, pathlib\n"
                     "d = pathlib.Path(tempfile.mkdtemp())\n"
                     "(d / 'photo.jpg').write_text('x'); (d / 'image.JPG').write_text('x')\n"
                     "(d / 'notes.txt').write_text('x')\n"
                     "res = ranger(str(d))\n"
                     "assert res == {'jpg': 2, 'txt': 1}, res\n"
                     "assert (d / 'jpg' / 'photo.jpg').exists()\n"
                     "assert (d / 'txt' / 'notes.txt').exists()\n",
            "solution": "from pathlib import Path\nimport shutil\n\ndef ranger(dossier):\n"
                        "    base = Path(dossier)\n    compte = {}\n"
                        "    for fichier in list(base.iterdir()):\n"
                        "        if fichier.is_file():\n"
                        "            ext = fichier.suffix.lstrip('.').lower() or 'sans_extension'\n"
                        "            cible = base / ext\n            cible.mkdir(exist_ok=True)\n"
                        "            shutil.move(str(fichier), str(cible / fichier.name))\n"
                        "            compte[ext] = compte.get(ext, 0) + 1\n    return compte\n",
        },
    ],
}
