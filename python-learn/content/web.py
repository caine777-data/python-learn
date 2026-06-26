"""Parcours 7 — Python & le web."""

LEVEL = {
    "id": "web",
    "title": "7 · Python & le web",
    "lessons": [
        {
            "id": "web-01",
            "title": "Comment marche le web",
            "content": """## Client et serveur

Le web repose sur un dialogue : ton navigateur (le **client**) envoie
une **requête** à un **serveur**, qui renvoie une **réponse** (souvent
une page HTML ou des données).

Ce dialogue suit le protocole **HTTP**. Une requête vise une **URL** :

```
https://api.exemple.fr/villes?pays=france&page=2
\\_____/   \\____________/\\____/ \\___________________/
schéma        domaine    chemin      paramètres
```

Les **paramètres** (après le `?`) précisent la demande : ici, les
villes de France, page 2. Ils s'écrivent `clé=valeur` et se séparent
par des `&`.

Python peut jouer le client (récupérer des pages, interroger des API)
ou le serveur (fabriquer des pages). On commence par construire une URL.

## À toi

Écris `construire_url(base, params)` qui assemble une URL avec ses
paramètres. Exemple :
`construire_url("https://site.fr/data", {"q": "python", "page": 2})`
→ `"https://site.fr/data?q=python&page=2"`.""",
            "starter": "def construire_url(base, params):\n    ...\n",
            "check": 'assert construire_url("https://site.fr/data", {"q": "python", "page": 2}) == "https://site.fr/data?q=python&page=2"\n'
                     'assert construire_url("http://a.b", {"x": 1}) == "http://a.b?x=1"\n',
            "solution": 'def construire_url(base, params):\n'
                        '    return base + "?" + "&".join(f"{c}={v}" for c, v in params.items())\n',
        },
        {
            "id": "web-02",
            "title": "Générer du HTML",
            "content": """## Une page web est du texte

Une page web n'est rien d'autre que du **texte** au format HTML, fait
de balises : `<h1>titre</h1>`, `<p>paragraphe</p>`, `<ul>` pour une
liste, etc. Python peut donc fabriquer des pages en construisant des
chaînes.

```
titre = "Mes courses"
items = ["pain", "lait", "œufs"]

html = f"<h1>{titre}</h1>"
html += "<ul>"
for item in items:
    html += f"<li>{item}</li>"
html += "</ul>"
```

C'est exactement ce que fait un serveur web : il assemble du HTML qu'il
renvoie au navigateur. Les frameworks (vus plus loin) automatisent ça,
mais le principe reste celui-là.

## À toi

Écris `liste_html(items)` qui transforme une liste en liste HTML.
Exemple : `["a", "b"]` → `"<ul><li>a</li><li>b</li></ul>"`.""",
            "starter": "def liste_html(items):\n    ...\n",
            "check": 'assert liste_html(["a", "b"]) == "<ul><li>a</li><li>b</li></ul>"\n'
                     'assert liste_html([]) == "<ul></ul>"\n',
            "solution": 'def liste_html(items):\n'
                        '    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"\n',
        },
        {
            "id": "web-03",
            "title": "Lire les données d'une API",
            "content": """## Récupérer des données en ligne

Beaucoup de services exposent des **API** : des adresses web qui
renvoient des données en **JSON** plutôt qu'une page à afficher. Météo,
taux de change, catalogues...

Pour interroger une API, Python dispose de `urllib.request` (intégré)
ou de la bibliothèque `requests` (très populaire, à installer) :

```
import urllib.request, json

url = "https://api.exemple.fr/meteo"
with urllib.request.urlopen(url) as reponse:
    donnees = json.load(reponse)
print(donnees["temperature"])
```

La réponse est du JSON : on la décode comme on l'a vu, puis on pioche
les valeurs voulues. Ici, pour rester hors-ligne, on te fournit
directement la réponse JSON.

## À toi

La variable `texte` contient la réponse JSON d'une API de villes.
Extrais dans `noms` la **liste des noms** de toutes les villes.""",
            "starter": 'import json\n'
                       'texte = \'{"villes": [{"nom": "Paris", "hab": 2100000}, {"nom": "Lyon", "hab": 520000}]}\'\n'
                       'noms = ...\n',
            "check": 'assert noms == ["Paris", "Lyon"]\n',
            "solution": 'import json\n'
                        'texte = \'{"villes": [{"nom": "Paris", "hab": 2100000}, {"nom": "Lyon", "hab": 520000}]}\'\n'
                        'noms = [v["nom"] for v in json.loads(texte)["villes"]]\n',
        },
        {
            "id": "web-04",
            "title": "Un mini serveur web (sans rien installer)",
            "content": """## Servir une page avec Python seul

Python contient un module `http.server` qui permet de lancer un vrai
serveur web en quelques lignes, **sans aucune installation**. Copie ce
code dans un fichier et lance-le, puis ouvre `http://localhost:8000`
dans ton navigateur :

```
from http.server import HTTPServer, BaseHTTPRequestHandler

class MonServeur(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        page = "<h1>Bonjour depuis Python !</h1>"
        self.wfile.write(page.encode("utf-8"))

serveur = HTTPServer(("localhost", 8000), MonServeur)
print("Serveur sur http://localhost:8000")
serveur.serve_forever()
```

C'est la base de tout site dynamique : recevoir une requête, renvoyer
du HTML. (`Ctrl+C` dans le terminal arrête le serveur.)

## À toi

Écris `page_html(titre, corps)` qui renvoie une page HTML complète au
format exact :
`<!DOCTYPE html><html><head><title>TITRE</title></head><body>CORPS</body></html>`""",
            "starter": "def page_html(titre, corps):\n    ...\n",
            "check": 'r = page_html("Accueil", "<p>Salut</p>")\n'
                     'assert r == "<!DOCTYPE html><html><head><title>Accueil</title></head><body><p>Salut</p></body></html>", r\n',
            "solution": 'def page_html(titre, corps):\n'
                        '    return (f"<!DOCTYPE html><html><head><title>{titre}</title>"\n'
                        '            f"</head><body>{corps}</body></html>")\n',
        },
        {
            "id": "web-05",
            "title": "Pour aller plus loin : Flask & Django",
            "content": """## Les frameworks web

Écrire un site « à la main » devient vite fastidieux. Les
**frameworks** font le gros du travail. Les deux stars en Python :

- **Flask** : léger, parfait pour débuter et pour les petits sites/API.
- **Django** : complet (base de données, authentification, admin...),
  pour les grosses applications.

Un site minimal avec Flask ressemble à ça (après `pip install flask`) :

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def accueil():
    return "<h1>Bienvenue</h1>"

@app.route("/contact")
def contact():
    return "<h1>Contactez-nous</h1>"

app.run()
```

Chaque fonction (`@app.route`) répond à une **adresse** (route). Le
framework s'occupe de recevoir les requêtes et d'appeler la bonne
fonction. C'est exactement la logique d'**aiguillage** que tu vas coder
ci-dessous.

## À toi

Écris `router(chemin)` qui renvoie le contenu selon l'adresse :
`"/"` → `"Accueil"`, `"/contact"` → `"Contact"`, et **toute autre
adresse** → `"404"`.""",
            "starter": "def router(chemin):\n    ...\n",
            "check": 'assert router("/") == "Accueil"\n'
                     'assert router("/contact") == "Contact"\n'
                     'assert router("/inconnu") == "404"\n',
            "solution": 'def router(chemin):\n'
                        '    routes = {"/": "Accueil", "/contact": "Contact"}\n'
                        '    return routes.get(chemin, "404")\n',
        },
    ],
}
