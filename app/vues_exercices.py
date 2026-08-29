"""
Les deux vues des exercices « prédis la sortie » et « remets dans l'ordre ».

Chaque vue construit son propre cadre, sait charger une leçon et se
vérifier. Elle reçoit l'application pour trois choses seulement : traduire
(`app.tr`), enregistrer la réussite (`app.valider_item`) et connaître le
thème courant. Le reste — le curriculum, la progression — ne la regarde pas.
"""

import tkinter as tk
from tkinter import ttk

from app import exercices


class _VueBase:
    """Ce que les deux vues ont en commun : un cadre et le suivi du thème."""

    def __init__(self, parent, app):
        self.app = app
        self.lecon = None
        self.frame = ttk.Frame(parent)
        self._zones_texte = []      # widgets tk purs à recolorer au changement

    def tr(self, cle, **kw):
        return self.app.tr(cle, **kw)

    def appliquer_theme(self, C):
        for widget, role in self._zones_texte:
            fond = C["editor"] if role == "saisie" else C["console"]
            widget.configure(bg=fond, fg=C["fg"],
                             selectbackground=C["accent"],
                             selectforeground=C["sel_fg"])
            if isinstance(widget, tk.Text):
                # Le curseur de saisie n'existe pas sur une Listbox.
                widget.configure(insertbackground=C["fg"])

    def afficher(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def masquer(self):
        self.frame.pack_forget()


class VuePrediction(_VueBase):
    """« Que va afficher ce programme ? » — on lit avant d'exécuter."""

    def __init__(self, parent, app):
        super().__init__(parent, app)
        f = self.frame

        self.titre = ttk.Label(f, text="", style="Title.TLabel",
                               wraplength=720, justify="left")
        self.titre.pack(anchor="w", padx=16, pady=(14, 8))

        self.code = tk.Text(f, height=8, relief="flat", wrap="none",
                            font=app.code_font, state="disabled")
        self.code.pack(fill=tk.X, padx=16)
        self._zones_texte.append((self.code, "console"))

        self.invite = ttk.Label(f, text="", style="Muted.TLabel")
        self.invite.pack(anchor="w", padx=16, pady=(10, 4))

        self.saisie = tk.Text(f, height=5, relief="flat", wrap="none",
                              font=app.code_font, undo=True)
        self.saisie.pack(fill=tk.X, padx=16)
        self._zones_texte.append((self.saisie, "saisie"))

        barre = ttk.Frame(f)
        barre.pack(anchor="w", padx=16, pady=10)
        self.bouton = ttk.Button(barre, text="", command=self.verifier,
                                 style="Primary.TButton")
        self.bouton.pack(side=tk.LEFT)

        self.retour = ttk.Label(f, text="", style="TLabel",
                                wraplength=720, justify="left")
        self.retour.pack(anchor="w", padx=16)

        self.detail = tk.Text(f, height=7, relief="flat", wrap="word",
                              font=app.code_font, state="disabled")
        self.detail.pack(fill=tk.BOTH, expand=True, padx=16, pady=(8, 12))
        self._zones_texte.append((self.detail, "console"))

        self.saisie.bind("<Control-Return>", lambda e: self.verifier())

    def _ecrire(self, widget, texte):
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert("1.0", texte)
        widget.configure(state="disabled")

    def traduire(self):
        self.titre.configure(text=self.tr("pred_titre"))
        self.invite.configure(text=self.tr("pred_saisie"))
        self.bouton.configure(text=self.tr("pred_verifier"))

    def charger(self, lecon):
        self.lecon = lecon
        self._ecrire(self.code, (lecon.get("code") or "").rstrip("\n"))
        self.saisie.delete("1.0", tk.END)
        self._ecrire(self.detail, "")
        self.retour.configure(text="")
        self.traduire()
        self.saisie.focus_set()

    def verifier(self):
        if not self.lecon:
            return
        prediction = self.saisie.get("1.0", "end-1c")
        reussi, sortie, erreur = exercices.verifier_prediction(
            self.lecon.get("code", ""), prediction,
            stdin_lines=self.lecon.get("stdin"))

        C = self.app.C
        if erreur:
            self.retour.configure(text=self.tr("pred_erreur"), foreground=C["err"])
            self._ecrire(self.detail, erreur)
            return

        if reussi:
            self.retour.configure(text=self.tr("pred_juste"), foreground=C["ok"])
            self._ecrire(self.detail,
                         self.tr("pred_reelle") + "\n" + sortie.rstrip("\n")
                         + self._explication())
            self.app.valider_item(self.lecon["id"], self.tr("banner_exo"))
        else:
            rang = exercices.premiere_difference(prediction, sortie)
            details = [self.tr("pred_tienne"), prediction.rstrip("\n") or "—",
                       "", self.tr("pred_reelle"), sortie.rstrip("\n") or "—"]
            if rang:
                details += ["", self.tr("pred_diff", n=rang)]
            self.retour.configure(text=self.tr("pred_faux"), foreground=C["err"])
            self._ecrire(self.detail, "\n".join(details))

    def _explication(self):
        texte = self.lecon.get("explanation")
        return "\n\n💡 " + texte if texte else ""


class VueOrdre(_VueBase):
    """Problème de Parsons : remettre en ordre des lignes mélangées."""

    def __init__(self, parent, app):
        super().__init__(parent, app)
        f = self.frame

        self.titre = ttk.Label(f, text="", style="Title.TLabel",
                               wraplength=720, justify="left")
        self.titre.pack(anchor="w", padx=16, pady=(14, 4))
        self.aide = ttk.Label(f, text="", style="Muted.TLabel")
        self.aide.pack(anchor="w", padx=16, pady=(0, 8))

        corps = ttk.Frame(f)
        corps.pack(fill=tk.BOTH, expand=True, padx=16)

        self.liste = tk.Listbox(corps, font=app.code_font, relief="flat",
                                activestyle="none", height=10,
                                exportselection=False)
        self.liste.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._zones_texte.append((self.liste, "console"))

        fleches = ttk.Frame(corps)
        fleches.pack(side=tk.LEFT, padx=8)
        self.monter = ttk.Button(fleches, text="", width=12,
                                 command=lambda: self._deplacer(-1))
        self.monter.pack(pady=2)
        self.descendre = ttk.Button(fleches, text="", width=12,
                                    command=lambda: self._deplacer(1))
        self.descendre.pack(pady=2)

        barre = ttk.Frame(f)
        barre.pack(anchor="w", padx=16, pady=10)
        self.bouton = ttk.Button(barre, text="", command=self.verifier,
                                 style="Primary.TButton")
        self.bouton.pack(side=tk.LEFT)

        self.retour = ttk.Label(f, text="", style="TLabel",
                                wraplength=720, justify="left")
        self.retour.pack(anchor="w", padx=16, pady=(0, 12))

        # Déplacer au clavier, plus rapide que de viser les boutons.
        self.liste.bind("<Control-Up>", lambda e: self._deplacer(-1))
        self.liste.bind("<Control-Down>", lambda e: self._deplacer(1))

    def traduire(self):
        self.titre.configure(text=self.tr("ord_titre"))
        self.aide.configure(text=self.tr("ord_aide"))
        self.monter.configure(text=self.tr("ord_monter"))
        self.descendre.configure(text=self.tr("ord_descendre"))
        self.bouton.configure(text=self.tr("ord_verifier"))

    def charger(self, lecon):
        self.lecon = lecon
        lignes = exercices.melanger(exercices.lignes_de(lecon), lecon["id"])
        self.liste.delete(0, tk.END)
        for ligne in lignes:
            self.liste.insert(tk.END, ligne)
        if lignes:
            self.liste.selection_set(0)
        self.retour.configure(text="")
        self.traduire()

    def _lignes(self):
        return list(self.liste.get(0, tk.END))

    def _deplacer(self, sens):
        selection = self.liste.curselection()
        if not selection:
            return "break"
        depart = selection[0]
        arrivee = depart + sens
        if not 0 <= arrivee < self.liste.size():
            return "break"
        lignes = self._lignes()
        lignes[depart], lignes[arrivee] = lignes[arrivee], lignes[depart]
        self.liste.delete(0, tk.END)
        for ligne in lignes:
            self.liste.insert(tk.END, ligne)
        self.liste.selection_set(arrivee)
        self.liste.see(arrivee)
        return "break"

    def verifier(self):
        if not self.lecon:
            return
        proposition = self._lignes()
        reussi, message = exercices.verifier_ordre(proposition, self.lecon)
        C = self.app.C
        if reussi:
            self.retour.configure(text=self.tr("ord_juste"), foreground=C["ok"])
            self.app.valider_item(self.lecon["id"], self.tr("banner_exo"))
            return

        rang = exercices.premiere_ligne_fautive(proposition, self.lecon)
        texte = self.tr("ord_faux")
        if rang:
            texte += "  " + self.tr("ord_indice", n=rang)
        self.retour.configure(text=texte, foreground=C["err"])
