"""
Palettes de couleurs de l'interface, et petits calculs sur les teintes.

Trois thèmes sont proposés : sombre, clair et contraste élevé — ce
dernier existe pour les personnes qui distinguent mal les nuances, et
ne doit donc jamais être traité comme une simple variante décorative.

Chaque thème donne une couleur à un ROLE (fond, texte, accent, erreur…)
et non à un élément précis : c'est ce qui permet d'en ajouter un
quatrième sans toucher au reste de l'application.
"""

THEMES = {
    "dark": {
        "label": "sombre", "label_en": "dark",
        "bg": "#1e1f26", "panel": "#272935", "editor": "#15161c",
        "console": "#0e0f14", "fg": "#e6e6e6", "accent": "#4d8bf0",
        "ok": "#52c97a", "err": "#f0635c", "muted": "#9aa0b4",
        "heading": "#7fb0ff", "code": "#ffd479", "code_bg": "#15161c",
        "sel_fg": "#ffffff", "curline": "#23252f",
        "kw": "#c792ea", "builtin": "#82aaff", "num": "#f78c6c",
        "deff": "#ffcb6b", "str": "#c3e88d", "com": "#637777",
    },
    "light": {
        "label": "clair", "label_en": "light",
        "bg": "#f4f5f7", "panel": "#e7e9ee", "editor": "#ffffff",
        "console": "#eef0f4", "fg": "#1c1d22", "accent": "#2f6fe0",
        "ok": "#1f9d57", "err": "#d23b34", "muted": "#5a6172",
        "heading": "#1e4fa3", "code": "#9a6b00", "code_bg": "#eceef2",
        "sel_fg": "#ffffff", "curline": "#eaf0fb",
        "kw": "#8a2fb8", "builtin": "#2f6fe0", "num": "#b5530a",
        "deff": "#9a6b00", "str": "#2e8b3d", "com": "#8a93a3",
    },
    "contrast": {
        "label": "contraste élevé", "label_en": "high contrast",
        "bg": "#000000", "panel": "#0c0c0c", "editor": "#000000",
        "console": "#000000", "fg": "#ffffff", "accent": "#ffd400",
        "ok": "#42ff7a", "err": "#ff5b5b", "muted": "#cccccc",
        "heading": "#ffd400", "code": "#ffd400", "code_bg": "#0c0c0c",
        "sel_fg": "#000000", "curline": "#181818",
        "kw": "#ff9cf0", "builtin": "#7fd4ff", "num": "#ffb86b",
        "deff": "#ffd400", "str": "#8dff8d", "com": "#bbbbbb",
    },
}
THEME_ORDER = ["dark", "light", "contrast"]


def melange(hex1, hex2, t):
    """Mélange deux couleurs #rrggbb (t=0 -> hex1, t=1 -> hex2)."""
    def comp(h):
        h = h.lstrip("#")
        return [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    a, b = comp(hex1), comp(hex2)
    m = [round(a[i] + (b[i] - a[i]) * t) for i in range(3)]
    return "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, v)) for v in m))


def eclaircir(hexc, t=0.12):
    return melange(hexc, "#ffffff", t)


def assombrir(hexc, t=0.15):
    return melange(hexc, "#000000", t)
