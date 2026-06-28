"""
Un quiz (QCM) de fin pour chaque parcours.

Ces leçons sont injectées automatiquement à la fin du parcours
correspondant par content/__init__.py — inutile de modifier les
fichiers de cours.
"""

QUIZ = {
    "debutant": {
        "id": "qz-deb", "type": "quiz",
        "title": "Quiz : récap Débutant",
        "content": "## Vérifie tes bases\n\nUne petite question pour clore le parcours.",
        "question": "Que renvoie len(\"Python\") ?",
        "options": ["5", "6", "7", "une erreur"],
        "answer": 1,
        "explanation": "« Python » compte 6 caractères, donc len vaut 6.",
    },
    "intermediaire": {
        "id": "qz-int", "type": "quiz",
        "title": "Quiz : récap Intermédiaire",
        "content": "## Structures de données",
        "question": "Quelle structure ne contient que des valeurs uniques ?",
        "options": ["list", "tuple", "set", "str"],
        "answer": 2,
        "explanation": "Un set (ensemble) élimine automatiquement les doublons.",
    },
    "avance": {
        "id": "qz-adv", "type": "quiz",
        "title": "Quiz : récap Avancé",
        "content": "## Générateurs et POO",
        "question": "Quel mot-clé fabrique un générateur ?",
        "options": ["return", "yield", "generate", "async"],
        "answer": 1,
        "explanation": "yield « met en pause » la fonction et produit une valeur à la fois.",
    },
    "expert": {
        "id": "qz-exp", "type": "quiz",
        "title": "Quiz : récap Expert",
        "content": "## Outils experts",
        "question": "Quel décorateur mémorise les résultats d'une fonction ?",
        "options": ["@property", "@lru_cache", "@staticmethod", "@wraps"],
        "answer": 1,
        "explanation": "functools.lru_cache met en cache les résultats déjà calculés.",
    },
    "scripts": {
        "id": "qz-scr", "type": "quiz",
        "title": "Quiz : récap Scripts",
        "content": "## Automatisation",
        "question": "Quel module lit et écrit le format JSON ?",
        "options": ["csv", "json", "pickle", "io"],
        "answer": 1,
        "explanation": "Le module json convertit entre objets Python et texte JSON.",
    },
    "interfaces": {
        "id": "qz-gui", "type": "quiz",
        "title": "Quiz : récap Interfaces",
        "content": "## Tkinter",
        "question": "Quelle méthode lance la boucle d'événements d'une fenêtre Tkinter ?",
        "options": ["run()", "start()", "mainloop()", "show()"],
        "answer": 2,
        "explanation": "mainloop() affiche la fenêtre et réagit aux clics jusqu'à sa fermeture.",
    },
    "web": {
        "id": "qz-web", "type": "quiz",
        "title": "Quiz : récap Web",
        "content": "## Le web",
        "question": "Sous quel format les API renvoient-elles le plus souvent leurs données ?",
        "options": ["HTML", "JSON", "PDF", "PNG"],
        "answer": 1,
        "explanation": "Les API renvoient généralement du JSON, facile à décoder en Python.",
    },
    "admin": {
        "id": "qz-adm", "type": "quiz",
        "title": "Quiz : récap Administration",
        "content": "## Administrer son PC",
        "question": "Quel module sert à copier et déplacer des fichiers ?",
        "options": ["shutil", "platform", "sys", "time"],
        "answer": 0,
        "explanation": "shutil fournit copy(), move(), copytree(), rmtree()…",
    },
    "sqlite": {
        "id": "qz-sql", "type": "quiz",
        "title": "Quiz : récap SQLite",
        "content": "## Bases de données",
        "question": "Quelle commande SQL récupère des données dans une table ?",
        "options": ["GET", "SELECT", "FETCH", "OPEN"],
        "answer": 1,
        "explanation": "SELECT colonnes FROM table lit les données.",
    },
    "turtle": {
        "id": "qz-trt", "type": "quiz",
        "title": "Quiz : récap turtle",
        "content": "## Dessin",
        "question": "Quelle instruction fait avancer la tortue ?",
        "options": ["move", "forward", "go", "step"],
        "answer": 1,
        "explanation": "forward(distance) fait avancer la tortue.",
    },
}
