"""Niveau 1 — Débutant (version pas à pas pour grand débutant)."""

LEVEL = {
    "id": "debutant",
    "title": "1 · Débutant",
    "lessons": [
        {
            "id": "deb-00",
            "title": "Bienvenue : c'est quoi programmer ?",
            "content": """## Programmer, c'est donner des ordres

Un ordinateur est rapide mais bête : il ne fait que ce qu'on lui dit,
exactement, dans l'ordre. **Programmer**, c'est écrire une liste
d'instructions claires qu'il va exécuter une par une, de haut en bas,
comme une recette de cuisine.

Python est un langage de programmation réputé pour être **lisible** :
ses instructions ressemblent presque à de l'anglais courant. C'est pour
ça qu'on le conseille pour débuter.

## Comment ça marche ici

À droite, tu as un **éditeur** : c'est là que tu écris ton programme.
En dessous, une **console** : c'est là que l'ordinateur te répond.

- Le bouton **Exécuter** lance ton programme et affiche le résultat.
- Le bouton **Vérifier** contrôle que tu as réussi l'exercice.
- Le bouton **Solution** te montre une réponse possible si tu bloques.

Il n'y a aucun risque à se tromper : essaie, observe, recommence. C'est
exactement comme ça qu'on apprend à coder.

## Ton tout premier ordre

L'instruction `print(...)` veut dire « affiche ceci à l'écran ».
Essaie de faire afficher la phrase : `Je commence Python !`""",
            "starter": '# Écris ton premier programme ci-dessous :\nprint("...")\n',
            "expected_output": "Je commence Python !",
            "solution": 'print("Je commence Python !")\n',
        },
        {
            "id": "deb-01",
            "title": "Afficher du texte avec print()",
            "content": """## La fonction print()

`print` est l'instruction la plus utilisée pour débuter : elle
**affiche** ce qu'on lui donne entre ses parenthèses. Le texte se met
entre guillemets (`"` ou `'`).

```
print("Bonjour")
print('Ça marche aussi avec des apostrophes')
```

Chaque `print` écrit sur **sa propre ligne**. Trois `print`, trois
lignes.

```
print("Ligne 1")
print("Ligne 2")
```

On peut afficher plusieurs choses d'un coup en les séparant par des
virgules : Python ajoute une espace entre chaque.

```
print("J'ai", 3, "chats")     # affiche : J'ai 3 chats
```

## À toi

Affiche exactement ces deux lignes (une par `print`) :
```
Salut
Le monde
```""",
            "starter": '\n',
            "expected_output": "Salut\nLe monde",
            "solution": 'print("Salut")\nprint("Le monde")\n',
        },
        {
            "id": "deb-02",
            "title": "Les variables : des étiquettes",
            "content": """## Garder une valeur sous la main

Une **variable**, c'est un nom qu'on colle sur une valeur pour la
réutiliser, comme une étiquette sur une boîte. On l'écrit avec le signe
`=` (qui se lit ici « reçoit »).

```
age = 30          # la boîte "age" contient 30
prenom = "Ada"    # la boîte "prenom" contient "Ada"
```

Ensuite, il suffit de citer le nom pour récupérer la valeur :

```
print(prenom)     # affiche : Ada
print(age)        # affiche : 30
```

On peut changer le contenu d'une variable quand on veut :

```
age = 31          # maintenant "age" contient 31
```

## Les grands types de valeurs

- un **nombre entier** (`int`) : `30`
- un **nombre à virgule** (`float`) : `1.78`
- un **texte** (`str`, pour *string* = chaîne) : `"Ada"`
- un **booléen** (`bool`) : `True` (vrai) ou `False` (faux)

## À toi

Crée une variable `ville` contenant `"Toulouse"` et une variable
`habitants` contenant le nombre entier `500000`.""",
            "starter": "ville = ...\nhabitants = ...\n",
            "check": 'assert ville == "Toulouse", "ville doit contenir Toulouse"\n'
                     'assert habitants == 500000, "habitants doit valoir 500000"\n',
            "solution": 'ville = "Toulouse"\nhabitants = 500000\n',
        },
        {
            "id": "deb-03",
            "title": "Calculer avec les nombres",
            "content": """## Python sait compter

On utilise les opérateurs habituels :

- `+` addition, `-` soustraction
- `*` multiplication, `/` division
- `**` puissance (`2 ** 3` vaut 8)
- `//` division entière (le quotient), `%` modulo (le reste)

```
print(10 + 5)     # 15
print(10 / 4)     # 2.5
print(10 // 4)    # 2  (combien de fois 4 entre dans 10)
print(10 % 4)     # 2  (ce qu'il reste)
print(2 ** 10)    # 1024
```

On peut bien sûr calculer avec des variables :

```
largeur = 5
hauteur = 3
aire = largeur * hauteur
print(aire)       # 15
```

## À toi

Un article coûte `prix_ht = 80` euros hors taxes. La TVA est de 20 %.
Calcule le prix TTC dans la variable `prix_ttc` (indice : +20 %, c'est
multiplier par `1.2`).""",
            "starter": "prix_ht = 80\nprix_ttc = ...\n",
            "check": "assert abs(prix_ttc - 96) < 1e-9, 'le prix TTC devrait valoir 96'\n",
            "solution": "prix_ht = 80\nprix_ttc = prix_ht * 1.2\n",
        },
        {
            "id": "deb-04",
            "title": "Le texte : les chaînes de caractères",
            "content": """## Manipuler du texte

Une chaîne, c'est du texte entre guillemets. On peut **coller** deux
chaînes avec `+` (on appelle ça la concaténation) :

```
debut = "Bon"
fin = "jour"
print(debut + fin)        # Bonjour
```

`len(...)` donne la **longueur** (le nombre de caractères) :

```
print(len("Python"))      # 6
```

Les chaînes ont des **méthodes** : des actions qu'on déclenche avec un
point. Quelques-unes très utiles :

```
mot = "python"
print(mot.upper())        # PYTHON   (tout en majuscules)
print(mot.capitalize())   # Python   (première lettre en majuscule)
print("  salut  ".strip())# "salut"  (enlève les espaces autour)
```

## À toi

À partir de `nom = "monna"`, range dans `nom_majuscule` le nom tout en
**majuscules** (utilise `.upper()`).""",
            "starter": 'nom = "monna"\nnom_majuscule = ...\n',
            "check": 'assert nom_majuscule == "MONNA"\n',
            "solution": 'nom = "monna"\nnom_majuscule = nom.upper()\n',
        },
        {
            "id": "deb-05",
            "title": "Insérer des variables : les f-strings",
            "content": """## Mélanger texte et variables

Pour construire une phrase à partir de variables, la méthode moderne et
simple est la **f-string** : on met un `f` juste avant le guillemet
ouvrant, puis on place les variables entre **accolades** `{ }`.

```
prenom = "Ada"
age = 36
print(f"{prenom} a {age} ans.")     # Ada a 36 ans.
```

On peut même calculer directement dans les accolades :

```
prix = 4
print(f"Total : {prix * 3} euros")  # Total : 12 euros
```

C'est beaucoup plus lisible que de coller des morceaux avec des `+`.

## À toi

Avec une f-string, construis la variable `phrase` qui vaut exactement
`Il reste 5 jours.` à partir de `jours = 5`.""",
            "starter": "jours = 5\nphrase = ...\n",
            "check": 'assert phrase == "Il reste 5 jours."\n',
            "solution": 'jours = 5\nphrase = f"Il reste {jours} jours."\n',
        },
        {
            "id": "deb-06",
            "title": "Dialoguer avec input()",
            "content": """## Demander quelque chose à l'utilisateur

`input()` met le programme en pause et attend que la personne tape
quelque chose au clavier, puis valide avec Entrée.

```
prenom = input("Comment t'appelles-tu ? ")
print(f"Enchanté, {prenom} !")
```

**Point important :** `input()` renvoie toujours du **texte**, même si
on tape des chiffres. Pour faire un calcul, il faut convertir :

- `int("42")` transforme le texte `"42"` en nombre entier `42`
- `float("3.5")` donne le nombre à virgule `3.5`
- `str(42)` transforme un nombre en texte `"42"`

```
age_texte = input("Ton âge ? ")
age = int(age_texte)
print(f"Dans 10 ans tu auras {age + 10} ans")
```

## À toi

Deux nombres sont saisis (simulés ici). Lis-les avec `input()`,
convertis-les en entiers et range leur **somme** dans `total`.""",
            "starter": "a = int(input())\nb = int(input())\ntotal = ...\n",
            "stdin": ["15", "27"],
            "check": "assert total == 42 and isinstance(total, int)\n",
            "solution": "a = int(input())\nb = int(input())\ntotal = a + b\n",
        },
        {
            "id": "deb-07",
            "title": "Prendre des décisions : if / else",
            "content": """## Faire des choix

Un programme doit souvent réagir différemment selon la situation. C'est
le rôle de `if` (« si »), `else` (« sinon ») et `elif`
(contraction de *else if*, « sinon si »).

L'**indentation** (le décalage de 4 espaces vers la droite) indique ce
qui appartient au bloc. C'est essentiel en Python.

```
age = 20
if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")
```

Pour comparer, on utilise :
- `==` égal à (attention : deux signes égal !)
- `!=` différent de
- `<`, `>`, `<=`, `>=`

Avec plusieurs cas :

```
note = 14
if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
else:
    mention = "À revoir"
```

## À toi

Écris une fonction-test : selon la variable `temperature`, range dans
`message` le texte `"Il gèle"` si elle est **inférieure ou égale à 0**,
sinon `"Au-dessus de zéro"`.""",
            "starter": "temperature = -3\nif ... :\n    message = ...\nelse:\n    message = ...\n",
            "check": 'assert message == "Il gèle"\n'
                     't2 = 12\nm2 = "Il gèle" if t2 <= 0 else "Au-dessus de zéro"\n'
                     'assert m2 == "Au-dessus de zéro"\n',
            "solution": 'temperature = -3\nif temperature <= 0:\n    message = "Il gèle"\n'
                        'else:\n    message = "Au-dessus de zéro"\n',
        },
        {
            "id": "deb-08",
            "title": "Combiner des conditions",
            "content": """## Et, ou, non

On relie plusieurs conditions avec des mots simples :

- `and` (« et ») : vrai seulement si **les deux** sont vraies
- `or` (« ou ») : vrai si **au moins une** est vraie
- `not` (« non ») : inverse (vrai devient faux)

```
age = 25
a_le_permis = True
if age >= 18 and a_le_permis:
    print("Peut conduire")
```

```
jour = "samedi"
if jour == "samedi" or jour == "dimanche":
    print("C'est le week-end")
```

## À toi

Écris une fonction `peut_entrer(age, accompagne)` qui renvoie `True` si
la personne a **au moins 16 ans** OU si elle est **accompagnée**
(`accompagne` vaut `True`), et `False` sinon.""",
            "starter": "def peut_entrer(age, accompagne):\n    return ...\n",
            "check": "assert peut_entrer(18, False) is True\n"
                     "assert peut_entrer(12, True) is True\n"
                     "assert peut_entrer(12, False) is False\n",
            "solution": "def peut_entrer(age, accompagne):\n    return age >= 16 or accompagne\n",
        },
        {
            "id": "deb-09",
            "title": "Répéter avec une boucle for",
            "content": """## Faire la même chose plusieurs fois

Plutôt que de copier-coller, on **boucle**. `for` répète un bloc pour
chaque valeur d'une série.

`range(n)` fabrique la série des nombres de 0 à n-1 :

```
for i in range(3):
    print("Tour numéro", i)
# Tour numéro 0
# Tour numéro 1
# Tour numéro 2
```

`range(debut, fin)` va de `debut` à `fin - 1` :

```
for i in range(1, 6):
    print(i)        # 1 2 3 4 5
```

On peut accumuler un résultat dans une variable :

```
total = 0
for i in range(1, 5):
    total = total + i   # ou : total += i
print(total)            # 10  (1+2+3+4)
```

## À toi

Avec une boucle `for`, calcule dans `somme` la somme de tous les
entiers de 1 à 50 inclus.""",
            "starter": "somme = 0\nfor i in range(...):\n    ...\n",
            "check": "assert somme == 1275\n",
            "solution": "somme = 0\nfor i in range(1, 51):\n    somme += i\n",
        },
        {
            "id": "deb-10",
            "title": "Répéter tant que : la boucle while",
            "content": """## Répéter sous condition

`while` (« tant que ») répète **tant qu'une condition reste vraie**.
Utile quand on ne sait pas d'avance combien de tours il faudra.

```
compte = 3
while compte > 0:
    print(compte)
    compte = compte - 1
print("Décollage !")
```

⚠️ **Attention** : il faut que la condition finisse par devenir fausse,
sinon la boucle tourne à l'infini ! Ici, c'est `compte` qui diminue à
chaque tour jusqu'à atteindre 0.

`break` permet de sortir d'une boucle immédiatement.

## À toi

En partant de `n = 1`, double `n` à chaque tour (`n = n * 2`) **tant
que** `n` est inférieur à 1000. Quelle est la première valeur atteinte
qui dépasse 1000 ? Range-la dans `n`.""",
            "starter": "n = 1\nwhile n < 1000:\n    ...\n",
            "check": "assert n == 1024\n",
            "solution": "n = 1\nwhile n < 1000:\n    n = n * 2\n",
        },
        {
            "id": "deb-11",
            "title": "Ranger plusieurs valeurs : les listes",
            "content": """## Une boîte qui contient plusieurs choses

Une **liste** regroupe plusieurs valeurs, dans l'ordre, entre crochets
`[ ]` :

```
courses = ["pain", "lait", "œufs"]
```

On accède à un élément par sa **position** (appelée *indice*), en
commençant à **0** :

```
print(courses[0])     # pain  (le premier !)
print(courses[2])     # œufs
print(courses[-1])    # œufs  (le dernier)
print(len(courses))   # 3
```

On ajoute, on modifie :

```
courses.append("beurre")   # ajoute à la fin
courses[0] = "baguette"    # remplace le premier
```

Et on parcourt une liste avec une boucle `for` :

```
for article in courses:
    print(article)
```

## À toi

Pars de `notes = [12, 8, 15, 18, 9]`. Range dans `moyenne` la moyenne
de ces notes (indice : `sum(notes)` fait la somme, `len(notes)` compte
les éléments).""",
            "starter": "notes = [12, 8, 15, 18, 9]\nmoyenne = ...\n",
            "check": "assert abs(moyenne - 12.4) < 1e-9\n",
            "solution": "notes = [12, 8, 15, 18, 9]\nmoyenne = sum(notes) / len(notes)\n",
        },
        {
            "id": "deb-12",
            "title": "Ranger sa logique : les fonctions",
            "content": """## Donner un nom à un bloc de code

Une **fonction** est un morceau de programme réutilisable, à qui on
donne un nom. On la définit avec `def`, et on lui donne des
**paramètres** (les informations dont elle a besoin). `return` indique
le résultat qu'elle renvoie.

```
def saluer(prenom):
    return f"Bonjour {prenom} !"

# on l'utilise (on dit "on l'appelle") autant de fois qu'on veut :
print(saluer("Ada"))      # Bonjour Ada !
print(saluer("Alan"))     # Bonjour Alan !
```

Une fonction peut prendre plusieurs paramètres :

```
def aire_rectangle(largeur, hauteur):
    return largeur * hauteur

print(aire_rectangle(4, 3))   # 12
```

Les fonctions évitent de se répéter et rendent le code clair : chacune
fait une chose précise.

## À toi

Écris une fonction `double(nombre)` qui renvoie le double du nombre
reçu.""",
            "starter": "def double(nombre):\n    return ...\n",
            "check": "assert double(5) == 10\nassert double(0) == 0\nassert double(-3) == -6\n",
            "solution": "def double(nombre):\n    return nombre * 2\n",
        },
        {
            "id": "deb-13",
            "title": "Utiliser un module tout prêt",
            "content": """## Ne pas tout réécrire soi-même

Python est livré avec des **modules** : des boîtes à outils déjà
écrites, prêtes à l'emploi. Pour s'en servir, on les **importe** avec
le mot `import` au début du programme.

Le module `math` contient des outils mathématiques :

```
import math
print(math.sqrt(16))    # 4.0   (racine carrée)
print(math.pi)          # 3.1415926...
```

Le module `random` génère du hasard :

```
import random
print(random.randint(1, 6))   # un nombre au hasard entre 1 et 6 (un dé)
```

On peut aussi n'importer qu'un outil précis :

```
from random import choice
print(choice(["pile", "face"]))
```

Il existe des centaines de modules : pour les dates, les fichiers, le
web... Tu en découvriras beaucoup dans les parcours suivants.

## À toi

Avec le module `math`, calcule l'**hypoténuse** d'un triangle rectangle
de côtés `a = 3` et `b = 4` (formule : racine carrée de a² + b²).
Range le résultat dans `hypotenuse`.""",
            "starter": "import math\na = 3\nb = 4\nhypotenuse = ...\n",
            "check": "assert abs(hypotenuse - 5.0) < 1e-9\n",
            "solution": "import math\na = 3\nb = 4\nhypotenuse = math.sqrt(a**2 + b**2)\n",
        },
        {
            "id": "deb-14",
            "title": "Atelier : ton premier vrai programme",
            "content": """## On assemble tout !

Tu sais maintenant : afficher, stocker des variables, calculer, faire
des choix, boucler, utiliser des listes et écrire des fonctions. C'est
déjà de quoi écrire de vrais petits programmes.

Voici l'idée d'un petit programme de gestion de budget :

```
def bilan(depenses):
    total = sum(depenses)
    moyenne = total / len(depenses)
    return total, moyenne          # renvoie deux valeurs (un tuple)

total, moyenne = bilan([20, 35, 12, 8])
print(f"Total : {total} € — moyenne : {moyenne} €")
```

Remarque : une fonction peut renvoyer **plusieurs valeurs** d'un coup,
séparées par une virgule.

## À toi

Écris la fonction `bilan(depenses)` ci-dessus : elle reçoit une liste
de dépenses et renvoie un couple `(total, moyenne)`.""",
            "starter": "def bilan(depenses):\n    ...\n    return total, moyenne\n",
            "check": "t, m = bilan([20, 35, 12, 8])\nassert t == 75\nassert abs(m - 18.75) < 1e-9\n"
                     "t2, m2 = bilan([10, 10])\nassert t2 == 20 and m2 == 10\n",
            "solution": "def bilan(depenses):\n    total = sum(depenses)\n"
                        "    moyenne = total / len(depenses)\n    return total, moyenne\n",
        },
    ],
}
