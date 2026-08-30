"""
Version de l'application — source unique de vérité.

Elle est lue par :
  - `main.py --version` (et le contrôle de santé de la CI) ;
  - les scripts d'empaquetage (installateur Windows, .deb, .dmg) ;
  - le workflow GitHub Actions, qui la compare au tag `vX.Y.Z` publié.

Pour publier une nouvelle version : modifier __version__ ici, committer,
puis poser le tag correspondant (ex. `git tag v1.1.0`).
"""

__version__ = "1.3.0"

APP_NAME = "PythonLearn"
APP_ID = "python-learn"
AUTEUR = "Cédric Monna"
ANNEE = "2026"
DEPOT = "https://github.com/caine777-data/python-learn"
DESCRIPTION = "Apprendre Python pas à pas, du débutant à l'expert."
