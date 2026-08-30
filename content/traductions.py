"""
Traductions du CONTENU des leçons (l'interface, elle, vit dans app/i18n.py).

Les cours s'écrivent en français. Plutôt que d'alourdir chaque fichier de
contenu avec une seconde version, les traductions sont regroupées ici :

  - les fichiers de cours restent lisibles ;
  - le travail de traduction peut être confié à quelqu'un qui ne touchera
    qu'à ce fichier ;
  - une nouvelle langue s'ajoute sans modifier une seule leçon.

Chaque entrée est repérée par l'identifiant du parcours ou de la leçon, et
ne contient que les champs traduits. Tout ce qui manque reste affiché en
français : on peut donc traduire leçon par leçon, sans jamais laisser de
trou dans l'application.

Pour connaître l'avancement :  python main.py --etat-traduction
"""

TRADUCTIONS = {
    "en": {
        # ------------------------------------------------- titres des parcours
        "debutant": {"title": "1 · Beginner"},
        "intermediaire": {"title": "2 · Intermediate"},
        "avance": {"title": "3 · Advanced"},
        "expert": {"title": "4 · Expert"},
        "scripts": {"title": "5 · Scripts & automation"},
        "interfaces": {"title": "6 · Graphical interfaces"},
        "web": {"title": "7 · Python & the web"},
        "admin": {"title": "8 · Managing your computer"},
        "sqlite": {"title": "9 · Databases (SQLite)"},
        "turtle": {"title": "10 · Drawing (turtle)"},
        "algos": {"title": "11 · Algorithms & data structures"},
        "donnees": {"title": "12 · Working with data"},
        "tests_tdd": {"title": "13 · Tests & TDD"},
        "projets": {"title": "14 · Guided projects"},
        "entrainement": {"title": "15 · Practice (debugging & fill-ins)"},
        "erreurs": {"title": "16 · Decoding errors"},

        # ------------------------------- parcours « Décoder les erreurs »
        "err-01": {
            "title": "Reading an error message",
            "content": """## Three pieces of information, always the same

When Python stops, it is not mocking you: it explains very precisely what
blocked it. You just need to know where to look.

```
Traceback (most recent call last):
  File "<exercice>", line 3, in <module>
    print(totl)
NameError: name 'totl' is not defined
```

Three things to spot, and only one to read first:

- **the last line**: the error TYPE (`NameError`) and its explanation
  (`name 'totl' is not defined`);
- **the line number** (`line 3`): where Python stopped;
- **the copied line of code**: what it was trying to do.

**Always read the last line first.** The rest is the path taken to get there.

- **Exercise**: this program stops. Read the error, fix the typo.""",
            "hints": [
                "Read the last line of the message: which name does Python not know?",
                "Compare the name inside print() with the one on line 3.",
                "« totl » does not exist: the variable is called « total ».",
            ],
        },
        "err-02": {
            "title": "Which type of error will show up?",
            "content": """## Recognise before fixing

Each error type matches a family of causes. Knowing them saves a lot of
time:

- `NameError` — a name Python does not know
- `TypeError` — an operation between incompatible things
- `ValueError` — the right type, but an impossible value
- `IndexError` — an item requested beyond the end of a list
- `KeyError` — a key missing from a dictionary
- `ZeroDivisionError` — a division by zero

Here the program works. Simply predict what it prints: it is a reminder of
what `type()` does, which is often how you understand a `TypeError`.""",
            "explanation": (
                "A TypeError almost always comes from this: two values that "
                "look alike on screen (3 and '3') but are not the same type. "
                "When in doubt, print type(my_variable)."
            ),
        },
        "err-03": {
            "title": "TypeError: adding apples and oranges",
            "content": """## Type matters more than appearance

```
TypeError: can only concatenate str (not "int") to str
```

This message says: « I know how to stick text onto text, but not a number
onto text ». Python never guesses what you meant.

The fix is almost always a **conversion**:

- `str(42)` turns the number 42 into the text `"42"`
- `int("42")` turns the text `"42"` into the number 42

```
age = 30
print("I am " + str(age) + " years old")
```

- **Exercise**: this program crashes. Convert what needs converting so
  that it prints `Il reste 5 places`.""",
            "hints": [
                "The message says only text can be stuck onto text.",
                "Which is the only value here that is not text?",
                "Wrap places in str(...).",
            ],
        },
        "err-04": {
            "title": "IndexError and KeyError: it does not exist",
            "content": """## Counting from zero

```
IndexError: list index out of range
```

The first item of a list has index **0**. A list of 3 items therefore has
indexes 0, 1 and 2 — never 3.

```
colours = ["red", "green", "blue"]
print(colours[0])    # red
print(colours[2])    # blue
print(colours[3])    # IndexError
```

The last item is reached with `my_list[-1]`, or `my_list[len(my_list) - 1]`.

For a dictionary the error is called `KeyError`: the requested key does not
exist. `my_dict.get("key")` returns `None` instead of crashing.

- **Exercise**: this program wants to print the last mark. Fix it.""",
            "hints": [
                "The list has 3 items: which indexes are valid?",
                "The last item is at index 2, not 3.",
                "notes[-1] always means the last item.",
            ],
        },
        "err-05": {
            "title": "SyntaxError: the mistake is often ABOVE",
            "content": """## The line-number trap

For a syntax error, Python points at the place where it **realised**
something was wrong — not always where the mistake is.

```
  File "<exercice>", line 2
    print("bonjour")
    ^^^^^
SyntaxError: invalid syntax
```

If the reported line looks fine, **look at the line above**: a bracket
never closed, a missing quote, or the colon forgotten at the end of an
`if`, `for`, `while` or `def`.

This is also the only family of errors Python catches **before** running
anything: if you see no output at all, not even from the first lines, it
is almost always a SyntaxError.

- **Exercise**: repair this program so that it prints `7`.""",
            "hints": [
                "The error is reported on line 2, but line 2 is correct.",
                "Look at line 1: count the opening and closing brackets.",
                "A closing bracket is missing after the 4.",
            ],
        },
        "err-06": {
            "title": "ValueError: right type, wrong value",
            "content": """## When the conversion fails

```
ValueError: invalid literal for int() with base 10: 'douze'
```

`int()` does expect text — so the **type** is right. But « douze » is not a
way of writing a number: it is the **value** that does not fit. Hence
`ValueError` rather than `TypeError`.

This error is very common with `input()`, which always returns text: if the
user types anything other than a number, `int()` fails.

- **Exercise**: this program should print twice 12. Fix the value so that
  the conversion succeeds.""",
            "hints": [
                "int() can read « 12 », but not « douze ».",
                "Write the number in digits, between quotes.",
            ],
        },
        "err-07": {
            "title": "Following a traceback",
            "content": """## Retracing the path

When the error happens inside a function, Python shows the whole path
taken:

```
Traceback (most recent call last):
  File "<exercice>", line 7, in <module>
    print(moyenne([]))
  File "<exercice>", line 4, in moyenne
    return total / len(valeurs)
ZeroDivisionError: division by zero
```

Two levels, read **from bottom to top**:

- the error happened on **line 4**, inside the `moyenne` function;
- that function had been called on **line 7**.

The cause is often at the top (the faulty call: an empty list), the symptom
at the bottom (the division). That is why you read the last line first,
then work your way back up.

- **Exercise**: guard the function so that an empty list returns `0`
  instead of crashing.""",
            "hints": [
                "The error comes from dividing by len(valeurs), which is 0.",
                "Handle the empty list BEFORE dividing.",
                "Add at the top: if len(valeurs) == 0: return 0",
            ],
        },
        "err-08": {
            "title": "Put in order: a guarded input",
            "content": """## The right order to protect yourself

Here is the usual way to convert an input without risking a `ValueError`:
you attempt the conversion, and plan for the case where it fails.

Put the lines back in order so that the program prints `nombre invalide`
without crashing.""",
        },
        # --------------------------------------- parcours « Débutant »
        # Attention : les noms de variables demandés dans les consignes
        # (ville, habitants, prix_ttc…) ne sont PAS traduits — le code de
        # vérification les recherche tels quels.
        "deb-00": {
            "title": "Welcome: what does programming mean?",
            "content": """## Programming means giving orders

A computer is fast but dim: it only does what it is told, exactly, and
in order. **Programming** means writing a list of clear instructions
that it will carry out one by one, from top to bottom, like a recipe.

Python is a programming language known for being **readable**: its
instructions look almost like plain English. That is why it is
recommended for a first language.

## How it works here

On the right you have an **editor**: that is where you write your
program. Below it, a **console**: that is where the computer answers.

- The **Run** button starts your program and shows the result.
- The **Check** button verifies that you solved the exercise.
- The **Solution** button shows one possible answer if you are stuck.

There is no risk in getting it wrong: try, look, try again. That is
exactly how coding is learnt.

## Your very first order

The instruction `print(...)` means « show this on screen ».
Try to display the sentence: `Je commence Python !`""",
        },
        "deb-01": {
            "title": "Showing text with print()",
            "content": """## The print() function

`print` is the most used instruction when starting out: it **displays**
whatever you put between its brackets. Text goes between quotes (`"` or
`'`).

```
print("Bonjour")
print('Ça marche aussi avec des apostrophes')
```

Each `print` writes on **its own line**. Three `print`, three lines.

```
print("Ligne 1")
print("Ligne 2")
```

You can display several things at once by separating them with commas:
Python adds a space between each.

```
print("J'ai", 3, "chats")     # shows: J'ai 3 chats
```

## Your turn

Display exactly these two lines (one `print` each):
```
Salut
Le monde
```""",
        },
        "deb-02": {
            "title": "Variables: labels on values",
            "content": """## Keeping a value at hand

A **variable** is a name stuck onto a value so you can reuse it, like a
label on a box. You write it with the `=` sign (read here as
« receives »).

```
age = 30          # the box "age" holds 30
prenom = "Ada"    # the box "prenom" holds "Ada"
```

After that, just name it to get the value back:

```
print(prenom)     # shows: Ada
print(age)        # shows: 30
```

You can change what a variable holds at any time:

```
age = 31          # now "age" holds 31
```

## The main kinds of value

- a **whole number** (`int`): `30`
- a **decimal number** (`float`): `1.78`
- a **text** (`str`, for *string*): `"Ada"`
- a **boolean** (`bool`): `True` or `False`

## Your turn

Create a variable `ville` holding `"Toulouse"` and a variable
`habitants` holding the whole number `500000`.""",
        },
        "deb-03": {
            "title": "Doing sums with numbers",
            "content": """## Python can count

You use the usual operators:

- `+` addition, `-` subtraction
- `*` multiplication, `/` division
- `**` power (`2 ** 3` is 8)
- `//` whole division (the quotient), `%` modulo (the remainder)

```
print(10 + 5)     # 15
print(10 / 4)     # 2.5
print(10 // 4)    # 2  (how many times 4 fits into 10)
print(10 % 4)     # 2  (what is left over)
print(2 ** 10)    # 1024
```

You can of course compute with variables:

```
largeur = 5
hauteur = 3
aire = largeur * hauteur
print(aire)       # 15
```

## Your turn

An item costs `prix_ht = 80` euros before tax. VAT is 20 %. Work out the
price including tax in the variable `prix_ttc` (hint: adding 20 % means
multiplying by `1.2`).""",
        },
        "deb-04": {
            "title": "Text: character strings",
            "content": """## Working with text

A string is text between quotes. You can **stick** two strings together
with `+` (this is called concatenation):

```
debut = "Bon"
fin = "jour"
print(debut + fin)        # Bonjour
```

`len(...)` gives the **length** (the number of characters):

```
print(len("Python"))      # 6
```

Strings have **methods**: actions triggered with a dot. A few very
useful ones:

```
mot = "python"
print(mot.upper())        # PYTHON   (all capitals)
print(mot.capitalize())   # Python   (first letter capitalised)
print("  salut  ".strip())# "salut"  (removes surrounding spaces)
```

## Your turn

Starting from `nom = "monna"`, put the name in **all capitals** into
`nom_majuscule` (use `.upper()`).""",
        },
        "deb-05": {
            "title": "Inserting variables: f-strings",
            "content": """## Mixing text and variables

To build a sentence from variables, the modern and simple way is the
**f-string**: put an `f` just before the opening quote, then place the
variables between **braces** `{ }`.

```
prenom = "Ada"
age = 36
print(f"{prenom} a {age} ans.")     # Ada a 36 ans.
```

You can even compute directly inside the braces:

```
prix = 4
print(f"Total : {prix * 3} euros")  # Total : 12 euros
```

This is far more readable than gluing pieces together with `+`.

## Your turn

Using an f-string, build the variable `phrase` so that it is exactly
`Il reste 5 jours.`, starting from `jours = 5`.""",
        },
        "deb-06": {
            "title": "Talking to the user with input()",
            "content": """## Asking the user for something

`input()` pauses the program and waits for the person to type something
on the keyboard, then press Enter.

```
prenom = input("Comment t'appelles-tu ? ")
print(f"Enchanté, {prenom} !")
```

**Important:** `input()` always returns **text**, even when digits are
typed. To compute with it, you must convert:

- `int("42")` turns the text `"42"` into the whole number `42`
- `float("3.5")` gives the decimal number `3.5`
- `str(42)` turns a number into the text `"42"`

```
age_texte = input("Ton âge ? ")
age = int(age_texte)
print(f"Dans 10 ans tu auras {age + 10} ans")
```

## Your turn

Two numbers are typed in (simulated here). Read them with `input()`,
convert them to whole numbers and put their **sum** into `total`.""",
        },
        "deb-07": {
            "title": "Making decisions: if / else",
            "content": """## Making choices

A program often has to react differently depending on the situation.
That is the job of `if`, `else` and `elif` (short for *else if*).

**Indentation** (shifting 4 spaces to the right) shows what belongs to
the block. This is essential in Python.

```
age = 20
if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")
```

To compare, you use:
- `==` equal to (careful: two equals signs!)
- `!=` different from
- `<`, `>`, `<=`, `>=`

With several cases:

```
note = 14
if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
else:
    mention = "À revoir"
```

## Your turn

Depending on the variable `temperature`, put into `message` the text
`"Il gèle"` if it is **less than or equal to 0**, and
`"Au-dessus de zéro"` otherwise.""",
        },
        "deb-08": {
            "title": "Combining conditions",
            "content": """## And, or, not

Several conditions are linked with simple words:

- `and`: true only if **both** are true
- `or`: true if **at least one** is true
- `not`: the opposite (true becomes false)

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

## Your turn

Write a function `peut_entrer(age, accompagne)` returning `True` if the
person is **at least 16** OR is **accompanied** (`accompagne` is
`True`), and `False` otherwise.""",
        },
        "deb-09": {
            "title": "Repeating with a for loop",
            "content": """## Doing the same thing several times

Rather than copy and paste, you **loop**. `for` repeats a block for each
value of a series.

`range(n)` builds the series of numbers from 0 to n-1:

```
for i in range(3):
    print("Tour numéro", i)
# Tour numéro 0
# Tour numéro 1
# Tour numéro 2
```

`range(start, end)` goes from `start` to `end - 1`:

```
for i in range(1, 6):
    print(i)        # 1 2 3 4 5
```

You can build up a result in a variable:

```
total = 0
for i in range(1, 5):
    total = total + i   # or: total += i
print(total)            # 10  (1+2+3+4)
```

## Your turn

Using a `for` loop, compute in `somme` the sum of every whole number
from 1 to 50 inclusive.""",
        },
        "deb-10": {
            "title": "Repeating while: the while loop",
            "content": """## Repeating under a condition

`while` repeats **as long as a condition stays true**. Useful when you
do not know in advance how many turns will be needed.

```
compte = 3
while compte > 0:
    print(compte)
    compte = compte - 1
print("Décollage !")
```

⚠️ **Careful**: the condition must eventually become false, otherwise
the loop runs forever! Here it is `compte` that decreases every turn
until it reaches 0.

`break` leaves a loop immediately.

## Your turn

Starting from `n = 1`, double `n` every turn (`n = n * 2`) **while** `n`
is below 1000. What is the first value reached that goes past 1000? Put
it into `n`.""",
        },
        "deb-11": {
            "title": "Holding several values: lists",
            "content": """## A box holding several things

A **list** groups several values, in order, between square brackets
`[ ]`:

```
courses = ["pain", "lait", "œufs"]
```

You reach an item by its **position** (called the *index*), starting at
**0**:

```
print(courses[0])     # pain  (the first one!)
print(courses[2])     # œufs
print(courses[-1])    # œufs  (the last one)
print(len(courses))   # 3
```

You can add and change:

```
courses.append("beurre")   # adds at the end
courses[0] = "baguette"    # replaces the first
```

And you walk through a list with a `for` loop:

```
for article in courses:
    print(article)
```

## Your turn

Start from `notes = [12, 8, 15, 18, 9]`. Put the average of those marks
into `moyenne` (hint: `sum(notes)` adds them up, `len(notes)` counts
them).""",
        },
        "deb-12": {
            "title": "Organising your logic: functions",
            "content": """## Giving a name to a block of code

A **function** is a reusable piece of program given a name. You define
it with `def`, and give it **parameters** (the information it needs).
`return` states the result it hands back.

```
def saluer(prenom):
    return f"Bonjour {prenom} !"

# you use it (you « call » it) as many times as you like:
print(saluer("Ada"))      # Bonjour Ada !
print(saluer("Alan"))     # Bonjour Alan !
```

A function can take several parameters:

```
def aire_rectangle(largeur, hauteur):
    return largeur * hauteur

print(aire_rectangle(4, 3))   # 12
```

Functions avoid repetition and keep code clear: each one does a single
precise thing.

## Your turn

Write a function `double(nombre)` returning twice the number it
receives.""",
        },
        "deb-13": {
            "title": "Using a ready-made module",
            "content": """## Not rewriting everything yourself

Python ships with **modules**: toolboxes already written, ready to use.
To use one, you **import** it with the word `import` at the top of the
program.

The `math` module holds mathematical tools:

```
import math
print(math.sqrt(16))    # 4.0   (square root)
print(math.pi)          # 3.1415926...
```

The `random` module produces randomness:

```
import random
print(random.randint(1, 6))   # a random number between 1 and 6 (a die)
```

You can also import just one tool:

```
from random import choice
print(choice(["pile", "face"]))
```

There are hundreds of modules: for dates, files, the web… You will meet
many of them in the following tracks.

## Your turn

Using the `math` module, work out the **hypotenuse** of a right-angled
triangle with sides `a = 3` and `b = 4` (formula: square root of
a² + b²). Put the result into `hypotenuse`.""",
        },
        "deb-14": {
            "title": "Workshop: your first real program",
            "content": """## Putting it all together!

You now know how to display, store variables, compute, make choices,
loop, use lists and write functions. That is already enough to write
real little programs.

Here is the idea of a small budget program:

```
def bilan(depenses):
    total = sum(depenses)
    moyenne = total / len(depenses)
    return total, moyenne          # returns two values (a tuple)

total, moyenne = bilan([20, 35, 12, 8])
print(f"Total : {total} € — moyenne : {moyenne} €")
```

Note: a function can return **several values** at once, separated by a
comma.

## Your turn

Write the function `bilan(depenses)` above: it receives a list of
expenses and returns a pair `(total, moyenne)`.""",
        },
        "qz-deb": {
            "title": "Quiz: Beginner recap",
            "content": "## Check your basics\n\nOne short question to close the track.",
            "question": "What does len(\"Python\") return?",
            "options": ["5", "6", "7", "an error"],
            "explanation": "« Python » has 6 characters, so len is 6.",
        },
        # ---------------------------------- parcours « Intermédiaire »
        "int-01": {
            "title": "Slicing and list comprehensions",
            "content": """## Cutting a sequence

The syntax `my_list[start:end:step]` extracts a portion.

```
lettres = list("PYTHON")
print(lettres[1:4])    # ['Y', 'T', 'H']
print(lettres[::-1])   # backwards
```

## List comprehensions

A concise and idiomatic way of building a list:

```
carres = [x * x for x in range(1, 6)]   # [1, 4, 9, 16, 25]
pairs = [n for n in range(20) if n % 2 == 0]
```

## Exercise

Using a comprehension, put into `cubes` the list of the cubes (x³) of
the numbers from 1 to 10 inclusive.""",
        },
        "int-02": {
            "title": "Tuples and unpacking",
            "content": """## The tuple: an unchangeable sequence

A tuple looks like a list but cannot be modified. You write it with
brackets (or without).

```
point = (3, 4)
x, y = point          # unpacking
print(x, y)           # 3 4
```

Unpacking is very Pythonic. It lets you swap two variables without a
temporary one:

```
a, b = 1, 2
a, b = b, a           # a is 2, b is 1
```

## Exercise

With a single unpacking, assign `mini` the smaller and `maxi` the larger
of `(42, 7)`. Use the `min()` and `max()` functions.""",
        },
        "int-03": {
            "title": "Dictionaries",
            "content": """## Pairing keys with values

A dictionary stores key → value pairs, between braces.

```
personne = {"nom": "Monna", "ville": "Le Fauga"}
print(personne["nom"])          # Monna
personne["metier"] = "auteur"   # adding
```

You walk through it with `.items()`, `.keys()`, `.values()`:

```
for cle, valeur in personne.items():
    print(cle, "->", valeur)
```

`.get(key, default)` avoids the error when the key does not exist.

## Exercise

From the sentence `"le chat le chien le chat"`, build a dictionary
`freq` counting how many times each word appears.
Hint: `phrase.split()` cuts it into words.""",
        },
        "int-04": {
            "title": "Functions",
            "content": """## Factoring out your code

A function wraps up a reusable piece of work. `def` defines it, `return`
hands back a result.

```
def aire_rectangle(largeur, hauteur):
    return largeur * hauteur

print(aire_rectangle(3, 4))   # 12
```

Parameters can be given default values:

```
def saluer(nom, politesse="Bonjour"):
    return f"{politesse} {nom}"

print(saluer("Ada"))                 # Bonjour Ada
print(saluer("Ada", "Coucou"))       # Coucou Ada
```

## Exercise

Write a function `est_pair(n)` returning `True` if `n` is even, `False`
otherwise.""",
        },
        "int-05": {
            "title": "*args, **kwargs and lambda",
            "content": """## A variable number of arguments

`*args` captures a list of positional arguments, `**kwargs` a dictionary
of named ones.

```
def total(*nombres):
    return sum(nombres)

print(total(1, 2, 3, 4))     # 10
```

## Lambda functions

A tiny anonymous function, on one line:

```
double = lambda x: x * 2
print(double(21))            # 42
```

Very handy with `sorted`, `map`, `filter`:

```
mots = ["python", "go", "rust"]
print(sorted(mots, key=lambda m: len(m)))  # ['go', 'rust', 'python']
```

## Exercise

Write `moyenne(*notes)` returning the average of the marks it receives
(and `0` when there is none).""",
        },
        "int-06": {
            "title": "Handling errors: try / except",
            "content": """## Catching exceptions

When an operation fails, Python raises an exception. You intercept it
with `try` / `except` to avoid a crash.

```
try:
    resultat = 10 / 0
except ZeroDivisionError:
    resultat = None
    print("Division par zéro évitée")
```

You can raise an exception yourself with `raise`:

```
def racine(x):
    if x < 0:
        raise ValueError("nombre négatif")
    return x ** 0.5
```

`finally` always runs, error or not.

## Exercise

Write `division_sure(a, b)` returning `a / b`, but returning the string
`"erreur"` when `b` is 0.""",
        },
        "int-07": {
            "title": "Sets",
            "content": """## Unique values

A `set` is an **unordered** collection of **unique** items. Ideal for
removing duplicates or testing membership very quickly.

```
nombres = {1, 2, 2, 3, 3, 3}
print(nombres)          # {1, 2, 3}
print(2 in nombres)     # True
```

Set operations are built in:

```
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)   # intersection: {2, 3}
print(a | b)   # union       : {1, 2, 3, 4}
print(a - b)   # difference  : {1}
```

## Exercise

From the list `doublons = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]`, put into
`uniques` the **number** of distinct values.""",
        },
        "int-08": {
            "title": "Modules and imports",
            "content": """## Reusing existing code

A module is a file of code that you import. The standard library is full
of them.

```
import math
print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.1415...

from random import randint
print(randint(1, 6))     # a die

import datetime as dt
print(dt.date.today())
```

Three forms: `import module`, `from module import name`,
`import module as alias`.

## Exercise

Using the `math` module, put into `resultat` the floor (largest whole
number below) of `7.8` (the `math.floor` function).""",
        },
        "int-09": {
            "title": "Sorting with sorted() and key",
            "content": """## Ordering precisely

`sorted()` returns a new sorted list; `.sort()` sorts in place. The `key`
parameter says **by which criterion** to sort, and `reverse` flips the
order.

```
mots = ["banane", "kiwi", "pomme"]
print(sorted(mots, key=len))          # by length
print(sorted(mots, reverse=True))     # descending order

gens = [("Ada", 36), ("Alan", 41)]
print(sorted(gens, key=lambda p: p[1]))   # by age
```

## Exercise

Sort the list of pairs `scores = [("A", 9), ("B", 3), ("C", 7)]` by
**descending** score and put the result into `classement`.""",
        },
        "int-10": {
            "title": "Dictionary comprehensions",
            "content": """## Building a dictionary in one line

Same idea as list comprehensions, but with `key: value`.

```
carres = {n: n * n for n in range(1, 5)}
# {1: 1, 2: 4, 3: 9, 4: 16}

prix = {"pain": 1.2, "lait": 0.9}
promo = {produit: p * 0.8 for produit, p in prix.items()}
```

You can add a condition:

```
pairs = {n: "pair" for n in range(6) if n % 2 == 0}
```

## Exercise

From `mots = ["python", "go", "rust"]`, build `longueurs`, a dictionary
pairing each word with its length.""",
        },
        "qz-int": {
            "title": "Quiz: Intermediate recap",
            "content": "## Data structures",
            "question": "Which structure holds only unique values?",
            "options": ["list", "tuple", "set", "str"],
            "explanation": "A set automatically removes duplicates.",
        },
        # ----------------------------------------- parcours « Avancé »
        "adv-01": {
            "title": "Generators: yield",
            "content": """## Producing values on demand

A generator produces its values one at a time, without keeping them all
in memory. The keyword `yield` replaces `return` and « pauses » the
function.

```
def compte_a_rebours(n):
    while n > 0:
        yield n
        n -= 1

for x in compte_a_rebours(3):
    print(x)        # 3 2 1
```

This is ideal for possibly endless or very large streams of data. The
generator expression is the short form:

```
total = sum(x * x for x in range(1000000))
```

## Exercise

Write a generator `pairs(limite)` producing the even numbers from 0
(included) up to `limite` (excluded).""",
        },
        "adv-02": {
            "title": "Object-oriented programming: classes",
            "content": """## Defining an object

A class is a mould for objects. `__init__` is the constructor; `self`
refers to the current instance.

```
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise ValueError("solde insuffisant")
        self.solde -= montant

c = Compte(100)
c.deposer(50)
print(c.solde)      # 150
```

## Exercise

Create a class `Chrono` with an attribute `secondes` starting at 0 and a
method `ajouter(s)` increasing it by `s`.""",
        },
        "adv-03": {
            "title": "Inheritance and polymorphism",
            "content": """## Reusing and specialising

A class can inherit from another, take over its methods and redefine
them. `super()` calls the parent version.

```
class Animal:
    def __init__(self, nom):
        self.nom = nom
    def cri(self):
        return "..."

class Chien(Animal):
    def cri(self):
        return "Ouaf"

class Chat(Animal):
    def cri(self):
        return "Miaou"

for a in [Chien("Rex"), Chat("Felix")]:
    print(a.nom, ":", a.cri())
```

That is polymorphism: one and the same call (`a.cri()`) behaves
differently depending on the real type of the object.

## Exercise

Create `Carre` inheriting from `Forme`. `Forme` has a method `aire()`
returning 0. `Carre.__init__(self, cote)` stores `cote`, and `aire()`
returns the area of the square.""",
        },
        "adv-04": {
            "title": "Special methods (dunder)",
            "content": """## Making your objects « Pythonic »

Methods surrounded by double underscores (`__...__`) let your objects
respond to operators and built-in functions.

```
class Vecteur:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)
    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

v = Vecteur(1, 2) + Vecteur(3, 4)
print(v)            # Vecteur(4, 6)
```

A few classics: `__str__`, `__repr__`, `__len__`, `__eq__`,
`__getitem__`.

## Exercise

Add to `Panier` the method `__len__` so that `len(panier)` returns the
number of items held in `self.articles`.""",
        },
        "adv-05": {
            "title": "Decorators",
            "content": """## Wrapping a function

A decorator is a function taking a function and returning an « enhanced »
version of it. The `@` syntax applies it.

```
def crier(fonction):
    def emballage(*args, **kwargs):
        return fonction(*args, **kwargs).upper()
    return emballage

@crier
def saluer(nom):
    return f"bonjour {nom}"

print(saluer("ada"))    # BONJOUR ADA
```

This is the machinery behind `@property`, `@staticmethod`, or the routes
of a web framework.

## Exercise

Write a decorator `double` multiplying by 2 the value returned by the
decorated function.""",
        },
        "adv-06": {
            "title": "The standard library: collections, itertools",
            "content": """## Not reinventing the wheel

Python ships « batteries included ». A few gems:

```
from collections import Counter, defaultdict

mots = "a b a c b a".split()
print(Counter(mots))          # Counter({'a': 3, 'b': 2, 'c': 1})

groupes = defaultdict(list)
groupes["pairs"].append(2)    # no need to create the key first
```

```
import itertools as it
print(list(it.combinations([1, 2, 3], 2)))  # [(1,2),(1,3),(2,3)]
```

`Counter` counts, `defaultdict` supplies a default value, `itertools`
chains, combines and accumulates.

## Exercise

Using `Counter`, put into `plus_courant` the most frequent character of
the string `"mississippi"` (use `.most_common(1)`).""",
        },
        "adv-07": {
            "title": "@property and encapsulation",
            "content": """## Controlling access to attributes

The `@property` decorator turns a method into a « computed » attribute,
and lets you validate assignments through a *setter*.

```
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        if valeur < -273.15:
            raise ValueError("sous le zéro absolu")
        self._celsius = valeur

t = Temperature(25)
print(t.fahrenheit)     # 77.0
t.celsius = 30          # goes through the setter
```

## Exercise

Add to `Cercle` a read-only property `aire` returning π·r² (use
`math.pi`).""",
        },
        "adv-08": {
            "title": "Class methods and static methods",
            "content": """## Three kinds of method

- an **instance method** receives `self` (the object);
- a **class method** (`@classmethod`) receives `cls` (the class):
  handy for alternative constructors;
- a **static method** (`@staticmethod`) receives neither: it is simply a
  function filed inside the class.

```
class Date:
    def __init__(self, jour, mois):
        self.jour, self.mois = jour, mois

    @classmethod
    def depuis_chaine(cls, texte):
        j, m = texte.split("/")
        return cls(int(j), int(m))

    @staticmethod
    def est_valide(mois):
        return 1 <= mois <= 12

d = Date.depuis_chaine("14/07")
print(Date.est_valide(13))   # False
```

## Exercise

Add to `Vecteur` a class method `origine()` returning a
`Vecteur(0, 0)`.""",
        },
        "adv-09": {
            "title": "Reading and writing files",
            "content": r"""## Working with files

You open a file with `open()`, ideally through `with` so that it is
always closed. The mode: `"r"` (read), `"w"` (write, overwrites),
`"a"` (append).

```
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("ligne 1\n")
    f.write("ligne 2\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    # or: for ligne in f: ...
```

Always state `encoding="utf-8"` to avoid nasty surprises with accented
characters.

## Exercise

Complete `ecrire_lire(chemin, lignes)`: write each item of `lignes` on
its own line in the file, then read the file back and return the list of
lines **without the trailing newline**.""",
        },
        "adv-10": {
            "title": "Regular expressions (re)",
            "content": r"""## Searching for patterns

The `re` module lets you search, extract and replace text according to
patterns.

```
import re

texte = "Appelle le 06 12 34 56 78 ou le 05 99 88 77 66"
nombres = re.findall(r"\d+", texte)   # ['06', '12', ...]

if re.search(r"\d{2}", texte):
    print("contient au moins 2 chiffres")

propre = re.sub(r"\s+", " ", "trop   d'  espaces")
```

Common patterns: `\d` digit, `\w` word character, `\s` whitespace,
`+` one or more, `*` zero or more, `{n}` exactly n times.

## Exercise

Using `re.findall`, extract every whole number from the string
`"il y a 3 chats, 12 chiens et 1 lapin"` as a list of integers in
`nombres`.""",
        },
        "qz-adv": {
            "title": "Quiz: Advanced recap",
            "content": "## Generators and OOP",
            "question": "Which keyword makes a generator?",
            "options": ["return", "yield", "generate", "async"],
            "explanation": (
                "yield « pauses » the function and produces one value at a "
                "time."
            ),
        },
        # ------------------------------------------ parcours « Expert »
        "exp-01": {
            "title": "Context managers (with)",
            "content": """## The `with` protocol

The `with` keyword ensures that a resource is properly released
(file closed, lock released…), even if an error occurs. You can create your
own context manager with `__enter__` and `__exit__`.

```
class Section:
    def __init__(self, nom):
        self.nom = nom
    def __enter__(self):
        print(f"-> entering {self.nom}")
        return self
    def __exit__(self, exc_type, exc, tb):
        print(f"<- leaving {self.nom}")
        return False   # does not swallow exceptions

with Section("bloc"):
    print("work in progress")
```

`contextlib.contextmanager` lets you write one with a simple
generator (a `yield` in the middle).

## Exercise

Write a class `Capture`: its `__enter__` returns an empty list
stored in `self.log`, and the `note(x)` method appends `x` to it.
(The test verifies its usage with `with`.)""",
        },
        "exp-02": {
            "title": "Type hints and dataclasses",
            "content": """## Type annotations

Annotations document expected types (without enforcing them at
runtime) and feed tools like mypy or your IDE.

```
def addition(a: int, b: int) -> int:
    return a + b

prenoms: list[str] = ["Ada", "Alan"]
```

## Dataclasses

`@dataclass` automatically generates `__init__`, `__repr__`, `__eq__`…
from the annotated fields.

```
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)            # Point(x=1, y=2)
print(p == Point(1, 2))  # True
```

## Exercise

Create a dataclass `Livre` with fields `titre: str` and
`pages: int`. The test compares two identical instances.""",
        },
        "exp-03": {
            "title": "Functional programming: functools",
            "content": """## Composing operations

`map`, `filter` and the `functools` module encourage a declarative
style.

```
from functools import reduce

nombres = [1, 2, 3, 4]
produit = reduce(lambda acc, x: acc * x, nombres, 1)   # 24
```

`functools.lru_cache` memoises the results of an expensive function:

```
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))      # instant thanks to the cache
```

## Exercise

Using `reduce`, store in `pgcd_resultat` the GCD (greatest common divisor) of the list
`[48, 36, 60]`. Hint: `math.gcd` calculates the GCD of two numbers.""",
        },
        "exp-04": {
            "title": "Parameterized decorators",
            "content": """## A decorator that takes arguments

For a decorator to accept arguments, we add an extra level of
nesting. `functools.wraps` preserves the original function's name and docstring.

```
import functools

def repeter(n):
    def decorateur(fonction):
        @functools.wraps(fonction)
        def emballage(*args, **kwargs):
            resultat = None
            for _ in range(n):
                resultat = fonction(*args, **kwargs)
            return resultat
        return emballage
    return decorateur

@repeter(3)
def coucou():
    print("hop")

coucou()            # prints "hop" three times
```

## Exercise

Write a parameterized decorator `multiplier(facteur)` that multiplies the
return value of the decorated function by `facteur`.""",
        },
        "exp-05": {
            "title": "Asynchronous Python: async / await",
            "content": """## Cooperative concurrency

`asyncio` allows multiple tasks to run "at the same time" on a single
thread by yielding control while waiting (network, I/O).
An `async def` function is a coroutine; `await` pauses execution until
a result is ready.

```
import asyncio

async def tache(nom, delai):
    await asyncio.sleep(delai)
    return f"{nom} terminée"

async def principal():
    resultats = await asyncio.gather(
        tache("A", 0.1),
        tache("B", 0.1),
    )
    return resultats

print(asyncio.run(principal()))
```

Both tasks run in logical parallelism: the total duration is ~0.1 s,
not 0.2 s.

## Exercise

Complete the coroutine `calcul(x)` so that it returns `x * 10` after
an `await asyncio.sleep(0)`. The test runs it via `asyncio.run`.""",
        },
        "exp-06": {
            "title": "Idioms and best practices",
            "content": """## Writing "Pythonic" code

A few habits that distinguish expert code:

Prefer direct iteration over indexing:
```
for fruit in fruits:        # yes
for i in range(len(fruits)): # avoid
```

`enumerate` when you need both the index AND the value:
```
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

`zip` to iterate over two sequences in parallel:
```
for nom, age in zip(noms, ages):
    ...
```

The ternary operator, truthiness (`if my_list:` rather than
`if len(my_list) > 0:`), f-strings, unpacking: all hallmarks of proficiency.
The ultimate reference is just one command away: `import this`.

## Exercise

In a single line using `zip` and a dictionary comprehension,
build `assoc` which maps each key in `cles` to the value at the same
position in `valeurs`.""",
        },
        "exp-07": {
            "title": "Duck typing and abstract base classes",
            "content": """## “If it quacks like a duck…”

Python does not check types, but **behaviour**: the exact class
does not matter as long as the object has the expected methods. This is
*duck typing*.

To enforce a contract (require specific methods to be present), use
an Abstract Base Class (`ABC`):

```
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        ...

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote
    def aire(self):
        return self.cote ** 2

# Forme() would raise a TypeError: abstract method not implemented
```

## Exercise

Create `Animal` (ABC with abstract method `cri`) and `Chien` which
implements it by returning `"Ouaf"`. The test verifies that `Animal`
cannot be instantiated directly.""",
        },
        "exp-08": {
            "title": "Unit tests (unittest)",
            "content": """## Testing code automatically

The built-in `unittest` module structures tests into classes. Each
`test_*` method checks behaviour using assertions
(`assertEqual`, `assertTrue`, `assertRaises`…).

```
import unittest

def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_positifs(self):
        self.assertEqual(addition(2, 3), 5)
    def test_negatifs(self):
        self.assertEqual(addition(-1, -1), -2)

# In practice we run: python -m unittest
```

Writing tests ensures that future changes will not break
anything (regression testing).

## Exercise

Write the function `inverse(s)` returning the reversed string.
A `unittest` suite will validate it automatically.""",
        },
        "exp-09": {
            "title": "Custom exceptions and chaining",
            "content": """## Custom errors

You define your own exceptions by inheriting from `Exception`. Exception
chaining (`raise ... from ...`) preserves the original cause, which is
invaluable for debugging.

```
class SoldeInsuffisant(Exception):
    pass

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisant(f"manque {montant - solde} €")
    return solde - montant

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("conversion impossible") from e
```

## Exercise

Define an exception `AgeInvalide` and a function `valider_age(n)`
that raises this exception if `n` is negative, and returns `n` otherwise.""",
        },
        "exp-10": {
            "title": "itertools: data pipelines",
            "content": """## Composing data streams

`itertools` provides building blocks to chain operations lazily
(without loading everything into memory).

```
import itertools as it

# Infinite counter, sliced with islice
premiers_pairs = it.islice((n for n in it.count() if n % 2 == 0), 5)
print(list(premiers_pairs))      # [0, 2, 4, 6, 8]

# Group consecutive elements
data = "aaabbbcca"
groupes = [(k, len(list(g))) for k, g in it.groupby(data)]
# [('a', 3), ('b', 3), ('c', 2), ('a', 1)]

# Flatten a list of lists
plat = list(it.chain.from_iterable([[1, 2], [3, 4]]))
```

`accumulate`, `product`, `permutations`, `takewhile` complete the
toolkit.

## Exercise

Using `itertools.accumulate`, store in `cumul` the list of
accumulated sums of `[1, 2, 3, 4]` (that is `[1, 3, 6, 10]`).""",
        },
        "qz-exp": {
            "title": "Quiz: Expert recap",
            "content": "## Expert tools",
            "question": "Which decorator memoises the results of a function?",
            "options": ["@property", "@lru_cache", "@staticmethod", "@wraps"],
            "explanation": "functools.lru_cache caches previously computed results.",
        },
        # ---------------------------- parcours « Scripts & automatisation »
        "scr-01": {
            "title": "What is a script?",
            "content": """## A program you run

A **script** is simply a `.py` file containing a series of
instructions that you execute to accomplish a task: renaming files,
sending a report, cleaning up a folder...

You run it from a **terminal** (command prompt):

```
python my_script.py
```

A good script does **one useful thing**, automatically, without having
to repeat the steps manually. That is the whole point: write it once,
reuse it a thousand times.

A script can receive **arguments** (information passed when launching),
for instance the name of a folder to process. We will see that later;
for now, let's practice with a function.

## Your turn

Write a function `resumer(taches)` that takes a list of tasks
(strings) and returns a sentence formatted like
`3 tâche(s) : ranger, coder, dormir`.""",
        },
        "scr-02": {
            "title": "File paths with pathlib",
            "content": """## Handling paths cleanly

The `pathlib` module represents file paths as objects, and works the
same way across Windows, macOS, and Linux.

```
from pathlib import Path

chemin = Path("dossier") / "photo.png"   # combine with /
print(chemin.name)      # photo.png      (file name)
print(chemin.stem)      # photo          (without extension)
print(chemin.suffix)    # .png           (extension)
print(chemin.parent)    # dossier        (parent folder)
```

A few common actions:

```
Path("rapport.txt").exists()     # True / False: does the file exist?
Path("mon_dossier").mkdir()      # creates a folder
```

`pathlib` prevents path separator issues (`/` vs `\\`) between operating systems.

## Your turn

Write a function `extension(nom_fichier)` that returns the file's
extension (in lowercase, **without the dot**). Example:
`"Rapport.PDF"` → `"pdf"`.""",
        },
        "scr-03": {
            "title": "Reading and writing files",
            "content": """## Saving data

To write to a file, open it in `"w"` (write) mode. The `with` block
ensures the file is properly closed when done.

```
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\\n")
    f.write("Deuxième ligne\\n")
```

To read it back:

```
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())   # .strip() removes the newline
```

Always specify `encoding="utf-8"` to handle accented characters properly.

## Your turn

Write two functions:
- `sauver(chemin, lignes)`: writes each item of `lignes` on its own line in the file;
- `charger(chemin)`: reads the file back and returns the list of lines **without** trailing newlines.""",
        },
        "scr-04": {
            "title": "The JSON format",
            "content": """## Exchanging structured data

**JSON** is the most widespread format for storing and exchanging data
(configurations, web API responses...). It closely resembles Python
dictionaries.

The `json` module translates in both directions:

```
import json

donnees = {"nom": "Ada", "langages": ["Python", "C"]}

# Python -> JSON string
texte = json.dumps(donnees)

# JSON string -> Python
retour = json.loads(texte)
print(retour["nom"])        # Ada
```

To read/write directly from/to a `.json` file, use
`json.dump(obj, fichier)` and `json.load(fichier)`.

## Your turn

You are given a JSON string in `texte`. Decode it and store in `ville`
the value associated with the key `"ville"`.""",
        },
        "scr-05": {
            "title": "Reading a CSV file",
            "content": """## Data tables

A **CSV** (Comma-Separated Values) file is the format used by spreadsheets:
each row is a record, each column is a field. This is typically what you
export from Excel.

The `csv` module reads it cleanly. `DictReader` provides each row as a
dictionary (key = column name):

```
import csv, io

data = "nom,age\\nAda,36\\nAlan,41\\n"
lecteur = csv.DictReader(io.StringIO(data))
for ligne in lecteur:
    print(ligne["nom"], ligne["age"])
```

(Here we read from a string via `io.StringIO`; with a real file, you would
use `open("fichier.csv")` instead.)

## Your turn

From the CSV provided in `data`, calculate the **sum of the ages** in
`total_age` (remember: values read are strings, convert them to `int`).""",
        },
        "scr-06": {
            "title": "Dates, times and scheduling",
            "content": """## Working with time

The `datetime` module manages dates and times, essential for scripts
that sort by date, calculate deadlines, etc.

```
from datetime import date, datetime, timedelta

aujourdhui = date.today()
print(aujourdhui)                 # 2026-06-26

dans_une_semaine = date.today() + timedelta(days=7)

debut = date(2026, 1, 1)
fin = date(2026, 12, 31)
print((fin - debut).days)         # 364 (difference in days)
```

`datetime.now()` gives both date **and** time. You can format the display
with `.strftime("%d/%m/%Y")`.

## Your turn

Calculate in `ecart` the **number of days** between `debut` and `fin`
(an integer).""",
        },
        "qz-scr": {
            "title": "Quiz: Scripts recap",
            "content": "## Automation",
            "question": "Which module reads and writes the JSON format?",
            "options": ["csv", "json", "pickle", "io"],
            "explanation": "The json module converts between Python objects and JSON text.",
        },
        # ----------------------------- parcours « Interfaces graphiques »
        "gui-01": {
            "title": "Your first window",
            "content": """## Programs with buttons

So far our programs only interacted through the console. We can also
create real **windows** with buttons, input fields, etc.
The built-in Python tool for this is called **Tkinter**.

Here is the minimal skeleton of an application. **Copy this code into a
file `app.py` and run it** to see a window appear:

```
import tkinter as tk

fenetre = tk.Tk()                    # creates the main window
fenetre.title("My first app")
fenetre.geometry("300x150")          # width x height

etiquette = tk.Label(fenetre, text="Hello!")
etiquette.pack(pady=20)              # places the text in the window

fenetre.mainloop()                   # displays and waits for events
```

`mainloop()` is the "event loop": it keeps the window open and reacts to clicks.
The program ends when the window is closed.

> ⚠️ Do not run `mainloop()` here in the editor: it is meant for real windows.
> In this workshop, we focus on the **logic** of the apps.

## Your turn

Write a function `texte_accueil(prenom)` that returns the text the label
should display: `Bienvenue, <prenom> !`""",
        },
        "gui-02": {
            "title": "Widgets: labels, fields, buttons",
            "content": """## User interface building blocks

A **widget** is a UI element. The most common ones:

- `Label`: displays text
- `Entry`: an input field where the user types
- `Button`: a clickable button

```
import tkinter as tk

fenetre = tk.Tk()

champ = tk.Entry(fenetre)            # text input zone
champ.pack()

bouton = tk.Button(fenetre, text="Submit")
bouton.pack()

fenetre.mainloop()
```

You **read** what the user typed in an `Entry` with
`champ.get()`, and you **update** a `Label` with
`etiquette.config(text="new text")`.

## Your turn

When the user types text and clicks "Shout", the app should display it in
uppercase with a `!`. Write the function `crier(texte)` that returns the
text in UPPERCASE followed by `!`.
Example: `"bonjour"` → `"BONJOUR!"`.""",
        },
        "gui-03": {
            "title": "Reacting to clicks: callbacks",
            "content": """## Attaching an action to a button

A button triggers a **function** when clicked. You connect it using
the `command` parameter (pass the **name** of the function, without parentheses):

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

On every click, `au_clic` runs: it updates the counter and refreshes the display.
This is the core of interactive applications.

## Your turn

Write the function `incrementer(valeur)` that returns `valeur + 1`
(the logic that a "+1" button would call on every click).""",
        },
        "gui-04": {
            "title": "Laying out widgets",
            "content": """## Arranging the window

Tkinter provides several ways to position widgets:

- `.pack()`: simple stacking (top/bottom or left/right) — quick and simple to start.
- `.grid(row=..., column=...)`: places in a grid (rows / columns) — ideal for forms.

```
import tkinter as tk
fenetre = tk.Tk()

tk.Label(fenetre, text="Name:").grid(row=0, column=0)
tk.Entry(fenetre).grid(row=0, column=1)
tk.Label(fenetre, text="Age:").grid(row=1, column=0)
tk.Entry(fenetre).grid(row=1, column=1)

fenetre.mainloop()
```

You can add spacing with `padx`/`pady`. The key rule is to **choose a single
layout manager** per container (never mix `pack` and `grid` at the same level).

## Your turn

For a form, we want to generate labels. Write `etiquettes(champs)` which
transforms a list of names into a list of labels ending with ` :`. Example:
`["Nom", "Âge"]` → `["Nom :", "Âge :"]`.""",
        },
        "gui-05": {
            "title": "Mini-project: °C → °F converter",
            "content": """## A complete mini-app

Let's bring everything together in a temperature converter. **Copy this code
into a file and run it**: enter degrees Celsius, click the button, and the
Fahrenheit result appears.

```
import tkinter as tk

def convertir():
    try:
        c = float(champ.get())
        f = c * 9 / 5 + 32
        resultat.config(text=f"{c} °C = {f} °F")
    except ValueError:
        resultat.config(text="Enter a valid number")

fenetre = tk.Tk()
fenetre.title("Converter")

champ = tk.Entry(fenetre)
champ.pack(pady=5)
tk.Button(fenetre, text="Convert", command=convertir).pack()
resultat = tk.Label(fenetre, text="")
resultat.pack(pady=5)

fenetre.mainloop()
```

You now have a real application: input, processing, and output.

## Your turn

Write the calculation logic: the function `celsius_vers_fahrenheit(c)` which
applies the formula `c × 9/5 + 32`.""",
        },
        "qz-gui": {
            "title": "Quiz: Graphical interfaces recap",
            "content": "## Tkinter",
            "question": "Which method starts the event loop of a Tkinter window?",
            "options": ["run()", "start()", "mainloop()", "show()"],
            "explanation": "mainloop() displays the window and handles events until it is closed.",
        },
        # ----------------------------------- parcours « Python & le web »
        "web-01": {
            "title": "How the web works",
            "content": """## Client and server

The web is built on a conversation: your browser (the **client**) sends
a **request** to a **server**, which returns a **response** (often
an HTML page or data).

This conversation follows the **HTTP** protocol. A request targets a **URL**:

```
https://api.example.com/cities?country=france&page=2
\\_____/   \\____________/\\____/ \\___________________/
scheme        domain     path       parameters
```

The **parameters** (after the `?`) refine the request: here, cities in
France, page 2. They are formatted as `key=value` and separated by `&`.

Python can act as the client (fetching pages, querying APIs) or the
server (building pages). Let's start by building a URL.

## Your turn

Write `construire_url(base, params)` which combines a base URL with its
query parameters. Example:
`construire_url("https://site.fr/data", {"q": "python", "page": 2})`
→ `"https://site.fr/data?q=python&page=2"`.""",
        },
        "web-02": {
            "title": "Generating HTML",
            "content": """## A web page is text

A web page is simply **text** in HTML format, structured with tags:
`<h1>title</h1>`, `<p>paragraph</p>`, `<ul>` for a list, etc.
Python can generate web pages by building strings.

```
titre = "My groceries"
items = ["bread", "milk", "eggs"]

html = f"<h1>{titre}</h1>"
html += "<ul>"
for item in items:
    html += f"<li>{item}</li>"
html += "</ul>"
```

This is exactly what a web server does: it stitches together HTML to send
back to the browser. Frameworks (covered later) automate this, but the core
idea remains the same.

## Your turn

Write `liste_html(items)` which converts a list into an HTML list.
Example: `["a", "b"]` → `"<ul><li>a</li><li>b</li></ul>"`.""",
        },
        "web-03": {
            "title": "Reading API data",
            "content": """## Fetching online data

Many services expose **APIs**: web endpoints that return **JSON** data
rather than a full visual page. Weather forecasts, currency rates, product
catalogues...

To query an API, Python provides `urllib.request` (built-in) or the
popular `requests` library (installed separately):

```
import urllib.request, json

url = "https://api.example.com/weather"
with urllib.request.urlopen(url) as response:
    data = json.load(response)
print(data["temperature"])
```

The response is JSON: we decode it as seen earlier, then extract the desired
values. Here, to keep tests offline, the JSON response is provided directly.

## Your turn

The variable `texte` contains the JSON response from a cities API.
Extract into `noms` the **list of names** of all the cities.""",
        },
        "web-04": {
            "title": "A mini web server (zero install)",
            "content": """## Serving a page with Python alone

Python includes an `http.server` module that lets you launch a real web
server in a few lines, **without installing anything**. Copy this code
into a file, run it, and open `http://localhost:8000` in your browser:

```
from http.server import HTTPServer, BaseHTTPRequestHandler

class MonServeur(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        page = "<h1>Hello from Python!</h1>"
        self.wfile.write(page.encode("utf-8"))

serveur = HTTPServer(("localhost", 8000), MonServeur)
print("Server running on http://localhost:8000")
serveur.serve_forever()
```

This is the foundation of every dynamic site: receive a request, return
HTML. (`Ctrl+C` in the terminal stops the server.)

## Your turn

Write `page_html(titre, corps)` which returns a full HTML page matching
the exact format:
`<!DOCTYPE html><html><head><title>TITRE</title></head><body>CORPS</body></html>`""",
        },
        "web-05": {
            "title": "Going further: Flask & Django",
            "content": """## Web frameworks

Writing a site "by hand" quickly becomes tedious. **Frameworks** handle
the heavy lifting. The two most popular in Python:

- **Flask**: lightweight, perfect for beginners and small sites/APIs.
- **Django**: batteries-included (database, auth, admin panel...), for
  large-scale applications.

A minimal Flask app looks like this (after `pip install flask`):

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def accueil():
    return "<h1>Welcome</h1>"

@app.route("/contact")
def contact():
    return "<h1>Contact us</h1>"

app.run()
```

Each function (`@app.route`) responds to a **URL path** (route). The
framework routes incoming requests to the appropriate function. That is
the exact **routing** logic you will code below.

## Your turn

Write `router(chemin)` which returns the content depending on the path:
`"/"` → `"Accueil"`, `"/contact"` → `"Contact"`, and **any other path**
→ `"404"`.""",
        },
        "qz-web": {
            "title": "Quiz: Web recap",
            "content": "## The web",
            "question": "In which format do APIs most commonly return their data?",
            "options": ["HTML", "JSON", "PDF", "PNG"],
            "explanation": "APIs typically return JSON, which is easy to parse in Python.",
        },
        # ----------------------------------- parcours « Administrer son PC »
        "adm-01": {
            "title": "System information: os, sys, platform",
            "content": """## Knowing the machine

Several built-in modules provide information about the environment:

```
import platform, os, sys

print(platform.system())            # 'Windows', 'Linux' or 'Darwin' (macOS)
print(platform.python_version())    # '3.12.10'
print(os.getcwd())                  # current working directory
print(sys.argv)                     # command-line arguments passed to the script
```

The `subprocess` module even lets you **run system commands**
(just like in a terminal) from Python:

```
import subprocess
resultat = subprocess.run(["ping", "localhost"], capture_output=True, text=True)
print(resultat.stdout)
```

> Note: in an application bundled as an `.exe`, `sys.executable` points
> to the application itself, not the Python interpreter — something to keep
> in mind if you re-invoke Python via `subprocess`.

## Your turn

Write a function `infos()` that returns a dictionary with two keys:
`"systeme"` (the system name via `platform.system()`) and `"python"`
(the version via `platform.python_version()`).""",
        },
        "adm-02": {
            "title": "Environment variables",
            "content": """## Reading system configuration

**Environment variables** store system and user settings: file paths,
language, user folders, secret API keys... You read them via `os.environ`.

```
import os

# Safe reading with a fallback default if the variable does not exist:
utilisateur = os.environ.get("USER") or os.environ.get("USERNAME")
chemin = os.environ.get("PATH", "")
print(utilisateur)
```

Using `.get(nom, defaut)` rather than `os.environ[nom]` avoids crashing
if the variable is missing. This is a best practice, especially to avoid
hardcoding passwords in source code (place them in environment variables instead).

## Your turn

Write `lire_env(nom, defaut="absente")` that returns the value of the
environment variable `nom`, or `defaut` if it does not exist.""",
        },
        "adm-03": {
            "title": "Iterating through folders",
            "content": """## Exploring the filesystem

`pathlib` lets you list and filter folder contents cleanly.

```
from pathlib import Path

dossier = Path(".")
for element in dossier.iterdir():       # all items
    print(element.name)

# Filter by pattern:
for image in dossier.glob("*.png"):     # all .png files
    print(image)

# Recursive (including subdirectories):
for fichier in dossier.rglob("*.txt"):
    print(fichier)
```

`glob("*.png")` only keeps files matching the pattern. This is the foundation
of every batch sorting, counting, or processing script.

## Your turn

Write `compter_fichiers(dossier, extension)` that returns the **number**
of files with a given extension in the directory. Example:
`compter_fichiers(chemin, ".txt")`.""",
        },
        "adm-04": {
            "title": "Copy, move, delete (shutil)",
            "content": """## Acting on files

The `shutil` module complements `pathlib` for file operations:

```
import shutil

shutil.copy("source.txt", "copie.txt")       # copy
shutil.move("ancien.txt", "dossier/")        # move
shutil.copytree("dossier", "dossier_copie")  # copy an entire directory
```

To delete files or folders, use `pathlib` or `shutil`:

```
from pathlib import Path
Path("inutile.txt").unlink()        # deletes a file
shutil.rmtree("vieux_dossier")      # deletes a folder and all its contents
```

> ⚠️ These operations are **permanent**: no recycle bin. Always test your
> scripts on temporary copies before running them on real files.

## Your turn

Write `sauvegarder(source, destination)` which copies `source` to
`destination` and returns `destination`.""",
        },
        "adm-05": {
            "title": "Mini-project: automatically organize a folder",
            "content": """## A genuinely useful script

Let's combine everything to solve a common nuisance: a cluttered downloads folder.
We will **sort each file into a subfolder named after its extension** (`jpg`, `pdf`, `txt`...).

The plan:
1. iterate over files in the directory;
2. find each file's extension;
3. create the corresponding subfolder if it does not already exist;
4. move the file into it.

```
from pathlib import Path
import shutil

def ranger(dossier):
    base = Path(dossier)
    compte = {}
    for fichier in list(base.iterdir()):
        if fichier.is_file():
            ext = fichier.suffix.lstrip(".").lower() or "sans_extension"
            cible = base / ext
            cible.mkdir(exist_ok=True)
            shutil.move(str(fichier), str(cible / fichier.name))
            compte[ext] = compte.get(ext, 0) + 1
    return compte
```

This is a real script you can use in daily life.

## Your turn

Write the `ranger(dossier)` function described above: it sorts files by
extension (in lowercase) and returns a dictionary
`{extension: number_of_moved_files}`.""",
        },
        "qz-adm": {
            "title": "Quiz: Administration recap",
            "content": "## Managing your computer",
            "question": "Which module is used to copy and move files?",
            "options": ["shutil", "platform", "sys", "time"],
            "explanation": "shutil provides copy(), move(), copytree(), rmtree()…",
        },
        # ---------------------------- parcours « Bases de données (SQLite) »
        "sql-01": {
            "title": "First database",
            "content": """## Storing data for good

A **database** arranges data into **tables** (like spreadsheet sheets)
and lets you query them using the **SQL** language. Python includes
**SQLite**: a complete database engine in a single file, **with zero installation**.

```
import sqlite3

conn = sqlite3.connect("ma_base.db")   # or ":memory:" for an in-RAM database
conn.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)")
conn.commit()                          # commits the changes
conn.close()
```

`execute(...)` sends an SQL statement. `commit()` saves changes. A table
is created with `CREATE TABLE nom (colonne TYPE, ...)`.

## Your turn

Write `creer_table(conn)` which creates a `contacts` table with two
columns: `id` (INTEGER PRIMARY KEY) and `nom` (TEXT).""",
            "hints": [
                "Use conn.execute('CREATE TABLE ...').",
                "Syntax: CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)",
            ],
        },
        "sql-02": {
            "title": "Inserting data (INSERT)",
            "content": """## Adding rows

You insert data with `INSERT INTO table (colonnes) VALUES (...)`. For the
values, use parameterized placeholders `?` (never f-strings: this protects
against SQL injection).

```
conn.execute("INSERT INTO contacts (nom) VALUES (?)", ("Ada",))
conn.commit()
```

The `?` placeholder is replaced by the tuple's value. With multiple columns:
`VALUES (?, ?)` and a 2-element tuple.

## Your turn

Write `ajouter(conn, nom)` which inserts a contact with that `nom` into the
`contacts` table (already created).""",
            "hints": [
                "INSERT INTO contacts (nom) VALUES (?)",
                "Pass the value in a tuple: (nom,) — with the trailing comma.",
            ],
        },
        "sql-03": {
            "title": "Reading data (SELECT)",
            "content": """## Retrieving rows

`SELECT colonnes FROM table` reads data. `execute` returns a cursor that
you can iterate over, or fetch everything at once with `fetchall()`.
Each row is returned as a tuple.

```
cur = conn.execute("SELECT nom FROM contacts ORDER BY id")
for ligne in cur:
    print(ligne[0])
# or: noms = [l[0] for l in cur]
```

`ORDER BY` sorts the result set. `SELECT *` retrieves all columns.

## Your turn

Write `tous_les_noms(conn)` which returns the **list** of names of all
contacts, ordered by `id`.""",
            "hints": [
                "SELECT nom FROM contacts ORDER BY id",
                "Extract the 1st column of each row: ligne[0].",
            ],
        },
        "sql-04": {
            "title": "Filtering (WHERE)",
            "content": """## Keeping only what matters

`WHERE` filters rows based on a condition. `LIKE` supports wildcards
(`%` = any sequence of characters).

```
cur = conn.execute("SELECT nom FROM contacts WHERE nom LIKE ?", ("A%",))
# all names starting with A
```

Other conditions: `WHERE age > 18`, `WHERE ville = ?`, combinable with
`AND` / `OR`.

## Your turn

Write `commencant_par(conn, lettre)` which returns the list of names that
**start** with the given letter (use `LIKE`).""",
            "hints": [
                "WHERE nom LIKE ?",
                "The pattern is lettre + '%' (e.g. 'A%').",
            ],
        },
        "sql-05": {
            "title": "Updating and deleting",
            "content": """## Updating, deleting

`UPDATE` modifies existing rows, `DELETE` removes them. Always remember
the `WHERE` clause, otherwise **the whole table** is affected!

```
conn.execute("UPDATE contacts SET nom = ? WHERE nom = ?", ("Ada L.", "Ada"))
conn.execute("DELETE FROM contacts WHERE nom = ?", ("Alan",))
conn.commit()
```

## Your turn

Write `supprimer(conn, nom)` which removes from the `contacts` table all
rows matching that `nom`.""",
            "hints": [
                "DELETE FROM contacts WHERE nom = ?",
                "Do not forget conn.commit() to persist changes.",
            ],
        },
        "sql-06": {
            "title": "Counting and grouping (GROUP BY)",
            "content": """## Summarizing data

Aggregate functions summarize: `COUNT(*)` counts, `SUM(col)` sums,
`AVG`, `MAX`, `MIN`. `GROUP BY` computes **per group**.

```
cur = conn.execute(
    "SELECT client, SUM(montant) FROM commandes GROUP BY client")
for client, total in cur:
    print(client, total)
```

This is what turns a database into an analytical tool.

## Your turn

A table `commandes(client TEXT, montant INTEGER)` is provided. Write
`total_par_client(conn)` which returns a **dictionary** `{client: total}`.""",
            "hints": [
                "SELECT client, SUM(montant) ... GROUP BY client",
                "Build the dict: {client: total for client, total in cur}.",
            ],
        },
        "qz-sql": {
            "title": "Quiz: SQLite recap",
            "content": "## Databases",
            "question": "Which SQL command retrieves data from a table?",
            "options": ["GET", "SELECT", "FETCH", "OPEN"],
            "explanation": "SELECT columns FROM table reads data.",
        },
        # ----------------------------------- parcours « Dessiner (turtle) »
        "dsn-01": {
            "title": "A turtle that draws",
            "content": """## The turtle module

`turtle` (included with Python) moves a "turtle" that leaves a pen trail:
ideal for learning through visual drawing. **Copy this code into a file and
run it** to see a square drawn:

```
import turtle

t = turtle.Turtle()
for _ in range(4):
    t.forward(100)   # moves forward 100 pixels
    t.right(90)      # turns 90° to the right

turtle.done()        # keeps the window open
```

A square is 4 sides and four 90° turns. For a regular polygon with `n` sides,
the turning angle is **360 / n**.

> As with GUI windows, we focus on the **logic** of drawing here in the
> editor; run the turtle code in a real file to see the visual output.

## Your turn

Write `angle_polygone(n)` which returns the turning angle (in degrees)
required to draw a regular polygon with `n` sides.""",
            "hints": [
                "The exterior angle of a regular polygon is 360 / n.",
                "return 360 / n",
            ],
        },
        "dsn-02": {
            "title": "Moving and turning",
            "content": """## Core commands

The turtle understands a few essential commands:
- `forward(d)` / `backward(d)`: move forward / backward `d` pixels
- `right(a)` / `left(a)`: turn right / left by `a` degrees
- `penup()` / `pendown()`: lift / lower the pen (move without drawing)
- `goto(x, y)`: move to an exact coordinate

```
t.penup(); t.goto(-50, 0); t.pendown()   # positions without drawing
t.forward(100)
```

A drawing can be described as a **series of commands**. Let's represent a
square as a list of instructions `("avance", 100)` / `("tourne", 90)`.

## Your turn

Write `instructions_carre(cote)` which returns the list of commands to
draw a square: for each of the 4 sides, an `("avance", cote)` followed by
a `("tourne", 90)`.""",
            "hints": [
                "Loop 4 times.",
                "On each iteration, append ('avance', cote) then ('tourne', 90).",
            ],
        },
        "dsn-03": {
            "title": "Repeating to create patterns",
            "content": """## Loops: the key to drawing

By repeating a pattern while turning slightly, you get striking figures.
Example of a **spiral** (to run in a standalone file):

```
import turtle
t = turtle.Turtle()
for i in range(1, 40):
    t.forward(i * 5)   # increasingly longer sides
    t.right(90)
turtle.done()
```

Here each side measures `i * 5`: 5, 10, 15, 20… The length grows with each
iteration of the loop.

## Your turn

Write `longueurs_spirale(n, pas)` which returns the list of `n` side
lengths: `pas, 2*pas, 3*pas, …, n*pas`.""",
            "hints": [
                "range(1, n+1) yields 1, 2, …, n.",
                "Multiply each by pas: [i * pas for i in range(1, n+1)]",
            ],
        },
        "dsn-04": {
            "title": "Coordinates and displacement",
            "content": """## Where is the turtle?

The turtle screen is a coordinate plane: `(0, 0)` in the centre, `x` pointing
right, `y` pointing up. When the turtle moves forward `d` pixels at heading
`a` degrees, its new position is computed with trigonometry:

```
import math
nx = x + d * math.cos(math.radians(a))
ny = y + d * math.sin(math.radians(a))
```

`math.radians` converts degrees into radians (expected by `cos` and `sin`).
At 0°, movement is towards the right; at 90°, upwards.

## Your turn

Write `nouvelle_position(x, y, cap, distance)` which returns the tuple
`(nx, ny)` of the new position, with each value **rounded to 3 decimal
places**.""",
            "hints": [
                "Convert heading to radians with math.radians(cap).",
                "nx with cos, ny with sin, then round(..., 3).",
            ],
        },
        "dsn-05": {
            "title": "Mini-project: a rosette",
            "content": """## Composing a figure

A **rosette** is drawn by repeating the same pattern (a circle, a
square…) rotated evenly around a centre. For `n` repetitions, each pattern
is rotated by `360 / n` additional degrees. **Run in a standalone file**:

```
import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(12):
    t.circle(80)        # draws a circle
    t.right(360 / 12)   # turns before the next one
turtle.done()
```

## Your turn

Write `angles_rosace(n)` which returns the list of orientation angles
for each motif: `0, 360/n, 2*360/n, …` (n values).""",
            "hints": [
                "There are n patterns, from #0 to #(n-1).",
                "Pattern angle i: i * 360 / n.",
            ],
        },
        "qz-trt": {
            "title": "Quiz: turtle recap",
            "content": "## Drawing",
            "question": "Which command moves the turtle forward?",
            "options": ["move", "forward", "go", "step"],
            "explanation": "forward(distance) moves the turtle forward.",
        },
        # ----------------- parcours « Algorithmes & structures de données »
        "alg-01": {
            "title": "Linear search",
            "content": """## Searching for an item

The simplest algorithm: scan the list from start to finish until finding
the sought element.

```
def trouver(liste, cible):
    for i, valeur in enumerate(liste):
        if valeur == cible:
            return i
    return -1
```

We return the found **index**, or `-1` if the item is absent. Its complexity
is O(n): in the worst case, we check everything.

## Your turn

Write `trouver(liste, cible)` which returns the index of the first occurrence
of `cible`, or `-1` if not found.""",
            "hints": [
                "enumerate(liste) yields (index, value).",
                "Return i as soon as valeur == cible; otherwise -1 at the end.",
            ],
        },
        "alg-02": {
            "title": "Binary search",
            "content": """## Divide and conquer

On an **already sorted** list, we can do much better than checking every item:
look at the middle element and discard the half that cannot contain the target.
Complexity is O(log n).

```
def recherche_binaire(liste, cible):
    bas, haut = 0, len(liste) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if liste[milieu] == cible:
            return milieu
        elif liste[milieu] < cible:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1
```

## Your turn

Implement `recherche_binaire(liste, cible)` (the list is sorted in ascending
order). Return the index, or `-1`.""",
            "hints": [
                "Maintain two bounds: bas and haut.",
                "Compare the middle element to the target and narrow down the matching half.",
                "milieu = (bas + haut) // 2",
            ],
        },
        "alg-03": {
            "title": "Bubble sort",
            "content": """## Sorting by hand

`sorted()` exists, but understanding **how** sorting works is essential. Bubble
sort compares adjacent elements and swaps them if needed, repeating until
everything is in order.

```
def tri_bulles(liste):
    l = list(liste)            # copy, so we do not modify original
    n = len(l)
    for i in range(n):
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l
```

## Your turn

Implement `tri_bulles(liste)` which returns a **new** list sorted in ascending
order (without using `sorted()`).""",
            "hints": [
                "Work on a copy: l = list(liste).",
                "Two nested loops; swap unordered adjacent pairs.",
                "Python swap: a, b = b, a",
            ],
        },
        "alg-04": {
            "title": "Recursion: factorial",
            "content": """## A function that calls itself

A **recursive** function is defined in terms of itself, with a **base case**
that stops the descent.

```
def factorielle(n):
    if n <= 1:        # base case
        return 1
    return n * factorielle(n - 1)   # recursive case
```

`factorielle(4)` = 4 × 3 × 2 × 1 = 24.

## Your turn

Write `factorielle(n)` **recursively** (n is an integer ≥ 0).""",
            "hints": [
                "Base case: n <= 1 returns 1.",
                "Recursive case: n * factorielle(n - 1).",
            ],
        },
        "alg-05": {
            "title": "Recursion: Fibonacci",
            "content": """## The Fibonacci sequence

Each term is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13…
Two base cases (`fib(0) = 0`, `fib(1) = 1`), then the recursive rule.

```
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

## Your turn

Write `fib(n)` which returns the nth term (`fib(0) = 0`, `fib(1) = 1`).""",
            "hints": [
                "Two base cases: fib(0)=0 and fib(1)=1 (so return n if n < 2).",
                "Otherwise: fib(n-1) + fib(n-2).",
            ],
        },
        "alg-06": {
            "title": "Stack (LIFO)",
            "content": """## Last in, first out

A **stack** works like a pile of plates: you add and remove from the top.
Last In, First Out (LIFO). It is easily implemented with a list.

```
class Pile:
    def __init__(self):
        self.elements = []
    def empiler(self, x):
        self.elements.append(x)
    def depiler(self):
        return self.elements.pop()
    def est_vide(self):
        return len(self.elements) == 0
```

## Your turn

Write the `Pile` class with `empiler(x)`, `depiler()` (returns and removes
the top item) and `est_vide()`.""",
            "hints": [
                "Store items in a list: self.elements.",
                "empiler = append; depiler = pop() (removes the last item).",
            ],
        },
        "alg-07": {
            "title": "Queue (FIFO)",
            "content": """## First in, first out

A **queue** works like a waiting line: you add at the back, and remove from
the front. First In, First Out (FIFO).

```
from collections import deque   # deque is more efficient for a queue

class File:
    def __init__(self):
        self.elements = []
    def enfiler(self, x):
        self.elements.append(x)
    def defiler(self):
        return self.elements.pop(0)
    def est_vide(self):
        return not self.elements
```

## Your turn

Write the `File` class with `enfiler(x)`, `defiler()` (returns and removes
the **first** element) and `est_vide()`.""",
            "hints": [
                "enfiler = append (at the end).",
                "defiler = pop(0) (removes the first item).",
            ],
        },
        "qz-alg": {
            "title": "Quiz: Algorithms recap",
            "content": "## Algorithms",
            "question": "Which algorithm requires the list to be already sorted?",
            "options": [
                "linear search",
                "binary search",
                "bubble sort",
                "full traversal",
            ],
            "explanation": (
                "Binary search eliminates half the remaining items at each "
                "step: it requires the list to be sorted."
            ),
        },
        # ----------------------------- parcours « Manipuler des données »
        "don-01": {
            "title": "Statistics: the mean",
            "content": """## The statistics module

Rather than recalculating everything manually, the built-in **statistics**
module offers standard metrics: `mean`, `median`, `mode`, `stdev` (standard
deviation)…

```
import statistics
print(statistics.mean([10, 20, 30]))   # 20
```

## Your turn

Write `moyenne(valeurs)` which returns the mean, using `statistics.mean`.""",
            "hints": [
                "Call statistics.mean(valeurs).",
                "return statistics.mean(valeurs)",
            ],
        },
        "don-02": {
            "title": "Statistics: the median",
            "content": """## The midpoint of data

The **median** is the middle value once data is sorted: it is much more
resilient to extreme outliers than the mean.

```
import statistics
print(statistics.median([1, 2, 100]))   # 2
```

## Your turn

Write `mediane(valeurs)` with `statistics.median`.""",
            "hints": [
                "Call statistics.median(valeurs).",
                "The function sorts data automatically for you.",
            ],
        },
        "don-03": {
            "title": "Counting with Counter",
            "content": """## Counting in one line

`collections.Counter` tallies occurrences automatically, and extracts the
most frequent ones with `most_common`.

```
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(1))   # [('a', 5)]
```

## Your turn

Write `mot_le_plus_frequent(texte)` which returns the most frequent word
(words separated by spaces).""",
            "hints": [
                "Split the text into words with texte.split().",
                "Counter(...).most_common(1) returns [(word, count)].",
                "The word is at index [0][0].",
            ],
        },
        "don-04": {
            "title": "Grouping with defaultdict",
            "content": """## Effortless grouping

`collections.defaultdict` automatically initializes a default value whenever
a key is missing — ideal for grouping data.

```
from collections import defaultdict
groupes = defaultdict(list)
for mot in ["ada", "alan", "bob"]:
    groupes[mot[0]].append(mot)
# {'a': ['ada', 'alan'], 'b': ['bob']}
```

## Your turn

Write `grouper_par_initiale(mots)` which returns a (standard) **dictionary**
mapping each initial letter to its corresponding list of words.""",
            "hints": [
                "defaultdict(list) creates an empty list for each new key.",
                "The key is the initial letter mot[0].",
                "Convert to a standard dict at the end: dict(groupes).",
            ],
        },
        "don-05": {
            "title": "Reading a CSV",
            "content": """## The spreadsheet format

**CSV** (Comma-Separated Values) is the most ubiquitous data exchange
format. The `csv` module parses it for you; with `DictReader`, each row
becomes a dictionary.

```
import csv, io
texte = "nom,age\\nAda,30\\nBob,25\\n"
for ligne in csv.DictReader(io.StringIO(texte)):
    print(ligne["nom"], ligne["age"])
```

(`io.StringIO` lets a string behave like a file.)

## Your turn

Write `lire_csv(texte)` which returns the **list of rows** as dictionaries.""",
            "hints": [
                "Wrap the text with io.StringIO(texte).",
                "csv.DictReader(...) yields one dict per row; convert to list.",
            ],
        },
        "don-06": {
            "title": "Aggregating data",
            "content": """## Summarizing a table

Once data is loaded, we **aggregate** it: totals per category, averages
per group… This is the core of data analysis.

You receive a list of rows (dictionaries) with keys `ville` and `ventes`
(strings, as read from a CSV).

## Your turn

Write `total_par_ville(lignes)` which returns a dictionary
`{ville: total_sales}` (remember to convert sales to integer).""",
            "hints": [
                "Iterate through rows and accumulate into a dict.",
                "totaux.get(ville, 0) gives 0 if the city has not been seen yet.",
                "Convert sales with int(...).",
            ],
        },
        "qz-don": {
            "title": "Quiz: Data manipulation recap",
            "content": "## Working with data",
            "question": "Which object counts occurrences in one line?",
            "options": ["list", "Counter", "set", "tuple"],
            "explanation": "collections.Counter counts automatically and provides the most common elements.",
        },
        # ---------------------------------------- parcours « Tests & TDD »
        "tdd-01": {
            "title": "assert: the basic building block",
            "content": """## Verifying an assertion

`assert` checks that a condition is true. If it is, nothing happens; if
not, the program stops with an `AssertionError`. This is the foundation
of all tests.

```
assert 2 + 2 == 4        # ok, nothing happens
assert "abc".upper() == "ABC"
```

## Your turn

Write `aire_rectangle(largeur, hauteur)` which returns the area. Your
tests (below, invisible) will verify several cases.""",
            "hints": [
                "The area of a rectangle is largeur × hauteur.",
                "return largeur * hauteur",
            ],
        },
        "tdd-02": {
            "title": "Reading a test as a specification",
            "content": """## Tests describe what needs to be done

With `unittest`, we group checks inside a class. This test **specifies**
the expected behaviour of the `prix_ttc` function:

```
import unittest

class TestPrix(unittest.TestCase):
    def test_tva_20(self):
        self.assertEqual(prix_ttc(100, 20), 120)
    def test_zero(self):
        self.assertEqual(prix_ttc(0, 20), 0)
```

No guessing needed: tests tell you exactly what to code.
`prix_ttc(ht, taux)` adds `taux` % to the pre-tax price.

## Your turn

Implement `prix_ttc(ht, taux)` to satisfy the specification.""",
            "hints": [
                "Adding taux % means adding ht * taux / 100.",
                "return ht + ht * taux / 100",
            ],
        },
        "tdd-03": {
            "title": "Thinking about edge cases",
            "content": """## Edge cases: where bugs hide

A good test suite covers "normal" cases **and** edge cases: empty lists,
zero/null values, duplicates… `maximum(liste)` must return the largest
element, but what should happen if the list is empty? Here: return `None`.

## Your turn

Write `maximum(liste)` which returns the largest element, or `None` if
the list is empty.""",
            "hints": [
                "Handle the empty list case first: if not liste: return None.",
                "Otherwise, max(liste) does the job.",
            ],
        },
        "tdd-04": {
            "title": "Red, green, refactor",
            "content": """## The TDD cycle

In **TDD** (Test-Driven Development), we first write a failing test
(*red*), then write the minimal code to make it pass (*green*), and finally
clean it up (*refactor*). Let's implement `palindrome(mot)`: true if the
word reads the same forwards and backwards (ignoring case).

```
class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(palindrome("kayak"))
    def test_casse(self):
        self.assertTrue(palindrome("Radar"))
    def test_non(self):
        self.assertFalse(palindrome("python"))
```

## Your turn

Write `palindrome(mot)` (case-insensitive).""",
            "hints": [
                "Convert the word to lowercase with .lower().",
                "A reversed string is written mot[::-1].",
                "Compare the word to its reverse.",
            ],
        },
        "tdd-05": {
            "title": "Writing your own tests",
            "content": """## Your turn to write tests

Now it's your turn to write the tests. The `inverser` function is already
written. Fill in the `____` blanks with the **expected results** so that
all assertions pass (a correct test verifies a true condition!).

Hint: `inverser("abc")` returns `"cba"`.""",
            "hints": [
                "inverser reverses the string: \"abc\" → \"cba\".",
                "An empty string reversed remains empty: \"\".",
                "\"Python\" reversed gives \"nohtyP\".",
            ],
        },
        "qz-tdd": {
            "title": "Quiz: Tests & TDD recap",
            "content": "## Tests & TDD",
            "question": "Which standard library module is used to write tests?",
            "options": ["pytest", "unittest", "nose", "checker"],
            "explanation": "unittest is built into Python; pytest and nose are external packages.",
        },
        # ---------------------------------------- parcours « Projets guidés »
        "proj-pendu": {
            "title": "Project: Hangman game",
            "content": """## Let's build a real game

**Hangman**: the computer picks a word, the player guesses letters, and
loses a life on each mistake. We will build it **step by step**, in the form
of small functions that you validate one by one.

Here is the complete game once assembled (copy it into a file to play it
in your terminal):

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

Now it's your turn to code each piece. Use the **Exercise 1, 2, 3** buttons
above to switch from one step to the next.""",
            "exercices": [
                {
                    "prompt": "Step 1 — masquer(mot, trouvees): returns the word with "
                              "'_' in place of letters not yet guessed. "
                              "Ex.: masquer(\"python\", {\"p\", \"o\"}) → \"p___o_\".",
                    "hints": [
                        "Iterate through each letter of the word.",
                        "If the letter is in trouvees, keep it, otherwise put '_'.",
                        "Use \"\".join(...) with a comprehension.",
                    ],
                },
                {
                    "prompt": "Step 2 — est_gagne(mot, trouvees): returns True if ALL "
                              "letters of the word have been found.",
                    "hints": [
                        "The all(...) function returns True if everything is true.",
                        "Check that each letter of the word is in trouvees.",
                    ],
                },
                {
                    "prompt": "Step 3 — jouer(etat, lettre): updates the game state. "
                              "etat is a dict {\"mot\", \"trouvees\" (set), \"vies\" (int)}. "
                              "If the letter is in the word, add it to trouvees; "
                              "otherwise decrement vies by 1. Return etat.",
                    "hints": [
                        "Test: if lettre in etat[\"mot\"].",
                        "Add with etat[\"trouvees\"].add(lettre).",
                        "Else: etat[\"vies\"] -= 1.",
                    ],
                },
            ],
        },
        "proj-todo": {
            "title": "Project: To-do list",
            "content": """## Managing tasks

We build the core of a **to-do list** application. Each task is a small
dictionary `{"texte": ..., "fait": False}`. We code the three core operations,
then combine them.

Complete console app once the functions are written (copy into a file to run):

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

Code the three functions below (buttons **Exercise 1, 2, 3**).""",
            "exercices": [
                {
                    "prompt": "Step 1 — ajouter(taches, texte): appends a new task "
                              "{\"texte\": texte, \"fait\": False} to the list and returns the list.",
                    "hints": [
                        "Create a dictionary with keys texte and fait.",
                        "Use taches.append({...}).",
                    ],
                },
                {
                    "prompt": "Step 2 — basculer(taches, index): toggles the 'fait' boolean status "
                              "of the task at that index, then returns the list.",
                    "hints": [
                        "Access the task: taches[index].",
                        "Invert a boolean with not: ... = not ...",
                    ],
                },
                {
                    "prompt": "Step 3 — restantes(taches): returns the number of tasks "
                              "NOT yet completed.",
                    "hints": [
                        "Count tasks where \"fait\" is False.",
                        "sum(1 for t in taches if not t[\"fait\"]).",
                    ],
                },
            ],
        },
        "proj-blocnotes": {
            "title": "Project: mini notepad (Tkinter)",
            "content": """## A text editor with menu

We build a real **notepad**: a text area, and buttons to open and save
a file. Copy this code into a file and run it to get a working application:

```
import tkinter as tk
from tkinter import filedialog

fenetre = tk.Tk()
fenetre.title("Notepad")

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
tk.Button(barre, text="Open", command=ouvrir).pack(side="left")
tk.Button(barre, text="Save", command=enregistrer).pack(side="left")

fenetre.mainloop()
```

Let's add **text processing tools**. Code the three functions below (which
would power a word count and find/replace feature).""",
            "exercices": [
                {
                    "prompt": "Step 1 — compter_mots(texte): returns the number of words "
                              "(separated by spaces).",
                    "hints": [
                        "texte.split() splits on whitespace.",
                        "len(...) counts the resulting pieces.",
                    ],
                },
                {
                    "prompt": "Step 2 — compter_lignes(texte): returns the number of lines "
                              "(0 if the text is empty).",
                    "hints": [
                        "Number of lines = number of newlines + 1.",
                        "Be careful with empty text which must return 0.",
                        "texte.count(\"\\n\") counts newlines.",
                    ],
                },
                {
                    "prompt": "Step 3 — remplacer(texte, ancien, nouveau): returns the text "
                              "with all occurrences of 'ancien' replaced with 'nouveau' "
                              "(the Find & Replace feature).",
                    "hints": [
                        "Strings have a .replace(ancien, nouveau) method.",
                        "return texte.replace(ancien, nouveau)",
                    ],
                },
            ],
        },
        "proj-devises": {
            "title": "Project: currency converter",
            "content": """## Converting amounts

We build the core of a **currency converter**: a conversion function,
clean formatted output, and the reverse rate calculation. Example console
app (to copy into a file):

```
TAUX = {"USD": 1.08, "GBP": 0.85}   # 1 EUR = ... currency

montant = float(input("Amount in euros: "))
devise = input("Currency (USD/GBP): ")
resultat = round(montant * TAUX[devise], 2)
print(f"{montant} EUR = {resultat:.2f} {devise}")
```

Code the three building blocks below (buttons **Exercise 1, 2, 3**).""",
            "exercices": [
                {
                    "prompt": "Step 1 — convertir(montant, taux): returns montant × taux, "
                              "rounded to 2 decimal places.",
                    "hints": [
                        "Multiply montant by taux.",
                        "round(..., 2) rounds to 2 decimal places.",
                    ],
                },
                {
                    "prompt": "Step 2 — formater(montant, devise): returns a string "
                              "with 2 decimal places and the currency code. Ex.: formater(12.5, \"USD\") "
                              "→ \"12.50 USD\".",
                    "hints": [
                        "An f-string with formatting: f\"{montant:.2f}\".",
                        "Add a space and the currency name.",
                    ],
                },
                {
                    "prompt": "Step 3 — taux_inverse(taux): returns the reciprocal rate "
                              "(1 / taux), rounded to 4 decimal places.",
                    "hints": [
                        "The reciprocal of rate is 1 / rate.",
                        "round(1 / taux, 4)",
                    ],
                },
            ],
        },
        "proj-vie": {
            "title": "Project: Conway's Game of Life",
            "content": """## Living and dying cells

The **Game of Life** simulates a grid of cells (1 = alive, 0 = dead) that
evolves according to simple rules based on the number of living neighbours
(out of the 8 surrounding cells):

- a **living** cell survives if it has **2 or 3** neighbours, otherwise it dies;
- a **dead** cell becomes alive if it has **exactly 3** neighbours.

Console display of a generation (to copy into a file):

```
def afficher(grille):
    for ligne in grille:
        print("".join("█" if c else " " for c in ligne))
```

We code the simulation step by step (buttons **Exercise 1, 2, 3**).""",
            "exercices": [
                {
                    "prompt": "Step 1 — compter_voisins(grille, i, j): counts living "
                              "neighbours (1) among the 8 cells surrounding (i, j). "
                              "Watch out for grid boundaries.",
                    "hints": [
                        "Iterate over offsets di, dj in (-1, 0, 1).",
                        "Skip (0, 0) — that is the cell itself.",
                        "Check that ni and nj stay within the grid bounds before adding.",
                    ],
                },
                {
                    "prompt": "Step 2 — prochaine_cellule(vivante, voisins): applies the "
                              "rules. Returns 1 (alive) or 0 (dead) in the next generation. "
                              "vivante is 1 or 0.",
                    "hints": [
                        "If alive: survives with 2 or 3 neighbours.",
                        "If dead: born with exactly 3 neighbours.",
                    ],
                },
                {
                    "prompt": "Step 3 — etape(grille): returns the NEW grid after one "
                              "generation (without modifying the old one). A vertical blinker "
                              "should become horizontal.",
                    "hints": [
                        "Build a NEW grid, do not mutate the old one.",
                        "For each cell: count neighbours, apply rules.",
                        "Survives (2-3 neighbours) / born (exactly 3).",
                    ],
                },
            ],
        },
        "proj-motdepasse": {
            "title": "Project: securing a password",
            "content": """## Never store passwords in plain text

A secure application **never** stores plain text passwords. It stores an
irreversible cryptographic **hash**. The standard method: `pbkdf2_hmac`
(in `hashlib`), with a random **salt** (unique per user) and many
iterations to slow down brute-force attacks.

```
import hashlib, os

sel = os.urandom(16)               # random salt, stored alongside the hash
empreinte = hashlib.pbkdf2_hmac("sha256", "secret".encode(), sel, 100000)
print(empreinte.hex())
```

To verify a password, re-hash the user's input with the **same salt** and
compare hashes. We will code that, along with a small strength checker.""",
            "exercices": [
                {
                    "prompt": "Step 1 — hacher(mot_de_passe, sel): returns the hexadecimal "
                              "hash via pbkdf2_hmac('sha256', ..., sel, 100000). "
                              "mot_de_passe is a string, sel is bytes.",
                    "hints": [
                        "Encode password to bytes with .encode().",
                        "hashlib.pbkdf2_hmac('sha256', ..., sel, 100000).hex()",
                    ],
                },
                {
                    "prompt": "Step 2 — verifier(mot_de_passe, sel, empreinte): returns True "
                              "if the password matches the hash (by re-hashing it).",
                    "hints": [
                        "Re-hash password with the same salt.",
                        "Compare computed hash to provided hash.",
                    ],
                },
                {
                    "prompt": "Step 3 — est_robuste(mot_de_passe): returns True if the password "
                              "is at least 8 characters long AND contains at least one digit "
                              "AND at least one letter.",
                    "hints": [
                        "any(c.isdigit() for c in mot_de_passe) checks for a digit.",
                        "Combine the three conditions with and.",
                    ],
                },
            ],
        },
        # ------------------- parcours « Entraînement (débogage & trous) »
        "dbg-01": {
            "title": "Debug: the missing upper bound",
            "content": """## Reading code, finding the error

Knowing how to **fix** code is just as important as writing it. Here, the
function is supposed to sum all integers from 1 to `n` inclusive… but
it stops one step short. Find the bug and fix it.

Method hint: test `somme_jusqua(5)` with "Run", compare to the expected
result (15), and check the loop's upper bound.""",
            "hints": [
                "range(1, n) stops at n-1: the last value is missing.",
                "You need to go up to n inclusive: range(1, n + 1).",
            ],
        },
        "dbg-02": {
            "title": "Debug: the inverted condition",
            "content": """## Backwards logic

`est_pair(n)` should return `True` when `n` is even. Yet it answers the
exact opposite. Identify the faulty comparison and fix it.""",
            "hints": [
                "n % 2 is 0 for an even number, 1 for an odd number.",
                "Compare the remainder to 0, not to 1.",
            ],
        },
        "dbg-03": {
            "title": "Debug: off-by-one index",
            "content": """## When Python raises an error

`dernier(liste)` should return the **last** element. But running it
crashes with an `IndexError`. Read the error message (click "Run"): it tells
you the index is out of bounds. Fix the index calculation.

Remember: list indexes range from 0 to `len(liste) - 1`.""",
            "hints": [
                "The last valid index is len(liste) - 1.",
                "You can also write liste[-1].",
            ],
        },
        "tro-01": {
            "title": "Fill in: the f-string",
            "content": """## Filling in the blanks

Sometimes, almost everything is written: only a small detail is missing.
Replace the `____` so that the function returns the right greeting.

Expected example: `saluer("Ada")` should return `"Bonjour Ada !"`. """,
            "hints": [
                "Inside an f-string, expressions inside { } are evaluated.",
                "Place the parameter nom between the curly braces.",
            ],
        },
        "tro-02": {
            "title": "Fill in: the accumulator",
            "content": """## The missing operator

The function sums all numbers in a list. Replace `____` with the correct
operator so that the total is built properly.""",
            "hints": [
                "We want to add each number to the total.",
                "The addition operator is +.",
            ],
        },
        "tro-03": {
            "title": "Fill in: the comparison",
            "content": """## The right condition

`mention(note)` returns `"réussi"` if the mark is greater than or equal to
10, and `"échec"` otherwise. Replace `____` with the right comparison
operator (note: 10 counts as passing).""",
            "hints": [
                "\"greater than or equal\" is written >=.",
                "With >, a mark of 10 would be rejected incorrectly: use >=.",
            ],
        },
        "pre-01": {
            "title": "Predict: plus does not always mean add",
            "content": """## Read before running

The surest way to improve is to **predict** what a program will do,
and then check. If your prediction is wrong, you've just learned something
precise.

Here, the `+` sign appears three times — but behaves differently depending
on its operands.""",
            "explanation": (
                "Between quotes, '2' and '3' are TEXT: '+' concatenates "
                "them (23) and '*' repeats ('222'). Without quotes, they "
                "are numbers, and '+' adds them (5)."
            ),
        },
        "pre-02": {
            "title": "Predict: the loop that changes nothing",
            "content": """## A very common trap

This loop looks like it multiplies each number by 10. Look carefully at
what is printed **at the end**, and ask yourself what `n` really represents
inside the loop.""",
            "explanation": (
                "`n` is a COPY of the value, not the slot in the list: "
                "modifying it does not alter `nombres`. To mutate the list, "
                "you must write into it, for instance with `nombres[i] = ...`."
            ),
        },
        "ord-01": {
            "title": "Put in order: summing a list",
            "content": """## Finding the structure

The lines of a working program have been shuffled. Put them back in the
correct order so that it prints the sum of the numbers.

Think about what must exist **before** being used: you cannot add to a
total before creating it.""",
        },
        "ord-02": {
            "title": "Put in order: a function with a condition",
            "content": """## Function ordering

Here indentation gives you clues: indented lines belong **inside** a block.
A function must also be defined before it is called.""",
        },
        "qz-err": {
            "title": "Quiz: Decoding errors recap",
            "content": "## Reading an error\n\nOne last check of the reflex.",
            "question": "In an error message, which line should you start with?",
            "options": [
                "The first line of the Traceback",
                "The last line, giving the type and the explanation",
                "The copied line of code",
                "The line number",
            ],
            "explanation": (
                "Always read the last line first: it names the error and "
                "explains it. The rest of the Traceback then helps you find "
                "where the call came from."
            ),
        },
        # ------------------------------------------ Track 17: Cybersecurity
        "cybersecurite": {"title": "17 · Cybersecurity & Cryptography"},
        "sec-01": {
            "title": "Hashing and constant-time comparison",
            "content": """## Hashing with hashlib

A cryptographic hash function converts any data into a fixed-size digital footprint
(e.g., SHA-256 generates 64 hexadecimal characters). It is one-way: reversing the hash
to find the original password is computationally impossible.

```python
import hashlib
import hmac

h = hashlib.sha256(b"my_password").hexdigest()
```

## Timing attacks

Comparing two strings with `==` stops at the first mismatch: an attacker can
measure response times to guess passwords character by character! To prevent this,
we use `hmac.compare_digest()` which always takes **constant time**.

## Your turn

Write `verifier_signature(cle_attendue, cle_recue)` which compares two strings
using `hmac.compare_digest` and returns a boolean.""",
            "hints": [
                "Use hmac.compare_digest(cle_attendue, cle_recue).",
                "Make sure both arguments are of the same type (str or bytes)."
            ],
        },
        "sec-02": {
            "title": "Generating true cryptographic secrets",
            "content": """## The pitfall of the random module

The standard `random` module uses a pseudo-random generator (Mersenne Twister)
meant for simulations, not security. By observing a few outputs, an attacker can
predict future numbers!

For session tokens, API keys, and password resets, Python provides the `secrets` module:

```python
import secrets

token = secrets.token_hex(16)        # 32 hex characters (16 bytes)
url_safe = secrets.token_urlsafe(16) # safe for URLs
secure_num = secrets.randbelow(100)  # integer from 0 to 99
```

## Your turn

Write `generer_jetons(n, nb_octets=16)` that returns a list of `n` unique hex
tokens generated with `secrets.token_hex(nb_octets)`.""",
            "hints": [
                "Use a list comprehension or loop.",
                "[secrets.token_hex(nb_octets) for _ in range(n)]"
            ],
        },
        "sec-03": {
            "title": "Symmetric XOR encryption",
            "content": """## The XOR (exclusive OR) operator

At the core of symmetric encryption lies the binary XOR operator (`^`).
Its key property: `(A ^ B) ^ B == A`. Encrypting a byte with a key and then
re-applying the same key restores the original message!

In Python, byte sequences are manipulated using `bytes` or `bytearray`:

```python
text = b"Hello"
mask = 42
encrypted = bytes([byte ^ mask for byte in text])
decrypted = bytes([byte ^ mask for byte in encrypted]) # b"Hello"
```

## Your turn

Write `chiffrer_xor(donnees: bytes, masque: int) -> bytes` which applies the
XOR mask `masque` to every byte in `donnees` and returns the resulting `bytes`.""",
            "hints": [
                "Transform each byte b with b ^ masque.",
                "Pass the generator or list to bytes(...)."
            ],
        },
        "sec-04": {
            "title": "Preventing SQL injections",
            "content": """## Never concatenate into SQL queries!

A SQL injection occurs when unsanitized user input is directly concatenated into a SQL string:

```python
# DANGEROUS: a login like 'admin -- bypasses password verification!
cursor.execute(f"SELECT * FROM users WHERE username = '{login}'")
```

The gold standard is using **parameterized queries** with `?`. The database engine
treats parameters purely as literal values, never as executable code.

```python
cursor.execute("SELECT * FROM users WHERE username = ?", (login,))
```

## Your turn

Write `preparer_insertion_utilisateur(nom, email, role)` that returns a tuple
`(requete_sql, parametres)` where:
- `requete_sql` is `'INSERT INTO users (nom, email, role) VALUES (?, ?, ?)'`
- `parametres` is the tuple `(nom, email, role)`.""",
            "hints": [
                "Use ? placeholders for substitution values.",
                "Return (sql, (nom, email, role))."
            ],
        },
        "sec-05": {
            "title": "Blocking Path Traversal attacks",
            "content": """## What is Path Traversal?

If your application allows downloading files based on a user-provided name, an attacker
could supply `../../../../etc/passwd` or `..\\..\\Windows\\win.ini` to escape the directory.

With `pathlib`, resolve absolute paths with `.resolve()` and verify that the target
stays inside the authorized directory using `.is_relative_to()` (or `.relative_to()`):

```python
from pathlib import Path

base = Path("/var/www/uploads").resolve()
target = (base / filename).resolve()

if not target.is_relative_to(base):
    raise PermissionError("Access forbidden!")
```

## Your turn

Write `est_chemin_sur(dossier_racine, chemin_demande)` which returns `True` if
the resolved target path is strictly inside `dossier_racine`, and `False` otherwise.""",
            "hints": [
                "Use Path(dossier_racine).resolve() and (base / chemin_demande).resolve().",
                "Check cible.relative_to(base) inside a try/except ValueError block."
            ],
        },
        "sec-06": {
            "title": "Brute-force attack detection",
            "content": """## Analyzing authentication logs

A brute force attack tests thousands of passwords sequentially. To detect it,
we inspect authentication logs and flag IP addresses with excessive consecutive failures.

Given logs like:
`[{"ip": "192.168.1.10", "succes": False}, {"ip": "192.168.1.10", "succes": True}]`

## Your turn

Write `detecter_bruteforce(logs, seuil_echecs=3)` which returns a set of IP
addresses that have accumulated at least `seuil_echecs` failures (`"succes": False`).""",
            "hints": [
                "Count failed logins per IP.",
                "Filter IPs whose fail count reaches or exceeds seuil_echecs."
            ],
        },
        "qz-sec": {
            "title": "Quiz: Cybersecurity recap",
            "content": "## Security principles",
            "question": "Why should you use `secrets` instead of `random` for security tokens?",
            "options": [
                "secrets is faster in computation time.",
                "random is predictable (pseudo-random) and not cryptographically secure.",
                "random can only generate integers and not text.",
                "secrets automatically encrypts variables in RAM.",
            ],
            "explanation": (
                "The random module uses the Mersenne Twister which is deterministic. "
                "The secrets module pulls cryptographically secure entropy from the OS."
            ),
        },
        # ------------------------------------------ Track 18: Math & Science
        "maths_sciences": {"title": "18 · Mathematics, Science & Simulation"},
        "mat-01": {
            "title": "Prime numbers & Sieve of Eratosthenes",
            "content": """## The Sieve of Eratosthenes

A prime number is an integer greater than 1 divisible only by 1 and itself.
To find all primes up to `n`, the Sieve of Eratosthenes systematically eliminates
multiples of each newly discovered prime:

```python
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [i for i, p in enumerate(is_prime) if p]
```

## Your turn

Write `premiers_jusqua(n)` which returns an ordered list of all prime numbers
less than or equal to `n`.""",
            "hints": [
                "Create a boolean list of size n + 1 initialized to True.",
                "Set indices 0 and 1 to False, then cross off multiples."
            ],
        },
        "mat-02": {
            "title": "Exact precision with Decimal and Fraction",
            "content": """## The floating-point precision issue

In binary computing, simple decimals cannot always be represented exactly
(e.g., `0.1 + 0.2` produces `0.30000000000000004`).

For financial and scientific precision, Python includes `decimal` and `fractions`:

```python
from decimal import Decimal
from fractions import Fraction

# Exact currency precision (always pass numbers as strings!)
price = Decimal("0.1") + Decimal("0.2") # Decimal('0.3')

# Exact fractions without rounding error
f = Fraction(1, 3) + Fraction(1, 6)    # Fraction(1, 2)
```

## Your turn

Write `calculer_total_facture(prix_lignes: list[str], taux_tva: str) -> Decimal`
which sums the prices as `Decimal` instances, applies the VAT tax rate (e.g. `"0.20"`),
and returns the total as a `Decimal`.""",
            "hints": [
                "Convert each string price with Decimal(p).",
                "Total = HT * (1 + VAT)."
            ],
        },
        "mat-03": {
            "title": "Monte-Carlo Simulation (Estimating Pi)",
            "content": r"""## Estimating Pi with randomness

Imagine a quarter circle of radius 1 inscribed inside a 1x1 square.
The area of the square is 1, and the quarter circle area is \(\pi / 4\).

By generating \(N\) random points \((x, y)\) inside the square, the proportion of
points falling inside the circle (\(x^2 + y^2 \le 1\)) approximates \(\pi / 4\):
\[ \pi \approx 4 \times \frac{\text{points in circle}}{\text{total points}} \]

## Your turn

Write `estimer_pi(points: list[tuple[float, float]]) -> float` that counts points
satisfying \(x^2 + y^2 \le 1.0\) and returns \(4 \times \frac{\text{in}}{\text{total}}\).
Return `0.0` if points is empty.""",
            "hints": [
                "Check x*x + y*y <= 1.0 for each (x, y) point.",
                "Return 4.0 * in_count / len(points)."
            ],
        },
        "mat-04": {
            "title": "Vector math & Dot product",
            "content": r"""## Vectors in geometry and physics

A vector \(\vec{u} = (x_1, y_1)\) and a vector \(\vec{v} = (x_2, y_2)\) have the dot product:
\[ \vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 \]

Two non-zero vectors are **orthogonal** (perpendicular) if and only if their
dot product is zero (\(\vec{u} \cdot \vec{v} = 0\)).

## Your turn

Write two functions:
1. `produit_scalaire(u, v) -> float`: calculates \(\sum u_i v_i\).
2. `sont_orthogonaux(u, v) -> bool`: returns `True` if the dot product is approximately zero (tolerance `1e-9`).""",
            "hints": [
                "Use zip(u, v) to pair components.",
                "sum(a * b for a, b in zip(u, v))"
            ],
        },
        "mat-05": {
            "title": "Root finding by Bisection (Dichotomy)",
            "content": r"""## Finding the root of f(x) = 0

If a continuous function \(f\) changes sign across an interval \([a, b]\)
(\(f(a) \times f(b) \le 0\)), the Intermediate Value Theorem guarantees at least
one root \(c\) where \(f(c) = 0\).

The bisection method bisects the interval at \(m = (a + b) / 2\) at each step
until reaching the desired tolerance.

## Your turn

Write `resoudre_dichotomie(f, a, b, precision=1e-5)` which returns an approximate
root \(x\) where \(f(x) \approx 0\).""",
            "hints": [
                "While (b - a) > precision, compute midpoint m = (a + b) / 2.",
                "If f(a) * f(m) <= 0 then b = m, else a = m."
            ],
        },
        "mat-06": {
            "title": "Collatz Conjecture (3n + 1)",
            "content": r"""## The Syracuse sequence

For any positive integer \(n\):
- If even, divide by 2 (\(n / 2\)).
- If odd, multiply by 3 and add 1 (\(3n + 1\)).

The conjecture states that repeating this process always reaches 1.

Example for 6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

## Your turn

Write `vol_syracuse(n: int) -> list[int]` that returns the full sequence of
numbers visited starting from `n` down to 1 inclusive.""",
            "hints": [
                "Start with [n].",
                "In a while n > 1 loop, append the next value."
            ],
        },
        "qz-mat": {
            "title": "Quiz: Mathematics recap",
            "content": "## Floating point and precision",
            "question": "What is the reason behind `0.1 + 0.2 != 0.3` in standard Python floats?",
            "options": [
                "A known bug in the CPython interpreter.",
                "The impossibility of representing certain decimal fractions in finite binary format (IEEE 754).",
                "Python always rounding down by default.",
                "RAM hardware memory limitations.",
            ],
            "explanation": (
                "Binary computers represent floating point numbers in base 2. "
                "Just like 1/3 has no finite decimal representation in base 10 (0.333...), "
                "1/10 has no finite binary representation in base 2."
            ),
        },
        # ------------------------------------------ Track 19: Multimedia
        "multimedia": {"title": "19 · Image & Audio Processing"},
        "med-01": {
            "title": "Structure of an RGB pixel",
            "content": """## How digital color works

On a screen, every pixel combines three color channels:
- **R**: Red (0 to 255)
- **G**: Green (0 to 255)
- **B**: Blue (0 to 255)

Examples:
- `(255, 0, 0)` = Pure Red
- `(255, 255, 255)` = White
- `(0, 0, 0)` = Black

To **invert** a color (photo negative effect), subtract each channel from 255:
`255 - r`, `255 - g`, `255 - b`.

## Your turn

Write `inverser_pixel(r: int, g: int, b: int) -> tuple[int, int, int]` which
returns the inverted negative color tuple.""",
            "hints": [
                "Compute 255 - r, 255 - g, 255 - b.",
                "Return (255 - r, 255 - g, 255 - b)."
            ],
        },
        "med-02": {
            "title": "Generating images in pure Python (PPM Format)",
            "content": """## The Netpbm PPM (P3) format

You can create real image files without installing any external library like Pillow.
The standard **PPM (Portable Pixmap)** format is plain ASCII text!

Structure:
```text
P3
# width height
2 2
# max color value
255
# R G B triplets
255 0 0    0 255 0
0 0 255    255 255 0
```

## Your turn

Write `generer_ppm_uni(largeur: int, hauteur: int, couleur: tuple[int, int, int]) -> str`
that creates and returns the full PPM text for a solid single-color image.""",
            "hints": [
                "Start with header f'P3\\n{largeur} {hauteur}\\n255'.",
                "Repeat the color string across all rows."
            ],
        },
        "med-03": {
            "title": "Image filters: Grayscale luminance",
            "content": r"""## The luminance formula

The human eye is much more sensitive to green than red or blue. To convert
color to realistic grayscale, use the standard luminance formula (ITU-R BT.601):
\[ Y = 0.299 \times R + 0.587 \times G + 0.114 \times B \]

## Your turn

Write `pixel_vers_gris(r: int, g: int, b: int) -> tuple[int, int, int]` which
computes the rounded luminance and returns `(gris, gris, gris)`.""",
            "hints": [
                "val = round(0.299 * r + 0.587 * g + 0.114 * b)",
                "Return (val, val, val)."
            ],
        },
        "med-04": {
            "title": "Generating checkerboard patterns",
            "content": """## Matrix coordinates (row, col)

A 2D image grid can generate a checkerboard by inspecting the parity of `(row + col)`:
`color1 if (row + col) % 2 == 0 else color2`

## Your turn

Write `generer_grille_damier(taille: int, c1: tuple, c2: tuple) -> list[list[tuple]]`
which returns a `taille x taille` 2D list alternating `c1` and `c2`.""",
            "hints": [
                "Use nested list comprehensions across range(taille).",
                "c1 if (i + j) % 2 == 0 else c2"
            ],
        },
        "med-05": {
            "title": "Audio synthesis: Sampling a sine wave",
            "content": r"""## Digital audio & sine waves

A pure musical tone (e.g. A4 440 Hz) is a sine wave of frequency \(f\):
\[ s(t) = A \times \sin(2 \pi f t) \]

At a sampling rate of 44100 Hz, we sample 44100 times per second:

```python
import math

freq = 440.0
rate = 44100
duration = 1.0
samples = [
    int(32767 * math.sin(2 * math.pi * freq * (i / rate)))
    for i in range(int(rate * duration))
]
```

## Your turn

Write `echantillonner_sinus(frequence: float, duree_sec: float, taux=44100, amplitude=10000) -> list[int]`
that returns the list of sampled integer values.""",
            "hints": [
                "Total samples = int(taux * duree_sec).",
                "Compute int(amplitude * math.sin(2 * math.pi * frequence * (i / taux)))."
            ],
        },
        "med-06": {
            "title": "Programming a melody",
            "content": """## Concatenating musical notes

Each musical note has a physical frequency (A4 = 440 Hz, C4 = 261.63 Hz...).
A sheet score can be represented as a list of `(frequency, duration_sec)` tuples.

## Your turn

Write `concatener_partition(partition: list[tuple[float, float]], taux=1000) -> list[int]`
which returns the concatenated audio samples for the full melody (amplitude = 10000).""",
            "hints": [
                "Iterate over (freq, duration) pairs.",
                "Generate samples for each note and append to the result."
            ],
        },
        "qz-med": {
            "title": "Quiz: Multimedia recap",
            "content": "## Netpbm and PPM",
            "question": "What is unique about the Netpbm (PPM P3) image format?",
            "options": [
                "It uses proprietary lossless vector compression.",
                "It is a human-readable ASCII text format created without external libraries.",
                "It strictly requires Pillow to be installed.",
                "It only supports monochrome black and white images.",
            ],
            "explanation": (
                "PPM (P3) is plain ASCII text with a simple header followed by decimal RGB triplets, "
                "making it ideal for creating images using pure standard Python."
            ),
        },
        # ------------------------------------------ Track 20: AI & Machine Learning
        "ia_ml": {"title": "20 · Artificial Intelligence (from scratch)"},
        "ia-01": {
            "title": "k-Nearest Neighbors (k-NN)",
            "content": r"""## Classification by proximity

The **k-NN** algorithm classifies a new data point by finding the `k` closest
known data points in Euclidean space and taking the majority class.

Euclidean distance:
\[ d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} \]

## Your turn

Write `knn_classifier(points_connus: list[tuple[float, float, str]], point_cible: tuple[float, float], k=3) -> str`
which calculates distances, selects the `k` closest, and returns the most frequent label.""",
            "hints": [
                "Compute distance ((x - xt)**2 + (y - yt)**2)**0.5 for each known point.",
                "Sort by distance, take the top k, and use Counter to find the majority."
            ],
        },
        "ia-02": {
            "title": "Linear Regression by Least Squares",
            "content": r"""## Finding the trendline y = ax + b

Linear regression predicts a continuous value by minimizing squared errors:
\[ a = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} \]
\[ b = \bar{y} - a \bar{x} \]

## Your turn

Write `regression_lineaire(points: list[tuple[float, float]]) -> tuple[float, float]`
that calculates and returns `(a, b)` as floats.""",
            "hints": [
                "Calculate x_bar and y_bar first.",
                "Compute numerator and denominator sums."
            ],
        },
        "ia-03": {
            "title": "Decision Tree logic",
            "content": """## Branching rule engines

A decision tree classifies data by evaluating a series of conditional rules (if/else).

Rules for loan evaluation:
1. If income < 1500 -> `"refus"`
2. Else if has debts and down payment < 5000 -> `"refus"`
3. Otherwise -> `"accord"`

## Your turn

Write `evaluer_pret(revenu: float, apport: float, a_dettes: bool) -> str`
that implements these rules and returns `"accord"` or `"refus"`.""",
            "hints": [
                "Check income < 1500 first.",
                "Then check a_dettes and apport < 5000."
            ],
        },
        "ia-04": {
            "title": "The Perceptron (Artificial Neuron)",
            "content": r"""## The foundation of Neural Networks

A perceptron calculates a weighted sum of inputs plus a bias:
\[ z = \sum_{i} x_i w_i + b \]

If \(z \ge 0\), the neuron activates and returns `1`, otherwise `0`.

## Your turn

Write `activer_perceptron(entrees: list[float], poids: list[float], biais: float) -> int`
that computes \(z = \sum x_i w_i + b\) and returns `1` if \(z \ge 0\) else `0`.""",
            "hints": [
                "Use zip(entrees, poids) to sum products.",
                "Return 1 if z >= 0 else 0."
            ],
        },
        "ia-05": {
            "title": "Text Sentiment Analysis",
            "content": """## Classifying emotional tone

Lexicon-based sentiment analysis scores a text by subtracting negative word count
from positive word count:
- Score > 0 -> `"positif"`
- Score < 0 -> `"negatif"`
- Score == 0 -> `"neutre"`

## Your turn

Write `analyser_sentiment(texte: str, mots_positifs: set, mots_negatifs: set) -> str`
that tokenizes lowercase words and returns `"positif"`, `"negatif"`, or `"neutre"`.""",
            "hints": [
                "Use re.findall(r'\\w+', texte.lower()) to extract clean words.",
                "Count positive and negative occurrences."
            ],
        },
        "ia-06": {
            "title": "Recommendation engine (Cosine Similarity)",
            "content": r"""## Comparing user preferences

To measure similarity between two preference vectors:
\[ \text{similarity}(u, v) = \frac{u \cdot v}{\|u\| \|v\|} \]

A score of `1.0` indicates identical preferences.

## Your turn

Write `similarite_cosinus(u: list[float], v: list[float]) -> float` that returns
the cosine similarity between two vectors (return `0.0` if any norm is zero).""",
            "hints": [
                "Compute dot product sum(a * b for a, b in zip(u, v)).",
                "Divide by math.sqrt(sum(a*a)) * math.sqrt(sum(b*b))."
            ],
        },
        "qz-ia": {
            "title": "Quiz: Artificial Intelligence recap",
            "content": "## Machine Learning fundamentals",
            "question": "In the k-Nearest Neighbors (k-NN) algorithm, what does 'k' represent?",
            "options": [
                "The number of dimensions in the dataset.",
                "The number of closest neighbors consulted for the majority vote.",
                "The learning rate of the optimization step.",
                "The number of neurons in the hidden layer.",
            ],
            "explanation": (
                "k represents the number of closest data points examined to determine "
                "the majority classification label."
            ),
        },
        # ------------------------------------------ Track 21: Networks
        "reseaux": {"title": "21 · Networks & Protocols"},
        "net-01": {
            "title": "IP addresses and Ports",
            "content": """## Machine identification on a network

Network communication requires:
1. **IP Address** (e.g. `192.168.1.1` or `127.0.0.1`): identifies the host.
2. **Port** (e.g. `80` HTTP, `443` HTTPS): identifies the listening application.

The `ipaddress` module validates IP addresses in standard Python.

## Your turn

Write `analyser_adresse(hote_port: str, port_defaut=80) -> tuple[str, int]` that
splits a string like `"192.168.1.1:8080"` into `(host, port_int)`.""",
            "hints": [
                "Check if ':' is in hote_port.",
                "Use rsplit(':', 1) and int(port)."
            ],
        },
        "net-02": {
            "title": "Framing with delimited JSON",
            "content": """## Why frame stream data?

TCP sockets deliver a continuous byte stream without message boundaries.
Adding a `\\n` delimiter allows reliable message reconstruction.

## Your turn

Write two functions:
1. `encoder_trame(donnees: dict) -> bytes`: serializes to JSON utf-8 with trailing `\\n`.
2. `decoder_trame(paquet_octets: bytes) -> dict`: decodes and parses JSON.""",
            "hints": [
                "json.dumps(donnees).encode('utf-8') + b'\\n'",
                "json.loads(paquet_octets.decode('utf-8').strip())"
            ],
        },
        "net-03": {
            "title": "Decoding raw HTTP requests",
            "content": """## Anatomy of HTTP/1.1 requests

The first line of an HTTP request is structured as: `METHOD PATH VERSION`.

## Your turn

Write `parser_ligne_requete(ligne_brute: str) -> dict` that parses `"GET /api/users HTTP/1.1"`
into `{"methode": "GET", "chemin": "/api/users", "version": "HTTP/1.1"}`.""",
            "hints": [
                "Strip whitespace and split().",
                "Map parts to methode, chemin, version."
            ],
        },
        "net-04": {
            "title": "Testing port connectivity (Sockets)",
            "content": """## The socket module

`socket.create_connection((host, port), timeout)` tests whether a TCP port is reachable.

## Your turn

Write `formater_statut_port(hote: str, port: int, est_ouvert: bool) -> str` that
returns `f"{hote}:{port} -> OUVERT"` if open, else `f"{hote}:{port} -> FERME"`.""",
            "hints": [
                "Use ternary condition 'OUVERT' if est_ouvert else 'FERME'.",
                "Format string with f'{hote}:{port} -> {statut}'."
            ],
        },
        "net-05": {
            "title": "Private subnets and loopback addresses",
            "content": """## RFC 1918 Private ranges

Private IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `127.0.0.1`)
are non-routable on the public Internet.

## Your turn

Write `est_adresse_locale(ip_str: str) -> bool` using `ipaddress.ip_address`
returning `True` if private or loopback, `False` otherwise.""",
            "hints": [
                "Use ipaddress.ip_address(ip_str) in try/except ValueError.",
                "Return ip.is_private or ip.is_loopback."
            ],
        },
        "net-06": {
            "title": "Chat server message broadcasting",
            "content": """## Broadcasting to connected clients

When a client sends a message, a chat server broadcasts it to all other active clients.

## Your turn

Write `diffuser_message(clients: list, expediteur, message: str) -> list[tuple[str, str]]`
that returns `[(recipient, f"[{expediteur}] {message}"), ...]` for all other clients.""",
            "hints": [
                "Format f'[{expediteur}] {message}'.",
                "Filter clients where c != expediteur."
            ],
        },
        "qz-net": {
            "title": "Quiz: Networks recap",
            "content": "## Sockets and TCP",
            "question": "Why do TCP socket protocols require delimiters (like '\\n') or length headers?",
            "options": [
                "Because TCP requires all payloads to be ASCII.",
                "Because TCP is a continuous byte stream with no application message boundaries.",
                "To automatically encrypt network packets.",
                "To force routers to retransmit dropped packets.",
            ],
            "explanation": (
                "TCP delivers a stream of bytes without message boundaries. "
                "Delimiters or length headers allow the receiver to segment discrete messages."
            ),
        },
        # ------------------------------------------ Track 22: Video Games
        "jeux_video": {"title": "22 · Game Architecture & 2D Logic"},
        "gam-01": {
            "title": "Game loop & Delta Time",
            "content": r"""## The Game Loop

A game loop updates game state 60 times per second. Multiplying velocities by
**Delta Time** (`dt`) guarantees consistent movement speeds across all display refresh rates:
\[ \text{new\_pos} = \text{pos} + \text{velocity} \times dt \]

## Your turn

Write `calculer_nouvelle_position(x: float, vx: float, dt: float) -> float`.""",
            "hints": [
                "Apply x + vx * dt.",
                "Return float result."
            ],
        },
        "gam-02": {
            "title": "2D Grid movement and collision detection",
            "content": """## Grid traversal

Given a 2D tilemap where `'.'` is walkable and `'#'` is a solid wall:
prevent movement into walls or out-of-bounds cells.

## Your turn

Write `deplacer_joueur(grille: list[str], x: int, y: int, dx: int, dy: int) -> tuple[int, int]`
which returns `(nx, ny)` if walkable, else `(x, y)`.""",
            "hints": [
                "Compute nx = x + dx, ny = y + dy.",
                "Verify boundary constraints and check grille[ny][nx] != '#'."
            ],
        },
        "gam-03": {
            "title": "Inventory systems & Weight capacity",
            "content": """## RPG Inventory management

An inventory contains `[{"nom": ..., "poids": ..., "quantite": ...}]` with a max weight limit.

## Your turn

Write `ajouter_au_sac(sac: list[dict], nom: str, poids_unitaire: float, quantite: int, capacite_max=20.0) -> bool`.""",
            "hints": [
                "Sum existing item weights.",
                "Reject if total exceeds capacite_max, otherwise update quantity or append."
            ],
        },
        "gam-04": {
            "title": "Turn-based combat damage calculation",
            "content": r"""## Damage formulas with critical hits

\[ \text{damage} = \max(1, \text{attack} - \text{defense}) \times (\text{2 if critical else 1}) \]

HP cannot fall below 0.

## Your turn

Write `subir_attaque(pv_actuels: int, attaque: int, defense: int, est_critique=False) -> int`.""",
            "hints": [
                "degats = max(1, attaque - defense)",
                "Double if critical, return max(0, pv_actuels - degats)."
            ],
        },
        "gam-05": {
            "title": "Enemy pursuit AI",
            "content": """## Chasing the player

A basic pursuit AI moves one step along each axis towards the player.

## Your turn

Write `pas_poursuite(monstre: tuple[int, int], joueur: tuple[int, int]) -> tuple[int, int]`
returning `(dx, dy)` where each component is `-1`, `0`, or `1`.""",
            "hints": [
                "Compare xm with xj for dx (-1, 0, 1).",
                "Compare ym with yj for dy (-1, 0, 1)."
            ],
        },
        "gam-06": {
            "title": "Game save/load with JSON",
            "content": """## Serializing game state

Serialize game progress into JSON strings for persistent saves.

## Your turn

Write `sauvegarder_partie(joueur_nom, score, objets)` and `charger_partie(json_str)`.""",
            "hints": [
                "json.dumps({'nom': ..., 'score': ..., 'objets': ...})",
                "json.loads(json_str)"
            ],
        },
        "qz-gam": {
            "title": "Quiz: Video Games recap",
            "content": "## Game loop architecture",
            "question": "What is the purpose of Delta Time (dt) in a game loop?",
            "options": [
                "To increase game difficulty over time.",
                "To maintain identical movement speed regardless of monitor refresh rate (FPS).",
                "To compress textures in GPU VRAM.",
                "To calculate magic damage formulas.",
            ],
            "explanation": (
                "By scaling movements by the real elapsed time between frames (dt), "
                "motion remains smooth and speed-consistent across 30, 60, or 144 Hz displays."
            ),
        },
        # ------------------------------------------ Track 23: Design Patterns
        "design_patterns": {"title": "23 · Design Patterns & Modern Typing"},
        "pat-01": {
            "title": "The Factory pattern",
            "content": """## Decoupling object instantiation

The Factory pattern delegates object creation to a specialized creator.

## Your turn

Write `Voiture` (with `type() -> 'voiture'`), `Moto` (with `type() -> 'moto'`), and
`fabrique_vehicule(nom: str)` returning the matching instance (or raising `ValueError`).""",
            "hints": [
                "Implement type(self) on both classes.",
                "Return Voiture() or Moto() based on nom."
            ],
        },
        "pat-02": {
            "title": "The Observer pattern (Event Emitter)",
            "content": """## Decoupling event publishers and subscribers

The Observer pattern notifies registered callbacks whenever an event triggers.

## Your turn

Write `GestionnaireEvenements` with `__init__`, `abonner(callback)`, and `emettre(donnees)`.""",
            "hints": [
                "Store callbacks in a list.",
                "Call cb(donnees) on all listeners during emettre."
            ],
        },
        "pat-03": {
            "title": "The Strategy pattern",
            "content": """## Interchangeable algorithms

The Strategy pattern allows swapping calculation algorithms dynamically.

## Your turn

Write `CalculateurPrix(strategie)` with method `calculer(prix_base: float) -> float`.""",
            "hints": [
                "Save self.strategie in __init__.",
                "Return self.strategie(prix_base) in calculer."
            ],
        },
        "pat-04": {
            "title": "Abstract Base Classes (abc.ABC)",
            "content": """## Enforcing interface contracts

Use `@abstractmethod` from `abc` to mandate child class implementations.

## Your turn

Define abstract `Notificateur(ABC)` with `@abstractmethod def envoyer(self, message)`
and concrete subclass `NotificateurEmail(Notificateur)` returning `f"[EMAIL] {message}"`.""",
            "hints": [
                "Decorate with @abstractmethod.",
                "Implement def envoyer(self, message): return f'[EMAIL] {message}' in NotificateurEmail."
            ],
        },
        "pat-05": {
            "title": "Structural typing with Protocol (Duck Typing)",
            "content": """## Static Duck Typing with typing.Protocol

`typing.Protocol` defines interfaces by structure rather than inheritance.

## Your turn

Define `Sauvegardable(Protocol)` with `sauvegarder(self) -> bool: ...`
and `sauvegarder_tous(elements: list) -> bool`.""",
            "hints": [
                "Use all(e.sauvegarder() for e in elements).",
                "Return True for empty lists."
            ],
        },
        "pat-06": {
            "title": "Robust enumerations with Enum",
            "content": """## Replacing magic strings with enum.Enum

Named constants eliminate typo bugs in application state.

## Your turn

Create `NiveauAlerte(Enum)` with `INFO = 1`, `ATTENTION = 2`, `CRITIQUE = 3`
and `est_urgent(niveau: NiveauAlerte) -> bool` returning `True` for `CRITIQUE`.""",
            "hints": [
                "Declare members INFO = 1, ATTENTION = 2, CRITIQUE = 3 in NiveauAlerte(Enum).",
                "Return niveau == NiveauAlerte.CRITIQUE."
            ],
        },
        "qz-pat": {
            "title": "Quiz: Design Patterns recap",
            "content": "## Protocols and ABCs",
            "question": "What is the core difference between `abc.ABC` and `typing.Protocol` in Python?",
            "options": [
                "Protocol is slower at runtime than ABC.",
                "ABC enforces explicit nominal subclassing, while Protocol enables static structural Duck Typing.",
                "ABC only works with functions, not classes.",
                "Protocol cannot support type hints.",
            ],
            "explanation": (
                "ABC validates formal subclass inheritance, whereas typing.Protocol checks structural "
                "conformance (methods and attributes) without forcing inheritance."
            ),
        },
    },
}


def appliquer(curriculum):
    """Injecte les traductions dans le curriculum, sous la forme « champ_langue ».

    Les leçons ne sont pas dupliquées : on leur ajoute simplement les
    champs traduits, que content.traduit() servira quand l'interface est
    dans cette langue. Idempotent — rappeler la fonction ne fait rien de
    plus.
    """
    for langue, entrees in TRADUCTIONS.items():
        for niveau in curriculum:
            for element in [niveau] + list(niveau["lessons"]):
                champs = entrees.get(element.get("id"))
                if not champs:
                    continue
                for champ, valeur in champs.items():
                    element[f"{champ}_{langue}"] = valeur
                    if champ == "exercices" and isinstance(valeur, list) and "exercices" in element:
                        for idx, exo_trad in enumerate(valeur):
                            if idx < len(element["exercices"]):
                                for k, v in exo_trad.items():
                                    element["exercices"][idx][f"{k}_{langue}"] = v
    return curriculum
