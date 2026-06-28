"""Parcours — Bases de données (SQLite)."""

LEVEL = {
    "id": "sqlite",
    "title": "9 · Bases de données (SQLite)",
    "lessons": [
        {
            "id": "sql-01",
            "title": "Première base de données",
            "content": """## Stocker des données pour de bon

Une **base de données** range des données dans des **tables** (comme des
feuilles de tableur) et permet de les retrouver avec le langage **SQL**.
Python intègre **SQLite** : une base complète, dans un simple fichier,
**sans rien installer**.

```
import sqlite3

conn = sqlite3.connect("ma_base.db")   # ou ":memory:" pour une base en RAM
conn.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)")
conn.commit()                          # valide les changements
conn.close()
```

`execute(...)` envoie une commande SQL. `commit()` enregistre. Une table
se crée avec `CREATE TABLE nom (colonne TYPE, ...)`.

## À toi

Écris `creer_table(conn)` qui crée une table `contacts` avec deux
colonnes : `id` (INTEGER PRIMARY KEY) et `nom` (TEXT).""",
            "starter": "import sqlite3\n\ndef creer_table(conn):\n    ...\n",
            "check": "import sqlite3\nconn = sqlite3.connect(':memory:')\ncreer_table(conn)\n"
                     "cur = conn.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'\")\n"
                     "assert cur.fetchone() is not None, 'la table contacts doit exister'\n",
            "solution": "import sqlite3\n\ndef creer_table(conn):\n"
                        "    conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)')\n"
                        "    conn.commit()\n",
            "hints": ["Utilise conn.execute('CREATE TABLE ...').",
                      "Syntaxe : CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)"],
        },
        {
            "id": "sql-02",
            "title": "Insérer des données (INSERT)",
            "content": """## Ajouter des lignes

On insère avec `INSERT INTO table (colonnes) VALUES (...)`. Pour les
valeurs, on utilise des **paramètres** `?` (jamais de f-string : ça
protège des injections SQL).

```
conn.execute("INSERT INTO contacts (nom) VALUES (?)", ("Ada",))
conn.commit()
```

Le `?` est remplacé par la valeur du tuple. Avec plusieurs colonnes :
`VALUES (?, ?)` et un tuple à deux éléments.

## À toi

Écris `ajouter(conn, nom)` qui insère un contact avec ce `nom` dans la
table `contacts` (déjà créée).""",
            "starter": "def ajouter(conn, nom):\n    ...\n",
            "check": "import sqlite3\nconn = sqlite3.connect(':memory:')\n"
                     "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)')\n"
                     "ajouter(conn, 'Ada')\najouter(conn, 'Alan')\n"
                     "n = conn.execute('SELECT COUNT(*) FROM contacts').fetchone()[0]\n"
                     "assert n == 2, f'2 contacts attendus, {n} trouvés'\n",
            "solution": "def ajouter(conn, nom):\n"
                        "    conn.execute('INSERT INTO contacts (nom) VALUES (?)', (nom,))\n"
                        "    conn.commit()\n",
            "hints": ["INSERT INTO contacts (nom) VALUES (?)",
                      "Passe la valeur dans un tuple : (nom,) — avec la virgule."],
        },
        {
            "id": "sql-03",
            "title": "Lire des données (SELECT)",
            "content": """## Récupérer des lignes

`SELECT colonnes FROM table` lit les données. `execute` renvoie un
curseur que l'on parcourt, ou dont on récupère tout avec `fetchall()`.
Chaque ligne est un tuple.

```
cur = conn.execute("SELECT nom FROM contacts ORDER BY id")
for ligne in cur:
    print(ligne[0])
# ou : noms = [l[0] for l in cur]
```

`ORDER BY` trie le résultat. `SELECT *` récupère toutes les colonnes.

## À toi

Écris `tous_les_noms(conn)` qui renvoie la **liste** des noms de tous
les contacts, triés par `id`.""",
            "starter": "def tous_les_noms(conn):\n    ...\n",
            "check": "import sqlite3\nconn = sqlite3.connect(':memory:')\n"
                     "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)')\n"
                     "conn.executemany('INSERT INTO contacts (nom) VALUES (?)', [('Ada',), ('Alan',), ('Grace',)])\n"
                     "assert tous_les_noms(conn) == ['Ada', 'Alan', 'Grace']\n",
            "solution": "def tous_les_noms(conn):\n"
                        "    cur = conn.execute('SELECT nom FROM contacts ORDER BY id')\n"
                        "    return [ligne[0] for ligne in cur]\n",
            "hints": ["SELECT nom FROM contacts ORDER BY id",
                      "Récupère la 1re colonne de chaque ligne : ligne[0]."],
        },
        {
            "id": "sql-04",
            "title": "Filtrer (WHERE)",
            "content": """## Ne garder que ce qui nous intéresse

`WHERE` filtre les lignes selon une condition. `LIKE` permet les motifs
(`%` = n'importe quelle suite de caractères).

```
cur = conn.execute("SELECT nom FROM contacts WHERE nom LIKE ?", ("A%",))
# tous les noms commençant par A
```

Autres conditions : `WHERE age > 18`, `WHERE ville = ?`, combinables
avec `AND` / `OR`.

## À toi

Écris `commencant_par(conn, lettre)` qui renvoie la liste des noms qui
**commencent** par la lettre donnée (utilise `LIKE`).""",
            "starter": "def commencant_par(conn, lettre):\n    ...\n",
            "check": "import sqlite3\nconn = sqlite3.connect(':memory:')\n"
                     "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)')\n"
                     "conn.executemany('INSERT INTO contacts (nom) VALUES (?)', [('Ada',), ('Alan',), ('Grace',)])\n"
                     "assert commencant_par(conn, 'A') == ['Ada', 'Alan']\n"
                     "assert commencant_par(conn, 'G') == ['Grace']\n",
            "solution": "def commencant_par(conn, lettre):\n"
                        "    cur = conn.execute('SELECT nom FROM contacts WHERE nom LIKE ? ORDER BY id', (lettre + '%',))\n"
                        "    return [l[0] for l in cur]\n",
            "hints": ["WHERE nom LIKE ?",
                      "Le motif est lettre + '%' (ex. 'A%')."],
        },
        {
            "id": "sql-05",
            "title": "Modifier et supprimer",
            "content": """## Mettre à jour, effacer

`UPDATE` modifie des lignes existantes, `DELETE` les supprime. Pense
toujours au `WHERE`, sinon **toute la table** est touchée !

```
conn.execute("UPDATE contacts SET nom = ? WHERE nom = ?", ("Ada L.", "Ada"))
conn.execute("DELETE FROM contacts WHERE nom = ?", ("Alan",))
conn.commit()
```

## À toi

Écris `supprimer(conn, nom)` qui supprime de la table `contacts` toutes
les lignes ayant ce `nom`.""",
            "starter": "def supprimer(conn, nom):\n    ...\n",
            "check": "import sqlite3\nconn = sqlite3.connect(':memory:')\n"
                     "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, nom TEXT)')\n"
                     "conn.executemany('INSERT INTO contacts (nom) VALUES (?)', [('Ada',), ('Alan',)])\n"
                     "supprimer(conn, 'Alan')\n"
                     "restants = [l[0] for l in conn.execute('SELECT nom FROM contacts')]\n"
                     "assert restants == ['Ada'], restants\n",
            "solution": "def supprimer(conn, nom):\n"
                        "    conn.execute('DELETE FROM contacts WHERE nom = ?', (nom,))\n"
                        "    conn.commit()\n",
            "hints": ["DELETE FROM contacts WHERE nom = ?",
                      "N'oublie pas conn.commit() pour valider."],
        },
        {
            "id": "sql-06",
            "title": "Compter et regrouper (GROUP BY)",
            "content": """## Synthétiser les données

Les fonctions d'agrégation résument : `COUNT(*)` compte, `SUM(col)`
additionne, `AVG`, `MAX`, `MIN`. `GROUP BY` calcule **par groupe**.

```
cur = conn.execute(
    "SELECT client, SUM(montant) FROM commandes GROUP BY client")
for client, total in cur:
    print(client, total)
```

C'est ce qui transforme une base de données en outil d'analyse.

## À toi

Une table `commandes(client TEXT, montant INTEGER)` est fournie. Écris
`total_par_client(conn)` qui renvoie un **dictionnaire** `{client: total}`.""",
            "starter": "def total_par_client(conn):\n    ...\n",
            "check": "import sqlite3\nconn = sqlite3.connect(':memory:')\n"
                     "conn.execute('CREATE TABLE commandes (client TEXT, montant INTEGER)')\n"
                     "conn.executemany('INSERT INTO commandes VALUES (?, ?)', "
                     "[('Ada', 10), ('Ada', 5), ('Alan', 20)])\n"
                     "assert total_par_client(conn) == {'Ada': 15, 'Alan': 20}\n",
            "solution": "def total_par_client(conn):\n"
                        "    cur = conn.execute('SELECT client, SUM(montant) FROM commandes GROUP BY client')\n"
                        "    return {client: total for client, total in cur}\n",
            "hints": ["SELECT client, SUM(montant) ... GROUP BY client",
                      "Construis le dict : {client: total for client, total in cur}."],
        },
    ],
}
