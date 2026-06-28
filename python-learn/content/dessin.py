"""Parcours — Dessiner avec turtle."""

LEVEL = {
    "id": "turtle",
    "title": "10 · Dessiner (turtle)",
    "lessons": [
        {
            "id": "dsn-01",
            "title": "Une tortue qui dessine",
            "content": """## Le module turtle

`turtle` (inclus dans Python) fait avancer une « tortue » qui laisse une
trace : parfait pour apprendre en dessinant. **Copie ce code dans un
fichier et lance-le** pour voir un carré se tracer :

```
import turtle

t = turtle.Turtle()
for _ in range(4):
    t.forward(100)   # avance de 100 pixels
    t.right(90)      # tourne de 90° à droite

turtle.done()        # garde la fenêtre ouverte
```

Un carré, c'est 4 côtés et 4 rotations de 90°. Pour un polygone régulier
à `n` côtés, l'angle de rotation vaut **360 / n**.

> Comme pour les fenêtres, on travaille ici la **logique** du dessin
> dans l'éditeur ; lance le code turtle dans un vrai fichier pour voir
> le résultat.

## À toi

Écris `angle_polygone(n)` qui renvoie l'angle de rotation (en degrés)
pour tracer un polygone régulier à `n` côtés.""",
            "starter": "def angle_polygone(n):\n    ...\n",
            "check": "assert angle_polygone(4) == 90\nassert angle_polygone(3) == 120\n"
                     "assert angle_polygone(6) == 60\n",
            "solution": "def angle_polygone(n):\n    return 360 / n\n",
            "hints": ["L'angle extérieur d'un polygone régulier vaut 360/n.",
                      "return 360 / n"],
        },
        {
            "id": "dsn-02",
            "title": "Avancer et tourner",
            "content": """## Les ordres de base

La tortue comprend quelques ordres essentiels :
- `forward(d)` / `backward(d)` : avancer / reculer de `d` pixels
- `right(a)` / `left(a)` : tourner de `a` degrés
- `penup()` / `pendown()` : lever / baisser le crayon (se déplacer sans tracer)
- `goto(x, y)` : aller à une position précise

```
t.penup(); t.goto(-50, 0); t.pendown()   # se positionne sans dessiner
t.forward(100)
```

On peut décrire un dessin comme une **suite d'ordres**. Représentons un
carré par une liste d'instructions `("avance", 100)` / `("tourne", 90)`.

## À toi

Écris `instructions_carre(cote)` qui renvoie la liste des ordres pour
tracer un carré : pour chacun des 4 côtés, un `("avance", cote)` suivi
d'un `("tourne", 90)`.""",
            "starter": "def instructions_carre(cote):\n    ...\n",
            "check": "r = instructions_carre(100)\n"
                     "assert r == [('avance', 100), ('tourne', 90)] * 4, r\n"
                     "assert len(instructions_carre(50)) == 8\n",
            "solution": "def instructions_carre(cote):\n"
                        "    ordres = []\n    for _ in range(4):\n"
                        "        ordres.append(('avance', cote))\n"
                        "        ordres.append(('tourne', 90))\n    return ordres\n",
            "hints": ["Boucle 4 fois.",
                      "À chaque tour, ajoute ('avance', cote) puis ('tourne', 90)."],
        },
        {
            "id": "dsn-03",
            "title": "Répéter pour créer des motifs",
            "content": """## La boucle, reine du dessin

En répétant un motif tout en tournant un peu, on obtient des figures
spectaculaires. Exemple d'une **spirale** (à lancer dans un fichier) :

```
import turtle
t = turtle.Turtle()
for i in range(1, 40):
    t.forward(i * 5)   # côté de plus en plus long
    t.right(90)
turtle.done()
```

Ici chaque côté mesure `i * 5` : 5, 10, 15, 20… La longueur grandit à
chaque tour de boucle.

## À toi

Écris `longueurs_spirale(n, pas)` qui renvoie la liste des `n` longueurs
de côté : `pas, 2*pas, 3*pas, …, n*pas`.""",
            "starter": "def longueurs_spirale(n, pas):\n    ...\n",
            "check": "assert longueurs_spirale(4, 5) == [5, 10, 15, 20]\n"
                     "assert longueurs_spirale(3, 10) == [10, 20, 30]\n",
            "solution": "def longueurs_spirale(n, pas):\n"
                        "    return [i * pas for i in range(1, n + 1)]\n",
            "hints": ["range(1, n+1) donne 1, 2, …, n.",
                      "Multiplie chaque par pas : [i * pas for i in range(1, n+1)]"],
        },
        {
            "id": "dsn-04",
            "title": "Coordonnées et déplacement",
            "content": """## Où se trouve la tortue ?

L'écran turtle est un repère : `(0, 0)` au centre, `x` vers la droite,
`y` vers le haut. Quand la tortue avance de `d` pixels avec un cap de
`a` degrés, sa nouvelle position se calcule avec la trigonométrie :

```
import math
nx = x + d * math.cos(math.radians(a))
ny = y + d * math.sin(math.radians(a))
```

`math.radians` convertit les degrés en radians (ce qu'attendent `cos` et
`sin`). À 0°, on va vers la droite ; à 90°, vers le haut.

## À toi

Écris `nouvelle_position(x, y, cap, distance)` qui renvoie le tuple
`(nx, ny)` de la nouvelle position, chaque valeur **arrondie à 3
décimales**.""",
            "starter": "import math\n\ndef nouvelle_position(x, y, cap, distance):\n    ...\n",
            "check": "assert nouvelle_position(0, 0, 0, 10) == (10.0, 0.0)\n"
                     "assert nouvelle_position(0, 0, 90, 10) == (0.0, 10.0)\n"
                     "assert nouvelle_position(5, 5, 180, 5) == (0.0, 5.0)\n",
            "solution": "import math\n\ndef nouvelle_position(x, y, cap, distance):\n"
                        "    rad = math.radians(cap)\n"
                        "    nx = round(x + distance * math.cos(rad), 3)\n"
                        "    ny = round(y + distance * math.sin(rad), 3)\n"
                        "    return (nx, ny)\n",
            "hints": ["Convertis le cap en radians avec math.radians(cap).",
                      "nx avec cos, ny avec sin, puis round(..., 3)."],
        },
        {
            "id": "dsn-05",
            "title": "Mini-projet : une rosace",
            "content": """## Composer une figure

Une **rosace** se dessine en répétant un même motif (un cercle, un
carré…) tourné régulièrement autour d'un centre. Pour `n` répétitions,
chaque motif est tourné de `360 / n` degrés de plus. **À lancer dans un
fichier** :

```
import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(12):
    t.circle(80)        # dessine un cercle
    t.right(360 / 12)   # tourne avant le suivant
turtle.done()
```

## À toi

Écris `angles_rosace(n)` qui renvoie la liste des angles d'orientation
de chaque motif : `0, 360/n, 2*360/n, …` (n valeurs).""",
            "starter": "def angles_rosace(n):\n    ...\n",
            "check": "assert angles_rosace(4) == [0.0, 90.0, 180.0, 270.0]\n"
                     "assert len(angles_rosace(12)) == 12\n",
            "solution": "def angles_rosace(n):\n"
                        "    return [i * 360 / n for i in range(n)]\n",
            "hints": ["Il y a n motifs, du n°0 au n°(n-1).",
                      "Angle du motif i : i * 360 / n."],
        },
    ],
}
