"""
Interface graphique (Tkinter / ttk) de PythonLearn.

Fonctionnalités : parcours en arborescence, éditeur de code avec
exécution réelle et vérification automatique, suivi de progression,
thème clair/sombre commutable, badges de réussite par niveau.
"""

import tkinter as tk
from tkinter import ttk, font, messagebox

from content import CURRICULUM, total_count
from app import progress as prog
from app.runner import run_exercise, run_code

try:
    from app.icon import ICON_B64
except Exception:
    ICON_B64 = None


# Deux palettes de couleurs
THEMES = {
    "dark": {
        "bg": "#1e1f26", "panel": "#272935", "editor": "#15161c",
        "console": "#0e0f14", "fg": "#e6e6e6", "accent": "#4d8bf0",
        "ok": "#52c97a", "err": "#f0635c", "muted": "#9aa0b4",
        "heading": "#7fb0ff", "code": "#ffd479", "code_bg": "#15161c",
        "sel_fg": "#ffffff",
    },
    "light": {
        "bg": "#f4f5f7", "panel": "#e7e9ee", "editor": "#ffffff",
        "console": "#eef0f4", "fg": "#1c1d22", "accent": "#2f6fe0",
        "ok": "#1f9d57", "err": "#d23b34", "muted": "#5a6172",
        "heading": "#1e4fa3", "code": "#9a6b00", "code_bg": "#eceef2",
        "sel_fg": "#ffffff",
    },
}

LEVEL_BADGE_NAMES = {
    "debutant": "Débutant",
    "intermediaire": "Intermédiaire",
    "avance": "Avancé",
    "expert": "Expert",
}


class PythonLearnApp:
    def __init__(self, root):
        self.root = root
        self.data = prog.load_progress()
        self.theme_name = self.data.get("theme", "dark")
        self.C = THEMES.get(self.theme_name, THEMES["dark"])
        self.current = None

        # carte leçon -> niveau
        self.lesson_level = {}
        for level in CURRICULUM:
            for lesson in level["lessons"]:
                self.lesson_level[lesson["id"]] = level

        root.title("PythonLearn — apprendre Python pas à pas")
        root.geometry("1120x760")
        root.minsize(960, 640)

        self._init_fonts()
        self._build_layout()
        self.apply_theme()
        self._populate_tree()
        self._refresh_badges()
        self._refresh_status()
        self._select_first_incomplete()

    # ------------------------------------------------------------- polices
    def _init_fonts(self):
        self.mono = font.nametofont("TkFixedFont").copy()
        self.mono.configure(size=11)
        self.body = font.nametofont("TkDefaultFont").copy()
        self.body.configure(size=11)
        self.title_font = self.body.copy()
        self.title_font.configure(size=16, weight="bold")
        self.h2_font = (self.body.cget("family"), 13, "bold")

    # ---------------------------------------------------------------- layout
    def _build_layout(self):
        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass

        outer = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        outer.pack(fill=tk.BOTH, expand=True, padx=8, pady=(8, 0))

        # --- barre latérale ---
        side = ttk.Frame(outer, style="Panel.TFrame", width=300)
        outer.add(side, weight=0)
        self.side = side

        self.side_header = tk.Label(side, text="  Parcours",
                                    font=self.title_font, anchor="w")
        self.side_header.pack(fill=tk.X, pady=(10, 4), padx=4)

        tree_wrap = ttk.Frame(side, style="Panel.TFrame")
        tree_wrap.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)
        self.tree = ttk.Treeview(tree_wrap, show="tree", selectmode="browse")
        sb = ttk.Scrollbar(tree_wrap, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        # bandeau des badges
        self.badge_title = tk.Label(side, text="  Badges", anchor="w",
                                    font=(self.body.cget("family"), 10, "bold"))
        self.badge_title.pack(fill=tk.X, padx=4, pady=(4, 0))
        self.badge_bar = tk.Frame(side)
        self.badge_bar.pack(fill=tk.X, padx=6, pady=(2, 6))
        self.badge_labels = {}
        for level in CURRICULUM:
            lbl = tk.Label(self.badge_bar, text="🔒", font=(self.body.cget("family"), 9))
            lbl.pack(side=tk.LEFT, expand=True)
            self.badge_labels[level["id"]] = lbl

        # boutons bas de barre
        self.theme_btn = ttk.Button(side, text="", command=self.toggle_theme)
        self.theme_btn.pack(fill=tk.X, padx=6, pady=(0, 4))
        ttk.Button(side, text="Réinitialiser ma progression",
                   command=self._reset_progress).pack(fill=tk.X, padx=6, pady=(0, 8))

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
                               font=self.body, padx=8, pady=8, height=12,
                               cursor="arrow")
        csb = ttk.Scrollbar(content_wrap, orient="vertical", command=self.content.yview)
        self.content.configure(yscrollcommand=csb.set)
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        csb.pack(side=tk.RIGHT, fill=tk.Y)
        self.content.configure(state="disabled")

        bottom = ttk.Frame(main)
        main.add(bottom, weight=4)
        ttk.Label(bottom, text="Éditeur de code", style="Muted.TLabel").pack(
            anchor="w", padx=12, pady=(6, 2))

        ed_wrap = ttk.Frame(bottom)
        ed_wrap.pack(fill=tk.BOTH, expand=True, padx=12)
        self.editor = tk.Text(ed_wrap, wrap="none", relief="flat", font=self.mono,
                              padx=10, pady=8, undo=True)
        esb = ttk.Scrollbar(ed_wrap, orient="vertical", command=self.editor.yview)
        self.editor.configure(yscrollcommand=esb.set)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        esb.pack(side=tk.RIGHT, fill=tk.Y)
        self.editor.bind("<Tab>", self._on_tab)
        self.editor.bind("<Return>", self._on_return)

        btn_row = ttk.Frame(bottom)
        btn_row.pack(fill=tk.X, padx=12, pady=8)
        ttk.Button(btn_row, text="▶  Exécuter (Ctrl+Entrée)",
                   command=self.run).pack(side=tk.LEFT)
        ttk.Button(btn_row, text="✓  Vérifier", command=self.check).pack(
            side=tk.LEFT, padx=6)
        ttk.Button(btn_row, text="Solution", command=self.show_solution).pack(
            side=tk.LEFT)
        ttk.Button(btn_row, text="Réinitialiser le code",
                   command=self.reset_code).pack(side=tk.LEFT, padx=6)
        self.feedback = ttk.Label(btn_row, text="", style="TLabel")
        self.feedback.pack(side=tk.LEFT, padx=10)

        con_wrap = ttk.Frame(bottom)
        con_wrap.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 8))
        self.console = tk.Text(con_wrap, wrap="word", relief="flat", font=self.mono,
                              height=7, padx=10, pady=8, state="disabled")
        consb = ttk.Scrollbar(con_wrap, orient="vertical", command=self.console.yview)
        self.console.configure(yscrollcommand=consb.set)
        self.console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        consb.pack(side=tk.RIGHT, fill=tk.Y)

        self.status = ttk.Label(self.root, text="", style="Status.TLabel",
                                anchor="w", padding=8)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

        self.root.bind("<Control-Return>", lambda e: self.run())

    # ----------------------------------------------------------------- thème
    def apply_theme(self):
        C = self.C
        self.root.configure(bg=C["bg"])

        self.style.configure("TFrame", background=C["bg"])
        self.style.configure("Panel.TFrame", background=C["panel"])
        self.style.configure("TLabel", background=C["bg"], foreground=C["fg"])
        self.style.configure("Muted.TLabel", background=C["bg"], foreground=C["muted"])
        self.style.configure("Title.TLabel", background=C["bg"], foreground=C["fg"],
                             font=self.title_font)
        self.style.configure("Status.TLabel", background=C["panel"], foreground=C["muted"])
        self.style.configure("TButton", font=self.body)
        self.style.configure("Treeview", background=C["panel"],
                             fieldbackground=C["panel"], foreground=C["fg"],
                             rowheight=26, borderwidth=0)
        self.style.map("Treeview", background=[("selected", C["accent"])],
                       foreground=[("selected", C["sel_fg"])])

        # widgets texte classiques
        self.content.configure(bg=C["bg"], fg=C["fg"], insertbackground=C["fg"])
        self.editor.configure(bg=C["editor"], fg=C["fg"], insertbackground=C["fg"])
        self.console.configure(bg=C["console"], fg=C["fg"], insertbackground=C["fg"])

        # bandeaux latéraux
        self.side_header.configure(bg=C["panel"], fg=C["accent"])
        self.badge_title.configure(bg=C["panel"], fg=C["muted"])
        self.badge_bar.configure(bg=C["panel"])

        self._configure_text_tags()
        self.console.tag_configure("ok", foreground=C["ok"])
        self.console.tag_configure("err", foreground=C["err"])
        self.console.tag_configure("muted", foreground=C["muted"])
        self.tree.tag_configure("done", foreground=C["ok"])
        self.tree.tag_configure("level", foreground=C["heading"])

        self.theme_btn.configure(
            text="🌙  Passer en sombre" if self.theme_name == "light"
            else "☀  Passer en clair")
        self._refresh_badges()

    def toggle_theme(self):
        self.theme_name = "light" if self.theme_name == "dark" else "dark"
        self.C = THEMES[self.theme_name]
        prog.set_theme(self.data, self.theme_name)
        self.apply_theme()

    def _configure_text_tags(self):
        C = self.C
        self.content.tag_configure("h2", foreground=C["heading"], font=self.h2_font,
                                   spacing1=8, spacing3=4)
        self.content.tag_configure("body", foreground=C["fg"], spacing3=4, font=self.body)
        self.content.tag_configure("code", foreground=C["code"], background=C["code_bg"],
                                   font=self.mono, lmargin1=16, lmargin2=16,
                                   spacing1=2, spacing3=2)
        self.content.tag_configure("inline", foreground=C["code"], font=self.mono)
        self.content.tag_configure("bullet", foreground=C["fg"], lmargin1=16, lmargin2=30)

    # ---------------------------------------------------------------- arbre
    def _populate_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.item_to_lesson = {}
        for level in CURRICULUM:
            badge = " 🏅" if level["id"] in self.data["badges"] else ""
            parent = self.tree.insert("", "end", text="  " + level["title"] + badge,
                                      open=True, tags=("level",))
            for lesson in level["lessons"]:
                done = lesson["id"] in self.data["completed"]
                label = ("  ✓ " if done else "  • ") + lesson["title"]
                node = self.tree.insert(parent, "end", text=label,
                                        tags=("done",) if done else ())
                self.item_to_lesson[node] = lesson

    def _refresh_badges(self):
        C = self.C
        for level in CURRICULUM:
            lbl = self.badge_labels[level["id"]]
            earned = level["id"] in self.data["badges"]
            lbl.configure(
                text="🏅" if earned else "🔒",
                bg=C["panel"],
                fg=C["accent"] if earned else C["muted"],
            )

    def _select_first_incomplete(self):
        for node, lesson in self.item_to_lesson.items():
            if lesson["id"] not in self.data["completed"]:
                self.tree.selection_set(node)
                self.tree.see(node)
                return
        if self.item_to_lesson:
            self.tree.selection_set(next(iter(self.item_to_lesson)))

    def _on_select(self, _event):
        sel = self.tree.selection()
        if not sel:
            return
        lesson = self.item_to_lesson.get(sel[0])
        if lesson:
            self._load_lesson(lesson)

    def _load_lesson(self, lesson):
        self.current = lesson
        self.lesson_title.configure(text=lesson["title"])
        self._render_content(lesson.get("content", ""))
        saved = self.data["code"].get(lesson["id"])
        code = saved if saved is not None else lesson.get("starter", "")
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", code)
        self.feedback.configure(text="")
        self._clear_console()

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
            self.content.insert(tk.END, part, "inline" if i % 2 else base_tag)

    # -------------------------------------------------------------- console
    def _clear_console(self):
        self.console.configure(state="normal")
        self.console.delete("1.0", tk.END)
        self.console.configure(state="disabled")

    def _write_console(self, text, tag=None):
        self.console.configure(state="normal")
        self.console.insert(tk.END, text, tag or ())
        self.console.configure(state="disabled")
        self.console.see(tk.END)

    # -------------------------------------------------------------- actions
    def _current_code(self):
        return self.editor.get("1.0", "end-1c")

    def run(self):
        if not self.current:
            return
        code = self._current_code()
        prog.store_code(self.data, self.current["id"], code)
        self._clear_console()
        result, _ = run_code(code)
        if result.output:
            self._write_console(result.output)
        if result.error:
            self._write_console(result.error + "\n", "err")
        elif not result.output:
            self._write_console("(aucune sortie)\n", "muted")
        self.feedback.configure(text="")

    def check(self):
        if not self.current:
            return
        code = self._current_code()
        prog.store_code(self.data, self.current["id"], code)
        self._clear_console()
        result, success, message = run_exercise(
            code, check_code=self.current.get("check"),
            expected_output=self.current.get("expected_output"),
            stdin_lines=self.current.get("stdin"))
        if result.output:
            self._write_console(result.output)
        if success:
            self._write_console("\n" + message + "\n", "ok")
            self.feedback.configure(text="Réussi ✓", foreground=self.C["ok"])
            self._mark_done(self.current["id"])
        else:
            self._write_console("\n" + message + "\n", "err")
            self.feedback.configure(text="Pas encore…", foreground=self.C["err"])

    def show_solution(self):
        if not self.current:
            return
        sol = self.current.get("solution")
        if not sol:
            messagebox.showinfo("Solution", "Pas de solution prédéfinie ici.")
            return
        if messagebox.askyesno("Afficher la solution",
                               "Remplacer ton code par la solution proposée ?"):
            self.editor.delete("1.0", tk.END)
            self.editor.insert("1.0", sol)

    def reset_code(self):
        if not self.current:
            return
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", self.current.get("starter", ""))
        self.feedback.configure(text="")
        self._clear_console()

    # --------------------------------------------------- progression/badges
    def _mark_done(self, lesson_id):
        was_new = lesson_id not in self.data["completed"]
        prog.mark_completed(self.data, lesson_id)
        if not was_new:
            return
        for node, lesson in self.item_to_lesson.items():
            if lesson["id"] == lesson_id:
                self.tree.item(node, text="  ✓ " + lesson["title"], tags=("done",))
                break
        self._refresh_status()
        self._check_level_badge(lesson_id)

    def _check_level_badge(self, lesson_id):
        level = self.lesson_level[lesson_id]
        ids = [l["id"] for l in level["lessons"]]
        if all(i in self.data["completed"] for i in ids):
            if prog.award_badge(self.data, level["id"]):
                self._populate_tree()
                self._refresh_badges()
                self._refresh_status()
                nb = len(self.data["badges"])
                nom = LEVEL_BADGE_NAMES.get(level["id"], level["title"])
                if nb == len(CURRICULUM):
                    messagebox.showinfo(
                        "🏆 Félicitations !",
                        f"Badge « {nom} » débloqué — et tu as terminé TOUS "
                        f"les niveaux !\n\nTu as parcouru Python de débutant "
                        f"à expert. Bravo 👏")
                else:
                    messagebox.showinfo(
                        "🏅 Badge débloqué !",
                        f"Tu as terminé le niveau « {nom} » !\n"
                        f"Badge obtenu : {nb}/{len(CURRICULUM)}.")

    def _refresh_status(self):
        done = len(self.data["completed"])
        total = total_count()
        pct = round(100 * done / total) if total else 0
        badges = len(self.data["badges"])
        self.status.configure(
            text=f"Progression : {done} / {total} leçons  ·  {pct} %"
                 f"   |   Badges : {badges} / {len(CURRICULUM)}")

    def _reset_progress(self):
        if messagebox.askyesno("Réinitialiser",
                               "Effacer toute ta progression et le code sauvegardé ?"):
            prog.reset_progress()
            self.data = {"completed": [], "code": {}, "badges": [],
                         "theme": self.theme_name}
            prog.save_progress(self.data)
            self._populate_tree()
            self._refresh_badges()
            self._refresh_status()
            self._select_first_incomplete()

    # ------------------------------------------------------------- éditeur
    def _on_tab(self, _event):
        self.editor.insert(tk.INSERT, "    ")
        return "break"

    def _on_return(self, _event):
        line = self.editor.get("insert linestart", "insert")
        indent = len(line) - len(line.lstrip(" "))
        if line.rstrip().endswith(":"):
            indent += 4
        self.editor.insert(tk.INSERT, "\n" + " " * indent)
        return "break"


def launch():
    root = tk.Tk()
    if ICON_B64:
        try:
            icon = tk.PhotoImage(data=ICON_B64)
            root.iconphoto(True, icon)
            root._icon_ref = icon  # conserver une référence
        except Exception:
            pass
    PythonLearnApp(root)
    root.mainloop()
