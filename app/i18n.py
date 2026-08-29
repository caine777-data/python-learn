"""
Traductions de l'interface (FR / EN).

Seuls les textes de l'INTERFACE sont traduits ; le contenu des leçons
reste en français. Usage : Translator(lang)(cle, **variables).
"""

LANGUES = ["fr", "en"]
NOMS_LANGUES = {"fr": "Français", "en": "English"}

STRINGS = {
    "fr": {
        # Barre d'outils
        "tb_theme": "🎨 Thème : {label}",
        "tb_glossaire": "📖 Glossaire",
        "tb_revision": "🎲 Révision",
        "tb_stats": "📊 Stats",
        "tb_doc": "🐍 Doc Python",
        "tb_brouillon": "✎ Brouillon",
        "tb_reset": "↻ Réinitialiser",
        "tb_lang": "🌐 EN",
        # Barre latérale
        "side_parcours": "  Parcours",
        "side_badges": "  Badges",
        # Boutons d'exercice
        "btn_run": "▶ Exécuter",
        "btn_check": "✓ Vérifier",
        "btn_step": "🐞 Pas-à-pas",
        "btn_hint": "💡 Indice",
        "btn_solution": "Solution",
        "btn_export": "⬇ .py",
        "mode_debug": "🐞 Ce code contient un bug : répare-le, puis clique Vérifier.",
        "mode_trous": "✏️ Complète les ____ manquants, puis clique Vérifier.",
        "trous_restants": "Il reste des ____ à compléter.",
        "tb_reco": "🧭 Et après ?",
        "tb_examen": "✍ Examen",
        "btn_note": "📝 Note",
        "fav_oui": "★",
        "fav_non": "☆",
        "note_title": "Ma note",
        "note_intro": "Note personnelle pour cette leçon :",
        "note_save": "Enregistrer",
        "reco_title": "Et maintenant ?",
        "reco_revision": "🧭 Révision conseillée : refais cet exercice de mémoire.",
        "reco_nouvelle": "🧭 Voici la prochaine leçon conseillée.",
        "reco_termine": "🎉 Tout est terminé, bravo ! Lance une révision quand tu veux.",
        "nudge_indice": "💡 Bloqué ? Pense aux boutons « Indice » et « Solution ».",
        "st_niveau": "⭐ Niveau {niv}  ({dans}/{pour} XP)",
        "st_hebdo": "📅 Cette semaine : {n}/{obj}",
        "st_hebdo_label": "Objectif hebdo :",
        "st_export": "⬇ Exporter…",
        "st_import": "⬆ Importer…",
        "dlg_export_ok": "Progression exportée.",
        "dlg_import_ok": "Progression importée avec succès.",
        "dlg_import_err": "Fichier de progression invalide.",
        "ex_title": "Mode examen",
        "ex_intro": "Des questions au hasard, 5 minutes chrono. Prêt ?",
        "ex_start": "Commencer l'examen",
        "ex_q": "Question {i}/{n}",
        "ex_time": "⏱ {m}:{s:02d}",
        "ex_valider": "Valider",
        "ex_suivant": "Suivant ▶",
        "ex_termine": "Examen terminé !",
        "ex_score": "Score : {bons}/{total}",
        "ex_temps": "⏱ Temps écoulé !",
        "ex_fermer": "Fermer",
        "gl_cards": "🃏 Flashcards",
        "gl_cheatsheet": "📄 Antisèche",
        "cheat_title": "Antisèche Python",
        "cheat_fail": "Impossible d'ouvrir l'antisèche.",
        "fc_title": "Flashcards",
        "fc_flip": "Retourner la carte",
        "fc_next": "Suivant ▶",
        "fc_progress": "Carte {i}/{n}",
        "fc_recto": "Terme",
        "fc_verso": "Définition",
        "fc_done": "Révision terminée 🎉",
        "fc_replay": "Recommencer",
        "fc_close": "Fermer",
        # Syntaxe
        "syntax_ok": "✓ syntaxe correcte",
        "syntax_err": "⚠ ligne {n} : {msg}",
        # Retours
        "fb_ok": "Réussi ✓",
        "fb_fail": "Pas encore…",
        "fb_exported": "Exporté ✓",
        "banner_exo": "Bravo, exercice réussi !",
        "banner_quiz": "Bonne réponse !",
        # Console
        "con_vars": "── Variables ──",
        "con_no_output": "(aucune sortie)",
        "con_compare": "── Comparaison ──",
        "con_expected": "Attendu :",
        "con_obtained": "Obtenu :",
        "con_first_diff": "(première différence à la ligne {n})",
        "con_no_hint": "Pas d'indice pour cet exercice.",
        "con_no_more_hint": "(plus d'indice — essaie « Solution »)",
        "con_hint": "💡 Indice {i}/{n} : {texte}",
        # Quiz
        "quiz_validate": "Valider",
        "quiz_choose": "Choisis une réponse.",
        "quiz_good": "✓ Bonne réponse ! ",
        "quiz_bad": "✗ Pas tout à fait, réessaie.",
        # Barre d'état
        "status": ("⭐ Nv {niv} · {done}/{total} · {pct}%   |   Badges {b}/{n}   |   "
                   "🔥 {s} j · auj. {cible}   |   révisions dues : {dus}"),
        # Fenêtre Brouillon
        "sb_title": "Brouillon — bac à sable",
        "sb_intro": "✎ Bac à sable : écris du code et exécute-le librement (modules limités)",
        "sb_run": "▶ Exécuter (Ctrl+Entrée)",
        "sb_clear": "Effacer le code",
        "sb_starter": ("# Bac à sable : teste ce que tu veux, puis clique Exécuter\n\n"
                       'message = "Bonjour"\nfor i in range(3):\n    print(message, i)\n'),
        # Fenêtre Stats
        "st_title": "📊 Mes statistiques",
        "st_streak": "🔥 Série en cours : {n} jour(s)",
        "st_record": "🏆 Record de série : {n} jour(s)",
        "st_total": "✅ Exercices et quiz réussis : {n}",
        "st_today": "🎯 Aujourd'hui : {auj}/{obj}",
        "st_due": "🔁 Révisions dues : {n}",
        "st_objective": "Objectif quotidien :",
        "st_7days": "7 derniers jours",
        "st_certs": "🎓 Certificats des parcours terminés",
        # Fenêtre pas-à-pas
        "step_title": "Exécution pas à pas",
        "step_prev": "◀ Précédent",
        "step_next": "Suivant ▶",
        "step_vars": "Variables à cette étape",
        "step_out": "Sortie produite",
        "step_label": "Étape {i}/{n}",
        "step_line": " — ligne {l}",
        "step_end": " — fin",
        "step_no_vars": "(aucune variable pour l'instant)",
        "step_no_out": "(pas encore de sortie)",
        "step_nothing": "Rien à exécuter ligne par ligne.",
        # Glossaire
        "gl_title": "📖 Glossaire Python",
        # Accueil
        "wel_title": "🐍  Bienvenue !",
        "wel_start": "Commencer",
        "wel_body": (
            "PythonLearn t'accompagne du tout début jusqu'aux projets concrets.\n\n"
            "• À gauche : les parcours et leurs leçons. Une coche verte = réussi.\n"
            "• Lis l'explication en haut, puis code dans l'éditeur.\n"
            "• « Exécuter » lance ton code ; « Vérifier » valide l'exercice.\n"
            "• Bloqué ? Clique « Indice » (plusieurs niveaux), puis « Solution ».\n"
            "• Termine un parcours entier pour décrocher son badge 🏅.\n\n"
            "Astuces : Ctrl+Entrée exécute, Ctrl+/ commente, A-/A+ zoome,\n"
            "et tu peux changer de thème ou de langue en haut.\n\n"
            "Aucune pression : essaie, observe, recommence. Bon code !"),
        # Dialogues
        "dlg_reset_title": "Réinitialiser",
        "dlg_reset_msg": "Effacer toute ta progression et le code sauvegardé ?",
        "dlg_cert_title": "Certificat",
        "dlg_cert_prompt": "Ton nom (pour le certificat) :",
        "dlg_cert_default": "Apprenti(e) Python",
        "dlg_cert_fail": "Impossible d'enregistrer le certificat.",
        "dlg_revision_title": "Révision",
        "dlg_revision_none": "Termine d'abord quelques exercices pour réviser.",
        "fb_revision_due": "Révision ({n} due(s)) — refais l'exercice de mémoire",
        "fb_revision_random": "Aucune révision due : exercice au hasard",
        "dlg_solution_title": "Solution",
        "dlg_solution_none": "Pas de solution prédéfinie ici.",
        "dlg_solution_confirm": "Remplacer ton code par la solution ?",
        "dlg_step_title": "Pas à pas",
        "con_zombie": ("⚠ {n} exécution(s) précédente(s) tourne(nt) "
                       "encore en arrière-plan : une boucle refuse de "
                       "s'arrêter. Ferme et rouvre l'application si "
                       "elle ralentit."),
        "err_timeout": ("TimeoutError : exécution interrompue, le "
                        "programme a tourné trop longtemps "
                        "(boucle infinie ?)."),
        "pred_titre": "Que va afficher ce programme ?",
        "pred_saisie": ("Écris ta prédiction avant d'exécuter "
                        "(une ligne par ligne affichée) :"),
        "pred_verifier": "✓ Vérifier ma prédiction",
        "pred_juste": "Exact — c'est bien ce que le programme affiche.",
        "pred_faux": "Pas tout à fait. Compare ci-dessous.",
        "pred_tienne": "Ta prédiction :",
        "pred_reelle": "Sortie réelle :",
        "pred_diff": "Première différence à la ligne {n}.",
        "pred_erreur": "Le programme s'arrête sur une erreur :",
        "ord_titre": "Remets les lignes dans le bon ordre",
        "ord_aide": ("Sélectionne une ligne, puis déplace-la "
                     "(ou Ctrl + ↑ / Ctrl + ↓)."),
        "ord_monter": "▲ Monter",
        "ord_descendre": "▼ Descendre",
        "ord_verifier": "✓ Vérifier l'ordre",
        "ord_juste": "Bon ordre, bravo !",
        "ord_faux": "Ce n'est pas encore le bon ordre.",
        "ord_indice": "La ligne {n} n'est pas à sa place.",
        "tb_apropos": "ℹ À propos",
        "ap_title": "À propos de PythonLearn",
        "ap_version": "Version {v}",
        "ap_par": "Conçu et réalisé par",
        "ap_desc": ("Une application pour apprendre Python pas à pas, "
                    "du tout débutant aux projets concrets."),
        "ap_licence": "Licence MIT — logiciel libre et gratuit",
        "ap_depot": "Code source",
        "ap_fermer": "Fermer",
        "tb_lecons": "📦 Mes leçons",
        "dlg_lecons_title": "Mes leçons",
        "dlg_lecons_msg": ("Dépose tes fichiers de leçons (.json) dans "
                           "ce dossier :\n{dossier}\n\n"
                           "Un exemple à modifier s'y trouve déjà. "
                           "Relance PythonLearn pour voir apparaître "
                           "ton parcours."),
        "dlg_packs_title": "Packs de leçons",
        "dlg_packs_msg": ("Certaines leçons ajoutées n'ont pas pu être "
                          "chargées :\n\n{details}\n\n"
                          "Pour le détail, lance dans un terminal :\n"
                          "python main.py --verifier-packs"),
        "dlg_incident_title": "Progression",
        "dlg_incident_restaure": (
            "Ton fichier de progression était illisible : une sauvegarde "
            "de secours a été restaurée.\n\nTu as peut-être perdu les "
            "toutes dernières minutes de travail, mais rien de plus."),
        "dlg_incident_perdu": (
            "Ton fichier de progression était illisible et aucune "
            "sauvegarde n'a pu le remplacer.\n\nIl a été mis de côté "
            "ici :\n{chemin}\n\nL'application repart d'une progression "
            "vierge."),
        "dlg_export_title": "Export",
        "dlg_export_fail": "Impossible d'enregistrer le fichier.",
    },
    "en": {
        "tb_theme": "🎨 Theme: {label}",
        "tb_glossaire": "📖 Glossary",
        "tb_revision": "🎲 Review",
        "tb_stats": "📊 Stats",
        "tb_doc": "🐍 Python Docs",
        "tb_brouillon": "✎ Scratchpad",
        "tb_reset": "↻ Reset",
        "tb_lang": "🌐 FR",
        "side_parcours": "  Tracks",
        "side_badges": "  Badges",
        "btn_run": "▶ Run",
        "btn_check": "✓ Check",
        "btn_step": "🐞 Step",
        "btn_hint": "💡 Hint",
        "btn_solution": "Solution",
        "btn_export": "⬇ .py",
        "mode_debug": "🐞 This code has a bug: fix it, then click Check.",
        "mode_trous": "✏️ Fill in the missing ____, then click Check.",
        "trous_restants": "Some ____ still need to be filled in.",
        "tb_reco": "🧭 What next?",
        "tb_examen": "✍ Exam",
        "btn_note": "📝 Note",
        "fav_oui": "★",
        "fav_non": "☆",
        "note_title": "My note",
        "note_intro": "Personal note for this lesson:",
        "note_save": "Save",
        "reco_title": "What now?",
        "reco_revision": "🧭 Suggested review: redo this exercise from memory.",
        "reco_nouvelle": "🧭 Here is the next suggested lesson.",
        "reco_termine": "🎉 All done, congrats! Start a review whenever you like.",
        "nudge_indice": "💡 Stuck? Remember the “Hint” and “Solution” buttons.",
        "st_niveau": "⭐ Level {niv}  ({dans}/{pour} XP)",
        "st_hebdo": "📅 This week: {n}/{obj}",
        "st_hebdo_label": "Weekly goal:",
        "st_export": "⬇ Export…",
        "st_import": "⬆ Import…",
        "dlg_export_ok": "Progress exported.",
        "dlg_import_ok": "Progress imported successfully.",
        "dlg_import_err": "Invalid progress file.",
        "ex_title": "Exam mode",
        "ex_intro": "Random questions, 5-minute timer. Ready?",
        "ex_start": "Start the exam",
        "ex_q": "Question {i}/{n}",
        "ex_time": "⏱ {m}:{s:02d}",
        "ex_valider": "Submit",
        "ex_suivant": "Next ▶",
        "ex_termine": "Exam finished!",
        "ex_score": "Score: {bons}/{total}",
        "ex_temps": "⏱ Time's up!",
        "ex_fermer": "Close",
        "gl_cards": "🃏 Flashcards",
        "gl_cheatsheet": "📄 Cheat-sheet",
        "cheat_title": "Python cheat-sheet",
        "cheat_fail": "Could not open the cheat-sheet.",
        "fc_title": "Flashcards",
        "fc_flip": "Flip the card",
        "fc_next": "Next ▶",
        "fc_progress": "Card {i}/{n}",
        "fc_recto": "Term",
        "fc_verso": "Definition",
        "fc_done": "Review finished 🎉",
        "fc_replay": "Restart",
        "fc_close": "Close",
        "syntax_ok": "✓ syntax OK",
        "syntax_err": "⚠ line {n}: {msg}",
        "fb_ok": "Passed ✓",
        "fb_fail": "Not yet…",
        "fb_exported": "Exported ✓",
        "banner_exo": "Well done, exercise solved!",
        "banner_quiz": "Correct answer!",
        "con_vars": "── Variables ──",
        "con_no_output": "(no output)",
        "con_compare": "── Comparison ──",
        "con_expected": "Expected:",
        "con_obtained": "Got:",
        "con_first_diff": "(first difference on line {n})",
        "con_no_hint": "No hint for this exercise.",
        "con_no_more_hint": "(no more hints — try “Solution”)",
        "con_hint": "💡 Hint {i}/{n}: {texte}",
        "quiz_validate": "Submit",
        "quiz_choose": "Pick an answer.",
        "quiz_good": "✓ Correct! ",
        "quiz_bad": "✗ Not quite, try again.",
        "status": ("⭐ Lv {niv} · {done}/{total} · {pct}%   |   Badges {b}/{n}   |   "
                   "🔥 {s} d · today {cible}   |   reviews due: {dus}"),
        "sb_title": "Scratchpad",
        "sb_intro": "✎ Scratchpad: write code and run it freely (limited modules)",
        "sb_run": "▶ Run (Ctrl+Enter)",
        "sb_clear": "Clear code",
        "sb_starter": ("# Scratchpad: try anything, then click Run\n\n"
                       'message = "Hello"\nfor i in range(3):\n    print(message, i)\n'),
        "st_title": "📊 My statistics",
        "st_streak": "🔥 Current streak: {n} day(s)",
        "st_record": "🏆 Best streak: {n} day(s)",
        "st_total": "✅ Exercises and quizzes passed: {n}",
        "st_today": "🎯 Today: {auj}/{obj}",
        "st_due": "🔁 Reviews due: {n}",
        "st_objective": "Daily goal:",
        "st_7days": "Last 7 days",
        "st_certs": "🎓 Certificates of completed tracks",
        "step_title": "Step-by-step execution",
        "step_prev": "◀ Previous",
        "step_next": "Next ▶",
        "step_vars": "Variables at this step",
        "step_out": "Output so far",
        "step_label": "Step {i}/{n}",
        "step_line": " — line {l}",
        "step_end": " — end",
        "step_no_vars": "(no variables yet)",
        "step_no_out": "(no output yet)",
        "step_nothing": "Nothing to run line by line.",
        "gl_title": "📖 Python glossary",
        "wel_title": "🐍  Welcome!",
        "wel_start": "Start",
        "wel_body": (
            "PythonLearn takes you from the very basics to real projects.\n\n"
            "• On the left: the tracks and their lessons. A green check = solved.\n"
            "• Read the explanation at the top, then code in the editor.\n"
            "• “Run” executes your code; “Check” validates the exercise.\n"
            "• Stuck? Click “Hint” (several levels), then “Solution”.\n"
            "• Finish a whole track to earn its badge 🏅.\n\n"
            "Tips: Ctrl+Enter runs, Ctrl+/ comments, A-/A+ zooms,\n"
            "and you can switch theme or language at the top.\n\n"
            "No pressure: try, observe, repeat. Happy coding!"),
        "dlg_reset_title": "Reset",
        "dlg_reset_msg": "Erase all your progress and saved code?",
        "dlg_cert_title": "Certificate",
        "dlg_cert_prompt": "Your name (for the certificate):",
        "dlg_cert_default": "Python Learner",
        "dlg_cert_fail": "Could not save the certificate.",
        "dlg_revision_title": "Review",
        "dlg_revision_none": "Solve a few exercises first to be able to review.",
        "fb_revision_due": "Review ({n} due) — redo the exercise from memory",
        "fb_revision_random": "No review due: random exercise",
        "dlg_solution_title": "Solution",
        "dlg_solution_none": "No predefined solution here.",
        "dlg_solution_confirm": "Replace your code with the solution?",
        "dlg_step_title": "Step-by-step",
        "con_zombie": ("⚠ {n} earlier run(s) still going in the "
                       "background: a loop refuses to stop. Close and "
                       "reopen the application if it slows down."),
        "err_timeout": ("TimeoutError: execution stopped, the program "
                        "ran for too long (infinite loop?)."),
        "pred_titre": "What will this program print?",
        "pred_saisie": ("Write your prediction before running it "
                        "(one line per printed line):"),
        "pred_verifier": "✓ Check my prediction",
        "pred_juste": "Correct — that is what the program prints.",
        "pred_faux": "Not quite. Compare below.",
        "pred_tienne": "Your prediction:",
        "pred_reelle": "Actual output:",
        "pred_diff": "First difference on line {n}.",
        "pred_erreur": "The program stops with an error:",
        "ord_titre": "Put the lines back in the right order",
        "ord_aide": ("Select a line, then move it "
                     "(or Ctrl + ↑ / Ctrl + ↓)."),
        "ord_monter": "▲ Up",
        "ord_descendre": "▼ Down",
        "ord_verifier": "✓ Check the order",
        "ord_juste": "Right order, well done!",
        "ord_faux": "Not the right order yet.",
        "ord_indice": "Line {n} is not in the right place.",
        "tb_apropos": "ℹ About",
        "ap_title": "About PythonLearn",
        "ap_version": "Version {v}",
        "ap_par": "Designed and built by",
        "ap_desc": ("An application to learn Python step by step, from "
                    "complete beginner to real projects."),
        "ap_licence": "MIT License — free and open source",
        "ap_depot": "Source code",
        "ap_fermer": "Close",
        "tb_lecons": "📦 My lessons",
        "dlg_lecons_title": "My lessons",
        "dlg_lecons_msg": ("Put your lesson files (.json) in this "
                           "folder:\n{dossier}\n\n"
                           "An example to edit is already there. "
                           "Restart PythonLearn to see your track "
                           "appear."),
        "dlg_packs_title": "Lesson packs",
        "dlg_packs_msg": ("Some added lessons could not be "
                          "loaded:\n\n{details}\n\n"
                          "For details, run in a terminal:\n"
                          "python main.py --verifier-packs"),
        "dlg_incident_title": "Progress",
        "dlg_incident_restaure": (
            "Your progress file could not be read, so a backup was "
            "restored.\n\nYou may have lost the last few minutes of work, "
            "but nothing more."),
        "dlg_incident_perdu": (
            "Your progress file could not be read and no backup could "
            "replace it.\n\nIt has been set aside here:\n{chemin}\n\n"
            "The app is starting from a blank progress."),
        "dlg_export_title": "Export",
        "dlg_export_fail": "Could not save the file.",
    },
}


class Translator:
    def __init__(self, lang="fr"):
        self.lang = lang if lang in LANGUES else "fr"

    def set(self, lang):
        if lang in LANGUES:
            self.lang = lang

    def __call__(self, cle, **kw):
        texte = STRINGS.get(self.lang, STRINGS["fr"]).get(cle, cle)
        return texte.format(**kw) if kw else texte
