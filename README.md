# PythonLearn 🐍

**Conçu et réalisé par Cédric Monna** — logiciel libre sous licence MIT.

Une application de bureau pour **apprendre Python pas à pas, du niveau
débutant au niveau expert**. Chaque leçon mêle une explication claire et
un exercice que l'on résout dans un éditeur intégré : le code s'exécute
pour de vrai et la réussite est vérifiée automatiquement.

- ✅ Parcours structuré : **16 parcours, 145 exercices**, du tout débutant aux projets concrets
- ✅ Éditeur intégré avec **coloration syntaxique**, **numéros de ligne** et **exécution réelle**
- ✅ **Syntaxe vérifiée en temps réel** (ligne fautive soulignée), **autocomplétion** (Ctrl+Espace)
- ✅ **Exécution pas-à-pas** : avance ligne par ligne en voyant les variables et la sortie évoluer
- ✅ **Export** du code d'un exercice en fichier `.py`
- ✅ Confort visuel : **surlignage de la ligne courante**, titres de leçons complets au survol, splash screen en fondu
- ✅ Interface soignée : **boutons d'action en couleur d'accent** avec effet de survol, **bannière de réussite animée**, barres de progression (global + niveau)
- ✅ **Vérification automatique** des exercices, avec **messages d'erreur expliqués en français**
- ✅ **Inspecteur de variables** après exécution + **comparaison attendu/obtenu** en cas d'échec
- ✅ **Bac à sable** libre (« Brouillon ») pour expérimenter sans exercice
- ✅ **Indices progressifs** (dévoilés un par un) avant de révéler la solution
- ✅ **Quiz (QCM) à la fin de chaque parcours** et **projets guidés multi-étapes**
- ✅ Exercices variés : à compléter (**trous**), à réparer (**débogue ce code**),
  **prédire la sortie** avant d'exécuter, et **remettre des lignes dans l'ordre**
- ✅ **3 thèmes** (sombre / clair / contraste élevé) + **zoom** du texte
- ✅ **Glossaire** intégré, **mode révision**, **recherche** de leçon, lien vers la doc Python
- ✅ **Antisèche imprimable** (mémo de syntaxe HTML) et **flashcards** de révision
- ✅ **Suivi de progression** (barre + compteurs par parcours) et **badges** par parcours
- ✅ **Série de jours (streak)**, objectif quotidien et **statistiques** (graphique 7 jours)
- ✅ **XP & niveaux**, **objectif hebdomadaire**, et **recommandation adaptative** (« 🧭 Et après ? »)
- ✅ **Notes personnelles** et **favoris** par leçon (marqueurs ★ / 📝 dans la liste)
- ✅ **Mode examen chronométré** (questions au hasard, 5 minutes, score final)
- ✅ **Export / import de la progression** en JSON (pour changer de machine)
- ✅ **Révision espacée** : les exercices reviennent à intervalles croissants (1, 3, 7, 16… jours)
- ✅ **Certificat** de fin de parcours (HTML imprimable, à ton nom)
- ✅ Confort d'édition : auto-fermeture des parenthèses, `Ctrl+/` pour commenter, indentation de bloc
- ✅ **Interface bilingue FR / EN** (bascule en un clic ; le contenu des leçons reste en français)
- ✅ **Écran d'accueil** : série de jours, progression, reprise en un clic,
  et **rattrapage ciblé** sur les exercices qui t'ont le plus résisté
- ✅ **Packs de leçons** : ajoute tes propres exercices avec un simple
  fichier `.json`, sans écrire une ligne de code (idéal en classe)
- ✅ **Zéro dépendance** pour l'utilisateur (tout est en bibliothèque standard)
- ✅ **Bac à sable sécurisé** : le « Brouillon » limite les modules importables et l'accès fichier/système
- ✅ **Tests automatisés** : les 145 exercices et 129 tests sont vérifiés par la CI
  sur 3 systèmes et 2 versions de Python
- ✅ **Installateurs** Windows (.exe), macOS (.dmg Apple Silicon)
  et Linux (.deb + archive) générés **automatiquement** par GitHub Actions

|  Thème sombre  |  Thème clair  |  Quiz (contraste élevé)  |
|:---:|:---:|:---:|
| ![sombre](assets/screenshot-dark.png) | ![clair](assets/screenshot-light.png) | ![quiz](assets/screenshot-quiz.png) |

> *Captures réalisées en environnement de test ; les emojis des badges
> s'affichent normalement sur Windows et macOS.*

Le tableau de bord **Stats** (série, objectif, graphique 7 jours, révisions, certificats) :

![stats](assets/screenshot-stats.png)

L'**exécution pas-à-pas** (ligne courante surlignée, variables et sortie à chaque étape) :

![pas-à-pas](assets/screenshot-step.png)

L'**interface bilingue** — ici en anglais (le contenu des leçons reste en français) :

![anglais](assets/screenshot-en.png)

Le mode **« débogue ce code »** (bandeau dédié, bug réel à réparer) :

![débogue](assets/screenshot-debug.png)

Le parcours **Algorithmes & structures de données** (ici la recherche dichotomique) :

![algorithmes](assets/screenshot-algos.png)

Le **mode examen** chronométré (questions au hasard, score final) :

![examen](assets/screenshot-exam.png)

Les **flashcards** de révision (recto terme / verso définition) et l'**antisèche** imprimable :

![flashcards](assets/screenshot-flashcards.png)

![antisèche](assets/screenshot-cheatsheet.png)

## ⌨️ Raccourcis

| Raccourci | Action |
|-----------|--------|
| `Ctrl + Entrée` | Exécuter le code |
| `Ctrl + Espace` | Autocomplétion (mots-clés et noms du code) |
| `Ctrl + /` | Commenter / décommenter la sélection |
| `Tab` / `Maj + Tab` | Indenter / désindenter la sélection |
| `Ctrl + +` / `Ctrl + -` / `Ctrl + 0` | Zoom avant / arrière / réinitialiser |

## 📚 Les parcours

Chaque parcours de cours se termine par un **quiz de récap**. Le dernier
parcours est entièrement consacré aux **projets guidés**.

**Fondamentaux**
1. **Débutant** — afficher, variables, calculs, texte, `input()`, conditions, boucles, listes, fonctions, modules, atelier + quiz.
2. **Intermédiaire** — slicing, compréhensions, tuples, dictionnaires, fonctions avancées, ensembles, modules, tri, exceptions + quiz.
3. **Avancé** — générateurs, POO complète, décorateurs, propriétés, fichiers, expressions régulières + quiz.
4. **Expert** — gestionnaires de contexte, dataclasses, `functools`, async, ABC, tests unitaires, `itertools` + quiz.

**Parcours pratiques (orientés projets)**

5. **Scripts & automatisation** — scripts, `pathlib`, fichiers, JSON, CSV, dates + quiz.
6. **Interfaces graphiques** — créer des fenêtres et des apps avec Tkinter + quiz.
7. **Python & le web** — HTTP, générer du HTML, lire une API, mini-serveur, Flask/Django + quiz.
8. **Administrer son PC** — système, variables d'environnement, fichiers, ranger un dossier + quiz.
9. **Bases de données (SQLite)** — créer une table, INSERT, SELECT, WHERE, UPDATE/DELETE, agrégats + quiz.
10. **Dessiner (turtle)** — polygones, motifs, spirales, coordonnées, rosace + quiz.

**Approfondissement**

11. **Algorithmes & structures de données** — recherche linéaire et dichotomique, tri à bulles, récursivité (factorielle, Fibonacci), pile (LIFO), file (FIFO) + quiz.
12. **Manipuler des données** — `statistics` (moyenne, médiane), `Counter`, `defaultdict`, lire un CSV, agréger des données + quiz.
13. **Tests & TDD** — `assert`, lire un test comme une spécification, cas limites, cycle rouge-vert-refactor, écrire ses propres tests + quiz.

**Projets guidés** (multi-étapes, validés exercice par exercice)

14. **Projets guidés** — le **Pendu**, une **liste de tâches**, un **bloc-notes** Tkinter, un **convertisseur de devises**, le **Jeu de la vie** de Conway, et le **hachage sécurisé** d'un mot de passe.
16. **Décoder les erreurs** — lire un message d'erreur, reconnaître les
    grands types (`NameError`, `TypeError`, `ValueError`, `IndexError`…),
    comprendre pourquoi une `SyntaxError` désigne souvent la ligne du dessus,
    et remonter un traceback à plusieurs niveaux. **Accessible dès la fin du
    niveau débutant** : c'est la compétence qui débloque le plus vite.

15. **Entraînement** — réparer des bugs classiques (borne, condition inversée, IndexError), compléter du code à trous, **prédire la sortie** d'un programme avant de l'exécuter, et **remettre dans l'ordre** les lignes d'un programme mélangé.

---

## 🚀 Lancer l'application depuis les sources

Il suffit d'avoir Python 3.10 ou plus.

```bash
git clone https://github.com/<ton-compte>/python-learn.git
cd python-learn
python main.py
```

> **Linux** : si tkinter manque, installe-le avec
> `sudo apt install python3-tk`.
> **Windows / macOS** : tkinter est inclus avec l'installateur officiel
> de [python.org](https://www.python.org/downloads/).

---

## 📦 Installer l'application (rien à compiler)

Va dans l'onglet **[Releases](../../releases)** et prends le fichier qui
correspond à ton système. **Python n'a pas besoin d'être installé** : tout
est embarqué dans le téléchargement.

| Système | Fichier | Installation |
|---|---|---|
| **Windows** | `PythonLearn-Setup-<version>.exe` | Double-clic. S'installe pour ton compte, sans droits administrateur. |
| Windows, sans installer | `PythonLearn-<version>-windows-portable.exe` | Se lance directement depuis le fichier téléchargé. |
| **macOS** Apple Silicon | `PythonLearn-<version>-arm64.dmg` | Glisse l'app dans Applications, puis **clic droit → Ouvrir** au premier lancement. |
| **macOS** Intel | *(aucun)* | Voir la note ci-dessous. |
| **Debian / Ubuntu / Mint** | `python-learn_<version>_amd64.deb` | `sudo apt install ./python-learn_<version>_amd64.deb` |
| **Autres Linux** | `python-learn-<version>-linux-amd64.tar.gz` | Décompresse, puis `bash installer.sh` (aucun `sudo` requis). |

Le fichier `SHA256SUMS.txt` joint à chaque Release permet de vérifier
l'intégrité de ce que tu as téléchargé.

> **Pourquoi rien pour les Mac Intel ?** GitHub a retiré les machines de
> construction Intel, et un binaire Apple Silicon ne démarre pas sur un
> processeur Intel. Ces Mac restent parfaitement servis par les sources :
> installe Python depuis [python.org](https://www.python.org/downloads/),
> puis lance `python main.py` (voir plus bas). C'est la même application.

### Les avertissements de sécurité, en clair

L'application n'est signée par aucun certificat payant. Les systèmes
préviennent donc l'utilisateur au premier lancement — c'est attendu, et sans
danger :

- **Windows** : *« Windows a protégé votre ordinateur »* →
  *Informations complémentaires* → *Exécuter quand même*.
- **macOS** : au premier lancement, **clic droit sur l'app → Ouvrir** (un
  double-clic ne proposerait pas l'option). Si macOS annonce que l'application
  est « endommagée » :
  `xattr -dr com.apple.quarantine /Applications/PythonLearn.app`.

---

## 🚢 Publier une nouvelle version

Tout est automatisé par GitHub Actions ; il n'y a rien à compiler soi-même.

1. Mettre à jour le numéro dans [`app/version.py`](app/version.py).
2. Committer, puis poser le tag correspondant :
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```
3. Le workflow `build.yml` lance les tests, construit les cinq fichiers
   d'installation (Windows, macOS, Linux), vérifie chaque exécutable
   produit, puis crée la **Release** avec ses empreintes.

> Le tag doit correspondre exactement à `app/version.py` : sinon la CI
> s'arrête avec un message explicite, plutôt que de publier une version mal
> étiquetée.

Pour essayer la chaîne sans rien publier : onglet **Actions** →
*Construire les installateurs* → **Run workflow**. Les fichiers sont alors
déposés en artefacts, sans créer de Release.

Le détail (signature de code, notarisation Apple, Inno Setup) est dans
**[DIFFUSION.md](DIFFUSION.md)**.

---

## 🎒 Créer ses propres leçons (sans programmer)

Tu peux ajouter tes propres parcours **sans toucher au code**, en déposant
un simple fichier `.json`. C'est pensé pour les enseignants : tes exercices
viennent s'ajouter aux 15 parcours livrés, et se partagent en envoyant un
seul fichier.

**Depuis l'application** — clique sur **📦 Mes leçons** dans la barre du
haut. Le dossier s'ouvre dans l'explorateur, avec un exemple à modifier.
Relance PythonLearn : ton parcours apparaît dans la liste, précédé de 📦.

**Depuis un terminal**, si tu travailles à partir des sources :

```bash
python main.py --exemple-pack
```

```bash
python main.py --verifier-packs
```

Tu peux aussi partir du fichier [`exemples/mon-cours.json`](exemples/mon-cours.json).

### À quoi ressemble un fichier de leçons

```json
{
  "format": 1,
  "id": "mon-cours",
  "titre": "Mon cours",
  "auteur": "Prénom Nom",
  "lecons": [
    {
      "id": "moncours-01",
      "title": "Afficher un message",
      "content": "## Afficher du texte\n\nLa fonction `print()` affiche...",
      "starter": "# Écris ton code ici\n",
      "expected_output": "Bonjour la classe",
      "solution": "print('Bonjour la classe')\n",
      "hints": ["Utilise print(...).", "Le texte va entre guillemets."]
    }
  ]
}
```

| Champ | Rôle |
|---|---|
| `id` | identifiant unique du parcours, puis de chaque leçon |
| `titre` | nom affiché dans la liste des parcours |
| `auteur` | facultatif, affiché à la vérification |
| `content` | l'explication (même balisage que les leçons livrées, voir plus bas) |
| `starter` | le code déjà présent dans l'éditeur au départ |
| `expected_output` | la sortie attendue, **ou** … |
| `check` | … du code de test (`assert ...`) exécuté après celui de l'élève |
| `solution` | la solution révélable |
| `hints` | les indices, dévoilés un par un |

### Les cinq sortes de leçons

| `type` | Ce que fait l'apprenant | Champs propres |
|---|---|---|
| *(aucun)* | écrit du code dans l'éditeur | `starter`, `check` / `expected_output` |
| `quiz` | répond à un QCM | `question`, `options`, `answer` (0 = première option) |
| `predire` | **annonce la sortie avant d'exécuter** | `code`, `explanation` |
| `ordre` | **remet des lignes mélangées dans l'ordre** | `lignes` (dans le bon ordre) |
| *(aucun)* + `exercices` | enchaîne plusieurs étapes | une liste `exercices` |

Les deux types en gras font travailler la **lecture** du code, là où
l'éditeur seul encourage parfois à modifier au hasard jusqu'à ce que la
vérification passe.

```json
{
  "id": "moncours-03",
  "type": "predire",
  "title": "Devine ce que ça affiche",
  "content": "## Lire avant d'exécuter\n\n…",
  "code": "print(2 + 3)\nprint('2' + '3')\n",
  "explanation": "Entre guillemets, « + » colle les textes bout à bout."
}
```

```json
{
  "id": "moncours-04",
  "type": "ordre",
  "title": "Remets le programme dans l'ordre",
  "lignes": ["total = 0", "for n in [1, 2, 3]:", "    total = total + n", "print(total)"],
  "expected_output": "6"
}
```

> Pour `ordre`, les `lignes` s'écrivent **dans le bon ordre** : l'application
> les mélange elle-même, toujours de la même façon pour un exercice donné, et
> jamais dans l'ordre correct. Si tu ajoutes `expected_output` ou `check`, la
> validation se fait en exécutant le programme reconstitué — plusieurs ordres
> peuvent alors être acceptés, ce qui est plus juste quand deux lignes sont
> réellement interchangeables.

### Vérifier son travail

`--verifier-packs` dit précisément ce qui ne va pas, sans jargon :

```
1 fichier(s) trouvé(s), 1 parcours utilisable(s).
  OK   mon-cours            3 leçon(s) — Prénom Nom

Points à corriger :
  - mon-cours.json — leçon 2 (« moncours-02 ») : « answer » vaut 5, mais il
    n'y a que 3 options (numérotées de 0 à 2). Quiz écarté : personne ne
    pourrait le réussir.
```

Un fichier mal formé n'empêche jamais l'application de démarrer : les leçons
en cause sont écartées, les autres sont chargées, et un message récapitule
ce qu'il faut corriger.

> ⚠️ **Un pack contient du code qui s'exécutera sur la machine de
> l'apprenant** (les champs `check` et `solution`), au moment où il clique
> sur « Vérifier » ou « Solution ». N'installe que des packs dont tu connais
> la provenance, comme pour n'importe quel programme. Rien n'est exécuté au
> simple chargement du fichier.

---

## ➕ Ajouter ou modifier des leçons

Tout le contenu pédagogique vit dans le dossier `content/`, un fichier
par niveau. Pour ajouter une leçon, ajoute simplement un dictionnaire à
la liste `lessons` du niveau voulu :

```python
{
    "id": "deb-08",                      # identifiant unique
    "title": "Ma nouvelle leçon",
    "content": "## Titre\n\nDu texte...\n```\nprint('exemple')\n```",
    "starter": "# code de départ\n",
    "expected_output": "résultat attendu",   # OU
    "check": "assert resultat == 42",        # code de test
    "solution": "resultat = 42\n",           # solution révélable
}
```

L'interface se met à jour automatiquement — aucune autre modification
n'est requise.

**Mini-balisage du champ `content` :**

| Syntaxe          | Rendu                          |
|------------------|--------------------------------|
| `## Titre`       | Sous-titre                     |
| `` ```...``` ``  | Bloc de code (monospace)       |
| `` `code` ``     | Code en ligne                  |
| `**gras**`       | Texte en gras                  |
| `- élément`      | Puce                           |

**Modes de validation d'un exercice :**

- `expected_output` : la sortie texte doit correspondre exactement ;
- `check` : du code Python exécuté ensuite (`assert ...`), avec accès aux
  variables/fonctions définies par l'apprenant ;
- `stdin` : liste de lignes simulant la saisie clavier (`input()`).

**Champs avancés (facultatifs) :**

- `hints` : liste d'indices dévoilés un par un (ou via `content/hints.py`) ;
- `type: "quiz"` + `question`, `options`, `answer` (index), `explanation` : une leçon QCM ;
- `exercices` : liste d'exercices (`prompt`, `starter`, `check`/`expected_output`,
  `solution`, `hints`) pour un projet multi-étapes affiché avec des onglets.

---

## 🗂️ Structure du projet

```
python-learn/
├── main.py                  # point d'entrée (--version, --check)
├── pyproject.toml           # métadonnées + configuration de ruff
├── .github/workflows/
│   ├── tests.yml            # tests + style (3 systèmes × 2 versions de Python)
│   └── build.yml            # installateurs Windows / macOS / Linux + Release
├── app/
│   ├── ui.py                # interface principale
│   ├── theme.py             # les 3 palettes de couleurs
│   ├── windows.py           # fenêtres : pas-à-pas, examen, flashcards…
│   ├── editor.py            # éditeur (coloration, n° de ligne, confort)
│   ├── runner.py            # exécution + vérification + bac à sable
│   ├── errors.py            # explication pédagogique des erreurs (FR / EN)
│   ├── stats.py             # streak, répétition espacée, certificat
│   ├── i18n.py              # traductions FR / EN de l'interface
│   ├── progress.py          # sauvegarde (atomique) de la progression
│   ├── version.py           # numéro de version, source unique
│   └── icon.py              # icône embarquée (base64)
├── exemples/
│   └── mon-cours.json       # pack de leçons d'exemple, à copier
├── content/
│   ├── __init__.py          # agrégation + utilitaires du schéma
│   ├── packs.py             # leçons ajoutées par l'utilisateur (.json)
│   ├── debutant.py … admin.py   # les 8 parcours de cours
│   ├── sqlite_db.py         # parcours Bases de données (SQLite)
│   ├── dessin.py            # parcours Dessiner (turtle)
│   ├── projets.py           # projets guidés multi-exercices
│   ├── quiz_parcours.py     # un quiz de fin par parcours (injecté auto)
│   ├── hints.py             # indices progressifs
│   └── glossaire.py         # termes du glossaire
├── packaging/
│   ├── installer.iss        # installateur Windows (Inno Setup)
│   ├── linux/               # paquet .deb + archive autonome
│   └── macos/               # disque d'installation .dmg
├── assets/                  # icônes + captures
├── tests/                   # tests du curriculum, du moteur et des traductions
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

La progression est stockée dans `~/.python-learn/progress.json`
(dossier personnel de l'utilisateur).

---

## 🌍 Traduire l'application

L'interface est **entièrement bilingue FR / EN**. Le contenu des leçons se
traduit progressivement, sans jamais casser quoi que ce soit : **ce qui
n'est pas encore traduit reste affiché en français**.

Déjà disponibles en anglais :

| Parcours | État |
|---|---|
| Les **16 titres de parcours** | ✅ |
| **1 · Débutant** (16 leçons) | ✅ intégralement |
| **2 · Intermédiaire** (11 leçons) | ✅ intégralement |
| **3 · Avancé** (11 leçons) | ✅ intégralement |
| **16 · Décoder les erreurs** (9 leçons) | ✅ intégralement |
| Les 10 autres parcours | à faire — affichés en français |

Soit **47 leçons sur 133 (35 %)**. Un anglophone peut donc suivre sans
rupture toute la progression générale — du tout premier `print()` jusqu'aux
générateurs, à la programmation objet et aux expressions régulières — puis
apprendre à décoder les messages d'erreur. Restent les parcours
thématiques (web, SQLite, turtle, projets…), que l'on choisit selon
l'envie plutôt que dans l'ordre.

Pour voir où en est le chantier :

```bash
python main.py --etat-traduction
```

Les traductions vivent toutes dans un seul fichier,
[`content/traductions.py`](content/traductions.py) — les fichiers de cours
restent en français et n'ont pas à être touchés. Une entrée se repère par
l'identifiant de la leçon, et ne contient que les champs traduits :

```python
"err-01": {
    "title": "Reading an error message",
    "content": "## Three pieces of information…",
    "hints": ["Read the last line of the message…"],
},
```

Ajouter une langue ne demande pas davantage : une nouvelle clé à côté de
`"en"`, et l'entrée correspondante dans `LANGUES` (`app/i18n.py`).

> Un test vérifie qu'aucune traduction ne devient orpheline : si une leçon
> est renommée, la CI le signale au lieu de laisser la traduction cesser
> silencieusement de s'appliquer.

---

## 📜 Licence

MIT — voir le fichier [LICENSE](LICENSE).
