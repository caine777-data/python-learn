"""Glossaire : termes essentiels, consultable dans l'application."""

GLOSSAIRE_FR = [
    ("Variable", "Un nom associé à une valeur, comme une étiquette sur une "
                 "boîte. Ex. : age = 30."),
    ("Fonction", "Un bloc de code réutilisable, défini avec def, qui peut "
                 "recevoir des paramètres et renvoyer un résultat avec return."),
    ("Paramètre / Argument", "Le paramètre est la variable déclarée par la "
                 "fonction ; l'argument est la valeur réellement passée à l'appel."),
    ("Chaîne (string)", "Du texte, entre guillemets. Type str. Ex. : \"Bonjour\"."),
    ("Entier (int)", "Un nombre sans virgule. Ex. : 42."),
    ("Flottant (float)", "Un nombre à virgule. Ex. : 3.14."),
    ("Booléen (bool)", "Une valeur vraie ou fausse : True ou False."),
    ("Liste", "Une collection ordonnée et modifiable, entre crochets. "
              "Ex. : [1, 2, 3]."),
    ("Tuple", "Une collection ordonnée mais NON modifiable, entre parenthèses. "
              "Ex. : (1, 2)."),
    ("Dictionnaire (dict)", "Une collection de paires clé→valeur, entre "
              "accolades. Ex. : {\"nom\": \"Ada\"}."),
    ("Ensemble (set)", "Une collection non ordonnée de valeurs uniques. "
              "Ex. : {1, 2, 3}."),
    ("Boucle", "Une structure qui répète du code : for (sur une série) ou "
               "while (tant qu'une condition est vraie)."),
    ("Condition", "Un choix dans le programme avec if / elif / else."),
    ("Indentation", "Le décalage (4 espaces) qui délimite les blocs de code. "
                    "Essentiel en Python."),
    ("Module", "Une boîte à outils prête à l'emploi qu'on charge avec import. "
               "Ex. : import math."),
    ("Méthode", "Une fonction attachée à un objet, appelée avec un point. "
                "Ex. : texte.upper()."),
    ("Exception", "Une erreur survenue à l'exécution. On la gère avec "
                  "try / except."),
    ("f-string", "Une chaîne préfixée par f où l'on insère des variables "
                 "entre accolades. Ex. : f\"{nom} a {age} ans\"."),
    ("Indice (index)", "La position d'un élément dans une séquence, à partir "
                       "de 0. Ex. : liste[0] est le premier."),
    ("Objet", "Une donnée qui regroupe des valeurs (attributs) et des actions "
              "(méthodes). La POO consiste à créer ses propres types d'objets."),
    ("Classe", "Le « moule » qui décrit comment fabriquer des objets, défini "
               "avec class."),
    ("return", "Le mot-clé qui renvoie un résultat depuis une fonction et "
               "termine son exécution."),
    ("API", "Une adresse web qui renvoie des données (souvent en JSON) plutôt "
            "qu'une page à afficher."),
    ("JSON", "Un format texte pour échanger des données structurées, proche "
             "des dictionnaires Python."),
]

GLOSSAIRE_EN = [
    ("Variable", "A name bound to a value, like a label on a box. Ex.: age = 30."),
    ("Function", "A reusable block of code, defined with def, that can accept "
                 "parameters and return a result with return."),
    ("Parameter / Argument", "A parameter is the variable declared by the "
                 "function; an argument is the actual value passed in the call."),
    ("String (str)", "Text enclosed in quotes. Type str. Ex.: \"Hello\"."),
    ("Integer (int)", "A whole number without a decimal point. Ex.: 42."),
    ("Float (float)", "A number with a decimal point. Ex.: 3.14."),
    ("Boolean (bool)", "A truth value: True or False."),
    ("List", "An ordered and mutable collection, enclosed in square brackets. "
             "Ex.: [1, 2, 3]."),
    ("Tuple", "An ordered but IMMUTABLE collection, enclosed in parentheses. "
              "Ex.: (1, 2)."),
    ("Dictionary (dict)", "A collection of key→value pairs, enclosed in curly "
              "braces. Ex.: {\"name\": \"Ada\"}."),
    ("Set (set)", "An unordered collection of unique values. Ex.: {1, 2, 3}."),
    ("Loop", "A control structure that repeats code: for (over an iterable) or "
             "while (as long as a condition is true)."),
    ("Condition", "A decision branch in the program using if / elif / else."),
    ("Indentation", "The spacing (4 spaces) defining code blocks. Essential in Python."),
    ("Module", "A ready-to-use toolbox loaded with import. Ex.: import math."),
    ("Method", "A function attached to an object, called with dot notation. "
               "Ex.: text.upper()."),
    ("Exception", "A runtime error. Handled with try / except."),
    ("f-string", "A string prefixed with f where variables/expressions are "
                 "inserted inside curly braces. Ex.: f\"{name} is {age} years old\"."),
    ("Index", "The position of an item in a sequence, starting at 0. "
              "Ex.: list[0] is the first item."),
    ("Object", "A data structure combining state (attributes) and behaviour "
               "(methods). OOP consists of creating custom object types."),
    ("Class", "The blueprint describing how to construct objects, defined with class."),
    ("return", "The keyword that outputs a value from a function and terminates its execution."),
    ("API", "A web endpoint that returns structured data (often in JSON) rather than a webpage."),
    ("JSON", "A text format for exchanging structured data, very similar to Python dictionaries."),
]

GLOSSAIRE = GLOSSAIRE_FR


def get_glossaire(lang="fr"):
    """Renvoie le glossaire dans la langue demandée (par défaut français)."""
    return GLOSSAIRE_EN if lang == "en" else GLOSSAIRE_FR

