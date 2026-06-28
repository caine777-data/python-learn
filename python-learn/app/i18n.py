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
        "status": ("{done}/{total} · {pct}%   |   Badges {b}/{n}   |   "
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
        "status": ("{done}/{total} · {pct}%   |   Badges {b}/{n}   |   "
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
