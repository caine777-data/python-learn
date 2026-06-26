"""Parcours 6 — Interfaces graphiques (Tkinter)."""

LEVEL = {
    "id": "interfaces",
    "title": "6 · Interfaces graphiques",
    "lessons": [
        {
            "id": "gui-01",
            "title": "Ta première fenêtre",
            "content": """## Des programmes avec des boutons

Jusqu'ici nos programmes parlaient dans la console. On peut aussi créer
de vraies **fenêtres** avec des boutons, des champs de saisie, etc.
L'outil intégré à Python pour ça s'appelle **Tkinter**.

Voici le squelette minimal d'une application. **Copie ce code dans un
fichier `app.py` et lance-le** pour voir apparaître une fenêtre :

```
import tkinter as tk

fenetre = tk.Tk()                    # crée la fenêtre principale
fenetre.title("Ma première app")
fenetre.geometry("300x150")          # largeur x hauteur

etiquette = tk.Label(fenetre, text="Bonjour !")
etiquette.pack(pady=20)              # place le texte dans la fenêtre

fenetre.mainloop()                   # affiche et attend les actions
```

`mainloop()` est la « boucle d'événements » : elle garde la fenêtre
ouverte et réagit aux clics. Le programme s'arrête quand on ferme la
fenêtre.

> ⚠️ Ne lance pas `mainloop()` ici dans l'éditeur : il sert à de vraies
> fenêtres. Dans cet atelier, on travaille la **logique** des apps.

## À toi

Écris une fonction `texte_accueil(prenom)` qui renvoie le texte que
l'étiquette devrait afficher : `Bienvenue, <prenom> !`""",
            "starter": "def texte_accueil(prenom):\n    ...\n",
            "check": 'assert texte_accueil("Ada") == "Bienvenue, Ada !"\n'
                     'assert texte_accueil("Cédric") == "Bienvenue, Cédric !"\n',
            "solution": 'def texte_accueil(prenom):\n    return f"Bienvenue, {prenom} !"\n',
        },
        {
            "id": "gui-02",
            "title": "Les widgets : étiquettes, champs, boutons",
            "content": """## Les briques de l'interface

Un **widget** est un élément d'interface. Les plus courants :

- `Label` : afficher du texte
- `Entry` : un champ où l'utilisateur tape
- `Button` : un bouton cliquable

```
import tkinter as tk

fenetre = tk.Tk()

champ = tk.Entry(fenetre)            # zone de saisie
champ.pack()

bouton = tk.Button(fenetre, text="Valider")
bouton.pack()

fenetre.mainloop()
```

On **lit** ce que l'utilisateur a tapé dans un `Entry` avec
`champ.get()`, et on **change** un `Label` avec
`etiquette.config(text="nouveau texte")`.

## À toi

Quand l'utilisateur tape un texte et clique sur « Crier », l'app doit
l'afficher en majuscules avec un `!`. Écris la fonction `crier(texte)`
qui renvoie le texte en MAJUSCULES suivi de `!`.
Exemple : `"bonjour"` → `"BONJOUR!"`.""",
            "starter": "def crier(texte):\n    ...\n",
            "check": 'assert crier("bonjour") == "BONJOUR!"\nassert crier("Salut") == "SALUT!"\n',
            "solution": 'def crier(texte):\n    return texte.upper() + "!"\n',
        },
        {
            "id": "gui-03",
            "title": "Réagir aux clics : les callbacks",
            "content": """## Brancher une action sur un bouton

Un bouton déclenche une **fonction** quand on clique dessus. On la
branche avec le paramètre `command` (on passe le **nom** de la fonction,
sans parenthèses) :

```
import tkinter as tk

fenetre = tk.Tk()
compteur = {"valeur": 0}
etiquette = tk.Label(fenetre, text="0")
etiquette.pack()

def au_clic():
    compteur["valeur"] += 1
    etiquette.config(text=str(compteur["valeur"]))

bouton = tk.Button(fenetre, text="+1", command=au_clic)
bouton.pack()

fenetre.mainloop()
```

À chaque clic, `au_clic` s'exécute : elle met à jour le compteur et le
réaffiche. C'est le cœur d'une application interactive.

## À toi

Écris la fonction `incrementer(valeur)` qui renvoie `valeur + 1`
(c'est la logique que le bouton « +1 » appellerait à chaque clic).""",
            "starter": "def incrementer(valeur):\n    ...\n",
            "check": "assert incrementer(0) == 1\nassert incrementer(41) == 42\n",
            "solution": "def incrementer(valeur):\n    return valeur + 1\n",
        },
        {
            "id": "gui-04",
            "title": "Disposer les widgets",
            "content": """## Organiser la fenêtre

Tkinter propose plusieurs façons de placer les widgets :

- `.pack()` : empile simplement (haut/bas ou gauche/droite) — simple et
  rapide pour commencer.
- `.grid(row=..., column=...)` : place dans une grille (lignes /
  colonnes) — idéal pour les formulaires.

```
import tkinter as tk
fenetre = tk.Tk()

tk.Label(fenetre, text="Nom :").grid(row=0, column=0)
tk.Entry(fenetre).grid(row=0, column=1)
tk.Label(fenetre, text="Âge :").grid(row=1, column=0)
tk.Entry(fenetre).grid(row=1, column=1)

fenetre.mainloop()
```

On peut espacer avec `padx`/`pady`. La clé est de **choisir une seule
méthode** par conteneur (pas de `pack` et `grid` mélangés au même
niveau).

## À toi

Pour un formulaire, on veut générer les libellés. Écris
`etiquettes(champs)` qui transforme une liste de noms en liste de
libellés finissant par ` :`. Exemple :
`["Nom", "Âge"]` → `["Nom :", "Âge :"]`.""",
            "starter": "def etiquettes(champs):\n    ...\n",
            "check": 'assert etiquettes(["Nom", "Âge"]) == ["Nom :", "Âge :"]\n'
                     'assert etiquettes([]) == []\n',
            "solution": 'def etiquettes(champs):\n    return [f"{c} :" for c in champs]\n',
        },
        {
            "id": "gui-05",
            "title": "Mini-projet : convertisseur °C → °F",
            "content": """## Une petite app complète

Assemblons tout dans un convertisseur de température. **Copie ce code
dans un fichier et lance-le** : tu tapes des degrés Celsius, tu cliques,
le résultat en Fahrenheit s'affiche.

```
import tkinter as tk

def convertir():
    try:
        c = float(champ.get())
        f = c * 9 / 5 + 32
        resultat.config(text=f"{c} °C = {f} °F")
    except ValueError:
        resultat.config(text="Entre un nombre valide")

fenetre = tk.Tk()
fenetre.title("Convertisseur")

champ = tk.Entry(fenetre)
champ.pack(pady=5)
tk.Button(fenetre, text="Convertir", command=convertir).pack()
resultat = tk.Label(fenetre, text="")
resultat.pack(pady=5)

fenetre.mainloop()
```

Tu as là une vraie application : saisie, traitement, affichage.

## À toi

Écris le cœur du calcul : la fonction `celsius_vers_fahrenheit(c)` qui
applique la formule `c × 9/5 + 32`.""",
            "starter": "def celsius_vers_fahrenheit(c):\n    ...\n",
            "check": "assert celsius_vers_fahrenheit(0) == 32\n"
                     "assert celsius_vers_fahrenheit(100) == 212\n"
                     "assert celsius_vers_fahrenheit(37) == 98.6\n",
            "solution": "def celsius_vers_fahrenheit(c):\n    return c * 9 / 5 + 32\n",
        },
    ],
}
