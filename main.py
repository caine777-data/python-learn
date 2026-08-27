"""
PythonLearn — application de bureau pour apprendre Python,
du niveau débutant au niveau expert.

Sans argument, lance l'interface graphique. Deux options servent aux
scripts d'empaquetage et à l'intégration continue :

    python main.py --version    affiche la version et sort
    python main.py --check      contrôle que l'installation est complète
"""

import argparse
import sys

from app.version import APP_NAME, __version__


def _dire(message):
    """Affiche un message sans échouer si l'exécutable n'a pas de console.

    Un binaire construit avec « --windowed » n'a pas de sortie standard
    sous Windows : print() y lève une exception. On l'ignore, le code de
    retour du processus suffit à la CI.
    """
    try:
        print(message)
        sys.stdout.flush()
    except Exception:
        pass


def controle_sante():
    """Vérifie qu'une installation (ou un exécutable) est utilisable.

    C'est le test de fumée lancé par la CI juste après l'empaquetage. Il
    attrape le grand classique du binaire PyInstaller livré sans tkinter,
    sans avoir besoin d'un écran : il suffit que les bibliothèques Tcl/Tk
    se chargent. Renvoie 0 si tout va bien, 1 sinon.
    """
    soucis = []

    try:
        import tkinter
        _dire(f"tkinter        : OK (Tcl/Tk {tkinter.TkVersion})")
        try:
            racine = tkinter.Tk()
            racine.destroy()
            _dire("fenêtre Tk     : OK")
        except tkinter.TclError as exc:
            # Aucun écran disponible (CI sans serveur graphique) : Tk s'est
            # bien chargé, c'est tout ce que l'on cherche à prouver ici.
            _dire(f"fenêtre Tk     : pas d'écran ({exc}) — sans gravité")
    except Exception as exc:
        soucis.append(f"tkinter indisponible : {exc}")

    try:
        from content import CURRICULUM, total_count
        parcours, items = len(CURRICULUM), total_count()
        lecons = sum(len(niveau["lessons"]) for niveau in CURRICULUM)
        _dire(f"curriculum     : {parcours} parcours, {lecons} leçons, {items} exercices")
        if parcours == 0 or items == 0:
            soucis.append("curriculum vide")
    except Exception as exc:
        soucis.append(f"curriculum illisible : {exc}")

    try:
        from app.runner import run_code
        resultat, _ = run_code("print('bonjour')")
        _dire("moteur d'exécution : " + ("OK" if resultat.ok else "KO"))
        if not resultat.ok or resultat.output.strip() != "bonjour":
            soucis.append("le moteur d'exécution ne renvoie pas la sortie attendue")
    except Exception as exc:
        soucis.append(f"moteur d'exécution cassé : {exc}")

    if soucis:
        for souci in soucis:
            _dire("ÉCHEC : " + souci)
        return 1
    _dire(f"{APP_NAME} {__version__} — installation complète.")
    return 0


def verifier_packs():
    """Contrôle les packs de leçons installés et affiche un rapport lisible.

    Destiné à qui écrit ses propres exercices : on obtient la liste des
    erreurs sans avoir à lancer l'interface ni à chercher où ça coince.
    """
    from content import ids_utilises
    from content.packs import DOSSIER_PACKS, charger_packs

    _dire(f"Dossier des packs : {DOSSIER_PACKS}")
    if not DOSSIER_PACKS.is_dir():
        _dire("Ce dossier n'existe pas encore : aucun pack installé.")
        _dire("Pour créer un exemple :  python main.py --exemple-pack")
        return 0

    fichiers = sorted(DOSSIER_PACKS.glob("*.json"))
    parcours, problemes = charger_packs(ids_existants=ids_utilises())
    _dire(f"{len(fichiers)} fichier(s) trouvé(s), "
          f"{len(parcours)} parcours utilisable(s).")

    for niveau in parcours:
        auteur = niveau.get("auteur")
        signature = f" — {auteur}" if auteur else ""
        _dire(f"  OK   {niveau['id']:<20} "
              f"{len(niveau['lessons'])} leçon(s){signature}")

    if problemes:
        _dire("")
        _dire("Points à corriger :")
        for souci in problemes:
            _dire("  - " + souci)
        return 1
    if fichiers:
        _dire("Aucun problème détecté.")
    return 0


def creer_exemple_pack():
    """Écrit un pack de leçons d'exemple, prêt à être modifié."""
    from content.packs import DOSSIER_PACKS, modele_pack

    chemin = DOSSIER_PACKS / "mon-cours.json"
    if chemin.exists():
        # On n'écrase jamais le travail de quelqu'un.
        _dire(f"Ce fichier existe déjà, rien n'a été écrit :\n  {chemin}")
        return 1
    try:
        DOSSIER_PACKS.mkdir(parents=True, exist_ok=True)
        chemin.write_text(modele_pack(), encoding="utf-8")
    except OSError as exc:
        _dire(f"Écriture impossible : {exc}")
        return 1
    _dire(f"Pack d'exemple créé :\n  {chemin}")
    _dire("Ouvre-le dans un éditeur de texte, modifie-le, puis relance "
          "PythonLearn : ton parcours apparaîtra dans la liste.")
    return 0


def main(argv=None):
    analyseur = argparse.ArgumentParser(
        prog="PythonLearn",
        description="Apprendre Python pas à pas, du débutant à l'expert.")
    analyseur.add_argument("--version", action="version",
                           version=f"{APP_NAME} {__version__}")
    analyseur.add_argument("--check", action="store_true",
                           help="contrôle que l'installation est complète, puis sort")
    analyseur.add_argument("--verifier-packs", action="store_true",
                           help="contrôle les packs de leçons installés, puis sort")
    analyseur.add_argument("--exemple-pack", action="store_true",
                           help="crée un pack de leçons d'exemple, puis sort")
    arguments = analyseur.parse_args(argv)

    if arguments.check:
        return controle_sante()
    if arguments.verifier_packs:
        return verifier_packs()
    if arguments.exemple_pack:
        return creer_exemple_pack()

    from app.ui import launch
    launch()
    return 0


if __name__ == "__main__":
    sys.exit(main())
