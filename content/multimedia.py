"""Parcours 19 — Traitement d'Images & Audio."""

LEVEL = {
    "id": "multimedia",
    "title": "19 · Traitement d'Images & Audio",
    "lessons": [
        {
            "id": "med-01",
            "title": "La structure d'un pixel RGB",
            "content": """## Comment est codée une couleur numérique ?

Sur un écran, chaque pixel est composé de trois sous-pixels lumineux :
- **R** : Rouge (0 à 255)
- **G** : Vert (0 à 255)
- **B** : Bleu (0 à 255)

Par exemple :
- `(255, 0, 0)` = Rouge pur
- `(255, 255, 255)` = Blanc
- `(0, 0, 0)` = Noir
- `(128, 128, 128)` = Gris moyen

Pour **inverser** une couleur (effet négatif photo), on soustrait chaque
composante à 255 : `255 - r`, `255 - g`, `255 - b`.

## À toi

Écris `inverser_pixel(r: int, g: int, b: int) -> tuple[int, int, int]` qui
renvoie le pixel inversé en couleur négative.""",
            "starter": "def inverser_pixel(r: int, g: int, b: int) -> tuple[int, int, int]:\n    ...\n",
            "check": "assert inverser_pixel(255, 0, 100) == (0, 255, 155)\n"
                     "assert inverser_pixel(0, 0, 0) == (255, 255, 255)\n"
                     "assert inverser_pixel(128, 128, 128) == (127, 127, 127)\n",
            "solution": "def inverser_pixel(r: int, g: int, b: int) -> tuple[int, int, int]:\n    return (255 - r, 255 - g, 255 - b)\n",
            "hints": [
                "Calcule 255 - r, 255 - g, 255 - b.",
                "Renvoie un tuple (255 - r, 255 - g, 255 - b)."
            ],
        },
        {
            "id": "med-02",
            "title": "Générer une image en pur Python (Format PPM)",
            "content": """## Le format Netpbm (PPM P3)

Saviez-vous qu'on peut créer un vrai fichier image sans installer aucune
bibliothèque comme Pillow ? Le format standard **PPM (Portable Pixmap)**
est du simple texte ASCII !

Structure d'un fichier PPM :
```text
P3
# largeur hauteur
2 2
# valeur maximale de couleur
255
# triplets R G B de chaque pixel
255 0 0    0 255 0
0 0 255    255 255 0
```

## À toi

Écris `generer_ppm_uni(largeur: int, hauteur: int, couleur: tuple[int, int, int]) -> str`
qui génère et renvoie le texte complet d'une image PPM unicolore.""",
            "starter": "def generer_ppm_uni(largeur: int, hauteur: int, couleur: tuple[int, int, int]) -> str:\n    ...\n",
            "check": "ppm = generer_ppm_uni(2, 2, (255, 0, 0))\n"
                     "assert ppm.startswith('P3\\n2 2\\n255\\n')\n"
                     "assert '255 0 0' in ppm\n",
            "solution": "def generer_ppm_uni(largeur: int, hauteur: int, couleur: tuple[int, int, int]) -> str:\n"
                        "    r, g, b = couleur\n"
                        "    lignes = [f'P3\\n{largeur} {hauteur}\\n255']\n"
                        "    pixel_str = f'{r} {g} {b}'\n"
                        "    for _ in range(hauteur):\n"
                        "        lignes.append(' '.join([pixel_str] * largeur))\n"
                        "    return '\\n'.join(lignes) + '\\n'\n",
            "hints": [
                "Commence par l'en-tête f'P3\\n{largeur} {hauteur}\\n255'.",
                "Répète le triplet de couleur largeur * hauteur fois."
            ],
        },
        {
            "id": "med-03",
            "title": "Filtres d'image : Niveaux de gris",
            "content": r"""## La formule de luminance

L'œil humain est beaucoup plus sensible à la lumière verte qu'au bleu ou au
rouge. Pour convertir une image couleur en noir et blanc de manière réaliste,
on utilise la formule de luminance normalisée (ITU-R BT.601) :
\[ Y = 0.299 \times R + 0.587 \times G + 0.114 \times B \]

L'arrondi de \(Y\) donne l'intensité du gris (de 0 à 255).

## À toi

Écris `pixel_vers_gris(r: int, g: int, b: int) -> tuple[int, int, int]` qui
calcule la luminance arrondie avec `round(0.299 * r + 0.587 * g + 0.114 * b)`
et renvoie le triplet de gris `(gris, gris, gris)`.""",
            "starter": "def pixel_vers_gris(r: int, g: int, b: int) -> tuple[int, int, int]:\n    ...\n",
            "check": "assert pixel_vers_gris(255, 255, 255) == (255, 255, 255)\n"
                     "assert pixel_vers_gris(0, 0, 0) == (0, 0, 0)\n"
                     "assert pixel_vers_gris(255, 0, 0) == (76, 76, 76)\n",
            "solution": "def pixel_vers_gris(r: int, g: int, b: int) -> tuple[int, int, int]:\n"
                        "    val = round(0.299 * r + 0.587 * g + 0.114 * b)\n"
                        "    return (val, val, val)\n",
            "hints": [
                "Calcule val = round(0.299 * r + 0.587 * g + 0.114 * b).",
                "Renvoie (val, val, val)."
            ],
        },
        {
            "id": "med-04",
            "title": "Générer un motif de damier",
            "content": """## Les coordonnées de matrice (ligne, colonne)

Une image matricielle est une grille 2D. Pour dessiner un damier alternant
deux couleurs (comme sur un échiquier), on observe la parité de la somme des
coordonnées :
`si (ligne + colonne) % 2 == 0 -> couleur 1 sinon couleur 2`

## À toi

Écris `generer_grille_damier(taille: int, c1: tuple, c2: tuple) -> list[list[tuple]]`
qui renvoie une matrice 2D carrée de dimensions `taille x taille` contenant
les couleurs `c1` et `c2` alternées selon la parité de `(i + j)`.""",
            "starter": "def generer_grille_damier(taille: int, c1: tuple, c2: tuple) -> list[list[tuple]]:\n    ...\n",
            "check": "noir, blanc = (0, 0, 0), (255, 255, 255)\n"
                     "d = generer_grille_damier(2, noir, blanc)\n"
                     "assert d == [[noir, blanc], [blanc, noir]]\n",
            "solution": "def generer_grille_damier(taille: int, c1: tuple, c2: tuple) -> list[list[tuple]]:\n"
                        "    return [[c1 if (i + j) % 2 == 0 else c2 for j in range(taille)] for i in range(taille)]\n",
            "hints": [
                "Utilise deux boucles for imbriquées pour i et j de 0 à taille - 1.",
                "c1 si (i + j) % 2 == 0 sinon c2."
            ],
        },
        {
            "id": "med-05",
            "title": "Synthèse sonore : Échantillonner une onde",
            "content": r"""## Le son numérique et les ondes sinusoïdales

Un son est une vibration de l'air. Une note pure (ex: le La 440 Hz) est une
onde sinusoïdale de fréquence \(f\) :
\[ s(t) = A \times \sin(2 \pi f t) \]

Pour numériser ce son à une cadence d'échantillonnage de 44100 Hz (qualité CD),
on prélève 44100 valeurs de \(t\) par seconde :

```python
import math

frequence = 440.0   # La 440
taux = 44100
duree = 1.0         # 1 seconde
amplitude = 32767   # amplitude max en 16 bits signés

echantillons = [
    int(amplitude * math.sin(2 * math.pi * frequence * (i / taux)))
    for i in range(int(taux * duree))
]
```

## À toi

Écris `echantillonner_sinus(frequence: float, duree_sec: float, taux=44100, amplitude=10000) -> list[int]`
qui calcule la liste des entiers d'échantillonnage pour la fréquence et durée données.""",
            "starter": "import math\n\ndef echantillonner_sinus(frequence: float, duree_sec: float, taux=44100, amplitude=10000) -> list[int]:\n    ...\n",
            "check": "ech = echantillonner_sinus(440.0, 0.01, 1000, 1000)\n"
                     "assert len(ech) == 10\n"
                     "assert isinstance(ech[0], int)\n"
                     "assert ech[0] == 0  # sin(0) == 0\n",
            "solution": "import math\n\ndef echantillonner_sinus(frequence: float, duree_sec: float, taux=44100, amplitude=10000) -> list[int]:\n"
                        "    nb_ech = int(taux * duree_sec)\n"
                        "    return [int(amplitude * math.sin(2 * math.pi * frequence * (i / taux))) for i in range(nb_ech)]\n",
            "hints": [
                "Le nombre total d'échantillons est int(taux * duree_sec).",
                "Pour chaque i, t = i / taux et calcule int(amplitude * math.sin(2 * math.pi * frequence * t))."
            ],
        },
        {
            "id": "med-06",
            "title": "Programmer une mélodie",
            "content": """## Enchaîner des notes musicales

Chaque note musicale correspond à une fréquence physique précise :
- **Do (C4)** : ~261.63 Hz
- **Ré (D4)** : ~293.66 Hz
- **Mi (E4)** : ~329.63 Hz
- **Fa (F4)** : ~349.23 Hz
- **Sol (G4)** : ~392.00 Hz
- **La (A4)** : ~440.00 Hz
- **Si (B4)** : ~493.88 Hz

Une partition peut être représentée par une suite de tuples `(frequence, duree_sec)`.

## À toi

Écris `concatener_partition(partition: list[tuple[float, float]], taux=1000) -> list[int]`
qui prend une liste de notes `(freq, duree)` et renvoie la séquence globale
concaténée de tous les échantillons générés (avec amplitude = 10000).""",
            "starter": "import math\n\ndef concatener_partition(partition: list[tuple[float, float]], taux=1000) -> list[int]:\n    ...\n",
            "check": "part = [(440.0, 0.01), (880.0, 0.01)]\n"
                     "res = concatener_partition(part, 1000)\n"
                     "assert len(res) == 20\n",
            "solution": "import math\n\ndef concatener_partition(partition: list[tuple[float, float]], taux=1000) -> list[int]:\n"
                        "    resultat = []\n"
                        "    for freq, duree in partition:\n"
                        "        nb = int(taux * duree)\n"
                        "        for i in range(nb):\n"
                        "            resultat.append(int(10000 * math.sin(2 * math.pi * freq * (i / taux))))\n"
                        "    return resultat\n",
            "hints": [
                "Parcours chaque couple (freq, duree) dans partition.",
                "Génère les échantillons de chaque note et ajoute-les au résultat."
            ],
        },
        {
            "id": "qz-med",
            "type": "quiz",
            "title": "Quiz — Images & Audio",
            "question": "Quelle est la particularité du format d'image Netpbm (PPM P3) ?",
            "options": [
                "Il utilise une compression vectorielle sans perte propriétaire.",
                "C'est un format de texte ASCII simple lisible et éditable avec un simple éditeur de texte.",
                "Il nécessite obligatoirement l'installation de la bibliothèque externe Pillow.",
                "Il ne peut enregistrer que des images monochromes noir et blanc."
            ],
            "answer": 1,
            "explanation": "Le format PPM (P3) est du texte brut contenant un en-tête simple suivi des triplets RGB en décimal, ce qui permet de créer des images sans aucune dépendance binaire externe."
        }
    ]
}
