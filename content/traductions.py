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
