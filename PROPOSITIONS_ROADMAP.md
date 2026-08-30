# 🗺️ Roadmap & Propositions d'Évolution pour PythonLearn

Ce document regroupe l'ensemble des propositions d'évolutions pédagogiques, techniques et ergonomiques conçues pour faire grandir l'application **PythonLearn**. Il est rédigé pour servir de guide d'étude et de feuille de route directement exploitable par **Claude Code** et les contributeurs du projet.

---

## 🧭 Principes fondamentaux du projet à préserver

Toute nouvelle fonctionnalité ou parcours doit respecter les règles d'or de PythonLearn :
1. **100 % Bibliothèque Standard (zéro dépendance externe)** : l'utilisateur final n'a besoin que d'une installation classique de Python avec Tkinter (aucun `pip install` requis).
2. **Bilinguisme intégral (FR / EN)** : tout texte d'interface, titre de leçon, énoncé, indice et quiz doit disposer de sa traduction dans [`content/traductions.py`](content/traductions.py).
3. **Pédagogie bienveillante et progressive** : explications courtes, concrètes, sans jargon inutile, avec feedback immédiat et indices progressifs.
4. **Qualité et non-régression** : 100 % des tests unitaires (`python -m unittest discover -s tests`) doivent passer.
5. **Résilience et fonctionnement hors-ligne** : l'application fonctionne sans connexion Internet, sauvegarde automatiquement et isole le code apprenant dans un bac à sable sécurisé.

---

## 📚 I. Nouveaux Parcours Pédagogiques Proposés (7 Parcours)

*(Le détail complet des leçons, starters, checks et solutions est documenté dans [`docs/propositions/NOUVEAUX_COURS.md`](docs/propositions/NOUVEAUX_COURS.md))*

| N° | Intitulé du parcours | Thème & Modules standard utilisés | Nombre de leçons | Statut |
|:---:|---|---|:---:|:---:|
| **17** | **Cybersécurité & Cryptographie** | Hachage, temps constant, tokens aléatoires, prévention SQLi/Path Traversal (`hashlib`, `hmac`, `secrets`, `pathlib`) | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |
| **18** | **Mathématiques, Sciences & Simulations** | Nombres premiers, précision exacte, Monte-Carlo, Newton, vecteurs (`math`, `cmath`, `decimal`, `fractions`, `random`) | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |
| **19** | **Traitement d'Images & Audio** | Pixels RGB, formats PPM/WAV en pur Python, filtres, synthèse de sons (`wave`, `struct`, `io`) | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |
| **20** | **Intelligence Artificielle (de zéro)** | k-NN, régression linéaire, perceptron, analyse de sentiments, recommandation cosinus | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |
| **21** | **Réseaux & Protocoles** | Sockets TCP/UDP, client/serveur, échange JSON, résolution DNS, mini-chat (`socket`, `threading`, `select`) | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |
| **22** | **Architecture & Jeux Vidéo 2D** | Game loop, grille 2D, collisions, inventaire, tour par tour, IA ennemie, sauvegarde JSON | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |
| **23** | **Design Patterns & Typage Moderne** | Singleton, Factory, Observateur, Stratégie, Protocoles, Enums, ABC (`typing`, `abc`, `enum`) | 6 leçons + 1 quiz | ✅ Implémenté & traduit (100%) |

---

## ⚡ II. Nouvelles Fonctionnalités Logicielles

*(Le détail d'implémentation est documenté dans [`docs/propositions/NOUVELLES_FONCTIONNALITES.md`](docs/propositions/NOUVELLES_FONCTIONNALITES.md))*

### 1. 🎯 Pédagogie & Pratique Quotidienne
- ✅ **Mode « Défi du Jour » (Daily Challenge)** : sélectionne automatiquement un exercice ou un quiz quotidien (basé sur le jour calendaire) pour entretenir sa série de jours (`streak 🔥`). Accessible depuis l'écran d'accueil (`AccueilWindow`).
- **Examen personnalisé & Mode « Mort Subite »** : choix des parcours inclus dans l'examen chronométré et mode survie où chaque erreur met fin à la session.
- **Mini-Linter pédagogique (Style PEP 8)** : alertes bienveillantes en temps réel (ex. suggérer `enumerate()`, `if x in (a, b):`, variables inutilisées).

### 2. 📊 Visualisations Riches & Interactives
- ✅ **Toile Turtle intégrée directement sur Canvas Tkinter (`VueTurtle`)** : affichage du tracé en direct pour le parcours Turtle sans ouvrir de fenêtre séparée.
- ✅ **Explorateur visuel de tables SQLite (`SqliteViewerWindow`)** : grille affichant en direct les tables de la base de données en mémoire et leurs modifications lors des requêtes.
- **Inspecteur de Mémoire & Références (façon Python Tutor)** : diagramme visuel interactif montrant les variables, les références et les objets en mémoire vive.

### 3. 🎮 Gamification, Multijoueur & Partage
- ✅ **Exportateur de paquets Anki (`.tsv`)** : réviser le glossaire et les concepts sur smartphone via un bouton dans la fenêtre de statistiques.
- **Trophées et Succès cachés (Achievements)** : badges de comportement (*Noctambule*, *Sans filet*, *Sprinter*, *Bilingue*, *Inarrêtable*).
- **Mode « Duel en Réseau Local » (LAN Code Battle)** : duel P2P de programmation chronométré entre deux ordinateurs sur le même Wi-Fi via `socket`.

### 4. 🛠️ Outils & Mode Enseignant
- ✅ **Inspecteur de Bytecode CPython (`dis`) (`BytecodeWindow`)** : voir les instructions machine virtuelles (`LOAD_FAST`, `BINARY_OP`, etc.) via un bouton dans la barre d'outils d'exercice.
- **Rechercher & Remplacer (`Ctrl+H`)** dans l'éditeur de code.
- **Console REPL interactive (`>>>`)** intégrée pour expérimenter instantanément.
- **Générateur de devoirs papier / PDF** : générer des feuilles d'exercices prêtes à imprimer avec corrigé pour les écoles et formateurs.

---

## 🏗️ III. Guide d'implémentation technique pour les contributeurs

### Structure des fichiers à respecter :
```text
LEARN_PYTHON/
├── app/
│   ├── editor.py           # Éditeur de code (coloration, raccourcis, recherche)
│   ├── errors.py           # Explications pédagogiques des erreurs d'exécution
│   ├── i18n.py             # Dictionnaires FR/EN de l'interface
│   ├── progress.py         # Gestion de la sauvegarde JSON et du spaced repetition (SRS)
│   ├── runner.py           # Moteur d'exécution sécurisé en sous-processus
│   ├── stats.py            # Calculs statistiques, badges SVG, certificats HTML
│   ├── theme.py            # Palettes graphiques (Dark, Light, Dracula, Nord, Contrast)
│   ├── ui.py               # Fenêtre principale Tkinter
│   └── windows.py          # Fenêtres secondaires (Examen, Flashcards, Palette, etc.)
├── content/
│   ├── <parcours>.py       # Définition d'un parcours (LEVEL dict avec lessons)
│   ├── glossaire.py        # Glossaire bilingue (get_glossaire)
│   ├── cheatsheet.py       # Antisèche bilingue (get_cheatsheet)
│   ├── traductions.py      # Dictionnaire TRADUCTIONS['en'] et fonction appliquer()
│   └── __init__.py         # Agrégation du CURRICULUM et helpers
└── tests/
    └── test_*.py           # Tests automatisés unittest
```

### Commandes de vérification rapide :
```bash
# Vérifier la santé globale de l'application
python main.py --check

# Vérifier le taux de traduction bilingue (doit être à 100 %)
python main.py --etat-traduction

# Lancer l'intégralité de la suite de tests automatisés
python -m unittest discover -s tests
```
