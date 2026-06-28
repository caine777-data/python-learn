"""Parcours 9 — Projets guidés (projets multi-exercices)."""

LEVEL = {
    "id": "projets",
    "title": "11 · Projets guidés",
    "lessons": [
        {
            "id": "proj-pendu",
            "title": "Projet : le jeu du Pendu",
            "content": """## Construisons un vrai jeu

Le **Pendu** : l'ordinateur choisit un mot, le joueur propose des
lettres, et perd une vie à chaque erreur. On va le construire **étape
par étape**, sous forme de petites fonctions que tu valides une par une.

Voici le jeu complet une fois assemblé (copie-le dans un fichier pour y
jouer dans le terminal) :

```
import random

def masquer(mot, trouvees):
    return "".join(l if l in trouvees else "_" for l in mot)

def est_gagne(mot, trouvees):
    return all(l in trouvees for l in mot)

mot = random.choice(["python", "ordinateur", "clavier"])
trouvees = set()
vies = 6

while vies > 0 and not est_gagne(mot, trouvees):
    print(masquer(mot, trouvees), "  vies :", vies)
    lettre = input("Une lettre : ")
    if lettre in mot:
        trouvees.add(lettre)
    else:
        vies -= 1

print("Gagné !" if est_gagne(mot, trouvees) else f"Perdu ! C'était {mot}")
```

À toi de coder chaque brique. Utilise les boutons **Exercice 1, 2, 3**
ci-dessus pour passer d'une étape à l'autre.""",
            "exercices": [
                {
                    "prompt": "Étape 1 — masquer(mot, trouvees) : renvoie le mot avec "
                              "un « _ » à la place des lettres pas encore trouvées. "
                              "Ex. : masquer(\"python\", {\"p\", \"o\"}) → \"p___o_\".",
                    "starter": "def masquer(mot, trouvees):\n    ...\n",
                    "check": 'assert masquer("python", {"p", "o"}) == "p___o_"\n'
                             'assert masquer("chat", set()) == "____"\n'
                             'assert masquer("chat", {"c","h","a","t"}) == "chat"\n',
                    "solution": 'def masquer(mot, trouvees):\n'
                                '    return "".join(l if l in trouvees else "_" for l in mot)\n',
                    "hints": ["Parcours chaque lettre du mot.",
                              "Si la lettre est dans trouvees, garde-la, sinon mets « _ ».",
                              'Utilise "".join(...) avec une compréhension.'],
                },
                {
                    "prompt": "Étape 2 — est_gagne(mot, trouvees) : renvoie True si TOUTES "
                              "les lettres du mot ont été trouvées.",
                    "starter": "def est_gagne(mot, trouvees):\n    ...\n",
                    "check": 'assert est_gagne("py", {"p", "y"}) is True\n'
                             'assert est_gagne("py", {"p"}) is False\n'
                             'assert est_gagne("aa", {"a"}) is True\n',
                    "solution": "def est_gagne(mot, trouvees):\n"
                                "    return all(l in trouvees for l in mot)\n",
                    "hints": ["La fonction all(...) renvoie True si tout est vrai.",
                              "Vérifie que chaque lettre du mot est dans trouvees."],
                },
                {
                    "prompt": "Étape 3 — jouer(etat, lettre) : met à jour l'état du jeu. "
                              "etat est un dict {\"mot\", \"trouvees\" (set), \"vies\" (int)}. "
                              "Si la lettre est dans le mot, ajoute-la aux trouvees ; "
                              "sinon enlève une vie. Renvoie etat.",
                    "starter": "def jouer(etat, lettre):\n    ...\n    return etat\n",
                    "check": 'e = {"mot": "chat", "trouvees": set(), "vies": 6}\n'
                             'jouer(e, "c")\nassert "c" in e["trouvees"] and e["vies"] == 6\n'
                             'jouer(e, "z")\nassert e["vies"] == 5\n',
                    "solution": "def jouer(etat, lettre):\n"
                                "    if lettre in etat[\"mot\"]:\n"
                                "        etat[\"trouvees\"].add(lettre)\n"
                                "    else:\n        etat[\"vies\"] -= 1\n    return etat\n",
                    "hints": ["Teste : if lettre in etat[\"mot\"].",
                              "Ajoute avec etat[\"trouvees\"].add(lettre).",
                              "Sinon : etat[\"vies\"] -= 1."],
                },
            ],
        },
        {
            "id": "proj-todo",
            "title": "Projet : une liste de tâches (to-do)",
            "content": """## Gérer des tâches

On construit le cœur d'une application de **liste de tâches**. Chaque
tâche est un petit dictionnaire `{"texte": ..., "fait": False}`. On code
les trois opérations de base, puis on les assemble.

Application console complète une fois les fonctions écrites (à copier
dans un fichier pour l'utiliser) :

```
taches = []
while True:
    print("\\n--- Mes tâches ---")
    for i, t in enumerate(taches):
        coche = "x" if t["fait"] else " "
        print(f"{i}. [{coche}] {t['texte']}")
    action = input("(a)jouter / (c)ocher / (q)uitter : ")
    if action == "a":
        taches.append({"texte": input("Tâche : "), "fait": False})
    elif action == "c":
        i = int(input("Numéro : "))
        taches[i]["fait"] = not taches[i]["fait"]
    elif action == "q":
        break
```

Code les trois fonctions ci-dessous (boutons **Exercice 1, 2, 3**).""",
            "exercices": [
                {
                    "prompt": "Étape 1 — ajouter(taches, texte) : ajoute une nouvelle tâche "
                              "{\"texte\": texte, \"fait\": False} à la liste et renvoie la liste.",
                    "starter": "def ajouter(taches, texte):\n    ...\n    return taches\n",
                    "check": 't = []\najouter(t, "courses")\n'
                             'assert t == [{"texte": "courses", "fait": False}]\n'
                             'ajouter(t, "sport")\n'
                             'assert len(t) == 2 and t[1]["texte"] == "sport"\n',
                    "solution": "def ajouter(taches, texte):\n"
                                "    taches.append({\"texte\": texte, \"fait\": False})\n"
                                "    return taches\n",
                    "hints": ["Crée un dictionnaire avec les clés texte et fait.",
                              "Utilise taches.append({...})."],
                },
                {
                    "prompt": "Étape 2 — basculer(taches, index) : inverse l'état « fait » "
                              "de la tâche située à cet index, puis renvoie la liste.",
                    "starter": "def basculer(taches, index):\n    ...\n    return taches\n",
                    "check": 't = [{"texte": "a", "fait": False}]\n'
                             'basculer(t, 0)\nassert t[0]["fait"] is True\n'
                             'basculer(t, 0)\nassert t[0]["fait"] is False\n',
                    "solution": "def basculer(taches, index):\n"
                                "    taches[index][\"fait\"] = not taches[index][\"fait\"]\n"
                                "    return taches\n",
                    "hints": ["Accède à la tâche : taches[index].",
                              "Inverse un booléen avec not : ... = not ..."],
                },
                {
                    "prompt": "Étape 3 — restantes(taches) : renvoie le nombre de tâches "
                              "PAS encore faites.",
                    "starter": "def restantes(taches):\n    ...\n",
                    "check": 't = [{"texte": "a", "fait": True}, {"texte": "b", "fait": False}, '
                             '{"texte": "c", "fait": False}]\n'
                             'assert restantes(t) == 2\nassert restantes([]) == 0\n',
                    "solution": "def restantes(taches):\n"
                                "    return sum(1 for t in taches if not t[\"fait\"])\n",
                    "hints": ["Compte les tâches dont \"fait\" est False.",
                              "sum(1 for t in taches if not t[\"fait\"])."],
                },
            ],
        },
        {
            "id": "proj-blocnotes",
            "title": "Projet : un mini bloc-notes (Tkinter)",
            "content": """## Un éditeur de texte avec menu

On crée un vrai **bloc-notes** : une zone de texte, et des boutons pour
ouvrir et enregistrer un fichier. Copie ce code dans un fichier et
lance-le pour obtenir une application fonctionnelle :

```
import tkinter as tk
from tkinter import filedialog

fenetre = tk.Tk()
fenetre.title("Bloc-notes")

zone = tk.Text(fenetre, width=60, height=20)
zone.pack()

def enregistrer():
    chemin = filedialog.asksaveasfilename(defaultextension=".txt")
    if chemin:
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(zone.get("1.0", "end-1c"))

def ouvrir():
    chemin = filedialog.askopenfilename()
    if chemin:
        with open(chemin, "r", encoding="utf-8") as f:
            zone.delete("1.0", "end")
            zone.insert("1.0", f.read())

barre = tk.Frame(fenetre)
barre.pack()
tk.Button(barre, text="Ouvrir", command=ouvrir).pack(side="left")
tk.Button(barre, text="Enregistrer", command=enregistrer).pack(side="left")

fenetre.mainloop()
```

Ajoutons-lui des **outils de texte**. Code les trois fonctions ci-dessous
(elles alimenteraient un compteur et un « rechercher/remplacer »).""",
            "exercices": [
                {
                    "prompt": "Étape 1 — compter_mots(texte) : renvoie le nombre de mots "
                              "(séparés par des espaces).",
                    "starter": "def compter_mots(texte):\n    ...\n",
                    "check": 'assert compter_mots("bonjour le monde") == 3\n'
                             'assert compter_mots("") == 0\n'
                             'assert compter_mots("  a   b ") == 2\n',
                    "solution": "def compter_mots(texte):\n    return len(texte.split())\n",
                    "hints": ["texte.split() découpe sur les espaces.",
                              "len(...) compte les morceaux obtenus."],
                },
                {
                    "prompt": "Étape 2 — compter_lignes(texte) : renvoie le nombre de lignes "
                              "(0 si le texte est vide).",
                    "starter": "def compter_lignes(texte):\n    ...\n",
                    "check": 'assert compter_lignes("a\\nb\\nc") == 3\n'
                             'assert compter_lignes("seule") == 1\n'
                             'assert compter_lignes("") == 0\n',
                    "solution": "def compter_lignes(texte):\n"
                                "    if texte == \"\":\n        return 0\n"
                                "    return texte.count(\"\\n\") + 1\n",
                    "hints": ["Le nombre de lignes = nombre de retours à la ligne + 1.",
                              "Attention au cas du texte vide qui doit renvoyer 0.",
                              "texte.count(\"\\n\") compte les retours à la ligne."],
                },
                {
                    "prompt": "Étape 3 — remplacer(texte, ancien, nouveau) : renvoie le texte "
                              "où toutes les occurrences de « ancien » sont remplacées par "
                              "« nouveau » (c'est la fonction Rechercher/Remplacer).",
                    "starter": "def remplacer(texte, ancien, nouveau):\n    ...\n",
                    "check": 'assert remplacer("le chat le chien", "le", "la") == "la chat la chien"\n'
                             'assert remplacer("aaa", "a", "b") == "bbb"\n',
                    "solution": "def remplacer(texte, ancien, nouveau):\n"
                                "    return texte.replace(ancien, nouveau)\n",
                    "hints": ["Les chaînes ont une méthode .replace(ancien, nouveau).",
                              "return texte.replace(ancien, nouveau)"],
                },
            ],
        },
        {
            "id": "proj-devises",
            "title": "Projet : convertisseur de devises",
            "content": """## Convertir des montants

On construit le cœur d'un **convertisseur de devises** : une fonction de
conversion, un affichage propre, et le taux inverse. Exemple d'appli
console (à copier dans un fichier) :

```
TAUX = {"USD": 1.08, "GBP": 0.85}   # 1 EUR = ... devise

montant = float(input("Montant en euros : "))
devise = input("Devise (USD/GBP) : ")
resultat = round(montant * TAUX[devise], 2)
print(f"{montant} EUR = {resultat:.2f} {devise}")
```

Code les trois briques ci-dessous (boutons **Exercice 1, 2, 3**).""",
            "exercices": [
                {
                    "prompt": "Étape 1 — convertir(montant, taux) : renvoie montant × taux, "
                              "arrondi à 2 décimales.",
                    "starter": "def convertir(montant, taux):\n    ...\n",
                    "check": "assert convertir(100, 1.08) == 108.0\n"
                             "assert convertir(50, 0.85) == 42.5\n"
                             "assert convertir(3, 0.3333) == 1.0\n",
                    "solution": "def convertir(montant, taux):\n    return round(montant * taux, 2)\n",
                    "hints": ["Multiplie montant par taux.",
                              "round(..., 2) arrondit à 2 décimales."],
                },
                {
                    "prompt": "Étape 2 — formater(montant, devise) : renvoie une chaîne "
                              "avec 2 décimales et la devise. Ex. : formater(12.5, \"USD\") "
                              "→ \"12.50 USD\".",
                    "starter": "def formater(montant, devise):\n    ...\n",
                    "check": 'assert formater(12.5, "USD") == "12.50 USD"\n'
                             'assert formater(100, "GBP") == "100.00 GBP"\n',
                    "solution": 'def formater(montant, devise):\n    return f"{montant:.2f} {devise}"\n',
                    "hints": ["Une f-string avec un format : f\"{montant:.2f}\".",
                              "Ajoute un espace puis la devise."],
                },
                {
                    "prompt": "Étape 3 — taux_inverse(taux) : renvoie le taux inverse "
                              "(1 / taux), arrondi à 4 décimales.",
                    "starter": "def taux_inverse(taux):\n    ...\n",
                    "check": "assert taux_inverse(1.25) == 0.8\n"
                             "assert taux_inverse(2) == 0.5\n",
                    "solution": "def taux_inverse(taux):\n    return round(1 / taux, 4)\n",
                    "hints": ["L'inverse de taux, c'est 1 / taux.",
                              "round(1 / taux, 4)"],
                },
            ],
        },
        {
            "id": "proj-vie",
            "title": "Projet : le Jeu de la vie de Conway",
            "content": """## Des cellules qui vivent et meurent

Le **Jeu de la vie** simule une grille de cellules (1 = vivante,
0 = morte) qui évolue selon des règles simples, en fonction du nombre de
voisines vivantes (parmi les 8 cases autour) :

- une cellule **vivante** survit si elle a **2 ou 3** voisines, sinon elle meurt ;
- une cellule **morte** naît si elle a **exactement 3** voisines.

Affichage console d'une génération (à copier dans un fichier) :

```
def afficher(grille):
    for ligne in grille:
        print("".join("█" if c else " " for c in ligne))
```

On code la simulation étape par étape (boutons **Exercice 1, 2, 3**).""",
            "exercices": [
                {
                    "prompt": "Étape 1 — compter_voisins(grille, i, j) : compte les voisines "
                              "vivantes (1) parmi les 8 cases entourant (i, j). Attention aux "
                              "bords (ne pas sortir de la grille).",
                    "starter": "def compter_voisins(grille, i, j):\n    ...\n",
                    "check": "g = [[0,1,0],[0,1,0],[0,1,0]]\n"
                             "assert compter_voisins(g, 1, 1) == 2\n"
                             "assert compter_voisins(g, 0, 1) == 1\n"
                             "assert compter_voisins(g, 0, 0) == 2\n",
                    "solution": "def compter_voisins(grille, i, j):\n"
                                "    h, w = len(grille), len(grille[0])\n    total = 0\n"
                                "    for di in (-1, 0, 1):\n        for dj in (-1, 0, 1):\n"
                                "            if di == 0 and dj == 0:\n                continue\n"
                                "            ni, nj = i + di, j + dj\n"
                                "            if 0 <= ni < h and 0 <= nj < w:\n"
                                "                total += grille[ni][nj]\n    return total\n",
                    "hints": ["Parcours les décalages di, dj dans (-1, 0, 1).",
                              "Ignore (0, 0) — c'est la cellule elle-même.",
                              "Vérifie que ni et nj restent dans la grille avant d'ajouter."],
                },
                {
                    "prompt": "Étape 2 — prochaine_cellule(vivante, voisins) : applique les "
                              "règles. Renvoie 1 (vivante) ou 0 (morte) à la génération suivante. "
                              "vivante est 1 ou 0.",
                    "starter": "def prochaine_cellule(vivante, voisins):\n    ...\n",
                    "check": "assert prochaine_cellule(1, 2) == 1\n"
                             "assert prochaine_cellule(1, 3) == 1\n"
                             "assert prochaine_cellule(1, 1) == 0\n"
                             "assert prochaine_cellule(1, 4) == 0\n"
                             "assert prochaine_cellule(0, 3) == 1\n"
                             "assert prochaine_cellule(0, 2) == 0\n",
                    "solution": "def prochaine_cellule(vivante, voisins):\n"
                                "    if vivante:\n        return 1 if voisins in (2, 3) else 0\n"
                                "    return 1 if voisins == 3 else 0\n",
                    "hints": ["Si vivante : survit avec 2 ou 3 voisins.",
                              "Si morte : naît avec exactement 3 voisins."],
                },
                {
                    "prompt": "Étape 3 — etape(grille) : renvoie la NOUVELLE grille après une "
                              "génération (sans modifier l'ancienne). Le clignotant vertical "
                              "doit devenir horizontal.",
                    "starter": "def etape(grille):\n    ...\n",
                    "check": "g = [[0,0,0],[1,1,1],[0,0,0]]\n"
                             "attendu = [[0,1,0],[0,1,0],[0,1,0]]\n"
                             "assert etape(g) == attendu, etape(g)\n",
                    "solution": "def etape(grille):\n"
                                "    h, w = len(grille), len(grille[0])\n"
                                "    def voisins(i, j):\n        t = 0\n"
                                "        for di in (-1, 0, 1):\n            for dj in (-1, 0, 1):\n"
                                "                if di or dj:\n"
                                "                    ni, nj = i + di, j + dj\n"
                                "                    if 0 <= ni < h and 0 <= nj < w:\n"
                                "                        t += grille[ni][nj]\n        return t\n"
                                "    nouvelle = []\n    for i in range(h):\n        ligne = []\n"
                                "        for j in range(w):\n            v = voisins(i, j)\n"
                                "            vivante = grille[i][j]\n"
                                "            if vivante:\n                ligne.append(1 if v in (2, 3) else 0)\n"
                                "            else:\n                ligne.append(1 if v == 3 else 0)\n"
                                "        nouvelle.append(ligne)\n    return nouvelle\n",
                    "hints": ["Construis une NOUVELLE grille, ne modifie pas l'ancienne.",
                              "Pour chaque case : compte les voisins, applique les règles.",
                              "Survit (2-3 voisins) / naît (exactement 3)."],
                },
            ],
        },
        {
            "id": "proj-motdepasse",
            "title": "Projet : sécuriser un mot de passe",
            "content": """## Ne jamais stocker un mot de passe en clair

Une application sérieuse ne conserve **jamais** les mots de passe en
clair. On stocke une **empreinte** (hash) impossible à inverser. La
bonne méthode : `pbkdf2_hmac` (dans `hashlib`), avec un **sel** (une
valeur aléatoire propre à chaque utilisateur) et de nombreuses
itérations, ce qui ralentit les attaques.

```
import hashlib, os

sel = os.urandom(16)               # sel aléatoire, stocké à côté de l'empreinte
empreinte = hashlib.pbkdf2_hmac("sha256", "secret".encode(), sel, 100000)
print(empreinte.hex())
```

Pour vérifier un mot de passe, on rehache la saisie avec le **même sel**
et on compare les empreintes. On code ça, plus un petit contrôle de
robustesse.""",
            "exercices": [
                {
                    "prompt": "Étape 1 — hacher(mot_de_passe, sel) : renvoie l'empreinte "
                              "hexadécimale via pbkdf2_hmac('sha256', ..., sel, 100000). "
                              "mot_de_passe est une chaîne, sel des bytes.",
                    "starter": "import hashlib\n\ndef hacher(mot_de_passe, sel):\n    ...\n",
                    "check": "import hashlib\nsel = b'0123456789abcdef'\n"
                             "h1 = hacher('secret', sel)\nh2 = hacher('secret', sel)\n"
                             "assert isinstance(h1, str) and h1 == h2\n"
                             "assert hacher('autre', sel) != h1\n"
                             "attendu = hashlib.pbkdf2_hmac('sha256', b'secret', sel, 100000).hex()\n"
                             "assert h1 == attendu\n",
                    "solution": "import hashlib\n\ndef hacher(mot_de_passe, sel):\n"
                                "    return hashlib.pbkdf2_hmac('sha256', mot_de_passe.encode(), sel, 100000).hex()\n",
                    "hints": ["Encode le mot de passe en bytes avec .encode().",
                              "hashlib.pbkdf2_hmac('sha256', ..., sel, 100000).hex()"],
                },
                {
                    "prompt": "Étape 2 — verifier(mot_de_passe, sel, empreinte) : renvoie True "
                              "si le mot de passe correspond à l'empreinte (en le rehachant).",
                    "starter": "import hashlib\n\ndef verifier(mot_de_passe, sel, empreinte):\n    ...\n",
                    "check": "import hashlib\nsel = b'0123456789abcdef'\n"
                             "emp = hashlib.pbkdf2_hmac('sha256', b'secret', sel, 100000).hex()\n"
                             "assert verifier('secret', sel, emp) is True\n"
                             "assert verifier('faux', sel, emp) is False\n",
                    "solution": "import hashlib\n\ndef verifier(mot_de_passe, sel, empreinte):\n"
                                "    calc = hashlib.pbkdf2_hmac('sha256', mot_de_passe.encode(), sel, 100000).hex()\n"
                                "    return calc == empreinte\n",
                    "hints": ["Rehache le mot de passe avec le même sel.",
                              "Compare l'empreinte calculée à celle fournie."],
                },
                {
                    "prompt": "Étape 3 — est_robuste(mot_de_passe) : renvoie True si le mot de "
                              "passe fait au moins 8 caractères ET contient au moins un chiffre "
                              "ET au moins une lettre.",
                    "starter": "def est_robuste(mot_de_passe):\n    ...\n",
                    "check": "assert est_robuste('abcd1234') is True\n"
                             "assert est_robuste('court1') is False\n"
                             "assert est_robuste('quesdeslettres') is False\n"
                             "assert est_robuste('12345678') is False\n",
                    "solution": "def est_robuste(mot_de_passe):\n"
                                "    a_chiffre = any(c.isdigit() for c in mot_de_passe)\n"
                                "    a_lettre = any(c.isalpha() for c in mot_de_passe)\n"
                                "    return len(mot_de_passe) >= 8 and a_chiffre and a_lettre\n",
                    "hints": ["any(c.isdigit() for c in mdp) teste la présence d'un chiffre.",
                              "Combine les trois conditions avec and."],
                },
            ],
        },
    ],
}
