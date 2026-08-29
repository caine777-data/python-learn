"""
Exécution du code de l'apprenant.

Le code est exécuté DANS le processus de l'application (et non via un
interpréteur externe), ce qui permet à l'.exe généré par PyInstaller de
fonctionner même si Python n'est pas installé sur la machine.

Une protection contre les boucles infinies est assurée en levant une
exception de façon asynchrone dans le thread d'exécution s'il dépasse
le délai imparti.
"""

import builtins as _builtins
import contextlib
import ctypes
import io
import sys
import threading
import traceback

# Modules autorisés dans le bac à sable « Brouillon » (expérimentation sûre).
SANDBOX_MODULES = {
    "math", "cmath", "random", "statistics", "decimal", "fractions",
    "datetime", "calendar", "time", "json", "re", "string", "textwrap",
    "unicodedata", "collections", "itertools", "functools", "heapq",
    "bisect", "operator", "enum", "typing", "dataclasses", "pprint",
}

# Fonctions intégrées retirées du bac à sable (accès fichier/système, eval…).
_BUILTINS_BLOQUES = {"open", "eval", "exec", "compile", "memoryview"}


def _import_garde(allow):
    reel = _builtins.__import__

    def gardien(name, *args, **kwargs):
        racine = name.split(".")[0]
        if racine not in allow:
            raise ImportError(
                f"Module « {racine} » non autorisé dans le bac à sable.")
        return reel(name, *args, **kwargs)
    return gardien


def _builtins_sandbox(allow):
    """Construit un __builtins__ restreint pour le bac à sable."""
    safe = {k: getattr(_builtins, k) for k in dir(_builtins)
            if not k.startswith("_")}
    for nom in _BUILTINS_BLOQUES:
        safe.pop(nom, None)
    safe["__import__"] = _import_garde(allow)
    safe["input"] = lambda *a, **k: ""   # pas de saisie bloquante
    return safe


class ExecutionResult:
    """Résultat brut d'une exécution de code."""

    def __init__(self, output="", error=None, timed_out=False):
        self.output = output
        self.error = error
        self.timed_out = timed_out

    @property
    def ok(self):
        return self.error is None and not self.timed_out


def _async_raise(thread_id, exctype):
    """Lève `exctype` dans le thread identifié par thread_id (CPython)."""
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread_id), ctypes.py_object(exctype)
    )
    if res > 1:
        # On a touché plusieurs threads : on annule.
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)


# Exécutions qui n'ont pas pu être arrêtées (voir _interrompre). On les
# garde pour pouvoir en avertir l'apprenant : un thread qui tourne encore
# en arrière-plan explique une application soudain lente.
_zombies = []


def zombies_actifs():
    """Nombre d'exécutions précédentes qui tournent encore en arrière-plan."""
    _zombies[:] = [t for t in _zombies if t.is_alive()]
    return len(_zombies)


def _interrompre(thread, tentatives=6, pause=0.25):
    """Tente d'arrêter un thread d'exécution, avec insistance.

    Une seule injection ne suffit pas toujours : le code de l'apprenant peut
    attraper l'exception, et gérer les exceptions est justement au programme.
    On réessaie donc plusieurs fois, en alternant KeyboardInterrupt et
    SystemExit — aucune des deux n'est arrêtée par un « except Exception ».

    Limite assumée : un « except: » nu (ou « except BaseException »)
    à l'intérieur d'une boucle infinie avale tout, y compris ceci. Seul
    l'arrêt du processus en viendrait à bout, et exécuter chaque exercice
    dans un processus séparé coûterait plusieurs secondes de démarrage à
    chaque « Exécuter » — le remède serait pire que le mal. Ces cas sont
    donc recensés dans _zombies et signalés à l'apprenant.

    Renvoie True si le thread s'est bien arrêté.
    """
    for essai in range(tentatives):
        if not thread.is_alive():
            return True
        _async_raise(thread.ident,
                     SystemExit if essai % 2 else KeyboardInterrupt)
        thread.join(pause)
    return not thread.is_alive()


def run_code(code, namespace=None, timeout=6.0, safe=False, allow=None):
    """
    Exécute `code` et capture sa sortie standard.

    Si `safe=True`, le code s'exécute dans un bac à sable restreint :
    seuls les modules de `allow` (par défaut SANDBOX_MODULES) sont
    importables, et les fonctions d'accès fichier/système sont retirées.

    Retourne (ExecutionResult, namespace) — le namespace contient les
    variables/fonctions définies par le code (utile pour les vérifications).
    """
    if namespace is None:
        namespace = {}
    namespace.setdefault("__name__", "__main__")
    if safe:
        namespace["__builtins__"] = _builtins_sandbox(allow or SANDBOX_MODULES)

    buffer = io.StringIO()
    holder = {"error": None}

    def target():
        try:
            compiled = compile(code, "<exercice>", "exec")
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
                exec(compiled, namespace)
        except BaseException as exc:  # noqa: BLE001  (on capture aussi notre interruption)
            holder["error"] = exc

    # On note la sortie standard AVANT de lancer le thread : contextlib
    # la détourne globalement, et un thread qui ne meurt jamais ne ressort
    # jamais de son bloc « with » — la sortie resterait alors détournée vers
    # son tampon pour le programme entier, qui deviendrait muet.
    sortie_avant, erreur_avant = sys.stdout, sys.stderr

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(timeout)

    timed_out = False
    if thread.is_alive():
        timed_out = True
        if not _interrompre(thread):
            _zombies.append(thread)
            sys.stdout, sys.stderr = sortie_avant, erreur_avant

    error_text = None
    if timed_out:
        # Préfixé comme une vraie exception Python : c'est ce qui permet
        # à errors.expliquer() de reconnaître le cas, dans les deux langues.
        error_text = ("TimeoutError: exécution interrompue, le programme a "
                      "tourné trop longtemps (boucle infinie ?).")
    elif holder["error"] is not None:
        exc = holder["error"]
        error_text = "".join(
            traceback.format_exception_only(type(exc), exc)
        ).strip()

    return (
        ExecutionResult(output=buffer.getvalue(), error=error_text, timed_out=timed_out),
        namespace,
    )


_TYPES_AFFICHABLES = (int, float, str, bool, list, dict, tuple, set,
                      frozenset, bytes, type(None))


def inspecter(namespace, limite=200):
    """
    Extrait les variables « simples » d'un espace de noms, pour les
    montrer à l'apprenant après exécution (int, listes, dicts...).

    Renvoie une liste de couples (nom, représentation).
    """
    out = []
    for nom, val in namespace.items():
        if nom.startswith("__") or nom == "input":
            continue
        if not isinstance(val, _TYPES_AFFICHABLES):
            continue
        try:
            rep = repr(val)
        except Exception:
            continue
        if len(rep) > limite:
            rep = rep[:limite - 1] + "…"
        out.append((nom, rep))
    return out


def run_exercise(user_code, check_code=None, expected_output=None,
                 stdin_lines=None, timeout=6.0):
    """
    Exécute le code de l'apprenant puis valide l'exercice.

    Retourne (ExecutionResult, reussi: bool, message: str).
    Trois modes de validation (cumulables) :
      - expected_output : la sortie texte doit correspondre exactement ;
      - check_code      : du code de test exécuté ensuite (assert ...) ;
      - aucun           : on se contente d'exécuter (mode bac à sable).
    """
    namespace = {}

    # Si l'exercice utilise input(), on simule l'entrée clavier.
    if stdin_lines is not None:
        feed = iter(stdin_lines)
        namespace["input"] = lambda prompt="": next(feed, "")

    result, namespace = run_code(user_code, namespace, timeout)

    if not result.ok:
        return result, False, result.error or "Une erreur est survenue."

    if expected_output is not None:
        if result.output.strip() == str(expected_output).strip():
            return result, True, "Sortie correcte, bien joué !"
        return (
            result,
            False,
            "La sortie ne correspond pas encore à ce qui est attendu.",
        )

    if check_code:
        check_result, _ = run_code(check_code, namespace, timeout)
        if check_result.ok:
            return result, True, "Bravo, tous les tests passent !"
        return result, False, check_result.error or "Un test a échoué."

    return result, True, "Code exécuté."


def tracer(code, stdin_lines=None, max_steps=2000):
    """
    Exécute le code en enregistrant, à chaque ligne, le numéro de ligne,
    l'état des variables simples et la sortie produite jusque-là.

    Renvoie (etapes, erreur). Chaque étape est un dict :
        {"ligne": int|None, "vars": [(nom, repr), ...], "sortie": str}
    """
    try:
        compiled = compile(code, "<pasapas>", "exec")
    except SyntaxError as e:
        return [], "Erreur de syntaxe : " + (e.msg or str(e))

    etapes = []
    buffer = io.StringIO()
    ns = {"__name__": "__main__"}
    if stdin_lines is not None:
        feed = iter(stdin_lines)
        ns["input"] = lambda prompt="": next(feed, "")
    else:
        ns["input"] = lambda prompt="": ""
    depasse = {"v": False}

    def trace(frame, event, arg):
        if frame.f_code.co_filename != "<pasapas>":
            return trace
        if event == "line":
            if len(etapes) >= max_steps:
                depasse["v"] = True
                raise KeyboardInterrupt
            variables = inspecter({**frame.f_globals, **frame.f_locals})
            etapes.append({"ligne": frame.f_lineno, "vars": variables,
                           "sortie": buffer.getvalue()})
        return trace

    erreur = None
    ancien = sys.gettrace()
    try:
        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
            sys.settrace(trace)
            exec(compiled, ns)
    except KeyboardInterrupt:
        pass
    except BaseException as exc:  # noqa: BLE001
        erreur = "".join(traceback.format_exception_only(type(exc), exc)).strip()
    finally:
        sys.settrace(ancien)

    # état final (après la dernière ligne)
    etapes.append({"ligne": None, "vars": inspecter(ns),
                   "sortie": buffer.getvalue()})
    if depasse["v"]:
        erreur = (erreur + " " if erreur else "") + "(arrêt : trop d'étapes)"
    return etapes, erreur
