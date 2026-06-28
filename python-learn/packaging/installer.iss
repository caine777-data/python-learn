; ============================================================================
;  PythonLearn — script d'installation Windows (Inno Setup 6)
;  Compile l'exécutable produit par PyInstaller en un installateur .exe.
;
;  Prérequis : avoir généré dist\PythonLearn.exe (voir DIFFUSION.md), puis :
;     iscc packaging\installer.iss
;  Le résultat est déposé dans : Output\PythonLearn-Setup.exe
; ============================================================================

#define MonApp "PythonLearn"
#define MaVersion "1.0.0"
#define MonAuteur "C. Monna"
#define MonExe "PythonLearn.exe"

[Setup]
AppId={{8E7B2D4A-9C31-4F6E-A1B2-PYTHONLEARN01}
AppName={#MonApp}
AppVersion={#MaVersion}
AppPublisher={#MonAuteur}
DefaultDirName={autopf}\{#MonApp}
DefaultGroupName={#MonApp}
DisableProgramGroupPage=yes
OutputDir=..\Output
OutputBaseFilename={#MonApp}-Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
; Installe pour l'utilisateur courant : pas besoin de droits administrateur.
PrivilegesRequired=lowest
ArchitecturesInstallIn64BitMode=x64compatible
; SetupIconFile=..\assets\icon.ico   ; décommenter si un .ico est fourni

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\dist\{#MonExe}"; DestDir: "{app}"; Flags: ignoreversion
; Si PyInstaller produit un dossier (--onedir), utiliser plutôt :
; Source: "..\dist\{#MonApp}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MonApp}"; Filename: "{app}\{#MonExe}"
Name: "{autodesktop}\{#MonApp}"; Filename: "{app}\{#MonExe}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MonExe}"; Description: "{cm:LaunchProgram,{#MonApp}}"; Flags: nowait postinstall skipifsilent
