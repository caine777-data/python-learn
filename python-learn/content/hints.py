"""
Indices progressifs, séparés du contenu des leçons.

HINTS[lesson_id] = [indice1, indice2, ...]  (dévoilés un par un)

L'interface fusionne ces indices avec un éventuel champ "hints" présent
directement dans une leçon ou un exercice.
"""

HINTS = {
    # --- Débutant ---
    "deb-00": ["La phrase exacte à afficher est : Je commence Python !",
               "Mets la phrase entre guillemets dans print(...).",
               'Réponse : print("Je commence Python !")'],
    "deb-01": ["Il te faut deux print, un par ligne.",
               'print("Salut") puis print("Le monde").'],
    "deb-02": ["Le texte va entre guillemets, le nombre sans guillemets.",
               'ville = "Toulouse" et habitants = 500000.'],
    "deb-03": ["Augmenter de 20 %, c'est multiplier par 1.2.",
               "prix_ttc = prix_ht * 1.2"],
    "deb-04": ["La méthode pour mettre en majuscules s'écrit .upper().",
               "nom_majuscule = nom.upper()"],
    "deb-05": ["Une f-string commence par f avant le guillemet.",
               'phrase = f"Il reste {jours} jours."'],
    "deb-06": ["input() renvoie du texte : entoure-le de int(...).",
               "total = a + b après avoir converti a et b en int."],
    "deb-07": ["Compare temperature avec 0 en utilisant <=.",
               "if temperature <= 0: ... else: ..."],
    "deb-08": ["« au moins 16 ans » se traduit par age >= 16.",
               "Relie les deux conditions avec or.",
               "return age >= 16 or accompagne"],
    "deb-09": ["range(1, 51) parcourt 1 à 50 inclus.",
               "Dans la boucle : somme += i"],
    "deb-10": ["Multiplie n par 2 à chaque tour : n = n * 2.",
               "La boucle s'arrête dès que n atteint ou dépasse 1000."],
    "deb-11": ["sum(notes) fait la somme, len(notes) compte les éléments.",
               "moyenne = sum(notes) / len(notes)"],
    "deb-12": ["Le double, c'est multiplier par 2.",
               "return nombre * 2"],
    "deb-13": ["math.sqrt(...) calcule la racine carrée.",
               "a**2 + b**2 puis racine carrée du tout."],
    "deb-14": ["sum() pour le total, divise par len() pour la moyenne.",
               "return total, moyenne (une virgule renvoie un couple)."],
    # --- Parcours pratiques (clés) ---
    "scr-02": ["Path(nom).suffix donne l'extension AVEC le point.",
               ".lstrip('.') enlève le point, .lower() met en minuscules."],
    "scr-03": ["En écriture : ouvre en mode 'w' et fais un f.write par ligne.",
               "En lecture : parcours le fichier et enlève '\\n' avec rstrip."],
    "scr-04": ["json.loads(texte) transforme le JSON en dictionnaire.",
               'Ensuite : ...["ville"]'],
    "gui-05": ["Applique la formule c * 9 / 5 + 32.",
               "return c * 9 / 5 + 32"],
    "web-02": ["Entoure chaque élément de <li>...</li>.",
               'Puis encadre le tout par <ul> et </ul>.'],
    "adm-03": ["Path(dossier).glob('*.txt') liste les .txt.",
               "len(list(...)) compte les résultats."],
    "adm-05": ["fichier.suffix.lstrip('.').lower() donne l'extension propre.",
               "cible.mkdir(exist_ok=True) crée le sous-dossier sans erreur."],
}
