"""
Logique « motivation » (sans dépendance à l'interface, donc testable) :
séries de jours (streak), répétition espacée (SRS) et certificat HTML.
"""

import datetime

# Intervalles de révision (en jours), de plus en plus espacés.
INTERVALLES = [1, 3, 7, 16, 35, 90]

# Points d'expérience.
XP_PAR_ITEM = 10      # chaque exercice/quiz réussi
XP_PAR_BADGE = 50     # chaque parcours terminé
XP_PAR_NIVEAU = 100   # paliers réguliers


def xp_total(completed, badges):
    """Expérience accumulée : items réussis + bonus de badges."""
    return XP_PAR_ITEM * len(completed) + XP_PAR_BADGE * len(badges)


def niveau(xp):
    """Traduit l'XP en (niveau, progression dans le niveau, palier).

    Niveau 1 dès 0 XP ; chaque niveau demande XP_PAR_NIVEAU points.
    """
    niv = xp // XP_PAR_NIVEAU + 1
    dans = xp % XP_PAR_NIVEAU
    return {"niveau": niv, "dans_niveau": dans, "pour_suivant": XP_PAR_NIVEAU, "xp": xp}


def cette_semaine(historique, today):
    """Nombre d'activités depuis lundi de la semaine en cours (inclus)."""
    lundi = today - datetime.timedelta(days=today.weekday())
    total = 0
    for d, c in historique.items():
        try:
            jour = datetime.date.fromisoformat(d)
        except ValueError:
            continue
        if lundi <= jour <= today:
            total += c
    return total


def prochaine_action(ordre_ids, completed, ids_dus):
    """Recommande quoi faire ensuite.

    - s'il y a des révisions dues  -> ("revision", id)
    - sinon la première leçon non faite -> ("nouvelle", id)
    - sinon tout est terminé -> ("termine", None)
    `ordre_ids` est la liste de tous les item_ids dans l'ordre du curriculum.
    """
    faits = set(completed)
    dus_a_faire = [i for i in ids_dus if i in set(ordre_ids)]
    if dus_a_faire:
        return ("revision", dus_a_faire[0])
    for item_id in ordre_ids:
        if item_id not in faits:
            return ("nouvelle", item_id)
    return ("termine", None)



# --------------------------------------------------------------- séries (streak)
def streak(historique, today):
    """Nombre de jours consécutifs d'activité se terminant aujourd'hui (ou hier)."""
    jour = today
    if historique.get(jour.isoformat(), 0) == 0:
        jour = jour - datetime.timedelta(days=1)
    s = 0
    while historique.get(jour.isoformat(), 0) > 0:
        s += 1
        jour -= datetime.timedelta(days=1)
    return s


def meilleur_streak(historique):
    jours = sorted(datetime.date.fromisoformat(d)
                   for d, c in historique.items() if c > 0)
    if not jours:
        return 0
    best = cur = 1
    for i in range(1, len(jours)):
        if (jours[i] - jours[i - 1]).days == 1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best


def sept_jours(historique, today, n=7):
    """Liste (label JJ/MM, nombre) pour les n derniers jours (ancien→récent)."""
    out = []
    for k in range(n - 1, -1, -1):
        d = today - datetime.timedelta(days=k)
        out.append((d.strftime("%d/%m"), historique.get(d.isoformat(), 0)))
    return out


# ------------------------------------------------------- répétition espacée (SRS)
def prochain_intervalle(courant):
    for v in INTERVALLES:
        if v > courant:
            return v
    return INTERVALLES[-1]


def planifier(srs, item_id, today, reussi=True):
    """Programme la prochaine révision d'un item (avance si réussi, sinon repart à 1)."""
    courant = srs.get(item_id, {}).get("interval", 0)
    inter = prochain_intervalle(courant) if reussi else 1
    srs[item_id] = {
        "interval": inter,
        "due": (today + datetime.timedelta(days=inter)).isoformat(),
    }
    return srs[item_id]


def dus(srs, today, completed):
    """Items dont la révision est due (et qui sont bien terminés)."""
    iso = today.isoformat()
    return [iid for iid, e in srs.items()
            if iid in completed and e.get("due", "") <= iso]


# ----------------------------------------------------------------- certificat
def certificat_html(nom, parcours, date_str):
    """Renvoie le HTML d'un certificat imprimable (autonome, sans dépendance)."""
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Certificat — {parcours}</title>
<style>
  body {{ font-family: Georgia, 'Times New Roman', serif; background:#f0f2f5;
         display:flex; justify-content:center; padding:40px; }}
  .cert {{ background:#fff; width:760px; padding:60px; text-align:center;
          border:12px solid #4d8bf0; border-radius:8px;
          box-shadow:0 8px 30px rgba(0,0,0,.15); }}
  .cert h1 {{ font-size:40px; color:#27406b; margin:0 0 6px; letter-spacing:2px; }}
  .sub {{ color:#7a8190; text-transform:uppercase; letter-spacing:4px; font-size:13px; }}
  .nom {{ font-size:34px; color:#1c1d22; margin:34px 0 6px; }}
  .ligne {{ width:300px; border-bottom:1px solid #cdd2db; margin:0 auto 20px; }}
  .parcours {{ font-size:22px; color:#4d8bf0; margin:10px 0 30px; }}
  .pied {{ display:flex; justify-content:space-between; margin-top:40px;
           color:#7a8190; font-size:14px; }}
  .badge {{ font-size:54px; }}
</style></head>
<body><div class="cert">
  <div class="badge">🏅</div>
  <h1>Certificat de réussite</h1>
  <div class="sub">PythonLearn</div>
  <div class="nom">{nom}</div>
  <div class="ligne"></div>
  <p>a terminé avec succès le parcours</p>
  <div class="parcours">{parcours}</div>
  <div class="pied"><span>PythonLearn 🐍</span><span>{date_str}</span></div>
</div>
<script>window.onload = () => {{ /* imprimable via Ctrl+P */ }};</script>
</body></html>"""


def cheatsheet_html(titre, sections):
    """Antisèche imprimable (HTML autonome) à partir de sections.

    `sections` = liste de (titre_section, [(code, explication), ...]).
    """
    import html as _html

    blocs = []
    for nom_section, lignes in sections:
        items = "\n".join(
            f'      <tr><td class="code">{_html.escape(code)}</td>'
            f'<td class="desc">{_html.escape(desc)}</td></tr>'
            for code, desc in lignes
        )
        blocs.append(
            f'  <section>\n    <h2>{_html.escape(nom_section)}</h2>\n'
            f'    <table>\n{items}\n    </table>\n  </section>'
        )
    corps = "\n".join(blocs)
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>{_html.escape(titre)}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif;
         margin: 24px; color: #1a1a2e; background: #f6f7fb; }}
  h1 {{ text-align: center; color: #5b4bdb; margin: 0 0 4px; }}
  .sub {{ text-align: center; color: #777; margin: 0 0 20px; font-size: 14px; }}
  .grid {{ column-count: 2; column-gap: 20px; }}
  @media (max-width: 760px) {{ .grid {{ column-count: 1; }} }}
  section {{ break-inside: avoid; background: #fff; border: 1px solid #e4e4f0;
            border-radius: 10px; padding: 10px 14px; margin: 0 0 16px; }}
  h2 {{ font-size: 15px; color: #5b4bdb; margin: 0 0 8px;
       border-bottom: 2px solid #eceaff; padding-bottom: 4px; }}
  table {{ width: 100%; border-collapse: collapse; }}
  td {{ padding: 3px 4px; vertical-align: top; font-size: 13px; }}
  .code {{ font-family: Consolas, Menlo, monospace; color: #1a1a2e;
          white-space: nowrap; }}
  .desc {{ color: #666; text-align: right; }}
  .pied {{ text-align: center; color: #999; font-size: 12px; margin-top: 8px; }}
  @media print {{ body {{ background: #fff; margin: 0; }}
                 section {{ border-color: #ccc; }} }}
</style></head><body>
  <h1>🐍 {_html.escape(titre)}</h1>
  <p class="sub">PythonLearn — mémo imprimable (Ctrl+P)</p>
  <div class="grid">
{corps}
  </div>
  <p class="pied">PythonLearn 🐍 — la syntaxe essentielle</p>
</body></html>"""
