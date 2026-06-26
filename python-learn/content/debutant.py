"""Niveau 1 — Débutant."""

LEVEL = {
    "id": "debutant",
    "title": "1 · Débutant",
    "lessons": [
        {
            "id": "deb-01",
            "title": "Premier programme : print()",
            "content": """## Afficher du texte

En Python, on affiche du texte à l'écran avec la fonction `print()`.
Le texte (une « chaîne de caractères ») se place entre guillemets,
simples ou doubles.

```
print("Bonjour le monde !")
print('Python, c\\'est parti.')
```

`print()` ajoute automatiquement un retour à la ligne après chaque appel.
On peut aussi afficher plusieurs valeurs séparées par des virgules :
elles seront jointes par une espace.

```
print("3 +", 4, "=", 3 + 4)
```

## À toi de jouer

Modifie le code à droite pour qu'il affiche exactement :
`Bonjour le monde !`""",
            "starter": 'print("...")\n',
            "expected_output": "Bonjour le monde !",
            "solution": 'print("Bonjour le monde !")\n',
        },
        {
            "id": "deb-02",
            "title": "Variables et types",
            "content": """## Stocker une valeur

Une variable est un nom qui pointe vers une valeur. On l'affecte avec `=`.

```
age = 30
prenom = "Cédric"
taille = 1.78
actif = True
```

Les types de base :
- `int` : nombre entier (30)
- `float` : nombre à virgule (1.78)
- `str` : chaîne de caractères ("Cédric")
- `bool` : booléen (`True` ou `False`)

La fonction `type()` révèle le type d'une valeur :

```
print(type(age))     # <class 'int'>
print(type(taille))  # <class 'float'>
```

## Exercice

Crée une variable `ville` valant `"Toulouse"` et une variable `code_postal`
valant l'entier `31000`. Les tests vérifient leur valeur.""",
            "starter": "ville = ...\ncode_postal = ...\n",
            "check": 'assert ville == "Toulouse", "ville doit valoir Toulouse"\n'
                     'assert code_postal == 31000, "code_postal doit valoir 31000"\n'
                     'assert isinstance(code_postal, int), "code_postal doit etre un entier"\n',
            "solution": 'ville = "Toulouse"\ncode_postal = 31000\n',
        },
        {
            "id": "deb-03",
            "title": "Les opérations",
            "content": """## Calculer

Python sait compter. Les opérateurs arithmétiques :
- `+` addition, `-` soustraction, `*` multiplication
- `/` division (résultat flottant), `//` division entière
- `%` modulo (le reste), `**` puissance

```
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(2 ** 10)  # 1024
```

L'ordre des priorités est le même qu'en maths ; on peut utiliser des
parenthèses pour lever toute ambiguïté.

## Exercice

Range dans `resultat` le reste de la division de `2024` par `7`.""",
            "starter": "resultat = ...\n",
            "check": "assert resultat == 2024 % 7\n",
            "solution": "resultat = 2024 % 7\n",
        },
        {
            "id": "deb-04",
            "title": "Les chaînes de caractères",
            "content": """## Manipuler du texte

Les chaînes se concatènent avec `+` et possèdent de nombreuses méthodes :

```
nom = "monna"
print(nom.upper())       # MONNA
print(nom.capitalize())  # Monna
print(len(nom))          # 5
```

## Les f-strings

La façon moderne d'insérer des variables dans du texte : préfixer la
chaîne par `f` et placer les expressions entre accolades.

```
prenom = "Cédric"
annee = 2026
print(f"{prenom} écrit en {annee}.")
```

## Exercice

À partir de `prenom = "ada"`, construis `message` qui vaut exactement
`Bonjour Ada !` (première lettre en majuscule) à l'aide d'une f-string.""",
            "starter": 'prenom = "ada"\nmessage = ...\n',
            "check": 'assert message == "Bonjour Ada !"\n',
            "solution": 'prenom = "ada"\nmessage = f"Bonjour {prenom.capitalize()} !"\n',
        },
        {
            "id": "deb-05",
            "title": "Les conditions : if / elif / else",
            "content": """## Prendre des décisions

Un bloc conditionnel exécute du code selon qu'une expression est vraie
ou fausse. L'indentation (4 espaces) délimite le bloc.

```
note = 14
if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 12:
    mention = "Assez bien"
else:
    mention = "Passable"
print(mention)
```

Opérateurs de comparaison : `==`, `!=`, `<`, `>`, `<=`, `>=`.
Opérateurs logiques : `and`, `or`, `not`.

## Exercice

Écris une fonction-libre : à partir de la variable `temperature`,
range dans `tenue` la valeur `"manteau"` si la température est
strictement inférieure à 10, sinon `"léger"`.""",
            "starter": "temperature = 7\ntenue = ...\n",
            "check": 'assert (tenue == "manteau") == (temperature < 10)\n'
                     'temperature2 = 20\n'
                     'tenue2 = "manteau" if temperature2 < 10 else "léger"\n'
                     'assert tenue2 == "léger"\n',
            "solution": 'temperature = 7\n'
                        'if temperature < 10:\n    tenue = "manteau"\nelse:\n    tenue = "léger"\n',
        },
        {
            "id": "deb-06",
            "title": "Les boucles : for et while",
            "content": """## Répéter

La boucle `for` parcourt une séquence. `range(n)` produit les nombres
de 0 à n-1.

```
for i in range(5):
    print(i)        # 0 1 2 3 4
```

La boucle `while` répète tant qu'une condition reste vraie :

```
n = 1
while n < 100:
    n = n * 2
print(n)            # 128
```

`break` interrompt la boucle, `continue` passe à l'itération suivante.

## Exercice

Calcule dans `somme` la somme des entiers de 1 à 100 inclus,
à l'aide d'une boucle.""",
            "starter": "somme = 0\nfor ... :\n    ...\n",
            "check": "assert somme == 5050\n",
            "solution": "somme = 0\nfor i in range(1, 101):\n    somme += i\n",
        },
        {
            "id": "deb-07",
            "title": "Les listes",
            "content": """## Collectionner des valeurs

Une liste regroupe plusieurs valeurs ordonnées, entre crochets.
L'indexation commence à 0.

```
fruits = ["pomme", "poire", "kiwi"]
print(fruits[0])     # pomme
print(fruits[-1])    # kiwi (dernier)
print(len(fruits))   # 3
```

On la modifie avec `append` (ajouter), `remove`, `insert`, etc.

```
fruits.append("mangue")
fruits[1] = "banane"
```

On la parcourt avec une boucle `for` :

```
for fruit in fruits:
    print(fruit)
```

## Exercice

Pars de `nombres = [4, 8, 15, 16, 23, 42]`. Ajoute `100` à la fin,
puis range dans `total` la somme de tous ses éléments
(`sum()` est ton ami).""",
            "starter": "nombres = [4, 8, 15, 16, 23, 42]\n# ajoute 100, puis calcule total\ntotal = ...\n",
            "check": "assert nombres[-1] == 100\nassert total == 4+8+15+16+23+42+100\n",
            "solution": "nombres = [4, 8, 15, 16, 23, 42]\nnombres.append(100)\ntotal = sum(nombres)\n",
        },
        {
            "id": "deb-08",
            "title": "Commentaires et saisie",
            "content": """## Documenter et dialoguer

Un commentaire commence par `#` : Python l'ignore. Il sert à expliquer
le code à un humain.

```
# Ceci est un commentaire
prix = 20  # commentaire en fin de ligne
```

La fonction `input()` lit une ligne tapée au clavier. Attention :
elle renvoie toujours une **chaîne de caractères**.

```
nom = input("Ton prénom ? ")
print("Bonjour", nom)
```

## Exercice

Une variable `reponse` contient déjà une saisie (simulée ici).
Construis `message` qui vaut `Tu as répondu : <reponse>`.""",
            "starter": "# reponse est fournie par la saisie\nmessage = ...\n",
            "stdin": ["oui"],
            "check": 'reponse = "oui"\nassert message == "Tu as répondu : oui"\n',
            "solution": 'reponse = input()\nmessage = f"Tu as répondu : {reponse}"\n',
        },
        {
            "id": "deb-09",
            "title": "Convertir les types",
            "content": """## D'un type à l'autre

Comme `input()` renvoie du texte, il faut souvent convertir. Les
fonctions de conversion portent le nom du type :

```
texte = "42"
nombre = int(texte)      # 42 (entier)
print(nombre + 1)        # 43

x = float("3.14")        # 3.14
mot = str(2026)          # "2026"
```

Une conversion impossible lève une erreur :
`int("bonjour")` provoque une `ValueError`.

## Exercice

Deux variables texte `a = "15"` et `b = "27"` contiennent des nombres.
Range leur somme (un entier) dans `total`.""",
            "starter": 'a = "15"\nb = "27"\ntotal = ...\n',
            "check": "assert total == 42 and isinstance(total, int)\n",
            "solution": 'a = "15"\nb = "27"\ntotal = int(a) + int(b)\n',
        },
        {
            "id": "deb-10",
            "title": "La logique booléenne",
            "content": """## Combiner des conditions

Les opérateurs logiques relient plusieurs conditions :
- `and` : vrai si **les deux** sont vraies
- `or` : vrai si **au moins une** est vraie
- `not` : inverse la valeur

```
age = 25
permis = True
if age >= 18 and permis:
    print("Peut conduire")
```

Tout objet possède une « valeur de vérité » : `0`, `""`, `[]`, `None`
sont considérés comme `False` ; presque tout le reste vaut `True`.

```
if not []:           # une liste vide est "fausse"
    print("liste vide")
```

## Exercice

Écris une fonction `bissextile(an)` qui renvoie `True` si l'année est
bissextile : divisible par 4 **et** (pas par 100 **ou** divisible par 400).""",
            "starter": "def bissextile(an):\n    ...\n",
            "check": "assert bissextile(2024) is True\nassert bissextile(2023) is False\n"
                     "assert bissextile(1900) is False\nassert bissextile(2000) is True\n",
            "solution": "def bissextile(an):\n    return an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)\n",
        },
    ],
}
