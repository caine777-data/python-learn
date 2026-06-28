# Diffuser PythonLearn

Ce guide explique comment transformer le code en exécutables téléchargeables
et les publier proprement. L'application reste **sans dépendance** pour
l'utilisateur final : tout est embarqué dans l'exécutable.

---

## 1. Construire l'exécutable (PyInstaller)

En local, depuis la racine du projet :

```bash
pip install -r requirements-dev.txt        # installe pyinstaller
pyinstaller --onefile --windowed --name PythonLearn main.py
```

- `--onefile` : un seul `.exe` (plus simple à distribuer).
- `--windowed` : pas de console noire au lancement.
- Le résultat est dans `dist/PythonLearn.exe` (ou `dist/PythonLearn` sur macOS/Linux).

Pour embarquer une icône : ajouter `--icon assets/icon.ico` (Windows) ou
`--icon assets/icon.icns` (macOS).

> La génération multi-plateforme est déjà automatisée : voir
> `.github/workflows/build.yml`, qui produit les exécutables Windows, macOS et
> Linux à chaque tag `v*`.

---

## 2. Installateur Windows (Inno Setup)

Un simple `.exe` suffit, mais un **installateur** fait plus professionnel
(raccourcis menu Démarrer + Bureau, désinstallation propre).

1. Installer [Inno Setup 6](https://jrsoftware.org/isdl.php) (gratuit).
2. Générer d'abord `dist\PythonLearn.exe` (étape 1).
3. Compiler l'installateur :

```bat
iscc packaging\installer.iss
```

Le résultat est déposé dans `Output\PythonLearn-Setup.exe`. Le script
installe **sans droits administrateur** (`PrivilegesRequired=lowest`).

---

## 3. Publier sur GitHub Releases

1. Taguer une version : `git tag v1.0.0 && git push origin v1.0.0`.
   → le workflow `build.yml` construit les exécutables.
2. Sur GitHub : **Releases → Draft a new release**, choisir le tag.
3. Joindre les fichiers : `PythonLearn.exe`, `PythonLearn-Setup.exe`,
   les binaires macOS / Linux.
4. Rédiger les notes de version (nouveautés) et publier.

On peut aussi laisser le workflow attacher automatiquement les artefacts à la
Release (action `softprops/action-gh-release`).

---

## 4. Signature & avertissement SmartScreen (Windows)

Un exécutable **non signé** déclenche l'écran bleu *« Windows a protégé votre
ordinateur »* (SmartScreen). C'est normal et sans danger, mais ça inquiète les
utilisateurs. Trois options, de la plus simple à la plus pro :

- **Ne rien signer** : indiquer aux utilisateurs de cliquer sur
  *« Informations complémentaires » → « Exécuter quand même »*. Acceptable pour
  un projet personnel/open-source.
- **Certificat de signature de code** (OV, ~70-150 €/an) : signe le binaire,
  mais la réputation SmartScreen se construit progressivement.
- **Certificat EV** (plus cher) : réputation immédiate, plus d'alerte.

Signer (si tu as un certificat `.pfx`) :

```bat
signtool sign /f certificat.pfx /p MOT_DE_PASSE /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\PythonLearn.exe
```

> La signature **n'est pas obligatoire** pour distribuer : l'app fonctionne
> parfaitement, c'est uniquement une question de confiance affichée.

---

## 5. macOS (optionnel)

```bash
pip install create-dmg            # ou: brew install create-dmg
pyinstaller --onefile --windowed --name PythonLearn main.py
create-dmg dist/PythonLearn.app   # produit un .dmg distribuable
```

Comme sous Windows, un binaire non notarisé affiche un avertissement
Gatekeeper ; l'utilisateur l'ouvre via *clic droit → Ouvrir*. La notarisation
(compte développeur Apple) supprime l'avertissement.
