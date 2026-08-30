"""Parcours 21 — Réseaux & Protocoles."""

LEVEL = {
    "id": "reseaux",
    "title": "21 · Réseaux & Protocoles",
    "lessons": [
        {
            "id": "net-01",
            "title": "Adresses IP et Ports",
            "content": """## Comment s'identifie une machine sur le réseau ?

Une communication réseau nécessite deux informations clés :
1. **L'adresse IP** (ex: `192.168.1.1` ou `127.0.0.1`) : identifie la machine sur le réseau.
2. **Le port** (ex: `80` pour HTTP, `443` pour HTTPS, `22` pour SSH) : identifie l'application spécifique qui écoute sur cette machine.

Pour valider une adresse IP en Python, on utilise le module standard `ipaddress` :

```python
import ipaddress

try:
    ip = ipaddress.ip_address("192.168.1.42")
    est_privee = ip.is_private   # True
except ValueError:
    print("Adresse IP invalide !")
```

## À toi

Écris `analyser_adresse(hote_port: str, port_defaut=80) -> tuple[str, int]` qui
découpe une chaîne comme `"192.168.1.1:8080"` ou `"localhost"` et renvoie le
couple `(hote, port_entier)`.""",
            "starter": "def analyser_adresse(hote_port: str, port_defaut=80) -> tuple[str, int]:\n    ...\n",
            "check": "assert analyser_adresse('192.168.1.1:8080') == ('192.168.1.1', 8080)\n"
                     "assert analyser_adresse('localhost') == ('localhost', 80)\n"
                     "assert analyser_adresse('example.org:443', 80) == ('example.org', 443)\n",
            "solution": "def analyser_adresse(hote_port: str, port_defaut=80) -> tuple[str, int]:\n"
                        "    if ':' in hote_port:\n"
                        "        hote, port = hote_port.rsplit(':', 1)\n"
                        "        return hote, int(port)\n"
                        "    return hote_port, port_defaut\n",
            "hints": [
                "Vérifie si ':' est présent dans hote_port.",
                "Utilise hote_port.rsplit(':', 1) et int(port)."
            ],
        },
        {
            "id": "net-02",
            "title": "Trames JSON délimitées (Framing)",
            "content": """## Pourquoi délimiter les messages réseau ?

Les sockets TCP transmettent un **flux continu d'octets** (stream). Si l'émetteur
envoie deux messages rapidement, le récepteur peut les recevoir collés en un
seul paquet !

Une technique classique consiste à terminer chaque message par un saut de
ligne `\\n` et à encoder les données au format JSON.

```python
import json

message = {"action": "salut", "user": "Alice"}
trame = json.dumps(message).encode("utf-8") + b"\\n"
```

## À toi

Écris deux fonctions :
1. `encoder_trame(donnees: dict) -> bytes` : sérialise en JSON utf-8 avec `\\n` final.
2. `decoder_trame(paquet_octets: bytes) -> dict` : décode la chaîne UTF-8 sans le `\\n` et renvoie le dictionnaire JSON.""",
            "starter": "import json\n\ndef encoder_trame(donnees: dict) -> bytes:\n    ...\n\ndef decoder_trame(paquet_octets: bytes) -> dict:\n    ...\n",
            "check": "d = {'cmd': 'PING', 'seq': 42}\n"
                     "t = encoder_trame(d)\n"
                     "assert isinstance(t, bytes) and t.endswith(b'\\n')\n"
                     "assert decoder_trame(t) == d\n",
            "solution": "import json\n\ndef encoder_trame(donnees: dict) -> bytes:\n"
                        "    return json.dumps(donnees).encode('utf-8') + b'\\n'\n\n"
                        "def decoder_trame(paquet_octets: bytes) -> dict:\n"
                        "    return json.loads(paquet_octets.decode('utf-8').strip())\n",
            "hints": [
                "json.dumps(donnees).encode('utf-8') + b'\\n'",
                "json.loads(paquet_octets.decode('utf-8').strip())"
            ],
        },
        {
            "id": "net-03",
            "title": "Décoder une requête HTTP brute",
            "content": """## L'anatomie d'une requête HTTP/1.1

Quand un navigateur visite une page, il envoie un texte brut formaté ainsi :
```http
GET /index.html HTTP/1.1
Host: example.org
User-Agent: Mozilla/5.0

```

La première ligne contient : `METHODE CHEMIN VERSION`.
Les lignes suivantes contiennent les en-têtes `Cle: Valeur`, séparées du
corps par une ligne vide `\\r\\n\\r\\n`.

## À toi

Écris `parser_ligne_requete(ligne_brute: str) -> dict` qui prend la première
ligne d'une requête HTTP (ex: `"GET /api/users HTTP/1.1"`) et renvoie un
dictionnaire `{"methode": "GET", "chemin": "/api/users", "version": "HTTP/1.1"}`.""",
            "starter": "def parser_ligne_requete(ligne_brute: str) -> dict:\n    ...\n",
            "check": "r = parser_ligne_requete('GET /index.html HTTP/1.1\\r\\n')\n"
                     "assert r == {'methode': 'GET', 'chemin': '/index.html', 'version': 'HTTP/1.1'}\n"
                     "r2 = parser_ligne_requete('POST /login HTTP/1.0')\n"
                     "assert r2 == {'methode': 'POST', 'chemin': '/login', 'version': 'HTTP/1.0'}\n",
            "solution": "def parser_ligne_requete(ligne_brute: str) -> dict:\n"
                        "    morceaux = ligne_brute.strip().split()\n"
                        "    return {'methode': morceaux[0], 'chemin': morceaux[1], 'version': morceaux[2]}\n",
            "hints": [
                "Nettoie la ligne avec .strip() puis découpe avec .split().",
                "Associe les 3 éléments à 'methode', 'chemin' et 'version'."
            ],
        },
        {
            "id": "net-04",
            "title": "Tester la connectivité d'un port (Socket)",
            "content": """## Le module standard socket

Pour savoir si un service réseau est disponible sur une machine distante, on
tente d'établir une connexion TCP avec un délai d'attente (*timeout*) court.

La fonction `socket.create_connection((hote, port), timeout)` tente la
connexion et lève une exception (`OSError` ou `socket.timeout`) si le port
est fermé ou inaccessible.

```python
import socket

try:
    with socket.create_connection(("example.com", 80), timeout=2.0) as s:
        print("Port ouvert !")
except (socket.timeout, OSError):
    print("Port fermé ou inaccessible.")
```

## À toi

Écris `formater_statut_port(hote: str, port: int, est_ouvert: bool) -> str` qui
renvoie `f"{hote}:{port} -> OUVERT"` si `est_ouvert` est vrai, sinon
`f"{hote}:{port} -> FERME"`.""",
            "starter": "def formater_statut_port(hote: str, port: int, est_ouvert: bool) -> str:\n    ...\n",
            "check": "assert formater_statut_port('127.0.0.1', 80, True) == '127.0.0.1:80 -> OUVERT'\n"
                     "assert formater_statut_port('localhost', 443, False) == 'localhost:443 -> FERME'\n",
            "solution": "def formater_statut_port(hote: str, port: int, est_ouvert: bool) -> str:\n"
                        "    statut = 'OUVERT' if est_ouvert else 'FERME'\n"
                        "    return f'{hote}:{port} -> {statut}'\n",
            "hints": [
                "Utilise une condition ternaire 'OUVERT' if est_ouvert else 'FERME'.",
                "Formate la chaîne avec f'{hote}:{port} -> {statut}'."
            ],
        },
        {
            "id": "net-05",
            "title": "Validation et masques de sous-réseau",
            "content": """## Les réseaux locaux privés (RFC 1918)

Certaines plages d'adresses IP sont réservées aux réseaux locaux (domicile,
entreprise) et ne sont pas routables sur l'Internet public :
- `10.0.0.0/8` (10.0.0.0 à 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 à 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 à 192.168.255.255)
- `127.0.0.1` (boucle locale / localhost)

Le module `ipaddress` permet de vérifier cela instantanément avec `.is_private`
et `.is_loopback`.

## À toi

Écris `est_adresse_locale(ip_str: str) -> bool` qui renvoie `True` si l'adresse
IP est une adresse privée locale ou une adresse de boucle locale (loopback),
et `False` sinon (ou si l'adresse est invalide).""",
            "starter": "import ipaddress\n\ndef est_adresse_locale(ip_str: str) -> bool:\n    ...\n",
            "check": "assert est_adresse_locale('192.168.1.50') is True\n"
                     "assert est_adresse_locale('127.0.0.1') is True\n"
                     "assert est_adresse_locale('8.8.8.8') is False\n"
                     "assert est_adresse_locale('invalide.ip') is False\n",
            "solution": "import ipaddress\n\ndef est_adresse_locale(ip_str: str) -> bool:\n"
                        "    try:\n"
                        "        ip = ipaddress.ip_address(ip_str)\n"
                        "        return ip.is_private or ip.is_loopback\n"
                        "    except ValueError:\n"
                        "        return False\n",
            "hints": [
                "Instancie ipaddress.ip_address(ip_str) dans un bloc try/except ValueError.",
                "Vérifie ip.is_private or ip.is_loopback."
            ],
        },
        {
            "id": "net-06",
            "title": "Diffusion de messages de chat (Broadcast)",
            "content": """## Le principe d'un serveur de discussion

Dans un serveur de chat, lorsqu'un utilisateur envoie un message, le serveur
doit le **diffuser** (broadcast) à tous les autres clients connectés, à
l'exclusion de l'expéditeur.

Supposons une liste de clients connectés : `["Alice", "Bob", "Charlie"]`.
Si `"Alice"` envoie `"Bonjour à tous"`, les destinataires sont `["Bob", "Charlie"]`.

## À toi

Écris `diffuser_message(clients: list, expediteur, message: str) -> list[tuple[str, str]]`
qui renvoie la liste des messages à expédier sous la forme `[(destinataire, f"[{expediteur}] {message}"), ...]`
pour tous les clients différents de `expediteur`.""",
            "starter": "def diffuser_message(clients: list, expediteur, message: str) -> list[tuple[str, str]]:\n    ...\n",
            "check": "clients = ['Alice', 'Bob', 'Charlie']\n"
                     "res = diffuser_message(clients, 'Alice', 'Salut !')\n"
                     "assert res == [('Bob', '[Alice] Salut !'), ('Charlie', '[Alice] Salut !')]\n"
                     "assert diffuser_message(['Alice'], 'Alice', 'Seul') == []\n",
            "solution": "def diffuser_message(clients: list, expediteur, message: str) -> list[tuple[str, str]]:\n"
                        "    texte = f'[{expediteur}] {message}'\n"
                        "    return [(c, texte) for c in clients if c != expediteur]\n",
            "hints": [
                "Formate le message f'[{expediteur}] {message}'.",
                "Filtre la liste avec c for c in clients if c != expediteur."
            ],
        },
        {
            "id": "qz-net",
            "type": "quiz",
            "title": "Quiz — Réseaux & Protocoles",
            "question": "Pourquoi ajoute-t-on un délimiteur (comme '\\n') lors de l'envoi de messages sur un socket TCP ?",
            "options": [
                "Parce que le protocole TCP impose que chaque paquet contienne du texte.",
                "Parce que TCP est un flux continu (stream) : le délimiteur permet au récepteur de découper les messages.",
                "Pour chiffrer automatiquement les données transmises.",
                "Pour forcer le routeur à réexpédier les paquets perdus."
            ],
            "answer": 1,
            "explanation": "TCP ne préserve pas les limites des messages (pas de notion de paquet au niveau applicatif). Sans délimiteur ou en-tête de taille, deux messages consécutifs peuvent être reçus collés."
        }
    ]
}
