"""Parcours — Entraînement : débogage et exercices à trous.

Illustre quatre façons de travailler autrement que par la seule écriture :
- mode "debug"   : le starter contient un bug à corriger ;
- mode "trous"   : le starter contient des ____ à compléter ;
- type "predire" : prévoir la sortie AVANT d'exécuter ;
- type "ordre"   : remettre dans l'ordre des lignes mélangées.
"""

LEVEL = {
    "id": "entrainement",
    "title": "15 · Entraînement (débogage & trous)",
    "lessons": [
        # ---------------------------------------------------------- DÉBOGAGE
        {
            "id": "dbg-01",
            "title": "Débogue : la borne oubliée",
            "mode": "debug",
            "content": """## Lire un code, trouver l'erreur

Savoir **corriger** du code est aussi important que l'écrire. Ici, la
fonction devrait additionner tous les entiers de 1 à `n` inclus… mais
elle se trompe d'un cran. Trouve le bug et corrige-le.

Indice de méthode : essaie `somme_jusqua(5)` avec « Exécuter », compare
au résultat attendu (15), et regarde la borne de la boucle.""",
            "starter": "def somme_jusqua(n):\n    total = 0\n    for i in range(1, n):\n"
                       "        total = total + i\n    return total\n",
            "check": "assert somme_jusqua(5) == 15\nassert somme_jusqua(1) == 1\n"
                     "assert somme_jusqua(10) == 55\n",
            "solution": "def somme_jusqua(n):\n    total = 0\n    for i in range(1, n + 1):\n"
                        "        total = total + i\n    return total\n",
            "hints": ["range(1, n) s'arrête à n-1 : la dernière valeur manque.",
                      "Il faut aller jusqu'à n inclus : range(1, n + 1)."],
        },
        {
            "id": "dbg-02",
            "title": "Débogue : la condition inversée",
            "mode": "debug",
            "content": """## Une logique à l'envers

`est_pair(n)` doit renvoyer `True` quand `n` est pair. Pourtant elle
répond le contraire. Repère la comparaison fautive et corrige-la.""",
            "starter": "def est_pair(n):\n    return n % 2 == 1\n",
            "check": "assert est_pair(4) is True\nassert est_pair(3) is False\n"
                     "assert est_pair(0) is True\n",
            "solution": "def est_pair(n):\n    return n % 2 == 0\n",
            "hints": ["n % 2 vaut 0 pour un nombre pair, 1 pour un impair.",
                      "Compare donc le reste à 0, pas à 1."],
        },
        {
            "id": "dbg-03",
            "title": "Débogue : l'indice qui dépasse",
            "mode": "debug",
            "content": """## Quand Python lève une erreur

`dernier(liste)` doit renvoyer le **dernier** élément. Mais l'exécution
plante avec une `IndexError`. Lis le message d'erreur (clique
« Exécuter ») : il te dira que l'indice est hors limites. Corrige le
calcul de l'indice.

Rappel : les indices d'une liste vont de 0 à `len(liste) - 1`.""",
            "starter": "def dernier(liste):\n    return liste[len(liste)]\n",
            "check": "assert dernier([1, 2, 3]) == 3\nassert dernier(['a']) == 'a'\n"
                     "assert dernier([10, 20]) == 20\n",
            "solution": "def dernier(liste):\n    return liste[len(liste) - 1]\n",
            "hints": ["Le dernier indice valide est len(liste) - 1.",
                      "Tu peux aussi écrire liste[-1]."],
        },
        # ------------------------------------------------------------- TROUS
        {
            "id": "tro-01",
            "title": "Complète : la f-string",
            "mode": "trous",
            "content": """## Remplir les blancs

Parfois, presque tout est écrit : il ne manque qu'un détail. Remplace
les `____` pour que la fonction renvoie la bonne salutation.

Exemple attendu : `saluer("Ada")` doit donner `"Bonjour Ada !"`.""",
            "starter": 'def saluer(nom):\n    return f"Bonjour {____} !"\n',
            "check": 'assert saluer("Ada") == "Bonjour Ada !"\n'
                     'assert saluer("Sam") == "Bonjour Sam !"\n',
            "solution": 'def saluer(nom):\n    return f"Bonjour {nom} !"\n',
            "hints": ["Dans une f-string, ce qui est entre { } est évalué.",
                      "Mets le paramètre nom entre les accolades."],
        },
        {
            "id": "tro-02",
            "title": "Complète : l'accumulateur",
            "mode": "trous",
            "content": """## L'opérateur manquant

La fonction additionne tous les nombres d'une liste. Remplace le `____`
par le bon opérateur pour que le total se construise correctement.""",
            "starter": "def somme(nombres):\n    total = 0\n    for n in nombres:\n"
                       "        total = total ____ n\n    return total\n",
            "check": "assert somme([1, 2, 3]) == 6\nassert somme([]) == 0\n"
                     "assert somme([10, -4]) == 6\n",
            "solution": "def somme(nombres):\n    total = 0\n    for n in nombres:\n"
                        "        total = total + n\n    return total\n",
            "hints": ["On veut ajouter chaque nombre au total.",
                      "L'opérateur d'addition est +."],
        },
        {
            "id": "tro-03",
            "title": "Complète : la comparaison",
            "mode": "trous",
            "content": """## La bonne condition

`mention(note)` renvoie `"réussi"` si la note est supérieure ou égale à
10, sinon `"échec"`. Remplace le `____` par le bon opérateur de
comparaison (attention : 10 doit compter comme réussi).""",
            "starter": 'def mention(note):\n    if note ____ 10:\n        return "réussi"\n'
                       '    return "échec"\n',
            "check": 'assert mention(12) == "réussi"\nassert mention(8) == "échec"\n'
                     'assert mention(10) == "réussi"\n',
            "solution": 'def mention(note):\n    if note >= 10:\n        return "réussi"\n'
                        '    return "échec"\n',
            "hints": ["« supérieur ou égal » se note >=.",
                      "Avec >, la note 10 serait refusée à tort : utilise >=."],
        },
        # ------------------------------------------------- PRÉDIS LA SORTIE
        {
            "id": "pre-01",
            "type": "predire",
            "title": "Prédis : plus n'est pas toujours additionner",
            "content": """## Lire avant d'exécuter

Le moyen le plus sûr de progresser est de **prévoir** ce qu'un programme
va faire, puis de vérifier. Si ta prédiction est fausse, tu viens
d'apprendre quelque chose de précis.

Ici, le signe `+` apparaît trois fois — mais ne fait pas la même chose
selon ce qu'on lui donne.""",
            "code": "print(2 + 3)\nprint('2' + '3')\nprint('2' * 3)\n",
            "explanation": (
                "Entre guillemets, « 2 » et « 3 » sont du TEXTE : « + » les "
                "colle bout à bout (23) et « * » répète (222). Sans "
                "guillemets, ce sont des nombres, et « + » additionne (5)."
            ),
        },
        {
            "id": "pre-02",
            "type": "predire",
            "title": "Prédis : la boucle qui ne change rien",
            "content": """## Un piège très courant

Cette boucle a l'air de multiplier chaque nombre par 10. Regarde bien ce
qui est affiché **à la fin**, et demande-toi ce que `n` représente
vraiment à l'intérieur de la boucle.""",
            "code": (
                "nombres = [1, 2, 3]\n"
                "for n in nombres:\n"
                "    n = n * 10\n"
                "print(nombres)\n"
            ),
            "explanation": (
                "`n` est une COPIE de la valeur, pas la case de la liste : la "
                "modifier ne touche pas `nombres`. Pour changer la liste, il "
                "faut écrire dedans, par exemple avec `nombres[i] = ...`."
            ),
        },
        # --------------------------------------------- REMETS DANS L'ORDRE
        {
            "id": "ord-01",
            "type": "ordre",
            "title": "Remets dans l'ordre : additionner une liste",
            "content": """## Retrouver la structure

Les lignes d'un programme correct ont été mélangées. Remets-les dans le
bon ordre pour qu'il affiche la somme des nombres.

Réfléchis à ce qui doit exister **avant** d'être utilisé : on ne peut pas
ajouter à un total qui n'a pas encore été créé.""",
            "lignes": [
                "total = 0",
                "for nombre in [4, 7, 2]:",
                "    total = total + nombre",
                "print(total)",
            ],
            "expected_output": "13",
        },
        {
            "id": "ord-02",
            "type": "ordre",
            "title": "Remets dans l'ordre : une fonction avec condition",
            "content": """## L'ordre d'une fonction

Ici l'indentation te donne des indices : les lignes décalées sont
**à l'intérieur** de quelque chose. Une fonction doit aussi être définie
avant d'être appelée.""",
            "lignes": [
                "def etiquette(age):",
                "    if age >= 18:",
                "        return 'majeur'",
                "    return 'mineur'",
                "print(etiquette(20))",
            ],
            "expected_output": "majeur",
        },
    ],
}
