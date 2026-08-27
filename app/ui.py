"""Interface graphique de PythonLearn (version enrichie)."""

import os
import pathlib
import random
import sys
import tkinter as tk
import webbrowser
from datetime import date
from tkinter import filedialog, font, messagebox, simpledialog, ttk

from app import errors, stats
from app import progress as prog
from app.editor import CodeEditor
from app.i18n import LANGUES, Translator
from app.theme import THEME_ORDER, THEMES, assombrir, eclaircir
from app.windows import Celebration, ExamWindow, FlashcardWindow, StepWindow
from content import (
    CURRICULUM,
    GLOSSAIRE,
    ajouter_packs,
    exercice_count,
    find_lesson,
    get_exercice,
    hints_for,
    lesson_done,
    lesson_items,
    total_count,
)

try:
    from app.icon import ICON_B64
except Exception:
    ICON_B64 = None


# Délai avant d'écrire le code de l'apprenant sur disque. Sans ce sursis,
# on réécrirait tout le fichier de progression à CHAQUE touche du clavier.
DELAI_SAUVEGARDE_MS = 700


LEVEL_BADGE_NAMES = {
    "debutant": "Débutant", "intermediaire": "Intermédiaire",
    "avance": "Avancé", "expert": "Expert",
    "scripts": "Scripts & automatisation", "interfaces": "Interfaces graphiques",
    "web": "Python & le web", "admin": "Administrer son PC",
    "sqlite": "Bases de données (SQLite)", "turtle": "Dessiner (turtle)",
    "algos": "Algorithmes", "donnees": "Manipuler des données",
    "tests_tdd": "Tests & TDD",
    "projets": "Projets guidés", "entrainement": "Entraînement",
}


class PythonLearnApp:
    def __init__(self, root):
        self.root = root
        self.data = prog.load_progress()
        self._incident = prog.dernier_incident()
        self.theme_name = self.data.get("theme", "dark")
        if self.theme_name not in THEMES:
            self.theme_name = "dark"
        self.C = THEMES[self.theme_name]
        self.lang = self.data.get("langue", "fr")
        if self.lang not in LANGUES:
            self.lang = "fr"
        self.tr = Translator(self.lang)
        self._i18n = []
        self.code_size = 11
        self.current = None
        self.exo_index = 0
        self._hints = []
        self._hint_idx = 0
        self.search_query = ""
        self._revision_item = None
        self._ignore_next_select = False
        self._echecs_session = 0
        self._tip = None
        self._tip_row = None
        self.soucis_packs = []          # packs de leçons mal formés
        self._save_after_id = None      # sauvegarde différée en attente
        self._code_en_attente = None    # (item_id, texte) restant à écrire

        self.lesson_level = {}
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                self.lesson_level[lesson["id"]] = level

        root.title("PythonLearn — apprendre Python pas à pas")
        root.geometry("1180x780")
        root.minsize(980, 660)

        self._init_fonts()
        self._build_layout()
        self.apply_theme()
        self._populate_tree()
        self._refresh_badges()
        self._refresh_status()
        self._select_first_incomplete()

        if self._incident:
            self.root.after(400, self._avertir_incident)
        elif not self.data.get("vu_accueil"):
            self.root.after(300, self._show_welcome)

    def _avertir_incident(self):
        """Prévient l'apprenant quand la progression n'a pas pu être lue telle quelle."""
        code, detail = self._incident
        self._incident = None
        cle = ("dlg_incident_restaure" if code == prog.INCIDENT_RESTAURE
               else "dlg_incident_perdu")
        messagebox.showwarning(self.tr("dlg_incident_title"),
                               self.tr(cle, chemin=detail))
        if not self.data.get("vu_accueil"):
            self._show_welcome()

    def _ouvrir_mes_lecons(self):
        """Ouvre le dossier des leçons personnelles dans l'explorateur.

        Le dossier est créé au besoin, et garni d'un exemple s'il est vide :
        celui qui découvre la fonction a ainsi tout de suite un fichier à
        modifier, plutôt qu'un dossier vide et une page blanche.
        """
        from content.packs import DOSSIER_PACKS, modele_pack
        try:
            DOSSIER_PACKS.mkdir(parents=True, exist_ok=True)
            exemple = DOSSIER_PACKS / "mon-cours.json"
            if not any(DOSSIER_PACKS.glob("*.json")):
                exemple.write_text(modele_pack(), encoding="utf-8")
        except OSError as exc:
            messagebox.showwarning(self.tr("dlg_lecons_title"), str(exc))
            return

        if not _ouvrir_dossier(DOSSIER_PACKS):
            # Pas d'explorateur disponible : on donne le chemin à recopier.
            messagebox.showinfo(self.tr("dlg_lecons_title"),
                                str(DOSSIER_PACKS))
            return
        messagebox.showinfo(self.tr("dlg_lecons_title"),
                            self.tr("dlg_lecons_msg", dossier=str(DOSSIER_PACKS)))

    def _avertir_packs(self):
        """Signale les leçons ajoutées qui n'ont pas pu être chargées."""
        soucis, self.soucis_packs = self.soucis_packs, []
        if not soucis:
            return
        apercu = "\n".join("• " + souci for souci in soucis[:8])
        if len(soucis) > 8:
            apercu += "\n… et " + str(len(soucis) - 8) + " autre(s)."
        messagebox.showwarning(self.tr("dlg_packs_title"),
                               self.tr("dlg_packs_msg", details=apercu))

    def quitter(self):
        """Ferme l'application après avoir écrit le code encore en attente."""
        self._flush_code()
        self.root.destroy()

    # --------------------------------------------------------------- polices
    def _init_fonts(self):
        self.code_font = font.nametofont("TkFixedFont").copy()
        self.code_font.configure(size=self.code_size)
        self.body = font.nametofont("TkDefaultFont").copy()
        self.body.configure(size=11)
        self.title_font = self.body.copy()
        self.title_font.configure(size=16, weight="bold")
        self.h2_font = (self.body.cget("family"), 13, "bold")

    # ---------------------------------------------------------------- layout
    def _tbtn(self, parent, key, command, **kw):
        btn = ttk.Button(parent, text=self.tr(key), command=command, **kw)
        self._i18n.append((btn, key))
        return btn

    def _build_layout(self):
        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass

        # barre d'outils supérieure
        toolbar = ttk.Frame(self.root, style="Panel.TFrame")
        toolbar.pack(fill=tk.X, side=tk.TOP)
        self.theme_btn = ttk.Button(toolbar, text="", command=self.cycle_theme, width=20)
        self.theme_btn.pack(side=tk.LEFT, padx=4, pady=4)
        self.lang_btn = ttk.Button(toolbar, text=self.tr("tb_lang"), width=6,
                                   command=self.cycle_langue)
        self.lang_btn.pack(side=tk.LEFT, pady=4)
        ttk.Button(toolbar, text="A-", width=3,
                   command=lambda: self._zoom(-1)).pack(side=tk.LEFT, padx=(6, 0), pady=4)
        ttk.Button(toolbar, text="A+", width=3,
                   command=lambda: self._zoom(1)).pack(side=tk.LEFT, padx=(0, 8), pady=4)
        self._tbtn(toolbar, "tb_glossaire", self._show_glossaire).pack(side=tk.LEFT, pady=4)
        self._tbtn(toolbar, "tb_revision", self._revision).pack(side=tk.LEFT, padx=6, pady=4)
        self._tbtn(toolbar, "tb_stats", self._show_stats).pack(side=tk.LEFT, pady=4)
        self._tbtn(toolbar, "tb_doc",
                   lambda: webbrowser.open("https://docs.python.org/fr/3/")).pack(side=tk.LEFT, padx=6, pady=4)
        self._tbtn(toolbar, "tb_brouillon", self._show_sandbox).pack(side=tk.LEFT, pady=4)
        self._tbtn(toolbar, "tb_reco", self._recommander).pack(side=tk.LEFT, padx=6, pady=4)
        self._tbtn(toolbar, "tb_examen", self._mode_examen).pack(side=tk.LEFT, pady=4)
        self._tbtn(toolbar, "tb_lecons", self._ouvrir_mes_lecons).pack(
            side=tk.LEFT, padx=6, pady=4)
        self._tbtn(toolbar, "tb_reset", self._reset_progress).pack(side=tk.RIGHT, padx=4, pady=4)

        outer = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        outer.pack(fill=tk.BOTH, expand=True, padx=8, pady=(6, 0))

        # --- barre latérale ---
        side = ttk.Frame(outer, style="Panel.TFrame", width=340)
        outer.add(side, weight=0)

        self.side_header = tk.Label(side, text=self.tr("side_parcours"),
                                    font=self.title_font, anchor="w")
        self.side_header.pack(fill=tk.X, pady=(8, 4), padx=4)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(side, textvariable=self.search_var)
        self.search_entry.pack(fill=tk.X, padx=6, pady=(0, 4))
        self.search_entry.bind("<KeyRelease>", self._on_search)

        tree_wrap = ttk.Frame(side, style="Panel.TFrame")
        tree_wrap.pack(fill=tk.BOTH, expand=True, padx=6, pady=4)
        self.tree = ttk.Treeview(tree_wrap, show="tree", selectmode="browse")
        self.tree.column("#0", width=320, minwidth=220, stretch=True)
        sb = ttk.Scrollbar(tree_wrap, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)
        self.tree.bind("<Motion>", self._tree_tooltip)
        self.tree.bind("<Leave>", lambda e: self._hide_tooltip())

        self.badge_title = tk.Label(side, text=self.tr("side_badges"), anchor="w",
                                    font=(self.body.cget("family"), 10, "bold"))
        self.badge_title.pack(fill=tk.X, padx=4, pady=(2, 0))
        self.badge_bar = tk.Frame(side)
        self.badge_bar.pack(fill=tk.X, padx=6, pady=(2, 8))
        self.badge_labels = {}
        for level in CURRICULUM:
            lbl = tk.Label(self.badge_bar, text="🔒",
                           font=(self.body.cget("family"), 9))
            lbl.pack(side=tk.LEFT, expand=True)
            self.badge_labels[level["id"]] = lbl

        # --- zone principale ---
        main = ttk.PanedWindow(outer, orient=tk.VERTICAL)
        outer.add(main, weight=1)

        top = ttk.Frame(main)
        main.add(top, weight=3)
        self.lesson_title = ttk.Label(top, text="", style="Title.TLabel")
        self.lesson_title.pack(fill=tk.X, padx=12, pady=(8, 4))

        content_wrap = ttk.Frame(top)
        content_wrap.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 4))
        self.content = tk.Text(content_wrap, wrap="word", relief="flat",
                               font=self.body, padx=8, pady=8, height=11,
                               cursor="arrow")
        csb = ttk.Scrollbar(content_wrap, orient="vertical", command=self.content.yview)
        self.content.configure(yscrollcommand=csb.set)
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        csb.pack(side=tk.RIGHT, fill=tk.Y)
        self.content.configure(state="disabled")

        # bandeau de succès (superposé)
        self.banner = tk.Label(top, text="", anchor="center")

        self.bottom = ttk.Frame(main)
        main.add(self.bottom, weight=4)
        self._build_exercise_frame()
        self._build_quiz_frame()

        # barre d'état
        status = ttk.Frame(self.root, style="Panel.TFrame")
        status.pack(fill=tk.X, side=tk.BOTTOM)
        self.progress = ttk.Progressbar(status, maximum=total_count(),
                                        length=200, mode="determinate")
        self.progress.pack(side=tk.LEFT, padx=8, pady=6)
        self.status = ttk.Label(status, text="", style="Status.TLabel", anchor="w")
        self.status.pack(side=tk.LEFT, padx=4)

        self.root.bind("<Control-Return>", lambda e: self.run())
        self.root.bind("<Control-plus>", lambda e: self._zoom(1))
        self.root.bind("<Control-KP_Add>", lambda e: self._zoom(1))
        self.root.bind("<Control-minus>", lambda e: self._zoom(-1))
        self.root.bind("<Control-KP_Subtract>", lambda e: self._zoom(-1))
        self.root.bind("<Control-0>", lambda e: self._zoom(0))

    def _build_exercise_frame(self):
        self.exo_frame = ttk.Frame(self.bottom)
        self.exo_tabs = ttk.Frame(self.exo_frame)
        self.exo_tabs.pack(fill=tk.X, padx=12, pady=(6, 0))
        self.tab_buttons = []

        self.mode_label = ttk.Label(self.exo_frame, text="", style="Mode.TLabel",
                                    wraplength=760, justify="left")
        self.mode_label.pack(anchor="w", padx=12, pady=(4, 0))

        self.enonce = ttk.Label(self.exo_frame, text="", style="Muted.TLabel",
                                wraplength=700, justify="left")
        self.enonce.pack(anchor="w", padx=12, pady=(2, 2))

        ed_wrap = ttk.Frame(self.exo_frame)
        ed_wrap.pack(fill=tk.BOTH, expand=True, padx=12)
        self.editor = CodeEditor(ed_wrap, self.code_font,
                                 on_change=self._on_code_change,
                                 on_syntax=self._maj_syntaxe)
        self.editor.pack(fill=tk.BOTH, expand=True)

        self.syntax_label = ttk.Label(self.exo_frame, text="", style="Muted.TLabel")
        self.syntax_label.pack(anchor="w", padx=12)

        btns = ttk.Frame(self.exo_frame)
        btns.pack(fill=tk.X, padx=12, pady=6)
        self._tbtn(btns, "btn_run", self.run, style="Primary.TButton").pack(side=tk.LEFT)
        self._tbtn(btns, "btn_check", self.check, style="Primary.TButton").pack(side=tk.LEFT, padx=6)
        self._tbtn(btns, "btn_step", self._pas_a_pas).pack(side=tk.LEFT)
        self._tbtn(btns, "btn_hint", self.show_hint).pack(side=tk.LEFT, padx=6)
        self._tbtn(btns, "btn_solution", self.show_solution).pack(side=tk.LEFT)
        self._tbtn(btns, "btn_export", self._exporter_py).pack(side=tk.LEFT, padx=6)
        self._tbtn(btns, "btn_note", self._editer_note).pack(side=tk.LEFT)
        self.fav_btn = ttk.Button(btns, text=self.tr("fav_non"), width=3,
                                  command=self._toggle_favori)
        self.fav_btn.pack(side=tk.LEFT, padx=6)
        ttk.Button(btns, text="↺", width=3, command=self.reset_code).pack(side=tk.LEFT)
        self.feedback = ttk.Label(btns, text="", style="TLabel")
        self.feedback.pack(side=tk.LEFT, padx=10)

        con_wrap = ttk.Frame(self.exo_frame)
        con_wrap.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 4))
        self.console = tk.Text(con_wrap, wrap="word", relief="flat",
                               font=self.code_font, height=6, padx=10, pady=8,
                               state="disabled")
        consb = ttk.Scrollbar(con_wrap, orient="vertical", command=self.console.yview)
        self.console.configure(yscrollcommand=consb.set)
        self.console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        consb.pack(side=tk.RIGHT, fill=tk.Y)

    def _build_quiz_frame(self):
        self.quiz_frame = ttk.Frame(self.bottom)
        self.quiz_question = ttk.Label(self.quiz_frame, text="", style="Title.TLabel",
                                       wraplength=720, justify="left")
        self.quiz_question.pack(anchor="w", padx=16, pady=(16, 10))
        self.quiz_var = tk.IntVar(value=-1)
        self.quiz_options = ttk.Frame(self.quiz_frame)
        self.quiz_options.pack(anchor="w", padx=24)
        self.quiz_radios = []
        self._tbtn(self.quiz_frame, "quiz_validate", self.check_quiz).pack(
            anchor="w", padx=16, pady=12)
        self.quiz_feedback = ttk.Label(self.quiz_frame, text="", style="TLabel",
                                       wraplength=720, justify="left")
        self.quiz_feedback.pack(anchor="w", padx=16)

    # ----------------------------------------------------------------- thème
    def apply_theme(self):
        C = self.C
        self.root.configure(bg=C["bg"])
        s = self.style
        s.configure("TFrame", background=C["bg"])
        s.configure("Panel.TFrame", background=C["panel"])
        s.configure("TLabel", background=C["bg"], foreground=C["fg"])
        s.configure("Muted.TLabel", background=C["bg"], foreground=C["muted"])
        s.configure("Mode.TLabel", background=C["bg"], foreground=C["accent"],
                    font=(self.body.cget("family"), 10, "bold"))
        s.configure("Title.TLabel", background=C["bg"], foreground=C["fg"],
                    font=self.title_font)
        s.configure("Status.TLabel", background=C["panel"], foreground=C["muted"])

        # Boutons plats et modernes, avec effet de survol.
        survol = eclaircir(C["panel"], 0.10) if self.theme_name != "light" \
            else assombrir(C["panel"], 0.06)
        s.configure("TButton", font=self.body, relief="flat", borderwidth=0,
                    padding=(11, 6), background=C["panel"], foreground=C["fg"],
                    focuscolor=C["panel"], bordercolor=C["panel"],
                    lightcolor=C["panel"], darkcolor=C["panel"])
        s.map("TButton",
              background=[("pressed", assombrir(C["panel"], 0.10)),
                          ("active", survol)],
              foreground=[("disabled", C["muted"])])
        # Boutons primaires (Exécuter / Vérifier) en couleur d'accent.
        s.configure("Primary.TButton", background=C["accent"], foreground=C["sel_fg"],
                    font=(self.body.cget("family"), 10, "bold"), padding=(13, 6),
                    borderwidth=0, relief="flat", focuscolor=C["accent"],
                    bordercolor=C["accent"], lightcolor=C["accent"],
                    darkcolor=C["accent"])
        s.map("Primary.TButton",
              background=[("pressed", assombrir(C["accent"], 0.22)),
                          ("active", assombrir(C["accent"], 0.10))])
        s.configure("TButton", font=self.body)
        s.configure("TEntry", fieldbackground=C["editor"], foreground=C["fg"])
        s.configure("Treeview", background=C["panel"], fieldbackground=C["panel"],
                    foreground=C["fg"], rowheight=29, borderwidth=0)
        s.map("Treeview", background=[("selected", C["accent"])],
              foreground=[("selected", C["sel_fg"])])
        s.configure("TProgressbar", background=C["accent"], troughcolor=C["bg"],
                    borderwidth=0, thickness=10, bordercolor=C["bg"],
                    lightcolor=C["accent"], darkcolor=C["accent"])
        s.configure("Niv.Horizontal.TProgressbar", background=C["ok"],
                    troughcolor=C["panel"], borderwidth=0, thickness=12,
                    lightcolor=C["ok"], darkcolor=C["ok"])

        self.content.configure(bg=C["bg"], fg=C["fg"], insertbackground=C["fg"])
        self.console.configure(bg=C["console"], fg=C["fg"], insertbackground=C["fg"])
        self.editor.apply_theme(C)
        self.search_entry.configure(bg=C["editor"], fg=C["fg"], insertbackground=C["fg"],
                                    relief="flat")
        self.side_header.configure(bg=C["panel"], fg=C["accent"])
        self.badge_title.configure(bg=C["panel"], fg=C["muted"])
        self.badge_bar.configure(bg=C["panel"])
        self.banner.configure(bg=C["panel"], fg=C["fg"])

        self._configure_text_tags()
        self.console.tag_configure("ok", foreground=C["ok"])
        self.console.tag_configure("err", foreground=C["err"])
        self.console.tag_configure("muted", foreground=C["muted"])
        self.console.tag_configure("hint", foreground=C["accent"])
        self.console.tag_configure("var", foreground=C["builtin"])
        self.tree.tag_configure("done", foreground=C["ok"])
        self.tree.tag_configure("level", foreground=C["heading"])

        label = self.C["label_en"] if self.lang == "en" else self.C["label"]
        self.theme_btn.configure(text=self.tr("tb_theme", label=label))
        self._refresh_badges()

    def cycle_langue(self):
        i = (LANGUES.index(self.lang) + 1) % len(LANGUES)
        self.lang = LANGUES[i]
        self.tr.set(self.lang)
        prog.set_langue(self.data, self.lang)
        self._apply_language()

    def _apply_language(self):
        for widget, key in self._i18n:
            try:
                widget.configure(text=self.tr(key))
            except tk.TclError:
                pass
        self.lang_btn.configure(text=self.tr("tb_lang"))
        self.side_header.configure(text=self.tr("side_parcours"))
        self.badge_title.configure(text=self.tr("side_badges"))
        label = self.C["label_en"] if self.lang == "en" else self.C["label"]
        self.theme_btn.configure(text=self.tr("tb_theme", label=label))
        self._refresh_status()
        if self.current and self.current.get("type") != "quiz":
            self.editor._verifier_syntaxe()

    def cycle_theme(self):
        i = (THEME_ORDER.index(self.theme_name) + 1) % len(THEME_ORDER)
        self.theme_name = THEME_ORDER[i]
        self.C = THEMES[self.theme_name]
        prog.set_theme(self.data, self.theme_name)
        self.apply_theme()

    def _zoom(self, delta):
        if delta == 0:
            self.code_size = 11
        else:
            self.code_size = max(8, min(22, self.code_size + delta))
        self.code_font.configure(size=self.code_size)
        self.editor.refresh_font()
        self.editor.highlight()

    def _configure_text_tags(self):
        C = self.C
        self.content.tag_configure("h2", foreground=C["heading"], font=self.h2_font,
                                   spacing1=8, spacing3=4)
        self.content.tag_configure("body", foreground=C["fg"], spacing3=4, font=self.body)
        self.content.tag_configure("code", foreground=C["code"], background=C["code_bg"],
                                   font=self.code_font, lmargin1=16, lmargin2=16,
                                   spacing1=2, spacing3=2)
        self.content.tag_configure("inline", foreground=C["code"], font=self.code_font)
        self.content.tag_configure("bullet", foreground=C["fg"], lmargin1=16, lmargin2=30)
        self.content.tag_configure("bold", font=(self.body.cget("family"), 11, "bold"))

    # ---------------------------------------------------------------- arbre
    def _on_search(self, _e):
        self.search_query = self.search_var.get().strip().lower()
        self._populate_tree()

    def _tree_tooltip(self, e):
        row = self.tree.identify_row(e.y)
        if not row:
            self._hide_tooltip()
            return
        if row == self._tip_row:
            return
        self._hide_tooltip()
        self._tip_row = row
        texte = self.tree.item(row, "text").strip()
        if not texte:
            return
        self._tip = tk.Toplevel(self.tree)
        self._tip.overrideredirect(True)
        self._tip.attributes("-topmost", True)
        self._tip.geometry(f"+{e.x_root + 16}+{e.y_root + 12}")
        tk.Label(self._tip, text=texte, bg=self.C["panel"], fg=self.C["fg"],
                 relief="solid", borderwidth=1, padx=6, pady=2,
                 font=self.body).pack()

    def _hide_tooltip(self):
        if self._tip:
            self._tip.destroy()
            self._tip = None
        self._tip_row = None

    def _populate_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.item_to_lesson = {}
        q = self.search_query
        for level in CURRICULUM:
            lessons = [lecon for lecon in level["lessons"]
                       if not q or q in lecon["title"].lower()]
            if q and not lessons:
                continue
            done = sum(1 for lecon in level["lessons"]
                       if lesson_done(lecon, self.data["completed"]))
            total = len(level["lessons"])
            badge = " 🏅" if level["id"] in self.data["badges"] else ""
            parent = self.tree.insert(
                "", "end", open=True, tags=("level",),
                text=f"  {level['title']}  ({done}/{total}){badge}")
            for lesson in lessons:
                d = lesson_done(lesson, self.data["completed"])
                if d:
                    icone = "✓"
                elif lesson.get("type") == "quiz":
                    icone = "?"
                elif lesson.get("mode") == "debug":
                    icone = "🐞"
                elif lesson.get("mode") == "trous":
                    icone = "✏"
                else:
                    icone = "•"
                suffixe = self._suffixe_lecon(lesson)
                node = self.tree.insert(parent, "end",
                                        text=f"  {icone} {lesson['title']}{suffixe}",
                                        tags=("done",) if d else ())
                self.item_to_lesson[node] = lesson

    def _suffixe_lecon(self, lesson):
        """Petits marqueurs en fin de titre : ★ favori, 📝 note."""
        suffixe = ""
        if lesson.get("id") in self.data["favoris"]:
            suffixe += "  ★"
        if lesson.get("id") in self.data["notes"]:
            suffixe += " 📝"
        return suffixe

    def _refresh_badges(self):
        C = self.C
        for level in CURRICULUM:
            lbl = self.badge_labels[level["id"]]
            earned = level["id"] in self.data["badges"]
            lbl.configure(text="🏅" if earned else "🔒", bg=C["panel"],
                          fg=C["accent"] if earned else C["muted"])

    def _select_first_incomplete(self):
        for node, lesson in self.item_to_lesson.items():
            if not lesson_done(lesson, self.data["completed"]):
                self.tree.selection_set(node)
                self.tree.see(node)
                return
        if self.item_to_lesson:
            self.tree.selection_set(next(iter(self.item_to_lesson)))

    def _on_select(self, _e):
        if self._ignore_next_select:
            self._ignore_next_select = False
            return
        sel = self.tree.selection()
        if not sel:
            return
        lesson = self.item_to_lesson.get(sel[0])
        if lesson:
            self._load_lesson(lesson)

    # -------------------------------------------------------------- chargement
    def _load_lesson(self, lesson):
        self._flush_code()          # le code de la leçon quittée part sur disque
        self.current = lesson
        self.exo_index = 0
        self._revision_item = None
        self._echecs_session = 0
        self.lesson_title.configure(text=lesson["title"])
        self._maj_favori_btn()
        self._render_content(lesson.get("content", ""))
        if lesson.get("type") == "quiz":
            self.exo_frame.pack_forget()
            self.quiz_frame.pack(fill=tk.BOTH, expand=True)
            self._load_quiz(lesson)
        else:
            self.quiz_frame.pack_forget()
            self.exo_frame.pack(fill=tk.BOTH, expand=True)
            self._build_exo_tabs()
            self._load_exercice(0)

    def _maj_favori_btn(self):
        if not self.current:
            return
        actif = self.current.get("id") in self.data["favoris"]
        self.fav_btn.configure(text=self.tr("fav_oui" if actif else "fav_non"))

    def _toggle_favori(self):
        if not self.current:
            return
        actif = prog.toggle_favori(self.data, self.current["id"])
        self.fav_btn.configure(text=self.tr("fav_oui" if actif else "fav_non"))
        self._populate_tree()

    def _mode_examen(self):
        quizzes = [lesson for level in CURRICULUM for lesson in level["lessons"]
                   if lesson.get("type") == "quiz"]
        if not quizzes:
            return
        questions = random.sample(quizzes, min(10, len(quizzes)))
        ExamWindow(self.root, self, questions, self.C)

    def _editer_note(self):
        if not self.current:
            return
        C = self.C
        cid = self.current["id"]
        win = tk.Toplevel(self.root)
        win.title(self.tr("note_title"))
        win.configure(bg=C["bg"])
        win.geometry("460x320")
        tk.Label(win, text=self.tr("note_intro"), bg=C["bg"], fg=C["muted"],
                 anchor="w").pack(fill=tk.X, padx=12, pady=(10, 4))
        txt = tk.Text(win, wrap="word", relief="flat", font=self.body,
                      bg=C["console"], fg=C["fg"], padx=8, pady=6)
        txt.pack(fill=tk.BOTH, expand=True, padx=12)
        txt.insert("1.0", self.data["notes"].get(cid, ""))

        def enregistrer():
            prog.set_note(self.data, cid, txt.get("1.0", "end").strip())
            self._populate_tree()
            win.destroy()
        ttk.Button(win, text=self.tr("note_save"),
                   command=enregistrer).pack(pady=10)
        txt.focus_set()

    def _ordre_item_ids(self):
        ids = []
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                ids.extend(lesson_items(lesson))
        return ids

    def _recommander(self):
        dus = stats.dus(self.data["srs"], date.today(), self.data["completed"])
        action, item_id = stats.prochaine_action(
            self._ordre_item_ids(), self.data["completed"], dus)
        if action == "termine":
            messagebox.showinfo(self.tr("reco_title"), self.tr("reco_termine"))
            return
        self._charger_item(item_id)
        cle = "reco_revision" if action == "revision" else "reco_nouvelle"
        if action == "revision":
            self._revision_item = item_id
        self.feedback.configure(text=self.tr(cle), foreground=self.C["accent"])

    def _build_exo_tabs(self):
        for b in self.tab_buttons:
            b.destroy()
        self.tab_buttons = []
        n = exercice_count(self.current)
        if n <= 1:
            return
        items = lesson_items(self.current)
        for i in range(n):
            done = items[i] in self.data["completed"]
            txt = f"{'✓ ' if done else ''}Exercice {i + 1}"
            b = ttk.Button(self.exo_tabs, text=txt,
                           command=lambda idx=i: self._load_exercice(idx))
            b.pack(side=tk.LEFT, padx=(0, 4))
            self.tab_buttons.append(b)

    def _load_exercice(self, index):
        self._flush_code()          # idem entre deux exercices d'un projet
        self.exo_index = index
        exo = get_exercice(self.current, index)
        item_id = lesson_items(self.current)[index]
        self.enonce.configure(text=exo.get("prompt", "") if exercice_count(self.current) > 1 else "")
        mode = exo.get("mode") or self.current.get("mode")
        if mode == "debug":
            self.mode_label.configure(text=self.tr("mode_debug"))
        elif mode == "trous":
            self.mode_label.configure(text=self.tr("mode_trous"))
        else:
            self.mode_label.configure(text="")
        saved = self.data["code"].get(item_id)
        self.editor.set_text(saved if saved is not None else exo.get("starter", ""))
        self._hints = hints_for(self.current, exo if exercice_count(self.current) > 1 else None)
        self._hint_idx = 0
        self.feedback.configure(text="")
        self._clear_console()
        self._hide_banner()
        for i, b in enumerate(self.tab_buttons):
            b.state(["pressed"] if i == index else ["!pressed"])

    def _load_quiz(self, lesson):
        self.quiz_var.set(-1)
        self.quiz_question.configure(text=lesson.get("question", ""))
        for r in self.quiz_radios:
            r.destroy()
        self.quiz_radios = []
        for i, opt in enumerate(lesson.get("options", [])):
            r = ttk.Radiobutton(self.quiz_options, text=opt, value=i,
                                variable=self.quiz_var)
            r.pack(anchor="w", pady=3)
            self.quiz_radios.append(r)
        self.quiz_feedback.configure(text="")

    def _render_content(self, text):
        self.content.configure(state="normal")
        self.content.delete("1.0", tk.END)
        in_code = False
        for line in text.splitlines():
            if line.strip() == "```":
                in_code = not in_code
                continue
            if in_code:
                self.content.insert(tk.END, line + "\n", "code")
            elif line.startswith("## "):
                self.content.insert(tk.END, line[3:] + "\n", "h2")
            elif line.startswith("- "):
                self.content.insert(tk.END, "•  ", "bullet")
                self._insert_inline(line[2:] + "\n", "bullet")
            else:
                self._insert_inline(line + "\n", "body")
        self.content.configure(state="disabled")

    def _insert_inline(self, text, base_tag):
        for i, part in enumerate(text.split("`")):
            if i % 2 == 1:
                self.content.insert(tk.END, part, "inline")
            else:
                for j, seg in enumerate(part.split("**")):
                    tags = (base_tag, "bold") if j % 2 == 1 else base_tag
                    self.content.insert(tk.END, seg, tags)

    # -------------------------------------------------------------- console
    def _clear_console(self):
        self.console.configure(state="normal")
        self.console.delete("1.0", tk.END)
        self.console.configure(state="disabled")

    def _write(self, text, tag=None):
        self.console.configure(state="normal")
        self.console.insert(tk.END, text, tag or ())
        self.console.configure(state="disabled")
        self.console.see(tk.END)

    # ---------------------------------------------------------- bandeau succès
    def _show_banner(self, text, color):
        self.banner.configure(text=text, bg=color, fg="#ffffff")
        self._banner_anim(0)
        self.root.after(2600, self._hide_banner)

    def _banner_anim(self, etape):
        """Petit glissement d'entrée de la bannière (8 images)."""
        n = 8
        if etape > n:
            return
        rely = -0.06 + 0.06 * (etape / n)
        self.banner.place(relx=0.5, rely=rely, anchor="n", relwidth=0.7)
        self.root.after(16, lambda: self._banner_anim(etape + 1))

    def _hide_banner(self):
        self.banner.place_forget()

    # -------------------------------------------------------------- actions
    def _on_code_change(self):
        """Mémorise le code en cours et programme son écriture sur disque.

        On retient l'identifiant de l'exercice MAINTENANT : si l'apprenant
        change de leçon avant la fin du délai, le code partira bien dans
        l'exercice où il a été tapé, et pas dans le suivant.
        """
        if not self.current or self.current.get("type") == "quiz":
            return
        item_id = lesson_items(self.current)[self.exo_index]
        self._code_en_attente = (item_id, self.editor.get())
        if self._save_after_id is not None:
            self.root.after_cancel(self._save_after_id)
        self._save_after_id = self.root.after(DELAI_SAUVEGARDE_MS, self._flush_code)

    def _flush_code(self):
        """Écrit sans attendre le code en attente (idempotent).

        Appelé par la minuterie, mais aussi avant tout changement de leçon,
        avant d'exécuter ou de vérifier, et à la fermeture de l'application.
        """
        if self._save_after_id is not None:
            self.root.after_cancel(self._save_after_id)
            self._save_after_id = None
        if self._code_en_attente is None:
            return
        item_id, texte = self._code_en_attente
        self._code_en_attente = None
        prog.store_code(self.data, item_id, texte)

    def run(self):
        if not self.current or self.current.get("type") == "quiz":
            return
        from app.runner import inspecter, run_code
        self._flush_code()
        self._clear_console()
        self._avertir_zombies()
        result, ns = run_code(self.editor.get())
        if result.output:
            self._write(result.output)
        if result.error:
            self._write(self._message_erreur(result, result.error) + "\n", "err")
            conseil = errors.expliquer(result.error, self.lang)
            if conseil:
                self._write("💡 " + conseil + "\n", "hint")
        elif not result.output:
            self._write(self.tr("con_no_output") + "\n", "muted")
        if not result.error:
            variables = inspecter(ns)
            if variables:
                self._write("\n" + self.tr("con_vars") + "\n", "var")
                for nom, rep in variables:
                    self._write(f"{nom} = {rep}\n", "var")
        self.feedback.configure(text="")

    def check(self):
        if not self.current or self.current.get("type") == "quiz":
            return
        from app.runner import run_exercise
        self._flush_code()
        exo = get_exercice(self.current, self.exo_index)
        self._clear_console()
        self._avertir_zombies()
        mode = exo.get("mode") or self.current.get("mode")
        if mode == "trous" and "____" in self.editor.get():
            self._write(self.tr("trous_restants") + "\n", "muted")
            self.feedback.configure(text=self.tr("fb_fail"), foreground=self.C["err"])
            return
        result, success, message = run_exercise(
            self.editor.get(), check_code=exo.get("check"),
            expected_output=exo.get("expected_output"), stdin_lines=exo.get("stdin"))
        if result.output:
            self._write(result.output)
        item_id = lesson_items(self.current)[self.exo_index]
        if success:
            self._write("\n" + message + "\n", "ok")
            self.feedback.configure(text=self.tr("fb_ok"), foreground=self.C["ok"])
            self._echecs_session = 0
            self._mark_done(item_id)
            self._apres_reussite(item_id)
            self._show_banner(self.tr("banner_exo"), self.C["ok"])
        else:
            self._write("\n" + self._message_erreur(result, message) + "\n", "err")
            if exo.get("expected_output") is not None:
                self._afficher_diff(str(exo["expected_output"]).strip(),
                                    result.output.strip())
            conseil = errors.expliquer(message, self.lang)
            if conseil:
                self._write("💡 " + conseil + "\n", "hint")
            if self._revision_item == item_id:
                stats.planifier(self.data["srs"], item_id, date.today(), reussi=False)
                prog.save_progress(self.data)
                self._revision_item = None
                self._refresh_status()
            prog.enregistrer_echec(self.data, item_id)
            self._echecs_session += 1
            if self._echecs_session >= 2 and self._hints:
                self._write("\n" + self.tr("nudge_indice") + "\n", "hint")
            self.feedback.configure(text=self.tr("fb_fail"), foreground=self.C["err"])

    def _apres_reussite(self, item_id):
        """Enregistre l'activité du jour et planifie la prochaine révision."""
        today = date.today()
        prog.enregistrer_activite(self.data, today.isoformat())
        reussi_revision = (self._revision_item == item_id)
        stats.planifier(self.data["srs"], item_id, today, reussi=True)
        prog.save_progress(self.data)
        if reussi_revision:
            self._revision_item = None
        self._refresh_status()

    def _avertir_zombies(self):
        """Signale qu'une exécution précédente tourne encore en arrière-plan.

        Cela n'arrive que pour une boucle infinie qui attrape tout et refuse
        de s'arrêter. Mieux vaut le dire que laisser l'apprenant se demander
        pourquoi son application ralentit.
        """
        from app.runner import zombies_actifs
        restantes = zombies_actifs()
        if restantes:
            self._write(self.tr("con_zombie", n=restantes) + "\n", "muted")

    def _message_erreur(self, result, defaut):
        """Texte d'erreur à afficher, traduit quand nous le maîtrisons.

        Les messages venant de Python restent tels quels — apprendre à les
        lire fait partie du programme. Seuls les nôtres, comme l'arrêt pour
        cause de boucle infinie, suivent la langue de l'interface.
        """
        if result.timed_out:
            return self.tr("err_timeout")
        return defaut

    def _afficher_diff(self, attendu, obtenu):
        """Montre côte à côte la sortie attendue et la sortie obtenue."""
        la, lo = attendu.split("\n"), obtenu.split("\n")
        premiere = None
        for i in range(max(len(la), len(lo))):
            a = la[i] if i < len(la) else None
            o = lo[i] if i < len(lo) else None
            if a != o:
                premiere = i + 1
                break
        self._write("\n" + self.tr("con_compare") + "\n", "muted")
        self._write(self.tr("con_expected") + "\n", "muted")
        self._write((attendu or "(rien)") + "\n", "ok")
        self._write(self.tr("con_obtained") + "\n", "muted")
        self._write((obtenu or "(rien)") + "\n", "err")
        if premiere:
            self._write(self.tr("con_first_diff", n=premiere) + "\n", "muted")

    def check_quiz(self):
        if not self.current or self.current.get("type") != "quiz":
            return
        choix = self.quiz_var.get()
        if choix < 0:
            self.quiz_feedback.configure(text=self.tr("quiz_choose"),
                                         foreground=self.C["muted"])
            return
        if choix == self.current.get("answer"):
            self.quiz_feedback.configure(
                text=self.tr("quiz_good") + self.current.get("explanation", ""),
                foreground=self.C["ok"])
            nouveau = self.current["id"] not in self.data["completed"]
            self._mark_done(self.current["id"])
            if nouveau:
                prog.enregistrer_activite(self.data, date.today().isoformat())
                self._refresh_status()
            self._show_banner(self.tr("banner_quiz"), self.C["ok"])
        else:
            self.quiz_feedback.configure(text=self.tr("quiz_bad"),
                                         foreground=self.C["err"])

    def show_hint(self):
        if not self._hints:
            self._write(self.tr("con_no_hint") + "\n", "muted")
            return
        if self._hint_idx >= len(self._hints):
            self._write(self.tr("con_no_more_hint") + "\n", "muted")
            return
        self._write(self.tr("con_hint", i=self._hint_idx + 1, n=len(self._hints),
                            texte=self._hints[self._hint_idx]) + "\n", "hint")
        self._hint_idx += 1

    def show_solution(self):
        exo = get_exercice(self.current, self.exo_index)
        sol = exo.get("solution")
        if not sol:
            messagebox.showinfo(self.tr("dlg_solution_title"), self.tr("dlg_solution_none"))
            return
        if messagebox.askyesno(self.tr("dlg_solution_title"),
                               self.tr("dlg_solution_confirm")):
            self.editor.set_text(sol)
            self._on_code_change()

    def reset_code(self):
        exo = get_exercice(self.current, self.exo_index)
        self.editor.set_text(exo.get("starter", ""))
        self._on_code_change()
        self.feedback.configure(text="")
        self._clear_console()

    def _maj_syntaxe(self, err):
        if err is None:
            self.syntax_label.configure(text=self.tr("syntax_ok"),
                                        foreground=self.C["ok"])
        else:
            self.syntax_label.configure(
                text=self.tr("syntax_err", n=err.lineno or "?", msg=err.msg),
                foreground=self.C["err"])

    def _exporter_py(self):
        if not self.current or self.current.get("type") == "quiz":
            return
        chemin = filedialog.asksaveasfilename(
            defaultextension=".py", initialfile=f"{self.current['id']}.py",
            filetypes=[("Fichier Python", "*.py"), ("Tous les fichiers", "*.*")])
        if not chemin:
            return
        try:
            pathlib.Path(chemin).write_text(self.editor.get(), encoding="utf-8")
            self.feedback.configure(text=self.tr("fb_exported"), foreground=self.C["ok"])
        except Exception:
            messagebox.showinfo(self.tr("dlg_export_title"), self.tr("dlg_export_fail"))

    def _pas_a_pas(self):
        if not self.current or self.current.get("type") == "quiz":
            return
        from app.runner import tracer
        exo = get_exercice(self.current, self.exo_index)
        etapes, err = tracer(self.editor.get(), stdin_lines=exo.get("stdin"))
        vraies = [e for e in etapes if e.get("ligne") is not None]
        if not vraies:
            messagebox.showinfo(self.tr("dlg_step_title"),
                                err or self.tr("step_nothing"))
            return
        StepWindow(self.root, self, etapes, self.C, err)

    # --------------------------------------------------- progression / badges
    def _mark_done(self, item_id):
        if item_id in self.data["completed"]:
            return
        prog.mark_completed(self.data, item_id)
        self._populate_tree()
        if self.current and exercice_count(self.current) > 1:
            self._build_exo_tabs()
        self._refresh_status()
        self._check_level_badge(item_id.split("#")[0])

    def _check_level_badge(self, lesson_id):
        level = self.lesson_level[lesson_id]
        if all(lesson_done(lecon, self.data["completed"])
               for lecon in level["lessons"]):
            if prog.award_badge(self.data, level["id"]):
                self._populate_tree()
                self._refresh_badges()
                self._refresh_status()
                nom = LEVEL_BADGE_NAMES.get(level["id"], level["title"])
                nb = len(self.data["badges"])
                if nb == len(CURRICULUM):
                    msg = (f"Badge « {nom} » débloqué — et tu as terminé TOUS "
                           f"les parcours ! Bravo 👏")
                else:
                    msg = f"Parcours « {nom} » terminé ! Badge {nb}/{len(CURRICULUM)}."
                Celebration(self.root, msg, self.C,
                            on_cert=lambda lid=level["id"]: self._generer_certificat(lid))

    def _refresh_status(self):
        done = len(self.data["completed"])
        total = total_count()
        # ne compte que les items réellement existants
        valides = set()
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                valides.update(lesson_items(lesson))
        done = len([i for i in self.data["completed"] if i in valides])
        pct = round(100 * done / total) if total else 0
        self.progress.configure(value=done)
        today = date.today()
        s = stats.streak(self.data["historique"], today)
        auj = self.data["historique"].get(today.isoformat(), 0)
        obj = self.data.get("objectif_quotidien", 3)
        n_dus = len(stats.dus(self.data["srs"], today, set(self.data["completed"])))
        cible = "✓" if auj >= obj else f"{auj}/{obj}"
        niv = stats.niveau(stats.xp_total(self.data["completed"], self.data["badges"]))["niveau"]
        self.status.configure(text=self.tr(
            "status", niv=niv, done=done, total=total, pct=pct,
            b=len(self.data["badges"]), n=len(CURRICULUM), s=s, cible=cible, dus=n_dus))

    def _reset_progress(self):
        if messagebox.askyesno(self.tr("dlg_reset_title"), self.tr("dlg_reset_msg")):
            theme = self.theme_name
            langue = self.lang
            prog.reset_progress()
            self.data = prog.load_progress()
            self.data["theme"] = theme
            self.data["langue"] = langue
            self.data["vu_accueil"] = True
            prog.save_progress(self.data)
            self._populate_tree()
            self._refresh_badges()
            self._refresh_status()
            self._select_first_incomplete()

    # ------------------------------------------------------------- fenêtres
    def _show_welcome(self):
        prog.marquer_accueil_vu(self.data)
        C = self.C
        win = tk.Toplevel(self.root)
        win.title(self.tr("wel_title"))
        win.configure(bg=C["panel"])
        win.geometry("520x380")
        tk.Label(win, text=self.tr("wel_title"), bg=C["panel"], fg=C["accent"],
                 font=self.title_font).pack(pady=(20, 8))
        tk.Label(win, text=self.tr("wel_body"), bg=C["panel"], fg=C["fg"], justify="left",
                 wraplength=470).pack(padx=20)
        tk.Button(win, text=self.tr("wel_start"), command=win.destroy).pack(pady=14)

    def _show_glossaire(self):
        C = self.C
        win = tk.Toplevel(self.root)
        win.title(self.tr("tb_glossaire").strip("📖 "))
        win.configure(bg=C["panel"])
        win.geometry("560x520")
        tk.Label(win, text=self.tr("gl_title"), bg=C["panel"], fg=C["accent"],
                 font=self.title_font).pack(pady=(12, 6))
        outils = ttk.Frame(win, style="Panel.TFrame")
        outils.pack(pady=(0, 6))
        ttk.Button(outils, text=self.tr("gl_cards"),
                   command=self._ouvrir_flashcards).pack(side=tk.LEFT, padx=4)
        ttk.Button(outils, text=self.tr("gl_cheatsheet"),
                   command=self._ouvrir_antiseche).pack(side=tk.LEFT, padx=4)
        var = tk.StringVar()
        entry = tk.Entry(win, textvariable=var, bg=C["editor"], fg=C["fg"],
                         insertbackground=C["fg"], relief="flat")
        entry.pack(fill=tk.X, padx=14, pady=(0, 8))
        txt = tk.Text(win, wrap="word", bg=C["bg"], fg=C["fg"], relief="flat",
                      padx=10, pady=8, font=self.body)
        txt.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 14))
        txt.tag_configure("terme", foreground=C["heading"],
                          font=(self.body.cget("family"), 11, "bold"), spacing1=8)

        def remplir(*_):
            f = var.get().strip().lower()
            txt.configure(state="normal")
            txt.delete("1.0", tk.END)
            for terme, definition in GLOSSAIRE:
                if not f or f in terme.lower() or f in definition.lower():
                    txt.insert(tk.END, terme + "\n", "terme")
                    txt.insert(tk.END, definition + "\n")
            txt.configure(state="disabled")
        var.trace_add("write", remplir)
        remplir()

    def _ouvrir_antiseche(self):
        from content.cheatsheet import CHEATSHEET
        html = stats.cheatsheet_html(self.tr("cheat_title"), CHEATSHEET)
        try:
            fichier = prog.DATA_DIR / "antiseche.html"
            prog.DATA_DIR.mkdir(parents=True, exist_ok=True)
            fichier.write_text(html, encoding="utf-8")
            webbrowser.open(fichier.as_uri())
        except Exception:
            messagebox.showinfo(self.tr("cheat_title"), self.tr("cheat_fail"))

    def _ouvrir_flashcards(self):
        cartes = list(GLOSSAIRE)
        if not cartes:
            return
        FlashcardWindow(self.root, self, cartes, self.C)

    def _revision(self):
        today = date.today()
        completed = set(self.data["completed"])
        # ne révise que des exercices (pas les quiz)
        ids_exercices = set()
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                if lesson.get("type") != "quiz":
                    ids_exercices.update(lesson_items(lesson))
        dus = [i for i in stats.dus(self.data["srs"], today, completed)
               if i in ids_exercices]
        if dus:
            self._charger_item(random.choice(dus))
            self.feedback.configure(text=self.tr("fb_revision_due", n=len(dus)),
                                    foreground=self.C["accent"])
            return
        faits = [i for i in completed if i in ids_exercices]
        if not faits:
            messagebox.showinfo(self.tr("dlg_revision_title"),
                                self.tr("dlg_revision_none"))
            return
        self._charger_item(random.choice(faits))
        self._revision_item = None
        self.feedback.configure(text=self.tr("fb_revision_random"),
                                foreground=self.C["muted"])

    def _charger_item(self, item_id):
        lid = item_id.split("#")[0]
        lesson = find_lesson(lid)
        if lesson is None:
            return
        for node, lecon in self.item_to_lesson.items():
            if lecon["id"] == lid:
                if self.tree.selection() != (node,):
                    self._ignore_next_select = True
                    self.tree.selection_set(node)
                    self.tree.see(node)
                break
        self._load_lesson(lesson)
        if "#" in item_id:
            self._load_exercice(int(item_id.split("#")[1]))
        self._revision_item = item_id

    def _exporter_progression(self):
        chemin = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON", "*.json")],
            initialfile="python-learn-progression.json")
        if not chemin:
            return
        try:
            pathlib.Path(chemin).write_text(prog.exporter_json(self.data),
                                            encoding="utf-8")
            messagebox.showinfo(self.tr("st_title").strip("📊 "),
                                self.tr("dlg_export_ok"))
        except Exception:
            messagebox.showinfo(self.tr("dlg_export_title"), self.tr("dlg_export_fail"))

    def _importer_progression(self, win=None):
        chemin = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if not chemin:
            return
        try:
            texte = pathlib.Path(chemin).read_text(encoding="utf-8")
            nouveau = prog.importer_json(texte)
        except Exception:
            messagebox.showinfo(self.tr("st_title").strip("📊 "),
                                self.tr("dlg_import_err"))
            return
        self.data = nouveau
        self.theme_name = self.data.get("theme", self.theme_name)
        if self.theme_name not in THEMES:
            self.theme_name = "dark"
        self.C = THEMES[self.theme_name]
        self.lang = self.data.get("langue", self.lang)
        if self.lang not in LANGUES:
            self.lang = "fr"
        self.tr.set(self.lang)
        prog.save_progress(self.data)
        self.apply_theme()
        self._apply_language()
        self._populate_tree()
        self._refresh_badges()
        self._refresh_status()
        self._select_first_incomplete()
        messagebox.showinfo(self.tr("st_title").strip("📊 "), self.tr("dlg_import_ok"))
        if win is not None:
            win.destroy()

    def _generer_certificat(self, level_id):
        nom = self.data.get("nom") or ""
        if not nom:
            nom = simpledialog.askstring(
                self.tr("dlg_cert_title"), self.tr("dlg_cert_prompt"),
                parent=self.root) or self.tr("dlg_cert_default")
            prog.set_nom(self.data, nom)
        parcours = LEVEL_BADGE_NAMES.get(level_id, level_id)
        html = stats.certificat_html(nom, parcours, date.today().strftime("%d/%m/%Y"))
        dossier = prog.DATA_DIR / "certificats"
        try:
            dossier.mkdir(parents=True, exist_ok=True)
            fichier = dossier / f"certificat_{level_id}.html"
            fichier.write_text(html, encoding="utf-8")
            webbrowser.open(fichier.as_uri())
        except Exception:
            messagebox.showinfo(self.tr("dlg_cert_title"), self.tr("dlg_cert_fail"))

    def _show_stats(self):
        C = self.C
        today = date.today()
        win = tk.Toplevel(self.root)
        win.configure(bg=C["bg"])
        win.geometry("520x600")
        win.title(self.tr("st_title").strip("📊 "))
        tk.Label(win, text=self.tr("st_title"), bg=C["bg"], fg=C["accent"],
                 font=self.title_font).pack(pady=(14, 8))

        s = stats.streak(self.data["historique"], today)
        record = stats.meilleur_streak(self.data["historique"])
        total_faits = len(self.data["completed"])
        auj = self.data["historique"].get(today.isoformat(), 0)
        obj = self.data.get("objectif_quotidien", 3)
        n_dus = len(stats.dus(self.data["srs"], today, set(self.data["completed"])))
        xp = stats.xp_total(self.data["completed"], self.data["badges"])
        niv = stats.niveau(xp)
        hebdo = stats.cette_semaine(self.data["historique"], today)
        obj_h = self.data.get("objectif_hebdo", 15)
        for t in [self.tr("st_niveau", niv=niv["niveau"], dans=niv["dans_niveau"],
                          pour=niv["pour_suivant"]),
                  self.tr("st_streak", n=s),
                  self.tr("st_record", n=record),
                  self.tr("st_total", n=total_faits),
                  self.tr("st_today", auj=auj, obj=obj),
                  self.tr("st_hebdo", n=hebdo, obj=obj_h),
                  self.tr("st_due", n=n_dus)]:
            tk.Label(win, text=t, bg=C["bg"], fg=C["fg"], anchor="w").pack(
                fill=tk.X, padx=28, pady=2)

        nivbar = ttk.Progressbar(win, style="Niv.Horizontal.TProgressbar",
                                 maximum=niv["pour_suivant"], length=320)
        nivbar.pack(pady=(2, 8))
        nivbar["value"] = niv["dans_niveau"]

        objrow = tk.Frame(win, bg=C["bg"])
        objrow.pack(pady=8)
        tk.Label(objrow, text=self.tr("st_objective"), bg=C["bg"],
                 fg=C["muted"]).pack(side=tk.LEFT)
        obj_var = tk.IntVar(value=obj)
        tk.Label(objrow, textvariable=obj_var, bg=C["bg"], fg=C["fg"],
                 width=3).pack(side=tk.LEFT, padx=6)

        def maj(delta):
            n = max(1, obj_var.get() + delta)
            obj_var.set(n)
            prog.set_objectif(self.data, n)
            self._refresh_status()
        tk.Button(objrow, text="–", command=lambda: maj(-1)).pack(side=tk.LEFT)
        tk.Button(objrow, text="+", command=lambda: maj(1)).pack(side=tk.LEFT, padx=4)

        hrow = tk.Frame(win, bg=C["bg"])
        hrow.pack(pady=(0, 4))
        tk.Label(hrow, text=self.tr("st_hebdo_label"), bg=C["bg"],
                 fg=C["muted"]).pack(side=tk.LEFT)
        objh_var = tk.IntVar(value=obj_h)
        tk.Label(hrow, textvariable=objh_var, bg=C["bg"], fg=C["fg"],
                 width=3).pack(side=tk.LEFT, padx=6)

        def maj_h(delta):
            n = max(1, objh_var.get() + delta)
            objh_var.set(n)
            prog.set_objectif_hebdo(self.data, n)
        tk.Button(hrow, text="–", command=lambda: maj_h(-1)).pack(side=tk.LEFT)
        tk.Button(hrow, text="+", command=lambda: maj_h(1)).pack(side=tk.LEFT, padx=4)

        iorow = tk.Frame(win, bg=C["bg"])
        iorow.pack(pady=(2, 6))
        ttk.Button(iorow, text=self.tr("st_export"),
                   command=self._exporter_progression).pack(side=tk.LEFT, padx=4)
        ttk.Button(iorow, text=self.tr("st_import"),
                   command=lambda: self._importer_progression(win)).pack(side=tk.LEFT, padx=4)

        tk.Label(win, text=self.tr("st_7days"), bg=C["bg"], fg=C["muted"]).pack(pady=(8, 0))
        cv = tk.Canvas(win, width=470, height=150, bg=C["panel"], highlightthickness=0)
        cv.pack(pady=6)
        donnees = stats.sept_jours(self.data["historique"], today)
        maxv = max([v for _, v in donnees] + [1])
        bw, gap, x = 50, 16, 16
        for label, v in donnees:
            hh = int(110 * v / maxv) if v else 0
            cv.create_rectangle(x, 124 - hh, x + bw, 124, fill=C["accent"], outline="")
            cv.create_text(x + bw / 2, 138, text=label, fill=C["muted"], font=("", 8))
            if v:
                cv.create_text(x + bw / 2, 116 - hh, text=str(v), fill=C["fg"], font=("", 8))
            x += bw + gap

        if self.data["badges"]:
            tk.Label(win, text=self.tr("st_certs"), bg=C["bg"],
                     fg=C["muted"]).pack(pady=(8, 2))
            cert = tk.Frame(win, bg=C["bg"])
            cert.pack(fill=tk.X, padx=28)
            for lid in self.data["badges"]:
                nom = LEVEL_BADGE_NAMES.get(lid, lid)
                tk.Button(cert, text=f"🎓 {nom}", anchor="w",
                          command=lambda parcours=lid:
                              self._generer_certificat(parcours)).pack(
                    fill=tk.X, pady=2)

    def _show_sandbox(self):
        """Éditeur libre, sans exercice ni vérification, pour expérimenter."""
        C = self.C
        win = tk.Toplevel(self.root)
        win.title(self.tr("sb_title"))
        win.configure(bg=C["bg"])
        win.geometry("720x600")

        tk.Label(win, text=self.tr("sb_intro"),
                 bg=C["bg"], fg=C["muted"], anchor="w").pack(fill=tk.X, padx=10, pady=(8, 2))

        ed = CodeEditor(win, self.code_font)
        ed.pack(fill=tk.BOTH, expand=True, padx=10)
        ed.apply_theme(C)
        ed.set_text(self.tr("sb_starter"))

        con = tk.Text(win, height=8, wrap="word", relief="flat", font=self.code_font,
                      bg=C["console"], fg=C["fg"], padx=10, pady=8, state="disabled")
        con.tag_configure("err", foreground=C["err"])
        con.tag_configure("var", foreground=C["builtin"])
        con.tag_configure("hint", foreground=C["accent"])
        con.tag_configure("muted", foreground=C["muted"])

        def lancer():
            from app.runner import inspecter, run_code
            con.configure(state="normal")
            con.delete("1.0", tk.END)
            result, ns = run_code(ed.get(), safe=True)   # bac à sable durci
            if result.output:
                con.insert(tk.END, result.output)
            if result.error:
                con.insert(tk.END,
                           self._message_erreur(result, result.error) + "\n",
                           "err")
                conseil = errors.expliquer(result.error, self.lang)
                if conseil:
                    con.insert(tk.END, "💡 " + conseil + "\n", "hint")
            elif not result.output:
                con.insert(tk.END, self.tr("con_no_output") + "\n", "muted")
            if not result.error:
                variables = inspecter(ns)
                if variables:
                    con.insert(tk.END, "\n" + self.tr("con_vars") + "\n", "var")
                    for nom, rep in variables:
                        con.insert(tk.END, f"{nom} = {rep}\n", "var")
            con.configure(state="disabled")
            con.see(tk.END)

        barre = ttk.Frame(win)
        barre.pack(fill=tk.X, padx=10, pady=6)
        ttk.Button(barre, text=self.tr("sb_run"), command=lancer).pack(side=tk.LEFT)
        ttk.Button(barre, text=self.tr("sb_clear"),
                   command=lambda: ed.set_text("")).pack(side=tk.LEFT, padx=6)
        con.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        win.bind("<Control-Return>", lambda e: lancer())
        ed.focus_editor()


def _ouvrir_dossier(chemin):
    """Ouvre un dossier dans l'explorateur de fichiers du système.

    Renvoie False si aucun explorateur n'a pu être lancé — auquel cas
    l'appelant se rabat sur l'affichage du chemin.
    """
    import subprocess
    try:
        if sys.platform == "win32":
            os.startfile(str(chemin))                      # noqa: S606
        elif sys.platform == "darwin":
            subprocess.run(["open", str(chemin)], check=True)
        else:
            subprocess.run(["xdg-open", str(chemin)], check=True)
        return True
    except Exception:
        return False


def _splash(root):
    """Petit écran d'accueil (avec fondu) affiché le temps du démarrage."""
    C = THEMES["dark"]
    sp = tk.Toplevel(root)
    sp.overrideredirect(True)
    w, h = 440, 260
    sw, sh = sp.winfo_screenwidth(), sp.winfo_screenheight()
    sp.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    sp.configure(bg=C["panel"])
    # liseré d'accent en haut
    tk.Frame(sp, bg=C["accent"], height=5).pack(fill=tk.X, side=tk.TOP)
    tk.Label(sp, text="🐍", bg=C["panel"], font=("", 60)).pack(pady=(34, 2))
    tk.Label(sp, text="PythonLearn", bg=C["panel"], fg=C["accent"],
             font=("", 25, "bold")).pack()
    tk.Label(sp, text="Apprendre Python, pas à pas", bg=C["panel"],
             fg=C["muted"]).pack(pady=(2, 0))
    try:
        sp.attributes("-topmost", True)
        sp.attributes("-alpha", 0.0)
    except tk.TclError:
        pass

    def _fondu(a=0.0):
        try:
            sp.attributes("-alpha", min(1.0, a))
        except tk.TclError:
            return
        if a < 1.0:
            sp.after(20, lambda: _fondu(a + 0.12))
    _fondu()
    return sp


def launch():
    # Les leçons ajoutées par l'utilisateur doivent être connues AVANT que
    # l'interface ne construise sa liste de parcours.
    _, soucis_packs = ajouter_packs()

    root = tk.Tk()
    root.withdraw()
    if ICON_B64:
        try:
            icon = tk.PhotoImage(data=ICON_B64)
            root.iconphoto(True, icon)
            root._icon_ref = icon
        except Exception:
            pass
    sp = _splash(root)
    root.update()
    app = PythonLearnApp(root)
    app.soucis_packs = soucis_packs
    root.protocol("WM_DELETE_WINDOW", app.quitter)
    if soucis_packs:
        root.after(900, app._avertir_packs)

    def _demarrer():
        def _sortie(a=1.0):
            try:
                sp.attributes("-alpha", max(0.0, a))
            except tk.TclError:
                a = 0
            if a > 0:
                sp.after(18, lambda: _sortie(a - 0.15))
            else:
                sp.destroy()
                root.deiconify()
        _sortie()
    root.after(1100, _demarrer)
    root.mainloop()
