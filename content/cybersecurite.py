"""Parcours 17 — Cybersécurité & Cryptographie."""

LEVEL = {
    "id": "cybersecurite",
    "title": "17 · Cybersécurité & Cryptographie",
    "lessons": [
        {
            "id": "sec-01",
            "title": "Hachage et comparaison sécurisée",
            "content": """## Le hachage avec hashlib

Une fonction de hachage cryptographique transforme n'importe quelle donnée
en une empreinte numérique de taille fixe (ex: SHA-256 produit 64 caractères
hexadécimaux). Elle est à sens unique : impossible de retrouver le mot de
passe original à partir de son hash.

```python
import hashlib
import hmac

h = hashlib.sha256(b"mon_mot_de_passe").hexdigest()
```

## Attaque temporelle (Timing Attack)

Comparer deux chaînes avec `==` s'arrête au premier caractère différent : un
attaquant peut mesurer le temps de réponse pour deviner un mot de passe
caractère par caractère ! Pour éviter cela, on utilise `hmac.compare_digest()`
qui compare toujours en **temps constant**.

## À toi

Écris `verifier_signature(cle_attendue, cle_recue)` qui compare deux
chaînes de caractères en utilisant `hmac.compare_digest` et renvoie un booléen.""",
            "starter": "import hmac\n\ndef verifier_signature(cle_attendue, cle_recue):\n    ...\n",
            "check": "assert verifier_signature('secret123', 'secret123') is True\n"
                     "assert verifier_signature('secret123', 'secret999') is False\n"
                     "assert verifier_signature('a', 'b') is False\n",
            "solution": "import hmac\n\ndef verifier_signature(cle_attendue, cle_recue):\n    return hmac.compare_digest(str(cle_attendue), str(cle_recue))\n",
            "hints": [
                "Utilise hmac.compare_digest(cle_attendue, cle_recue).",
                "Assure-toi que les deux arguments sont du même type (str ou bytes)."
            ],
        },
        {
            "id": "sec-02",
            "title": "Générer de vrais secrets aléatoires",
            "content": """## Le piège du module random

Le module `random` classique utilise un générateur pseudo-aléatoire (Mersenne
Twister) conçu pour les simulations, pas pour la sécurité. En observant
quelques tirages, un pirate peut prédire les nombres suivants !

Pour les jetons de session, clés d'API et réinitialisations de mot de passe,
la bibliothèque standard fournit le module `secrets` :

```python
import secrets

jeton = secrets.token_hex(16)   # 32 caractères hexadécimaux (16 octets)
url_safe = secrets.token_urlsafe(16)  # sûr pour une URL
nombre_sur = secrets.randbelow(100)   # entier de 0 à 99
```

## À toi

Écris `generer_jetons(n, nb_octets=16)` qui renvoie une liste de `n` jetons
hexadécimaux uniques générés avec `secrets.token_hex(nb_octets)`.""",
            "starter": "import secrets\n\ndef generer_jetons(n, nb_octets=16):\n    ...\n",
            "check": "jets = generer_jetons(5, 8)\n"
                     "assert len(jets) == 5\n"
                     "assert len(set(jets)) == 5\n"
                     "assert all(len(j) == 16 for j in jets)\n",
            "solution": "import secrets\n\ndef generer_jetons(n, nb_octets=16):\n    return [secrets.token_hex(nb_octets) for _ in range(n)]\n",
            "hints": [
                "Utilise une boucle ou une compréhension de liste.",
                "[secrets.token_hex(nb_octets) for _ in range(n)]"
            ],
        },
        {
            "id": "sec-03",
            "title": "Chiffrement symétrique par XOR",
            "content": """## L'opérateur XOR (OU exclusif)

Au cœur des chiffrements symétriques se trouve l'opération binaire XOR (`^`).
Sa propriété magique : `(A ^ B) ^ B == A`. Chiffrer un octet avec une clé puis
réappliquer la même clé redonne le message d'origine !

En Python, on manipule des séquences d'octets avec `bytes` ou `bytearray` :

```python
texte = b"Hello"
masque = 42
chiffre = bytes([octet ^ masque for octet in texte])
clair = bytes([octet ^ masque for octet in chiffre])  # b"Hello"
```

## À toi

Écris `chiffrer_xor(donnees: bytes, masque: int) -> bytes` qui applique le
masque XOR `masque` à chaque octet de `donnees` et renvoie le résultat en `bytes`.""",
            "starter": "def chiffrer_xor(donnees: bytes, masque: int) -> bytes:\n    ...\n",
            "check": "msg = b'Python'\n"
                     "c = chiffrer_xor(msg, 77)\n"
                     "assert isinstance(c, bytes)\n"
                     "assert c != msg\n"
                     "assert chiffrer_xor(c, 77) == msg\n",
            "solution": "def chiffrer_xor(donnees: bytes, masque: int) -> bytes:\n    return bytes(b ^ masque for b in donnees)\n",
            "hints": [
                "Transforme chaque octet b avec b ^ masque.",
                "Passe le générateur ou la liste à bytes(...)."
            ],
        },
        {
            "id": "sec-04",
            "title": "Prévenir les injections SQL",
            "content": """## Ne jamais concaténer dans une requête SQL !

Une injection SQL survient lorsqu'une entrée utilisateur non nettoyée est
injectée directement dans une chaîne SQL :

```python
# DANGEREUX : un login comme 'admin -- permet de contourner le mot de passe !
curseur.execute(f"SELECT * FROM users WHERE nom = '{login}'")
```

La bonne pratique consiste à utiliser des **requêtes paramétrées** avec `?`.
La base de données traite les paramètres comme des valeurs pures et jamais
comme du code exécutable.

```python
curseur.execute("SELECT * FROM users WHERE nom = ?", (login,))
```

## À toi

Écris `preparer_insertion_utilisateur(nom, email, role)` qui renvoie un
tuple contenant `(requete_sql, parametres)` où :
- `requete_sql` vaut `"INSERT INTO users (nom, email, role) VALUES (?, ?, ?)"`
- `parametres` est le tuple `(nom, email, role)`.""",
            "starter": "def preparer_insertion_utilisateur(nom, email, role):\n    ...\n",
            "check": "sql, params = preparer_insertion_utilisateur('Alice', 'alice@test.org', 'admin')\n"
                     "assert '?' in sql and 'Alice' not in sql\n"
                     "assert params == ('Alice', 'alice@test.org', 'admin')\n",
            "solution": "def preparer_insertion_utilisateur(nom, email, role):\n"
                        "    sql = 'INSERT INTO users (nom, email, role) VALUES (?, ?, ?)'\n"
                        "    params = (nom, email, role)\n"
                        "    return sql, params\n",
            "hints": [
                "Utilise des points d'interrogation ? comme paramètres de substitution.",
                "Renvoie (sql, (nom, email, role))."
            ],
        },
        {
            "id": "sec-05",
            "title": "Bloquer les traversées de répertoires (Path Traversal)",
            "content": """## Qu'est-ce que le Path Traversal ?

Si votre application permet de télécharger un fichier d'après un nom saisi
par l'utilisateur, un pirate peut fournir `../../../../etc/passwd` ou
`..\\..\\Windows\\win.ini` pour accéder à des fichiers système sensibles.

Avec `pathlib`, on résout le chemin absolu avec `.resolve()` puis on vérifie
qu'il reste bien enfant du dossier autorisé avec `.is_relative_to()` :

```python
from pathlib import Path

base = Path("/var/www/uploads").resolve()
cible = (base / nom_fichier).resolve()

if not cible.is_relative_to(base):
    raise PermissionError("Accès interdit !")
```

## À toi

Écris `est_chemin_sur(dossier_racine, chemin_demande)` qui renvoie `True`
si le chemin cible résolu se situe bien à l'intérieur de `dossier_racine`,
et `False` sinon (ou en cas de tentative d'évasion).""",
            "starter": "from pathlib import Path\n\ndef est_chemin_sur(dossier_racine, chemin_demande):\n    ...\n",
            "check": "import tempfile\nwith tempfile.TemporaryDirectory() as tmp:\n"
                     "    root = Path(tmp)\n"
                     "    assert est_chemin_sur(root, 'images/photo.png') is True\n"
                     "    assert est_chemin_sur(root, '../secret.txt') is False\n"
                     "    assert est_chemin_sur(root, '../../etc/passwd') is False\n",
            "solution": "from pathlib import Path\n\ndef est_chemin_sur(dossier_racine, chemin_demande):\n"
                        "    base = Path(dossier_racine).resolve()\n"
                        "    cible = (base / chemin_demande).resolve()\n"
                        "    try:\n"
                        "        cible.relative_to(base)\n"
                        "        return True\n"
                        "    except ValueError:\n"
                        "        return False\n",
            "hints": [
                "Utilise Path(dossier_racine).resolve() et (base / chemin_demande).resolve().",
                "Utilise cible.relative_to(base) dans un bloc try/except ValueError."
            ],
        },
        {
            "id": "sec-06",
            "title": "Détection d'attaque par force brute",
            "content": """## Analyse de journaux de connexion

Une attaque par force brute consiste à tester des milliers de mots de passe
successifs. Pour la détecter, on analyse les logs d'authentification et on
repère les adresses IP cumulant trop d'échecs.

Supposons une liste de logs au format :
`[{"ip": "192.168.1.10", "succes": False}, {"ip": "192.168.1.10", "succes": True}]`

## À toi

Écris `detecter_bruteforce(logs, seuil_echecs=3)` qui renvoie un ensemble (`set`)
contenant les adresses IP ayant cumulé au moins `seuil_echecs` échecs
(`"succes": False`).""",
            "starter": "from collections import Counter\n\ndef detecter_bruteforce(logs, seuil_echecs=3):\n    ...\n",
            "check": "logs = [\n"
                     "    {'ip': '1.1.1.1', 'succes': False},\n"
                     "    {'ip': '2.2.2.2', 'succes': True},\n"
                     "    {'ip': '1.1.1.1', 'succes': False},\n"
                     "    {'ip': '1.1.1.1', 'succes': False},\n"
                     "    {'ip': '3.3.3.3', 'succes': False},\n"
                     "]\n"
                     "assert detecter_bruteforce(logs, 3) == {'1.1.1.1'}\n"
                     "assert detecter_bruteforce(logs, 1) == {'1.1.1.1', '3.3.3.3'}\n",
            "solution": "from collections import Counter\n\ndef detecter_bruteforce(logs, seuil_echecs=3):\n"
                        "    echecs = Counter(l['ip'] for l in logs if not l.get('succes'))\n"
                        "    return {ip for ip, count in echecs.items() if count >= seuil_echecs}\n",
            "hints": [
                "Compte les occurrences de chaque IP lorsque succes vaut False.",
                "Filtre les adresses IP dont le compteur atteint ou dépasse seuil_echecs."
            ],
        },
        {
            "id": "qz-sec",
            "type": "quiz",
            "title": "Quiz — Cybersécurité",
            "question": "Pourquoi doit-on utiliser `secrets` au lieu de `random` pour générer un jeton de sécurité ?",
            "options": [
                "secrets est plus rapide en temps de calcul.",
                "random est prédictible et non adapté aux besoins cryptographiques.",
                "random ne sait générer que des entiers et pas de texte.",
                "secrets chiffre automatiquement les variables en mémoire vive."
            ],
            "answer": 1,
            "explanation": "Le générateur de random (Mersenne Twister) est pseudo-aléatoire et déterministe. Le module secrets fait appel aux sources d'entropie sécurisées du système d'exploitation."
        }
    ]
}
