"""Parcours 22 — Architecture & Jeux Vidéo 2D."""

LEVEL = {
    "id": "jeux_video",
    "title": "22 · Architecture & Jeux Vidéo 2D",
    "lessons": [
        {
            "id": "gam-01",
            "title": "La boucle de jeu & Delta Time",
            "content": r"""## Le cœur d'un jeu vidéo : la Game Loop

Un jeu vidéo s'exécute à l'intérieur d'une boucle infinie qui se répète
60 fois par seconde :
1. **Événements** : lire les touches du clavier et les clics.
2. **Mise à jour (Update)** : déplacer les personnages, calculer les collisions.
3. **Rendu (Render)** : afficher les graphismes à l'écran.

Pour que la vitesse du personnage reste constante quel que soit le taux de
rafraîchissement de l'écran (60 FPS ou 144 FPS), on multiplie la vitesse par
le temps écoulé depuis la dernière image (**Delta Time** `dt`) :
\[ \text{nouvelle\_position} = \text{position} + \text{vitesse} \times dt \]

## À toi

Écris `calculer_nouvelle_position(x: float, vx: float, dt: float) -> float` qui
calcule la nouvelle coordonnée avec `x + vx * dt`.""",
            "starter": "def calculer_nouvelle_position(x: float, vx: float, dt: float) -> float:\n    ...\n",
            "check": "assert abs(calculer_nouvelle_position(10.0, 100.0, 0.016) - 11.6) < 1e-4\n"
                     "assert calculer_nouvelle_position(0.0, -50.0, 1.0) == -50.0\n",
            "solution": "def calculer_nouvelle_position(x: float, vx: float, dt: float) -> float:\n    return x + vx * dt\n",
            "hints": [
                "Applique la formule x + vx * dt.",
                "Renvoie le résultat flottant."
            ],
        },
        {
            "id": "gam-02",
            "title": "Grille 2D et détection d'obstacles",
            "content": """## Déplacement sur un plateau de jeu

Considérons un labyrinthe 2D représenté par une liste de chaînes :
- `'.'` = case libre
- `'#'` = mur infranchissable

```python
grille = [
    "####",
    "#..#",
    "#..#",
    "####"
]
```

Si le joueur tente de se déplacer vers un mur (`'#'`) ou en dehors de la
grille, le déplacement est annulé et sa position reste inchangée.

## À toi

Écris `deplacer_joueur(grille: list[str], x: int, y: int, dx: int, dy: int) -> tuple[int, int]`
qui renvoie les nouvelles coordonnées `(nx, ny)` si la case visée est valide
et vaut `'.'`, sinon les anciennes coordonnées `(x, y)`.""",
            "starter": "def deplacer_joueur(grille: list[str], x: int, y: int, dx: int, dy: int) -> tuple[int, int]:\n    ...\n",
            "check": "g = [\n"
                     "    '####',\n"
                     "    '#. .#',\n"
                     "    '####'\n"
                     "]\n"
                     "assert deplacer_joueur(g, 1, 1, 1, 0) == (2, 1)  # case libre '.'\n"
                     "assert deplacer_joueur(g, 1, 1, -1, 0) == (1, 1) # mur '#' à gauche\n"
                     "assert deplacer_joueur(g, 1, 1, 0, -1) == (1, 1) # mur '#' en haut\n",
            "solution": "def deplacer_joueur(grille: list[str], x: int, y: int, dx: int, dy: int) -> tuple[int, int]:\n"
                        "    nx, ny = x + dx, y + dy\n"
                        "    if 0 <= ny < len(grille) and 0 <= nx < len(grille[ny]):\n"
                        "        if grille[ny][nx] != '#':\n"
                        "            return nx, ny\n"
                        "    return x, y\n",
            "hints": [
                "Calcule nx = x + dx et ny = y + dy.",
                "Vérifie que ny est dans [0, len(grille)[ et nx dans [0, len(grille[ny])[.",
                "Si la case grille[ny][nx] n'est pas '#', renvoie (nx, ny)."
            ],
        },
        {
            "id": "gam-03",
            "title": "Système d'inventaire et limite de poids",
            "content": """## Gérer un sac d'objets dans un RPG

Un sac d'aventurier contient une liste d'objets `[{"nom": "Épée", "poids": 3.5, "quantite": 1}, ...]`.
Le sac a une capacité de charge maximale (ex: 20.0 kg).

Si l'ajout d'un objet fait dépasser la capacité totale, l'opération échoue et
renvoie `False`. Sinon, elle met à jour la quantité (si l'objet est déjà présent)
ou l'ajoute, et renvoie `True`.

## À toi

Écris `ajouter_au_sac(sac: list[dict], nom: str, poids_unitaire: float, quantite: int, capacite_max=20.0) -> bool`
qui tente d'ajouter l'objet au sac et renvoie un booléen de succès.""",
            "starter": "def ajouter_au_sac(sac: list[dict], nom: str, poids_unitaire: float, quantite: int, capacite_max=20.0) -> bool:\n    ...\n",
            "check": "sac = [{'nom': 'Potion', 'poids': 0.5, 'quantite': 2}]  # poids = 1.0\n"
                     "assert ajouter_au_sac(sac, 'Epee', 5.0, 1, 20.0) is True\n"
                     "assert len(sac) == 2\n"
                     "assert ajouter_au_sac(sac, 'Enclume', 50.0, 1, 20.0) is False\n"
                     "assert len(sac) == 2\n",
            "solution": "def ajouter_au_sac(sac: list[dict], nom: str, poids_unitaire: float, quantite: int, capacite_max=20.0) -> bool:\n"
                        "    poids_actuel = sum(item['poids'] * item['quantite'] for item in sac)\n"
                        "    poids_suppl = poids_unitaire * quantite\n"
                        "    if poids_actuel + poids_suppl > capacite_max:\n"
                        "        return False\n"
                        "    for item in sac:\n"
                        "        if item['nom'] == nom:\n"
                        "            item['quantite'] += quantite\n"
                        "            return True\n"
                        "    sac.append({'nom': nom, 'poids': poids_unitaire, 'quantite': quantite})\n"
                        "    return True\n",
            "hints": [
                "Calcule le poids total actuel avec sum(item['poids'] * item['quantite']).",
                "Si actuel + nouveau > capacite_max, renvoie False.",
                "Sinon cherche si l'item existe déjà pour incrémenter sa quantité, ou append un nouveau dict."
            ],
        },
        {
            "id": "gam-04",
            "title": "Calcul de combat au tour par tour",
            "content": r"""## Formule de dégâts avec coup critique

Dans les combats au tour par tour, les dégâts infligés dépendent de l'attaque,
de la défense de la cible et d'un multiplicateur de coup critique :
\[ \text{dégâts} = \max(1, \text{attaque} - \text{défense}) \times (\text{2 si critique sinon 1}) \]

Les points de vie de la cible ne peuvent jamais descendre en dessous de 0.

## À toi

Écris `subir_attaque(pv_actuels: int, attaque: int, defense: int, est_critique=False) -> int`
qui calcule les dégâts et renvoie les nouveaux points de vie restants de la cible.""",
            "starter": "def subir_attaque(pv_actuels: int, attaque: int, defense: int, est_critique=False) -> int:\n    ...\n",
            "check": "assert subir_attaque(100, 20, 5, False) == 85   # 20 - 5 = 15 dégâts -> 85 PV\n"
                     "assert subir_attaque(100, 20, 5, True) == 70    # 15 * 2 = 30 dégâts -> 70 PV\n"
                     "assert subir_attaque(10, 50, 0, False) == 0     # PV ne descendent pas sous 0\n"
                     "assert subir_attaque(50, 5, 20, False) == 49    # minimum 1 dégât infligé\n",
            "solution": "def subir_attaque(pv_actuels: int, attaque: int, defense: int, est_critique=False) -> int:\n"
                        "    degats = max(1, attaque - defense)\n"
                        "    if est_critique:\n        degats *= 2\n"
                        "    return max(0, pv_actuels - degats)\n",
            "hints": [
                "degats = max(1, attaque - defense)",
                "Double les dégâts si est_critique vaut True.",
                "Renvoie max(0, pv_actuels - degats)."
            ],
        },
        {
            "id": "gam-05",
            "title": "Intelligence Artificielle ennemie (Poursuite)",
            "content": r"""## Rapprocher un monstre du joueur

Une intelligence artificielle simple de poursuite compare les coordonnées du
monstre \((x_m, y_m)\) avec celles du joueur \((x_j, y_j)\) :
- Si \(x_m < x_j\), le monstre avance vers la droite (\(+1\)).
- Si \(x_m > x_j\), le monstre recule vers la gauche (\(-1\)).
- Idem sur l'axe vertical \(y\).

## À toi

Écris `pas_poursuite(monstre: tuple[int, int], joueur: tuple[int, int]) -> tuple[int, int]`
qui renvoie le vecteur de déplacement unitaire `(dx, dy)` que doit effectuer
le monstre pour se rapprocher du joueur (chaque composante vaut `-1`, `0` ou `1`).""",
            "starter": "def pas_poursuite(monstre: tuple[int, int], joueur: tuple[int, int]) -> tuple[int, int]:\n    ...\n",
            "check": "assert pas_poursuite((0, 0), (5, 3)) == (1, 1)\n"
                     "assert pas_poursuite((5, 5), (2, 5)) == (-1, 0)\n"
                     "assert pas_poursuite((3, 4), (3, 4)) == (0, 0)\n",
            "solution": "def pas_poursuite(monstre: tuple[int, int], joueur: tuple[int, int]) -> tuple[int, int]:\n"
                        "    xm, ym = monstre\n"
                        "    xj, yj = joueur\n"
                        "    dx = (1 if xj > xm else (-1 if xj < xm else 0))\n"
                        "    dy = (1 if yj > ym else (-1 if yj < ym else 0))\n"
                        "    return dx, dy\n",
            "hints": [
                "Compare xj et xm pour déterminer dx (-1, 0 ou 1).",
                "Compare yj et ym pour déterminer dy (-1, 0 ou 1)."
            ],
        },
        {
            "id": "gam-06",
            "title": "Sauvegarder et Charger une partie en JSON",
            "content": """## Sérialiser l'état du monde

Pour permettre au joueur de reprendre sa partie plus tard, on rassemble toutes
les variables d'état (position, niveau, inventaire, score) dans un dictionnaire
et on le sérialise avec `json.dumps()` / `json.loads()`.

```python
import json

partie = {
    "score": 1500,
    "position": [4, 7],
    "inventaire": ["épée", "bouclier"]
}
sauvegarde_texte = json.dumps(partie)
```

## À toi

Écris deux fonctions :
1. `sauvegarder_partie(joueur_nom: str, score: int, objets: list[str]) -> str` : renvoie la chaîne JSON formatée.
2. `charger_partie(json_str: str) -> tuple[str, int, list[str]]` : lit la chaîne JSON et renvoie le triplet `(joueur_nom, score, objets)`.""",
            "starter": "import json\n\ndef sauvegarder_partie(joueur_nom: str, score: int, objets: list[str]) -> str:\n    ...\n\ndef charger_partie(json_str: str) -> tuple[str, int, list[str]]:\n    ...\n",
            "check": "txt = sauvegarder_partie('Lancelot', 250, ['potion', 'cle'])\n"
                     "nom, score, objs = charger_partie(txt)\n"
                     "assert nom == 'Lancelot' and score == 250\n"
                     "assert objs == ['potion', 'cle']\n",
            "solution": "import json\n\ndef sauvegarder_partie(joueur_nom: str, score: int, objets: list[str]) -> str:\n"
                        "    return json.dumps({'nom': joueur_nom, 'score': score, 'objets': objets})\n\n"
                        "def charger_partie(json_str: str) -> tuple[str, int, list[str]]:\n"
                        "    d = json.loads(json_str)\n"
                        "    return d['nom'], d['score'], d['objets']\n",
            "hints": [
                "Utilise json.dumps({'nom': joueur_nom, 'score': score, 'objets': objets}).",
                "Utilise json.loads(json_str) pour extraire les trois champs."
            ],
        },
        {
            "id": "qz-gam",
            "type": "quiz",
            "title": "Quiz — Logique de Jeu Vidéo",
            "question": "Quel est le rôle du 'Delta Time' (dt) dans une boucle de jeu vidéo ?",
            "options": [
                "Rendre le jeu plus difficile au fil du temps.",
                "Garantir une vitesse de déplacement identique quel que soit le taux de rafraîchissement (FPS) de l'écran.",
                "Compresser les textures pour économiser la mémoire de la carte graphique.",
                "Calculer les dégâts magiques des sorts."
            ],
            "answer": 1,
            "explanation": "En multipliant les vitesses par le temps réel écoulé entre deux images (dt), les mouvements restent fluides et synchronisés que le jeu tourne à 30, 60 ou 144 images par seconde."
        }
    ]
}
