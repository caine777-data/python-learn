"""
Logique « motivation » (sans dépendance à l'interface, donc testable) :
séries de jours (streak), répétition espacée (SRS) et certificat HTML.
"""

import datetime

# Intervalles de révision (en jours), de plus en plus espacés.
INTERVALLES = [1, 3, 7, 16, 35, 90]


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
