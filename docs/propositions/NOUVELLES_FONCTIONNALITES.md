# 🛠️ Spécifications des Nouvelles Fonctionnalités Logicielles

Ce document détaille l'architecture technique, les maquettes d'interface et les modalités d'implémentation pour les fonctionnalités proposées dans PythonLearn.

---

## 1. 🐢 Visualiseur de Tracé Graphique (Turtle Canvas direct)

### Objectif :
Permettre d'exécuter et d'observer en direct le tracé de la tortue dans le parcours 10 (Dessiner) sans faire surgir une fenêtre `turtle` séparée qui bloque l'interface Tkinter principale.

### Conception technique :
- Utiliser `turtle.RawTurtle` et `turtle.TurtleScreen` attachés directement à un `tk.Canvas` embarqué dans `app/ui.py`.
- Créer une classe `VueTurtle(tk.Frame)` dans `app/vues_exercices.py` similairement à `VuePrediction` et `VueOrdre`.
- Exécuter les commandes de tracé de façon fluide ou avec un bouton de vitesse réglable.

---

## 2. 🧠 Inspecteur de Mémoire & Références (Memory & Scope Visualizer)

### Objectif :
Afficher visuellement les variables locales/globales et des flèches pointant vers les objets en mémoire vive (listes, dicts, instances) pour comprendre le passage par référence et les mutations d'objets.

### Conception technique :
- Intégré dans la fenêtre pas-à-pas (`StepWindow` dans `app/windows.py`) ou un onglet dédié.
- Utilise `id(objet)` et `type(objet)` pour détecter si deux variables partagent la même référence mémoire (`a is b`).
- Rendu graphique sur un `tk.Canvas` :
  - Colonne de gauche : Table des symboles (noms de variables).
  - Colonne de droite : Blocs mémoires (adresses et valeurs d'objets).
  - Lignes de connexion vectorielles entre les étiquettes et les objets.

---

## 3. 🎯 Mode « Défi du Jour » (Daily Challenge)

### Objectif :
Proposer chaque jour un exercice ou un quiz adapté pour stimuler la régularité et alimenter la série de jours consécutifs (`streak`).

### Conception technique :
- Formule déterministe basée sur la date : `index = date.today().toordinal() % total_exercices`.
- Ajout d'une section dédiée sur `AccueilWindow` (`app/windows.py`) avec un bouton d'action directe : **« Relever le défi du jour ⚡ »**.
- Enregistrement dans `self.data["defis_reussis"][iso_date] = item_id`.

---

## 4. ⚔️ Mode « Duel en Réseau Local » (LAN Code Battle)

### Objectif :
Défier un ami ou un camarade sur le même réseau Wi-Fi local sans aucun serveur tiers ni connexion Internet.

### Conception technique :
- Utilise uniquement le module standard `socket` et `threading`.
- Rôles :
  - **Hôte** : Crée un serveur TCP sur un port libre (ex. 4242) et affiche l'adresse IP locale (`socket.gethostbyname(...)`).
  - **Client** : Rejoint l'adresse IP saisie.
- Déroulement :
  - Synchronisation de l'exercice choisi.
  - Compte à rebours 3, 2, 1, Partez !
  - Dès qu'un joueur clique sur « Vérifier » et que son code réussit les tests, un paquet JSON `{"gagne": True, "temps": ...}` est envoyé à l'adversaire.
  - Affichage d'un écran de victoire / défaite avec confettis (`Celebration`).

---

## 5. 🔍 Inspecteur de Bytecode CPython (`dis`)

### Objectif :
Permettre aux apprenants curieux de visualiser le bytecode compilé par CPython pour leur fonction.

### Conception technique :
- Ajout d'un bouton discret **« Bytecode ⚙ »** à côté du bouton d'exportation `.py`.
- Utilisation du module standard `dis.Bytecode(code_string)`.
- Rendu dans une fenêtre modale avec coloration des opcodes (`LOAD_FAST`, `BINARY_OP`, `STORE_FAST`, `RETURN_VALUE`) et explications de chaque instruction de pile.

---

## 6. 🗄️ Explorateur Visuel de Base de Données SQLite

### Objectif :
Pour le parcours SQLite (Track 9), afficher sous l'éditeur un tableau interactif représentant la base de données en mémoire.

### Conception technique :
- Inspection du schéma via `SELECT name FROM sqlite_master WHERE type='table';`.
- Récupération des colonnes via `PRAGMA table_info(nom_table);`.
- Affichage dans un widget `ttk.Treeview` multi-colonnes mis à jour après chaque exécution.

---

## 7. 📱 Exportateur Anki & Flashcards (.tsv)

### Objectif :
Permettre d'exporter les 24 fiches de vocabulaire et les questions de quiz pour les réviser sur mobile.

### Conception technique :
- Dans le menu Outils / Glossaire : bouton **« Exporter pour Anki (.tsv) »**.
- Format généré :
  ```tsv
  Terme / Question<TAB>Définition / Réponse<TAB>Tag
  ```
- Compatible avec Anki Desktop, AnkiMobile, AnkiDroid et Quizlet.

---

## 8. 🛡️ Mini-Linter Pédagogique (Style PEP 8 en direct)

### Objectif :
Aider les débutants à acquérir de bonnes habitudes d'écriture sans être bloquant.

### Conception technique :
- Analyse par AST (`ast.parse(code)`) lors de la saisie (`_on_code_change`).
- Détecte :
  - `range(len(...))` -> suggère `enumerate(...)`.
  - Comparaisons chaînées `x == 1 or x == 2` -> suggère `x in (1, 2)`.
  - Nom de variable avec majuscule (non-classe).
  - Variables créées mais jamais réutilisées.
- Affichage d'une discrète ampoule 💡 avec astuce de style non-bloquante.
