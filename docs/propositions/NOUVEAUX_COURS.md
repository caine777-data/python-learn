# 📚 Spécifications des 7 Nouveaux Parcours Proposés

Ce document détaille le contenu pédagogique, les leçons, les exercices pratiques et les vérifications (`check`) pour les 7 nouveaux parcours prêts à être intégrés dans `content/`.

---

## 1. Parcours 17 · Cybersécurité & Cryptographie (`content/cybersecurite.py`)

*Identifiant de niveau : `cybersecurite` — Titre : `17 · Cybersécurité & Cryptographie`*

### Leçons :
1. **`sec-01` — Hachage et comparaison à temps constant**
   - **Thème** : Calculer un hash SHA-256 et comparer deux signatures avec `hmac.compare_digest` pour éviter les attaques temporelles (*timing attacks*).
   - **Fonction à écrire** : `verifier_signature(cle_attendue, cle_recue) -> bool`.
   - **Check** : `assert verifier_signature("abc", "abc") is True` et `assert verifier_signature("abc", "abd") is False`.

2. **`sec-02` — Génération de tokens aléatoires sécurisés**
   - **Thème** : Comprendre pourquoi `random` est prédictible et utiliser `secrets.token_hex(n)` pour créer des jetons d'authentification réinitialisation de mot de passe.
   - **Fonction à écrire** : `generer_jeton(longueur_octets) -> str`.
   - **Check** : `t = generer_jeton(16); assert len(t) == 32 and isinstance(t, str)`.

3. **`sec-03` — Chiffrement XOR de flux d'octets**
   - **Thème** : Comprendre le chiffrement symétrique au niveau binaire en appliquant l'opérateur `^` (XOR) entre des octets (`bytes`) et une clé.
   - **Fonction à écrire** : `chiffrer_xor(donnees: bytes, masque: int) -> bytes`.
   - **Check** : `assert chiffrer_xor(b"ABC", 42) == bytes([ord(c) ^ 42 for c in "ABC"])`.

4. **`sec-04` — Prévention des injections SQL**
   - **Thème** : Utiliser des requêtes préparées avec `?` au lieu de la concaténation de chaînes.
   - **Fonction à écrire** : `rechercher_utilisateur(curseur, login, mdp_hash) -> list`.
   - **Check** : `curseur.execute("SELECT * FROM users WHERE login = ? AND mdp = ?", (login, mdp_hash))`.

5. **`sec-05` — Bloquer les traversées de répertoires (Path Traversal)**
   - **Thème** : Sécuriser les téléchargements de fichiers en vérifiant que le chemin résolu reste à l'intérieur du dossier racine autorisé via `Path.resolve()`.
   - **Fonction à écrire** : `est_chemin_sur(dossier_base: Path, chemin_demande: str) -> bool`.
   - **Check** : Rejette `../../etc/passwd` et accepte `images/photo.png`.

6. **`sec-06` — Détecteur d'attaque par force brute**
   - **Thème** : Analyser une liste de logs `[{"ip": ..., "succes": False}]` et lister les IP ayant plus de `seuil` échecs consécutifs.
   - **Fonction à écrire** : `ips_suspectes(logs, seuil=3) -> set`.

7. **`qz-sec` — Quiz Cybersécurité**
   - Question : *« Pourquoi ne doit-on pas utiliser le module `random` pour générer des tokens d'authentification ? »*

---

## 2. Parcours 18 · Mathématiques, Sciences & Simulations (`content/maths_sciences.py`)

*Identifiant de niveau : `maths_sciences` — Titre : `18 · Mathématiques, Sciences & Simulations`*

### Leçons :
1. **`mat-01` — Crible d'Ératosthène & nombres premiers**
   - **Fonction à écrire** : `premiers_jusqua(n) -> list[int]`.
   - **Check** : `assert premiers_jusqua(10) == [2, 3, 5, 7]`.

2. **`mat-02` — Précision financière et décimale exacte**
   - **Thème** : Découvrir `decimal.Decimal` pour éviter l'imprécision des flottants IEEE 754 (`0.1 + 0.2 != 0.3`).
   - **Fonction à écrire** : `total_centimes(montants_str: list[str]) -> Decimal`.

3. **`mat-03` — Simulation de Monte-Carlo (Estimation de Pi)**
   - **Thème** : Générer \(N\) points dans un carré \([0, 1] \times [0, 1]\) et compter ceux à l'intérieur du quart de cercle pour estimer \(\pi \approx 4 \times \frac{\text{dans}}{\text{total}}\).
   - **Fonction à écrire** : `estimer_pi(points: list[tuple[float, float]]) -> float`.

4. **`mat-04` — Vecteurs et produit scalaire**
   - **Fonction à écrire** : `produit_scalaire(u, v) -> float` et `norme(u) -> float`.
   - **Check** : `assert produit_scalaire((1, 2), (3, 4)) == 11`.

5. **`mat-05` — Résolution d'équations par dichotomie**
   - **Thème** : Trouver le zéro d'une fonction continue monotone sur \([a, b]\) avec une tolérance donnée.
   - **Fonction à écrire** : `trouver_racine(f, a, b, precision=1e-5) -> float`.

6. **`mat-06` — Suite de Syracuse (Conjecture de Collatz)**
   - **Fonction à écrire** : `vol_syracuse(n) -> list[int]`.
   - **Check** : `assert vol_syracuse(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]`.

7. **`qz-mat` — Quiz Mathématiques & Sciences**

---

## 3. Parcours 19 · Traitement d'Images & Audio (`content/multimedia.py`)

*Identifiant de niveau : `multimedia` — Titre : `19 · Traitement d'Images & Audio`*

### Leçons :
1. **`med-01` — La structure d'un pixel RGB**
   - **Fonction à écrire** : `inverser_pixel(r, g, b) -> tuple[int, int, int]`.
   - **Check** : `assert inverser_pixel(255, 0, 100) == (0, 255, 155)`.

2. **`med-02` — Écrire une image en pur Python (Format PPM)**
   - **Thème** : Le format Netpbm PPM (P3) est du texte brut : entête `P3\nlargeur hauteur\n255\n` suivi des triplets RGB.
   - **Fonction à écrire** : `generer_ppm_uni(largeur, hauteur, couleur_rgb) -> str`.

3. **`med-03` — Filtre de niveau de gris**
   - **Thème** : Formule de luminance standard \(L = 0.299 R + 0.587 G + 0.114 B\).
   - **Fonction à écrire** : `vers_gris(pixels_rgb: list[tuple[int, int, int]]) -> list[int]`.

4. **`med-04` — Générateur de damier graphique**
   - **Fonction à écrire** : `grille_damier(taille, couleur1, couleur2) -> list[list[tuple]]`.

5. **`med-05` — Synthèse audio avec le module `wave`**
   - **Thème** : Échantillonnage sonore (44100 Hz), sinusoïde mathématique et paquetage en octets avec `struct.pack`.
   - **Fonction à écrire** : `echantillons_sinus(frequence, duree_sec, cadence=44100) -> list[int]`.

6. **`med-06` — Générateur de sonnerie / mélodie**
   - **Fonction à écrire** : `generer_melodie(notes: list[tuple[float, float]]) -> list[int]`.

7. **`qz-med` — Quiz Multimédia**

---

## 4. Parcours 20 · Intelligence Artificielle & Machine Learning (`content/ia_ml.py`)

*Identifiant de niveau : `ia_ml` — Titre : `20 · Intelligence Artificielle (de zéro)`*

### Leçons :
1. **`ia-01` — Les k plus proches voisins (k-NN)**
   - **Thème** : Distance euclidienne entre points, tri par proximité et vote majoritaire des étiquettes.
   - **Fonction à écrire** : `knn_classifier(points_connus, nouveau_point, k=3) -> str`.

2. **`ia-02` — Régression linéaire simple**
   - **Thème** : Calcul des coefficients \(a\) (pente) et \(b\) (ordonnée à l'origine) par la méthode des moindres carrés.
   - **Fonction à écrire** : `regression_lineaire(points: list[tuple[float, float]]) -> tuple[float, float]`.

3. **`ia-03` — Arbre de décision logique**
   - **Fonction à écrire** : `classer_pret(revenu, apport, a_dettes) -> str` (`"accorde"` ou `"refuse"`).

4. **`ia-04` — Le Perceptron (neurone artificiel)**
   - **Thème** : Somme pondérée \(z = \sum w_i x_i + b\) et fonction d'activation seuil (Heaviside).
   - **Fonction à écrire** : `activer_perceptron(entrees, poids, biais) -> int`.

5. **`ia-05` — Analyse de sentiments textuelle**
   - **Thème** : Score de polarité d'un texte par décompte des mots positifs et négatifs normalisé.
   - **Fonction à écrire** : `score_sentiment(texte, positifs, negatifs) -> int`.

6. **`ia-06` — Moteur de recommandation par similarité cosinus**
   - **Thème** : \(\cos(\theta) = \frac{u \cdot v}{\|u\| \|v\|}\) entre profils d'utilisateurs.
   - **Fonction à écrire** : `similarite_cosinus(u, v) -> float`.

7. **`qz-ia` — Quiz IA & Machine Learning**

---

## 5. Parcours 21 · Réseaux & Protocoles (`content/reseaux.py`)

*Identifiant de niveau : `reseaux` — Titre : `21 · Réseaux & Protocoles`*

### Leçons :
1. **`net-01` — Anatomie d'une URL et d'une adresse réseau**
   - **Fonction à écrire** : `analyser_hote_port(adresse: str, port_defaut=80) -> tuple[str, int]`.
   - **Check** : `assert analyser_hote_port("example.com:8080") == ("example.com", 8080)`.

2. **`net-02` — Protocole d'échange de trames JSON délimitées**
   - **Thème** : Découpage de flux réseau avec délimiteur `\n`.
   - **Fonction à écrire** : `encoder_trame(commande: str, donnees: dict) -> bytes` et `decoder_trame(paquet: bytes) -> dict`.

3. **`net-03` — Parseur de requêtes HTTP/1.1 manuelles**
   - **Thème** : Parser `GET /chemin HTTP/1.1\r\nHost: ...\r\n\r\n`.
   - **Fonction à écrire** : `parser_requete_http(texte_brut: str) -> dict`.

4. **`net-04` — Détecteur de ports ouverts (Scanner local sécurisé)**
   - **Thème** : Utiliser `socket.create_connection` avec un court timeout pour tester l'accessibilité d'un port.
   - **Fonction à écrire** : `tester_port(hote, port, timeout=0.2) -> bool`.

5. **`net-05` — Résolution DNS et validation d'IP**
   - **Thème** : Module `ipaddress` et `socket.gethostbyname`.
   - **Fonction à écrire** : `est_ip_valide(chaine) -> bool`.

6. **`net-06` — Simulateur de serveur de chat (Broadcast)**
   - **Fonction à écrire** : `diffuser_message(clients: list, expediteur, message: str) -> list`.

7. **`qz-net` — Quiz Réseaux**

---

## 6. Parcours 22 · Architecture & Jeux Vidéo (`content/jeux_video.py`)

*Identifiant de niveau : `jeux_video` — Titre : `22 · Architecture & Jeux Vidéo 2D`*

### Leçons :
1. **`gam-01` — La boucle de jeu (Game Loop & Delta Time)**
   - **Fonction à écrire** : `mettre_a_jour_position(x, v, dt) -> float`.

2. **`gam-02` — Déplacement sur grille 2D & collisions**
   - **Fonction à écrire** : `deplacer_joueur(grille, x, y, direction) -> tuple[int, int]`.

3. **`gam-03` — Système d'inventaire avec capacité maximale**
   - **Fonction à écrire** : `ajouter_inventaire(sac, item, poids, capacite_max=20) -> bool`.

4. **`gam-04` — Calcul de combat au tour par tour**
   - **Fonction à écrire** : `calculer_degats(attaque, defense, est_critique=False) -> int`.

5. **`gam-05` — Pathfinding direct (IA de poursuite)**
   - **Fonction à écrire** : `prochain_pas(ennemi_xy, cible_xy) -> tuple[int, int]`.

6. **`gam-06` — Sérialisation de l'état du jeu (Sauvegarde JSON)**
   - **Fonction à écrire** : `sauvegarder_partie(joueur, inventaire, niveau) -> str`.

7. **`qz-gam` — Quiz Jeux Vidéo**

---

## 7. Parcours 23 · Design Patterns & Typage Moderne (`content/design_patterns.py`)

*Identifiant de niveau : `design_patterns` — Titre : `23 · Design Patterns & Typage Moderne`*

### Leçons :
1. **`pat-01` — Le pattern Singleton & Factory**
   - **Fonction à écrire** : `CreerVehicule.fabriquer(type_vehicule)`.

2. **`pat-02` — Le pattern Observateur (Event Emitter)**
   - **Classe à écrire** : `GestionnaireEvenements` (`abonner`, `notifier`).

3. **`pat-03` — Le pattern Stratégie (Calculs de réduction interchangeables)**
   - **Fonction/Classes à écrire** : `CalculateurPrix(strategie)`.

4. **`pat-04` — Classes abstraites et contrats (`abc.ABC`)**
   - **Thème** : `@abstractmethod` imposant l'implémentation de `rendre()` et `calculer()`.

5. **`pat-05` — Typage structurel avec `typing.Protocol`**
   - **Thème** : Duck typing statique vérifié.

6. **`pat-06` — Les Énumérations robustes (`enum.Enum`, `enum.auto`)**
   - **Classe à écrire** : `StatutCommande(Enum)`.

7. **`qz-pat` — Quiz Design Patterns**
