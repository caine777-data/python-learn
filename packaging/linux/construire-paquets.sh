#!/usr/bin/env bash
# ============================================================================
#  Construit les deux formats d'installation Linux à partir du binaire
#  produit par PyInstaller (dist/PythonLearn) :
#
#    1. un paquet .deb        -> installation système (Debian, Ubuntu, Mint…)
#    2. une archive .tar.gz   -> installation sans droits root, toutes distros
#
#  Usage, depuis la racine du projet (python-learn/) :
#      bash packaging/linux/construire-paquets.sh 1.2.3
#
#  Les fichiers finis sont déposés dans dist/.
# ============================================================================
set -euo pipefail

VERSION="${1:?usage: construire-paquets.sh <version>}"
NOM="python-learn"
BINAIRE="dist/PythonLearn"
ARCH="$(dpkg --print-architecture 2>/dev/null || echo amd64)"

if [ ! -x "$BINAIRE" ]; then
    echo "Binaire introuvable : $BINAIRE (lancer PyInstaller d'abord)" >&2
    exit 1
fi

racine="$(pwd)"
travail="$(mktemp -d)"
trap 'rm -rf "$travail"' EXIT

# ---------------------------------------------------------------- paquet .deb
# Arborescence : le binaire va dans /usr/lib/python-learn/ et un lien dans
# /usr/bin/ le rend appelable depuis n'importe où.
deb="$travail/deb"
mkdir -p "$deb/DEBIAN" \
         "$deb/usr/lib/$NOM" \
         "$deb/usr/bin" \
         "$deb/usr/share/applications" \
         "$deb/usr/share/icons/hicolor/256x256/apps" \
         "$deb/usr/share/doc/$NOM"

install -m 755 "$BINAIRE" "$deb/usr/lib/$NOM/PythonLearn"
ln -s "/usr/lib/$NOM/PythonLearn" "$deb/usr/bin/$NOM"
install -m 644 packaging/linux/$NOM.desktop "$deb/usr/share/applications/$NOM.desktop"
install -m 644 assets/icon.png "$deb/usr/share/icons/hicolor/256x256/apps/$NOM.png"
install -m 644 LICENSE "$deb/usr/share/doc/$NOM/copyright"

# Le binaire PyInstaller embarque Python et Tcl/Tk : aucune dépendance à
# déclarer au-delà de la libc, ce qui rend le paquet installable partout.
cat > "$deb/DEBIAN/control" <<CONTROL
Package: $NOM
Version: $VERSION
Section: education
Priority: optional
Architecture: $ARCH
Maintainer: C. Monna <cedricmonna@gmail.com>
Homepage: https://github.com/cedricmonna/python-learn
Description: Apprendre Python pas à pas, du débutant à l'expert
 PythonLearn est une application de bureau qui enseigne Python à travers
 15 parcours et 132 exercices corrigés automatiquement. Chaque leçon
 associe une explication et un exercice résolu dans un éditeur intégré :
 le code s'exécute réellement et la réussite est vérifiée.
 .
 L'application fonctionne hors ligne et n'a besoin d'aucune installation
 de Python : tout est embarqué dans l'exécutable.
CONTROL

dpkg-deb --build --root-owner-group "$deb" "$racine/dist/${NOM}_${VERSION}_${ARCH}.deb"

# ------------------------------------------------------------- archive .tar.gz
# Pour les distributions non-Debian : un dossier autonome avec un script
# d'installation qui ne demande pas les droits administrateur.
tgz="$travail/${NOM}-${VERSION}"
mkdir -p "$tgz"
install -m 755 "$BINAIRE" "$tgz/PythonLearn"
install -m 644 packaging/linux/$NOM.desktop "$tgz/$NOM.desktop"
install -m 644 assets/icon.png "$tgz/$NOM.png"
install -m 644 LICENSE "$tgz/LICENSE"
install -m 644 README.md "$tgz/README.md"

cat > "$tgz/installer.sh" <<'INSTALL'
#!/usr/bin/env bash
# Installe PythonLearn pour l'utilisateur courant (aucun droit root requis).
# Pour désinstaller : bash installer.sh --desinstaller
set -euo pipefail

ici="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bin="$HOME/.local/bin"
apps="$HOME/.local/share/applications"
icones="$HOME/.local/share/icons/hicolor/256x256/apps"

if [ "${1:-}" = "--desinstaller" ]; then
    rm -f "$bin/python-learn" "$apps/python-learn.desktop" "$icones/python-learn.png"
    echo "PythonLearn a été retiré. Ta progression (~/.python-learn) est conservée."
    exit 0
fi

mkdir -p "$bin" "$apps" "$icones"
install -m 755 "$ici/PythonLearn" "$bin/python-learn"
install -m 644 "$ici/python-learn.png" "$icones/python-learn.png"
install -m 644 "$ici/python-learn.desktop" "$apps/python-learn.desktop"
command -v update-desktop-database >/dev/null 2>&1 && \
    update-desktop-database "$apps" 2>/dev/null || true

echo "PythonLearn est installé."
case ":$PATH:" in
    *":$bin:"*) echo "Lance-le avec : python-learn" ;;
    *) echo "Ajoute $bin à ton PATH, ou lance directement : $bin/python-learn" ;;
esac
INSTALL
chmod 755 "$tgz/installer.sh"

tar -czf "$racine/dist/${NOM}-${VERSION}-linux-${ARCH}.tar.gz" -C "$travail" "${NOM}-${VERSION}"

echo "Paquets construits :"
ls -lh "$racine/dist/"*.deb "$racine/dist/"*.tar.gz
