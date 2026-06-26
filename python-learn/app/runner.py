"""
Exécution du code de l'apprenant.

Le code est exécuté DANS le processus de l'application (et non via un
interpréteur externe), ce qui permet à l'.exe généré par PyInstaller de
fonctionner même si Python n'est pas installé sur la machine.

Une protection contre les boucles infinies est assurée en levant une
exception de façon asynchrone dans le thread d'exécution s'il dépasse
le délai imparti.
"""

import ctypes
import threading
import io
import contextlib
import traceback


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


def run_code(code, namespace=None, timeout=6.0):
    """
    Exécute `code` et capture sa sortie standard.

    Retourne (ExecutionResult, namespace) — le namespace contient les
    variables/fonctions définies par le code (utile pour les vérifications).
    """
    if namespace is None:
        namespace = {}
    namespace.setdefault("__name__", "__main__")

    buffer = io.StringIO()
    holder = {"error": None}

    def target():
        try:
            compiled = compile(code, "<exercice>", "exec")
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
                exec(compiled, namespace)
        except BaseException as exc:  # noqa: BLE001  (on capture aussi notre interruption)
            holder["error"] = exc

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(timeout)

    timed_out = False
    if thread.is_alive():
        _async_raise(thread.ident, KeyboardInterrupt)
        thread.join(1.0)
        timed_out = True

    error_text = None
    if timed_out:
        error_text = "Exécution interrompue : trop longue (boucle infinie ?)."
    elif holder["error"] is not None:
        exc = holder["error"]
        error_text = "".join(
            traceback.format_exception_only(type(exc), exc)
        ).strip()

    return (
        ExecutionResult(output=buffer.getvalue(), error=error_text, timed_out=timed_out),
        namespace,
    )


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
