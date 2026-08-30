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
    return curriculum
